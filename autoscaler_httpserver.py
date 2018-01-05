from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, json, time, ast, random
from pprint import pprint
from threading import Thread
from experiment import Experiment 

def add_experiment(experiment_json):
    experiment_id = experiment['experiment_id']
    experiment = Experiment(experiment_json)
    experiment.start()
    experiments[experiment_id] = experiment
    return str(experiment_id) + " has been added successfully\n"

class HTTP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()
        
    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def do_POST(self):
        #pprint(vars(self))
        # Doesn't do anything with posted data
        content_length= None
        data_json = None
        try:
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            data = self.rfile.read(int(content_length)).decode('utf-8')
            data_json = ast.literal_eval(data)
            print(data_json['service_name'])
            pass
        except Exception as e:
            print("Error in parsing the content_length and packet data")
        data_back = ""

        if (self.path == '/experiment/add'):
            print(str(data_json))
            data_back = add_experiment(data_json)
            print("------------------/experiment/add---------------")
        elif (self.path == '/experiment/del'):
            print(str(data_json))
            data_back = experiment_operations.del_experiment(data_json)
            print("------------------/experiment/del---------------")
        
        self._set_headers()
        self.wfile.write(bytes(str(data_back), "utf-8"))


def start(port=81):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HTTP)
    print('Starting Autoscasler HTTP Server ... ' + str(port))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("********************** Error in Autoscasler HTTP Server ")
        pass

    httpd.server_close()
    print(time.asctime(), "Autoscaler HTTP Server Stopped - %s:%s" % (server_address, port))