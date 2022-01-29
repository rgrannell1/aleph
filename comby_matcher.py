
from rule_set import RuleSet
from rules_go import GoRuleSet
from rules_js import JsRuleSet
from rules_py import PyRuleSet
from rules_ts import TsRuleSet


class CombyMatcher:
  @staticmethod
  def matches(fpath: str, ruleSet: RuleSet):
    with open(fpath) as conn:
      content = conn.read()

    for match in ruleSet.matches(fpath, content):
      print(match.data)

  @staticmethod
  def go(fpath: str):
    CombyMatcher.matches(fpath, GoRuleSet)

  @staticmethod
  def js(fpath: str):
    CombyMatcher.matches(fpath, JsRuleSet)

  @staticmethod
  def ts(fpath: str):
    CombyMatcher.matches(fpath, TsRuleSet)

  @staticmethod
  def py(fpath: str):
    CombyMatcher.matches(fpath, PyRuleSet)
