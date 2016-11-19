
from nova.compute import monitors


class _MyDriver(object):

    def get_metric_free(self, **kwargs):
        return 3213

    def get_metric_percent(self, **kwargs):
        return 0.35

    def get_metric_used(self, **kwargs):
        return 5783

    def get_USB(self, **kwargs):
        return True



class MetricMonitor(monitors.ResourceMonitorBase):
    """Metric monitor."""

    def __init__(self, parent):
        super(MetricMonitor, self).__init__(parent)
        self.source = "My source"
        self.mdriver = _MyDriver()

    def _get_metric_free(self, **kwargs):
        """Return free metric and its timestamp."""
        return self.mdriver.get_metric_free(), None

    def _get_metric_percent(self, **kwargs):
        """Return metric usage and its timestamp."""
        return self.mdriver.get_metric_percent(), None

    def _get_metric_used(self, **kwargs):
        """Return metric used and its timestamp."""
        return self.mdriver.get_metric_used(), None

    def _get_USB(self, **kwargs):
        """Return metric USB and its timestamp."""
        return self.mdriver.get_USB(), None
