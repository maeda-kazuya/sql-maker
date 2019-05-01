#! /anaconda3/bin/python
import sys
import re

#print ('Hello')
if (len(sys.argv) > 1): 
    print('# arg: ' + sys.argv[1])

draft = open("draft.txt", "r")
out = open("InsertQuote.ddl", "w")

phrase = ''
url = ''
sql = ''

# 一行ずつ読み込んでは表示する
#for line in draft:
for line in draft.read().splitlines():
    if 'http' in line:
        url = line
#        url = line.rstrip('\n')
    else:
        phrase = line
#        phrase = line.rstrip('\n')
        continue

    sql = 'INSERT INTO quote(phrase_org, speaker, category_id, work_id, image_url) values(\'' + phrase + '\', \'\', , 100, \'' + url + '\');\n'

    out.write(sql)
    

#out.write(sql)    

# ファイルをクローズする
draft.close()
out.close()


# INSERT INTO quote(phrase_org, speaker, category_id, work_id, image_url) values('', '', , 100, '');
