def fizzBuzz(a):
	if(a%3==0):
		if(a%5==0):
			return 3
		return 0
	elif(a%5==0):
		return 2 
	else:
		return 1

def printOut():
	x=1
	f="fizz"
	b="buzz"
	fb="fizzBuzz"
	for x in range(1,100):
		if(fizzBuzz(x)==1):
			print(x)
		elif(fizzBuzz(x)==0):
			print(f) 
		elif(fizzBuzz(x)==2):
			print(b)
 		elif(fizzBuzz(x)==3):
			print(fb)
			
			
printOut() 
