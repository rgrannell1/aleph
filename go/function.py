
from matches.function import FunctionRuleMatch, MethodRuleMatch
from rule import Rule, RuleMatch
from comby import Comby


class GoMethod(Rule):
  """Extract method definition information for Golang"""

  pattern = 'func (:[[receiver]] *:[[type]]) :[[name]]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> MethodRuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      yield MethodRuleMatch({
        "fpath": fpath,
        "receiver": match.environment['receiver'].fragment,
        "type": match.environment['type'].fragment,
        "name": match.environment['name'].fragment
      })


class GoFunction(Rule):
  """Extract function definition information for Golang"""

  pattern = 'func :[[name]] (...)'

  @classmethod
  def matches(cls, fpath: str, content: str) -> FunctionRuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      yield FunctionRuleMatch({
        "fpath": fpath,
        "name": match.environment['name'].fragment
      })
