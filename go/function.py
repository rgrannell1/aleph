
from rule import Rule, RuleMatch
from comby import Comby


class GoMethod(Rule):
  """Extract method definition information for Golang"""

  pattern = 'func (:[[receiver]] *[[type]]) [[name]]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      raise Exception(10)
      print('xxx')
      yield RuleMatch()


class GoFunction(Rule):
  """Extract function definition information for Golang"""

  pattern = 'func (:[[receiver]] *[[type]]) [[name]]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      raise Exception(11)
      print('xxx')
      yield RuleMatch()
