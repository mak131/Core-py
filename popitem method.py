sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Original dict:")
print(sub)
print(id(sub))
print()



r = sub.popitem()

print("After Removing dict:")
print(sub)
print(id(sub))
print()
print("Remov value",r)