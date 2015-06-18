from flask import Flask
from flask import render_template, url_for, redirect
import logging
import yaml
import analytics
import os

app = Flask(__name__)

analytics.write_key = os.environ['SEGMENT_WRITE_KEY']

def load_shorturls():
  with open('./shorturls/shorturls.yaml') as stream:
    doc = yaml.load(stream)
  return doc

def lookup_shorturl(shorturl):
  shortcuts = load_shorturls()
  return redirect(shortcuts.get(shorturl, shortcuts['default']), 302)

@app.route("/", methods=['GET'])
@app.route("/<path:shorturl>", methods=['GET'])
def plinky(shorturl=None):

  analytics.track('plinky-server', 'Redirect Short URL', {
    'shorturl': shorturl
  })

  return lookup_shorturl(shorturl)

@app.route("/discover", methods=['GET'])
def discover():
  return render_template('discover.html')

@app.route("/stats", methods=['GET'])
def stats():
  return  render_template('stats.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

if __name__ == "__main__":
    app.debug = True
    analytics.debug = True;
    app.run()
