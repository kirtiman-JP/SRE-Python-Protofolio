# simple type casting
a = "1"
b = "2"
print(int(a) + int(b))
print("-" * 20)
# explict type casting
string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print("The Sum of both numbers is:", sum)
print("-" * 20)
# implict type cating
#python automaticly converts a to int
a = 7
print(type(a))
# python automatically converts b to float
b = 3.0
print(type(b))
# python automatically converts C to float as it is an float addition
c = (a+b)
print("The value is:", c)
print(type(c))
print("-" * 20)
