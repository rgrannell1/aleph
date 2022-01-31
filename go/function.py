
from matches.function import FunctionRuleMatch, MethodRuleMatch
from rule import Rule
from comby import Comby


class GoMethod(Rule):
  """Extract method definition information for Golang"""

  patterns = ['func (:[[receiver]] *:[[type]]) :[[name]]']

  @classmethod
  def matches(cls, fpath: str, content: str) -> MethodRuleMatch:
    """"""

    comby = Comby()
    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        yield MethodRuleMatch({
          "file": fpath,
          "receiver": match.environment['receiver'].fragment,
          "type": match.environment['type'].fragment,
          "name": match.environment['name'].fragment,
          "location": match.location
        })

      if matched:
        return


class GoFunction(Rule):
  """Extract function definition information for Golang"""

  patterns = ['func :[[name]] (...)']

  @classmethod
  def matches(cls, fpath: str, content: str) -> FunctionRuleMatch:
    """"""

    comby = Comby()
    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        yield FunctionRuleMatch({
          "file": fpath,
          "type": "",
          "name": match.environment['name'].fragment,
          "location": match.location
        })

      if matched:
        return
