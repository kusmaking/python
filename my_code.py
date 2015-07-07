def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]


def square(n):
   return n * n 

#p = 85
print square (5)




# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.



def abbaize (a,b):
    return a + b + b + a


print abbaize ('dog','cat')




#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'

def sum (a,b):
	a = a + b
	return a

print sum (2,123)