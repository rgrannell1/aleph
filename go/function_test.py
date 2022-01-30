import unittest

from go.function import GoFunction, GoMethod


class TestGoMethod(unittest.TestCase):
  def testGoMethod(self):
    cases = [
        ('func (foo *bar) BazTest (', 10)
    ]

    for src, results in cases:
      matches = list(GoMethod.matches('test.go', src))


class TestGoFunction(unittest.TestCase):
  def testGoFunction(self):
    cases = [
        ('func (foo *bar) BazTest (', 10)
    ]

    for src, results in cases:
      matches = list(GoMethod.matches('test.go', src))
