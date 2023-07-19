import numpy
N,M = map(int, input().split(" "))
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(round(numpy.std(A, axis = None),11))
