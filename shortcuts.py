import yaml
import logging

class Shortcuts():

  def __init__(self, filename):
    with open(filename) as stream:
      logging.warning("Loading shortcuts file '%s'" % filename)
      self.shortcuts = {x.lower(): y for x, y in yaml.load(stream).items()}

  def lookup_shorturl(self, shorturl):
    return self.shortcuts.get(shorturl, self.shortcuts['default'])
