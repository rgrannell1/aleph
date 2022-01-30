
from abc import abstractmethod


class RuleMatch:
  """Contains information for each extracted piece of code-information"""

  def __init__(self, data):
    for prop in self.props:
      if not prop in data:
        raise Exception(f'missing property {prop} from {self}')
    self.data = data

  @abstractmethod
  def create_table(self, conn):
    """Construct an sqlite table to store information"""
    pass

  @abstractmethod
  def write(self, conn):
    """Write SQL information to sqlite"""
    pass
