
################# PRINT #################

def printHeader(matrixHeader):
  for k in matrixHeader:
    print(k,matrixHeader[k])

def printMatrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j]," ",end='')
    print()

################# PRE-PROCESSING #################

def removeAccents(text):
  vowelReplacements = [
    ('á','a'),
    ('é','e'),
    ('í','i'),
    ('ó','o'),
    ('ú','u')
  ]
  for a1, a2 in vowelReplacements:
    text = text.replace(a1, a2)
  return text

def removeSpacesSigns(text):
  punctuationMarks = [',',';',':','¿','?','!','¡','.']
  for item in punctuationMarks:
    text = text.replace(item,'')
  text = text.replace(' ','').replace('\n','')
  return text

def preprocess(text):
  text = removeSpacesSigns(text)
  text = removeAccents(text)
  text = text.replace('ñ','n')
  text = text.upper()
  return text

################# HEAD MATRIX #################

def sortKey (clave):
  clave = ''.join(sorted(clave))
  orderedKey = list(clave)
  return orderedKey

def generateHeader(key, orderedKey):
  matrixHeader = {}
  for i in range(len(orderedKey)):
    pos = orderedKey.index(key[i])
    matrixHeader[pos + 1] = key[i]
    orderedKey[pos] = "-"
  return matrixHeader

################# TRANSPOSITION INTERRUPTED #################

def getEncryptedText(matrixHeader, matrix):
  result = ""
  for col in range(len(matrixHeader)):
    colMatrix = list(matrixHeader).index(col+1)
    for row in matrix:
      result += row[colMatrix]
    result += " "
  return result

def interruptedTransposition(key, text):
  # HEAD
  orderedKey = sortKey(key)
  matrixHeader = generateHeader(key, orderedKey)

  # MATRIX
  matrix = []
  flag = False 

  i = 0 # Preprocessed text index 
  numrow = 0 # Variable that stores the row number

  while flag == False:

    row = [""] * len(matrixHeader) # Row
    f = 0 # Index of the created row

    for key in matrixHeader:

      # If all the preprocessed text has been read, break the two loops
      if i >= len(text):
        flag = True
        break

      # If the row number matches the column key,
      # break the loop and go to the next row
      if (numrow + 1) == key:
        row[f] += text[i]
        f += 1
        i += 1
        break
      else:
        row[f] += text[i]
        f += 1
        i += 1

    numrow += 1
    matrix.append(row)

  # printHeader(matrixHeader)
  # printMatrix(matrix)

  # GET ENCRYPTED TEXT
  result = getEncryptedText(matrixHeader, matrix)
  return result

################# MAIN #################

if __name__ == "__main__":

  # Password and plain text entry
  key  = "convenience"
  text = "Here is a secret message enciphered by transposition"

  # Key and plain text preprocessing
  key = preprocess(key)
  text = preprocess(text)

  # Text encryption
  textEncryption = interruptedTransposition(key, text)

  print(textEncryption)

