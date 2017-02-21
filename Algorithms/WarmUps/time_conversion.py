# Problem:
#
# Sample Input:
# 07:05:45PM
#
# Sample Output:
# 19:05:45

# Solution:

time = raw_input().strip()
if 'AM' in time:
    splited_time = time.split(':')
    hours = int(splited_time[0])
    if  hours is 12:
        hours = "00"
    elif hours < 10:
        hours = "0" + str(hours)
    else:
        hours = str(hours)
    print hours + ':' + splited_time[1] + ':' + splited_time[2].replace('AM','')
else:
    splited_time = time.split(':')
    hours = int(splited_time[0])
    if  hours is 12:
        hours = "12"
    else:
        hours = str(hours + 12)
    print hours + ':' + splited_time[1] + ':' + splited_time[2].replace('PM','')