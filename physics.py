Function to find the speed of an object

def speed(distance, time):
return distance / time

Function to calculate the force of an object

def force(mass, acceleration):
return mass * acceleration

Function to calculate the weight of an object

def weight(mass):
return mass * 9.8

Function to calculate potential energy

def potential_energy(mass, height):
return mass * 9.8 * height

Function to calculate pressure

def pressure(force, area):
return force / area

Main program

def main():
print("WELCOME TO PHYSICS CALCULATOR")
print("--------------------------------")
print("Select the calculation you want to perform:")
print("1. Calculate Speed")
print("2. Calculate Force")
print("3. Calculate Weight")
print("4. Calculate Potential Energy")
print("5. Calculate Pressure")

option = input("Enter option (1-5): ")

if option == "1":
    d = float(input("Input distance in metres: "))
    t = float(input("Input time in seconds: "))

    if t <= 0:
        print("Time must be greater than zero.")
    else:
        result = speed(d, t)
        print("Speed:", result, "m/s")

elif option == "2":
    m = float(input("Input mass in kg: "))
    a = float(input("Input acceleration in m/s²: "))

    result = force(m, a)
    print("Force:", result, "N")

elif option == "3":
    m = float(input("Input mass in kg: "))

    result = weight(m)
    print("Weight:", result, "N")

elif option == "4":
    m = float(input("Input mass in kg: "))
    h = float(input("Input height in metres: "))

    result = potential_energy(m, h)
    print("Potential Energy:", result, "J")

elif option == "5":
    f = float(input("Input force in Newtons: "))
    ar = float(input("Input area in square metres: "))

    if ar <= 0:
        print("Area must be greater than zero.")
    else:
        result = pressure(f, ar)
        print("Pressure:", result, "Pa")

else:
    print("Wrong selection! Please choose a number from 1 to 5.")

main()
