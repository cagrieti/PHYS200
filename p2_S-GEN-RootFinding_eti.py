def root_finder(a,b,c):
    discriminant =(b**2-4*a*c)
    root_one = ((-b)+(discriminant**(1/2)))/(2*a)
    root_two = ((-b)-(discriminant**(1/2)))/(2*a)
    if discriminant > 0:
        print("The roots are real and they are: " + str(round(root_one,3)) + " and " + str(round(root_two,3)))

    elif discriminant < 0:
        discriminant = discriminant * -1
        print("The roots are imaginary and they are: " + str(round(-b/(2*a),3))+" + "+str(round(((discriminant**(1/2))/(2*a)),3))+"i and " + str(round(-b/(2*a),3))+ " - " +str(round(((discriminant**(1/2))/(2*a)),3))+"i")

    else:
        print("There is only one root which is real and it is: " + str(round(root_one,3)))

while True:
    N = input("\nEnter coefficients (e.g. 1,2,3): ")
    w = N.split(",")

    if len(w) != 3:
        print("You must enter three integers or floats.")
    elif float(w[0]) > 0:   # I initially used float(w[0) == 0.0 but I was adviced to not check for == 0 conditions unless it is an integer
        a = float(w[0])
        b = float(w[1])
        c = float(w[2])
        root_finder(a,b,c)
    elif float(w[0]) < 0:
        a = float(w[0])
        b = float(w[1])
        c = float(w[2])
        root_finder(a,b,c)
    else:
        print("This is not a quadratic equation.")
