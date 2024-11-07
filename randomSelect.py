import random

# Initialize the random number generator with a seed
random.seed(100000000)

# Get and set the state of the random number generator
state = random.getstate()
print("Current state of RNG:", state)
random.setstate(state)
print("State reset.")

# Generate random bits
print("Random bits:", random.getrandbits(8))  # Generates a random integer with 8 random bits

# Random number in range
print("Random number in range (1-100):", random.randrange(1, 100))

# Random integer between two numbers
print("Random integer (1-10):", random.randint(1, 10))

# Random choice from a sequence
fruits = ['apple', 'banana', 'cherry', 'date']
print("Random choice from list:", random.choice(fruits))

# Random selection of multiple elements from a sequence
print("Random selection from list:", random.choices(fruits, k=2))

# Shuffle a sequence
random.shuffle(fruits)
print("Shuffled list:", fruits)

# Random sample of elements from a sequence
print("Random sample of 2 elements:", random.sample(fruits, 2))

# Random float between 0 and 1
print("Random float (0-1):", random.random())

# Random float in a specified range
print("Random float between 5 and 10:", random.uniform(5, 10))

# Random float with triangular distribution
print("Triangular random float:", random.triangular(1, 10, 5))

# Random float based on Beta distribution
print("Beta variate (alpha=2, beta=5):", random.betavariate(2, 5))

# Random float based on Exponential distribution
print("Exponential variate (lambda=1.5):", random.expovariate(1.5))

# Random float based on Gamma distribution
print("Gamma variate (alpha=2, beta=2):", random.gammavariate(2, 2))

# Random float based on Gaussian distribution
print("Gaussian variate (mu=0, sigma=1):", random.gauss(0, 1))

# Random float based on Log-normal distribution
print("Log-normal variate (mu=0, sigma=1):", random.lognormvariate(0, 1))

# Random float based on Normal distribution
print("Normal variate (mu=0, sigma=1):", random.normalvariate(0, 1))

# Random float based on von Mises distribution
print("von Mises variate (mu=0, kappa=4):", random.vonmisesvariate(0, 4))

# Random float based on Pareto distribution
print("Pareto variate (alpha=2):", random.paretovariate(2))

# Random float based on Weibull distribution
print("Weibull variate (alpha=1, beta=1.5):", random.weibullvariate(1, 1.5))
