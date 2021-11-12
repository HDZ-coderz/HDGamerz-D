import os
import traceback
print("Welcome to S.py")
def f():
    m0="dir"
    m1="exit"
    m2="clear"
    m3="printf"
    m4="help"
    m5="rf"
    m6="ver"
    u=input("")
    if u==m0:
        try:
            u1=input("Location: ")
            a=os.listdir(u1)
            print(a)
        except:
            print("E:1")
            traceback.print_exc()
        f()
    elif u==m1:
    	quit()
    	f()
    elif u==m2:
    	os.system("clear")
    	f()
    elif u==m3:
    	u2=input("")
    	print("> "+u2)
    	f()
    elif u=="":
    	f()
    elif u==m4:
    	print("> Command:-\ndir-To display directory\nexit-To exit\nclear-To clear text\nprintf-To print text\nhelp-help\nrf-To read file\nver-Useless command.")
    	f()
    elif u==m5:
    	try:
    	    print("Write file name with loaction to read")
    	    u3=input("")
    	    ff0=open(u3,"r")
    	    print(ff0.read())
    	    ff0.close()
    	except:
    		print("E:2")
    	f()
    elif u==m6:
    	print("S.py terminal program V-0.9 2021 29 Sep 2021")
    	f()
    else:
    	print("No command Found.E:0")
    	f()
f()