class PrecalcOperations:
    """A class to perform basic precalculus operations."""
    
    def __init__(self):
        pass
    
    def factorial(self, n):
        """Returns the factorial of a non-negative integer n."""
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)
    
    def power(self, base, exponent):
        """Returns base raised to the power of exponent."""
        return base ** exponent
    
    def quadratic_formula(self, a, b, c):
        """Solves a quadratic equation ax^2 + bx + c = 0 and returns the roots."""
        import math
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real roots"
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
    def gcd(self, a, b):
        """Returns the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        """Returns the least common multiple of a and b."""
        return abs(a * b) // self.gcd(a, b)
    
# Example usage
if __name__ == "__main__":
    precalc = PrecalcOperations()
    print("Factorial of 5:", precalc.factorial(5))
    print("2^3:", precalc.power(2, 3))
    print("Quadratic roots of x^2 - 3x + 2:", precalc.quadratic_formula(1, -3, 2))
    print("GCD of 36 and 24:", precalc.gcd(36, 24))
    print("LCM of 6 and 8:", precalc.lcm(6, 8))
