
from matches.function import FunctionRuleMatch
from rule import Rule
from comby import Comby


class PyFunction(Rule):
  """Extract function definition information for Python"""

  pattern = 'def :[name](...)'

  @classmethod
  def matches(cls, fpath: str, content: str) -> FunctionRuleMatch:
    """"""

    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      yield FunctionRuleMatch({
        "file": fpath,
        "type": "",
        "name": (match.environment['name'].fragment).strip(),
        "location": match.location
      })


class PyFunctionCall(Rule):
  """Extract function call information for Python"""

  pattern = ':[[name]](...)'

  @classmethod
  def matches(cls, fpath: str, content: str) -> FunctionRuleMatch:
    """"""

    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      yield FunctionRuleMatch({
        "file": fpath,
        "type": "",
        "name": (match.environment['name'].fragment).strip(),
        "location": match.location
      })
