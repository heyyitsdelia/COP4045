import matplotlib.pyplot as plt
import math as math

#while infitie loop for user input on coefficients
while True:
    #get user input for a first to determine continuation of loop
    a = input("please provide a coefficient for a: ")
    if a == "":
        False

    else:#get remaining coefficients including a
        a = float(a)
        b = float(input("please provide a coefficient for b: "))
        c = float(input("please provide a coefficient for c: "))

        #first condition
        if b**2 - 4*(a*c) < 0:
            print("no real solutions")

            ##plotting for no real roots
            #center function domain around x_opt max and min
            x_opt = -b/(2*a)
            fx_min = x_opt - 2
            fx_max = x_opt + 2


        #second condition
        elif b**2 - 4*(a*c) == 0:
            x1 = -b/(2*a)
            print("one solution: ", x1)

            ##making root visible since there is one root
            fx_min = x1 - 4
            fx_max = x1 + 4


        #third condition
        else: 
            #use formula to get the two solutions
            formula = b**2 - 4*(a*c) 

            x1 = (-b + math.sqrt(formula)) / (2*a)
            x2 = (-b - math.sqrt(formula)) / (2*a)

        
            print("two solutions: {}, {} ", format(x1, x2))

            ##making root visible since there is two roots
            fx_min = x2 - 4
            fx_max = x1 + 4

        ##graphing portion of question 1
        #chart figures
        xs = []
        ys = []

        #graphing variables
        n = 150
        x0 = fx_min
        x1 = fx_max 
        x = x0
        dx = (x1 - x0)/ n #delta bwtn points

        i = 0

        while i < n:
            xs.append(x)

            y = a*x**2 + b*x +c
            ys.append(y)

            x = x + dx
            i = i + 1

        plt.plot(xs, ys, "rx-")
        plt.show()




