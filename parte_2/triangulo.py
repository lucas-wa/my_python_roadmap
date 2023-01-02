class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):

        if (self.a == self.b and self.a == self.c):
            return "equilátero"
        
        elif  (self.a == self.b or self.a == self.c or self.b == self.c):
            return "isóceles"
        
        else:
            return "escaleno"
    
    def retangulo(self):
        sides = sorted([
            self.a,
            self.b,
            self.c
        ])


        return sides[0]**2 + sides[1]**2 == sides[2]**2
        
    def semelhantes(self, triangle):
        self_sides = sorted([
            self.a,
            self.b,
            self.c
        ])

        other_sides = sorted([
            triangle.a,
            triangle.b,
            triangle.c
        ])

        return self_sides[0] / other_sides[0] == self_sides[1] / other_sides[1]


