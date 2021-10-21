from prometheus_client import start_http_server
from prometheus_client import Gauge

class Prometheus():

    def __init__(self):
        start_http_server(8000)
        self.g_lcp = Gauge('sensor_data_lcp', 'Value gathered by sensor_lcp', ['domain', 'cat'])
        self.g_fcp = Gauge('sensor_data_fcp', 'Value gathered by sensor_fcp', ['domain', 'cat'])
        self.g_cls = Gauge('sensor_data_cls', 'Value gathered by sensor_cls', ['domain', 'cat'])
        self.g_ttfb = Gauge('sensor_data_ttfb', 'Value gathered by sensor_ttfb', ['domain', 'cat'])

    def get_promethus(self, domain, cat, value):
        print("value %d %d %d",domain, cat, value)
        if cat == "average_lcp":
            self.g_lcp.labels(domain, cat).set(value)
        if cat == "average_fcp":
            self.g_fcp.labels(domain, cat).set(value)
        if cat == "average_cls":
            self.g_cls.labels(domain, cat).set(value)
        if cat == "average_ttfb":
            self.g_ttfb.labels(domain, cat).set(value)



        # self.g.set_function()
        print("===========================")
