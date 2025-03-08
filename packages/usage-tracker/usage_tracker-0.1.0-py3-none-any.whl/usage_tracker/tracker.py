import os
import uuid
import json
from datetime import datetime
import threading
import queue
import time
import pymysql

def get_connection(user, password, host):
    """
    Create and return a pymysql connection using provided credentials.
    """
    conn = pymysql.connect(
        host=host, 
        user=user,
        password=password,
        database="llm_usage",
        port=3306  # default MySQL port
    )
    return conn


class UsageTracker:
    def __init__(self, db_username, db_password, db_host):
        """
        Initialize the usage tracker with a MySQL database.
        We store the credentials for use in creating a new connection per operation.
        Also, we create the table using a temporary connection.
        """
        self.db_username = db_username
        self.db_password = db_password
        self.db_host = db_host
        
        # Create table using a temporary connection.
        conn = get_connection(db_username, db_password, db_host)
        self._create_table(conn)
        conn.close()

    def _create_table(self, conn):
        """
        Create the usage table if it doesn't exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS usage_data (
            unique_id VARCHAR(36) PRIMARY KEY,
            service_name VARCHAR(255) NOT NULL,
            tags TEXT,
            input_token INT,
            output_token INT,
            timestamp DATETIME
        );
        """
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()

    def record_usage(
        self, 
        service_name: str, 
        tags: list, 
        input_token: int, 
        output_token: int, 
        timestamp: str = None
    ):
        """
        Insert a usage record into the database using a new connection.
        """
        if timestamp is None:
            # Format the timestamp as MySQL DATETIME
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        unique_id = str(uuid.uuid4())
        tags_json = json.dumps(tags)
        query = """
        INSERT INTO usage_data (unique_id, service_name, tags, input_token, output_token, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        # Create a new connection for this operation
        conn = get_connection(self.db_username, self.db_password, self.db_host)
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (unique_id, service_name, tags_json, input_token, output_token, timestamp))
            conn.commit()
        finally:
            conn.close()

    def get_all_records(self):
        """
        Fetch all records from the usage table.
        Returns:
            A list of dictionaries, where each dictionary represents a row.
        """
        conn = get_connection(self.db_username, self.db_password, self.db_host)
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM usage_data;")
                records = cursor.fetchall()
        finally:
            conn.close()
        return records

    def close(self):
        """
        In this design, each operation manages its own connection,
        so there is nothing to close at the tracker level.
        """
        pass


class AsyncUsageTracker:
    """
    A usage tracker that offloads the actual database writes to a background thread.
    """
    def __init__(self, db_username, db_password, db_host):
        self.tracker = UsageTracker(db_username, db_password, db_host)
        self.queue = queue.Queue()
        self._stop_event = threading.Event()
        self.worker_thread = threading.Thread(target=self._process_queue)
        self.worker_thread.daemon = True  # Daemonize so it won't block app exit
        self.worker_thread.start()

    def _process_queue(self):
        while not self._stop_event.is_set():
            try:
                # Wait up to 1 second for an event
                event = self.queue.get(timeout=1)
                self.tracker.record_usage(**event)
                self.queue.task_done()
            except queue.Empty:
                continue

    def record_usage(
        self, 
        service_name: str, 
        tags: list, 
        input_token: int, 
        output_token: int, 
        timestamp: str = None
    ):
        """
        Instead of writing directly to the DB, add the event to a queue.
        """
        event = {
            "service_name": service_name,
            "tags": tags,
            "input_token": input_token,
            "output_token": output_token,
            "timestamp": timestamp,
        }
        self.queue.put(event)

    def stop(self):
        """
        Stop the background worker.
        """
        self.queue.join()
        self._stop_event.set()
        self.worker_thread.join()
        self.tracker.close()

    def get_all_records(self):
        """
        Fetch all records from the usage table.
        Returns:
            A list of dictionaries representing each row.
        """
        return self.tracker.get_all_records()
