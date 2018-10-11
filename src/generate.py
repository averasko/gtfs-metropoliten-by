# - *- coding: utf- 8 - *-

import urllib
import re

TEST_URL = "file:input/schedule.html"
URL = "http://metropoliten.by/information/schedule/"

# loading STOPS data
with open('./data/stops.txt', 'r') as file_stops:
  STOP_HEADERS = file_stops.readline().split(',')
  STOPS = map(lambda l: l.rstrip('\r\n').split(','), file_stops.readlines())


def extract_freq(s):
  s = s.replace(",", ".")
  if re.match("[\.0-9]+-[\.0-9]+$", s) or re.match("[\.0-9]+$", s):
    if re.search("-", s):
      pattern = "([\.0-9]+)-([\.0-9]+)$"
      s_ab = re.findall(pattern, s)
      s_from = float(s_ab[0][0])
      s_to = float(s_ab[0][1])
    else:
      s_from = float(s)
      s_to = s_from
    return (s_from, s_to)
  else:
    # note: obviously, that was not a clean check
    # TODO: fix that
    return None

def extract_schedule(url = TEST_URL):
  f = urllib.urlopen(url)
  myfile = f.read()
  #result = re.findall("<td.*\n.*<p.*[0-9]{2}.[0-9]{2}-[0-9]{2}.[0-9]{2}.*</p", myfile)
  elem = ".*<td.*\n.*>(.*)<o.*\n"
  pattern = elem + elem + elem + elem + elem
  return re.findall(pattern, myfile)

def extract_time(s):
  pattern = "([0-9]+)\.([0-9]+)-([0-9]+)\.([0-9]+)"
  #had to adjust regex due to incorrect data on site: '09.00-10-00'
  pattern = "([0-9]+)\.([0-9]+)-([0-9]+)[\.-]([0-9]+)"
  t_ab = re.findall(pattern, s)
  t_from_h = int(t_ab[0][0])
  t_from_m = int(t_ab[0][1])
  t_to_h = int(t_ab[0][2])
  t_to_m = int(t_ab[0][3])
  return (t_from_h, t_from_m, t_to_h, t_to_m)

def apply_on_column(index, func, interval):
  res = []
  for i, col in enumerate(interval):
    if i == index:
      res.append(func(col))
    else:
      res.append(col)
  return res

def apply_extract_time_on_first_column(interval):
  return apply_on_column(0, extract_time, interval)

# OMG OMG!!! need to figure out how to use partially filled functions in py
def apply_on_column_in_list(intervals):
  return list(map(apply_extract_time_on_first_column, intervals))

def split_time(intervals):
  return apply_on_column_in_list(intervals)

def apply_extract_freq_on_oneplus_column(interval):
  interval = apply_on_column(1, extract_freq, interval)
  interval = apply_on_column(2, extract_freq, interval)
  interval = apply_on_column(3, extract_freq, interval)
  interval = apply_on_column(4, extract_freq, interval)
  return interval

# OMG OMG!!! need to figure out how to use partially filled functions in py
def apply_on_column_in_list_2(intervals):
  return list(map(apply_extract_freq_on_oneplus_column, intervals))

def split_freqs(intervals):
  return apply_on_column_in_list_2(intervals)



intervals = extract_schedule()
intervals = split_time(intervals)
intervals = split_freqs(intervals)


for interval in intervals:
  print(interval)


#print(extract_freq("5,0-7.0"))
#print(extract_freq("2,2"))
#print(extract_freq("5-2"))
#print(extract_freq("garbage"))
