import urllib.request
import requests
import re, os

def get_file(url):
 if isFile(url):
  print(url)
  try:
   download(url)
  except:
   pass
 else:
  urls = get_url(url)
  for u in urls:
   get_file(u)

def isFile(url):
 if url.endswith('/'):
  return False
 else:
  return True

def download(url):
   full_name = url.split('//')[-1]
   filename = full_name.split('/')[-1]
   dirname = "/".join(full_name.split('/')[:-1])
   if os.path.exists(dirname):
    pass
   else:
    os.makedirs(dirname, exist_ok=True)
   urllib.request.urlretrieve(url, full_name)

def get_url(base_url):
    text = ''
    try:
     text = requests.get(base_url).text
    except Exception as e:
     print("error - > ",base_url,e)
     pass
    reg = '<a href="(.*)" rel="external nofollow" >.*</a>'
    urls = [base_url + url for url in re.findall(reg, text) if url != '../']

    return urls

if __name__ == '__main__':
    get_file('*')
