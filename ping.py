import subprocess as sp

def ipcheck():
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
    if status == 0:
        print("System " + str(pop) + " is UP !")
    else:
        print("System " + str(pop) + " is DOWN !")


pop = input("Enter the ip address: ")
ipcheck()
