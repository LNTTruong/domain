from prometheus_client import start_http_server
from prometheus_client import Gauge
from prometheus_client import Histogram, CollectorRegistry, push_to_gateway, write_to_textfile
import random
import time

class Prometheus():

    def __init__(self):
        start_http_server(8000)
        registry = CollectorRegistry()
        self.lcp_histogram = Histogram('bfmonitor_request_lcp', 'lcp histogram', ['host'], registry=registry)

        self.fcp_histogram = Histogram('bfmonitor_request_fcp', 'fcp histogram', ['host'], registry=registry)
        self.cls_histogram = Histogram('bfmonitor_request_cls', 'cls histogram', ['host'], registry=registry)
        self.ttfb_histogram = Histogram('bfmonitor_request_ttfb', 'ttfb histogram', ['host'], registry=registry)
    #
    #     # self.g_lcp = Gauge(stt + '_lcp', 'Value gathered by sensor_lcp', ['domain','cat'])
    #     # self.g_fcp = Gauge(stt + '_fcp', 'Value gathered by sensor_fcp', ['domain','cat'])
    #     # self.g_cls = Gauge(stt + '_cls', 'Value gathered by sensor_cls', ['domain','cat'])
    #     # self.g_ttfb = Gauge(stt + '_ttfb', 'Value gathered by sensor_ttfb', ['domain','cat'])

    def get_promethus( self, domain, cat, value):
        # registry = CollectorRegistry()
        # lcp_histogram = Histogram('bfmonitor_request_lcp', 'lcp histogram', ['host'], registry=registry)
        #
        # fcp_histogram = Histogram('bfmonitor_request_fcp', 'fcp histogram', ['host'], registry=registry)
        # cls_histogram = Histogram('bfmonitor_request_cls', 'cls histogram', ['host'], registry=registry)
        # ttfb_histogram = Histogram('bfmonitor_request_ttfb', 'ttfb histogram', ['host'], registry=registry)

        print("value %d %d %d",domain, cat, value)
        # time = random.random()
        # self.g_lcp.labels(domain, cat).set(value)
        if cat == "average_lcp":
            self.lcp_histogram.labels(domain).observe(value)
            # g_lcp = Gauge(stt + '_lcp', 'Value gathered by sensor_lcp', ['domain', 'cat'])
            # g_lcp.labels(domain, cat).set(value)
            # self.g_lcp.set_to_current_time(time)
        if cat == "average_fcp":
            self.fcp_histogram.labels(domain).observe(value)
            # g_fcp = Gauge(stt + '_fcp', 'Value gathered by sensor_lcp', ['domain', 'cat'])
            #
            # g_fcp.labels(domain, cat).set(value)
            # self.g_fcp.set_to_current_time(time)
        if cat == "average_cls":
            self.cls_histogram.labels(domain).observe(value)
            # g_cls = Gauge(stt + '_cls', 'Value gathered by sensor_lcp', ['domain', 'cat'])
            #
            # g_cls.labels(domain, cat).set(value)
            # self.g_cls.set_to_current_time(time)
        if cat == "average_ttfb":
            self.ttfb_histogram.labels(domain).observe(value)
            # g_ttfb = Gauge(stt + '_ttfb', 'Value gathered by sensor_lcp', ['domain', 'cat'])
            #
            # g_ttfb.labels(domain, cat).set(value)

            # self.g_ttfb.set_to_current_time(time)



        # self.g.set_function()
        print("===========================")
