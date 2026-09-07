import matplotlib.pyplot as plt
import math as math

def plot_function(fun_str, domain, ns):

    #list for xs and ys
    xs = []
    ys = []

    #store min and max values from domain
    x_min, x_max = domain[0], domain[1]

    #distance btwn points
    dx = (x_max - x_min)/ ns

    ##Starting points for graphing loop
    #loop for evening out the ns sample points into xs
    for i in range(ns):
        x = x_min + i *dx
        xs.append(x)

    #loop for results of fun_str eval into ys
    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    ##table formating
    #display view
    print("{:10} {:10}". format("x", "y"))

    #loop to interate through lists onto table for viewing
    for i in range(ns):
        print("{:<10.2f} {:<10.2f}".format(xs[i], ys[i]))

    ##plotting onto graph and labels for graph
    plt.plot(xs, ys, "rx-")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    
    plt.show()


fun_str = input("Enter a function with the variable x: ")
ns = int(input("Enter the number of samples you'd like to see: "))
x_min = float(input("Enter xmin: "))
x_max = float(input("Enter xman: "))

#combine the min and max to create domain variable
domain = (x_min, x_max)

#testing
#print(domain)
#print(fun_str)

plot_function(fun_str, domain, ns)

