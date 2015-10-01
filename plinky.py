from flask import Flask, render_template, url_for, redirect
import logging
import analytics
import os
from shortcuts import Shortcuts

app = Flask(__name__)

analytics.write_key = os.environ.get('SEGMENT_WRITE_KEY', '')
shortcut_file = os.environ['SHORTCUT_FILE']

shortcuts = Shortcuts(shortcut_file)

@app.route("/", methods=['GET'])
@app.route("/<path:shorturl>", methods=['GET'])
def redirect_to_short_url(shorturl=""):

  analytics.track('plinky-server', 'redirect_to_short_url', {
    'shorturl': shorturl
  })

  return redirect(shortcuts.lookup_shorturl(shorturl), 301)

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
