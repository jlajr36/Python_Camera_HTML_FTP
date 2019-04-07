import urllib2
response = urllib2.urlopen('http://worldclockapi.com/api/json/est/now')
html = response.read()
splitData = html.split(',')
_dateTime = splitData[1]
print _dateTime
