# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if type(numero) != int:
        return None
    if numero <=1:
        return None
    
    #esta parte no la entiendo:
    factorial = 1
    while (numero > 1):
        factorial = factorial * numero      #(factorial*=numero)
        numero = numero - 1                 #(numero-=1)
    return factorial

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    
    #El chequeo del tipo de dato debe realizarse al principio de la función.
    if type(valor) != int:
        return None
    # Si el valor es menor o igual a 1, no es primo
    if valor <= 1:
        return False

    # Comprobar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(valor ** 0.5) + 1):
        if valor % i == 0:
            return False
        
    return True
    

    
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self, especie, color): #la edad no la coloco en el init. 
            #ahora se inicializa en cero directamente dentro del método __init__, sin importar si se pasa o no 
            # un valor de edad al crear una nueva instancia de la clase Animal. 
            # De esta manera, cada vez que cree una nueva instancia de Animal, la edad se establecerá 
            # automáticamente en cero.
            self.edad = 0
            self.especie = especie
            self.color = color
        
        #no es necesaria esta instancia:
        # animalito1 = Animal (8,"perrito", "amarillo")

        def CumplirAños (self):
            self.edad = self.edad + 1
            return self.edad

    return Animal(especie,color)


