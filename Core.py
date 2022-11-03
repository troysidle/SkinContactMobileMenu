#This code reads in two documents and creates a third file to combine them.

#This code now also parses a string into two strings to designate an item (wine name) and its description (the wine description).

#Core.txt

#designate the array for the HTML code.

#Updated 10.31.22




# Open the Template file
with open('Template.txt') as templateFile:
    templateCode = templateFile.readlines()

     
# Create the Result HTML file   
resultFile = open("Result.html", "a")

#Define the key word to look for within the Template file.
keyWord = 'BY THE GLASS HEADER\n'

keyWord2 = 'BY THE GLASS PRODUCT\n'

keyWord3 = 'BY THE BOTTLE HEADER\n'

keyWord4 = 'BY THE BOTTLE PRODUCT\n'


#______
#initialzing a variable
item = 'initializing Item'
price = 'initializing Item'
#_________



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
# This function writes a by the glass wine item.
#
# Included are all associated attributes - description, origin, price, et.
#--------------------------------------------------------------------------------------



def writeGlassWineItem(lineReference):

    wineName = 'blank'
    wineGrapes = 'blank'
    wineDescription = 'blank'
    wineOrigin = 'blank'
    chilled = 'blank'
    price = 'blank'
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(lineReference)
    
    if split != -1:
        wineInfo = split[0]
        price = split[1]
    
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(wineInfo)
    
        c = splitChilled(price)
    
        if c != -1:
            chilled = c[0]
            price = c[1]
            
    
        if split != -1:
            wineName = split[0]
            wineGrapes = split[1]
        
        # Assing the following line the by the glass origin
        if menuContent[j+1] != 'blank':
            wineOrigin = menuContent[j+1]
        

            
                
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
        resultFile.write('\n')
        resultFile.write(GlassOriginHTMLEnd) 
    
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

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function writes a by the glass non wine item, such as beer, vermouth, etc.
#
# Included are all associated attributes - description, origin, price, et.
#--------------------------------------------------------------------------------------

def  writeGlassNonWineItem(lineReference):

    nonWineName = 'blank'
    nonWineOrigin = 'blank'
    nonWineDescription = 'blank'
    price = 'blank'
    
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(lineReference)
    
    
    if split != -1:
        nonWineInfo = split[0]
        price = split[1]
    
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(nonWineInfo)
    
        c = splitChilled(price)
    
        if c != -1:
            nonWineDescription = c[0]
            price = c[1]
            
    
        if split != -1:
            nonWineName = split[0]
            nonWineOrigin = split[1]
            

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
        resultFile.write('\n')
        resultFile.write(GlassOriginHTMLEnd) 
    
    if price != 'blank':
        #resultFile.write('Price:')
        resultFile.write(GlassPriceHTMLStart)
        #resultFile.write('Non Wine Price:')
        resultFile.write(price)
        resultFile.write(GlassPriceHTMLEnd)
        resultFile.write('\n') 


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
# This function pertains to Beer, Cider, Vermouth, Non-Alcoholic
#--------------------------------------------------------------------------------------

#is lineReference used in multiple functions incorrectly?
def writeOtherByTheGlass(lineReference):
  
    #all these variables can likely be deleted
    pricedItem = 'blank'
    item = 'blank'
    price = 'blank'
    description = 'blank'
    wineName = 'blank'
    wineDescription = 'blank'
    header = 'blank'
    wineInfo = 'blank'
    wineGrapes = 'blank'
    wineOrigin = 'blank'
    chilled = 'blank'
    

    if beerFinder != -1 or ciderFinder != -1 or vermouthFinder != -1 or nonalcoholicFinder != -1:
	       print('found a keyword')
    
    else:
	       print('no keywords found')

    #newnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnewnew            
    
    # If the line is separated by multiple blanks, assign wine info and price
    split = splitBlank(lineReference)
    
    if split != -1:
        wineInfo = split[0]
        price = split[1]
    
        # Look for a hyphen in the wine info and split into wine name and grapes
        split = splitHyphen(wineInfo)
    
        c = splitChilled(price)
    
        if c != -1:
            chilled = c[0]
            price = c[1]
            
    
        if split != -1:
            wineName = split[0]
            wineGrapes = split[1]
        
        # Assessing the following line the by the glass origin
        if menuContent[j+1] != 'blank':
            wineOrigin = menuContent[j+1]
        
    
    
    # Write the header with correspondin HTML tags
    if header != 'blank':
        resultFile.write(GlassHeaderHTMLStart)
        resultFile.write(header)
        resultFile.write(GlassHeaderHTMLEnd)
        resultFile.write('\n')
            
    if wineName != 'blank':                
        resultFile.write(GlassProductHTMLStart)
        resultFile.write(wineName)
        resultFile.write(GlassProductHTMLEnd)
        resultFile.write('\n')
                
    if wineGrapes != 'blank':        
        resultFile.write(GlassGrapesHTMLStart)
        resultFile.write(wineGrapes)
        resultFile.write(GlassGrapesHTMLEnd)
        resultFile.write('\n')    
            
    if wineDescription != 'blank':
        resultFile.write(GlassDescriptionHTMLStart)
        resultFile.write(wineDescription)
        resultFile.write('\n')
        resultFile.write(GlassDescriptionHTMLEnd) 
    
    if wineOrigin != 'blank':
        resultFile.write(GlassOriginHTMLStart)
        resultFile.write(wineOrigin)
        resultFile.write('\n')
        resultFile.write(GlassOriginHTMLEnd) 
    
    if chilled != 'blank':
        resultFile.write(GlassChilledHTMLStart)
        resultFile.write(chilled)
        resultFile.write(GlassChilledHTMLEnd)
        resultFile.write('\n')
    
    if price != 'blank':
        resultFile.write(GlassPriceHTMLStart)
        resultFile.write(price)
        resultFile.write(GlassPriceHTMLEnd)
        resultFile.write('\n')              
    

#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
# This function pertains to By The Glass
#--------------------------------------------------------------------------------------

def writeByTheGlassItem(lineReference):
  
    pricedItem = 'blank'
    item = 'blank'
    price = 'blank'
    description = 'blank'
    wineName = 'blank'
    wineDescription = 'blank'
    header = 'blank'
    wineInfo = 'blank'
    wineGrapes = 'blank'
    wineOrigin = 'blank'
    chilled = 'blank'
    
    
    # Get rid of any blank space at the beginning of the line
    #lineReference = menuContent[j].lstrip()
    
    beerFinder = lineReference.find("BEER")
    ciderFinder = lineReference.find("CIDER")
    vermouthFinder = lineReference.find("VERMOUTH")
    nonalcoholicFinder = lineReference.find("NON-ALCOHOLIC")
    
    notBeerHeader = 'true'
        
    while notBeerHeader == 'true':
    
    # If the line is all uppercase, assign header
    x = lineReference.isupper()
    #print(x)
    if x == True:
        header = lineReference
        
        # Write the header with correspondin HTML tags
    
        resultFile.write(GlassHeaderHTMLStart)
        resultFile.write(header)
        resultFile.write(GlassHeaderHTMLEnd)
        resultFile.write('\n')
        
        # go to the next line
        j += 1
        
        y = menuContent[j].isupper()
        
        while y == False:     
        lineReference = menuContent[j].lstrip()
        
            writeGlassWineItem(lineReference)
            
            j+=1
            
        else:
    
            notBeerHeader = 'false'
            writeGlassNonWineItem(lineReference)
    
    
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
# This function...
#--------------------------------------------------------------------------------------

def writeAnItem(lineReference):
  
    pricedItem = 'blank'
    Item = 'blank'
    Price = 'blank'
    glassDescription = 'blank'
    wineName = 'blank'
    wineDescription = 'blank'
    
    
    # Get rid of any blank space at the beginning of the line
    lineReference = menuContent[j].lstrip()
    
    # Split the full line where there are more than two spaces
    split = splitBlank(lineReference)
    
    # Assign item and price if there is a line with blanks.
    if split != -1:
        pricedItem = split[0]
        Price = split[1]
    
    
    
    # Look for a hyphen in the Item and split into wine name and wine description
    
    split = splitBlank(Item)
    
    if split != -1:
        wineName = split[0]
        wineDescription = split[1]
        
    else:
        Item = pricedItem
    
    
    if Item == 'blank':
        glassDescription = lineReference
    
    
    if Item != 'blank':                
        resultFile.write(GlassProductHTMLStart)
        resultFile.write('Item:')
        resultFile.write(Item)
        resultFile.write('\n')
        resultFile.write(GlassProductHTMLEnd)        
        
    if wineDescription != 'blank':
        resultFile.write(BottleDescriptionHTMLStart)
        resultFile.write(wineDescription)
        resultFile.write('\n')
        resultFile.write(BottleDescriptionHTMLEnd) 
                   
    if glassDescription != 'blank':
        resultFile.write(GlassDescriptionHTMLStart)
        resultFile.write (glassDescription)
        resultFile.write('\n')
        resultFile.write(GlassDescriptionHTMLEnd) 
    
    if Price != 'blank':
        resultFile.write(BottlePriceHTMLStart)
        resultFile.write(Price)
        resultFile.write(BottlePriceHTMLEnd)
        resultFile.write('\n')              
    

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
while i < templateLength and keyWord !=templateCode[i]:
    
    #print(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1

i += 1

#parse the template string here first.

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
        

#---------------------------------------------------------------------------------------------------------
# End Template Part 1
#---------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------
#
# Content Part 1
#
#---------------------------------------------------------------------------------------------------------

#Add Content elements to the results array.    
with open('SCtestRed.txt') as contentFile:
    #rename menuContent to something like contentLine
    menuContent = contentFile.readlines()    


FoodKeyWord = 'FOOD\n'

BottleKeyWord = 'SPARKLING WHITE\n'


j = 0
contentLength = len(menuContent)

#Print all the elements of the Content file
#Amend those elements to the Results file.
while j < contentLength: 

        
    #---------------    
    # Product - BY THE GLASS    
    #---------------  
        
    #Until the end first key word...
    # as long not at the end of the file...
    while menuContent[j] != FoodKeyWord:
        
        # Separate an item and its price
        #should this line be included in the writeAnItem function?
        contentByTheGlass = menuContent[j].lstrip()

        writeByTheGlassItem(contentByTheGlass)
        
        j += 1
            
        
    
    #---------------    
    # Header - FOOD
    #---------------   
    
    #if the title is FOOD
    if FoodKeyWord == menuContent[j]:  
        
        resultFile.write(GlassHeaderHTMLStart)
        resultFile.write(menuContent[j])
        resultFile.write(GlassHeaderHTMLEnd)
        
        j += 1 
        

    
        #---------------    
        # Product - FOOD    
        #---------------  
        
        #Until the end next key word...
        # as long not at the end of the file...
        while j < contentLength:
        
            if menuContent[j] != BottleKeyWord and menuContent[j] != '\n':
        
                # Separate an item and its price
                contentFood = menuContent[j].lstrip()

                writeAnItem(contentFood)
            
            if BottleKeyWord == menuContent[j]:
    
                resultFile.write(BottleHeaderHTMLStart)
                resultFile.write(menuContent[j])
                resultFile.write(BottleHeaderHTMLEnd)
                
                j += 1
    
                #Until the end next blank line...
                while menuContent[j] != '\n':
                
                    writeAnItem(menuContent[j])
        
                    j += 1
                
            j += 1

    
    j += 1

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
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1 

#---------------------------------------------------------------------------------------------------------
# End Template Part 2
#---------------------------------------------------------------------------------------------------------



#Close the Result File
resultFile.close()



#Open and read the file after the appending:
resultFile = open("Result.html", "r")
print(resultFile.read())




    
    
    
    
    
    
    
    
    

