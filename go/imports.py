
from matches.dependency import DependencyRuleMatch
from rule import Rule, RuleMatch
from comby import Comby



class GoMultiImport(Rule):
  pattern = 'import (:[imports])'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['imports'].fragment
      pkgs = [pkg.strip() for pkg in frag.encode(
          'raw_unicode_escape').decode('unicode_escape').replace('"', '').split('\n') if len(pkg) > 0]

      yield DependencyRuleMatch({
          "packages": pkgs,
          "fpath": fpath
      })


class GoImport(Rule):
  pattern = 'import ":[import]"'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      comby = Comby()

      for match in comby.matches(content, cls.pattern):
        frag = match.environment['import'].fragment

        yield DependencyRuleMatch({
            "packages": [frag],
            "fpath": fpath
        })
