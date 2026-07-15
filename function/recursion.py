#recursion function
from ast import main


def factorial(n):
    print("factorial() called with", n)
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  



# int factorial(int n) {
#   print("factorial() called with $n");

#   if (n == 1) {
#     return 1;
#   }

#   return n * factorial(n - 1);
# }

# void main() {
#   print(factorial(5));
# }


# sum of n natural numbers using recursion
def sum_natural(n):
    print("sum natural number",n)
    if n ==1:
        return 1
    return sum_natural(n-1)+n
print(sum_natural(5))