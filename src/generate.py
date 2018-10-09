import urllib
import re

TEST_URL = "file:../input/schedule.html"
URL = "http://metropoliten.by/information/schedule/"



def extract_schedule(url = TEST_URL):
  f = urllib.urlopen(url)
  myfile = f.read()
  #result = re.findall("<td.*\n.*<p.*[0-9]{2}.[0-9]{2}-[0-9]{2}.[0-9]{2}.*</p", myfile)
  elem = ".*<td.*\n.*>(.*)<o.*\n"
  pattern = elem + elem + elem + elem + elem
  result = re.findall(pattern, myfile)
  print(result)


extract_schedule()
