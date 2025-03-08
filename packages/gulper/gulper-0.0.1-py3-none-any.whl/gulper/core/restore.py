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

import json
from gulper.module import Config
from gulper.module import State
from gulper.module import Logger
from gulper.module import get_storage
from gulper.module import get_database
from gulper.exception import BackupNotFound
from gulper.exception import OperationFailed


class Restore:
    """
    Restore Core Functionalities
    """

    def __init__(
        self,
        config: Config,
        state: State,
        logger: Logger,
    ):
        self._config = config
        self._state = state
        self._logger = logger

    def setup(self):
        """
        Setup calls
        """
        self._logger.get_logger().info("Connect into the state database")
        self._state.connect()
        self._logger.get_logger().info("Migrate the state database tables")
        self._state.migrate()

    def restore(self, db_name: str, backup_id: str) -> bool:
        """
        Restore a database from a backup

        Args:
            db_name (str): The database name
            backup_id (str): The backup id

        Returns:
            bool: whether the restore succeeded or not
        """
        backup = self._state.get_backup_by_id(id)

        if backup is None:
            raise BackupNotFound(f"Backup with id {id} not found!")

        backup = True
        meta = json.loads(backup.get("meta"))

        file = None
        for backup in meta["backups"]:
            try:
                storage = get_storage(self._config, backup.get("storage_name"))
                storage.download_file(backup.get("file"), self._config.get_temp_dir())
                file = backup.get("file")
                backup = True
            except Exception as e:
                backup = False
                self._logger.get_logger().error(
                    "Unable to restore backup {} file {} in storage {}: {}".format(
                        id,
                        backup.get("file"),
                        backup.get("storage_name"),
                        str(e),
                    )
                )
            if backup and file:
                break

        if file is None:
            raise BackupNotFound(f"Backup with id {id} not found!")

        try:
            database = get_database(self._config, backup.get("dbIdent"))
            database.restore("{}/{}".format(self._config.get_temp_dir(), file))
        except Exception as e:
            raise OperationFailed(
                "Failed to restore database {}: {}".format(
                    backup.get("dbIdent"), str(e)
                )
            )

        return True
