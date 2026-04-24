def diagnose():
    fever = input("Do you have fever? (yes/no): ")
    cough = input("Do you have cough? (yes/no): ")

    if fever == "yes" and cough == "yes":
        print("Possible Flu")
    elif fever == "yes":
        print("Possible Infection")
    else:
        print("You are fine")

diagnose()
