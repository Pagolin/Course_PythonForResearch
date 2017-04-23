import matplotlib.pyplot as plt
import numpy as np

# linspace-> vector of linearly distributed values (first, last, number of values)
# other available distributions e.g. logspace(np.log10(start), np.log10(end), number of values)
x = np.logspace(-1,1,40)
# vector withelementwise squared x-arguments
y1 = x**3
y2 = x**4

"""
plotting a parabola
additional keyword arguments "bo-" => blue, circle markers, solid line
linewidth, makersize
"""
plotOb1 = plt.loglog(x,y1, "bo-", linewidth= 2, markersize= 4, label = "First")
plotOb2 = plt.loglog(x,y2, "rs-", linewidth= 2, markersize= 4, label = "Second")

"""
customizing plots
pyplot knows Latex syntax e.g. $ $ 
legend  : legen()
axis    : axis()
labels  : xlabel() ylabel()
save    : savefig() where format extension specifies the file format saved
scaling axes : plt.semilogx() semilogy loglog() for log 10 scales of x, y or both
"""
plt.xlabel("X")
plt.ylabel("Y")
# plt.axis([xmin, xmax, ymin, ymax])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")
plt.show()
