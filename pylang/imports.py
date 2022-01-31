
from matches.dependency import DependencyRuleMatch
from rule import Rule
from comby import Comby
from rule_match import RuleMatch


class PyFromImport(Rule):
  """A `from module` import in python, capturing the target module"""

  patterns = ['from :[import] import']

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        frag = match.environment['import'].fragment

        cls.log(cls.__name__, match)
        yield DependencyRuleMatch({
          "packages": [frag],
          "file": fpath,
          "location": match.location
        })

      if matched:
        return


class PyImport(Rule):
  """A single module import, capturing the target module"""

  patterns = [':[~^import] :[import]']

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    matched = False

    for pattern in cls.patterns:
      for match in comby.matches(content, pattern):
        matched = True

        frag = match.environment['import'].fragment

        cls.log(cls.__name__, match)
        yield DependencyRuleMatch({
          "packages": [frag],
          "file": fpath,
          "location": match.location
        })

      if matched:
        return
