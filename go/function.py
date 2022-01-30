
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
        "file": fpath,
        "receiver": match.environment['receiver'].fragment,
        "type": match.environment['type'].fragment,
        "name": match.environment['name'].fragment,
        "startLine": 0,
        "startCol": 0,
        "startOffset": 0,
        "stopLine": 0,
        "stopCol": 0,
        "stopOffset": 0
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
        "startLine": 0,
        "startCol": 0,
        "startOffset": 0,
        "stopLine": 0,
        "stopCol": 0,
        "stopOffset": 0
      })
