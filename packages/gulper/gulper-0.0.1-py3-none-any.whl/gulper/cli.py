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

import click
from gulper import __version__


@click.group(
    help="🐺 A Command Line Tool to Backup and Restore SQLite, MySQL and PostgreSQL!"
)
@click.version_option(version=__version__, help="Show the current version")
@click.option(
    "--config", default="/etc/config.yaml", help="Path to the configuration file"
)
@click.pass_context
def main(ctx, config):
    """Main command group for Gulper CLI."""
    ctx.ensure_object(dict)
    ctx.obj["config"] = config


@main.group()
@click.pass_context
def backup(ctx):
    """Backup related commands"""
    pass


@backup.command("list", help="List available backups.")
@click.option("--db", help="Database name")
@click.option("--since", help="Time range for listing backups")
@click.pass_context
def backup_list(ctx, db, since):
    click.echo(
        f"Listing backups for db: {db}, since: {since}, config: {ctx.obj['config']}"
    )


@backup.command("run", help="Run a backup for a specified database.")
@click.argument("db")
@click.pass_context
def backup_run(ctx, db):
    click.echo(f"Running backup for db: {db}, config: {ctx.obj['config']}")


@backup.command("get", help="Retrieve details of a specific backup.")
@click.argument("backup_id")
@click.pass_context
def backup_get(ctx, backup_id):
    click.echo(f"Getting backup: {backup_id}, config: {ctx.obj['config']}")


@backup.command("delete", help="Delete a backup by its ID.")
@click.argument("backup_id")
@click.pass_context
def backup_delete(ctx, backup_id):
    click.echo(f"Deleting backup: {backup_id}, config: {ctx.obj['config']}")


@main.group()
@click.pass_context
def restore(ctx):
    """Restore related commands"""
    pass


@restore.command("run", help="Restore a database from a specific backup.")
@click.argument("backup_id")
@click.pass_context
def restore_run(ctx, backup_id):
    click.echo(f"Running restore for backup: {backup_id}, config: {ctx.obj['config']}")


@restore.command("db", help="Restore a specific database.")
@click.argument("db")
@click.pass_context
def restore_db(ctx, db):
    click.echo(f"Restoring database: {db}, config: {ctx.obj['config']}")


@main.command(help="Run backup schedules")
@click.option("--daemon", is_flag=True, help="Run in daemon mode")
@click.pass_context
def cron(ctx, daemon):
    click.echo(
        f"Running cron{'in daemon mode' if daemon else ''}, config: {ctx.obj['config']}"
    )


@main.group()
@click.pass_context
def log(ctx):
    """Log related commands"""
    pass


@log.command("list", help="List available logs.")
@click.option("--db", help="Database name to filter logs")
@click.option("--since", help="Time range for listing logs")
@click.pass_context
def log_list(ctx, db, since):
    click.echo(
        f"Listing logs for db: {db}, since: {since}, config: {ctx.obj['config']}"
    )


if __name__ == "__main__":
    main()
