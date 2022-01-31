
from matches.function import FunctionRuleMatch, MethodRuleMatch
from rule import Rule
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
        "file": fpath,
        "receiver": match.environment['receiver'].fragment,
        "type": match.environment['type'].fragment,
        "name": match.environment['name'].fragment,
        "location": match.location
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
        "file": fpath,
        "type": "",
        "name": match.environment['name'].fragment,
        "location": match.location
      })
