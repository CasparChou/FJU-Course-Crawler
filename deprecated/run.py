#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import sys
from BeautifulSoup import BeautifulSoup

url = "http://estu.fju.edu.tw/fjucourse/firstpage.aspx"

payload = "__VIEWSTATE={PASTE_TOKEN_HERE}&__EVENTVALIDATION={PASTE_TOKEN_HERE}&DDL_Class=All-%E5%85%A8%E9%83%A8&But_Run=%E6%9F%A5%E8%A9%A2%EF%BC%88Search%EF%BC%89&DDL_Avadpt="+sys.argv[2]+"&DDL_AvaDiv="+sys.argv[1]
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

parsed_html = BeautifulSoup( response.text )
table_body = parsed_html.find('table', {'id':'GV_CourseList'})
rows = table_body.findAll('tr',recursive=False)
data = []
i = 0
target = open("/absolute/path/to/sql/%s/%s.sql"%(sys.argv[1], sys.argv[2]), 'w')
target.write("INSERT INTO Course VALUES \n")
for row in rows:
    course = []
    skip = 1
    cols = row.findAll('td')
    for ele in cols:
        if skip > 0:
            skip -= 1
            continue
        if ele.find('table'):
            for d in ele.findAll("span") :
                remove = u"(最(高|低)年級|分發優先順序|開放|外系|屬性|拒退年級|領域|學群|專長)："
                if re.compile(remove).search(d.text) :
                    continue
                course.append( d.text.strip().replace("'", "\\'") )
            skip = len(ele.findAll('td'))
            continue
        course.append(ele.text.strip().replace("&nbsp;", "").replace("'", "\\'"))
    write = ("('%s')") if i == 0 else (",\n('%s')")
    if len(course) > 0 :
        target.write(write%"','".join(course).encode('utf-8'))
        data.append(course)
        i += 1
target.write(";\n")
target.close()

#for d in data:
#    print d
#print sys.argv
