import yaml
import logging

class Shortcuts():

  def __init__(self, filename):
    with open(filename) as stream:
      logging.warning("Loading shortcuts file '%s'" % filename)
      self.shortcuts = yaml.load(stream)

  def lookup_shorturl(self, shorturl):
    return self.shortcuts.get(shorturl, self.shortcuts['default'])
