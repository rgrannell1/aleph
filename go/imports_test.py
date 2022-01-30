import unittest

from go.imports import GoImport, GoMultiImport


class TestGoMultiImport(unittest.TestCase):
  def testGoMultiImport(self):
    cases = [
        ('''import (
          "a",
          "b",
          "c",
        )''', ['a', 'b', 'c']),
        ('''import ("a")''', ['a'])
    ]

    for src, packages in cases:
      matches = list(GoMultiImport.matches('test.go', src))

      assert len(matches) == 1
      data = matches[0].data

      assert len(data['packages']) == len(packages)


class TestGoImport(unittest.TestCase):
  def testGoImport(self):
    cases = [
      ('import "foo/bar"', 'foo/bar'),
      ('import "baz"', 'baz')
    ]

    for src, imported in cases:
      matches = list(GoImport.matches('test.go', src))

      assert len(matches) == 1
      data = matches[0].data

      assert data['packages'][0] == imported
      assert data['fpath'] == 'test.go'
