import unittest

from go.function import GoFunction, GoMethod


class TestGoMethod(unittest.TestCase):
  def testGoMethod(self):
    cases = [
        ('func (foo *bar) BazTest', ('foo', 'bar', 'BazTest'))
    ]

    for src, results in cases:
      receiver, type, name = results

      matches = list(GoMethod.matches('test.go', src))
      assert len(matches) == 1

      data = matches[0].data
      assert data['receiver'] == receiver
      assert data['type'] == type
      assert data['name'] == name


class TestGoFunction(unittest.TestCase):
  def testGoFunction(self):
    cases = [
        ('func BazTest ()', 'BazTest')
    ]

    for src, results in cases:
      name = results

      matches = list(GoFunction.matches('test.go', src))
      assert len(matches) == 1

      data = matches[0].data
      assert data['name'] == name
