

#Try to find the file from AWS that is downloaded


with open("http_access_log.txt") as file_in:
    #Set array to look for specific data
    array = []
    for line in file_in:
        array.append(line)

 # begin with 0       

count = 0



# try to find the months you are looking for in the data 


for i in array:
    if i.find("Apr") != -1 and i.find("1995") != -1 and i.find("[11") != -1:
        count += 1
    elif i.find("May") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jun") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jul") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Aug") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Sep") != -1 and i.find("1995") != -1:
        count += 1
        array[count] = i
    elif i.find("Oct") != -1 and i.find("1995") != -1:
        count += 1



#count all the entries by using the array (gives us boundaries) function inside a len (counts the length) function


countall = len(array)

# Use print to see the results from the selected entry 


print("Total Number of Requests in the past six months: ", count)
print("Total Number of Requests: ", countall)