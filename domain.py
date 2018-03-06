from urlparse import urlparse

def getDomainName(url):
    try:
        results = getSubdomainName(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# get subdomain name
def getSubdomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return 'urlparse error'

# print('Test - getDomainName()')
# print(getDomainName("http://www.impactsignsusa.com/one/two/three.html"))
