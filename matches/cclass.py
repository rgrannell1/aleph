

from rule_match import RuleMatch



class ClassRuleMatch(RuleMatch):
  props = {
    'name',
    'file',
    'extends',
    'location'
  }


  def create_table(self, conn):
    sql = '''
    create table if not exists class (
      name        string not null,
      file        string not null,
      extends     string not null,
      startLine   integer,
      startCol    integer,
      startOffset integer,
      stopLine    integer,
      stopCol     integer,
      stopOffset  integer,

      primary key(name, file)
    );
    '''
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

  def write(self, conn):
    sql = 'insert or replace into class (name, file, extends, startLine, startCol, startOffset, stopLine, stopCol, stopOffset) values (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    loc = self.data['location']

    curr = conn.cursor()
    curr.execute(sql, (
      self.data['name'],
      self.data['file'],
      self.data['extends'],
      loc.start.line,
      loc.start.col,
      loc.start.offset,
      loc.stop.line,
      loc.stop.col,
      loc.stop.offset))

    conn.commit()
