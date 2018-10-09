import urllib
import re

TEST_URL = "file:../input/schedule.html"
URL = "http://metropoliten.by/information/schedule/"


def extract_freq(s):
  s = s.replace(",", ".")
  if re.search("-", s):
    pattern = "([\.0-9]*)-([\.0-9]*)"
    s_ab = re.findall(pattern, s)
    s_from = float(s_ab[0][0])
    s_to = float(s_ab[0][1])
  else:
    s_from = float(s)
    s_to = s_from
  return (s_from, s_to)


def extract_schedule(url = TEST_URL):
  f = urllib.urlopen(url)
  myfile = f.read()
  #result = re.findall("<td.*\n.*<p.*[0-9]{2}.[0-9]{2}-[0-9]{2}.[0-9]{2}.*</p", myfile)
  elem = ".*<td.*\n.*>(.*)<o.*\n"
  pattern = elem + elem + elem + elem + elem
  result = re.findall(pattern, myfile)
  print(result)


#extract_schedule()
print(extract_freq("5,0-7.0"))
print(extract_freq("2,2"))
print(extract_freq("5-2"))
