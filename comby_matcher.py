
from rule_set import RuleSet
from go.ruleset import GoRuleSet
from js.ruleset import JsRuleSet
from py.ruleset import PyRuleSet
from ts.ruleset import TsRuleSet


class CombyMatcher:
  @staticmethod
  def matches(fpath: str, ruleSet: RuleSet):
    with open(fpath) as conn:
      try:
        content = conn.read()
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
    return CombyMatcher.matches(fpath, TsRuleSet)

  @staticmethod
  def py(fpath: str):
    return CombyMatcher.matches(fpath, PyRuleSet)
