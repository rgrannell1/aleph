
from pylang.imports import PyFromImport, PyImport
from rule_set import RuleSet


class PyRuleSet(RuleSet):
  """All data to extract from Python"""

  rules = [
    PyFromImport,
    PyImport
  ]
