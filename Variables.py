# a=10
# b,c=20,30
# d=e=f=40
# print(a)
# print(c)
# print(f)
# a=int(input("Enter a value"))#5
# b=int(input("Enter b value"))#6
# print(a)
# print(a+b)
# d,e,f=map(int,input("Enter d,e and f").split())#10,20
# print(e)
# age=18
# if(age>18):
#     print("Eligible")
# elif(age==18):
#     print("Welcome to new voter")
# else:
#     print("Not Eligible")
# # print("if condition executed")


# for i in range(10,99):
#     if i%10==2 or i//10==2:  #floor division
#         print(i,end=" ")


#COMPREHENSIVE LIST
# list1=[10,20,True]
# print(sum(list1))
# list1=[10,20,False]
# print(sum(list1))

# even number
n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
#print even number using comprehensive list
list2=[x for x in range(n) if x % 2==1]
print(list2)