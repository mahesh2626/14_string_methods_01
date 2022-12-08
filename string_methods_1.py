w='python'
print(w,type(w))
print(w[0:5])
print(w[1:4])
print(w[0:2:1])
print(w[0:5:3])

a='python'
print(a[0])
print(a[1:5:3])

"""concatenation"""
a="hello world"
x=(a+' '+'python')
print(x)
print(len(x))
print(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[12]+x[13]+x[14]+x[15]+x[16]+x[17])

a="heLLo_WORld"
print(a.capitalize())
print(a.casefold())
print(a.lower())
print(a.isupper())
print(a.islower())
print(a.isidentifier())
print(a.upper())

a=" hello world "
print(a.center(20))
print(a.center(26,'@'))
print(a.center(30,'$'))

x=a.encode()
print(x,type(x))
print(x.decode())