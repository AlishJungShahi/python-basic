
# a = 10
# def hello():
#     a =11
#     print(a)
    
    
# hello()
# print(a)


# a = 10
# def outer():
#     a = 11
#     def inner():
#         a = 12
#         print('inner sees as a ',a)
#     # print('outer sees as a ',a)
    
#     inner()
#     print('outer sees as a ',a)
# print('Global sees as a ', a)
# outer()

#how to change global variable 
a = 10
def changer():
    global a
    a = 11
changer()
print(a)
