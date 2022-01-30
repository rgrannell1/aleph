
from go.function import GoFunction, GoMethod
from go.imports import GoImport, GoMultiImport
from rule_set import RuleSet
from comby import Comby


class GoRuleSet(RuleSet):
  rules = [
    GoMethod,
    GoFunction,
    GoMultiImport,
    GoImport
  ]
