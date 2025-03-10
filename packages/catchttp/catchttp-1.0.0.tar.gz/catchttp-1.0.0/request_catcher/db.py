import sqlite3
from datetime import datetime
import json
from typing import Dict, Any
import threading

class DatabaseManager:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self, db_path: str = "requests.db"):
        self.db_path = db_path
        self._init_db()
    
    @classmethod
    def get_instance(cls, db_path: str = "requests.db") -> 'DatabaseManager':
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls(db_path)
        return cls._instance
    
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    url TEXT NOT NULL,
                    method TEXT NOT NULL,
                    headers TEXT NOT NULL,
                    params TEXT,
                    body TEXT,
                    response_status INTEGER,
                    response_body TEXT,
                    response_headers TEXT,
                    duration_ms REAL,
                    source TEXT
                )
            """)
            conn.commit()
    
    def log_request(self, 
                   url: str,
                   method: str,
                   headers: Dict[str, str],
                   params: Dict[str, Any] = None,
                   body: Any = None,
                   response_status: int = None,
                   response_body: Any = None,
                   response_headers: Dict[str, str] = None,
                   duration_ms: float = None,
                   source: str = None):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO requests (
                    timestamp, url, method, headers, params, body,
                    response_status, response_body, response_headers,
                    duration_ms, source
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                datetime.utcnow().isoformat(),
                url,
                method,
                json.dumps(headers),
                json.dumps(params) if params else None,
                json.dumps(body) if body else None,
                response_status,
                json.dumps(response_body) if response_body else None,
                json.dumps(response_headers) if response_headers else None,
                duration_ms,
                source
            ))
            conn.commit()
    
    def get_requests(self, limit: int = 100, offset: int = 0):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT * FROM requests 
                ORDER BY timestamp DESC 
                LIMIT ? OFFSET ?
            """, (limit, offset))
            return [dict(row) for row in cursor.fetchall()]
    
    def get_request_by_id(self, request_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM requests WHERE id = ?", (request_id,))
            row = cursor.fetchone()
            return dict(row) if row else None 