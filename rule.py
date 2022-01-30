
import comby
import logging


class Rule:
  """Contains rule information, describing some aspect of the code we want to extract"""

  def log(name: str, match: comby.Match):
    """Log debug information for matched rule data"""

    logging.debug(f"Matched {name}\n\n{match.matched}\n\n")
