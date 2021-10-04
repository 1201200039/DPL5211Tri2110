# Given an array of 3, 6, 9, 12, 23
# Create another array containing the squared number of each number

#Student ID: 1201200039
#Student Name: Tan Jiue Hong

array = [3,6,9,12,23]
square=[]

for i in range(0,5) :
  square.append(array[i]*array[i])
  print(square[i])