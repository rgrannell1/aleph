
from pylang.ruleset import PyRuleSet
from rule_set import RuleSet
from go.ruleset import GoRuleSet
from js.ruleset import JsRuleSet


class CombyMatcher:
  """Extract all interesting information for each programming language supported."""

  @staticmethod
  def matches(fpath: str, ruleSet: RuleSet):
    with open(fpath) as conn:
      try:
        content = conn.read()

        if len(content) == 0:
          return
      except Exception as err:
        print(err)
        return

    for match in ruleSet.matches(fpath, content):
      yield match

  @staticmethod
  def go(fpath: str):
    return CombyMatcher.matches(fpath, GoRuleSet)

  @staticmethod
  def js(fpath: str):
    return CombyMatcher.matches(fpath, JsRuleSet)

  @staticmethod
  def ts(fpath: str):
    return CombyMatcher.matches(fpath, JsRuleSet)

  @staticmethod
  def py(fpath: str):
    return CombyMatcher.matches(fpath, PyRuleSet)
