# # # tuple
# # # tuple is a data structure in python used to store
# # # multiple data of different types with coma(,) in round braces.
# # # immutable
# # # support indexing slicing and ordered.

# # # creation of tuple.
# # # t1=(50,56)
# # # print(type(t1))
# # # print(t1)
# # t1,t2,t3=(50,40,30)
# # print(type(t1))
# # print(t2)

# #indexing and slicing.
# marks_tuple=(50,55,69,34,89)
# print(marks_tuple[0])
# print(marks_tuple[::-1])
# #  mutability not
# marks_tuple=(50,55,69,34,89)
# marks_tuple[2]=500
# print(marks_tuple)
# traversing
# waf to extract all num greater than 55 
# marks=(50,55,69,34,89)
# for i in marks:
#     if i>=55:
#         print("greatest marks are:",i)
# def tuple_fun(m):
#     new_value=[]
#     for i in m:
#         if i>=55:
#             new_value.append(i)
#     return new_value
# marks_tuple=(50,55,69,34,89)
# res=tuple_fun(marks_tuple)
# print(res)
# waf to sum of indices of tuple
# def sum_idx(n):
#     count=0
#     for i in range(len(n)):
#         count=count+i
#     return count
# res=sum_idx((1,2,3,4,5,6))
# print(res)
marks_tuple=(50,55,69,34,89)
s=0
for i in range(len(marks_tuple)):
    s+=i
print(s)
