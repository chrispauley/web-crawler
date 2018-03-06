# This will share the queue and crawled files.
# spider.py
import urllib2
from link_finder import LinkFinder
from general import *


class Spider:
    projectName = ''
    baseUrl = ''
    domainName = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queue_file = Spider.projectName + '/queue.txt'
        Spider.crawled_file = Spider.projectName + '/crawled.txt'
        Spider.queue = set()
        Spider.crawled = set()
        # super().__init__()
        self.boot()
        self.crawlPage('First Spider', Spider.baseUrl)

    # @staticmethod
    def boot(self):
        create_project(Spider.projectName)
        create_data_files(Spider.projectName, Spider.baseUrl)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled_file = file_to_set(Spider.crawled_file)
        print('Boot - Queue ' + str(len(Spider.queue)) + ' | Crawled: ' + str(len(Spider.crawled)))

    @staticmethod
    def crawlPage(threadName, pageUrl):
        if pageUrl not in Spider.crawled:
            print(threadName + ' now crawling: ' + pageUrl)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled: ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gatherLinks(pageUrl))
            Spider.crawled.add(pageUrl)
            print(Spider.crawled)
            append_to_file(Spider.crawled_file, pageUrl)
            Spider.queue.discard(pageUrl)
            set_to_file(Spider.queue, Spider.queue_file)

            # Spider.updateFiles()

    @staticmethod
    def gatherLinks(pageUrl):
        htmlString = ''
        try:
            request = urllib2.Request(pageUrl)
            request.add_header('User-Agent', 'My python spider')
            request.add_header('Referer', 'the refererer')
            response = urllib2.urlopen(request)
            header = response.info().getheader('Content-Type')
            if header == 'text/html':
                htmlBytes = response.read()
                htmlString = htmlBytes.decode('utf-8')
            finder = LinkFinder(Spider.baseUrl, pageUrl)
            finder.feed(htmlString)
        except Exception as e:
            print('Error: cannot crawl the page ' + pageUrl)
            print(str(e))
            return set()
        return finder.pageLinks()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domainName != getDomainName(url):
                continue
            Spider.queue.add(url)
        print('links: ' + str(len(links)))
        print('Spider.queue: ' + str(len(Spider.queue)))

    @staticmethod
    def updateFiles():
        # print('updateFiles() set_to_file(queue, queue_file): ')
        # print(Spider.queue)
        # print(Spider.queue_file)
        qf = Spider.queue_file
        set_to_file(Spider.queue, qf)
        # print('set_to_file(crawled, Spider.crawled_file): ')
        # print(Spider.crawled)
        print(type(Spider.crawled_file))
        cf = Spider.crawled_file
        set_to_file(Spider.crawled, cf)

    def error(self, message):
        pass

spider = Spider("guggersgutters", "http://guggersgutters.com", "guggersgutters.com")

print('done')
