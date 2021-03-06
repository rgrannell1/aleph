
from pylang.cclass import PyClass, PyClassExtends
from pylang.function import PyFunction
from pylang.imports import PyFromImport, PyImport
from rule_set import RuleSet


class PyRuleSet(RuleSet):
  """All data to extract from Python"""

  rules = [
    PyFromImport,
    PyImport,
    PyFunction,
    PyClassExtends,
    PyClass
  ]
