'''
from urllib import parse, request

params = parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'280',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'_ga=GA1.2.453498494.1478212819; DCA0_reg809=!8lzUtZzDeDSa384JO1aveY9C8BcsKsPrx+EXjopxMmUqCy9Vi8h6DlUurOHAToidvphXRU90nnn9fhI=',
'Host':'www.reg.uci.edu',
'Origin':'https://www.reg.uci.edu',
'Referer':'https://www.reg.uci.edu/perl/WebSoc',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36}'
}
req = request.Request("https://www.reg.uci.edu/perl/WebSoc", params.encode('ascii'), headers)
response = request.urlopen(req)
'''
'''
from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'https://www.reg.uci.edu/perl/WebSoc' # Set destination URL here
headers = {'Host':'www.reg.uci.edu',
           'Connection':'keep-alive'
           'Content-Length}   # Set POST fields here

request = Request(url, urlencode(headers).encode())
json = urlopen(request).read().decode()
print(json)
'''

import threading
import json
import urllib.request
headers = {'Host':'www.reg.uci.edu',
           'Connection':'keep-alive',
           'Content-Length': '280',
           'Cache-Control':'max-age=0',
           'Origin':'https://www.reg.uci.edu',
           'Upgrade-Insecure-Requests':'1',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Referer':'https://www.reg.uci.edu/perl/WebSoc',
           'Accept-Encoding':'gzip, deflate, br',
           'Accept-Language':' en-US,en;q=0.8',
           'Cookie':' _ga=GA1.2.453498494.1478212819; DCA0_reg809=!8lzUtZzDeDSa384JO1aveY9C8BcsKsPrx+EXjopxMmUqCy9Vi8h6DlUurOHAToidvphXRU90nnn9fhI='
           }
'''
conditionsSetURL = 'https://www.reg.uci.edu/perl/WebSoc/'
newConditions = {"YearTerm":'2017-14', "ShowComments":'on', "ShowFinals":'on', "breadth":'ANY', "Dept":"WRITING",
                 'CourseNum':'','Division':'ANY','CourseCodes':'','InstrName':'','CourseTitle':'','ClassType':'ALL','Units':'','Days':'',
                 'StartTime':'','EndTime':'','MaxCap':'','FullCourses':'ANY','FontSize':'100','CanceledCourse':'Exclude','Bldg':'',
                 'Room':'','Submit':'Display Web Results'}
'''






 #BEST WORKING ONE FOR 39C
'''  
conditionsSetURL = 'https://www.reg.uci.edu/perl/WebSoc/'
newConditions = {"YearTerm":'2017-14', "ShowComments":'on', "ShowFinals":'on', "breadth":'ANY', "Dept":"WRITING",
                 'CourseNum':'','Division':'ANY','InstrName':'','CourseTitle':'','ClassType':'ALL','Units':'','Days':'',
                 'StartTime':'','EndTime':'','MaxCap':'','FullCourses':'SkipFullWaitlist','FontSize':'100','CanceledCourse':'Exclude','Bldg':'',
                 'Room':'','Submit':'Display Web Results'}



import datetime
import tkinter
window = tkinter.Tk()
label = tkinter.Label(master=window,text='Checking')
label.pack()
window.lift()
window.attributes('-topmost', True)
def lolk():
    count=0
    #k = threading.Timer(5,lolk)
    #k.start()

    #window.attributes('-topmost', False)
    #window.mainloop()
    k = threading.Timer(5,lolk)
    k.start()
    data = urllib.parse.urlencode(newConditions)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(conditionsSetURL, data)
    the_page = urllib.request.urlopen(req).read()
    the_page=the_page.decode(encoding='ascii')
    file = open("results.html","w")
    file.write(the_page)
    kk = open("results.html",'r').readlines()
   # print(kk)
    for line in range(len(kk)):
        if '39C' in kk[line]:
            count+=1
            #if 'OPEN' in kk[line+10]:
             #   ex = kk[line+10]
              #  ex = ex[ex.index('>'):]
               # label.config(text=datetime.datetime.now()+'\n'+ex)

    if count != 1 and count !=0:
        print('HEY',count,datetime.datetime.now())
       # label.destroy()
        #label1 = tkinter.Label(master=window,text=datetime.datetime.now())
        #label1.pack()
        label.config(text=datetime.datetime.now())
        #label.destroy()
    else:
        label.config(text='Checking')
    window.mainloop()
       
    
        #k.stop()

        
lolk()

'''


conditionsSetURL = 'https://www.reg.uci.edu/perl/WebSoc/'
newConditions = {"YearTerm":'2017-14', "ShowComments":'on', "ShowFinals":'on', "Creadth":'ANY', "Dept":"ALL",
                 'CourseNum':'','CourseCodes':'77110','Division':'ANY','InstrName':'','CourseTitle':'','ClassType':'ALL','Units':'','Days':'',
                 'StartTime':'','EndTime':'','MaxCap':'','FullCourses':'ANY','FontSize':'100','CanceledCourse':'Exclude','Bldg':'',
                 'Room':'','Submit':'Display Web Results'}



import datetime
import tkinter
window = tkinter.Tk()
label = tkinter.Label(master=window,text='Checking')
label.pack()
window.lift()
window.attributes('-topmost', True)
def lolk():
    count=0
    #k = threading.Timer(5,lolk)
    #k.start()

    #window.attributes('-topmost', False)
    #window.mainloop()
    k = threading.Timer(10,lolk)
    k.start()
    data = urllib.parse.urlencode(newConditions)
    data = data.encode('ascii') # data should be bytes
    print(data)
    req = urllib.request.Request(conditionsSetURL, data)
    
    the_page = urllib.request.urlopen(req).read()
    #print(the_page)
    the_page=the_page.decode(encoding='ascii')
    file = open("results.html","w")
    file.write(the_page)
    kk = open("results.html",'r').readlines()
   # print(kk)
    for line in range(len(kk)):
        if 'OPEN' in kk[line]:
            count+=1
            #if 'OPEN' in kk[line+10]:
             #   ex = kk[line+10]
              #  ex = ex[ex.index('>'):]
               # label.config(text=datetime.datetime.now()+'\n'+ex)

    if count == 1:
        print('HEY',count,datetime.datetime.now())
       # label.destroy()
        #label1 = tkinter.Label(master=window,text=datetime.datetime.now())
        #label1.pack()
        label.config(text=datetime.datetime.now())
        #label.destroy()
    else:
        label.config(text='Checking')
    window.mainloop()
       
    
        #k.stop()

        
lolk()

    
