# a = 0
# while a!=30:
#     a += 2
#     print(a)

# a = 1
# b = 0
# while b<=225:
#     b = a**2
#     a += 2
#     print(b)

# a = int(input())
# b = int(input())
# c = 0
# d = 0
# while a<=b:
#     c = a
#     a **= 2
#     d += a
#     a = c + 1
# print(d)

# i = 1
# a = int(input())
# b = 1
# while i <= a:
#     b *= i
#     i += 1
# if i > a:
#         a = 1
#         i = 1
#         while i <= b:
#             a *= i
#             i += 1
#
# print(a)




# print('Введите в порядке возрастания ')
# a = 1
# i = 0
# b = -1000000
# while i<5:
#     a = int(input())
#     i += 1
#     if a < b:
#         print('407 1505')
#         i = 10
#     b = a
# if i!=10:
#     print('Molodets')

# from random import randint
# a = randint(1, 100)
# b = 0
# i = 0
# n = 0
# while b!=a:
#     i = 0
#     while b!=a and i!=3:
#         b = randint(1, 100)
#         i +=1
#         if b==a:
#             print('Ugadal')
#         else:
#             print('prougral')
#             n += 1
#     print(n)

# from random import randint
#
# rnd = randint(1, 100)
# print('Random number: {}' .format(rnd))
# num = int(input('input a number: '))
#
# while num!=rnd:
#     if num > rnd:
#         print('num is bigger')
#     if num < rnd:
#         print('num is smaller')
#     num = int(input('input a number: '))
# print('Thats right')

# from random import randint
# secret = randint(9824, 9900)
# i, j = 0, 0
# x = 1
# while i<10:
#     while j < 10:
#         num = randint(9824, 9900)
#         if (i*10+j+1)%9==0:
#             print('{}: {}' .format(x, chr(secret)), end='\t')
#         else:
#             print('{}: {}' .format(x, chr(num)), end='\t')
#         j += 1
#         x += 1
#
#     print()
#     i += 1
#     j = 0

# name = input('Input name:')
# surname = input('Input surname:')
# patronymic = input('Input patronymic:')
# print('{} {}. {}.' .format(surname, name[0], patronymic[0]))

# name = input('Input ФИО: ')
# a = name.find(' ') + 1
# b = name.rfind(' ') + 1
# print('{}{}. {}.'.format(name[:a], name[a], name[b]))

# str = input()
# i = 0
# k = 0
# while i!=1:
#     a = str.find(' ') + 1
#     print(a)
#     str = str[a:]
#     print(str)
#     k += 1
#     if a == 0:
#         i = 1
# print (k)

# text = input('Write a text')
# a = len(text)
# if a > 10:
#     print('Текст больше 10 символов на {}'.format(a-10))

# a = input('Сколько звезд на небе?')
# b = input('Сколько листьев на дереве?')
# c = input('Почему в трамвайных поручнях не живут тараканы?')
# try:
#     if a.isdigit and b.isdigit and int(a)>=0 and int(b)>=0 and c.isalpha:
#         print('Верно')
# except ValueError:
#     print('Stupid')

# s = input('Скобочки')
# a = 1
# b = -1
# while a!=-1:
#     a = s.find('(')
#     b = s.find(')')
#     print(a)
#     print(b)
#     if a > b:
#         print('error1')
#         break
#     else:
#         s = s[:a] + s[a+1:]
#         s = s[:b] + s[b+1:]
# a = s.find('(')
# b = s.find(')')
# if a == -1 and b == -1:
#     print('Right')
# else: print('error2')

# a=int(input('Введите число'))
# print(a**(1/3))
# print(int(a**(1/3)))
# print(a%2)
# if a%2==0 and a**(1/3)==int(a**(1/3)):
#     print(a)

# blank_list=[]
# blank_list.insert(0, input('you name'))
# blank_list.insert(1, input('you name'))
# blank_list.insert(2, input('you name'))
# print(blank_list)
#
# blank_list.sort()
# blank_list.pop(len(blank_list)-1)
# print(blank_list)
#
# blank_list=blank_list[::-1]
# blank_list.pop(len(blank_list)-1)
# print(blank_list)
#
# if len == 1:
#     print('Верно')

# a=[1,5,231,4234,-10,2312,123]
# i=0
# try:
#     c=a[0]
# except(IndexError):
#         print('error')
#         i=-1
#
# while i<len(a):
#     print(c)
#     print(a[i+1])
#     if a[i+1]<c:
#         c=a[i+1]
#     else:
#         c=c
#     i += 1
# try:
#     print(c)
# except(NameError):
#     print()

# import random
# a=[]
# i=0
# while i!=199:
#     a.append(random.randint(0, 1000))
#     i+=1
#     print(a)
# i=0
# sum=0
# while i!=199:
#     sum+=a[i]
#     print(sum)
#     i+=1
# print(sum)
# print(sum/200)

# a=[input()]
# b=[input()]
# i=0
# while i<len(a) or i==0:
#     i+=1
#     print(i)
#     if a==b:
#         print(a)

# list2 = [[1,2],[3,4],[5,6]]
# k=0
# i=0
# sum=0
# print('len0 ', len(list2))
# while i<len(list2):
#     print('len1 ', len(list2[i]))
#     while k<len(list2[i]):
#         print('element', list2[i][k])
#         if list2[i][k]%2==0 and list2[i][k]>0:
#             sum += list2[i][k]
#         k+=1
#     k=0
#     i+=1
#     print('sum', sum)
# print(sum)
#
# list1=[1,3,4,5,7,8]
# i = 0
# a = 0
# while i < len(list1)-1:
#     print('i=',i)
#     print('list1', list1[i])
#     print('list1 2', list1[i+1])
#     if list1[i]!=list1[i+1]-1:
#         a=list1[i]+1
#         print('a',a)
#     i+=1

# list1 = [1, 2, 3, 60, 42]
# s = "hello!"
# for i in list1:
#     print(i)
#
# for i in s:
#     print(i)
# for num in range(10):
#     print(num)
# for i in range(len(list1)):
#     print(list1[i])
# for i in range(len(list1)):
#     list1[i] *= 2
# print(list1)

# s=1000
# list1=[[1,1],[1,1],[1,1],[1,1]]
# for i in range(4):
#     for k in range(2):
#         list1[i][k]=s-100
#         s-=100
# print(list1)

# s=0
# list1=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(3):
#     for k in range(3):
#         list1[i][k]=s+1
#         s+=1
# print(list1)

