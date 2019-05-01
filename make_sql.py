import sys
import re

workId = 0
phrase = ''
url = ''
sql = ''

if (len(sys.argv) > 1):
    workId = sys.argv[1]
    print('# work_id: ' + workId)
else:
    print('# Please put work_id as argument')

draft = open("draft.txt", "r")
out = open("InsertQuote.ddl", "w")

for line in draft.read().splitlines():
    if 'http' in line:
        url = line
    else:
        phrase = line
        continue

    # Format: INSERT INTO quote(phrase_org, speaker, category_id, work_id, image_url) values('', '', , workId, '');
    sql = 'INSERT INTO quote(phrase_org, speaker, category_id, work_id, image_url) values(\'' + phrase + '\', \'\', , ' + workId + ', \'' + url + '\');\n'

    out.write(sql)
    
draft.close()
out.close()

