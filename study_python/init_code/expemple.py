# import test
# 
# print(test)
# print(test.A)

# import test as t
# 
# print(t)

# from test import A
# print(A)

# from test import A as MyA
# print(MyA)

# import mypackage
# print(mypackage)
# print(mypackage.B)

# import mypackage.mymodule
# print(mypackage.mymodule)
# print(dir(mypackage.mymodule))
# print(mypackage)
# print(dir(mypackage))

# import mypackage.mymodule
# print(mypackage.mymodule.f())
# print(mypackage.mymodule.__package__)

# import mypackage
# print(mypackage.f())

from mypackage import f
print(f())