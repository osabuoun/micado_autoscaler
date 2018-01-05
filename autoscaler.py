from pprint import pprint
from threading import Thread
import prometheus_getter
import autoscaler_httpserver

experiments = {}

prometheus_protocol = 'http'
prometheus_ip       = '127.0.0.1'
prometheus_port     = 9090

if __name__ == '__main__':
    autoscaler_http_server_thread = Thread(target = autoscaler_httpserver.start, args = (experiments, port))
    autoscaler_http_server_thread.start()

    prometheus_getter_thread = Thread(target = prometheus_getter.start, 
        args = (prometheus_protocol, prometheus_ip, prometheus_port, experiments)
        )
    prometheus_getter_thread.start()
