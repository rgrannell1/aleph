
from matches.cclass import ClassRuleMatch
from rule import Rule
from comby import Comby


class PyClass(Rule):
  """Extract class definition information for Python"""

  pattern = 'class :[name]:'

  @classmethod
  def matches(cls, fpath: str, content: str) -> ClassRuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      name = match.environment['name'].fragment.strip()

      yield ClassRuleMatch({
        "file": fpath,
        "extends": "",
        "name": name,
        "startLine": 0,
        "startCol": 0,
        "startOffset": 0,
        "stopLine": 0,
        "stopCol": 0,
        "stopOffset": 0
      })


class PyClassExtends(Rule):
  """Extract class definition information for Python"""

  pattern = 'class :[name](:[extends])'

  @classmethod
  def matches(cls, fpath: str, content: str) -> ClassRuleMatch:
    """"""

    comby = Comby()
    for match in comby.matches(content, cls.pattern):


      name = match.environment['name'].fragment.strip()
      extends = match.environment['extends'].fragment.strip()

      yield ClassRuleMatch({
          "file": fpath,
          "extends": extends,
          "name": name,
          "startLine": 0,
          "startCol": 0,
          "startOffset": 0,
          "stopLine": 0,
          "stopCol": 0,
          "stopOffset": 0
      })
