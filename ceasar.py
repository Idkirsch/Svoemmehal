
# text = raw_input("Enter the text : ") 
text = "haha^hehe"
termsAmount = len(text) 
counter = 0

print(str(termsAmount)+" terms")
print("Text: "+text)


# Logic in terms (characters)

# counterArray = list(range(0, termsAmount))
# print(counterArray)

for term in text:
	# print(term)
	# if term == "h":
		# print("HAHA")
	# if term != "^":
		# print(term)
	
	print("Count: "+str(counter))
	print("Term: "+str(term))

	if term == "^":


		
		print("OH! A HAT!")
		# Ikke printe hatten 
		# Ikke printe term før hatten
		# if den efterfølgende character OGSÅ er "^"-tjek

	

	# print("Prev char: "+str(text[counter-1]))
	
		# print(type(term))

	# print(text[2])

	counter = counter + 1
