"""
This problem is an equation system with multiple solutions, But given some
restrictions the solution is only one.

Starting with:
a^2 + b^2 = c^2
a + b + c = 1000
a > 0
b > a
c > b

# 0 < a < -500*(sqrt(2)-2) = 0 < a < 293
# b = (1000*(a-500))/(a-1000)
# c = (-a^2+1000 a-500000)/(a-1000)
"""

if __name__ == "__main__":
    for a in range(1, 293):
        b = (1000*(a-500))//(a-1000)
        c = (-(a*a)+1000*a-500000)//(a-1000)
        if (a + b + c) == 1000:
            break
    print(a * b * c)
