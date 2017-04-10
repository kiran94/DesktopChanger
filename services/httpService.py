import urllib2

# Service for HTTP services.
class httpService:

    # GET the document from the URL. 
    def get(self, url):
        headers = { 'User-Agent' : 'Mozilla/5.0' }
        req = urllib2.Request(url, None, headers)
        return urllib2.urlopen(req).read()
