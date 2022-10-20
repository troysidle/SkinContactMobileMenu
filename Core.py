#This code reads in two documents as arrays and creates a third file to combine them.

#This code now also parses a string into two strings to designate an item (wine name) and its description (the wine description).

#Core2.txt

#designate the array for the HTML code.
with open('Template.txt') as templateFile:
    templateCode = templateFile.readlines()

resultFile = open("Result.html", "a")

#Define the key word to look for within the HTML file.
keyWord = 'BY THE GLASS HEADER\n'

keyWord2 = 'BY THE GLASS PRODUCT\n'

keyWord3 = 'BY THE BOTTLE HEADER\n'

keyWord4 = 'BY THE BOTTLE PRODUCT\n'

#define an array to show (print) what is happening at the end.
resultContent = [] 



def firstFunction(fullLine):
    print("Hello from a function")
  
    fullLine = contentByTheGlass[j].lstrip()

    #print("contendFood variable is:", contentFood)
    k = 0
    componentLength = len(fullLine)

    wineName = 'blank'
    wineDescription = 'blank'

    #split the string where there are more than two spaces
    while k < componentLength: 
        #print("step E")
            
        if fullLine[k] == " ":
    
            if fullLine[k+1] == " ":
    
                Item = fullLine[:k]
                #print('Item:', Item)
                
                
                            
                
                Price = fullLine[k+1:]
                Price = Price.lstrip()
                #print ('Price here:', Price)
                
            
                k = componentLength
            
        k += 1
        
    x = Item.rfind(" - ")
                
    if x != -1:
                    #print("step C")
                    parsedMenuItem = Item.split(' - ')

                    wineName = parsedMenuItem[0]
                    wineDescription = parsedMenuItem[1]
                    
                    Item = wineName

        
        
                    
                    
                    
    resultFile.write(GlassProductHTMLStart)
    #resultFile.write('Item:')
    resultFile.write(Item)
    resultFile.write('\n')
    resultFile.write(GlassProductHTMLEnd)        
                    
    #if wineName != 'blank':
    #    resultFile.write('Wine Name:')
    #    resultFile.write(BottleProductHTMLStart)
    #    resultFile.write(wineName)
    #    resultFile.write('\n')
    #    resultFile.write(BottleProductHTMLEnd)
        
    if wineDescription != 'blank':
        #resultFile.write('Description:')
        resultFile.write(BottleDescriptionHTMLStart)
        resultFile.write(wineDescription)
        resultFile.write('\n')
        resultFile.write(BottleDescriptionHTMLEnd)            
                    
    #resultFile.write('Price:')
    resultFile.write(BottlePriceHTMLStart)
    resultFile.write(Price)
    resultFile.write(BottlePriceHTMLEnd)
    resultFile.write('\n')                
        #print("check B")
        #print(contentByTheGlass[j])
            
#    x = contentByTheGlass[j].rfind(" - ")
#    
#    if x != -1:
#        
#        #print("step C")
#        parsedMenuItem = contentByTheGlass[j].split(' - ')
#
#        wineName = parsedMenuItem[0]
#        wineDescription = parsedMenuItem[1]
#
#        
#        
#        
#        resultFile.write(BottleProductHTMLStart)
#        resultFile.write(wineName)
#        resultFile.write('\n')
#        resultFile.write(BottleProductHTMLEnd)
#        
#        resultFile.write(BottleDescriptionHTMLStart)
#        
#        resultFile.write(wineDescription)
#        resultFile.write('\n')
#        resultFile.write(BottleDescriptionHTMLEnd)
#
#    
#        #print("step D")
#        #resultContent.append(contentByTheGlass[j])
#        #resultFile.write(contentByTheGlass[j])
#        #resultFile.write('\n')
#        #print(j)













#---------------------------------------------------------------------------------------------------------
#
# Template Part 1
#
#---------------------------------------------------------------------------------------------------------

#Print all the elements of the Template array until the keyword is reached.
#Add those elements to the Results array.

#Write to the Result file all the elements of the Template array until the keyword is reached.

templateLength = len(templateCode)
i = 0
while i < templateLength and keyWord !=templateCode[i]:
    resultContent.append(templateCode[i])
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
        

# Write each line of the Template to the Result file.
        
while i < templateLength and keyWord2 !=templateCode[i]:
    resultContent.append(templateCode[i])
    #print(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1    

i += 1
    
CodeKeyWord = templateCode[i].rfind(' By The Glass Product ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Product ') #consider coverting this to a variable

        GlassProductHTMLStart = parsedTemplateCode[0]
        GlassProductHTMLEnd = parsedTemplateCode[1]
        
i += 1

CodeKeyWord = templateCode[i].rfind(' By The Glass Price ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Price ') #consider coverting this to a variable

        GlassPriceHTMLStart = parsedTemplateCode[0]
        GlassPriceHTMLEnd = parsedTemplateCode[1]


# Write each line of the Template to the Result file.
# --------------- BOTTLES --------------- #
        
while i < templateLength and keyWord3 !=templateCode[i]:
    resultContent.append(templateCode[i])
    #print(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
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
    resultContent.append(templateCode[i])
    #print(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
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
with open('Content.txt') as contentFile:
    #rename contentByTheGlass to something like contentLine
    contentByTheGlass = contentFile.readlines()    


FoodKeyWord = 'FOOD\n'

BottleKeyWord = 'WHITE WINE\n'


j = 0
contentLength = len(contentByTheGlass)

#Print all the elements of the Content file
#Amend those elements to the Results file.
while j < contentLength: 

        
    
    #---------------    
    # Header    
    #---------------   
    
    #if the title is FOOD
    if FoodKeyWord == contentByTheGlass[j]:  

        
        #print("step A")
        
        resultFile.write(GlassHeaderHTMLStart)
        resultFile.write(contentByTheGlass[j])
        resultFile.write(GlassHeaderHTMLEnd)

        
        j += 1 
        

    
        #---------------    
        # Product    
        #---------------  
        
        
        
        
        #Until the end next blank line...
        while contentByTheGlass[j] != '\n':
            #print("check A")
            #print(contentByTheGlass[j])
            
            #if it's not a blank line...
            #if contentByTheGlass[j] != '\n':
            
            
            #print("step B")
            # Separate an item and its price
            contentFood = contentByTheGlass[j].lstrip()
        

            firstFunction(contentFood)
            
            
                
                
            j += 1         
            
    
    
    
    if BottleKeyWord == contentByTheGlass[j]:
    
        resultFile.write(BottleHeaderHTMLStart)
        resultFile.write(contentByTheGlass[j])
        resultFile.write(BottleHeaderHTMLEnd)
                
        j += 1
    
        #Until the end next blank line...
        while contentByTheGlass[j] != '\n':
                
                firstFunction(contentByTheGlass[j])
        
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



#---------------------------------------------------------------------------------------------------------
# End Template Part 2
#---------------------------------------------------------------------------------------------------------

    



#Close the Result File
resultFile.close()



#Open and read the file after the appending:
resultFile = open("Result.html", "r")
print(resultFile.read())



    
    
    
    
    
    
    
    
    

