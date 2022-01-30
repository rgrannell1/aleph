
import json

class Config:
  """Load configuration from a JSON file"""
  def __init__(self, fpath: str):
    with open(fpath) as conn:
      data = json.load(conn)

      self.fpath = data['fpath']
      self.extensions = set(data['extensions'])
      self.ignored_folders = set(data['ignored_folders'])
      self.ignored_projects = set(data['ignored_projects'])
