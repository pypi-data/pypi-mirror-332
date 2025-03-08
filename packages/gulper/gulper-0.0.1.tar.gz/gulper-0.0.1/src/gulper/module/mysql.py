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

from typing import Any, Dict, Optional
from .database import Database


class MySQL(Database):
    """
    Manages MySQL database operations,
    including backups, restores and connection testing.
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int,
        databases: list[str],
        temp_path: str,
        options: Optional[Dict[str, Any]],
    ):
        """
        Initializes the MySQL instance

        Args:
            host (str): The mysql database host
            username (str): The mysql database username
            password (str): The mysql database password
            port (int): The mysql database port
            databases (list[str]): The database to backup or empty list if all databases
            temp_path (str): The temp path to use for backup
            options (Optional[Dict[str, Any]]): The list of options for backups
        """
        self._host = host
        self._username = username
        self._password = password
        self._port = port
        self._databases = databases
        self._temp_path = temp_path
        self._options = options

    def backup(self) -> str:
        """
        Backup the database

        Returns:
            str: the path to the backup
        """
        pass

    def restore(self, backup_path: str) -> bool:
        """
        Restore the database from a backup

        Args:
            backup_path (str): The path to .tar.gz backup

        Returns:
            bool: whether the restore succeeded or not
        """
        pass

    def connect(self) -> bool:
        """
        Connect into the database

        Returns:
            bool: whether the connection is established or not
        """
        pass


def get_mysql(
    host: str,
    username: str,
    password: str,
    port: int,
    databases: list[str],
    temp_path: str,
    options: Optional[Dict[str, Any]],
) -> MySQL:
    """
    Get MySQL instance

    Args:
        host (str): The mysql database host
        username (str): The mysql database username
        password (str): The mysql database password
        port (int): The mysql database port
        databases (list[str]): The database to backup or empty list if all databases
        temp_path (str): The temp path to use for backup
        options (Optional[Dict[str, Any]]): The list of options for backups

    Returns:
        MySQL: The mysql instance
    """
    return MySQL(host, username, password, port, databases, temp_path, options)
