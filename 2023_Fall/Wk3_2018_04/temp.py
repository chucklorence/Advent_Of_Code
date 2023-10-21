import datetime
from operator import itemgetter

str1 = '[1518-04-25 00:24] falls asleep'
str2 = '[1518-05-22 23:50] Guard #3299 begins shift'
str3 = '[1518-06-25 00:25] falls asleep'
str4 = '[1518-04-13 00:54] wakes up'


date = str2[6:11]
entryType = str2[:]
hour = str2[:]
minute = str2[:]
if entryType == 'G':
    guardNum = str2[:]
    
'''
[1518-10-07 23:58] Guard #919 begins shift
[1518-10-08 00:40] falls asleep
[1518-10-08 00:50] wakes up
[1518-10-08 00:54] falls asleep
[1518-10-08 00:58] wakes up

[1518-10-09 00:04] Guard #283 begins shift
[1518-10-09 00:07] falls asleep
[1518-10-09 00:39] wakes up

[1518-10-09 23:57] Guard #2801 begins shift
[1518-10-10 00:13] falls asleep
[1518-10-10 00:39] wakes up
[1518-10-10 00:48] falls asleep
[1518-10-10 00:49] wakes up
[1518-10-10 00:52] falls asleep
[1518-10-10 00:58] wakes up

[1518-10-10 23:58] Guard #3571 begins shift
[1518-10-11 00:22] falls asleep
[1518-10-11 00:47] wakes up

[1518-10-11 23:52] Guard #1619 begins shift
[1518-10-12 00:56] wakes up
[1518-10-12 00:05] falls asleep
'''

'''
DataList [] of Dic = {DateTimeObj, Month, Day, Hour, Minute, Type, GuardNum, Checked}
1. Load all the lines of data into the list of Dictionaries
2. Sort the DataList by DateTimeObj
    from operator import itemgetter
    list_of_dictionaries.sort(key=itemgetter('key1'))

GuardList [] of Dic = {Guard, TotalSleepMinutes, ListOfMinutes[60] }
2. Load all the guards into the list of Dicts

3. For each Guard
    1 - Loop through the DataList
    2 - Find the GuardNum, DateTimeObj where Type = G
    3 - Set Checked = 1
    4 - Loop through DataList looking for the DateTimeObj within 90 minutes of the Guard's DateTimeObj where Type = F and W AND Checked = 0
        1. Add each item to a list
        2. Set Checked = 1, Set GuardNum to GuardNum
        3. Sort the list by DateTimeObj and Type (F will be listed before W) 
    5 - Once we have F and W
        1. Grab 2 items - 1st will be F and the 2nd will be W
        2. Subtract F from W to get total minutes alseep        
        3. Increment ListOfMinutes by 1 for each minute in range(F,W)
        4. repeat until end of list
4. Look for the Guard with the largest TotalSleepMinutes
5. Loop through that guard's ListOfMinutes to find the minute when they are most asleep
'''

dtList = ['1518-10-07 00:58',   '1518-10-07 23:58','1518-10-08 00:40','1518-10-08 00:50','1518-10-08 00:54','1518-10-08 00:58',    '1518-10-09 23:57' ]
dtListObjs = []
for str in dtList:
    dtObj = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M")
    dtListObjs.append(dtObj)

#for dtObj in dtListObjs:
#    if dtObj     



date_string = '2023-10-12 00:05'
    
# Convert the string to a date and time object
date_time_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M")

# Print the date and time object
#print(date_time_object)    

