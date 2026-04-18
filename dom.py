def information():
    # 1. Ask for the input first
    name_input = input("Please input your name: ")
    age_input = input ("Please input your ages")
    
    # 2. Now you can print it because the variable exists
    print(f"Stored name: {name_input}")
    print(f"Stored age: {age_input}")

# Call the function
information()