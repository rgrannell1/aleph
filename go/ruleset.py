
from go.function import GoCall, GoFunction, GoMethod
from go.imports import GoImport, GoMultiImport
from rule_set import RuleSet


class GoRuleSet(RuleSet):
  """All data to extract from Golang"""

  rules = [
    GoMethod,
    GoFunction,
    GoMultiImport,
    GoImport,
    GoCall
  ]
