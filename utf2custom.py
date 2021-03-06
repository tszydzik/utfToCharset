# Hello World program in Python

# Strings
f = open("./utfStrings.csv",'r', encoding='utf8') # change to utf

# output file
outputF = open("./encoded.txt",'w', encoding='ascii')

# Code list
codeFile = open("./codeTable.txt",'r')
codeList = []

for code in codeFile:
    codeList.append(code.rstrip())

# Var names
varNamesFile = open("./varNames.txt",'r')
varNamesList = []


for varName in varNamesFile:
    curLine = varName.rstrip() + " = {"
    textLine = f.readline().rstrip();
    letterCnt = 0
    for letter in textLine:
        if letterCnt != 0: curLine+= ", "
        curLine += codeList[ord(letter)]
        letterCnt+=1
    curLine += "};\n"
    print(curLine)
    varNamesList.append(curLine)
    outputF.write(str(curLine))

# for each variable, read one line from file
for item in f:
    curLine = item.rstrip()
    for letter in curLine:
        print(codeList[ord(letter)])



outputF.close()
codeFile.close()
f.close()

# with open("./codeTable.txt",'r') as codeTable:
#     codes = [next(codeTable) for x in xrange(255)]
# print(codes)

