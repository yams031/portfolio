animals = ['bear','cat','dog','elephant','fox','giraffe','snake','turtle']
first = 0
last = len(animals) - 1
notFound = True
t = input ("What animal are you looking for?")
term = t.lower()

while notFound == True and first < last:
    index = int((first + last)/2)
    if animals [index] == term:
        print ("Found the", term, "!")
        notFound = False
    else:
        if term < animals [index]:
            last = index - 1
        else:
            first = index + 1
    if notFound==True:
        print("Sorry, the", term, "was not found!")
