
class RuleSet:

  @classmethod
  def matches(cls, fpath: str, content: str):
    for rule in cls.rules:
      for match in rule.matches(fpath, content):
        yield match
