# This code reads in two documents and creates a third file to combine them.
#
# This version separates sections of the menu into 5 distict arrays.
#
# CoreArrays.py
#
# Updated 11.3.22




# Open the Template file
with open('indexOutline.html') as templateFile:
    templateCode = templateFile.readlines()

import json
            

    
# Create the Result HTML file   
resultFile = open("Result.html", "a") 

# Define Arrays (2D?) for Template
template1A = []
template1B = []
template2A = []

#Define the key word to look for within the Template file.
keyWord = 'BY THE GLASS HEADER\n'




keyWord1A =      '<!--__________ HTML HEADER START __________-->\n'

keyWord1B =      '<!--__________ HTML HEADER END __________-->\n'


keyWord2_1A =    '<!--__________ BY THE GLASS SECTION HEADER START __________-->\n'

keyWord2_1B =    '<!--__________ BY THE GLASS SECTION HEADER END __________-->\n'


keyWord2_2A =    '<!--__________ BY THE GLASS TITLE HEADER START __________-->\n'

keyWord2_2B =    '<!--__________ BY THE GLASS TITLE HEADER END __________-->\n'


keyWord2_3A =    '<!--__________ BY THE GLASS TITLE FOOTER START __________-->\n'

keyWord2_3B =    '<!--__________ BY THE GLASS TITLE FOOTER END __________-->\n'

                
keyWord2_4A =    '<!--__________ BY THE GLASS ITEM HEADER START __________-->\n'
     
keyWord2_4B =    '<!--__________ BY THE GLASS ITEM HEADER END __________-->\n'                           


keyWord2_5A =    '<!--__________ BY THE GLASS NAME HEADER START __________-->\n'

keyWord2_5B =    '<!--__________ BY THE GLASS NAME HEADER END __________-->\n'


keyWord2_6A =    '<!--__________ BY THE GLASS NAME HEADER END __________-->\n'                     

keyWord2_6B =    '<!--__________ BY THE GLASS NAME END __________-->\n'
                    
    
keyWord2_7A =    '<!--__________ BY THE GLASS GRAPE HEADER START __________-->\n'                        

keyWord2_7B =    '<!--__________ BY THE GLASS GRAPE HEADER END __________-->\n'


keyWord2_8A =    '<!--__________ BY THE GLASS GRAPE FOOTER START __________-->\n'

keyWord2_8B =    '<!--__________ BY THE GLASS GRAPE FOOTER END __________-->\n'
            
    
keyWord2_9A =    '<!--__________ BY THE GLASS PRICE HEADER START __________-->\n'

keyWord2_9B =    '<!--__________ BY THE GLASS PRICE HEADER END __________-->\n'               


keyWord2_10A =    '<!--__________ BY THE GLASS FOOTER START __________-->\n'

keyWord2_10B =    '<!--__________ BY THE GLASS PRICE FOOTER END __________-->\n'               


keyWord2_11A =    '<!--__________ BY THE GLASS ORIGIN HEADER START __________-->\n'                

keyWord2_11B =    '<!--__________ BY THE GLASS ORIGIN HEADER END __________-->\n'          


keyWord2_12A =    '<!--__________ BY THE GLASS ORIGIN FOOTER START __________-->\n'          
                                     
keyWord2_12B =    '<!--__________ BY THE GLASS ORIGIN FOOTER END __________-->\n'      







'''

keyWord1A = '<!--__________ HTML HEADER START __________-->\n'

keyWord1B = '<!--__________ HTML HEADER END __________-->\n'

keyWord2A = '<!--__________ BY THE GLASS SECTION HEADER START __________-->\n'

keyWord2B = '<!--__________ BY THE GLASS SECTION HEADER END __________-->\n'

keyWord3A = '<!--__________ BY THE GLASS TITLE START __________-->\n'
            
keyWord3B = '<!--__________ BY THE GLASS TITLE END __________-->\n'

keyWord = 'BY THE GLASS HEADER\n'

keyWord2 = 'BY THE GLASS PRODUCT\n'

keyWord3 = 'BY THE BOTTLE HEADER\n'

keyWord4 = 'BY THE BOTTLE PRODUCT\n'

'''

#--------------------------------------------------------------------------------------
# This function takes in an array and prints it as lines.
#--------------------------------------------------------------------------------------

def writeLines (arrayOfLines):
    
    totalLines = len(arrayOfLines)

    p = 0

    print('array test start')
    
    # While there are at least two lines left
    while p < totalLines:
        
        resultFile.write(arrayOfLines[p])
        
        print(arrayOfLines[p])
        
        p += 1

    resultFile.write('\n')
    print('array test end')
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


    #split the string where there are more than two spaces
    while k < componentLength: 
        
            
        if checkForBlanks[k] == " ":
    
            if checkForBlanks[k+1] == " ":
    
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
    
    x = checkForHyphen.rfind(" - ")
                
    if x != -1:
        splitLine = checkForHyphen.split(' - ')
    
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
    
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(singleLine)
    
    
    if split != -1:
        nonWineInfo = split[0]
        price = split[1]
    
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(nonWineInfo)
    
        price = price.lstrip()
    
        #rename this function to splitPrice?
        descriptionCheck = splitBlank(price)
    
        if descriptionCheck != -1:
            nonWineDescription = descriptionCheck[0]
            price = descriptionCheck[1]
            
    
        if split != -1:
            nonWineName = split[0]
            nonWineOrigin = split[1]
            
        else:
            nonWineName = nonWineInfo
            
'''removed to test JSON writing (arrays)

    if nonWineName != 'blank':                
        resultFile.write(GlassProductHTMLStart)
        #resultFile.write('Non Wine Name:')
        resultFile.write(nonWineName)
        resultFile.write(GlassProductHTMLEnd)
        resultFile.write('\n')
                
    #edit tags
    if nonWineOrigin != 'blank':        
        resultFile.write(GlassGrapesHTMLStart)
        #resultFile.write('Grapes:')
        resultFile.write(nonWineOrigin)
        resultFile.write(GlassGrapesHTMLEnd)
        resultFile.write('\n')    
    
    
    #edit tags
    if nonWineDescription != 'blank':
        resultFile.write(GlassOriginHTMLStart)
        #resultFile.write('Wine Origin:')
        resultFile.write(nonWineDescription)
        #resultFile.write('\n')
        resultFile.write(GlassOriginHTMLEnd) 
    
    if price != 'blank':
        #resultFile.write('Price:')
        resultFile.write(GlassPriceHTMLStart)
        #resultFile.write('Non Wine Price:')
        resultFile.write(price)
        resultFile.write(GlassPriceHTMLEnd)
        resultFile.write('\n') 

'''
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
        

'''removed to test JSON writing (arrays)
                
    if wineName != 'blank':                
        resultFile.write(GlassProductHTMLStart)
        #resultFile.write('Wine Name:')
        resultFile.write(wineName)
        resultFile.write(GlassProductHTMLEnd)
        resultFile.write('\n')
                
    if wineGrapes != 'blank':        
        resultFile.write(GlassGrapesHTMLStart)
        #resultFile.write('Grapes:')
        resultFile.write(wineGrapes)
        resultFile.write(GlassGrapesHTMLEnd)
        resultFile.write('\n')    
            
    if wineDescription != 'blank':
        resultFile.write(GlassDescriptionHTMLStart)
        #resultFile.write('Wine Description:')
        resultFile.write(wineDescription)
        resultFile.write('\n')
        resultFile.write(GlassDescriptionHTMLEnd) 
    
    if wineOrigin != 'blank':
        resultFile.write(GlassOriginHTMLStart)
        #resultFile.write('Wine Origin:')
        resultFile.write(wineOrigin)
        resultFile.write(GlassOriginHTMLEnd)
        resultFile.write('\n')
    
    if chilled != 'blank':
        resultFile.write(GlassChilledHTMLStart)
        #resultFile.write('Wine Price:')
        resultFile.write(chilled)
        resultFile.write(GlassChilledHTMLEnd)
        resultFile.write('\n')
    
    if price != 'blank':
        #resultFile.write('Price:')
        resultFile.write(GlassPriceHTMLStart)
        #resultFile.write('Wine Price:')
        resultFile.write(price)
        resultFile.write(GlassPriceHTMLEnd)
        resultFile.write('\n') 
        
'''

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function writes a single bottle item.
#
# Included are all associated attributes - description, origin, price, etc.
#--------------------------------------------------------------------------------------



def writeSingleBottleInfo(firstLine, secondLine):

    bottleName = 'blank'
    bottleGrapes = 'blank'
    bottleDescription = 'blank'
    bottleOrigin = 'blank'
    price = 'blank'
    
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
            
'''removed to test JSON writing (arrays)
                
    if bottleName != 'blank':                
        resultFile.write(BottleProductHTMLStart)
        #resultFile.write('Bottle Name:')
        resultFile.write(bottleName)
        resultFile.write(BottleProductHTMLEnd)
        resultFile.write('\n')
                
    if bottleGrapes != 'blank':        
        resultFile.write(BottleGrapesHTMLStart)
        #resultFile.write('Grapes:')
        resultFile.write(bottleGrapes)
        resultFile.write(BottleGrapesHTMLEnd)
        resultFile.write('\n')    
            
    if bottleDescription != 'blank':
        resultFile.write(BottleDescriptionHTMLStart)
        #resultFile.write('Wine Description:')
        resultFile.write(bottleDescription)
        resultFile.write('\n')
        resultFile.write(BottleDescriptionHTMLEnd) 
    
    if bottleOrigin != 'blank':
        resultFile.write(BottleOriginHTMLStart)
        #resultFile.write('Wine Origin:')
        resultFile.write(bottleOrigin)
        resultFile.write('\n')
        resultFile.write(BottleOriginHTMLEnd) 
    

    if price != 'blank':
        #resultFile.write('Price:')
        resultFile.write(BottlePriceHTMLStart)
        #resultFile.write('Wine Price:')
        resultFile.write(price)
        resultFile.write(BottlePriceHTMLEnd)
        resultFile.write('\n') 

'''

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
                
'''removed to test JSON writing (arrays)
    if foodName != 'blank':    
        # Note this should possibly renamed in either the template or a food section should be added
        resultFile.write(GlassProductHTMLStart)
        #resultFile.write('Food Name:')
        resultFile.write(foodName)
        resultFile.write(GlassProductHTMLEnd)
        resultFile.write('\n')
                
    if foodDescription != 'blank':
        resultFile.write(GlassDescriptionHTMLStart)
        #resultFile.write('Wine Description:')
        resultFile.write(foodDescription)
        resultFile.write('\n')
        resultFile.write(GlassDescriptionHTMLEnd) 
    
    if price != 'blank':
        #resultFile.write('Price:')
        resultFile.write(GlassPriceHTMLStart)
        #resultFile.write('Wine Price:')
        resultFile.write(price)
        resultFile.write(GlassPriceHTMLEnd)
        resultFile.write('\n') 
        
'''

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function takes in an array and writes it as content for wine by the glass.
#
# This is part A.1
#--------------------------------------------------------------------------------------

def writeWineByTheGlass(wine):


    # While not at the end

    wineLine = len(wine)

    i = 0
    

    
    # While there are at least two lines left
    while (i+1) < wineLine:

        
        # Because end of line has already been removed, check for a blank.
        # Advance index if the line is blank
        while wine[i] == '':
            i += 1

        # If the line is all uppercase, assign header
        upperCase = wine[i].isupper()
    
        if upperCase == True:
            
            # Write a header
            header = wine[i]
        
            # Write the header with correspondin HTML tags
    
            # resultFile.write(GlassHeaderHTMLStart)
            # resultFile.write(template1A)
            
            # ^ the above is replaced by this JSON line
            
            #resultFile.write('new code start')
            #resultFile.writelines(template1A)
            #resultFile.write(json.dumps(template1A))
            #resultFile.write('new code end')
            #resultFile.write(header)
            #resultFile.write(GlassHeaderHTMLEnd)
            #resultFile.write('\n')
        
        # Else
        else:
     
            # Write a wine
            writeSingleWineByTheGlassInfo(wine[i], wine[i+1])
            
            # Advance to the next line to account for two lines of information
            i += 1
        
        i += 1
        


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
        
            # Write the header with correspondin HTML tags
            '''removed to test JSON writing (arrays)    
            resultFile.write(GlassHeaderHTMLStart)
            resultFile.write(header)
            resultFile.write(GlassHeaderHTMLEnd)
            resultFile.write('\n')
            '''            
        
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
    
        '''removed to test JSON writing (arrays)
       
        if upperCase == True:
            
            
            # Write a header
            header = food[i]
        
            # Write the header with correspondin HTML tags
    
            resultFile.write(GlassHeaderHTMLStart)
            resultFile.write(header)
            resultFile.write(GlassHeaderHTMLEnd)
            resultFile.write('\n')
        
        # Else
        else:
     
            # Write a wine
            writeFoodInfo(food[i], food[i+1])
            
            # Advance to the next line to account for two lines of information
            i += 1
        '''
        i += 1

        

#--------------------------------------------------------------------------------------
# This function takes in an array and writes it as content for bottles.
#
# This is part C
#--------------------------------------------------------------------------------------

def writeBottles(bottle):
    
    # While not at the end

    bottleLine = len(bottle)

    i = 0

    # While there are at least two lines left
    while (i+1) < bottleLine:

        # Because end of line has already been removed, check for a blank.
        # Advance index if the line is blank
        while bottle[i] == '':
            i += 1

        # If the line is all uppercase, assign header
        upperCase = bottle[i].isupper()
    
       
        if upperCase == True:
            
            # Write a header
            header = bottle[i]
        
            # Write the header with correspondin HTML tags
    
            #resultFile.write(BottleHeaderHTMLStart)
            #resultFile.write(header)
            #resultFile.write(BottleHeaderHTMLEnd)
            #resultFile.write('\n')
        
        # Else
        else:
     
            # Write a wine
            writeSingleBottleInfo(bottle[i], bottle[i+1])
            
            # Advance to the next line to account for two lines of information
            i += 1
        
        i += 1



        

        
        
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


j = 0
    
while i < templateLength and keyWord1A != templateCode[i]:
    
    #resultFile.write(templateCode[i])
    #resultFile.write('\n')
    i += 1
    j += 1

i += 1

while i < templateLength and keyWord1B != templateCode[i]:
        
    
    #print(keyWord1B)
    #print(templateCode[i])
    template1A.append(templateCode[i])    
    #resultFile.write(templateCode[i])
    #resultFile.write('\n')
    i += 1
    
i += 1

# Advance to the next section
while i < templateLength and keyWord2_1A != templateCode[i]:
    
    i += 1
    
i += 1


while i < templateLength and keyWord2_1B != templateCode[i]:
            
    template1B.append(templateCode[i])    
    i += 1
    
i += 1

# Advance to the next section
while i < templateLength and keyWord2_2A != templateCode[i]:
    
    i += 1
    
i += 1

while i < templateLength and keyWord2_2B != templateCode[i]:
            
    template2A.append(templateCode[i])    
    i += 1
    
i += 1
'''
while i < templateLength and keyWord2A != templateCode[i]:
    
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1

i += 1


while i < templateLength and keyWord2B != templateCode[i]:
        
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1
    
i += 1

while i < templateLength and keyWord3A != templateCode[i]:
    
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1

i += 1


while i < templateLength and keyWord3B != templateCode[i]:
        
        
    CodeKeyWord = templateCode[i].rfind(' By The Glass Title ')

    if CodeKeyWord != -1:
        
        parsedTemplateCode = templateCode[i].split(' By The Glass Title ') #consider coverting this to a variable

        GlassHeaderHTMLStart = parsedTemplateCode[0]
        GlassHeaderHTMLEnd = parsedTemplateCode[1]
    
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1
    
i += 1
'''

'''
# Advance to the next Key Word.
        
while i < templateLength and keyWord !=templateCode[i]:
    
    i += 1    

    
#By the glass product    
    
i += 1



CodeKeyWord = templateCode[i].rfind(' By The Glass Header ')

if CodeKeyWord != -1:
        
    
        parsedTemplateCode = templateCode[i].split(' By The Glass Header ') #consider coverting this to a variable

        GlassHeaderHTMLStart = parsedTemplateCode[0]
        GlassHeaderHTMLEnd = parsedTemplateCode[1]
        

# Advance to the next Key Word.



while i < templateLength and keyWord2 !=templateCode[i]:
    
    i += 1    

    
#By the glass product    
    
i += 1
    
CodeKeyWord = templateCode[i].rfind(' By The Glass Product ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Product ') #consider coverting this to a variable

        GlassProductHTMLStart = parsedTemplateCode[0]
        GlassProductHTMLEnd = parsedTemplateCode[1]


#By the glass grapes   
    
i += 1
    
CodeKeyWord = templateCode[i].rfind(' By The Glass Grapes ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Grapes ') #consider coverting this to a variable

        GlassGrapesHTMLStart = parsedTemplateCode[0]
        GlassGrapesHTMLEnd = parsedTemplateCode[1]

        
        
#By the glass description
        
i += 1

CodeKeyWord = templateCode[i].rfind(' By The Glass Description ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Description ') #consider coverting this to a variable

        GlassDescriptionHTMLStart = parsedTemplateCode[0]
        GlassDescriptionHTMLEnd = parsedTemplateCode[1]          
        
        
#By the glass "Chilled"
        
i += 1

CodeKeyWord = templateCode[i].rfind(' By The Glass Chilled ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Chilled ') #consider coverting this to a variable

        GlassChilledHTMLStart = parsedTemplateCode[0]
        GlassChilledHTMLEnd = parsedTemplateCode[1]         
        
#By the glass price        
        
i += 1

CodeKeyWord = templateCode[i].rfind(' By The Glass Price ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Price ') #consider coverting this to a variable

        GlassPriceHTMLStart = parsedTemplateCode[0]
        GlassPriceHTMLEnd = parsedTemplateCode[1]

        
#By the glass origin        
        
i += 1

CodeKeyWord = templateCode[i].rfind(' By The Glass Origin ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Origin ') #consider coverting this to a variable

        GlassOriginHTMLStart = parsedTemplateCode[0]
        GlassOriginHTMLEnd = parsedTemplateCode[1]      
        
        
        

# Write each line of the Template to the Result file.
# --------------- BOTTLES --------------- #
        
while i < templateLength and keyWord3 !=templateCode[i]:
    
   
    i += 1         
        
# -------- 1 ----------- #

i += 1

CodeKeyWord = templateCode[i].rfind(' Bottle Header ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' Bottle Header ') #consider coverting this to a variable

        BottleHeaderHTMLStart = parsedTemplateCode[0]
        BottleHeaderHTMLEnd = parsedTemplateCode[1]
        
# -------- 2 ----------- #


while i < templateLength and keyWord4 !=templateCode[i]:
    

    i += 1   

i += 1

CodeKeyWord = templateCode[i].rfind(' Bottle Product ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' Bottle Product ') #consider coverting this to a variable

        BottleProductHTMLStart = parsedTemplateCode[0]
        BottleProductHTMLEnd = parsedTemplateCode[1]
        
# -------- 3 ----------- #

i += 1

CodeKeyWord = templateCode[i].rfind(' Bottle Description ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' Bottle Description ') #consider coverting this to a variable

        BottleDescriptionHTMLStart = parsedTemplateCode[0]
        BottleDescriptionHTMLEnd = parsedTemplateCode[1]

# -------- 4 ----------- #

i += 1

CodeKeyWord = templateCode[i].rfind(' Bottle Price ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' Bottle Price ') #consider coverting this to a variable

        BottlePriceHTMLStart = parsedTemplateCode[0]
        BottlePriceHTMLEnd = parsedTemplateCode[1]
        
# -------- 5 ----------- #

i += 1

CodeKeyWord = templateCode[i].rfind(' Bottle Grapes ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' Bottle Grapes ') #consider coverting this to a variable

        BottleGrapesHTMLStart = parsedTemplateCode[0]
        BottleGrapesHTMLEnd = parsedTemplateCode[1]
        
# -------- 6 ----------- #

i += 1

CodeKeyWord = templateCode[i].rfind(' Bottle Origin ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' Bottle Origin ') #consider coverting this to a variable

        BottleOriginHTMLStart = parsedTemplateCode[0]
        BottleOriginHTMLEnd = parsedTemplateCode[1]
        
'''
#---------------------------------------------------------------------------------------------------------
# End Template Part 1
#---------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------
#
# Content Part 1
#
#---------------------------------------------------------------------------------------------------------

#Add Content elements to the results array.    
with open('SCTestShort.txt') as contentFile:
    #rename menuContent to something like contentLine
    menuContent = contentFile.readlines()  



foodKeyWord = 'FOOD\n'
bottleKeyWord = 'SPARKLING WHITE\n'
# this variable does not include the end of line character, bacause it has already been removed.
nonWineKeyWord = 'BEER, CIDER, VERMOUTH & NON-ALCOHOLIC'


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

# Determine where FOOD starts in the document.
menuIndex = menuContent.index(foodKeyWord)

# Populate the array for by the glass.
byTheGlassIndex = 0
while byTheGlassIndex < menuIndex:

    contentWithoutEndOfLine = menuContent[byTheGlassIndex].strip("\n")
    byTheGlassContent.append(contentWithoutEndOfLine)
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
writeLines(template1B)


writeWineByTheGlass(byTheGlassWineContent)
    
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

writeNonWineByTheGlass(byTheGlassNonWineContent)

# ---------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------    


# Determine where bottles start ['SPARKLING WHITE'] in the document.
menuIndex = menuContent.index(bottleKeyWord)

# Populate the array for by the glass.

# Start the foodIndex where byTheGlassIndex left off.
foodIndex = byTheGlassIndex
while foodIndex < menuIndex:

    contentWithoutEndOfLine = menuContent[foodIndex].strip("\n")
    foodContent.append(contentWithoutEndOfLine)
    foodIndex += 1
    
writeFood(foodContent)


# ---------------------------------------------------------------------
# Part C
# ---------------------------------------------------------------------    

# Determine where the end of the file is.
menuIndex = len(menuContent)

# Populate the array for bottles.

# Start the bottleIndex where foodIndex left off.
bottleIndex = foodIndex
while bottleIndex < menuIndex:

    contentWithoutEndOfLine = menuContent[bottleIndex].strip("\n")
    bottleContent.append(contentWithoutEndOfLine)
    bottleIndex += 1
    
writeBottles(bottleContent)    



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

#Print all the elements of the Template array.
#Amend those elements to the Results array.
while i < templateLength: # and keyWord !=templateCode[i]:
    #matched_indexes.append(i)
    #print(templateCode[i])
    #resultFile.write(templateCode[i])
    #resultFile.write('\n')
    i += 1 

#---------------------------------------------------------------------------------------------------------
# End Template Part 2
#---------------------------------------------------------------------------------------------------------



#Close the Result File
resultFile.close()



#Open and read the file after the appending:
resultFile = open("Result.html", "r")
#print(resultFile.read())


    
    
    
    
    
    
    
    
    

