
listen = list(range(0, 10))

def binarySearch(alist, value):

    first = 0
    last = len(alist)-1
    counter = 0
    found = False
    # steps = [0,1,2]
    while first<=last and not found:
        midpoint = (first + last)//2
        if value == alist[midpoint]:        
            found =  True 
            counter = counter+1
            # steps = steps.append(2)
            # print(steps)
        else:
            if value < alist[midpoint]:
                last = midpoint-1
                counter = counter+1
            else:
                if value > midpoint:
                    first = midpoint+1 
                    counter = counter+1

    # steps = []                
    # print(counter)

    return counter


# result = []

result = []
# print(counter)
# liste2 = listen
for tal in listen:
    print(str(tal) + " : " +str(binarySearch(listen,tal)))
    # print(binarySearch(listen,tal))

    


# for tal in listen:
	# print('fuck '+str(tal))
    # binarySearch(listen,tal)
	# if binarySearch(listen,tal):
		# result.append(3) 
		# print("... steps for tallet "+str(tal))

# print(result)












