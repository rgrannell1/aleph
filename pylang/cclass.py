
from matches.cclass import ClassRuleMatch
from rule import Rule
from comby import Comby


class PyClass(Rule):
  """Extract class definition information for Python"""

  patterns = ['class :[name]:']

  @classmethod
  def matches(cls, fpath: str, content: str) -> ClassRuleMatch:
    """"""

    comby = Comby()
    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True
        name = match.environment['name'].fragment.strip()

        yield ClassRuleMatch({
          "file": fpath,
          "extends": "",
          "name": name,
          "startLine": match.location.start.line,
          "startCol": match.location.start.col,
          "startOffset": match.location.start.offset,
          "stopLine": match.location.stop.line,
          "stopCol": match.location.stop.col,
          "stopOffset": match.location.stop.offset
        })

      if matched:
        return


class PyClassExtends(Rule):
  """Extract class definition information for Python"""

  patterns = ['class :[name](:[extends])']

  @classmethod
  def matches(cls, fpath: str, content: str) -> ClassRuleMatch:
    """"""

    comby = Comby()
    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        name = match.environment['name'].fragment.strip()
        extends = match.environment['extends'].fragment.strip()

        yield ClassRuleMatch({
            "file": fpath,
            "extends": extends,
            "name": name,
            "startLine": match.location.start.line,
            "startCol": match.location.start.col,
            "startOffset": match.location.start.offset,
            "stopLine": match.location.stop.line,
            "stopCol": match.location.stop.col,
            "stopOffset": match.location.stop.offset
        })

      if matched:
        return
