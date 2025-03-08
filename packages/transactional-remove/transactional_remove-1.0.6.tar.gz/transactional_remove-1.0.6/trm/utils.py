import sqlite3
import pkg_resources

# type constants (file, links, empty directories, and directories with items)
FILE = "file"
DIR = "dir"
LINK = "link"
DIRF = "dirf"

# action constants (true for rollback, false for remove)
RM = False
RB = True

def log(item: str, type: str, action: bool):
    # logs actions
    db_path = pkg_resources.resource_filename("trm", "trm.sql")
    db = sqlite3.connect(db_path)
    cur = db.cursor()

def save(item: str):
    # copies file
    pass