import matplotlib.pyplot as plt
print("WELCOME TO THE ONE DIMENSIONAL TRAJECTORY CALCULATOR, KEEP IN MIND THAT THE VALUES ARE IN SI UNITS.")

while True:
    v0 = input("Please type the velocity of the object (in m/s where a positive value will mean upwards direction): ")
    h0 = input("Please type the height of the object (in m): ")
    if h0.isdigit() and v0.lstrip("-").isdigit():
        h0 = float(h0)
        v0 = float(v0)
        break
    else:
        print("Please only write numerical values!")

rho = 1.225 #kg/m^3
m = 0.02 #kg
dt = 0.01 #s
A = 0.003928 #m^2
C_d = 0.47 #unitless
g = -9.8 #m/s^2
terminal_velocity = ((2*m*-g)/(rho*A*C_d))**(1/2) #m/s 
v = v0
t = 0
height = []
velocity = []
time = []
h = h0

while True:
    if v > 0:
        acceleration = ((m*g - (1/2)*rho*A*C_d*(v**2))/m)  #because of the formula we do not need to check the terminal velocity, it can never reach to that value anyways (due to laws of physics)
    elif v < 0:
        acceleration = ((m*g + (1/2)*rho*A*C_d*(v**2))/m)
    else:
        acceleration = m*g
    dv = acceleration*dt
    v = v + dv
    dh = v*dt
    h = h + dh 
    t = t + dt
    time.append(t)
    velocity.append(v)
    height.append(h)          
    if h < 0:
        break
    else:
        pass

plt.plot(time,velocity)
plt.plot(time,height)
plt.show()

MyF = open("S21.dat", "w")
MyF.write("Time     " + "Height     " + "Velocity     \n" )
for i in range(len(height)):
    MyF.write(str(time[i]) + " " + str(height[i]) +  " " + str(velocity[i]) +"\n")
MyF.close()

inF = open("S21.dat", "r")
file = inF.read()
print(file)
