filePath = ''
fileName = ''

dataOld = ""
dataNew = ''

with open(filePath + fileName, 'r') as file:
    dataOld = file.read()

dataNew = dataOld.replace("'", '"')

with open(filePath + 'FIX_' + fileName, 'w') as file:
    file.write(dataNew)
