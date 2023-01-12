# TODO - clarify this description
# 
# This code reads in two documents and creates a third file to combine them.
#
# This version separates sections of the menu into 5 distinct arrays.
#
# CoreArrays.py
#
# Updated 11.3.22




# Open the Template file
with open('indexOutline.html') as templateFile:
    templateCode = templateFile.readlines()

#This can likely be deleted
import json
            
from os.path import exists

resultFileName = "Result01112023.html"

fileExists = exists(resultFileName)
    
    
import os

if fileExists == True:
    # Remove the old result file
    os.remove(resultFileName)
    
    
# Create the new Result HTML file   
resultFile = open(resultFileName, "a") 

# Define Arrays (2D?) for Template
template1A = []
template1B = []
template1AAStart = []
template1AAEnd = []
template2A = []
template2B = []
template2C = []
template2D = []
template2E = []
template2F = []
template2G = []
template2H = [] #price
template2I = [] #price-end
template2J = []
template2K = []
template3 =  []

templateBStart = []
templateB1Start = []
templateB1aStart = []
templateB1aEnd = []
templateB1bStart = []
templateB1bEnd = []
templateB1cStart = []
templateB1cEnd = []
templateB1dStart = []
templateB1dEnd = []
templateBEnd = []

templateCStart = []
templateC1Start = []
templateC1aStart = []
templateC1aEnd = []
templateC1bStart = []
templateC1bEnd = []
templateC1cStart = []
templateC1cEnd = []
templateC1dStart = []
templateC1dEnd = []
templateCEnd = []

templateDStart = []
templateD1Start = []
templateD3Start = []
templateD3End = []
templateD3Endb = []
templateD3aStart = []
templateD3aEnd = []
templateD1bStart = []
templateD1bEnd = []
templateD1cStart = []
templateD1cEnd = []
templateD1dStart = []
templateD1dEnd = []
templateD1eStart = []
templateD1eEnd = []
templateDEnd = []





templateIEnd = []

singleProduct = []

#Define the key word to look for within the Template file.
keyWord = 'BY THE GLASS HEADER\n'




keyWord1A =      '<!--__________ HTML HEADER START __________-->\n'

keyWord1B =      '<!--__________ HTML HEADER END __________-->\n'


keyWord2_1A =    '<!--__________ BY THE GLASS SECTION HEADER START __________-->\n'

keyWord2_1B =    '<!--__________ BY THE GLASS SECTION HEADER END __________-->\n'


keyWord2_1Aa =    '<!--__________ BY THE GLASS CATEGORY HEADER START __________-->\n'

keyWord2_1Bb =    '<!--__________ BY THE GLASS CATEGORY HEADER END __________-->\n'


keyWord2_2A =    '<!--__________ BY THE GLASS TITLE HEADER START __________-->\n'

keyWord2_2B =    '<!--__________ BY THE GLASS TITLE HEADER END __________-->\n'


keyWord2_3A =    '<!--__________ BY THE GLASS TITLE FOOTER START __________-->\n'

keyWord2_3B =    '<!--__________ BY THE GLASS TITLE FOOTER END __________-->\n'

                
keyWord2_4A =    '<!--__________ BY THE GLASS ITEM HEADER START __________-->\n'
     
keyWord2_4B =    '<!--__________ BY THE GLASS ITEM HEADER END __________-->\n'                           


keyWord2_5A =    '<!--__________ BY THE GLASS NAME HEADER START __________-->\n'

keyWord2_5B =    '<!--__________ BY THE GLASS NAME HEADER END __________-->\n'


keyWord2_6A =    '<!--__________ BY THE GLASS NAME FOOTER START __________-->\n'                     

keyWord2_6B =    '<!--__________ BY THE GLASS NAME FOOTER END __________-->\n'
                    
    
keyWord2_7A =    '<!--__________ BY THE GLASS GRAPE HEADER START __________-->\n'

keyWord2_7B =    '<!--__________ BY THE GLASS GRAPE HEADER END __________-->\n'


keyWord2_8A =    '<!--__________ BY THE GLASS GRAPE FOOTER START __________-->\n'

keyWord2_8B =    '<!--__________ BY THE GLASS GRAPE FOOTER END __________-->\n'
            
    
keyWord2_9A =    '<!--__________ BY THE GLASS PRICE HEADER START __________-->\n'

keyWord2_9B =    '<!--__________ BY THE GLASS PRICE HEADER END __________-->\n'               


keyWord2_10A =    '<!--__________ BY THE GLASS PRICE FOOTER START __________-->\n'

keyWord2_10B =    '<!--__________ BY THE GLASS PRICE FOOTER END __________-->\n'               


keyWord2_11A =    '<!--__________ BY THE GLASS ORIGIN HEADER START __________-->\n'                

keyWord2_11B =    '<!--__________ BY THE GLASS ORIGIN HEADER END __________-->\n'          


keyWord2_12A =    '<!--__________ BY THE GLASS ORIGIN FOOTER START __________-->\n'          
                                     
keyWord2_12B =    '<!--__________ BY THE GLASS ORIGIN FOOTER END __________-->\n'


keyWord2_13A =    '<!--__________ BY THE GLASS CATEGORY FOOTER START __________-->\n'

keyWord2_13B =    '<!--__________ BY THE GLASS CATEGORY FOOTER END __________-->\n'


keyWord3_A =    '<!--__________ BY THE GLASS SECTION FOOTER START __________-->\n'

keyWord3_B =    '<!--__________ BY THE GLASS SECTION FOOTER END __________-->\n'


keyWord4_1A =    '<!--__________ BEER SECTION HEADER START __________-->\n'

keyWord4_1B =    '<!--__________ BEER SECTION HEADER END __________-->\n'    


keyWord4_2A =    '<!--__________ BEER ITEM HEADER START __________-->\n'

keyWord4_2B =    '<!--__________ BEER ITEM HEADER END __________-->\n'


keyWord4_3A =    '<!--__________ BEER TITLE HEADER START __________-->\n' 

keyWord4_3B =    '<!--__________ BEER TITLE HEADER END __________-->\n'                                    


keyWord4_4A =    '<!--__________ BEER TITLE FOOTER START __________-->\n'                

keyWord4_4B =    '<!--__________ BEER TITLE FOOTER END __________-->\n'                


keyWord4_5A =    '<!--__________ BEER ORIGIN HEADER START __________-->\n'                

keyWord4_5B =    '<!--__________ BEER ORIGIN HEADER END __________-->\n'                


keyWord4_6A =    '<!--__________ BEER ORIGIN FOOTER START __________-->\n'  

keyWord4_6B =    '<!--__________ BEER ORIGIN FOOTER END __________-->\n'                


keyWord4_7A =    '<!--__________ BEER PRICE HEADER START __________-->\n'                

keyWord4_7B =    '<!--__________ BEER PRICE HEADER END __________-->\n'                


keyWord4_8A =    '<!--__________ BEER PRICE FOOTER START __________-->\n'  

keyWord4_8B =    '<!--__________ BEER PRICE FOOTER END __________-->\n'                


keyWord4_9A =    '<!--__________ BEER DESCRIPTION HEADER START __________-->\n'                

keyWord4_9B =    '<!--__________ BEER DESCRIPTION HEADER END __________-->\n'                


keyWord4_10A =    '<!--__________ BEER DESCRIPTION FOOTER START __________-->\n'  

keyWord4_10B =    '<!--__________ BEER DESCRIPTION FOOTER END __________-->\n'                


keyWord4_11A =    '<!--__________ BEER SECTION FOOTER START __________-->\n'  

keyWord4_11B =    '<!--__________ BEER SECTION FOOTER END __________-->\n' 






keyWord6_1A =    '<!--__________ FOOD SECTION HEADER START __________-->\n'

keyWord6_1B =    '<!--__________ FOOD SECTION HEADER END __________-->\n'    


keyWord6_2A =    '<!--__________ FOOD TITLE HEADER START __________-->\n' 

keyWord6_2B =    '<!--__________ FOOD TITLE HEADER END __________-->\n'                                    


keyWord6_3A =    '<!--__________ FOOD TITLE FOOTER START __________-->\n'                

keyWord6_3B =    '<!--__________ FOOD TITLE FOOTER END __________-->\n'                

keyWord6_4A =    '<!--__________ FOOD NAME HEADER START __________-->\n' 

keyWord6_4B =    '<!--__________ FOOD NAME HEADER END __________-->\n'                                    


keyWord6_5A =    '<!--__________ FOOD NAME FOOTER START __________-->\n'                

keyWord6_5B =    '<!--__________ FOOD NAME FOOTER END __________-->\n'                


keyWord6_6A =    '<!--__________ FOOD PRICE HEADER START __________-->\n'                

keyWord6_6B =    '<!--__________ FOOD PRICE HEADER END __________-->\n'                


keyWord6_7A =    '<!--__________ FOOD PRICE FOOTER START __________-->\n'  

keyWord6_7B =    '<!--__________ FOOD PRICE FOOTER END __________-->\n'                


keyWord6_8A =    '<!--__________ FOOD DESCRIPTION HEADER START __________-->\n'                

keyWord6_8B =    '<!--__________ FOOD DESCRIPTION HEADER END __________-->\n'                


keyWord6_9A =    '<!--__________ FOOD DESCRIPTION FOOTER START __________-->\n'  

keyWord6_9B =    '<!--__________ FOOD DESCRIPTION FOOTER END __________-->\n'                


keyWord6_12A =    '<!--__________ FOOD SECTION FOOTER START __________-->\n'  

keyWord6_12B =    '<!--__________ FOOD SECTION FOOTER END __________-->\n' 






keyWord8_1A =    '<!--__________ BOTTLE SECTION HEADER START __________-->\n'

keyWord8_1B =    '<!--__________ BOTTLE SECTION HEADER END __________-->\n'    


keyWord8_1x5xA =    '<!--__________ BOTTLE CATEGORY HEADER START __________-->\n'

keyWord8_1x5xB =    '<!--__________ BOTTLE CATEGORY HEADER END __________-->\n'    


keyWord8_2A =    '<!--__________ BOTTLE TITLE HEADER START __________-->\n' 

keyWord8_2B =    '<!--__________ BOTTLE TITLE HEADER END __________-->\n'                                    


keyWord8_3A =    '<!--__________ BOTTLE TITLE FOOTER START __________-->\n'                

keyWord8_3B =    '<!--__________ BOTTLE TITLE FOOTER END __________-->\n'

keyWord8_3Ba =  '<!--__________ LARGE BOTTLE NOTICE START __________-->'

keyWord8_3Bb =  '<!--__________ LARGE BOTTLE NOTICE END __________-->'

keyWord8_4A =    '<!--__________ BOTTLE NAME HEADER START __________-->\n' 

keyWord8_4B =    '<!--__________ BOTTLE NAME HEADER END __________-->\n'                                    


keyWord8_5A =    '<!--__________ BOTTLE NAME FOOTER START __________-->\n'                

keyWord8_5B =    '<!--__________ BOTTLE NAME FOOTER END __________-->\n'                


keyWord8_6A =    '<!--__________ BOTTLE PRICE HEADER START __________-->\n'                

keyWord8_6B =    '<!--__________ BOTTLE PRICE HEADER END __________-->\n'                


keyWord8_7A =    '<!--__________ BOTTLE PRICE FOOTER START __________-->\n'  

keyWord8_7B =    '<!--__________ BOTTLE PRICE FOOTER END __________-->\n'                


keyWord8_8A =    '<!--__________ BOTTLE ORIGIN HEADER START __________-->\n'                

keyWord8_8B =    '<!--__________ BOTTLE ORIGIN HEADER END __________-->\n'                


keyWord8_9A =    '<!--__________ BOTTLE ORIGIN FOOTER START __________-->\n'  

keyWord8_9B =    '<!--__________ BOTTLE ORIGIN FOOTER END __________-->\n'                


keyWord8_10A =    '<!--__________ BOTTLE GRAPE HEADER START __________-->\n'                

keyWord8_10B =    '<!--__________ BOTTLE GRAPE HEADER END __________-->\n'                


keyWord8_11A =    '<!--__________ BOTTLE GRAPE FOOTER START __________-->\n'  

keyWord8_11B =    '<!--__________ BOTTLE GRAPE FOOTER END __________-->\n'                


keyWord8_12A =    '<!--__________ BOTTLE DESCRIPTION HEADER START __________-->\n'                

keyWord8_12B =    '<!--__________ BOTTLE DESCRIPTION HEADER END __________-->\n'                


keyWord8_13A =    '<!--__________ BOTTLE DESCRIPTION FOOTER START __________-->\n'  

keyWord8_13B =    '<!--__________ BOTTLE DESCRIPTION FOOTER END __________-->\n'                


keyWord8_13x5xA =    '<!--__________ BOTTLE CATEGORY FOOTER START __________-->\n'

keyWord8_13x5xB =    '<!--__________ BOTTLE CATEGORY FOOTER END __________-->\n'    


keyWord8_14A =    '<!--__________ BOTTLE SECTION FOOTER START __________-->\n'  

keyWord8_14B =    '<!--__________ BOTTLE SECTION FOOTER END __________-->\n'


keyWord_ZA =   '<!--__________ HTML FOOTER START __________-->\n'

keyWord_ZB =   '<!--__________ HTML FOOTER END __________-->\n'



#--------------------------------------------------------------------------------------
# This function takes in an array and prints it as lines.
#--------------------------------------------------------------------------------------

def writeLines (arrayOfLines):
    
    totalLines = len(arrayOfLines)

    p = 0
    
    # While there are at least two lines left
    while p < totalLines:
        
        resultFile.write(arrayOfLines[p])
        
        p += 1

    resultFile.write('\n')
    
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function takes in a string and checks for multiple blanks.
#
# Returns an array of two strings if there are blanks.
#
# Returns -1 if not.
#
# Other white space and end of line characters are also removed.
#--------------------------------------------------------------------------------------

def splitBlank(checkForBlanks):
    
    splitLine = ['blank']
    k = 0
    componentLength = len(checkForBlanks)


    #split the string where there are more than three spaces
    while k < componentLength: 
        
            
        if checkForBlanks[k] == " ":
    
            if checkForBlanks[k+1] == " " and checkForBlanks[k+2] == " ":
    
                beforeBlanks = checkForBlanks[:k]
                
                afterBlanks = checkForBlanks[k+1:]
                afterBlanks = afterBlanks.lstrip()
                afterBlanks = afterBlanks.strip("\n")
                    
                splitLine = [beforeBlanks, afterBlanks]
            
                k = componentLength
                
        k += 1
    
    if splitLine != ['blank']:
        return splitLine
                    
    else:
        return -1


#ALT

#--------------------------------------------------------------------------------------
# This function takes in a string and checks for multiple blanks.
#
# Returns an array of two strings if there are blanks.
#
# Returns -1 if not.
#
# Other white space and end of line characters are also removed.
#--------------------------------------------------------------------------------------

def alternateSplitBlank(checkForBlanks):
    
    splitLine = ['blank']
    k = 0
    componentLength = len(checkForBlanks)


    #split the string where there are more than two spaces
    while componentLength > k:
        
        
        if checkForBlanks[componentLength-1] == " ":
    
            if checkForBlanks[componentLength-1] == " ":
    
                beforeBlanks = checkForBlanks[:componentLength-2]
                
                afterBlanks = checkForBlanks[componentLength-1:]
                afterBlanks = afterBlanks.lstrip()
                afterBlanks = afterBlanks.strip("\n")
                    
                splitLine = [beforeBlanks, afterBlanks]
            
                componentLenth = k
                
        componentLength -= 1
    
    if splitLine != ['blank']:
        return splitLine
                    
    else:
        return -1



#--------------------------------------------------------------------------------------
# This function adjusts for lines not having a carriage return in the original document.
#--------------------------------------------------------------------------------------

def parseForNoCarriageReturn(longContent):
    
    

    
    individualWords = longContent.split()


    number = 'blank'

    n = 0
    yWords = ['initalA', 'initialB']

    for j in individualWords:
        p = j.isdigit()

        if p == True:
            
            priceCheck = longContent.find(j)
            if longContent[priceCheck-1] == " ":
                
                #Rename these variables, "number", "j"
                number = j
               
                before = individualWords[:n+1]
                after = individualWords[n+1:]
        
                n += 1
        
        
        #txt = "De La Soif, 'L'inattendu' - Chardonnay, Assyrtiko, Picpoul, Malvasia                        17                California, USA"

    
    
    xWord = longContent.replace(number, number + "||")

    
 

    if xWord.find('||') != -1:
        yWords = xWord.split("||")

    if yWords[1] != "initialB":
        return yWords[0], yWords[1]
    else:
        return False

#infoA = " ".join(before)



# CURRENTLY WORKING

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function takes in a string and checks for the word "chilled".
#
# Returns an array of two strings - one being the price, the other being "chilled".
#
# Returns -1 if "chilled" is not present.
#
# White space and end of line characters are also removed.
#--------------------------------------------------------------------------------------


def splitPrice(checkForDescription):
    
    x = checkForDescription.rfind("Chilled")
                
    if x != -1:
        extractedPrice = checkForChilled.strip('Chilled')

        extractedPrice = extractedPrice.strip("\n")
        
        extractedPrice = extractedPrice.lstrip()
        
        splitLine = ["Chilled", extractedPrice]
    
        return splitLine
    
    else:
        return -1

#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
# This function takes in a string and checks for the word "chilled".
#
# Returns an array of two strings - one being the price, the other being "chilled".
#
# Returns -1 if "chilled" is not present.
#
# White space and end of line characters are also removed.
#--------------------------------------------------------------------------------------


def splitChilled(checkForChilled):
    
    x = checkForChilled.rfind("Chilled")
                
    if x != -1:
        extractedPrice = checkForChilled.strip('Chilled')

        extractedPrice = extractedPrice.strip("\n")
        
        extractedPrice = extractedPrice.lstrip()
        
        splitLine = ["Chilled", extractedPrice]
    
        return splitLine
                    
    else:
        return -1

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function takes in a string and checks for a hyphen.
#
# Returns an array of two strings if there is a hyphen.
#
# Returns -1 if not.
#
# White space and end of line characters are also removed.
#--------------------------------------------------------------------------------------



def splitHyphen(checkForHyphen):
    
    x = checkForHyphen.rfind("- ")
                
    if x != -1:
        splitLine = checkForHyphen.split('- ')
    
        beforeHyphen = splitLine[0]
                
        afterHyphen = splitLine[1]
        afterHyphen = afterHyphen.lstrip()
        afterHyphen = afterHyphen.strip("\n")
                    
        splitLine = [beforeHyphen, afterHyphen]
    
        return splitLine
                    
    else:
        return -1

#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
# This function writes a by the glass non-wine item.
#
# Included are all associated attributes - description, origin, price, etc.
#--------------------------------------------------------------------------------------



def writeSingleNonWineByTheGlassInfo(singleLine):

    nonWineName = 'blank'
    nonWineOrigin = 'blank'
    nonWineDescription = 'blank'
    price = 'blank'
    
    writeLines(templateB1Start)
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(singleLine)
    
        
    if split != -1:
        nonWineInfo = split[0]
        
        price = split[1]
    
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(nonWineInfo)
        
        #This variable 'price' should be renamed to something like priceInfo since it is not yet definitely the price
        
        price = price.lstrip()
        
        
    
        #rename this function to splitPrice?
        descriptionCheck = splitBlank(price)
    
    
        if descriptionCheck != -1:
            
       
            nonWineDescription = descriptionCheck[0]
     
            price = descriptionCheck[1]
            
    
        if split != -1:
            nonWineName = split[0]
            nonWineOrigin = split[1]
            
        # If there is no additional information other than price, that is the name to print    
        else:
            nonWineName = nonWineInfo
        
            


    if nonWineName != 'blank':                
        
        
        writeLines(templateB1aStart)
        resultFile.write(nonWineName)
        
        writeLines(templateB1aEnd)
                
    #edit tags
    if nonWineOrigin != 'blank':        
        
        writeLines(templateB1bStart)
        resultFile.write(nonWineOrigin)
  
        writeLines(templateB1bEnd)
    
    if price != 'blank':


        writeLines(templateB1cStart)
        resultFile.write(price)

        resultFile.write('\n')
        writeLines(templateB1cEnd)
    
    #edit tags
    if nonWineDescription != 'blank':
        writeLines(templateB1dStart)
        resultFile.write(nonWineDescription)
        resultFile.write('\n')
        writeLines(templateB1dEnd)
    
     


#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function writes a by the glass wine item.
#
# Included are all associated attributes - description, origin, price, etc.
#--------------------------------------------------------------------------------------



def writeSingleWineByTheGlassInfo(firstLine, secondLine):

    wineName = 'blank'
    wineGrapes = 'blank'
    wineDescription = 'blank'
    wineOrigin = 'blank'
    chilled = 'blank'
    price = 'blank'
    
    writeLines(template2C)
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(firstLine)
    
    if split != -1:
        wineInfo = split[0]
        price = split[1]
    
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(wineInfo)
    
        #perhaps this needs a better variable name?
        c = splitChilled(price)
    
        if c != -1:
            chilled = c[0]
            price = c[1]
            
    
        if split != -1:
            wineName = split[0]
            wineGrapes = split[1]
        
        # Assing the following line the by the glass origin
        if secondLine != 'blank':
            wineOrigin = secondLine
        

                
    if wineName != 'blank':                

        writeLines(template2D)
        resultFile.write(wineName)
        writeLines(template2E)
        resultFile.write('\n')
                
    
    if wineGrapes != 'blank':        
       
        writeLines(template2F)
        resultFile.write(wineGrapes)
        writeLines(template2G)

        resultFile.write('\n')    
            
    if wineDescription != 'blank':
        

        resultFile.write(wineDescription)
        resultFile.write('\n')

    
    
    
    if chilled != 'blank':
  
        resultFile.write(chilled)

        resultFile.write('\n')
    
    if price != 'blank':

        
        writeLines(template2H)
        resultFile.write(price)
        writeLines(template2I)
        resultFile.write('\n') 
        
    if wineOrigin != 'blank':

        writeLines(template2J)
        resultFile.write(wineOrigin)
        writeLines(template2K)

        resultFile.write('\n')
        
    
        
        

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function writes a single bottle item.
#
# Included are all associated attributes - description, origin, price, etc.
#--------------------------------------------------------------------------------------



def writeSingleBottleInfo(firstLine, secondLine):

    bottleInfo = 'blank'
    bottleGrapes = 'blank'
    bottleDescription = 'blank'
    bottleOrigin = 'blank'
    price = 'blank'
    additionalInfo = 'blank'
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(firstLine)
    
    if split != -1:

        bottleInfo = split[0]
        priceInfo = split[1]
      
        
        priceInfo = priceInfo.lstrip()
   
        split = splitBlank(priceInfo)
        
        if split != -1:
            bottleOrigin = split[0]
            price = split[1]
            
            #Check for the rare instance of extra info about the wine ie. "(500ml)"
            secondSplit = splitBlank(price)
            
            if secondSplit != -1:
            
                #What seemed to be bottleOrigin is actually additional info (rework this logic / variable names)
                additionalInfo = bottleOrigin
                bottleOrigin = secondSplit[0]
                price = secondSplit[1]
                
        else:
            price = priceInfo
                    
        # Assing the following line the by the glass origin
        if secondLine != 'blank':
            bottleGrapeAndDescription = secondLine
        
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(bottleGrapeAndDescription)

        if split != -1:
            bottleGrapes = split[0]
            bottleDescription = split[1]
            
    

    if bottleInfo != 'blank':                
        
        writeLines(templateD3aStart)
        resultFile.write(bottleInfo)
        
        if additionalInfo != 'blank':
            resultFile.write(" ")
            resultFile.write(additionalInfo)
                            

        resultFile.write('\n')
        writeLines(templateD3aEnd)

        
    if price != 'blank':

        writeLines(templateD3bStart)

        resultFile.write(price)

        writeLines(templateD3bEnd)
        resultFile.write('\n') 
        
    if bottleOrigin != 'blank':

        writeLines(templateD3cStart)
        resultFile.write(bottleOrigin)
        resultFile.write('\n')
        writeLines(templateD3cEnd)

    

    if bottleGrapes != 'blank':        

        writeLines(templateD3dStart)
        resultFile.write(bottleGrapes)

        resultFile.write('\n')    
        writeLines(templateD3dEnd)

    if bottleDescription != 'blank':

        writeLines(templateD3eStart)
        resultFile.write(bottleDescription)
        resultFile.write('\n')
        writeLines(templateD3eEnd)

        
    

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function writes a by the glass wine item.
#
# Included are all associated attributes - description, origin, price, etc.
#--------------------------------------------------------------------------------------



def writeFoodInfo(firstLine, secondLine):

    foodName = 'blank'
    foodDescription = 'blank'
    price = 'blank'
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(firstLine)
    
    
    if split != -1:
        foodName = split[0]
        price = split[1]
    
        # Assing the following line the by the glass origin
        if secondLine != 'blank':
            foodDescription = secondLine
                

                
    if foodName != 'blank':    
        # Note this should possibly renamed in either the template or a food section should be added
        writeLines(templateC1bStart)
        resultFile.write(foodName)
        resultFile.write('\n')
        writeLines(templateC1bEnd)

    if price != 'blank':

        writeLines(templateC1cStart)
        resultFile.write(price)
        
        resultFile.write('\n') 
        writeLines(templateC1cEnd)
    
        
    if foodDescription != 'blank':
        
        writeLines(templateC1dStart)
        resultFile.write(foodDescription)
        resultFile.write('\n')
        writeLines(templateC1dEnd)

        

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function takes in an array and writes it as content for wine by the glass.
#
# This is part A.1
#--------------------------------------------------------------------------------------

def writeWineByTheGlass(wine):


    writeLines(template1B)
    #writeLines(template2A)
    
    # While not at the end

    wineLine = len(wine)

    i = 0
    
    # While there are at least two lines left
    while (i+1) < wineLine:
        
        writeLines(template1AAStart)

        #resultFile.write('631')
        
        # Because end of line has already been removed, check for a blank.
        # Advance index if the line is blank
        while wine[i] == '':
            i += 1

        # If the line is all uppercase, assign header
        upperCase = wine[i].isupper()
    
        
    
        if upperCase == True:
            
            
            writeLines(template2A)
            
            resultFile.write(wine[i])
            
            writeLines(template2B)
            # Write a header
            header = wine[i]
        
          
            
        
        # Else
        else:
     
    
            
            # Write a wine
            writeSingleWineByTheGlassInfo(wine[i], wine[i+1])
            
            # Advance to the next line to account for two lines of information
            i += 1
        
        
        
        i += 1
        
        
        writeLines(template1AAEnd)


#--------------------------------------------------------------------------------------
# This function takes in an array and writes it as content for non-wine by the glass.
#
# This is part A.2
#--------------------------------------------------------------------------------------

def writeNonWineByTheGlass(nonWine):
    
    # While not at the end

    nonWineLine = len(nonWine)

    i = 0

    # While there are at least two lines left
    while (i+1) < nonWineLine:

        # Advance index if the line is blank
        while nonWine[i] == '\n':
            i += 1

        # If the line is all uppercase, assign header
        upperCase = nonWine[i].isupper()
    

       
        if upperCase == True:
            
            
            
            # Write a header
            header = nonWine[i]          
        
        # Else
        else:
     
        
            # Write a wine
            writeSingleNonWineByTheGlassInfo(nonWine[i])
                    
        i += 1

        

#--------------------------------------------------------------------------------------
# This function takes in an array and writes it as content for food.
#
# This is part B
#--------------------------------------------------------------------------------------

def writeFood(food):
    
    
    # While not at the end

    foodLine = len(food)

    i = 0

    # While there are at least two lines left
    while (i+1) < foodLine:

        # Because end of line has already been removed, check for a blank.
        # Advance index if the line is blank
        while food[i] == '':
            i += 1

        # If the line is all uppercase, assign header
        upperCase = food[i].isupper()
    
       
        if upperCase == True:
            
            
            # Write a header
            header = food[i]
        
            # Write the header with correspondin HTML tags
    
        
            writeLines(templateC1aStart)
            resultFile.write(header)
            writeLines(templateC1aEnd)
        
            resultFile.write('\n')
        
        # Else
        else:
     
            # Write a wine
            writeFoodInfo(food[i], food[i+1])
            
            # Advance to the next line to account for two lines of information
            i += 1
        
        i += 1

        

#--------------------------------------------------------------------------------------
# This function takes in an array and writes it as content for bottles.
#
# This is part C
#--------------------------------------------------------------------------------------

def writeBottles(bottle):
    
    
    templateD2StartWithCurrentCategory = []

    # While not at the end

    bottleLength = len(bottle)

    i = 0

    # While there are at least two lines left
    
    secondLoop = 0
    
    while (i+1) < bottleLength:

        
        
        # Because end of line has already been removed, check for a blank.
        # Advance index if the line is blank
        
        while bottle[i] == '':
            
            i += 1

        # If the line is all uppercase, assign header
        upperCase = bottle[i].isupper()
        #if upperCase == True:
    
       
        if upperCase == True:
            
            # Write a header
            bottleHeader = bottle[i]
        
            bottleHeaderToFormat = bottleHeader.title()

            firstFormat = bottleHeaderToFormat.replace("&", "")
            secondFormat = firstFormat.replace(",", "")
            thirdFormat = secondFormat.replace(" ", "")
            variableFormat = thirdFormat
            
            
            # Close out the previous section if there was one
            if secondLoop != 0:
                writeLines(templateD2End)
        
            secondLoop = 1
            # Write the header with correspondin HTML tags
    
            
        
            
            # Replace id with the corresponding category header
            bottleCategoryLength = len(templateD2Start)
            
            bottleCategoryIndex = 0
            while bottleCategoryIndex < bottleCategoryLength:
                ##replace bottleCategory with bottleheader
                
                categoryFound = templateD2Start[bottleCategoryIndex].find("Category")
                
                if categoryFound != -1:
                    
                    
                    replacement = templateD2Start[bottleCategoryIndex].replace("Category", variableFormat)

                    templateD2StartWithCurrentCategory.append(replacement)
                    
                    
                else:
                    
                    
                    
                    templateD2StartWithCurrentCategory.append(templateD2Start[bottleCategoryIndex])

                bottleCategoryIndex += 1

            

            
            
            
            
            writeLines(templateD2StartWithCurrentCategory)
            templateD2StartWithCurrentCategory = []
            writeLines(templateD3Start)
            if bottleHeader == 'LARGE FORMAT':
                
                resultFile.write(bottleHeader)
                resultFile.write('</u></b></b><i><u> (all wines are 1.5 Liter unless otherwise notated)</i></u>')
                #This is to account for the alternate code not being used
                resultFile.write('<u><b>')
            
                writeLines(templateD3End)
            else:
                resultFile.write(bottleHeader)
                
                #resultFile.write(BottleHeaderHTMLEnd)
                #resultFile.write('\n')
                writeLines(templateD3End)
        
        # Else (if not uppercase)
        else:
            # Write a wine by the bottle
        
            writeSingleBottleInfo(bottle[i], bottle[i+1])
            
            # Advance to the next line to account for two lines of information
            
            
            i += 1
        
        
        i += 1


#--------------------------------------------------------------------------------------
# This function assigns parts of a template to an array
#
# WORK IN PROGRESS
#--------------------------------------------------------------------------------------


def getTemplate(keyWordStart, keyWordEnd, templateSection, index):

    templateArray = []
    
    # Advance to the next section
    while index < templateLength and keyWordStart != templateSection[index]:
    
        index += 1
    
    index += 1
    

    while index < templateLength and keyWordEnd != templateSection[index]:
    
    
        templateArray.append(templateSection[index])
        index += 1

    index += 1
    
    return templateArray
#--------------------------------------------------------------------------------------
        
        
#---------------------------------------------------------------------------------------------------------
#
# Template Part 1
#
#---------------------------------------------------------------------------------------------------------

#Print all the elements of the Template array until the first keyword is reached.
#Add those elements to the Results array.

#Write to the Result file all the elements of the Template array until the keyword is reached.

templateLength = len(templateCode)
i = 0


#j = 0
   
    
template1A = getTemplate(keyWord1A, keyWord1B, templateCode, i)

template1B = getTemplate(keyWord2_1A, keyWord2_1B, templateCode, i)

template1AAStart = getTemplate(keyWord2_1Aa, keyWord2_1Bb, templateCode, i)

template2A = getTemplate(keyWord2_2A, keyWord2_2B, templateCode, i)

template2B = getTemplate(keyWord2_3A, keyWord2_3B, templateCode, i)

template2C = getTemplate(keyWord2_4A, keyWord2_4B, templateCode, i)

template2D = getTemplate(keyWord2_5A, keyWord2_5B, templateCode, i)

template2E = getTemplate(keyWord2_6A, keyWord2_6B, templateCode, i)

template2F = getTemplate(keyWord2_7A, keyWord2_7B, templateCode, i)

template2G = getTemplate(keyWord2_8A, keyWord2_8B, templateCode, i)

template2H = getTemplate(keyWord2_9A, keyWord2_9B, templateCode, i)

template2I = getTemplate(keyWord2_10A, keyWord2_10B, templateCode, i)

template2J = getTemplate(keyWord2_11A, keyWord2_11B, templateCode, i)

template2K = getTemplate(keyWord2_12A, keyWord2_12B, templateCode, i)

template1AAEnd = getTemplate(keyWord2_13A, keyWord2_13B, templateCode, i)

template3 = getTemplate(keyWord3_A, keyWord3_B, templateCode, i)

templateBStart = getTemplate(keyWord4_1A, keyWord4_1B, templateCode, i)

templateB1Start = getTemplate(keyWord4_2A, keyWord4_2B, templateCode, i)

templateB1aStart = getTemplate(keyWord4_3A, keyWord4_3B, templateCode, i)

templateB1aEnd = getTemplate(keyWord4_4A, keyWord4_4B, templateCode, i)

templateB1bStart = getTemplate(keyWord4_5A, keyWord4_5B, templateCode, i)

templateB1bEnd = getTemplate(keyWord4_6A, keyWord4_6B, templateCode, i)

templateB1cStart = getTemplate(keyWord4_7A, keyWord4_7B, templateCode, i)

templateB1cEnd = getTemplate(keyWord4_8A, keyWord4_8B, templateCode, i)

templateB1dStart = getTemplate(keyWord4_9A, keyWord4_9B, templateCode, i)

templateB1dEnd = getTemplate(keyWord4_10A, keyWord4_10B, templateCode, i)

templateBEnd = getTemplate(keyWord4_11A, keyWord4_11B, templateCode, i)




templateCStart = getTemplate(keyWord6_1A, keyWord6_1B, templateCode, i)
templateC1aStart = getTemplate(keyWord6_2A, keyWord6_2B, templateCode, i)
templateC1aEnd = getTemplate(keyWord6_3A, keyWord6_3B, templateCode, i)
templateC1bStart = getTemplate(keyWord6_4A, keyWord6_4B, templateCode, i)
templateC1bEnd = getTemplate(keyWord6_5A, keyWord6_5B, templateCode, i)
templateC1cStart = getTemplate(keyWord6_6A, keyWord6_6B, templateCode, i)
templateC1cEnd = getTemplate(keyWord6_7A, keyWord6_7B, templateCode, i)
templateC1dStart = getTemplate(keyWord6_8A, keyWord6_8B, templateCode, i)
templateC1dEnd = getTemplate(keyWord6_9A, keyWord6_9B, templateCode, i)
templateCEnd = getTemplate(keyWord6_12A, keyWord6_12B, templateCode, i)
 


templateDStart = getTemplate(keyWord8_1A, keyWord8_1B, templateCode, i)
templateD2Start = getTemplate(keyWord8_1x5xA, keyWord8_1x5xB, templateCode, i)


templateD3Start = getTemplate(keyWord8_2A, keyWord8_2B, templateCode, i)
templateD3End = getTemplate(keyWord8_3A, keyWord8_3B, templateCode, i)


templateD3Endb = getTemplate(keyWord8_3Ba, keyWord8_3Bb, templateCode, i)

templateD3aStart = getTemplate(keyWord8_4A, keyWord8_4B, templateCode, i)
templateD3aEnd = getTemplate(keyWord8_5A, keyWord8_5B, templateCode, i)
templateD3bStart = getTemplate(keyWord8_6A, keyWord8_6B, templateCode, i)
templateD3bEnd = getTemplate(keyWord8_7A, keyWord8_7B, templateCode, i)
templateD3cStart = getTemplate(keyWord8_8A, keyWord8_8B, templateCode, i)
templateD3cEnd = getTemplate(keyWord8_9A, keyWord8_9B, templateCode, i)
templateD3dStart = getTemplate(keyWord8_10A, keyWord8_10B, templateCode, i)
templateD3dEnd = getTemplate(keyWord8_11A, keyWord8_11B, templateCode, i)
templateD3eStart = getTemplate(keyWord8_12A, keyWord8_12B, templateCode, i)
templateD3eEnd = getTemplate(keyWord8_13A, keyWord8_13B, templateCode, i)
templateD2End = getTemplate(keyWord8_13x5xA, keyWord8_13x5xB, templateCode, i)



templateDEnd = getTemplate(keyWord8_14A, keyWord8_14B, templateCode, i)


templateIEnd = getTemplate(keyWord_ZA, keyWord_ZB, templateCode, i)









#---------------------------------------------------------------------------------------------------------
# End Template Part 1
#---------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------
#
# Content Part 1
#
#---------------------------------------------------------------------------------------------------------

#Add Content elements to the results array.    
with open('WINE LIST January 11 2023.txt') as contentFile:
    #rename menuContent to something like contentLine
    menuContent = contentFile.readlines()  




foodKeyWord = 'FOOD'
bottleKeyWord = 'SPARKLING WHITE'
# this variable does not include the end of line character, bacause it has already been removed.
nonWineKeyWord = 'BEER, CIDER, VERMOUTH & NON-ALCOHOLIC'


# Initiallize array to hold everything.
noSpacesMenuContent = []

# Initiallize array to hold everything without blank lines.
noBlankLinesMenuContent = []

# Initiallize array to hold everything by the glass.
byTheGlassContent = []

# Initiallize array to hold everything food.
foodContent = []

# Initiallize array to hold everything bottles.
bottleContent = []

# Initialize array to hold by the glass wine.
byTheGlassWineContent = []

# Initialize array to hold by the glass non-wine.
byTheGlassNonWineContent = []



# ---------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------

LineLengthTippingPoint = 110

# Remove all extra spaces
totalMenuContentLength = len(menuContent)

totalMenuIndex = 0
while totalMenuIndex < totalMenuContentLength:
    
    #Remove beginning and end spaces second
    
    #Check for lack of carriage return between lines
    if len(menuContent[totalMenuIndex]) > LineLengthTippingPoint:

            currentResult = parseForNoCarriageReturn(menuContent[totalMenuIndex])
            
            if currentResult != False:

                contentWithoutSpaces = currentResult[0].strip()
                noSpacesMenuContent.append(contentWithoutSpaces)
                contentWithoutSpaces = currentResult[1].strip()
                noSpacesMenuContent.append(contentWithoutSpaces)
    
            else:
                contentWithoutSpaces = menuContent[totalMenuIndex].strip()
                noSpacesMenuContent.append(contentWithoutSpaces)
    else:   
        #Check for a special case for LARGE FORMAT notice
        largeFormatLine = menuContent[totalMenuIndex].find("LARGE FORMAT")
        if largeFormatLine != -1:
            menuContent[totalMenuIndex] = "LARGE FORMAT"
            
        contentWithoutSpaces = menuContent[totalMenuIndex].strip()
        noSpacesMenuContent.append(contentWithoutSpaces)
    
    totalMenuIndex += 1

    
noBlankLinesMenuContent = list(filter(None, noSpacesMenuContent))


# Determine where FOOD starts in the document.
menuIndex = noBlankLinesMenuContent.index(foodKeyWord)

    
# Populate the array for by the glass.
byTheGlassIndex = 0
while byTheGlassIndex < menuIndex:

    byTheGlassContent.append(noBlankLinesMenuContent[byTheGlassIndex])
    byTheGlassIndex += 1
    

# ---------------------------------------------------------------------
# Part A.1
# ---------------------------------------------------------------------


# Determine where non-wine starts in the by the glass section.
subMenuIndex = byTheGlassContent.index(nonWineKeyWord)

# Populate the array for only wine by the glass.
wineByTheGlassIndex = 0
while wineByTheGlassIndex < subMenuIndex:

	byTheGlassWineContent.append(byTheGlassContent[wineByTheGlassIndex])
	wineByTheGlassIndex += 1
    

writeLines(template1A)


# This should be write section header
writeWineByTheGlass(byTheGlassWineContent)


#writeWineByTheGlass(byTheGlassWineContent)

#writeLines(template2E)
writeLines(template3)

# ---------------------------------------------------------------------
# Part A.2
# ---------------------------------------------------------------------

# Determine where the end of the by the glass section is.
subMenuIndex = len(byTheGlassContent)

# Populate the array for non-wine by the glass.

# Start the non wine by the glass index where wine by the glass index left off.
nonWineByTheGlassIndex = wineByTheGlassIndex
while nonWineByTheGlassIndex < subMenuIndex:

	byTheGlassNonWineContent.append(byTheGlassContent[nonWineByTheGlassIndex])
	nonWineByTheGlassIndex += 1

writeLines(templateBStart)    
writeNonWineByTheGlass(byTheGlassNonWineContent)
writeLines(templateBEnd)

# ---------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------    


# Determine where bottles start ['SPARKLING WHITE'] in the document.
menuIndex = noBlankLinesMenuContent.index(bottleKeyWord)

# Populate the array for by the glass.

# Start the foodIndex where byTheGlassIndex left off.
foodIndex = byTheGlassIndex
while foodIndex < menuIndex:


    contentWithoutEndOfLine = noBlankLinesMenuContent[foodIndex].strip("\n")
    foodContent.append(contentWithoutEndOfLine)
    foodIndex += 1
    
writeLines(templateCStart) 
writeFood(foodContent)
writeLines(templateCEnd)


# ---------------------------------------------------------------------
# Part C
# ---------------------------------------------------------------------    

# Determine where the end of the file is.
menuIndex = len(noBlankLinesMenuContent)

# Populate the array for bottles.

# Start the bottleIndex where foodIndex left off.
bottleIndex = foodIndex
while bottleIndex < menuIndex:


    contentWithoutEndOfLine = noBlankLinesMenuContent[bottleIndex].strip("\n")
    bottleContent.append(contentWithoutEndOfLine)
    bottleIndex += 1


    
writeLines(templateDStart)
writeBottles(bottleContent)
writeLines(templateDEnd)
writeLines(templateIEnd)


#---------------------------------------------------------------------------------------------------------
# End Content Part 1
#---------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------
#
# Template Part 2
#
#---------------------------------------------------------------------------------------------------------

#Don't include the Key Word
i = i+1


#Amend those elements to the Results array.
while i < templateLength: # and keyWord !=templateCode[i]:
    #matched_indexes.append(i)

    #resultFile.write(templateCode[i])
    #resultFile.write('\n')
    i += 1 

#---------------------------------------------------------------------------------------------------------
# End Template Part 2
#---------------------------------------------------------------------------------------------------------



#Close the Result File
resultFile.close()
    
    
