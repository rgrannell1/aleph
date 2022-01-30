
from matches.dependency import DependencyRuleMatch
from rule import Rule, RuleMatch
from comby import Comby


class PyFromImport(Rule):
  pattern = 'from :[import] import'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['import'].fragment

      yield DependencyRuleMatch({
        "packages": [frag],
        "fpath": fpath
      })


class PyImport(Rule):
  pattern = 'import :[import]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['import'].fragment

      yield DependencyRuleMatch({
        "packages": [frag],
        "fpath": fpath
      })
