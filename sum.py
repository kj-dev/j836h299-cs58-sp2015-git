"""
Kyle Jones
j836h299
project euler example program
"""

def get_total(mode):
	f= open("numbers.txt", 'r')
	stringer=f.read()

	l = []
	for val in stringer:
	    try:
	        l.append(int(val))
	    except ValueError:
	        pass

	if 'all' in mode:
		mode=len(l)
	else:
		mode=int(mode)

	total=0

	for x in range(1,mode):
		total=total+l[x]
		pass

	print("The total is: ",total)
	pass

def main():
	print("Do you want to calculate the first 10 digits or all of them? \n")
	mode=input("(10 or all): ")
	print(mode)
	get_total(mode)
	input("...")


main()
