# f= open("demo.txt","r")
# r=f.read()
# s=''
# for i in r:
#     if i not in '0123456789':
#         s+=i
# file=open("new_demo.txt","w")
# file.write(s)
# file.close()   

# with open("new_demo.txt","a") as f:
#     f.write("now the file has more content....!")

# with open("new_demo.txt") as f:
#     print(f.read())

# f= open("new_demo.txt","r")
# r=f.read()
# s=""
# for i in r:
#     if i not in "aeiouAEIOU":
#         s+=i
# file=open("new_demo.txt","w")
# file.write(s)
# file.close()

# f=open("demo.txt","w")
# f.write("i have added some more text.....")

# f=open("demo.txt")
# print(f.read())

# f=open("demo.txt","a")
# f.write("\nhello my name is akashdeep singh")
# file=open("demo.txt",'r')

# print(file.read())
# f.close()

# f=open("demo.txt","r")
# r=f.read()
# st=""
# for i in r:
#     if i not in "aeiou":
#         st=st+i
# f=open("demo.txt","w")
# f.write(st)
# f=open("demo.txt","r")
# f.read()
# f.close()


# emp_list=["aman","shivam","shubham","anshu","anshu","kamal"]
# for e in emp_list:
#     with open(f"{e}.txt","w") as file:

#         print(f"{e},txt File Created...")


import os

folder="Employee_Details"
# os.makedirs(folder)



emp_list=["aman","shivam","shubham","anshu","anshu","kamal"]
# for e in emp_list:
#     os.remove(f"{e}.txt")
#     print(e , "removed..") 
curr=os.getcwd()
target=curr+"\\"+folder
# print(target)
os.chdir(target)

emp_list=["aman","shivam","shubham","anshu","anshu","kamal"]
for e in emp_list:
    with open(f"{e}.txt","w") as file:
        print(f"{e},txt File Created...")






