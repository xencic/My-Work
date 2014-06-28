__author__ = 'xeniasaptefrati'


import urllib2
import MySQLdb, sys
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="newyork",
                  db="dataLinks")
x = conn.cursor()

file = open('urls.txt').read()
listUrls = file.split(',')
# print listUrls

allUrls = ''
for each_item in listUrls: # one url , or one item form the list
   contents = urllib2.urlopen(each_item).read()#one url at one time
   allUrls+=  "/n" + contents
   # print allUrls

file = open('tags.txt').read()
listTag = file.split(',')
# print listTag




try:

    for eachTag in listTag:
     count = allUrls.count(eachTag)
    # print eachTag , count
     query = """INSERT INTO allTags (tags_name,tags_number) VALUES ('%s',%d)""" %(eachTag,count)
     print query
     x.execute(query)
     conn.commit()

except :
  print "Oops!  That was no valid .  Try again..."
conn.close()