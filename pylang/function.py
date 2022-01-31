
from matches.function import FunctionRuleMatch
from rule import Rule
from comby import Comby


class PyFunction(Rule):
  """Extract function definition information for Python"""

  patterns = ['def :[name](...)']

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
          "name": (match.environment['name'].fragment).strip(),
          "location": match.location
        })

      if matched:
        return


class PyFunctionCall(Rule):
  """Extract function call information for Python"""

  patterns = [
    ':[prefix~[def ]*][name~[a-zA-Z0-9_]+](...)'
  ]

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
          "name": (match.environment['name'].fragment).strip(),
          "location": match.location
        })

      if matched:
        return
