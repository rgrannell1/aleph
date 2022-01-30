
from config import Config
from file import CodeBase, ProjectFile
import sqlite3


def main():
  conn = sqlite3.connect("/home/rg/.aleph.sqlite")
  cfg = Config("./config.json")
  base = CodeBase(cfg)

  for project in base.list_projects():
    for fpath in project.list_source_files():
      for match in ProjectFile(fpath).matches():
        print(match)

        if match:
          match.create_table(conn)
          match.write(conn)

main()
