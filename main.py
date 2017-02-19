#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as req
import re
from resource.fju import *  
from BeautifulSoup import BeautifulSoup as b4

url = 'http://estu.fju.edu.tw/fjucourse/secondpage.aspx'


default = {
    "enter":"__VIEWSTATE=%2FwEPDwUKMTU0NTI1Njk5MQ9kFgICAQ9kFhICAw9kFgQCCw8PFgIeBFRleHRlZGQCDQ8PFgIfAGVkZAIFDw8WAh4HVmlzaWJsZWhkFgoCAQ8QZGQWAWZkAgMPEGRkFgBkAgUPEGRkFgBkAhkPEGRkFgFmZAIbDxBkZBYBZmQCBw8PFgIfAWhkZAIJDw8WAh8BaGRkAgsPDxYCHwFoZBYEAgEPEGRkFgFmZAIDDxBkZBYAZAINDw8WAh8BaGQWAgIBDxBkZBYBZmQCDw8PFgIfAWhkZAIRDw8WAh8BaGRkAhMPDxYCHwFoZBYCAgEPPCsAEQEBEBYAFgAWAGQYAQUNR1ZfQ291cnNlTGlzdA9nZM%2FgNCX%2Bxqpki4HzOdFyDD4ZXaVNC3FQH6H2lBI4rQ8J&__EVENTVALIDATION=%2FwEWBgLEqNr7CwLvlZj3DAL%2B36urBAKC4OLACgLP5%2FC0CAK60JC3A7Rw83B53jkRYUWXpWV8FgNXIOKmMAHjocaf50Ar6soY&But_BaseData=%E4%BE%9D%E5%9F%BA%E6%9C%AC%E9%96%8B%E8%AA%B2%E8%B3%87%E6%96%99%E6%9F%A5%E8%A9%A2",
    "search":"__VIEWSTATE=%2FwEPDwUKMTU0NTI1Njk5MQ9kFgICAQ9kFhICAw9kFgQCCw8PFgIeBFRleHRlZGQCDQ8PFgIfAAUEQmFzZWRkAgUPDxYCHgdWaXNpYmxlZ2QWBgIBDxBkZBYBAgFkAgMPEA8WBh4NRGF0YVRleHRGaWVsZAUGRHB0Q25hHg5EYXRhVmFsdWVGaWVsZAUFRHB0Tm8eC18hRGF0YUJvdW5kZ2QQFVsKQWxsLeWFqOmDqBIwMS3kuK3lnIvmloflrbjns7sPMDIt5q235Y%2By5a2457O7DDAzLeWTsuWtuOezuxUwRS3kvIHmpa3nrqHnkIblrbjns7seMEYt6YeR6J6N6IiH5ZyL6Zqb5LyB5qWt5a2457O7JDBMLeWkqeS4u%2BaVmeeglOS%2FruWtuOWjq%2BWtuOS9jeWtuOeoizAwVi3mlZnogrLpoJjlsI7oiIfnp5HmioDnmbzlsZXlrbjlo6vlrbjkvY3lrbjnqIswMFct6Yar5a246LOH6KiK6IiH5Ym15paw5oeJ55So5a245aOr5a245L2N5a2456iLFTEwLeWcluabuOizh%2BioiuWtuOezuxUxMS3lvbHlg4%2FlgrPmkq3lrbjns7sVMTIt5paw6IGe5YKz5pKt5a2457O7FTEzLeW7o%2BWRiuWCs%2BaSreWtuOezuxsxNi3pq5TogrLlrbjns7vpq5TogrLlrbjntYQeMTct6auU6IKy5a2457O76YGL5YuV56u25oqA57WEJDE4LemrlOiCsuWtuOezu%2BmBi%2BWLleWBpeW6t%2BeuoeeQhue1hC0xOS3pm7vmqZ%2Flt6XnqIvlrbjns7vns7vntbHoiIfmmbbniYfoqK3oqIjntYQVMjAt6Iux5ZyL6Kqe5paH5a2457O7FTIyLeazleWci%2BiqnuaWh%2BWtuOezuxgyMy3opb%2Fnj63niZnoqp7mloflrbjns7sVMjQt5pel5pys6Kqe5paH5a2457O7GDI1Lee%2BqeWkp%2BWIqeiqnuaWh%2BWtuOezuxUyNi3lvrfoqp7oqp7mloflrbjns7sYMzAt5pW45a2457O757SU5pW45a2457WEGzMxLeaVuOWtuOezu%2BaHieeUqOaVuOWtuOe1hAwzMy3ljJblrbjns7sPMzkt5b%2BD55CG5a2457O7JDQ2Lee5lOWTgeacjeijneWtuOezu%2Be5lOWTgeioreioiOe1hCo0OC3nuZTlk4HmnI3oo53lrbjns7vnuZTlk4HmnI3po77ooYzpirfntYQVNTEt6LOH6KiK5bel56iL5a2457O7EjU0LeeUn%2BWRveenkeWtuOezuxg1NS3niannkIblrbjns7vniannkIbntYQeNTYt54mp55CG5a2457O75YWJ6Zu754mp55CG57WEFTU3LemkkOaXheeuoeeQhuWtuOezuxg1OC3lhZLnq6XoiIflrrbluq3lrbjns7sPNjMt56S%2B5pyD5a2457O7FTY0Leekvuacg%2BW3peS9nOWtuOezuw82NS3ntpPmv5%2Flrbjns7sPNjYt5rOV5b6L5a2457O7FTY3Leiyoee2k%2BazleW%2Bi%2BWtuOezuxg2OC3lrbjlo6vlvozms5Xlvovlrbjns7skNjkt57mU5ZOB5pyN6KOd5a2457O75pyN6aO%2B6Kit6KiI57WEDzcxLeacg%2BioiOWtuOezuxU3NC3os4foqIrnrqHnkIblrbjns7sVNzYt57Wx6KiI6LOH6KiK5a2457O7DzgwLemfs%2BaoguWtuOezuxU4MS3mh4nnlKjnvo7ooZPlrbjns7sVODIt5pmv6KeA6Kit6KiI5a2457O7Ejg1Lemjn%2BWTgeenkeWtuOezuxI4Ni3nh5%2FppIrnp5Hlrbjns7sPOTAt5a6X5pWZ5a2457O7DzkxLeitt%2BeQhuWtuOezuxU5Mi3lhazlhbHooZvnlJ%2Flrbjns7sMOTQt6Yar5a2457O7FTk1LeiHqOW6iuW%2Fg%2BeQhuWtuOezuxU5Ni3ogbfog73msrvnmYLlrbjns7sVOTgt5ZG85ZC45rK755mC5a2457O7LTk5Lembu%2Bapn%2BW3peeoi%2BWtuOezu%2Bmbu%2BiFpuiIh%2BmAmuioiuW3peeoi%2Be1hBZLMDUt6Zu75a2Q5ZWG5YuZ5a2456iLE0swOS3ogIHkurrlrbjlrbjnqIsWSzEyLeiLseiqnuiPgeiLseWtuOeoix9LMTgt5aSW5Lqk6IiH5ZyL6Zqb5LqL5YuZ5a2456iLHEsxOS3lsI3lpJboj6%2Foqp7mlZnlrbjlrbjnqIslSzI3LeatkOebn%2BiqnuiogOiIh%2BaWh%2BWMlueglOeptuWtuOeoixxLMjgt6Zuy56uv5pyN5YuZ6Lao5Yui5a2456iLNEszMC3phqvlrbjlt6XnqIvlrbjliIblrbjnqIsgICAgICAgICAgICAgICAgICAgICAgICA1SzMzLeenkeaKgOeUoualreWMluWtuOWIhuWtuOeoiyAgICAgICAgICAgICAgICAgICAgICA3SzM0LTNE5YiX5Y2w6Kit6KiI6IiH5oeJ55So5a245YiG5a2456iLICAgICAgICAgICAgICAgIDdLMzct5aSn5pW45pOa55Si5qWt5pm65oWn5a245YiG5a2456iLICAgICAgICAgICAgICAgICAgOEs0MC3li5XmhYvos4foqIroppboprroqK3oqIjlrbjliIblrbjnqIsgICAgICAgICAgICAgICAgNks0MS3pq5TmhJ%2FkupLli5XoqK3oqIjlrbjliIblrbjnqIsgICAgICAgICAgICAgICAgICAgIA9BVC3pq5TogrLoqrLnqIsJQ1Qt5ZyL5paHFUUgLeaVmeiCsuWtuOeoi%2Biqsueoiw9FVC3lsIjmpa3lgKvnkIYPRlQt5aSW6Kqe6Kqy56iLD0lULeWkp%2BWtuOWFpemWgA9MQy3oi7Hogb3oqrLnqIsPTFQt5Lq655Sf5ZOy5a24IU5ULeiHqueEtuenkeaKgOmgmOWfn%2BmAmuitmOiqsueoiyFQVC3kurrmlofol53ooZPpoJjln5%2FpgJrorZjoqrLnqIshU1Qt56S%2B5pyD56eR5a246aCY5Z%2Bf6YCa6K2Y6Kqy56iLFUFHLeiXneihk%2BWtuOmZouiqsueoixJDRy3mloflrbjpmaLoqrLnqIsVRkct5aSW6Kqe5a246Zmi6Kqy56iLFUhHLeawkeeUn%2BWtuOmZouiqsueoixVKRy3ms5XlvovlrbjpmaLoqrLnqIsVU0ct55CG5bel5a246Zmi6Kqy56iLFVdHLeekvuacg%2BWtuOmZouiqsueoixVWIC3lhbHlkIzoi7HmlofoqrLnqIsPWVQt6LuN6KiT6Kqy56iLFVsKQWxsLeWFqOmDqAIwMQIwMgIwMwIwRQIwRgIwTAIwVgIwVwIxMAIxMQIxMgIxMwIxNgIxNwIxOAIxOQIyMAIyMgIyMwIyNAIyNQIyNgIzMAIzMQIzMwIzOQI0NgI0OAI1MQI1NAI1NQI1NgI1NwI1OAI2MwI2NAI2NQI2NgI2NwI2OAI2OQI3MQI3NAI3NgI4MAI4MQI4MgI4NQI4NgI5MAI5MQI5MgI5NAI5NQI5NgI5OAI5OQNLMDUDSzA5A0sxMgNLMTgDSzE5A0syNwNLMjgDSzMwA0szMwNLMzQDSzM3A0s0MANLNDECQVQCQ1QBRQJFVAJGVAJJVAJMQwJMVAJOVAJQVAJTVAJBRwJDRwJGRwJIRwJKRwJTRwJXRwFWAllUFCsDW2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAQIBZAIFDxAPFgYfAgUIQ2xhc3NDbmEfAwUHQ2xhc3NObx8EZ2QQFQ4KQWxsLeWFqOmDqA4wMTAwLeS4reaWh%2Bezuw4wMTAxLeS4reaWh%2BS4gA4wMTAyLeS4reaWh%2BS6jA4wMTAzLeS4reaWh%2BS4iQ4wMTA0LeS4reaWh%2BWbmxEwMTExLeS4reaWh%2BS4gOeUshEwMTEyLeS4reaWh%2BS6jOeUshEwMTEzLeS4reaWh%2BS4ieeUshEwMTE0LeS4reaWh%2BWbm%2BeUshEwMTIxLeS4reaWh%2BS4gOS5mREwMTIyLeS4reaWh%2BS6jOS5mREwMTIzLeS4reaWh%2BS4ieS5mREwMTI0LeS4reaWh%2BWbm%2BS5mRUOCkFsbC3lhajpg6gEMDEwMAQwMTAxBDAxMDIEMDEwMwQwMTA0BDAxMTEEMDExMgQwMTEzBDAxMTQEMDEyMQQwMTIyBDAxMjMEMDEyNBQrAw5nZ2dnZ2dnZ2dnZ2dnZ2RkAgcPDxYCHwFoZGQCCQ8PFgIfAWhkZAILDw8WAh8BaGQWBAIBDxBkZBYBZmQCAw8QZGQWAGQCDQ8PFgIfAWhkFgICAQ8QZGQWAWZkAg8PDxYCHwFnZGQCEQ8PFgIfAWhkZAITDw8WAh8BaGQWAgIBDzwrABEBARAWABYAFgBkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYQBQpDaGVja0JveF9SBQpDaGVja0JveF9TBQpDaGVja0JveF9HBQpDaGVja0JveF9UBQpDaGVja0JveF9VBQpDaGVja0JveF9XBQ1DaGVja0JveF9IYWxmBQ1DaGVja0JveF9ZZWFyBRBDaGVja0JveF9PdXRGbGFnBQxDaGVja0JveF9XSzEFDENoZWNrQm94X1dLMgUMQ2hlY2tCb3hfV0szBQxDaGVja0JveF9XSzQFDENoZWNrQm94X1dLNQUMQ2hlY2tCb3hfV0s2BQxDaGVja0JveF9XSzcFDUdWX0NvdXJzZUxpc3QPZ2Qmg85qK5fb%2FjXuKnWxY%2FPVpLV3BWDt9B%2BTSRcAhAOVcQ%3D%3D&__EVENTVALIDATION=%2FwEWqAECj5%2Fy6wcC75WY9wwC%2Ft%2BrqwQCguDiwAoCz%2BfwtAgCutCQtwMCj5vOyAICn%2FTkpg4C0%2FTkpg4C0vTkpg4C1vTkpg4C4%2FTkpg4ClpvWrQkCnbfSygsChvSwwAUChvS0wAUChvSIwAUChvTA3QUChvTE3QUChvTs3QUChvSE3QUChvSY3QUCmfS8wAUCmfSwwAUCmfS0wAUCmfSIwAUCmfSEwAUCmfSYwAUCmfTcwwUCmfTQwwUCmPS8wAUCmPS0wAUCmPSIwAUCmPSMwAUCmPSAwAUCmPSEwAUCm%2FS8wAUCm%2FSwwAUCm%2FSIwAUCm%2FTQwwUCmvSEwAUCmvTcwwUCnfSwwAUCnfSMwAUCnfSAwAUCnfSEwAUCnfSYwAUCnfTcwwUCnPSIwAUCnPSMwAUCnPSAwAUCnPSEwAUCnPSYwAUCnPTcwwUCnPTQwwUCn%2FSwwAUCn%2FSMwAUCn%2FSEwAUCjvS8wAUCjvSwwAUCjvS0wAUCjvSAwAUCjvSEwAUCgfS8wAUCgfSwwAUCgfS0wAUCgfSMwAUCgfSAwAUCgfSEwAUCgfTcwwUCgfTQwwUCkKb0iQcC1NXqiA0Co5qTyQYCsf7MvQMC1NXuiA0CqpSA4wsCsf7AvQMC6bXXlwICxvGMVAL9yK6jDQKqlITjCwLptauUAgKMg83iDALJ9IzdBQLL9IzdBQLN9PzDBQLN9IzdBQLM9IzdBQLx9IzdBQLy9MjdBQLy9IzdBQL09IzdBQLm9IzdBQL79IzdBQLJ9NjdBQLL9NjdBQLM9NjdBQL%2B9NjdBQLw9NjdBQL79NjdBQL%2F9NjdBQL89PzDBQLh9IzdBQLQtoaiDwLxtMvCDQLxtLfpCgLxtKOUAwLxtI%2BzCALxtPtfAp6N0YQMAp6NvaMFAp6Nqc4NAp6NlfUKArua85MGArua374PAruay%2BUHAruat4AMApTjj70JApTjk70JApTj470JApTjp70JApTjq70JApTjo70JAqSTkNEHAqS4x%2FUOAvmn84MEApHF6%2B4JAs2qgYMFAs2qjYMFAs2qiYMFAs2qtYMFAs2qsYMFAs2q2Z4FAs2qvYMFAs2quYMFAs2qpYMFAs2q4YAFAsqqgYMFAsqqjYMFAsqqiYMFAsqqtYMFAsqqsYMFAoPF6%2B4JAt%2BqgYMFAt%2BqjYMFAt%2BqiYMFAt%2BqtYMFAt%2BqsYMFAt%2Bq2Z4FAt%2BqvYMFAt%2BquYMFAt%2BqpYMFAt%2Bq4YAFAtiqgYMFAtiqjYMFAtiqiYMFAtiqtYMFAtiqsYMFAqydrKsMAqyd6LwGAqyd1OENAqydkPMHAqyd%2FJcPAqyduKkJAqydpE4CrJbJpgYCsJb91A%2FerFsffYez0qSXcumkoXRsOy3MhPk4pFLAnwC0aeDMww%3D%3D&DDL_AvaDiv=D&DDL_Avadpt=01&But_Run=%E6%9F%A5%E8%A9%A2%EF%BC%88Search%EF%BC%89",
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
    return open("sql/1052.sql", 'w')
    #return open("/absolute/path/to/sql/%s/%s.sql"%(sys.argv[1], sys.argv[2]), 'w')


def main():
    view_state, even_vaild = prepare_token()

    line = 0
    data = []
    idlist = { "D":[], "C":[], "G":[], "T":[] }
    div2emo = {"D": "☀️️", "C": "🌙", "G": "🎓", "T": "2️⃣"}
    for div in divs:
        for dep in deps[div]:
            skipcid = 0
            print " 🔍  Fetching %s  - %s - %s"%(div2emo[div], dep,  depn[dep])    
            payload = default["search"] + '&' + (default["select"] % (div, dep))
            rows = crawler( payload )  
            for row in rows:
                skip = 1
                cols = row.findAll('td')
                course = []
                cid = -1
                for ele in cols:
                    if skip > 0:
                        skip -= 1
                    elif ele.find('table'):
                        for inner in ele.findAll('span'):
                            if re.compile(remove).search(inner.text) :
                                continue
                            if re.compile(u"[\s|\t|\b]+年級").search(inner.text):
                                course.append(re.sub('\s|\b|\t', '', inner.text))
                            else:
                                course.append( inner.text.strip().replace("'", "\\'") )
                        skip = len(ele.findAll('td'))
                    else:
                        if cid == -1:
                            cid = ele.text.strip()
                            if cid in idlist[div]:
                                skipcid += 1
                                break
                            idlist[div].append(cid)
                        else :
                            course.append(ele.text.strip().replace("&nbsp;", "").replace("'", "\\'"))
                if len(course) > 0 :
                    write = ("('%s')") if line == 0 else (",\n('%s')")
                    data.append( write%"','".join(course).encode('utf-8') )
                    line += 1
            if skipcid > 0:
                print " ⏩ %d courses have been recorded !"%skipcid

    line = 0
    f = open_file(div, dep)
    f.write("INSERT INTO Course VALUES \n")
    for course in data:
        line += 1
        f.write(course)
    f.close
    print 
    print "done, got  %d courses"
    print "🕶️ see that? It worked"


if __name__ == '__main__':
    main()
