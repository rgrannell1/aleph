

from rule_match import RuleMatch


class FunctionRuleMatch(RuleMatch):
  props = {
    'name',
    'file',
    'startLine',
    'startCol',
    'startOffset',
    'stopLine',
    'stopCol',
    'stopOffset'
  }

  def create_table(self, conn):
    sql = '''
    create table if not exists function (
      name        string not null,
      file        string not null,
      startLine   integer,
      startCol    integer,
      startOffset integer,
      stopLine    integer,
      stopCol     integer,
      stopOffset  integer,

      primary key(name, file, startLine, startCol, startOffset, stopLine, stopCol, stopOffset)
    );
    '''
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

  def write(self, conn):
    sql = 'insert or replace into function (name, file, startLine, startCol, startOffset, stopLine, stopCol, stopOffset) values (?, ?, ?, ?, ?, ?, ?, ?)'

    curr = conn.cursor()
    curr.execute(sql, (
      self.data['name'],
      self.data['file'],
      self.data['startLine'],
      self.data['startCol'],
      self.data['startOffset'],
      self.data['stopLine'],
      self.data['stopCol'],
      self.data['stopOffset']))

    conn.commit()


class MethodRuleMatch(RuleMatch):
  props = {
    'receiver',
    'name',
    'type',
    'file',
    'startLine',
    'startCol',
    'startOffset',
    'stopLine',
    'stopCol',
    'stopOffset'
  }


  def create_table(self, conn):
    sql = '''
    create table if not exists method (
      file        string not null,
      receiver    string not null,
      type        string,
      name        string not null,
      startLine   integer,
      startCol    integer,
      startOffset integer,
      stopLine    integer,
      stopCol     integer,
      stopOffset  integer,

      primary key(file, receiver, type, name, startLine, startCol, startOffset, stopLine, stopCol, stopOffset)
    );
    '''
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

  def write(self, conn):
    sql = 'insert into method (receiver, name, file, startLine, startCol, startOffset, stopLine, stopCol, stopOffset) values (?, ?, ?, ?, ?, ?, ?, ?, ?)'

    curr = conn.cursor()
    curr.execute(sql, (
      self.data['receiver'],
      self.data['name'],
      self.data['file'],
      self.data['startLine'],
      self.data['startCol'],
      self.data['startOffset'],
      self.data['stopLine'],
      self.data['stopCol'],
      self.data['stopOffset']))

    conn.commit()
