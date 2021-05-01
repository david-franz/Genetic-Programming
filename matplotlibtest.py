import matplotlib.pyplot as plt
  
class  eval:
	def add(x, y):
		return x + y

	def sub(x, y):
		return x - y

	def neg(x):
		return -x

	def mul(x,y):
		return x * y


x_list = [-2.0, -1.75, -1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75]
y_given_values = [37.00000, 24.16016, 15.06250, 8.91016, 5.00000, 2.72266, 1.56250, 1.09766, 1.00000, 1.03516, 1.06250, 1.03516, 1.00000, 1.09766, 1.56250, 2.72266, 5.00000, 8.91016, 15.06250, 24.16016]
  
# 3 function results
#y_list3 = [(x - 1) * (x + (((-x) * (x + 1) + (x**3)))) for x in x_list]


# plotting the points 
plt.plot(x_list, y_given_values, label="original line")

plt.plot(x_list, [(5 * x) * (x - 1) for x in x_list], label = "5x(x+1)")
plt.plot(x_list, [(-(x * ((x**2) - x) - ((x**2) - x)))* (-x) for x in x_list], label = "line 2")
#plt.plot(x_list, [(x - 1) * (x + (((-x) * (x + 1) + (x**3)))) for x in x_list], label = "line 3")

# this is the same as the above function (just algebraically simplified)
#plt.plot(x_list, [(x**4)-2*(x**3)+(x**2) for x in x_list], label = "x^4 + -2x^3 + x^2")

# I added these to experiment with just plugging the result that prints out directly into the plot
plt.plot(x_list, [eval.add(eval.add(-1, eval.neg(1)), eval.mul(eval.sub(x, 1), eval.add(eval.add(x, eval.add(eval.add(x, x), x)), eval.add(-1, x)))) for x in x_list], label="new line1")
plt.plot(x_list, [eval.add(eval.mul(eval.add(eval.add(eval.mul(x, eval.mul(x, eval.add(-1, x))), 0), eval.add(x, -1)), eval.add(-1, x)), eval.sub(x, eval.mul(x, eval.add(-1, x)))) for x in x_list], label="new line2")
  
# naming the x and axes
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.legend()
  
plt.show()