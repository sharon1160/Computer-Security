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
#### Resultado

```
iaz golpes en la vida, tan fvertes... ¡zo no sé!
Golpes como del odio de Dios; como si ante ellos,
la resaca de todo lo svfrido
se empozara en el alma... ¡zo no sé!

Son pocos; pero son... Abren zanias oscvras
en el rostro más fiero z en el lomo más fverte.
Serán tal vez los potros de bárbaros Atilas;
o los ieraldos negros qve nos manda la Mverte.

Son las caídas iondas de los Cristos del alma
de algvna fe adorable qve el Destino blasfema.
Esos golpes sangrientos son las crepitaciones
de algún pan qve en la pverta del iorno se nos qvema.

z el iombre... Pobre... ¡pobre! Vvelve los oios, como
cvando por sobre el iombro nos llama vna palmada;
vvelve los oios locos, z todo lo vivido
se empoza, como ciarco de cvlpa, en la mirada.

iaz golpes en la vida, tan fvertes... ¡zo no sé!
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

#### Resultado

```
iaz golpes en la vida, tan fvertes... ¡zo no se!
Golpes como del odio de Dios; como si ante ellos,
la resaca de todo lo svfrido
se empozara en el alma... ¡zo no se!

Son pocos; pero son... Abren zanias oscvras
en el rostro mas fiero z en el lomo mas fverte.
Seran tal vez los potros de barbaros Atilas;
o los ieraldos negros qve nos manda la Mverte.

Son las caidas iondas de los Cristos del alma
de algvna fe adorable qve el Destino blasfema.
Esos golpes sangrientos son las crepitaciones
de algun pan qve en la pverta del iorno se nos qvema.

z el iombre... Pobre... ¡pobre! Vvelve los oios, como
cvando por sobre el iombro nos llama vna palmada;
vvelve los oios locos, z todo lo vivido
se empoza, como ciarco de cvlpa, en la mirada.

iaz golpes en la vida, tan fvertes... ¡zo no se!
```

### 3) Convierta todas las letras a mayúsculas

```python
def a_mayusculas(archivo):
  return archivo.upper()
```
#### Resultado

```
IAZ GOLPES EN LA VIDA, TAN FVERTES... ¡ZO NO SE!
GOLPES COMO DEL ODIO DE DIOS; COMO SI ANTE ELLOS,
LA RESACA DE TODO LO SVFRIDO
SE EMPOZARA EN EL ALMA... ¡ZO NO SE!

SON POCOS; PERO SON... ABREN ZANIAS OSCVRAS
EN EL ROSTRO MAS FIERO Z EN EL LOMO MAS FVERTE.
SERAN TAL VEZ LOS POTROS DE BARBAROS ATILAS;
O LOS IERALDOS NEGROS QVE NOS MANDA LA MVERTE.

SON LAS CAIDAS IONDAS DE LOS CRISTOS DEL ALMA
DE ALGVNA FE ADORABLE QVE EL DESTINO BLASFEMA.
ESOS GOLPES SANGRIENTOS SON LAS CREPITACIONES
DE ALGUN PAN QVE EN LA PVERTA DEL IORNO SE NOS QVEMA.

Z EL IOMBRE... POBRE... ¡POBRE! VVELVE LOS OIOS, COMO
CVANDO POR SOBRE EL IOMBRO NOS LLAMA VNA PALMADA;
VVELVE LOS OIOS LOCOS, Z TODO LO VIVIDO
SE EMPOZA, COMO CIARCO DE CVLPA, EN LA MIRADA.

IAZ GOLPES EN LA VIDA, TAN FVERTES... ¡ZO NO SE!
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

#### Resultado

```
IAZGOLPESENLAVIDATANFVERTESZONOSEGOLPESCOMODELODIODEDIOSCOMOSIANTEELLOSLARESACADETODOLOSVFRIDOSEEMPOZARAENELALMAZONOSESONPOCOSPEROSONABRENZANIASOSCVRASENELROSTROMASFIEROZENELLOMOMASFVERTESERANTALVEZLOSPOTROSDEBARBAROSATILASOLOSIERALDOSNEGROSQVENOSMANDALAMVERTESONLASCAIDASIONDASDELOSCRISTOSDELALMADEALGVNAFEADORABLEQVEELDESTINOBLASFEMAESOSGOLPESSANGRIENTOSSONLASCREPITACIONESDEALGUNPANQVEENLAPVERTADELIORNOSENOSQVEMAZELIOMBREPOBREPOBREVVELVELOSOIOSCOMOCVANDOPORSOBREELIOMBRONOSLLAMAVNAPALMADAVVELVELOSOIOSLOCOSZTODOLOVIVIDOSEEMPOZACOMOCIARCODECVLPAENLAMIRADAIAZGOLPESENLAVIDATANFVERTESZONOSE
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
#### Resultado

```
DICCIONARIO DE FRECUENCIAS

 {'A': 65, 'B': 10, 'C': 16, 'D': 27, 'E': 74, 'F': 7, 'G': 8, 'H': 0, 'I': 28, 'J': 0, 'K': 0, 'L': 47, 'M': 20, 'N': 36, 'O': 83, 'P': 17, 'Q': 4, 'R': 33, 'S': 59, 'T': 18, 'U': 1, 'V': 26, 'W': 0, 'X': 0, 'Y': 0, 'Z': 12}

TABLA DE FRECUENCIAS
+---------------------------------------+
| Letra              Frecuencia         |
|---------------------------------------|
| A                  65                 |
| B                  10                 |
| C                  16                 |
| D                  27                 |
| E                  74                 |
| F                  7                  |
| G                  8                  |
| H                  0                  |
| I                  28                 |
| J                  0                  |
| K                  0                  |
| L                  47                 |
| M                  20                 |
| N                  36                 |
| O                  83                 |
| P                  17                 |
| Q                  4                  |
| R                  33                 |
| S                  59                 |
| T                  18                 |
| U                  1                  |
| V                  26                 |
| W                  0                  |
| X                  0                  |
| Y                  0                  |
| Z                  12                 |
+---------------------------------------+  


 DICCIONARIO DE LAS 5 MAYORES FRECUENCIAS

 {'O': 83, 'E': 74, 'A': 65, 'S': 59, 'L': 47}

TABLA DE LOS 5 CARÁCTERES CON MAYOR FRECUENCIA
+---------------------------------------+
| Letra              Frecuencia         |
|---------------------------------------|
| O                  83                 |
| E                  74                 |
| A                  65                 |
| S                  59                 |
| L                  47                 |
+---------------------------------------+  
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
#### Resultado

```
                                                 KASISKI
+------------------------------------------------------------------------------------------------------+
| Trigrama    Ocurrencias                                             Posiciones             Distancias|
|------------------------------------------------------------------------------------------------------|
| IAZ             2                                                      (0,558)                   558 |
| AZG             2                                                      (1,559)                   558 |
| ZGO             2                                                      (2,560)                   558 |
| GOL             4                                    (3,33) (33,339) (339,561)            30,306,222 |
| OLP             4                                    (4,34) (34,340) (340,562)            30,306,222 |
| LPE             4                                    (5,35) (35,341) (341,563)            30,306,222 |
| PES             4                                    (6,36) (36,342) (342,564)            30,306,222 |
| ESE             3                                            (7,186) (186,565)               179,379 |
| SEN             4                                  (8,150) (150,406) (406,566)           142,256,160 |
| ENL             4                                  (9,388) (388,548) (548,567)            379,160,19 |
| NLA             6             (10,262) (262,358) (358,389) (389,549) (549,568)      252,96,31,160,19 |
| LAV             2                                                     (11,569)                   558 |
| AVI             2                                                     (12,570)                   558 |
| VID             3                                           (13,519) (519,571)                506,52 |
| IDA             3                                           (14,268) (268,572)               254,304 |
| DAT             2                                                     (15,573)                   558 |
| ATA             2                                                     (16,574)                   558 |
| TAN             2                                                     (17,575)                   558 |
| ANF             2                                                     (18,576)                   558 |
| NFV             2                                                     (19,577)                   558 |
| FVE             3                                           (20,181) (181,578)               161,397 |
| VER             5                       (21,182) (182,255) (255,393) (393,579)        161,73,138,186 |
| ERT             5                       (22,183) (183,256) (256,394) (394,580)        161,73,138,186 |
| RTE             4                                 (23,184) (184,257) (257,581)            161,73,324 |
| TES             4                                 (24,185) (185,258) (258,582)            161,73,324 |
| ESZ             2                                                     (25,583)                   558 |
| SZO             2                                                     (26,584)                   558 |
| ZON             3                                           (27,112) (112,585)                85,473 |
| ONO             4                                 (28,113) (113,473) (473,586)            85,360,113 |
| NOS             7                     (29,114) (114,244) (244,404) (408,474)...      85,130,160,4... |
| OSE             6               (30,93) (93,115) (115,405) (405,522) (522,588)      63,22,290,117,66 |
| SCO             3                                             (38,55) (55,447)                17,392 |
| COM             4                                   (39,56) (56,448) (448,531)             17,392,83 |
| OMO             5                         (40,57) (57,175) (175,449) (449,532)         17,118,274,83 |
| ODE             3                                             (42,49) (49,540)                 7,491 |
| DEL             4                                 (43,278) (278,290) (290,398)            235,12,108 |
| ELO             4                                 (44,279) (279,440) (440,497)            235,161,57 |
| DIO             2                                                      (47,52)                     5 |
| IOS             3                                           (53,445) (445,502)                392,57 |
| OSC             4                                 (54,144) (144,281) (281,446)            90,137,165 |
| OSI             2                                                     (59,225)                   166 |
| ANT             2                                                     (62,190)                   128 |
| EEL             3                                           (65,317) (317,465)               252,148 |
| ELL             2                                                     (66,172)                   106 |
| LLO             2                                                     (67,173)                   106 |
| LOS             7                       (68,85) (85,198) (198,224) (280,441)...      17,113,26,56... |
| OSL             3                                           (69,475) (475,503)                406,28 |
| ADE             3                                           (78,296) (296,397)               218,101 |
| TOD             2                                                     (81,511)                   430 |
| ODO             2                                                     (82,512)                   430 |
| DOL             2                                                     (83,513)                   430 |
| OLO             3                                           (84,223) (223,514)               139,291 |
| IDO             2                                                     (91,520)                   429 |
| DOS             3                                           (92,232) (232,521)               140,289 |
| SEE             2                                                     (94,523)                   429 |
| EEM             2                                                     (95,524)                   429 |
| EMP             2                                                     (96,525)                   429 |
| MPO             2                                                     (97,526)                   429 |
| POZ             2                                                     (98,527)                   429 |
| OZA             2                                                     (99,528)                   429 |
| AEN             2                                                    (103,547)                   444 |
| ENE             3                                          (104,151) (151,170)                 47,19 |
| NEL             3                                          (105,152) (152,171)                 47,19 |
| ELA             2                                                    (106,291)                   185 |
| LAL             2                                                    (107,292)                   185 |
| ALM             3                                          (108,293) (293,486)               185,193 |
| LMA             3                                          (109,294) (294,487)               185,193 |
| MAZ             2                                                    (110,414)                   304 |
| ESO             3                                          (117,259) (259,335)                142,76 |
| SON             4                                (118,130) (130,260) (260,356)             12,130,96 |
| OCO             2                                                    (122,506)                   384 |
| COS             2                                                    (123,507)                   384 |
| OSP             2                                                    (124,199)                    75 |
| ERO             2                                                    (127,166)                    39 |
| ROS             5                      (128,155) (155,204) (204,214) (214,238)           27,49,10,24 |
| OSO             3                                          (129,442) (442,499)                313,57 |
| BRE             5                      (134,422) (422,427) (427,432) (432,463)            288,5,5,31 |
| ASO             2                                                    (142,221)                    79 |
| SOS             2                                                    (143,336)                   193 |
| TRO             2                                                    (158,203)                    45 |
| OMA             2                                                    (160,177)                    17 |
| MAS             2                                                    (161,178)                    17 |
| ASF             3                                          (162,179) (179,329)                17,150 |
| IER             2                                                    (165,227)                    62 |
| ERA             2                                                    (188,228)                    40 |
| LVE             3                                          (194,438) (438,495)                244,57 |
| OSD             2                                                    (205,288)                    83 |
| SDE             4                                (206,277) (277,289) (289,374)              71,12,85 |
| BAR             2                                                    (209,212)                     3 |
| LAS             4                                (220,263) (263,328) (328,359)              43,65,31 |
| OSQ             2                                                    (239,409)                   170 |
| SQV             2                                                    (240,410)                   170 |
| QVE             4                                (241,315) (315,385) (385,411)              74,70,26 |
| ENO             2                                                    (243,407)                   164 |
| AND             2                                                    (248,454)                   206 |
| NDA             2                                                    (249,274)                    25 |
| LAM             3                                          (252,478) (478,550)                226,72 |
| ONL             2                                                    (261,357)                    96 |
| ASC             2                                                    (264,360)                    96 |
| DAS             2                                                    (269,275)                     6 |
| ION             2                                                    (272,370)                    98 |
| SCR             2                                                    (282,361)                    79 |
| TOS             2                                                    (287,353)                    66 |
| MAD             2                                                    (295,488)                   193 |
| DEA             2                                                    (297,375)                    78 |
| EAL             2                                                    (298,376)                    78 |
| ALG             2                                                    (299,377)                    78 |
| VNA             2                                                    (302,482)                   180 |
| VEE             2                                                    (316,386)                    70 |
| EMA             2                                                    (332,413)                    81 |
| REP             3                                          (363,423) (423,428)                  60,5 |
| ELI             3                                          (399,417) (417,466)                 18,49 |
| LIO             3                                          (400,418) (418,467)                 18,49 |
| IOM             2                                                    (419,468)                    49 |
| OMB             2                                                    (420,469)                    49 |
| MBR             2                                                    (421,470)                    49 |
| EPO             2                                                    (424,429)                     5 |
| POB             2                                                    (425,430)                     5 |
| OBR             3                                          (426,431) (431,462)                  5,31 |
| VVE             2                                                    (435,492)                    57 |
| VEL             4                                (436,439) (439,493) (493,496)                3,54,3 |
| ELV             2                                                    (437,494)                    57 |
| SOI             2                                                    (443,500)                    57 |
| OIO             2                                                    (444,501)                    57 |
| MOC             2                                                    (450,533)                    83 |
| ADA             2                                                    (489,555)                    66 |
+------------------------------------------------------------------------------------------------------+  
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
```
#### Resultado

```
484159474F4C504553454E4C415649444154414E46554552544553594F4E4F53E474F4C504553434F4D4F44454C4F44494F444544494F53434F4D4F5349414E5445454C4C4F534C415245534143414445544F444F4C4F5355465249444F5345454D504F5A415241454E454C414C4D41594F4E4F53E534F4E504F434F535045524F534F4E414252454E5A414E4A41534F534355524153454E454C524F5354524F4DA53464945524F59454E454C4C4F4D4F4DA53465545525445534552A4E54414C56455A4C4F53504F54524F53444542A524241524F534154494C41534F4C4F53484552414C444F534E4547524F535155454E4F534D414E44414C414D5545525445534F4E4C41534341I444153484F4E44415344454C4F5343524953544F5344454C414C4D414445414C47554E41464541444F5241424C45515545454C44455354494E4F424C415346454D4145534F53474F4C50455353414E475249454E544F53534F4E4C41534352455049544143494F4E45534445414C47U4E50414E515545454E4C4150554552544144454C484F524E4F53454E4F535155454D4159454C484F4D425245504F425245504F4252455655454C56454C4F534F4A4F53434F4D4F4355414E444F504F52534F425245454C484F4D42524F4E4F534C4C414D41554E4150414C4D4144415655454C56454C4F534F4A4F534C4F434F5359544F444F4C4F56495649444F5345454D504F5A41434F4D4F43484152434F444543554C5041454E4C414D4952414441484159474F4C504553454E4C415649444154414E46554552544553594F4E4F53E
```

### 8) Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8230

```python
def unicode_8230(archivo):
  for i in archivo:
    archivo = archivo.replace(i,"\u8230")
  return archivo
```
#### Resultado

```
舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰舰
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
```
#### Resultado

```
IAZGOLPESENLAVIDATAAQUÍNFVERTESZONOSEGOLPEAQUÍSCOMODELODIODEDIOSCAQUÍOMOSIANTEELLOSLARESAQUÍACADETODOLOSVFRIDOSAQUÍEEMPOZARAENELALMAZOAQUÍNOSESONPOCOSPEROSONAQUÍABRENZANIASOSCVRASEAQUÍNELROSTROMASFIEROZEAQUÍNELLOMOMASFVERTESERAQUÍANTALVEZLOSPOTROSDEAQUÍBARBAROSATILASOLOSIAQUÍERALDOSNEGROSQVENOSAQUÍMANDALAMVERTESONLASAQUÍCAIDASIONDASDELOSCRAQUÍISTOSDELALMADEALGVNAQUÍAFEADORABLEQVEELDESAQUÍTINOBLASFEMAESOSGOLAQUÍPESSANGRIENTOSSONLAAQUÍSCREPITACIONESDEALGAQUÍUNPANQVEENLAPVERTADAQUÍELIORNOSENOSQVEMAZEAQUÍLIOMBREPOBREPOBREVVAQUÍELVELOSOIOSCOMOCVANAQUÍDOPORSOBREELIOMBRONAQUÍOSLLAMAVNAPALMADAVVAQUÍELVELOSOIOSLOCOSZTOAQUÍDOLOVIVIDOSEEMPOZACAQUÍOMOCIARCODECVLPAENLAQUÍAMIRADAIAZGOLPESENLAQUÍAVIDATANFVERTESZONOAQUÍSEXXX
```
