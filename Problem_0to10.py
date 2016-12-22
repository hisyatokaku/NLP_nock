#coding:utf-8
def solve_0(string = "stressed"):
    print string[::-1]

def solve_1(string = u"パタトクカシーー"):
    print string[::2]

def solve_2(str1 = u"パトカー", str2 = u"タクシー"):
    print ''.join([a+b for a,b in zip(str1,str2)])

def solve_3(string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."):
    string = string.replace(',','')
    string = string.replace('.','')
    string = string.split()
    print [len(i) for i in string]

def solve_4(string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."):
    string = string.replace('.','')
    string = string.replace(',','')
    string = string.split()

solve_4()
