#This code reads in two documents as arrays and creates a third file to combine them.

#This code now also parses a string into two strings to designate an item (wine name) and its description (the wine description).

#CoreContent3.txt

#designate the array for the HTML code.
with open('Template.txt') as templateFile:
    templateCode = templateFile.readlines()


resultFile = open("Result.html", "a")

#Define the key word to look for within the HTML file.
keyWord = 'BY THE GLASS HEADER\n'

keyWord2 = 'BY THE GLASS PRODUCT\n'

#define an array to show (print) what is happening at the end.
resultContent = [] 


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

        HTMLStart = parsedTemplateCode[0]
        HTMLEnd = parsedTemplateCode[1]
        

while i < templateLength and keyWord2 !=templateCode[i]:
    resultContent.append(templateCode[i])
    #print(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1    

    
#CodeKeyWord = templateCode[i].rfind(' By The Glass Product ')

if CodeKeyWord != -1:
        parsedTemplateCode = templateCode[i].split(' By The Glass Product ') #consider coverting this to a variable

        HTMLStart2 = 'HTML START CODE\n'
        HTMLEnd2 = 'HTML END CODE\n'
    


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
    contentByTheGlass = contentFile.readlines()    

#not yet using contentKeyWord
contentKeyWord = 'FOOD\n'


j = 0
contentLength = len(contentByTheGlass)

#Print all the elements of the Content file
#Amend those elements to the Results file.
while j < contentLength: 

    if contentByTheGlass[j].isupper():
        
        resultFile.write('The upper case has been found\n')
        
        
    #---------------    
    # Header    
    #---------------   
    
    if contentKeyWord == contentByTheGlass[j]:  

        
        print("step A")
        
        resultFile.write(HTMLStart)
        resultFile.write(contentByTheGlass[j])
        resultFile.write(HTMLEnd)
       
        
        
        
        
        #advance the respective indexes
        j += 1
        
    
        #---------------    
        # Product    
        #---------------   
        
        print("check A")
        print(contentByTheGlass[j])
        if contentByTheGlass[j] != '\n':
            
            
            print("step B")
            # Separate an item and its price
            contentFood = contentByTheGlass[j].lstrip()
        
            print("contendFood variable is:", contentFood)
            k = 0
            componentLength = len(contentFood)


            #split the string if more than two spaces
            while k < componentLength: 
                print("step E")
            
                if contentFood[k] == " ":
    
                    if contentFood[k+1] == " ":
    
                        Item = contentFood[:k]
                        #print('Item:', Item)
                        resultFile.write(HTMLStart2)
                        resultFile.write('Item:')
                        resultFile.write(Item)
                        resultFile.write('\n')
                        Price = contentFood[k+1:]
                        Price = Price.lstrip()
                        #print ('Price here:', Price)
                        resultFile.write('Price:')
                        resultFile.write(Price)
                        resultFile.write(HTMLEnd2)
                        resultFile.write('\n')
            
                        k = componentLength
            
                k += 1
        
    
            print("check B")
            print(contentByTheGlass[j])
    
    x = contentByTheGlass[j].rfind(" - ")
    
    if x != -1:
        
        print("step C")
        parsedMenuItem = contentByTheGlass[j].split(' - ')

        wineName = parsedMenuItem[0]
        wineDescription = parsedMenuItem[1]

        
        
        resultFile.write('\nWine Name Is:')
        resultFile.write(wineName)
        resultFile.write('\n')
        resultFile.write('\nWine Description Is:')
        resultFile.write(wineDescription)
        resultFile.write('\n')

    
    print("step D")
    resultContent.append(contentByTheGlass[j])
    #resultFile.write(contentByTheGlass[j])
    #resultFile.write('\n')
    #print(j)
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



    
    
    
    
    
    
    
    
    

