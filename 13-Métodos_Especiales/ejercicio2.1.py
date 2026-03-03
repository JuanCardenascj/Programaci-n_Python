#Ahora te hago una pregunta conceptual fuerte --> Si hago esto:
class A:
    def __new__(cls):
        print("New")
        return super().__new__(cls)

    def __init__(self):
        print("Init")

a = A
b = A()

print(type(a))
print(type(b))
print(type(type(A)))