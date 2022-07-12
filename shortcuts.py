import yaml
import logging

class Shortcuts():

  def __init__(self, filename):
    logging.warning("Loading shortcuts file '%s'" % filename)
    with open(filename) as stream:
      shortcuts = yaml.safe_load(stream)
    self.shortcuts = {shorturl.lower(): url for shorturl, url in shortcuts.items()}

  def lookup_shorturl(self, shorturl):
    return self.shortcuts.get(shorturl.lower(), self.shortcuts['default'])
