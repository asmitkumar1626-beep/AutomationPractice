try:
    a=int(input("give me the 1st number "))
    b=int(input("give me the 2nd number "))
    if b==0:
        raise Exception("hey you are dividing with zero you dumbass")
    c=a/b
    print(c)
except Exception as e:
    print(e)
    print("exception block mein ho aap")
else:
    print("program ran smoothly")
finally:
    print("goofy ahh program worked again!!")


