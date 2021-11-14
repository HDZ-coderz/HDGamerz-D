import os
import traceback
import time
import shutil
import sys
#username open file user.dat
ff4=open("/storage/emulated/0/Android_terminal/Android_terminal/LIB/user.dat","r")
#Welcome
print("Welcome to Mr.Bedrock Terminal "+ff4.read()+"\nType 'help' to list command")
#user.dat file close
ff4.close()
def f0():
#variables type string for command
#The user input will be match with it.
    m0="dir"
    m1="exit"
    m2="cf"
    m3="rf"
    m4="wf"
    m5="cfol"
    m6="af"
    m7="delf"
#Input where user will input command
    u0=input("")
#command display directory code
    if u0==m0:
        print("Input Location:")
        try:
            u1=input("")
            list0=os.listdir(u1)
            print (list0)
        except:
            print("E:1")
        f0()
#end
#terminate program
    elif u0==m1:
    	os._exit(0)
#end
#create file command code
    elif u0==m2:
        print("File name with location")
        try:
            u2=input("")
            ff0=open(u2,"x")
            ff0.close()
        except:
            traceback.print_exc()
            print("E:00")
        f0()
#end
#read file command code
    elif u0==m3:
        print("File Location to read")
        try:
            u3=input("")
            ff1=open(u3,"r")
            print(ff1.read())
            ff1.close()
            f0()
        except:
            traceback.print_exc()
            print("E:2")
        f0()
#end
#Write file command code
    elif u0==m4:
        print("File Location to Write\nWarning!\nAll data will be deleted which it had already.")
        try:
            u4=input("")
            ff2=open(u4,"w")
            u5=input("Write in file: ")
            ff2.write(u5)
            ff2.close()
        except:
            traceback.print_exc()
            print("E:3")
        f0()
#end
#Append file command code
    elif u0==m6:
        print("File Location to append")
        try:
            u6=input("")
            ff2=open(u6,"a")
            u7=input("Append in file: ")
            ff2.write(u7)
            ff2.close()
        except:
            traceback.print_exc()
            print("E:4")
        f0()
#end
#create folder command code
    elif u0==m5:
        try:
            print("Location Where to create with folder name")
            u9=input("")
            os.makedirs(u9)
            print("Success")
        except:
            traceback.print_exc()
            print("E:5 Got failure")
        f0()
#end
#Ignore move next without entering any command or data
    elif u0=="":
        f0()
#end
#print 'Enter command' if user input space
    elif u0==" ":
        print("Enter command!")
        f0()
#end
#clear command code -clear text
    elif u0=="clear":
        os.system("clear")
        f0()
#end
#delete file command code
    elif u0==m7:
        try:
            print("Enter File location to delete")
            u10=input("")
            print("File name")
            u11=input("")
#move it to custom recycle bin
            os.rename(u10,"/storage/emulated/0/Android_terminal/Android_terminal/LIB/Custom_Recycle_bin/"+u11)
            print("Do you want it to delete permanently?[yes/no]")
            u12=input("")
#ask user to delete it permanently
            if u12=="yes":
                print("It will be deleted after 20sec\nRecovery-File is at /storage/emeulated/0/Android_terminal/Android_terminal/LIB/Custom_Recycle_bin")
                time.sleep(20)
                os.remove("/storage/emulated/0/Android_terminal/Android_terminal/LIB/Custom_Recycle_bin/"+u11)
                print("Success")
            elif u12=="no":
                print("abort")
            else:
                print("We are considering it as no.Thank you\naborted")
        except:
            traceback.print_exc()
            print("E:6")
        f0()
#end
#version of Mr.Bedrock Terminal
    elif u0=="ver":
        print("Mr. Bedrock Terminal -V1.0")
        f0()
#end
#help - List commands
    elif u0=="help":
        print("delf-To delete file\ncf-create file\ncfol-To create folder\nclear-To clear\nexit-To exit\ndir-To directory\nrf-Read file\nwf-Write file\naf-Append file\nver-ver\npwd-Display Current directory\ndelfol=To delete folder\npython -V-To know version of python\nprint-To print text")
        f0()
#end
#pwd command return current directory
    elif u0=="pwd":
        print(os.getcwd())
        f0()
#end
#delete folder code
    elif u0=="delfol":
        try:
            print("Folder location:")
            u13=input("")
            shutil.rmtree(u13)
        except:
            print("E:7")
            traceback.print_exc()
        f0()
#end
#Python version command code
    elif u0=="python -V":
        os.system("python -V")
        f0()
#end
#input username command code
    elif u0=="username":
        print("Enter username")
        u17=input("")
#saves it at user.dat
        ff3=open("/storage/emulated/0/Android_terminal/Android_terminal/LIB/user.dat","w")
        ff3.write(u17)
        ff3.close()
        f0()
#end
#print command just like echo in cmd and etc but bit different
    elif u0=="print":
    	u00=input("")
    	print("> "+u00)
    	f0()
#end
#command not found
    else:
        print("Error:0 no command found")
        f0()
#end
#execution of f0() function
f0()
