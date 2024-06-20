a=12
b=23.1
c="Dennis"
d=True
e=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

str="Welcome to coding"
str2=" at eMobilis Training Academy"

print(str[0:4])
print(str[5])
print(str+str2)     #concatenatination

majina=["Dennis","Kipyegon","Arthur","Morgan"]
print(type(majina))
majina[0]="Jack"
print(f"My name is {majina[0]}")

#tupledatatype

matunda=("Banana","Mangoes","Pineapples","Oranges")
print(f"I like eating {matunda[2]}")

magari=("Dodge","Jaguar","Bentley","Lincoln","Toyota")
print(f"I would like to own a {magari[0]}")

print(majina)
print(matunda)
print(magari)

mydict={"age":23,"salary":200000,"gender":"Male","name":"Dennis"}
print(f"My name is {mydict['name']}")
print(f"My age is {mydict['age']}")
print(f"My gender is {mydict['gender']}")
print(f"My salary is {mydict['salary']}")
