import threading
from Queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'gpxdb'
HOME_PAGE = 'http://gpxdb.com'
DOMAIN_NAME = getDomainName(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 1
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

# Create worker threads
def createWorkers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()

def createJobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check the queue, if so, crawl them.
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links to crawl.')
        createJobs()

print('Starting....')
createWorkers()
crawl()
