name = "harry"
print("Hello\n" + name)
print('He said "I am good".')
#for multiple lines like this as we wanted many diff lines insted of continuing in one we either use (""") or (''') so whatever comes in this or is enclosed is considerd as string.
apple = """ Hello bro whats up?
what are you doing?
all good?
need any help?"""
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) this is index error cuse index 5 dosent exist in name variable
print("Lets use loop for\n")
for character in name:
    print(character)
for character in apple:
    print(character)