#Ahora subimos de nivel mental -> Predice esto:
class A:
    def __call__(self):
        return "Soy callable"

a = A()

print(callable(a))
print(a())

#Que pasó realmente?
#..1! Callable(a) -> Python verifica: ¿El objeto tiene denifido el método __call__? y si lo tiene entonces devuelve True
#...2! a() Cuando lo haces, python lo traduce internamente como: a__call__() y eso retorna "Soy callable"
