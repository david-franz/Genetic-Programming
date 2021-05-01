import matplotlib.pyplot as plt
import operator as o

x_list = [-2.0, -1.75, -1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75]
y_given_values = [37.00000, 24.16016, 15.06250, 8.91016, 5.00000, 2.72266, 1.56250, 1.09766, 1.00000, 1.03516, 1.06250, 1.03516, 1.00000, 1.09766, 1.56250, 2.72266, 5.00000, 8.91016, 15.06250, 24.16016]

# plotting the points 
plt.plot(x_list, y_given_values, label="original line")

#plt.plot(x_list, [(5 * x) * (x - 1) for x in x_list], label="5x(x+1)") # get a proper unsimplified version
#plt.plot(x_list, [(-(x * ((x**2) - x) - ((x**2) - x)))* (-x) for x in x_list], label="line2")
#plt.plot(x_list, [(x - 1) * (x + (((-x) * (x + 1) + (x**3)))) for x in x_list], label="line3")

# this is the same as the above function (just algebraically simplified)
#plt.plot(x_list, [(x**4)-2*(x**3)+(x**2) for x in x_list], label="x^4 + -2x^3 + x^2")
plt.plot(x_list, [(x**4)-2*(x**3)+(x**2)+1 for x in x_list], label="x^4 - 2x^3 + x^2 + 1")

# I added these to experiment with just plugging the result that prints out directly into the plot
# lower fitness is better
#plt.plot(x_list, [o.add(1, o.mul(o.mul(o.mul(o.add(x, -1), x), o.sub(x, 1)), x)) for x in x_list], label="new_line1") # 1.4062500000933654e-10 fitness
#plt.plot(x_list, [o.mul(o.mul(o.mul(x, x), o.add(x, -1)), o.add(x, -1)) for x in x_list], label="new_line2") # 20.000075000140622 fitness
#plt.plot(x_list, [o.sub(o.mul(o.add(o.add(-1, o.mul(o.add(o.sub(x, x), o.sub(x, -1)), 1)), o.mul(o.mul(x, x), o.add(x, -1))), o.add(-1, x)), 1) for x in x_list], label="new_line3") # 71.66407656264062 fitness
#plt.plot(x_list, [o.sub(o.mul(o.add(x, x), o.add(x, x)), o.add(o.add(o.sub(o.sub(o.add(1, x), o.mul(-1, 0)), o.mul(x, x)), o.add(x, x)), o.add(o.add(x, x), x))) for x in x_list], label="new_line4") # 202.67154100600004 fitness
#plt.plot(x_list, [o.add(o.mul(x, o.add(o.add(x, -1), -1)), o.mul(o.add(x, o.add(x, o.mul(o.neg(x), o.sub(x, x)))), o.add(x, o.add(o.add(x, -1), -1)))) for x in x_list], label="new_line5") # 218.09334100600003 fitness
#plt.plot(x_list, [o.mul(o.sub(x, 1), o.add(x, o.add(o.add(o.add(x, x), x), x))) for x in x_list], label="new_line6") # 233.929241006 fitness
#plt.plot(x_list, [o.sub(o.mul(o.sub(o.add(x, -1), o.neg(o.neg(o.mul(x, -1)))), o.sub(o.add(x, -1), o.neg(x))), o.neg(o.add(o.sub(x, x), o.neg(x)))) for x in x_list], label="new_line7") # 248.46937850600008 fitness
#plt.plot(x_list, [o.mul(o.mul(1, o.sub(o.sub(x, 1), o.mul(x, -1))), o.add(o.sub(x, 1), x)) for x in x_list], label="new_line8") # 272.430278506 fitness

# naming the x and y axes
plt.xlabel('x - axis'), plt.ylabel('y - axis')

plt.legend()
  
plt.show()