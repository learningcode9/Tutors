# import os
# print (os.path.expanduser('~'))

# test_str = '    Programming'
# # The trailing whitespaces are excluded
# print(test_str.lstrip())

# str1="hello welcome to sanfrancisco"
# str2=str1.split()
# print(str2)
# print(' '.join(str2))
# import copy
# list3=[1,2,3,4,5]
# list3.append(5)

# list2=copy.deepcopy(list3)
# list2.append(12)


# # tuple1=(1,2,3,4,5)

# # set1={1,2,3,4,5}
# # set1.add(6)
# print(list3)
# print(list2)
# print(tuple1)
# print(set1)



# def extendList(val,tuple=[]):
#     tuple.append(val)
#     return tuple

# list1 = extendList(10)
# #print ("lv after list1 call", list)

# list2 = extendList(123,[])
# #print ("lv list2 = %s" % list)

# list3 = extendList('a')
# #print ("lv list3 = %s" % list)


# print ("list1 = %s" % list1)
# print ("list2 = %s" % list2)
# print ("list3 = %s" % list3)
# s="welcome to sanfrancisco"
# count=0
# for x in s:
#    if x=='o':
#        count=count+1
      
# print(count)

# d=dict()
# s="hello welcome to sanfrancisco"
# for l in s:
   
#     if l in d:
#         d[l] = d[l] + 1
#     else:
#         d[l] = 1
# print(d)

# adict = {var:var**2 for var in range(10)}
# print(adict)
# ints = set([1,1,2,3,3,3,4])
# print(len(ints))

# def test1(param):
#  return str(param)

# def test2(param):
#  return str(2 * param)

# result = test1(1) + test2(2)
# print(result)

# mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
# import pdb
# for i in range(6):
#     print()
#     for j in range(i):
    
#         print("*",end="")
# def factorial(n): 
  
#     # single line to find factorial 
#     return 1 if (n==1 or n==0) else n * factorial(n - 1)  
  
  
# # Driver Code 
# num = 5
# print ("Factorial of",num,"is", 
#       factorial(num)) 

# start = 11
# end = 25
  
# for val in range(start, end + 1): 
#     if val > 1: 
#         for n in range(2, val//2 + 2): 
#             if (val % n) == 0: 
#                 break
#             else: 
#                 if n == val//2 + 1: 
#                     print(val) 

# num = 11
  
# # If given number is greater than 1 
# if num > 1: 
      
#    # Iterate from 2 to n / 2  
#    for i in range(2, num): 
         
#        # If num is divisible by any number between  
#        # 2 and n / 2, it is not prime  
#        if (num % i) == 0: 
#            print(num, "is not a prime number") 
#            break
#    else: 
#        print(num, "is a prime number") 
  
# else: 
#    print(num, "is not a prime number") 


newList=[7,2,1,4]
newList.sort()
print(newList[0])
