
from config import Config
from file import CodeBase, ProjectFile


def main():
  cfg = Config("./config.json")
  base = CodeBase(cfg)

  for project in base.list_projects():
    for fpath in project.list_source_files():
      file = ProjectFile(fpath)
      file.matches()


main()
