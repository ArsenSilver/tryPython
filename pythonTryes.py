from math import *
					#in order to get help() for an object you need first to create this obj, e.g. help(file)
chaos = ["Name 12.03.1998", "Last", (12,3,2019)]

try:

	Info = [None]

	Info[0] = (chaos[0][:chaos[0].index(" ")+1])+chaos[1] #or we may use split()
	Info.extend([chaos[0][(chaos[0].index(" ")+1):]])

	fullInfo = {
	"name": [Info[0]].copy(), #two vars a=b would change simultaniously(we have 'is' to check pointers)			#name has type list(), not str()
	"birth": Info[1]
	}
	fullInfo.update({"registred":chaos[2]})
	if(not(fullInfo["name"][0].islower()) and not(fullInfo["name"][0].isupper())):
		fullInfo["name"][0] = fullInfo["name"][0].lower()
		if(fullInfo["name"][0].count("n")==1):				#
			fullInfo["name"][0] = fullInfo["name"][0].replace(fullInfo["name"][0][0], fullInfo["name"][0].upper()[0])

	if (fullInfo["name"][0][:fullInfo["name"][0].index(" ")]\
										in "Name, Null"):        #del list[a:b:c] where d is step  
		fullInfo["name"][0] = input("input valid name\n")

except IndexError as my_error:
    file = open("IndexError", "w")
    print(str(my_error) + "\nfile {} is opened: ".format(str(file)) + str(file.writable())) #{0:.17f} to restrict digitals in float
    file.write(str(my_error))  # readlines() return a list! so you can use it with [] or as iter
    file.close()

except:
	print("other error\n")
even = list(filter(lambda x: x % 2 == 0,chaos[2]))
for i,val in zip(range(5),chaos[2]):# the same as enumerate([2,3,6])
	#it also may be multiple tuples	: for (k1, v1), (k2, v2)


class school_Student: #class school_Student(Student): inheritance
    def __init__(self, name):
        self.name = name

#we can generate lists using loops 
# [x**2 for x in range(21) if x % 2 == 0]

