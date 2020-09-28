

#leader program 


arr = [16,18,3,5,2]

def leaderProg(arr):
  size = len(arr)
  max_ele = arr[size-1]
  print(max_ele)
  for i in range(size-2,0,-1):
    if max_ele < arr[i]:
      print(arr[i])
      max_ele = arr[i]



leaderProg(arr)


arr = [1,1,2,2,2 ]


# from collections import Counter

# def maxCount(arr):
#   size = len(arr)
#   count = Counter(arr)
#   for c in count:
#     # if count[c] >= size/2:
#     if count[c] % 2 !=0:
#       print( c ,count[c])  

# print(maxCount(arr))






def counter(arr):
  dic = {}
  for i in arr:
    if i in dic :
      dic[i] = dic[i]+1
    else :
      dic[i] = 1
  dictionary = dic
  for i in  dictionary:
    if dictionary[i]%2!=0:
      return (i,dictionary[i])
   
# out = counter(arr)
# for i in out:
#   if out[i]%2 !=0:
#     print(i,out[i])

print(counter(arr))
