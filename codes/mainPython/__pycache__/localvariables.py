# 1
# def area(r,pi=3.14):
#     ar=pi*r*r
#     if r<0:
#         return
#     else:
#         print(ar)
# r=int(input("Enter radius: "))
# area(r)


# 2
# def simple_in(p,t,r=10):
#     si=p*r*t/100
#     print(si)
# p=int(input("Enter principle: "))
# t=int(input("Enter time: "))
# simple_in(p,t)

# a="x"
# def me():
#     a="y"
#     print(a)
# print(a)
# me()

# a="x"
# def me():
#     global a
#     a="y"
#     print(a)
# me()
# print(a)
def me():
    me=str(input("Enter strring: "))

    for me in range(0,len(me)):
        if me=="I Love Python":
            continue
        else:
            print("ilovepython")

me()