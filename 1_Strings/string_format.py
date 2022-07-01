myName = 'SKK'
myJob = 'Data Scientist'
print('My name is ', myName)
print('My Name is {}, and Im working as a {}'.format(myName, myJob))

x = 10
y = 20
print('The given value is:%i' % x)
print('The Values are: %i %i' % (x,y))
print('The Values are: %d %d' % (x,y))

for i in range(11):
    print('Number:{:.2f}'.format(i))

import datetime

my_date = datetime.datetime(2020, 2, 7, 12, 30, 45)
print('{:%B %d, %Y}'.format(my_date))

x = 'There are %d types of people' % 10
print(x)