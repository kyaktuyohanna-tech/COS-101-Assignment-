
# PHYSICS FORMULA CALCULATOR

# Function 1: Speed = Distance / Time
def calculate_speed():
    distance = float(input("Enter distance (meters): "))
    time = float(input("Enter time (seconds): "))

    speed = distance / time
    print("Speed =", speed, "m/s")


# Function 2: Force = Mass × Acceleration
def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))

    force = mass * acceleration
    print("Force =", force, "N")


# Function 3: Density = Mass / Volume
def calculate_density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))

    density = mass / volume
    print("Density =", density, "kg/m³")


# Function 4: Work Done = Force × Distance
def calculate_work():
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))

    work = force * distance
    print("Work Done =", work, "J")


# Function 5: Weight = Mass × Gravity
def calculate_weight():
    mass = float(input("Enter mass (kg): "))
    gravity = float(input("Enter gravitational acceleration (m/s²): "))

    weight = mass * gravity
    print("Weight =", weight, "N")


# Main Program
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Density")
    print("4. Calculate Work Done")
    print("5. Calculate Weight")

    choice = input("\nChoose a formula (1-5): ")

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_density()

    elif choice == "4":
        calculate_work()

    elif choice == "5":
        calculate_weight()

    else:
        print("\nThe option you selected does not exist.")

        answer = input("Do you still want to calculate? (yes/no): ").lower()

        if answer == "yes":
            continue

        elif answer == "no":
            print("Thank you for using the Physics Calculator!")
            break

        else:
            print("Invalid response. Program terminated.")
            break

    # Ask whether the user wants another calculation
    answer = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if answer == "no":
        print("Thank you for using the Physics Calculator!")
        break

    elif answer == "yes":
        continue

    else:
        print("Invalid response. Program terminated.")
        break