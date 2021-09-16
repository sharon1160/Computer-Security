import string
import operator

################# FUNCIONES PARA MOSTRAR LOS DATOS #################

def mostrar_trigramas(trigramas):
  print("\n\t\t\t\t\t\tKASISKI")
  Tabla = """\
+------------------------------------------------------------------------------------------------------+
| Trigrama    Ocurrencias                                             Posiciones             Distancias|
|------------------------------------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------------------------------------+\
  """
  listas = []
  for trigrama in trigramas:
    list = [trigrama, trigramas[trigrama]['Ocurrencias']]

    posCad = ""
    distCad = ""

    list_pos = trigramas[trigrama]['Posiciones']
    list_dist = trigramas[trigrama]['Distancias']

    if len(list_pos) > 6:
      c = 0
      for a,b in list_pos:
        if c < 4:
          posCad += "("+ str(a) + "," +str(b)+") "
        if c == 5:
          posCad += "("+ str(a) + "," +str(b)+")..."
          break
        c+=1
    else:
      for a,b in list_pos:
        posCad += "("+ str(a) + "," +str(b)+") "

    if len(list_dist) > 6:
      c = 0
      for i in range(len(list_dist)-1):
        if c < 4:
          distCad += str(list_dist[i]) + ","
        else:
          distCad += str(list_dist[i]) + "..."
          break
        c+=1
    else:
      for i in range(len(list_dist)-1):
        distCad += str(list_dist[i]) + ","
      distCad += str(list_dist[len(list_dist)-1])

    list.append(posCad)
    list.append(distCad)

    listas.append(list)

  Tabla = (Tabla.format('\n'.join("| {:<15} {:<2} {:>60} {:>20} |".format(*fila)for fila in listas)))
  print (Tabla)

def mostrar_frecuencias(frecuencias):
  Tabla = """\
+---------------------------------------+
| Letra              Frecuencia         |
|---------------------------------------|
{}
+---------------------------------------+\
  """
  listas = []
  for f in frecuencias:
    list = [f, frecuencias[f]]
    listas.append(list)

  Tabla = (Tabla.format('\n'.join("| {:<18} {:<18} |".format(*fila)for fila in listas)))
  print (Tabla)

################# FUNCIONES PARA EL PREPROCESAMIENTO #################

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


def a_mayusculas(archivo):
  return archivo.upper()

def eliminar_espacios_signos(archivo):
  signosPuntuacion = [',',';',':','¿','?','!','¡','.']
  for item in signosPuntuacion:
    archivo = archivo.replace(item,'')
  archivo = archivo.replace(' ','').replace('\n','')
  return archivo


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

################# METODO KASISKI #################

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

################# INSERTAR CADENA #################

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

################# PREPROCESAMIENTO #################

def preprocesamiento(file,insertar = False,cadena = ""):

  with open(file, 'r', encoding = 'utf-8-sig') as input:
    archivo = input.read()

    if insertar == True:
      archivo = insertarCad(cadena,archivo)

    # 1) Sustitucion de carácteres
    archivo = sustituir(archivo)

    # 2) Quitando tíldes 
    archivo = quitar_tildes(archivo)

    # 3) Convirtiendo todas las letras a mayúsculas 
    archivo = a_mayusculas(archivo)

    # 4) Eliminando los espacios en blanco y los signos de puntuación 
    archivo = eliminar_espacios_signos(archivo)

  with open('HERALDOSNEGROS_pre.txt', 'w') as output:
    output.write(archivo)

  with open('HERALDOSNEGROS_pre.txt', 'r', encoding='utf-8-sig') as input:
    archivo2 = input.read()

    # 5) Tabla de frecuencias para cada letra de la ’A’ a ’Z’. 
    frecuencias_result = frecuencias(archivo2)
    # mostrando el diccionario
    print("\n DICCIONARIO DE FRECUENCIAS")
    print("\n",frecuencias_result)
    print("\nTABLA DE FRECUENCIAS")
    mostrar_frecuencias(frecuencias_result)
    print()

    # Obteniendo los cinco caracteres de mayor frecuencia 
    # https://www.delftstack.com/es/howto/python/how-to-sort-a-dictionary-by-value/
    mayores_dic = frecuencias_mayores(frecuencias_result)
    print("\n DICCIONARIO DE LAS 5 MAYORES FRECUENCIAS")
    print("\n",mayores_dic)
    print("\nTABLA DE LOS 5 CARÁCTERES CON MAYOR FRECUENCIA")
    mostrar_frecuencias(mayores_dic)
    print()

    # 6) Aplicando el método Kasiski 
    trigamas = kasiski(archivo)
    mostrar_trigramas(trigamas)

def main():
  file = 'input.txt'
  preprocesamiento(file)

  # 9) Insertar AQUÍ cada 20 caracteres
  cadena = "AQUÍ"
  preprocesamiento(file,True,cadena)

  # comment

if __name__ == "__main__":
  main()
