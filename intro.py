# this is a comment

x = 3 # intiger
y = 4.2 # floating point intiger
z = "# this is not a comment"
a = 'world'
b = x + y - x
c = 8 / 3
d = 8 // 3 # when you don't want the floating point part.  This is like math.floor in JS
e = 8 % 3 # this is moduls
f = 8 ** 3 # this is 8 to the 3rd power aka math.pow
g = z + a # concatinaztion


print(c, d, z, f, g) # this is like console.log .. it prints to the command line

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

age = 20
gender = 'female'

if age >= 21 and (gender == 'female' or gender == 'male'):
    print('go have a drink')
else:
    print('go have your parents buy you a drink')

for x in range(20, 50, -5):
    print(x)

for x in range(20, -50, -5):
    print("{0} to the {1} power is{2}".format(x, 2, x**2))
