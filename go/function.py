
from rule import Rule, RuleMatch
from comby import Comby


class GoMethod(Rule):
  """Extract method definition information for Golang"""

  pattern = 'func (:[[receiver]] *:[[type]]) :[[name]]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      yield RuleMatch({
        "fpath": fpath,
        "receiver": match.environment['receiver'].fragment,
        "type": match.environment['type'].fragment,
        "name": match.environment['name'].fragment
      })


class GoFunction(Rule):
  """Extract function definition information for Golang"""

  pattern = 'func :[[name]] (...)'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      yield RuleMatch({
        "fpath": fpath,
        "name": match.environment['name'].fragment
      })
