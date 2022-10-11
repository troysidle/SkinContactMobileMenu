#This code reads in two documents as arrays and creates a third file to combine them.

#Core.txt

#designate the array for the HTML code.
with open('Template.txt') as templateFile:
    templateCode = templateFile.readlines()


resultFile = open("Result.html", "a")

#Define the key word to look for within the HTML file.
keyWord = 'stop\n'

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
    print(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1

print('    ')
#print('		After loop, count is', i)


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
contentKeyWord = 'FOOD'


j = 0
contentLength = len(contentByTheGlass)

#Print all the elements of the Content file
#Amend those elements to the Results file.
while j < contentLength:

    x = contentByTheGlass[j].rfind("-")
    
    if x != -1:
        print(x)
    
        parsedMenuItem = contentByTheGlass[j].split('-')

        wineName = parsedMenuItem[0]
        wineDescription = parsedMenuItem[1]

        print(wineName)

        print(wineDescription)
        resultFile.write('\nWine Name Is:')
        resultFile.write(wineName)
        resultFile.write('\nWine Description Is:')
        resultFile.write(wineDescription)
    
    
    print(contentByTheGlass[j])
    resultContent.append(contentByTheGlass[j])
    resultFile.write(contentByTheGlass[j])
    resultFile.write('\n')
    j += 1
    
    

    
print('    ')

#---------------------------------------------------------------------------------------------------------
# End Content Part 1
#---------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------
#
# Template Part 2
#
#---------------------------------------------------------------------------------------------------------



#Print all the elements of the Template array.
#Amend those elements to the Results array.
while i < templateLength: # and keyWord !=templateCode[i]:
    #matched_indexes.append(i)
    print(templateCode[i])
    resultContent.append(templateCode[i])
    resultFile.write(templateCode[i])
    resultFile.write('\n')
    i += 1    

#---------------------------------------------------------------------------------------------------------
# End Template Part 2
#---------------------------------------------------------------------------------------------------------

    
    
print('    ')
print('I count is', i)    
    


print(f'templateCode {templateCode}')

print(f'Content {resultContent}')



#Close the Result File
resultFile.close()



#Open and read the file after the appending:
resultFile = open("Result.html", "r")
print(resultFile.read())


#menuItem = "Domaine de VictorSample - a really nice sample red wine"

#parsedMenuItem = menuItem.split('-')

#wineName = parsedMenuItem[0]

#wineDescription = parsedMenuItem[1]

#print(wineName)

#print(wineDescription)

  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#---------------------------------- This is working code that parses at the hypen. 10-10-22. Needs commenting and incorporating into code above.
#Add Content elements to the results array.    
#.#contentByTheGlass = ['FOO-D', 'Almonds', 'Pickles', 'Cheese', 'Domaine de RogerSample - a really nice sample rose wine']
#with open('Content.txt') as contentFile:
#    contentByTheGlass = contentFile.readlines()    

#not yet using contentKeyWord
#.#contentKeyWord = 'FOOD'


#.#j = 0
#.#contentLength = len(contentByTheGlass)

#parsedMenuItem = ['hello-there', 'test']








#Print all the elements of the Content file
#Amend those elements to the Results file.
#.#while j < contentLength:


#.#    x = contentByTheGlass[j].rfind("-")

#.#    if x != -1:
#.#        print(x)
    
#.#        parsedMenuItem = contentByTheGlass[0].split('-')

#.#        wineName = parsedMenuItem[0]
#.#        wineDescription = parsedMenuItem[1]

#.#        print(wineName)

#.#        print(wineDescription)

	

#.#    print(wineName)
#.#    print(wineDescription)
#.#    print(contentByTheGlass[j])
#.#    #resultContent.append(contentByTheGlass[j])
#.#    #resultFile.write(contentByTheGlass[j])
#.#    #resultFile.write('\n')
#.#    j += 1
#.#---------------------#
    
