
from matches.dependency import DependencyRuleMatch
from rule import Rule
from comby import Comby
from rule_match import RuleMatch


class PyFromImport(Rule):
  """A `from module` import in python, capturing the target module"""

  pattern = 'from :[import] import'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['import'].fragment

      cls.log(cls.__name__, match)
      yield DependencyRuleMatch({
        "packages": [frag],
        "file": fpath,
        "startLine": match.location.start.line,
        "startCol": match.location.start.col,
        "startOffset": match.location.start.offset,
        "stopLine": match.location.stop.line,
        "stopCol": match.location.stop.col,
        "stopOffset": match.location.stop.offset
      })


class PyImport(Rule):
  """A single module import, capturing the target module"""

  pattern = ':[~^import] :[import]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['import'].fragment

      cls.log(cls.__name__, match)
      yield DependencyRuleMatch({
        "packages": [frag],
        "file": fpath,
        "startLine": match.location.start.line,
        "startCol": match.location.start.col,
        "startOffset": match.location.start.offset,
        "stopLine": match.location.stop.line,
        "stopCol": match.location.stop.col,
        "stopOffset": match.location.stop.offset

      })
