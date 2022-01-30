
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
          "startLine": 0,
          "startCol": 0,
          "startOffset": 0,
          "stopLine": 0,
          "stopCol": 0,
          "stopOffset": 0
      })
