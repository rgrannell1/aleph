import unittest

from pylang.function import PyFunction


class TestPyFunction(unittest.TestCase):
  def testPyFunction(self):
    cases = [
      ('def foo (a, b):', 'foo'),
      ('  def foo_bar():', 'foo_bar'),
    ]

    fpath = 'test.py'
    for src, expected in cases:
      matches = list(PyFunction.matches(fpath, src))

      assert len(matches) == 1
      data = matches[0].data

      assert data['name'] == expected
