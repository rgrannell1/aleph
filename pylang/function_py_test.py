import unittest

from pylang.function import PyFunction, PyFunctionCall


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


class TestFunctionCall(unittest.TestCase):
  def testPyFunctionCall(self):
    cases = [
      ('foobar()', 'foobar'),
      ('def bazbar():', None),
      ('bingbar(a, b, "123")', 'bingbar')
    ]

    fpath = 'test.py'
    for src, expected in cases:
      matches = list(PyFunctionCall.matches(fpath, src))

      if expected is None:
        assert len(matches) == 0, f"matched function-call with {matches[0].data['name']}"
      else:
        assert len(matches) == 1, f"did not receive a match for '{src}'"
        data = matches[0].data
        assert data['name'] == expected
