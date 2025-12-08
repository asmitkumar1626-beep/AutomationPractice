import datetime
a=datetime.datetime.today().time()
b=datetime.datetime.today().date()
c=datetime.datetime.today()
print(a)
print(b)
filename=c.strftime('%y-%m-%d')
print("file",filename)

