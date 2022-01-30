
from py.imports import PyFromImport, PyImport
from rule_set import RuleSet


class PyRuleSet(RuleSet):
  rules = [
    PyFromImport,
    PyImport
  ]
