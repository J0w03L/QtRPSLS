# This Python file uses the following encoding: utf-8
import logging
logger = logging.getLogger(__name__)

import sqlite3
import os

"""
    If any changes are made to the database structure, this number should be incremented.

    This is so that we can recognise databases that have been generated prior to an
    update and account for those accordingly.
"""
DB_VERSION = 1

class GameDB:
    def __init__(self, path: str):
        logger.debug("__init__()")

        self.path = path

        # Check if we already have a database at path; if we don't, we'll need to set up tables.
        dbNeedsSetup = not os.path.exists(path)
        logger.debug("Database needs table setup." if dbNeedsSetup else "Database exists; no setup needed.")

        # Create a Connection to the database.
        logger.debug(f"Creating connection at \"{path}\"")
        self.con = sqlite3.connect(path)

        # Make sure we setup the database tables if we need to.
        if dbNeedsSetup: self.setup_db()

        # Get database version.
        cur = self.con.cursor()
        foundVer = cur.execute("SELECT `version`, `created_version` FROM `meta`").fetchone()

        self.currentVersion = foundVer[0]
        self.createdVersion = foundVer[1]

        logger.debug(f"Game's DB_VERSION: {DB_VERSION}")
        logger.debug(f"Found  DB_VERSION: {self.currentVersion}")
        logger.debug(f"     Created with: {self.createdVersion}")

        # Cleanup after ourselves.
        cur.close()

    def setup_db(self):
        logger.debug("setup_db()")

        # Create a Cursor for the database.
        logger.debug("Creating cursor.")
        cur = self.con.cursor()

        # Setup the database tables.
        logger.debug("Creating tables.")
        cur.execute(
            """
            CREATE TABLE `meta` (
                `version`           INTEGER NOT NULL,
                `created_version`   INTEGER NOT NULL,
                `created`           INTEGER NOT NULL DEFAULT (unixepoch())
            );
            """
        )

        cur.execute(
            "INSERT INTO `meta` (`version`, `created_version`) VALUES (?, ?);",
            [DB_VERSION, DB_VERSION]
        )

        cur.execute(
            """
            CREATE TABLE `users` (
                `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
                `name`      TEXT NOT NULL
            );
            """
        )

        cur.execute(
            """
            CREATE TABLE `games` (
                `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
                `user`      INTEGER NOT NULL,
                `start`     INTEGER NOT NULL DEFAULT (unixepoch()),
                `end`       INTEGER NOT NULL DEFAULT (unixepoch()),
                `won`       INTEGER CHECK (`won` = 1 OR `won` = 0),
                FOREIGN KEY (`user`) REFERENCES `users` (`id`)
            );
            """
        )

        # We can speed up database queries by creating indexes for the columns we'll be querying.
        # Unique indexes double up as constraints, and are used to prevent certain rows having duplicate values.
        cur.execute("CREATE UNIQUE INDEX `uidx_users_name` ON `users` (`name`);")
        cur.execute("CREATE INDEX `idx_games_user` ON `games` (`user`);")

        # Save changes.
        logger.debug("Committing changes.")
        self.con.commit()

        # Cleanup after ourselves.
        cur.close()

        logger.debug("Database setup complete!")
