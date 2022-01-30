
import logging
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

      cls.log(cls.__name__, match)
      yield DependencyRuleMatch({
        "packages": [frag],
        "fpath": fpath
      })


class PyImport(Rule):
  pattern = ':[~^\s*]import :[import]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['import'].fragment

      cls.log(cls.__name__, match)
      yield DependencyRuleMatch({
        "packages": [frag],
        "fpath": fpath
      })
