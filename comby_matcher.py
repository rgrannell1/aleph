
from rule_set import RuleSet
from go.rules import GoRuleSet
from js.rules import JsRuleSet
from py.rules import PyRuleSet
from ts.rules import TsRuleSet


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
