def fact(n):
    if n == 0:
        return 1
    else:return n*fact(n-1)
num = eval(input())
print(fact(abs(int(num))))'''
'''#最大递归深度
def reverse(s):
    return reverse(s[1:]) +s[0]
reverse("ABCD")
#设定递归层数
import sys
sys.setrecursionlimit(2000) #新的递归层数2000
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
str = input("请输入一个字符")
print(reverse(str))