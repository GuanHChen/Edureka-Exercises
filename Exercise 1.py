"""
Edureka Case Study 1
Receive input of name and ID and check if it is a customer.
"""


def customer_name(details):
    #This function will return customer name and store ID input value. 
    #Input is split into first, last, and id values
    
    global idnum
    idnum = ""
    first = ""
    last = ""

    inputlist = details.split()
    first = inputlist[0]
    last = inputlist[1]
    idnum = inputlist[2]
   
    return first + " " + last


customer_info = {"Callie Chen" : "0001"}


entry = input("Please state name and ID number (John Doe 0012): ")

try:
    name = customer_name(entry)
    if idnum == customer_info[name]:
        print("Authorized User, Welcome")
    else:
        print("Unauthorized User.")

except:
    print("Oh no! Something went wrong. Please try again.")
    

