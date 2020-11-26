#write a program to create a list of n integer values and do the following
 L1=['21','32','43','54','65']
 # a) add an item in to the list (using function)
 L1.append('76')
print(L1)
['21', '32', '43', '54', '65', '76']
 # b) delete(using function)
L1.remove('32')
print(L1)
['21', '43', '54', '65', '76']
 # c) store the largest number from the list to a variable
 print(max(L1))
76
 # d) store the smallest number from the list to a variable
 print(min(L1))
21
 #create a tuple and point the reverse of the created tuple
 tuple = ('11','21','31','welcome','3.14')
>>> reversedtuples = tuple[::-1]
 print(reversedtuples)
('3.14', 'welcome', '31', '21', '11')
 #create a tuple and convert tuple into list
tuple = ('45','56','67','3.45','hello')
 list = list(tuple)
 print(type(list))
<class 'list'>
print(list)
['45', '56', '67', '3.45', 'hello']
