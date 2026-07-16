#multiple inheritance using class A, class b and c

class A:
    varA ="this is class a"
class B:
    varB ="this is class b"
class C(A,B):
    varC = "this is class c"
c1 = C
print(c1.varA)
print(c1.varB)
print(c1.varC)
