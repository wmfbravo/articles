# -*- coding:utf-8 -*-
import os
import sys
import re
import codecs

perfixPathLen = 0
IsSkip = False

def isnote(str):
    global IsSkip

    if IsSkip:
        if str.find('*/') != -1:
            IsSkip = False
            nonotestr = str[str.find('*/') + 2:]
        elif str.find('-->') != -1:
            IsSkip = False
            nonotestr = str[str.find('-->') + 4:]
        else:
            nonotestr = ''
    else:
        if  str.find('//') != -1:
            nonotestr = str[0:str.find('//')]
        elif str.find('/*') != -1:
            if str.find('*/') != -1:
                nonotestr = str[0:str.find('/*')] + str[str.find('*/') + 2:]
            else:
                nonotestr = str[0:str.find('/*')]
                IsSkip = True
        elif str.find('<!--') != -1 :
            if str.find('-->') != -1:
                nonotestr = str[0:str.find('<!--')] + str[str.find('-->') + 3:]
            else:
                nonotestr = str[0:str.find('<!--')]
                IsSkip = True
        else:
            nonotestr = str

    return nonotestr.strip()

def getStatment(line)

    line = EachLineNoNote.decode('utf-8', 'ignore')
    zhPattern = re.compile(ur'[^\u4e00-\u9fa5]')
    zhStr = " ".join(zhPattern.split(line)).strip()
    print zhStr
    zhStr = ",".join(zhStr.split())
    if isinstance(zhStr, unicode):
        zhStrlist = zhStr.split(',')


def splitChinese(fin):
    global IsSkip
    zhList = []
    lineNum = 0
    notelist = []
    IsSkip = False
    for eachLine in fin:
        lineNum += 1
        EachLineNoNote = isnote(eachLine.strip())
        if len(EachLineNoNote) == 0:
            continue

        zhStrlist = getStatment(EachLineNoNote)
        for chineseStr in zhStrlist:
            zhList.append(str(lineNum) + "," + chineseStr)

    return zhList

def getFileList(filePath, ignoredPathList):
    simplepath = os.path.split(filePath)[1]
    if simplepath not in ignoredPathList:
        returnstr = ""
        returndirstr = ""
        returnfilestr = ""
        filelist = os.listdir(filePath)
        for num in range(len(filelist)):
            filename = filelist[num]
            fileFullName = filePath + "/" + filename
            if os.path.isdir(fileFullName):
                returndirstr += getFileList(fileFullName, ignoredPathList)
            else:
                if filename == 'extractChinese.py':
                    continue

                fin = open(fileFullName, 'r')
                if filename.split('.').pop() == 'html':
                    chiList = splitChineseFromHtml(fin)
                else:
                    chiList = splitChinese(fin)
                fin.close()

                for chi in chiList:
                    returnfilestr += filePath[perfixPathLen:] + "/" + filename + "," + chi + "\n"

        returnstr += returnfilestr + returndirstr
        return returnstr
    else:
        return ""

#defaultRoot = 'D:\\git\\vDirector\\ztes\\api\\src\\main\\webapp\\'
defaultRoot = './'
defaultIgnore = 'libs,i18n,images,i18n,css,routes'

inputPath = raw_input("Please enter file path to be scanned(default:" + defaultRoot + "): ")
inputPassDirs = raw_input("Please enter ignored path (default:"+ defaultIgnore +"): ")
print 'Now begin to scan files...'
if inputPath == '':
  inputPath = defaultRoot
if inputPassDirs == '':
  inputPassDirs = defaultIgnore

ignoredPath = inputPassDirs.split(',')
usefulPath = inputPath.replace('\\', '/')
perfixPathLen = len(usefulPath)
if usefulPath.endswith("/"):
    usefulPath = usefulPath[:-1]
if not os.path.exists(usefulPath):
    print "Wrong path!"
elif not os.path.isdir(usefulPath):
    print "Not dir!"
else:
    filelist = os.listdir(usefulPath)
    with open('ScannedResult.csv', 'w') as f:
        f.write(codecs.BOM_UTF8)
        f.writelines(getFileList(usefulPath, ignoredPath).encode('utf-8'))
    f.close()
    print "Scanning finished, please check scannedResult.csv"