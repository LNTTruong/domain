from prometheus_client import start_http_server
from prometheus_client import Gauge

class Prometheus():

    def __init__(self):
        start_http_server(8000)
        self.g = Gauge('sensor_data', 'Value gathered by sensor', ['domain', 'cat'])

    def get_promethus(self, domain, cat, value):
        print("===========================")
        self.g.labels(domain, cat).set(value)