# Laboratorio Nro. 01

## Funciones Elementales de Criptografía

### Texto Plano
```
Hay golpes en la vida, tan fuertes... ¡Yo no sé!
Golpes como del odio de Dios; como si ante ellos,
la resaca de todo lo sufrido
se empozara en el alma... ¡Yo no sé!

Son pocos; pero son... Abren zanjas oscuras
en el rostro más fiero y en el lomo más fuerte.
Serán tal vez los potros de bárbaros Atilas;
o los heraldos negros que nos manda la Muerte.

Son las caídas hondas de los Cristos del alma
de alguna fe adorable que el Destino blasfema.
Esos golpes sangrientos son las crepitaciones
de algún pan que en la puerta del horno se nos quema.

Y el hombre... Pobre... ¡pobre! Vuelve los ojos, como
cuando por sobre el hombro nos llama una palmada;
vuelve los ojos locos, y todo lo vivido
se empoza, como charco de culpa, en la mirada.

Hay golpes en la vida, tan fuertes... ¡Yo no sé!
```

### 1) Realizar las siguientes sustituciones: j x i, h x i, ñ x n, k x l, u x v, w x v, y x z

```python
def sustituir(archivo):
  reemplazosCarateres = [
    ('j','i'), # j x i
    ('h','i'), # h x i
    ('ñ','n'), # ñ x n
    ('k','l'), # k x l
    ('u','v'), # u x v
    ('w','v'), # w x v
    ('y','z') # y x z
  ]
  for a1, a2 in reemplazosCarateres:
    archivo = archivo.replace(a1, a2).replace(a1.upper(), a2)
  return archivo
```

### 2) Elimine las tildes

```python
def quitar_tildes(archivo):
  reemplazosVocales = [
    ('á','a'),
    ('é','e'),
    ('í','i'),
    ('ó','o'),
    ('ú','u')
  ]
  for a1, a2 in reemplazosVocales:
    archivo = archivo.replace(a1, a2)
  return archivo
```

### 3) Convierta todas las letras a mayúsculas

```python
def a_mayusculas(archivo):
  return archivo.upper()
```

### 4) Elimine los espacios en blanco y los signos de puntuación y guarde el resultado en el archivo “HERALDOSNEGROS_pre.txt”

```python
def eliminar_espacios_signos(archivo):
  signosPuntuacion = [',',';',':','¿','?','!','¡','.']
  for item in signosPuntuacion:
    archivo = archivo.replace(item,'')
  archivo = archivo.replace(' ','').replace('\n','')
  return archivo
```

### 5) Abra el archivo generado e implementar una función que calcule una tabla de frecuencias para cada letra de la ’A’ a ’Z’.

```python
def frecuencias(archivo):
  frecuencias = {}
  letras = list(string.ascii_uppercase)
  for l in letras:
    frecuencias[l] = archivo.count(l)
  return frecuencias

def frecuencias_mayores(frecuencias):
  # ordenamos las frecuencias de acuerdo al value
  frecuencias_ordenadas = sorted(frecuencias.items(), key=operator.itemgetter(1))
  mayores_tuplas = frecuencias_ordenadas[len(frecuencias) - 5:len(frecuencias)][::-1]
  mayores_dic = {k: v for k, v in mayores_tuplas}
  return mayores_dic

with open('HERALDOSNEGROS_pre.txt', 'r', encoding='utf-8-sig') as input:
    archivo2 = input.read()

    # 5) Tabla de frecuencias para cada letra de la ’A’ a ’Z’. 
    frecuencias_result = frecuencias(archivo2)
    # mostrando el diccionario de frecuencias
    print("\n DICCIONARIO DE FRECUENCIAS")
    print("\n",frecuencias_result)
    # mostrando la tabla de frecuencias
    print("\nTABLA DE FRECUENCIAS")
    mostrar_frecuencias(frecuencias_result)
    print()

    # Obteniendo los cinco caracteres de mayor frecuencia 
    mayores_dic = frecuencias_mayores(frecuencias_result)
    # mostrando el diccionario de las 5 mayores frecuencias
    print("\n DICCIONARIO DE LAS 5 MAYORES FRECUENCIAS")
    print("\n",mayores_dic)
    # mostrando la tabla de las 5 mayores frecuencias
    print("\nTABLA DE LOS 5 CARÁCTERES CON MAYOR FRECUENCIA")
    mostrar_frecuencias(mayores_dic)
    print()
```

### 6) Aplicar el método Kasiski

```python
def contar_ocurrencias(string, substring): 
    count = 0
    start = 0
    listpos = []
    while start < len(string): 
        pos = string.find(substring, start) 
        if pos != -1: 
          start = pos + 1
          count += 1
          listpos.append(pos)
        else: 
          break
    return count, listpos
    
def kasiski(archivo):
  n = 3
  trigramas = {}

  for i in range(len(archivo)-(n-1)):
    trigrama = archivo[i:i+n]
    ocurrencias, list_posiciones = contar_ocurrencias(archivo,trigrama)
    features = {}
    if ocurrencias > 1:
      if trigrama not in trigramas:
        posiciones = [(list_posiciones[i],list_posiciones[i+1]) for i in range(ocurrencias-1)]
        distancias = [ b - a for a,b in posiciones]
        features['Ocurrencias'] = ocurrencias
        features['Posiciones'] = posiciones
        features['Distancias'] = distancias
        trigramas[trigrama] = features
  return trigramas
```

### 7) Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8

```python
def unicode_8(archivo):
  code_point = ["41","42","43","44","45",
  "46","47","48","49","4A","4B","4C","4D",
  "4E","4F","50","51","52","53","54","55",
  "56","57","58","59","5A"]
  letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  for i in range(len(letras)):
    archivo = archivo.replace(letras[i], code_point[i])
  
  return archivo
  
# 7) Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8
print("\n###################################################### SEGUNDO PREPROCESAMIENTO ######################################################")
archivo =  preprocesamiento(file)
archivo = unicode_8(archivo)
print("\nTEXTO PREPROCESADO SEGÚN UNICODE-8\n\n",archivo)
with open('HERALDOSNEGROS_unicode_8.txt', 'w') as output:
  output.write(archivo)
```

### 8) Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8230

```python
def unicode_8230(archivo):
  for i in archivo:
    archivo = archivo.replace(i,"\u8230")
  return archivo
 
# 8) Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8230
print("\n###################################################### TERCER PREPROCESAMIENTO ######################################################")
archivo =  preprocesamiento(file)
archivo = unicode_8230(archivo)
print("\nTEXTO PREPROCESADO SEGÚN UNICODE-8230\n\n",archivo)
with open('HERALDOSNEGROS_unicode_8230.txt', 'w') as output:
  output.write(archivo)
```

### 9) Volver a preprocesar el archivo insertando la cadena AQUÍ cada 20 caracteres,el texto resultante deberá contener un número de caracteres que sea múltiplo de 4, si es necesario rellenar al final con caracteres X según se necesite

```python
def insertarCad(cadena,archivo):
  c = 0
  pos = -1
  for i in range(19,len(archivo),20):
    if i+(c*3) < len(archivo):
      archivo = archivo[:i+(c*3)] + cadena + archivo[i+(c*3):]
      pos = i+(c*3)
      c+=1

  if pos != -1:
    if len(archivo) > pos + 23:
      archivo = archivo[:pos+23] + cadena + archivo[pos+23:]
      pos+=23
      while len(archivo[pos:]) > 20 and pos + 23 < len(archivo):
        archivo = archivo[:pos+23] + cadena + archivo[pos+23:]
        pos+=23

  if len(archivo) % 4 != 0:
    n = len(archivo) % 4
    for _ in range(n):
      archivo = archivo + "X"
  
  return archivo
  
# 9) Insertar AQUÍ cada 20 caracteres
cadena = "AQUÍ"
print("\n###################################################### CUARTO PREPROCESAMIENTO ######################################################")
archivo = preprocesamiento(file)
archivo = insertarCad(cadena,archivo)
print("\nTEXTO PREPROCESADO INSERTANDO 'AQUI'\n\n",archivo)
with open('HERALDOSNEGROS_insertando_aqui.txt', 'w') as output:
  output.write(archivo)
```

