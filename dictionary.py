#dictionary
#defination and property of dictionary
#1.dictionary is a data structure in python used to store multiple data in key:value format.
#2.ordered, mutable
#3.indexed by key, not position.
#4.key must be unique (immutable)
#5. value can be any type of data.
#6. used in fast lookup.

#-----------creation of dictionary.
# stu_profile={"aman":"noida","rohan":"delhi"}
# print(type(stu_profile))
# print(stu_profile)


# stu_marks=dict([('aman',300),("shivam",80)])
# print(stu_marks)

# stu_profile={"aman":"noida","rohan":"delhi"}
# stu_profile['aman']="dubai"
# print(stu_profile)

#inbuilt-methods


# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# res=stu_marks.get('dev',"N/A")
# print(v)
# print(k)
# print(i)
# print(res)


#update
# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
# new_marks={"kamal":89,"ram":77,"aman":30}
# stu_marks.update(new_marks)
# print(stu_marks)

profile={
    'aman':{
        'address':["noida","delhi","mumbai"],
        'hobbies':["reading","cooking","travelling"],
        'password':{"insta":443534,"fb":878678},
    },
    'dev':{
        'address':["noida","delhi","mumbai"],
        'hobbies':["reading","cooking","travelling"],
        'password':{"insta":443534,"fb":878678},
    },
}
print(profile['dev'])
