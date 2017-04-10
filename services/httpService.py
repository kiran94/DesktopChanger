import urllib2

# Service for HTTP services.
class httpService:

    # GET the document from the URL. 
    def get(self, url):
        return urllib2.urlopen(url).read()
