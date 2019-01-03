def atomicdictionary():
    
    mydict={"H":"Hydrogen","He":"Helium","Li":"Lithium","Be":"Berilium","Bo":"Boron","C":"Carbon","Li1":"Lithium"}
    print(mydict)

    answer="y"
    while answer=="y" or answer=="Y":
        key=input("Enter the atomic symbol: ")   
        value=input("Enter the Element: ")
        #Do the same as searching for element before accepting a value
        mydict[key]=value
    answer=input("Do you want to enter more values? Y/N: ")
   
   
    print("Updated Table:")   
    print(mydict)

    print("Number of elements:", len(mydict))

    search=input("Enter element to Search: ")
    flag=0
    for x in mydict:
        if x==search:
            flag=1
            break
    for x in mydict.values():
        if x==search:
            flag=1
            break
    
    if(flag is 1):
        print("Element found")
    else:
        print("Not Found")    
