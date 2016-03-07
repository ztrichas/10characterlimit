#! /usr/bin/python


#Open the input.txt file
#Write the same data to the output.txt file
#If length of a line > 10 print first 10 characters only

f = open("input.txt", "r+")
f2 = open("output.txt", "r+") 

lines = f.read()


for currentLine in lines: 
	if len(currentLine) < 10:
		f2.write(currentLine)
	else: 
		f2.write(currentLine [0:10])
		#Add \n
		#f.read().splitlines()


f.close()
f2.close()