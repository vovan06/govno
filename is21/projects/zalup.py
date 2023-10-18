x_n = float(input())
h = float(input())

f = input()

x1 = x_n + h
x2 = x_n - h
del_x = 2 * h

f_n1 = f(x1)
f_n2 = f(x2)

f_1 = (f_n1 - f_n2)/del_x
 