#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]

a = 1856
print(a)

# 2) Imprimir el tipo de dato de la constante 8.5
type(8.5)

# In[3]:





# 3) Imprimir el tipo de dato de la variable creada en el punto 1
type(a)
# In[8]:





# 4) Crear una variable que contenga tu nombre
my_name = "Lina María"
# In[2]:




# 5) Crear una variable que contenga un número complejo
num_comp = 52 + 7j
# In[3]:





# 6) Mostrar el tipo de dato de la variable crada en el punto 5
type(num_comp)
# In[4]:





# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var1 = "True"
var2 = True
# In[3]:





# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
type(var1)
Type(var2)
# In[5]:





# 10) Asignar a una variable, la suma de un número entero y otro decimal
b = 135 + 96.8
# In[1]:





# 11) Realizar una operación de suma de números complejos
c = 56j + 98
d = 65 + 23j
print(c+d)
# In[2]:





# 12) Realizar una operación de suma de un número real y otro complejo
e = 45.8 
f = 5 + 4j
print(e + f) 
# In[4]:





# 13) Realizar una operación de multiplicación
g = 6868787
h = 5567
print(g * h)
# In[5]:





# 14) Mostrar el resultado de elevar 2 a la octava potencia
2 ** 8
# In[6]:




# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)
# In[8]:





# 16) De la división anterior solamente mostrar la parte entera
print(27 // 4)
# In[9]:





# 17) De la división de 27 entre 4 mostrar solamente el resto
print(27 % 4)
# In[1]:





# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
x = 4 * 6 + 3
print(x)
# In[2]:





# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
nombre = "Lina María"
apellido = "Sanabria"
nombre_completo = nombre + " " + apellido

# In[3]:





# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
"2" == 2 
# In[4]:"2" == 2 





# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
resultado = int("2") == 2
# In[11]:resultado = int("2") == 2





# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float("3.8")
# In[12]:





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.
valor = 3
valor -= 1
# In[15]:





# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1 << 2
# In[29]:





# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
2 + "2"
# In[23]:






# 26) Realizar una operación válida entre valores de tipo entero y string
a = "te amo "
b = 5
print(a * b + "hasta el infinito")
# In[30]:



