
from matches.dependency import DependencyRuleMatch
from rule import Rule
from comby import Comby



class GoMultiImport(Rule):
  """Read go multi imports and extract package information"""

  patterns = ['import (:[imports])']

  @classmethod
  def matches(cls, fpath: str, content: str) -> DependencyRuleMatch:
    comby = Comby()

    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        frag = match.environment['imports'].fragment
        pkgs = [pkg.strip() for pkg in frag.encode(
            'raw_unicode_escape').decode('unicode_escape').replace('"', '').split('\n') if len(pkg.strip()) > 0]

        yield DependencyRuleMatch({
          "packages": pkgs,
          "file": fpath,
          "startLine": match.location.start.line,
          "startCol": match.location.start.col,
          "startOffset": match.location.start.offset,
          "stopLine": match.location.stop.line,
          "stopCol": match.location.stop.col,
          "stopOffset": match.location.stop.offset
        })

      if matched:
        return


class GoImport(Rule):
  """Read go single import and extract package information"""

  patterns = ['import ":[import]"']

  @classmethod
  def matches(cls, fpath: str, content: str) -> DependencyRuleMatch:
    comby = Comby()

    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        frag = match.environment['import'].fragment

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

      if matched:
        return
