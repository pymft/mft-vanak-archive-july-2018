class A:
    def speak(self):
        print("A")

class B:
    def speak(self):
        print("B")


class B2:
    def speak(self):
        print("B2")

class C(A, B):
    def speak(self):
        print("C")

class D(B, A):
    def speak(self):
        print("D")

class E(C, B2):
    def speak(self):
        print("E")


print('0')