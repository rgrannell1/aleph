
import comby
import logging
from abc import abstractmethod


class RuleMatch:
  def __init__(self, data):
    self.data = data


  @abstractmethod
  def create_table(self, conn):
    pass

  @abstractmethod
  def write(self, conn):
    pass


class Rule:
  def log(name: str, match: comby.Match):
    logging.info(f"Matched {name}\n\n{match.matched}\n\n")
