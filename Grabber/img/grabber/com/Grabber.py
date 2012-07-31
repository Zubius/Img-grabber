import urllib2, os
from HTMLParser import HTMLParser

proxy = {}
proxy_handler = urllib2.ProxyHandler(proxy)
some_url = 'http://facepaw.ru/uploads/'
path = 'booksimg/'
if not os.path.exists(path):
        os.makedirs(path)
rawdata = ''

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        data = data.replace('Index of /uploads', '')
        data = data.replace('Parent Directory', '')
        data = data.replace(' ', '')
        print '\'' + data + '\''
        if data != '' and data != '\n':
            downimg(some_url, data)
            return data
    
def takeimg():
        opener = urllib2.build_opener(proxy_handler)
        response = opener.open(some_url)
        html = response.read()
        return html

def downimg(some_url, img_url):
        img = some_url+img_url
        print img
        
        img_opener = urllib2.build_opener(proxy_handler)
        page = img_opener.open(img)
        my_img = page.read()
        
        local_file = path+img_url
        print local_file
        fout = open(local_file, "wb")
        fout.write(my_img)
        fout.close()


parser = MyHTMLParser()
rawdata = takeimg()
parser.feed(rawdata)
