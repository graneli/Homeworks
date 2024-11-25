
text=input(str("Enter text: "))

found = False

if "small" in text:
    found = True
    print ("small")

if "tall" in text:
    found = True
    print ("tall")

if "middle" in text:
    found = True
    print ("middle")

if found == False:
    print("No such words as 'small', 'tall' or 'middle' were found in the text." )


