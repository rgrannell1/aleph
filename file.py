
import collections
import os
import pathlib
from comby_matcher import CombyMatcher
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
