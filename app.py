print("Welcome to my Python program!") 
hours = input("How many hours did you study today?") # input promt for later calculation
hours = float(hours)
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours} this week.") # output calculation 
try: # basic error handling
    hours = float(hours)
# assume the same number of hours each day for a week
    weekly_hours = hours * 7 
except ValueError:
    print("Please enter a valid number.")
    
    print(f"If you study {hours:.1fr} hours per day,")
    print(f" you will study about {weekly_hours:.1f} hours this week.")

# (Optional) small encouragement message
    if weekly_hours >= 14:
        print("Nice job! You are putting in solid study time.")
    else:
        print("Consider adding a bit more study time to reach your goals.")

# Task 6 – Final cleanup & comments: program entry point
if __name__ == "__main__":
    print("Program finished. Good Luclk with your studies!")
