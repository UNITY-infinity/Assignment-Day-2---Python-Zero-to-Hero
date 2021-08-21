# Program that takes a string input and
# prints the number of occurrences of each character

import collections

#input string
st = str(input("Please enter a string - word or phrase or generally a sequence of symbols: "))

#use collections.Counter to count the number of occurences of each character in st
c = collections.Counter(st)

#using another counter for a visually pleasing result at the end of the printing
count=0

for i in c.keys():
   if count<len(c)-1:
      print(i,' - ',c[i], end = ', ')
      count+=1
   else:
      print(i,' - ',c[i])
  