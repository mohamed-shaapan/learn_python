# WHILE LOOP
# ***********************************************************
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

# FOR LOOP
# ***********************************************************
for index in range(1,100) : #range(len(list))
    if index == 20:
        continue
    if index == 50:
        break
    print (index)

print ("Good bye!")

# ENHANCED FOR LOOP
# ***********************************************************
fruits = ['banana', 'apple',  'mango']
for item in fruits:
   print ('Current fruit :', item)

print ("Good bye!")