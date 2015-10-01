import analytics
import logging

class TrackingHelper():

  def __init__(self, key):
    if key != "":
      self.tracking_enabled = True
      analytics.write_key = key
      logging.warning("Tracking Enabled")
    else:
      self.tracking_enabled = False
      logging.warning("Tracking Disabled")

  def track_redirect(self, shorturl):
    if self.tracking_enabled:
        analytics.track('plinky-server', 'redirect_to_short_url', {
          'shorturl': shorturl
        })
