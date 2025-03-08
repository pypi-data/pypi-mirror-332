# MIT License
#
# Copyright (c) 2025 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import uuid
import sqlite3
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta


class State:
    """A Class to Manage the System State."""

    def __init__(self, path: str):
        """Initialize the database with a file path.

        Args:
            path (str): Path to the SQLite database file.
        """
        self._path = path
        self._connection = None

    def connect(self) -> int:
        """Establish a connection to the SQLite database.

        Returns:
            int: The number of total changes to the database.
        """
        self._connection = sqlite3.connect(self._path)
        return self._connection.total_changes

    def migrate(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self._connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS backup (id TEXT, dbIdent TEXT, meta TEXT, lastStatus TEXT, lastBackupAt TEXT, createdAt TEXT, updatedAt TEXT)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS log (id TEXT, record TEXT, type TEXT, meta TEXT, createdAt TEXT, updatedAt TEXT)"
        )

        cursor.close()
        self._connection.commit()

    def insert_backup(self, backup: Dict[str, Any]) -> int:
        """Insert a new backup item

        Args:
            backup (Dict): The backup data

        Returns:
            The total rows inserted
        """
        cursor = self._connection.cursor()

        result = cursor.execute(
            "INSERT INTO backup VALUES (?, ?, ?, ?, datetime('now'), datetime('now'), datetime('now'))",
            (
                backup.get("id", str(uuid.uuid4())),
                backup.get("dbIdent"),
                backup.get("meta", "{}"),
                backup.get("lastStatus"),
            ),
        )

        cursor.close()

        self._connection.commit()

        return result.rowcount

    def insert_log(self, log: Dict[str, Any]) -> int:
        """Insert a new log record

        Args:
            log (Dict): The log data

        Returns:
            The total rows inserted
        """
        cursor = self._connection.cursor()

        result = cursor.execute(
            "INSERT INTO log VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))",
            (
                log.get("id", str(uuid.uuid4())),
                log.get("record"),
                log.get("type"),
                log.get("meta", "{}"),
            ),
        )

        cursor.close()

        self._connection.commit()

        return result.rowcount

    def delete_backup(self, id: str) -> None:
        """Delete a backup by its ID.

        Args:
            id (str): The ID of the backup to delete.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM backup WHERE id = ?", (id,))
        cursor.close()
        self._connection.commit()

    def delete_log(self, id: str) -> None:
        """Delete a log by its ID.

        Args:
            id (str): The ID of the log to delete.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM log WHERE id = ?", (id,))
        cursor.close()
        self._connection.commit()

    def get_backup_by_id(self, id: str) -> Dict[str, Any]:
        """Retrieve a backup by its ID.

        Args:
            id (str): The ID of the backup to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the backup details.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM backup WHERE id = ?", (id,))
        result = cursor.fetchone()
        cursor.close()

        return (
            dict(
                zip(
                    [
                        "id",
                        "dbIdent",
                        "meta",
                        "lastStatus",
                        "lastBackupAt",
                        "createdAt",
                        "updatedAt",
                    ],
                    result,
                )
            )
            if result
            else None
        )

    def get_log_by_id(self, id: str) -> Dict[str, Any]:
        """Retrieve a log by its ID.

        Args:
            id (str): The ID of the log to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the log details.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM log WHERE id = ?", (id,))
        result = cursor.fetchone()
        cursor.close()

        return (
            dict(
                zip(["id", "record", "type", "meta", "createdAt", "updatedAt"], result)
            )
            if result
            else None
        )

    def get_backups(
        self, dbIdent: Optional[str] = None, since: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve backups based on database identifier and time filter.

        Args:
            dbIdent (str, optional): The database identifier to filter backups. Defaults to None.
            since (str, optional): Human-readable time filter (e.g., "3 hours ago", "1 day ago", "1 month ago"). Defaults to None.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing backup details.
        """
        cursor = self._connection.cursor()

        # Convert human-readable time to datetime object
        if since:
            since_datetime = self._parse_human_readable_time(since)

            if since_datetime is None:
                raise ValueError(
                    "Invalid time format. Use 'X hours ago', 'X days ago', 'X months ago'."
                )

            # Convert datetime to string for SQL query
            since_datetime_str = since_datetime.strftime("%Y-%m-%d %H:%M:%S")

            # Prepare SQL query with time filter
            query = "SELECT * FROM backup WHERE lastBackupAt >= ?"
            params = (since_datetime_str,)

            if dbIdent:
                query += " AND dbIdent = ?"
                params += (dbIdent,)
        else:
            query = "SELECT * FROM backup"
            params = ()

            if dbIdent:
                query += " WHERE dbIdent = ?"
                params = (dbIdent,)

        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()

        return (
            [
                dict(
                    zip(
                        [
                            "id",
                            "dbIdent",
                            "meta",
                            "lastStatus",
                            "lastBackupAt",
                            "createdAt",
                            "updatedAt",
                        ],
                        result,
                    )
                )
                for result in results
            ]
            if results
            else []
        )

    def _parse_human_readable_time(self, time_str: str) -> Optional[datetime]:
        """
        Parse human-readable time string into a datetime object.

        Args:
            time_str (str): Time string (e.g., "3 hours ago", "1 day ago",
            "1 month ago", "30 minutes ago", "10 seconds ago", "2 weeks ago").

        Returns:
            datetime: The parsed datetime object or None if parsing fails.
        """
        now = datetime.now()

        # Basic parsing logic for "X units ago"
        parts = time_str.split()

        if len(parts) != 3 or parts[2] != "ago":
            return None

        try:
            value = int(parts[0])
        except ValueError:
            return None

        unit = parts[1]

        if unit == "hours" or unit == "hour":
            return now - timedelta(hours=value)
        elif unit == "minutes" or unit == "minute":
            return now - timedelta(minutes=value)
        elif unit == "seconds" or unit == "second":
            return now - timedelta(seconds=value)
        elif unit == "days" or unit == "day":
            return now - timedelta(days=value)
        elif unit == "weeks" or unit == "week":
            return now - timedelta(weeks=value)
        elif unit == "months" or unit == "month":
            return now - timedelta(days=value * 30)
        else:
            return None


def get_state_client(path: str) -> State:
    """Create and return a state instance.

    Args:
        path (str): SQLite database path.

    Returns:
        State: Initialized State client.
    """
    return State(path)
