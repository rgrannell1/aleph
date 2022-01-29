
from rule import Rule, RuleMatch
from rule_set import RuleSet
from comby import Comby


class GoMethod(Rule):
  pattern = 'func (:[[receiver]] *[[type]]) [[name]]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      raise Exception(10)
      print('xxx')
      yield RuleMatch()


class GoFunction(Rule):
  pattern = 'func (:[[receiver]] *[[type]]) [[name]]'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      raise Exception(11)
      print('xxx')
      yield RuleMatch()


class DependencyRuleMatch(RuleMatch):
  def create_table(self, conn):
    sql = '''
    create table if not exists dependency (
      name    string not null
      file    string not null

      primary key(name, file)
    );
    '''
    curr = conn.cursor()
    curr.execute(sql)
    curr.commit()

  def write(self, conn):
    sql = 'insert into dependency (name, file) values (?, ?)'

    curr = conn.cursor()
    for pkg in self.data['packages']:
      curr.execute(sql, pkg, self.data['fpath'])
    curr.commit()


class GoMultiImport(Rule):
  pattern = 'import (:[imports])'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()

    for match in comby.matches(content, cls.pattern):
      frag = match.environment['imports'].fragment
      pkgs = [pkg.strip() for pkg in frag.encode(
          'raw_unicode_escape').decode('unicode_escape').replace('"', '').split('\n') if len(pkg) > 0]

      yield DependencyRuleMatch({
        "packages": pkgs,
        "fpath": fpath
      })


class GoImport(Rule):
  pattern = 'import ":[import]"'

  @classmethod
  def matches(cls, fpath: str, content: str) -> RuleMatch:
    comby = Comby()
    for match in comby.matches(content, cls.pattern):
      comby = Comby()

      for match in comby.matches(content, cls.pattern):
        frag = match.environment['imports'].fragment
        raise Exception(frag)


class GoRuleSet(RuleSet):
  rules = [
    GoMethod,
    GoFunction,
    GoMultiImport,
    GoImport
  ]
