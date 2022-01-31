
from matches.dependency import DependencyRuleMatch
from rule import Rule
from comby import Comby



class GoMultiImport(Rule):
  """Read go multi imports and extract package information"""

  pattern = 'import (:[imports])'

  @classmethod
  def matches(cls, fpath: str, content: str) -> DependencyRuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['imports'].fragment
      pkgs = [pkg.strip() for pkg in frag.encode(
          'raw_unicode_escape').decode('unicode_escape').replace('"', '').split('\n') if len(pkg.strip()) > 0]

      yield DependencyRuleMatch({
        "packages": pkgs,
        "file": fpath,
        "location": match.location
      })



class GoImport(Rule):
  """Read go single import and extract package information"""

  pattern = 'import ":[import]"'

  @classmethod
  def matches(cls, fpath: str, content: str) -> DependencyRuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['import'].fragment

      yield DependencyRuleMatch({
        "packages": [frag],
        "file": fpath,
        "location": match.location
      })

