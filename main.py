
import os
import pathlib

from comby import Comby
import collections
from config import Config


class CodeBase:
  def __init__(self, config: Config):
    self.cfg = config


  def list_projects(self) -> None:
    children = os.listdir(self.cfg.fpath)

    for child in children:
      child_path = os.path.join(self.cfg.fpath, child)

      if os.path.isdir(child_path) and child not in self.cfg.ignored_projects:
        yield Project(child_path, self.cfg)


class Project:
  def __init__(self, fpath: str, cfg: Config):
    self.fpath = fpath
    self.cfg = cfg


  def is_ignored_folder(self, dir: str) -> bool:
    return os.path.basename(dir) in self.cfg.ignored_folders


  def is_ignored_file(self, file: str) -> bool:
    ext = pathlib.Path(file).suffix

    return ext not in self.cfg.extensions


  def list_source_files(self):
    queue = collections.deque([self.fpath])

    while len(queue) > 0:
      tgt = queue.pop()

      if os.path.isdir(tgt):
        if not self.is_ignored_folder(tgt):
          for child in os.listdir(tgt):
            child_path = os.path.join(tgt, child)
            queue.append(child_path)

      elif os.path.isfile(tgt):
        if self.is_ignored_file(tgt):
          pass
        else:
          yield tgt

      else:
        pass



class CombyMatcher:
  @staticmethod
  def matches(fpath: str, ruleset: any):
    with open(fpath) as conn:
      content = conn.read()

      cmb = Comby()
      matches = cmb.matches(content, ':[[receiver]].:[[message]]')

      for xyz in matches:
        print(xyz.environment)
        raise Exception(10)


  @staticmethod
  def go(fpath: str):
    CombyMatcher.matches(fpath, [])


  @staticmethod
  def js(fpath: str):
    CombyMatcher.matches(fpath, [])


  @staticmethod
  def ts(fpath: str):
    CombyMatcher.matches(fpath, [])


  @staticmethod
  def py(fpath: str):
    CombyMatcher.matches(fpath, [])


class ProjectFile:
  def __init__(self, fpath: str):
    self.fpath = fpath


  def matches(self):
    fpath = self.fpath
    ext = pathlib.Path(fpath).suffix

    if ext == '.go':
      return CombyMatcher.go(fpath)
    elif ext == '.js' or ext == '.jsx':
      return CombyMatcher.js(fpath)
    elif ext == '.ts' or ext == '.tsx':
      return CombyMatcher.ts(fpath)
    elif ext == '.py':
      return CombyMatcher.py(fpath)
    else:
      raise Exception(fpath)


def main():
  cfg = Config("./config.json")
  base = CodeBase(cfg)

  for project in base.list_projects():
    for fpath in project.list_source_files():
      file = ProjectFile(fpath)
      file.matches()


main()
