import matplotlib.pyplot as plt
import operator as o

x_list = [-2.0, -1.75, -1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75]
y_given_values = [37.00000, 24.16016, 15.06250, 8.91016, 5.00000, 2.72266, 1.56250, 1.09766, 1.00000, 1.03516, 1.06250, 1.03516, 1.00000, 1.09766, 1.56250, 2.72266, 5.00000, 8.91016, 15.06250, 24.16016]

# Plotting all given points in a line
plt.plot(x_list, y_given_values, label="original line")

# Best result (within computer truncation margin of error of original line) in reduced algebraic form
plt.plot(x_list, [(x**4)-2*(x**3)+(x**2)+1 for x in x_list], label="x^4 - 2x^3 + x^2 + 1") # fitness = 7.031250000466827e-12

# Model solution (to show that it gives the right answer)
#plt.plot(x_list, [o.add(o.add(o.sub(o.mul(o.mul(x, x), o.mul(x, x)), o.mul(o.add(1, 1), o.mul(o.mul(x, x), o.mul(x, 1)))), o.mul(x, x)), 1) for x in x_list], label="≡ x^4 - 2x^3 + x^2 + 1") # fitness = 7.031250000466827e-12

# Best three results in form given from algorithm (changed add,sub,mul,neg into o.add,o.sub.o.mul,o.neg to run)
plt.plot(x_list, [o.sub(o.mul(o.add(o.mul(o.add(o.sub(0, -1), o.add(-1, x)), o.mul(o.sub(x, 1), o.add(-1, x))), 1), x), o.add(-1, x)) for x in x_list], label="≡ x^4 - 2x^3 + x^2 + 1") # fitness = 7.031250000466827e-12
plt.plot(x_list, [o.mul(x, o.neg(o.mul(o.sub(o.add(-1, o.add(x, x)), o.mul(x, x)), x))) for x in x_list], label="line 2") # fitness = 1.0000037500070311
plt.plot(x_list, [o.mul(x, o.sub(o.sub(o.sub(o.neg(o.sub(1, x)), o.sub(o.neg(x), o.add(-1, x))), 1), o.neg(o.sub(o.sub(o.neg(o.sub(1, x)), o.sub(1, x)), 1)))) for x in x_list], label="line 3") # fitness = 10.904667050300002

# Some other results from the algorithm
#plt.plot(x_list, [o.mul(o.mul(o.mul(x, x), o.add(x, -1)), o.add(x, -1)) for x in x_list], label="new line 1")
#plt.plot(x_list, [o.sub(o.mul(o.add(o.add(-1, o.mul(o.add(o.sub(x, x), o.sub(x, -1)), 1)), o.mul(o.mul(x, x), o.add(x, -1))), o.add(-1, x)), 1) for x in x_list], label="new line 2")
#plt.plot(x_list, [o.sub(o.mul(o.add(x, x), o.add(x, x)), o.add(o.add(o.sub(o.sub(o.add(1, x), o.mul(-1, 0)), o.mul(x, x)), o.add(x, x)), o.add(o.add(x, x), x))) for x in x_list], label="new line 3")
#plt.plot(x_list, [o.add(o.mul(x, o.add(o.add(x, -1), -1)), o.mul(o.add(x, o.add(x, o.mul(o.neg(x), o.sub(x, x)))), o.add(x, o.add(o.add(x, -1), -1)))) for x in x_list], label="new line 4")
#plt.plot(x_list, [o.mul(o.sub(x, 1), o.add(x, o.add(o.add(o.add(x, x), x), x))) for x in x_list], label="new line 5")
#plt.plot(x_list, [o.sub(o.mul(o.sub(o.add(x, -1), o.neg(o.neg(o.mul(x, -1)))), o.sub(o.add(x, -1), o.neg(x))), o.neg(o.add(o.sub(x, x), o.neg(x)))) for x in x_list], label="new line 6")
#plt.plot(x_list, [o.mul(o.mul(1, o.sub(o.sub(x, 1), o.mul(x, -1))), o.add(o.sub(x, 1), x)) for x in x_list], label="new line 7")

# naming the x and y axes
plt.xlabel('x - axis'), plt.ylabel('y - axis')

plt.legend()
  
plt.show()