from django.test import TestCase

# Create your tests here.


#python数据类型： 可变数据类型， 不可变数据类型

# 可变数据类型：  []   dict
#
# 不可变数据类型： int   str   ()


# s="hello"
# ret=s.upper()
# print(s)
#
#
# l=[11,22,33]
#
# l.append(44)
#
# print(l)
#
#
# s=[{"name":"egon"},[12,45],l]
#
# s.append(l)
#
# print(s)
#
#
# l.append(55)
#
# print(s)


##################################################






'''
1
  4
    6
  5
2

3
  7
   8
9

'''






comment_list=[

    {"id":1,"content":"...","Pid":None},
    {"id":2,"content":"...","Pid":None},
    {"id":3,"content":"...","Pid":None},
    {"id":4,"content":"...","Pid":1},
    {"id":5,"content":"...","Pid":1},
    {"id":6,"content":"...","Pid":4},
    {"id":7,"content":"...","Pid":3},
    {"id":8,"content":"...","Pid":7},
    {"id":9,"content":"...","Pid":None},

]






import collections


comment_dict=collections.OrderedDict()


for comment in comment_list:

    comment["children_comments"]=[]
    comment_dict[comment["id"]]=comment




ret=[]

for comment in comment_dict:

    if comment_dict[comment]["Pid"]:
        pid=comment_dict[comment]["Pid"]

        comment_dict[pid]["children_comments"].append(comment_dict[comment])


    else:
        ret.append(comment_dict[comment])


print(ret)


















# comment_list=[
#
#     {"id":1,"content":"...","Pid":None,"children_comments":[]},
#     {"id":2,"content":"...","Pid":None,"children_comments":[]},
#     {"id":3,"content":"...","Pid":None,"children_comments":[]},
#     {"id":4,"content":"...","Pid":1,"children_comments":[]},
#     {"id":5,"content":"...","Pid":1,"children_comments":[]},
#     {"id":6,"content":"...","Pid":4,"children_comments":[]},
#     {"id":7,"content":"...","Pid":3,"children_comments":[]},
#     {"id":8,"content":"...","Pid":7,"children_comments":[]},
#     {"id":9,"content":"...","Pid":None,"children_comments":[]},
#
# ]




# comment_list={
#
#     1:{"id":1,"content":"...","Pid":None,"children_comments":[]},
#     2:{"id":1,"content":"...","Pid":None,"children_comments":[]},
#     3:{"id":1,"content":"...","Pid":None,"children_comments":[]},
#     4:{"id":1,"content":"...","Pid":1,"children_comments":[]},
#     5:{"id":1,"content":"...","Pid":1,"children_comments":[]},
#     6:{"id":1,"content":"...","Pid":4,"children_comments":[]},
#     7:{"id":1,"content":"...","Pid":3,"children_comments":[]},
#     8:{"id":1,"content":"...","Pid":7,"children_comments":[]},
#     9:{"id":1,"content":"...","Pid":None,"children_comments":[]},
#
# }


























