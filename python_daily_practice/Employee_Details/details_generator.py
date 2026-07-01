import os
import random
import string
curr=os.getcwd()
# print(curr)
# target = os.path.join(curr, "Employee_Details")
target=r"C:\Users\Akashdeep Singh\Desktop\python_class\python_daily_practice\Employee_Details"
os.chdir(target)
print(os.getcwd())

ID="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(9)]) 
MEETING_ID="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(25)])

def create_details(files):
    for i in files:
        if "txt." in i:
            print(f"files : {i}")
    select=input("select your file without ext:")
    with open(f"{select}.txt","a") as file:
        file.write(f"Name : {select}"+"\n")
        file.write(f"EMP_ID : {ID}")
        file.write(f"MEETING_ID : http://{MEETING_ID}"+"\n")
        file.write(f"CANDIDATE_EMAIL : {input("Enter Your Email : ")}"+"\n")

    print(f"{select} file updated....")
files=os.listdir()
print(files)
create_details(files)


