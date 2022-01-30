import unittest

from pylang.imports import PyFromImport, PyImport


class TestPyFromImport(unittest.TestCase):
  def testPyFromImport(self):
    cases = [
        ('from foo import baz', ['foo']),
        ('    from foo import baz', ['foo'])
    ]

    fpath = 'test.py'
    for src, packages in cases:
      matches = list(PyFromImport.matches(fpath, src))

      assert len(matches) == 1
      data = matches[0].data
      print(data)

      assert len(data['packages']) == len(packages)


class TestPyImport(unittest.TestCase):
  def testPyImport(self):
    cases = [
      ('import foo', ['foo']),
      ('    import foo', []),
    ]

    fpath = 'test.py'
    for src, imported in cases:
      matches = list(PyImport.matches(fpath, src))

      assert len(matches) == len(imported)

      if len(matches) > 0:
        data = matches[0].data

        assert data['file'] == fpath
        assert len(data['packages']) == len(imported)
        assert data['packages'][0] == imported[0]
