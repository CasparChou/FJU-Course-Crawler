#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as req
import re
from resource.fju import *  
from BeautifulSoup import BeautifulSoup as b4

url = 'http://estu.fju.edu.tw/fjucourse/firstpage.aspx'


default = {
    "enter": "__VIEWSTATE=%2FwEPDwUKMTU0NTI1Njk5MQ9kFgICAQ9kFhICAw9kFgQCCw8PFgIeBFRleHRlZGQCDQ8PFgIfAGVkZAIFDw8WAh4HVmlzaWJsZWhkFgoCAQ8QZGQWAWZkAgMPEGRkFgBkAgUPEGRkFgBkAhkPEGRkFgFmZAIbDxBkZBYBZmQCBw8PFgIfAWhkZAIJDw8WAh8BaGRkAgsPDxYCHwFoZBYEAgEPEGRkFgFmZAIDDxBkZBYAZAINDw8WAh8BaGQWAgIBDxBkZBYBZmQCDw8PFgIfAWhkZAIRDw8WAh8BaGRkAhMPDxYCHwFoZBYCAgEPPCsAEQEBEBYAFgAWAGQYAQUNR1ZfQ291cnNlTGlzdA9nZObFde%2B4KS3U%2F3AnwPa%2BuKR65n0C475E6DGiNL56tJvy&__EVENTVALIDATION=%2FwEWBgLQ%2FKWNDQLvlZj3DAL%2B36urBAKC4OLACgLP5%2FC0CAK60JC3A0Phg6W8LnIibEeGN5nu3B20gwAf1K8wRNXkOzzw%2BcwC&But_BaseData=%25E4%25BE%259D%25E5%259F%25BA%25E6%259C%25AC%25E9%2596%258B%25E8%25AA%25B2%25E8%25B3%2587%25E6%2596%2599%25E6%259F%25A5%25E8%25A9%25A2",
    "search": "__VIEWSTATE=%2FwEPDwUKMTU0NTI1Njk5MQ9kFgICAQ9kFhICAw9kFgQCCw8PFgIeBFRleHRlZGQCDQ8PFgIfAAUEQmFzZWRkAgUPDxYCHgdWaXNpYmxlZ2QWBgIBDxBkZBYBAgFkAgMPEA8WBh4NRGF0YVRleHRGaWVsZAUGRHB0Q25hHg5EYXRhVmFsdWVGaWVsZAUFRHB0Tm8eC18hRGF0YUJvdW5kZ2QQFVkKQWxsLeWFqOmDqBIwMS3kuK3lnIvmloflrbjns7sPMDIt5q235Y%2By5a2457O7DDAzLeWTsuWtuOezuxUwRS3kvIHmpa3nrqHnkIblrbjns7seMEYt6YeR6J6N6IiH5ZyL6Zqb5LyB5qWt5a2457O7JDBMLeWkqeS4u%2BaVmeeglOS%2FruWtuOWjq%2BWtuOS9jeWtuOeoizAwVi3mlZnogrLpoJjlsI7oiIfnp5HmioDnmbzlsZXlrbjlo6vlrbjkvY3lrbjnqIswMFct6Yar5a246LOH6KiK6IiH5Ym15paw5oeJ55So5a245aOr5a245L2N5a2456iLFTEwLeWcluabuOizh%2BioiuWtuOezuxUxMS3lvbHlg4%2FlgrPmkq3lrbjns7sVMTIt5paw6IGe5YKz5pKt5a2457O7FTEzLeW7o%2BWRiuWCs%2BaSreWtuOezuxsxNi3pq5TogrLlrbjns7vpq5TogrLlrbjntYQeMTct6auU6IKy5a2457O76YGL5YuV56u25oqA57WEJDE4LemrlOiCsuWtuOezu%2BmBi%2BWLleWBpeW6t%2BeuoeeQhue1hC0xOS3pm7vmqZ%2Flt6XnqIvlrbjns7vns7vntbHoiIfmmbbniYfoqK3oqIjntYQVMjAt6Iux5ZyL6Kqe5paH5a2457O7FTIyLeazleWci%2BiqnuaWh%2BWtuOezuxgyMy3opb%2Fnj63niZnoqp7mloflrbjns7sVMjQt5pel5pys6Kqe5paH5a2457O7GDI1Lee%2BqeWkp%2BWIqeiqnuaWh%2BWtuOezuxUyNi3lvrfoqp7oqp7mloflrbjns7sYMzAt5pW45a2457O757SU5pW45a2457WEGzMxLeaVuOWtuOezu%2BaHieeUqOaVuOWtuOe1hAwzMy3ljJblrbjns7sPMzkt5b%2BD55CG5a2457O7JDQ2Lee5lOWTgeacjeijneWtuOezu%2Be5lOWTgeioreioiOe1hCo0OC3nuZTlk4HmnI3oo53lrbjns7vnuZTlk4HmnI3po77ooYzpirfntYQVNTEt6LOH6KiK5bel56iL5a2457O7EjU0LeeUn%2BWRveenkeWtuOezuxg1NS3niannkIblrbjns7vniannkIbntYQeNTYt54mp55CG5a2457O75YWJ6Zu754mp55CG57WEFTU3LemkkOaXheeuoeeQhuWtuOezuxg1OC3lhZLnq6XoiIflrrbluq3lrbjns7sPNjMt56S%2B5pyD5a2457O7FTY0Leekvuacg%2BW3peS9nOWtuOezuw82NS3ntpPmv5%2Flrbjns7sPNjYt5rOV5b6L5a2457O7FTY3Leiyoee2k%2BazleW%2Bi%2BWtuOezuxg2OC3lrbjlo6vlvozms5Xlvovlrbjns7skNjkt57mU5ZOB5pyN6KOd5a2457O75pyN6aO%2B6Kit6KiI57WEDzcxLeacg%2BioiOWtuOezuxU3NC3os4foqIrnrqHnkIblrbjns7sVNzYt57Wx6KiI6LOH6KiK5a2457O7DzgwLemfs%2BaoguWtuOezuxU4MS3mh4nnlKjnvo7ooZPlrbjns7sVODIt5pmv6KeA6Kit6KiI5a2457O7Ejg1Lemjn%2BWTgeenkeWtuOezuxI4Ni3nh5%2FppIrnp5Hlrbjns7sPOTAt5a6X5pWZ5a2457O7DzkxLeitt%2BeQhuWtuOezuxU5Mi3lhazlhbHooZvnlJ%2Flrbjns7sMOTQt6Yar5a2457O7FTk1LeiHqOW6iuW%2Fg%2BeQhuWtuOezuxU5Ni3ogbfog73msrvnmYLlrbjns7sVOTgt5ZG85ZC45rK755mC5a2457O7LTk5Lembu%2Bapn%2BW3peeoi%2BWtuOezu%2Bmbu%2BiFpuiIh%2BmAmuioiuW3peeoi%2Be1hBZLMDUt6Zu75a2Q5ZWG5YuZ5a2456iLE0swOS3ogIHkurrlrbjlrbjnqIsWSzEyLeiLseiqnuiPgeiLseWtuOeoix9LMTgt5aSW5Lqk6IiH5ZyL6Zqb5LqL5YuZ5a2456iLHEsxOS3lsI3lpJboj6%2Foqp7mlZnlrbjlrbjnqIslSzI3LeatkOebn%2BiqnuiogOiIh%2BaWh%2BWMlueglOeptuWtuOeoixxLMjgt6Zuy56uv5pyN5YuZ6Lao5Yui5a2456iLNEszMC3phqvlrbjlt6XnqIvlrbjliIblrbjnqIsgICAgICAgICAgICAgICAgICAgICAgICA1SzMzLeenkeaKgOeUoualreWMluWtuOWIhuWtuOeoiyAgICAgICAgICAgICAgICAgICAgICA3SzM0LTNE5YiX5Y2w6Kit6KiI6IiH5oeJ55So5a245YiG5a2456iLICAgICAgICAgICAgICAgIDdLMzct5aSn5pW45pOa55Si5qWt5pm65oWn5a245YiG5a2456iLICAgICAgICAgICAgICAgICAgOEs0MC3li5XmhYvos4foqIroppboprroqK3oqIjlrbjliIblrbjnqIsgICAgICAgICAgICAgICAgD0FULemrlOiCsuiqsueoiwlDVC3lnIvmlocVRSAt5pWZ6IKy5a2456iL6Kqy56iLD0VULeWwiOalreWAq%2BeQhg9GVC3lpJboqp7oqrLnqIsPSVQt5aSn5a245YWl6ZaAD0xDLeiLseiBveiqsueoiw9MVC3kurrnlJ%2Flk7LlrbghTlQt6Ieq54S256eR5oqA6aCY5Z%2Bf6YCa6K2Y6Kqy56iLIVBULeS6uuaWh%2BiXneihk%2BmgmOWfn%2BmAmuitmOiqsueoiyFTVC3npL7mnIPnp5HlrbjpoJjln5%2FpgJrorZjoqrLnqIsSQ0ct5paH5a246Zmi6Kqy56iLFUZHLeWkluiqnuWtuOmZouiqsueoixVIRy3msJHnlJ%2FlrbjpmaLoqrLnqIsVSkct5rOV5b6L5a246Zmi6Kqy56iLFVNHLeeQhuW3peWtuOmZouiqsueoixVXRy3npL7mnIPlrbjpmaLoqrLnqIsVViAt5YWx5ZCM6Iux5paH6Kqy56iLD1lULei7jeiok%2BiqsueoixVZCkFsbC3lhajpg6gCMDECMDICMDMCMEUCMEYCMEwCMFYCMFcCMTACMTECMTICMTMCMTYCMTcCMTgCMTkCMjACMjICMjMCMjQCMjUCMjYCMzACMzECMzMCMzkCNDYCNDgCNTECNTQCNTUCNTYCNTcCNTgCNjMCNjQCNjUCNjYCNjcCNjgCNjkCNzECNzQCNzYCODACODECODICODUCODYCOTACOTECOTICOTQCOTUCOTYCOTgCOTkDSzA1A0swOQNLMTIDSzE4A0sxOQNLMjcDSzI4A0szMANLMzMDSzM0A0szNwNLNDACQVQCQ1QBRQJFVAJGVAJJVAJMQwJMVAJOVAJQVAJTVAJDRwJGRwJIRwJKRwJTRwJXRwFWAllUFCsDWWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnFgECAWQCBQ8QDxYGHwIFCENsYXNzQ25hHwMFB0NsYXNzTm8fBGdkEBUOCkFsbC3lhajpg6gOMDEwMC3kuK3mlofns7sOMDEwMS3kuK3mlofkuIAOMDEwMi3kuK3mlofkuowOMDEwMy3kuK3mlofkuIkOMDEwNC3kuK3mloflm5sRMDExMS3kuK3mlofkuIDnlLIRMDExMi3kuK3mlofkuoznlLIRMDExMy3kuK3mlofkuInnlLIRMDExNC3kuK3mloflm5vnlLIRMDEyMS3kuK3mlofkuIDkuZkRMDEyMi3kuK3mlofkuozkuZkRMDEyMy3kuK3mlofkuInkuZkRMDEyNC3kuK3mloflm5vkuZkVDgpBbGwt5YWo6YOoBDAxMDAEMDEwMQQwMTAyBDAxMDMEMDEwNAQwMTExBDAxMTIEMDExMwQwMTE0BDAxMjEEMDEyMgQwMTIzBDAxMjQUKwMOZ2dnZ2dnZ2dnZ2dnZ2dkZAIHDw8WAh8BaGRkAgkPDxYCHwFoZGQCCw8PFgIfAWhkFgQCAQ8QZGQWAWZkAgMPEGRkFgBkAg0PDxYCHwFoZBYCAgEPEGRkFgFmZAIPDw8WAh8BZ2RkAhEPDxYCHwFoZGQCEw8PFgIfAWhkFgICAQ88KwARAQEQFgAWABYAZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WEAUKQ2hlY2tCb3hfUgUKQ2hlY2tCb3hfUwUKQ2hlY2tCb3hfRwUKQ2hlY2tCb3hfVAUKQ2hlY2tCb3hfVQUKQ2hlY2tCb3hfVwUNQ2hlY2tCb3hfSGFsZgUNQ2hlY2tCb3hfWWVhcgUQQ2hlY2tCb3hfT3V0RmxhZwUMQ2hlY2tCb3hfV0sxBQxDaGVja0JveF9XSzIFDENoZWNrQm94X1dLMwUMQ2hlY2tCb3hfV0s0BQxDaGVja0JveF9XSzUFDENoZWNrQm94X1dLNgUMQ2hlY2tCb3hfV0s3BQ1HVl9Db3Vyc2VMaXN0D2dkNYx0Mq%2Fx9m3n3922OGlvHTExkVc5SG7U08VVQl3uDZQ%3D&__EVENTVALIDATION=%2FwEWpgEC3bfL9w0C75WY9wwC%2Ft%2BrqwQCguDiwAoCz%2BfwtAgCutCQtwMCj5vOyAICn%2FTkpg4C0%2FTkpg4C0vTkpg4C1vTkpg4C4%2FTkpg4ClpvWrQkCnbfSygsChvSwwAUChvS0wAUChvSIwAUChvTA3QUChvTE3QUChvTs3QUChvSE3QUChvSY3QUCmfS8wAUCmfSwwAUCmfS0wAUCmfSIwAUCmfSEwAUCmfSYwAUCmfTcwwUCmfTQwwUCmPS8wAUCmPS0wAUCmPSIwAUCmPSMwAUCmPSAwAUCmPSEwAUCm%2FS8wAUCm%2FSwwAUCm%2FSIwAUCm%2FTQwwUCmvSEwAUCmvTcwwUCnfSwwAUCnfSMwAUCnfSAwAUCnfSEwAUCnfSYwAUCnfTcwwUCnPSIwAUCnPSMwAUCnPSAwAUCnPSEwAUCnPSYwAUCnPTcwwUCnPTQwwUCn%2FSwwAUCn%2FSMwAUCn%2FSEwAUCjvS8wAUCjvSwwAUCjvS0wAUCjvSAwAUCjvSEwAUCgfS8wAUCgfSwwAUCgfS0wAUCgfSMwAUCgfSAwAUCgfSEwAUCgfTcwwUCgfTQwwUCkKb0iQcC1NXqiA0Co5qTyQYCsf7MvQMC1NXuiA0CqpSA4wsCsf7AvQMC6bXXlwICxvGMVAL9yK6jDQKqlITjCwLptauUAgLJ9IzdBQLL9IzdBQLN9PzDBQLN9IzdBQLM9IzdBQLx9IzdBQLy9MjdBQLy9IzdBQL09IzdBQLm9IzdBQL79IzdBQLL9NjdBQLM9NjdBQL%2B9NjdBQLw9NjdBQL79NjdBQL%2F9NjdBQL89PzDBQLh9IzdBQLQtoaiDwLxtMvCDQLxtLfpCgLxtKOUAwLxtI%2BzCALxtPtfAp6N0YQMAp6NvaMFAp6Nqc4NAp6NlfUKArua85MGArua374PAruay%2BUHAruat4AMApTjj70JApTjk70JApTj470JApTjp70JApTjq70JApTjo70JAqSTkNEHAqS4x%2FUOAvmn84MEApHF6%2B4JAs2qgYMFAs2qjYMFAs2qiYMFAs2qtYMFAs2qsYMFAs2q2Z4FAs2qvYMFAs2quYMFAs2qpYMFAs2q4YAFAsqqgYMFAsqqjYMFAsqqiYMFAsqqtYMFAsqqsYMFAoPF6%2B4JAt%2BqgYMFAt%2BqjYMFAt%2BqiYMFAt%2BqtYMFAt%2BqsYMFAt%2Bq2Z4FAt%2BqvYMFAt%2BquYMFAt%2BqpYMFAt%2Bq4YAFAtiqgYMFAtiqjYMFAtiqiYMFAtiqtYMFAtiqsYMFAqydrKsMAqyd6LwGAqyd1OENAqydkPMHAqyd%2FJcPAqyduKkJAqydpE4CrJbJpgYCsJb91A%2FRx5LBvPOUDlOxbpVvRwo3%2B0vSorjzmZ4w%2Br9n%2BGga5Q%3D%3D&But_Run=%E6%9F%A5%E8%A9%A2%EF%BC%88Search%EF%BC%89&",
    "select": "DDL_AvaDiv=%s&DDL_Avadpt=%s"
}

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
}

remove = u"(最(高|低)年級|分發優先順序|開放|外系|屬性|拒退年級|領域|學群|專長)："

def prepare_token():
    
    data = b4( req.request("POST", url, data=default["enter"], headers=headers).text )
    view_state = data.find('input', {'id':'__VIEWSTATE'}).get('value')
    even_vaild =  data.find('input', {'id':'__EVENTVALIDATION'}).get('value') 
    return view_state, even_vaild


def crawler( payload ):

    dom = b4( req.request("POST", url, data=payload, headers=headers).text )
    table = dom.find( 'table', {'id': 'GV_CourseList'} )
    if table:
        rows = table.findAll('tr', recursive=False)
        print " ✅  Gotcha! %s courses founded" % len(rows)
        return rows
    else:
        print " ❌  No courses founded"

def open_file(div, dep):
    return open("/home/caspar/course/sql2/%s/%s.sql"%(div, dep), 'w')
    #return open("/absolute/path/to/sql/%s/%s.sql"%(sys.argv[1], sys.argv[2]), 'w')


def main():
    view_state, even_vaild = prepare_token()

    div2emo = {"D": "☀️️", "C": "🌙", "G": "🎓", "T": "2️⃣"}
    for div in divs:
        for dep in deps[div]:
            print " 🔍  Fetching %s  - %s - %s"%(div2emo[div], dep,  depn[dep])    
            payload = default["search"] + '&' + (default["select"] % (div, dep))
            rows = crawler( payload )  
            line = 0
            f = open_file(div, dep)
            f.write("INSERT INTO Course VALUES \n")
            for row in rows:
                skip, course = 1, []
                cols = row.findAll('td')
                for ele in cols:
                    if skip > 0:
                        skip -= 1
                    elif ele.find('table'):
                        for inner in ele.findAll('span'):
                            if re.compile(remove).search(inner.text) :
                                continue
                            course.append( inner.text.strip().replace("'", "\\'") )
                        skip = len(ele.findAll('td'))
                    else:
                        course.append(ele.text.strip().replace("&nbsp;", "").replace("'", "\\'"))
                if len(course) > 0 :
                    write = ("('%s')") if line == 0 else (",\n('%s')")
                    f.write(write%"','".join(course).encode('utf-8'))
                    line += 1
            f.close
            quit()




if __name__ == '__main__':
    main()


#     for ele in cols:
#         if skip > 0:
#             skip -= 1
#             continue
#         if ele.find('table'):
#             for d in ele.findAll("span") :
#                 remove = u"(最(高|低)年級|分發優先順序|開放|外系|屬性|拒退年級|領域|學群|專長)："
#                 if re.compile(remove).search(d.text) :
#                     continue
#                 course.append( d.text.strip().replace("'", "\\'") )
#             skip = len(ele.findAll('td'))
#             continue
#         course.append(ele.text.strip().replace("&nbsp;", "").replace("'", "\\'"))
#     write = ("('%s')") if i == 0 else (",\n('%s')")
#     if len(course) > 0 :
#         target.write(write%"','".join(course).encode('utf-8'))
#         data.append(course)
#         i += 1
# target.write(";\n")
# target.close()
# 
# 
