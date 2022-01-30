import unittest

from pylang.cclass import PyClass, PyClassExtends


class TestPyClass(unittest.TestCase):
  def testPyClass(self):
    cases = [
      ('   class Testing', 'Testing'),
    ]

    fpath = 'test.py'
    for src, expected in cases:
      matches = list(PyClass.matches(fpath, src))

      assert len(matches) == 1
      data = matches[0].data

      assert data['name'] == expected


class TestPyClassExtends(unittest.TestCase):
  def testPyClassExtends(self):
    cases = [
      ('   class Testing(Foo)', ['Testing', 'Foo']),
    ]

    fpath = 'test.py'
    for src, expected in cases:
      name, extends = expected

      matches = list(PyClassExtends.matches(fpath, src))
      assert len(matches) == 1
      data = matches[0].data

      assert data['name'] == name
      assert data['extends'] == extends
