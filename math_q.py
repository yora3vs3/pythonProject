import math
import cmath

# Data points for demonstration
angle_deg = 45
angle_rad = math.radians(angle_deg)
value1 = 0.5
value2 = 1.0
point1 = (3, 4)
point2 = (6, 8)

# 1. Trigonometric functions
print(f"Angle (degrees): {angle_deg}")
print(f"Angle (radians): {angle_rad}")
print(f"Cosine: {math.cos(angle_rad)}")
print(f"Sine: {math.sin(angle_rad)}")
print(f"Tangent: {math.tan(angle_rad)}")
print(f"Arc Cosine: {math.acos(value1)}")
print(f"Arc Sine: {math.asin(value1)}")
print(f"Arc Tangent: {math.atan(value1)}")
print(f"Hyperbolic Cosine: {math.cosh(value1)}")
print(f"Inverse Hyperbolic Sine: {math.asinh(value1)}")

# 2. Distance and Norms
distance = math.dist(point1, point2)
print(f"\nEuclidean Distance between {point1} and {point2}: {distance}")

norm = math.hypot(point1[0], point1[1])  # Hypotenuse from origin to point1
print(f"Euclidean Norm of {point1}: {norm}")

# 3. Rounding and Truncation
value = 5.678
print(f"\nOriginal Value: {value}")
print(f"Rounded Up: {math.ceil(value)}")
print(f"Rounded Down: {math.floor(value)}")
print(f"Truncated Value: {math.trunc(value)}")

# 4. Logarithmic and Exponential Functions
print(f"\nNatural Logarithm of {value2}: {math.log(value2)}")
print(f"Logarithm base 10 of {value2}: {math.log10(value2)}")
print(f"Exponential of {value1}: {math.exp(value1)}")
print(f"e raised to the power of {value1} - 1: {math.expm1(value1)}")

# 5. Combinatorial Functions
n, k = 5, 3
print(f"\nCombinations of choosing {k} from {n}: {math.comb(n, k)}")
print(f"Permutations of choosing {k} from {n}: {math.perm(n, k)}")

# 6. Factorial, GCD, and LCM
num = 6
print(f"\nFactorial of {num}: {math.factorial(num)}")

num1, num2 = 36, 60
print(f"Greatest Common Divisor (GCD) of {num1} and {num2}: {math.gcd(num1, num2)}")

# 7. Constants
print("\nMathematical Constants:")
print(f"Pi: {math.pi}")
print(f"Euler's Number (e): {math.e}")
print(f"Tau (2π): {math.tau}")
print(f"Infinity: {math.inf}")
print(f"NaN (Not a Number): {math.nan}")

# 8. Error Function and Complementary Error Function
print(f"\nError Function of {value1}: {math.erf(value1)}")
print(f"Complementary Error Function of {value1}: {math.erfc(value1)}")

# 9. Absolute Value and Copysign
value = -10.5
positive_value = math.fabs(value)
print(f"\nAbsolute Value of {value}: {positive_value}")
print(f"Copy Sign of {value1} to {value2}: {math.copysign(value1, value2)}")

# 10. Advanced Use Cases: Hypotenuse, Isclose, and Trigonometric Angle Conversion
# Convert radians to degrees and check if close to original degrees
angle_in_degrees = math.degrees(angle_rad)
print(f"\nRadians to Degrees Conversion: {angle_in_degrees}")

# Check if two floating-point numbers are close within a tolerance
is_close = math.isclose(angle_deg, angle_in_degrees, rel_tol=1e-5)
print(f"Is {angle_deg} close to {angle_in_degrees}? {is_close}")

# 11. Custom function using sqrt, pow, and dist for 3D distance
def distance_3d(pointA, pointB):
    return math.sqrt(math.pow(pointB[0] - pointA[0], 2) +
                     math.pow(pointB[1] - pointA[1], 2) +
                     math.pow(pointB[2] - pointA[2], 2))

point3D1 = (1, 2, 3)
point3D2 = (4, 5, 6)
print(f"\n3D Distance between {point3D1} and {point3D2}: {distance_3d(point3D1, point3D2)}")

# 12. Using math.prod() to compute the product of an iterable
numbers = [1, 2, 3, 4, 5]
product = math.prod(numbers)
print(f"\nProduct of {numbers}: {product}")

# 13. Using log and exponential functions for compound interest calculation
def compound_interest(principal, rate, times_compounded, years):
    return principal * math.pow((1 + rate / times_compounded), times_compounded * years)

principal = 1000  # Initial amount
rate = 0.05  # Interest rate of 5%
times_compounded = 4  # Compounded quarterly
years = 10
final_amount = compound_interest(principal, rate, times_compounded, years)
print(f"\nFinal amount after {years} years with compound interest: {final_amount}")


# Sample complex number for testing
z = complex(2, 3)  # z = 2 + 3j

# Demonstrating cmath functions
print("Complex number z:", z)
print("Real part of z:", z.real)
print("Imaginary part of z:", z.imag)

# Trigonometric and hyperbolic functions
print("\nTrigonometric and Hyperbolic Functions:")
print("acos(z):", cmath.acos(z))
print("acosh(z):", cmath.acosh(z))
print("asin(z):", cmath.asin(z))
print("asinh(z):", cmath.asinh(z))
print("atan(z):", cmath.atan(z))
print("atanh(z):", cmath.atanh(z))
print("cos(z):", cmath.cos(z))
print("cosh(z):", cmath.cosh(z))
print("sin(z):", cmath.sin(z))
print("sinh(z):", cmath.sinh(z))
print("tan(z):", cmath.tan(z))
print("tanh(z):", cmath.tanh(z))

# Exponential and logarithmic functions
print("\nExponential and Logarithmic Functions:")
print("exp(z):", cmath.exp(z))
print("log(z):", cmath.log(z))
print("log10(z):", cmath.log10(z))

# Phase and polar conversion
print("\nPhase and Polar Coordinates:")
print("phase(z):", cmath.phase(z))  # Returns phase of z in radians
print("polar(z):", cmath.polar(z))  # Returns polar form (r, phase) of z
print("rect(r, phase):", cmath.rect(*cmath.polar(z)))  # Convert polar back to rectangular

# Mathematical constants
print("\nMathematical Constants:")
print("Euler's number (cmath.e):", cmath.e)
print("PI (cmath.pi):", cmath.pi)
print("Tau (cmath.tau):", cmath.tau)

# Special values and checks
print("\nSpecial Values and Checks:")
print("isclose(z, complex(2, 3)):", cmath.isclose(z, complex(2, 3)))  # True if z is close to 2+3j
print("isfinite(z):", cmath.isfinite(z))  # True if z is finite
print("isinf(cmath.inf):", cmath.isinf(cmath.inf))  # True as cmath.inf is positive infinity
print("isnan(cmath.nan):", cmath.isnan(cmath.nan))  # True as cmath.nan is Not a Number

# Square root and special number operations
print("\nSquare Root and Special Operations:")
print("sqrt(z):", cmath.sqrt(z))  # Square root of z
print("pow(z, 2):", cmath.exp(2 * cmath.log(z)))  # Equivalent to z squared
print("abs(z):", abs(z))  # Magnitude of z
print("conjugate(z):", z.conjugate())  # Conjugate of z

# Using constants in expressions
print("\nUsing Constants in Expressions:")
print("cmath.e ** cmath.pi:", cmath.exp(cmath.pi * 1j))  # Euler's formula: e^(i * pi) ≈ -1

# Example with infinity and NaN
try:
    inf_result = z / cmath.inf  # Result should be 0j
    print("z / cmath.inf:", inf_result)
except ValueError as e:
    print("Error with infinity:", e)

try:
    nan_result = cmath.sqrt(cmath.nan)  # Result should be nan + nanj
    print("sqrt(cmath.nan):", nan_result)
except ValueError as e:
    print("Error with NaN:", e)

# Demonstrating complex infinity (infj) and complex NaN (nanj)
print("\nComplex Infinity and NaN:")
print("Complex infinity (cmath.infj):", cmath.infj)
print("Complex NaN (cmath.nanj):", cmath.nanj)

# Operations involving complex infinity and NaN
print("cmath.isinf(cmath.infj):", cmath.isinf(cmath.infj))  # Check for complex infinity
print("cmath.isnan(cmath.nanj):", cmath.isnan(cmath.nanj))  # Check for complex NaN
