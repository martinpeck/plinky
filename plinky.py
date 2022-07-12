from flask import Flask, render_template, url_for, redirect
import logging
import os
from shortcuts import Shortcuts
from tracking import TrackingHelper
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

shortcuts = Shortcuts(os.environ['SHORTCUT_FILE'])
tracking = TrackingHelper(os.environ.get('SEGMENT_WRITE_KEY', ""))

@app.route("/", methods=['GET'])
@app.route("/<path:shorturl>", methods=['GET'])
def redirect_to_short_url(shorturl=""):
  tracking.track_redirect(shorturl)
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
    app.run()
