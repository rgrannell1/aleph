
from dataclasses import dataclass
import comby
import logging
from abc import abstractmethod


class RuleMatch:
  """Contains information for each extracted piece of code-information"""

  def __init__(self, data):
    for prop in self.props:
      if not prop in data:
        raise Exception(f'missing property {prop}')
    self.data = data


  @abstractmethod
  def create_table(self, conn):
    """Construct an sqlite table to store information"""
    pass

  @abstractmethod
  def write(self, conn):
    """Write SQL information to sqlite"""
    pass


class Rule:
  """Contains rule information, describing some aspect of the code we want to extract"""

  def log(name: str, match: comby.Match):
    """Log debug information for matched rule data"""

    logging.debug(f"Matched {name}\n\n{match.matched}\n\n")
