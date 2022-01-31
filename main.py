
from config import Config
from file import CodeBase, ProjectFile
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
  """Extract codebase information and save information"""

  conn = sqlite3.connect("/home/rg/.aleph.sqlite")
  cfg = Config("./config.json")
  base = CodeBase(cfg)

  for project in base.list_projects():
    for fpath in project.list_source_files():
      if '__init__' in fpath:
        continue # it makes things stall for some reason

      logging.info(f"analysing {fpath}")

      for match in ProjectFile(fpath).matches():
        if match:
          match.create_table(conn)
          match.write(conn)

  logging.info("all projects analysed")
  conn.close()

main()
