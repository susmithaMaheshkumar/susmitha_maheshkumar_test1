## Program is to find the greates of the both entered version strings
def get_input(text):
    return input(text)

def inputvalues():
    version1 = get_input('Please Enter the First version string: ')
    version2 = get_input('Please Enter the second version string: ')
    #check version1 and version2 is a number 
    try:
        floatversion1 = float(version1)
        floatversion2 = float(version2)
    except ValueError:
        return (-1,-1)
    return ((floatversion1),(floatversion2))

def greateststringcal(stringvalue1,stringvalue2):
    if stringvalue1 > stringvalue2:
        return (str(stringvalue1) +' is greater than '+ str(stringvalue2))
    elif stringvalue2 == stringvalue1:
         return (str(stringvalue1) +' is Equal to '+ str(stringvalue2))
    else:
        return (str(stringvalue1) +' is lesser than '+ str(stringvalue2))


def inputvaluevalidation():
    while True:
        value1,value2 = inputvalues()
        if value1 != -1 and value2 != -1:
           break
