# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from calls.models import Call
from django.utils import timezone
import datetime
from pyexcel_xlsx import get_data

data = get_data("DataMau.xlsx")

for i, call in enumerate(list(data.items())[0][1][1:]):
    if len(call) == 10:
        # print call
        # print call[0], call[1], call[2], call[3], call[4], call[5], call[6], call[7], call[8], call[9]
        q = Call(i+1, call[0], call[1], call[2], call[3], call[4], 
            call[5] if call[5] else None, call[6] if call[6] else None, call[7], call[8], call[9])
        q.save()
    elif len(call) == 9:
        # print call
        # print call[0], call[1], call[2], call[3], call[4], call[5], call[6], call[7], call[8]
        q = Call(i+1, call[0], call[1], call[2], call[3], call[4], 
            call[5] if call[5] else None, call[6] if call[6] else None, call[7], call[8])
        q.save()
    elif len(call) == 8:
        # print call
        # print call[0], call[1], call[2], call[3], call[4], call[5], call[6], call[7]
        q = Call(i+1, call[0], call[1], call[2], call[3], call[4], 
            call[5] if call[5] else None, call[6] if call[6] else None, call[7])
        q.save()

#x = list(data.items())[0][1]
#call1 = x[2]
#print call1[5], call1[6]
#if call1[6]: print("co mat")
#q = Call(2, call1[0], call1[1], call1[2], call1[3], call1[4], call1[5] if call1[5] else None, call1[6] if call1[6] else None, call1[7], call1[8])
#q.save()
#x = timezone.now()
#print x
#test2 = datetime.strptime('2022-03-15T17:00:56', "%Y-%m-%dT%H:%M:%S")
#print type(test2)
#test3 = datetime.time(1, 1, 0)
#test4 = datetime.time(1, 1, 1)
#if test3 > test4: print("lon hon")
#a = None
#b = 1
#f a and b: print "co het"
#c = datetime.time(1, 2, 3)
#print c
#now = datetime.datetime.strptime('2023-01-03T00:00:12', "%Y-%m-%dT%H:%M:%S")
#d = "04"
#print int(d)
'''
#print(list(data.items())[0][1])
x = list(data.items())[0][1]
#print(len(i))
#print(x[2][6])
#print(len(x))
#for i in list(data.items())[0][1]:
    #print i

call1 = x[1]
#print(type(call1[4]))
print(call1[4])
if call1[4].encode('utf-8') == "Trả lời":
    print("Đúng luôn")
print(call1[2])
if (call1[2] == "1004"): print("dung nguoi goi")

print(call1[1])
date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
print(date)
#if datetime.strptime(call1[1], "%Y-%m-%dT%H:%M:%S") > date: print("Lon hon")
test = datetime.strptime(call1[1], "%Y-%m-%dT%H:%M:%S")
print(test)
print(type(test))
now = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
#print(type(now))
#print(now)
if test < now: print("nho hon")
test2 = datetime.strptime('2022-03-15T17:00:56', "%Y-%m-%dT%H:%M:%S")
print(test2)
if (test2 >= test): print("test2 is later than test")
'''


