
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
          "startLine": match.location.start.line,
          "startCol": match.location.start.col,
          "startOffset": match.location.start.offset,
          "stopLine": match.location.stop.line,
          "stopCol": match.location.stop.col,
          "stopOffset": match.location.stop.offset
      })
