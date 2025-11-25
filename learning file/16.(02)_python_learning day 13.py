#match case statement
#a clean way to check a variable against multiple fixed, known values.
#the subject we are checking:


current_day = (input("enter the day name: "))
print(f"Checking schedule for: {current_day}\n" + ("-" * 30 ))
#1. start the match block: The variable we are testing goes here.
match current_day:
    #2.check the first possible case m(pattern)
     case "Monday":
          print("Case 1 Matched: Start of the work feek focous on planning.")
    #3.check the second posssible case
     case "Tuesday":
          print("case 2 Matched: id week intensity. focus on execution.")
     case "Wednesday":
          print("Case 3 Matched: Hump day! Time for creative review")
     # use (OR) to check for multiple valuse in one case.
     case "Saturday" | "Sunday" | "Thursday" | "Friday":
          print("Case 4 Matched: Weekend! Time for drawing and deep sudy.")
     #5. the default case if no other case matches, this runs.
     #it must be simply written as 'case _:'
     case _:
          print("Default case matched: day is known but not priotrised in this block. maybe u can enjoy :)")
    #this code exists the match block and continues here 
print("-" * 30)
print("Match process complete.")

