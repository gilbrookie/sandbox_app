
import argparse
import logging
import multiprocessing
import requests
import time

from datetime import datetime

description = u"Load_gen2 - HTTP/HTTPS traffic generator"


use_ssl = False
use_proxy = False
poll_interval = 0.2

default_host = 'httpbin.org'
default_run_time = 10  # 30s

"""
stats = {   
    transaction:    None,
    hit_rate:       None, 
    elapsed_time:   None, 
    data_sent:      None,
    avg_response_t: None,
    throughput:     None,
    concurrency:    None,
    success:        None,
    failed:         None,
    longest:        None,
    shortest:       None,
}
"""

class LoadManager(object):
    def __init__(self, config):
        self.conf = config
        self.jobs_q = multiprocessing.JoinableQueue()
        self.results_q = multiprocessing.Queue()
        self.raw_results = []

        num_threads = 1 # default
        
        # A flag used to interrupt execution
        self.stop_event = False

    def start(self):
        self.start_time = time.time()

        num_threads = multiprocessing.cpu_count() * 1
        agents = [ LoadAgent(self.jobs_q, self.results_q)
                     for i in xrange(num_threads) ]

        for a in agents:
            a.start()

        if not conf.run_time:
            enum_exec()
        else:
            timed_exec()

        collect_results()
        


    def collect_results(self):
        while not self.results_q.empty():
            res = self.results_q.get()
            self.raw_results.append(res)


    def timed_exec(self):

        while int((time.time() - self.start_time)) <= int(self.conf.run_time):
    
            if self.stop_event:
                break

            print int((time.time() - self.start_time)), self.conf.run_time 
            print int((time.time() - self.start_time)) < int(self.conf.run_time)

            self.jobs_q.put(RequestTask(self.conf))
            
            time.sleep(poll_interval)

    def enum_exec(self):

        for n in xrange(num_exec):
            
            if self.stop_event:
                break

            print n, num_exec

            self.jobs_q.put(RequestTask(self.conf))
            
            time.sleep(poll_interval)


    def interrupt_exec():
        for i in xrange(num_threads):
            self.jobs_q.put(None)

        self.jobs_q.join()

class ResultsProcessor(object):
    def __init__(self, raw):
        self.raw = raw

    def start(self):
        stats = {}

        stats['transactions'] = self.calc_transactions()
        stats['elapsed_time'] = self.calc_elapsed_time()
        stats['avg_time'] = self.calc_average_time()

    def calc_transactions(self):
        return len(self.raw)

    def calc_elapsed_time(self):
        sort = lambda date: self.raw[2]['date']
        start = min(self.raw, key=sort)
        end = max(self.raw, key=sort)
        
        return (end-start)

    def calc_average_time(self): 

        return reduce(lambda x, y:x+y, self.raw[0]) / len(self.raw)



class LoadAgent(multiprocessing.Process):
    """Send Request, record stats"""
    def __init__(self, task_queue, results_queue):
        multiprocessing.Process.__init__(self)
        self.tasks = task_queue
        self.results = results_queue

    def run(self):
        proc_name = self.name
        while True:

            next_task = self.tasks.get()
            #if isinstance(next_task, KillTask):
            if next_task is None:
                print "%s: Exiting" % proc_name
                self.tasks.task_done()
                break

            print "%s: %s" % (proc_name, next_task)

            # Call the RequestTask
            #if next_task:
            result = next_task()
    
            self.tasks.task_done()
            self.results.put(result)


class RequestTask(object):
    def __init__(self, config ):
        self.conf = config

    def __call__(self):
        #return self.do_request(conf)
        print "RequestTask Execute!"
        return self.do_request(self.conf)

    def do_request(self, conf):
   
        print conf
    
        start = time.clock()
        # build the request object
        r = requests.request( conf.method,
                              conf.url, 
                              proxies={"http":conf.proxy})
        end = time.clock()
        latency = (end - start)

        return (latency, r.status_code, r.headers)

def load_config(conf_file):
    pass

def main(args):
    print args

    print vars(args)
    l = LoadManager(args)
    l.start()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("url", type=str, 
                        help="The address of the destination, or a list of urls from file (one url per line)")

    parser.add_argument("-c", action="store", dest="config_file",
                        help="load configuration from file")

    parser.add_argument("-m", action="store", dest="method", 
                        help="selected HTTP method")

    parser.add_argument("-n", action="store", dest="threads",
                        help="Number of threads used")
    
    parser.add_argument("-l", action="store", dest="log_file",
                        help="write output to log_file")
    
    parser.add_argument("--time", 
                        action="store", 
                        dest="run_time",
                        default=default_run_time,
                        help="Execution time of the test (seconds)")

    parser.add_argument("--proxy", action="store", dest="proxy", 
                        help="Send request through proxy (http://host:port" )
    
    parser.add_argument("-v", action="store_true", default=False, 
                        help="show verbose messages" )                    

    main(parser.parse_args())



"""
optional args:
    - -h:host
    - -u:urls (list from file)
    - -m:method (GET/POST/PUT, etc...)
    - -n:threads
    - -t:run_time
    - -v:verbose
    - -l:log
    - -c:config


Config File

run_time=
threads=
proxy=
timeout=
urls = [
    {   url: "http://httpbin.org", 
        method: "GET", 
        headers:{user-agent:"test"},
        post_data:{},
        proxy: "10.168.100.157:8080",
        ssl_cert: "cert_file"
    }
    {   url: "huffingtonpost.com/sports/",
]


"""


