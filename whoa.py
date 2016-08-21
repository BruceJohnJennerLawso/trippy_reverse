## whoa.py #####################################################################
## squares and reverses ########################################################
################################################################################

class reversibleInteger:
	def __init__(self, value=0):
		self.digits = []
		increment = 1
		while(value != 0):
			self.digits.append(0)
			while(value%(10**increment) != 0):
				value -= (10**(increment -1))
				self.digits[increment - 1] += 1
			increment += 1
			
			
	def printValue(self):
		for place in reversed(self.digits):
			print place,
		print "\n"
		
	def getReversed(self):
		output = reversibleInteger()
		for cy in reversed(self.digits):
			output.digits.append(cy)
		return output
		
	def getValue(self):
		output = 0
		power = 0
		for cy in self.digits:
			output += (cy*(10**(power)))
			##print cy, power, output
			power += 1
		return output
			


if(__name__ == "__main__"):
	hits = 0
	
	lowerBound = 11
	upperBound = 9000
	for cy in range(lowerBound, upperBound):
		value = reversibleInteger(cy)
		reverseValue = reversibleInteger(value.getValue()).getReversed().getValue()
		
		if((reversibleInteger(cy**2).getReversed().getValue()) == (reversibleInteger(reverseValue**2).getValue())):
			print "%d, squared %d, %d reversed, %d reverse squared" % (cy, cy**2, reverseValue, reverseValue**2),
			print "hit"
			hits += 1

	print "%d hits in range(%d, %d)" % (hits, lowerBound, upperBound)		
	
	#print 422
	#foo = reversibleInteger(422)
	#foo.printValue()
	#bar = foo.getReversed()
	#bar.printValue()
	#print bar.getValue()
