
from rule import RuleMatch


class DependencyRuleMatch(RuleMatch):
  props = {
    'packages',
    'file'
  }

  def create_table(self, conn):
    sql = '''
    create table if not exists dependency (
      name    string not null,
      file    string not null,

      primary key(name, file)
    );
    '''
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

  def write(self, conn):
    sql = 'insert or replace into dependency (name, file) values (?, ?)'

    curr = conn.cursor()
    for pkg in self.data['packages']:
      curr.execute(sql, (
        pkg,
        self.data['file']))

    conn.commit()
