def add(firstName:str|list[int  ], lastName:str):
    firstName.capitalize()
    return firstName+  " " +lastName


fName = "bill"
lName = "gates"


name=add(fName,lName)

print(name)