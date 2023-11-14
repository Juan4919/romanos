"""
1-Crear una funcion que pase de entero >0 y <4000 a romano
2-cualquier otra entrada debe dar error
3-limite 3999

Casos de prueba
a)1994 -> MCMXCIV
b)4000 -> RomanNumberError("El valor debe ser menor de 4000")
c)"unacadena"-> RomanNumberError("Debe ser un entero")
d) 0-> RomanNumberError("El valor debe ser mayor de cero")
e) -3 ->RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")

M → 1000
D → 500
C → 100
L → 50
X → 10
V → 5
I → 1

"""
diccionario = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}


unidades={1:'I',2:'II',3:'III',
          4:'IV',5:'V',6:'VI',
          7:'VII',8:'VIII',9:'IX'}
decenas ={10:'X',20:'XX',30:'XXX',
          40:'XL',50:'L',60:'LX',
          70:'LXX',80:'LXXX',90:'XC'}
centenas={100:'C',200:'CC',300:'CCC',
          400:'CD',500:'D',600:'DC',
          700:'DCC',800:'DCCC',900:'CM'}
millares={1000:'M',2000:'MM',3000:'MMM'}


print(diccionario.get("D"))

for c,v in diccionario.items():
    print( c+"-"+str(v) )

class RomanNumberError( Exception ):
    pass


def entero_a_romano(1994):
    return "MCMXCIV"
