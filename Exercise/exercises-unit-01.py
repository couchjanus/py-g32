'''       
What is the easiest way to convert kilometers to miles?
The easiest way to convert any given kilometer value to miles in python is by defining the conversion factor.

The conversion factor is a variable in which we store the number that has to be multiplied by the given kilometer value to get the output in miles.
Formula: 1 km = 0.621371 miles

We have to multiple any given value in a unit kilometer with 0.621371 to get the output in miles. Therefore the conversion factor for km to miles conversion is 0.621371.
Make sure to use float as data type as kilometers are not necessarily integer values.
'''                  
# uncomment the next line to take input from the user
# km = float(input("Value in unit kilometers: "))

km = 15

# defining conversion factor
conversion_factor = 0.621371

# calculate miles
miles = km * conversion_factor
print('%0.2f km is equal to %0.2f miles' %(km,miles))
# Output: 15.00 km is equal to 9.32 miles


# Python Program to Convert Celsius to Fahrenheit
'''
T(℉) = T(℃) x 9/5 + 32
Or, 
T(℉) = T(℃) x 1.8 + 32

To convert the value from python Celsius to Fahrenheit, we take the user’s Celsius temperature as input, convert it to Fahrenheit using the conversion formula, then display it. Look at the examples given below:

Input :
90

Output :
90.00 degrees Celsius is the same as 194 degrees Fahrenheit.

Input :
50

Output :
50.00 degrees Celsius is the same as 122 degrees Fahrenheit.

Input :
12

Output :
12 degrees Celsius is equal to 53.6 degrees Fahrenheit.
'''
cls = float(input(‘Enter temperature in Celsius: ‘))  
#calculate the Fahrenheit temperature
fah = (cls * 1.8) + 32  

print(‘%0.1f Celsius is equal to %0.1f degrees Fahrenheit’%(cls,fah))  
'''
Output
37.5 degrees Celsius is equal to 99.5 degrees Fahrenheit

What is the fastest way to convert Celsius to Fahrenheit?
To convert the temperatures from python Celsius to Fahrenheit and vice versa, understand these 2 formulas:

Formula to convert Celsius to Fahrenheit: 
(°C * 1.8) + 32 = °F
Formula to convert Fahrenheit to Celsius: 
(°F – 32) / 1.8 = °C

How do you convert Fahrenheit to Celsius?
To convert this, we need to keep the Fahrenheit to Celsius formula in mind. 
C = (F-32)/1.8
'''
# Fahrenheit to Celsius without Function
                    
print("Enter Temperature in Fahrenheit: ")
fahren = float(input())
celi = (fahren-32)/1.8
print("\nEquivalent Temperature in Celsius: ", celi)

# Output:
# Enter Temperature in Fahrenheit:
# 98
# Equivalent Temperature in Celsius
# 36.6666666666

                
# Fahrenheit to Celsius using Function
'''
As mentioned above, to convert the temperature of Fahrenheit to Celsius, the compiler takes the Fahrenheit values as the input and converts them to Celsius using the formula:
(°F – 32) / 1.8 = °C

Input :
90
Output :
90.00 degrees Fahrenheit is the same as 32.2222 degrees Celsius.

Input :
50
Output :
50.00 degrees Fahrenheit is the same as 1- degrees Celsius.

Input :
12
Output :
12 degrees Fahrenheit is the same as -11.1111 degrees Celsius.
FahToCel is a user-defined function that is used to convert Fahrenheit to Celsius temperatures. This function accepts a value as an argument and returns its Celsius equivalent.
'''
                  
def FahToCel(fah):
    return (fah-32)/1.8

print("Enter Temperature in Fahrenheit: ", end="")
fahren = float(input())
celi = FahToCel(fahren)
print("\nEquivalent Temperature in Celsius = {:.2f}".format(cel))

# Output:
# Enter Temperature in Fahrenheit:
# 98
# Equivalent Temperature in Celsius
# 36.6666666666


# a, b, c are lengths of the sides of the triangle
# s is semi-perimeter = (a + b + c) / 2
# Heron’s Formula is the formula to find the area of a triangle when its three sides are given,
# A = √{s(s-a)(s-b)(s-c)}

# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f'The area of the triangle is {area}')

# Output
# The area of the triangle is 14.70
