#This code reads in two documents as arrays and creates a third file to combine them.


#designate the array for the HTML code.
templateHeader = ['<HTML>', 'line1', 'line2', '<p>', 'stop', '</p>', '<!--end-->', '</HTML>']
#with open('Template.txt') as templateFile:
#    templateHeader = templateFile.readlines()


resultFile = open("Result.html", "a")

#Define the key word to look for within the HTML file.
keyWord = 'stop'

#define an array to show what is happening at the end.
resultContent = [] 

i = 0
templateLength = len(templateHeader)

#Print all the elements of the Template array until the keyword is reached.
#Add those elements to the Results array.
while i < templateLength and keyWord !=templateHeader[i]:
    resultContent.append(templateHeader[i])
    print(templateHeader[i])
    resultFile.write(templateHeader[i])
    resultFile.write('\n')
    i += 1

print('    ')
#print('		After loop, count is', i)
    
#Add Content elements to the results array.    
contentByTheGlass = ['FOOD', 'Almonds', 'Pickles', 'Cheese']
#with open('Content.txt') as contentFile:
#    contentByTheGlass = contentFile.readlines()    

#not yet using contentKeyWord
contentKeyWord = 'FOOD'


j = 0
contentLength = len(contentByTheGlass)

#Print all the elements of the Content file
#Amend those elements to the Results file.
while j < contentLength:

    print(contentByTheGlass[j])
    resultContent.append(contentByTheGlass[j])
    resultFile.write(contentByTheGlass[j])
    resultFile.write('\n')
    j += 1
    
    

    
print('    ')
    

#Print all the elements of the Template array.
#Amend those elements to the Results array.
while i < templateLength: # and keyWord !=templateHeader[i]:
    #matched_indexes.append(i)
    print(templateHeader[i])
    resultContent.append(templateHeader[i])
    resultFile.write(templateHeader[i])
    resultFile.write('\n')
    i += 1    


print('    ')
print('I count is', i)    
    


print(f'TemplateHeader {templateHeader}')

print(f'Content {resultContent}')



#Close the Result File
resultFile.close()



#Open and read the file after the appending:
resultFile = open("Result.html", "r")
print(resultFile.read())


menuItem = "Domaine de Victor - a really nice red wine"

parsedMenuItem = menuItem.split('-')

wineName = parsedMenuItem[0]

wineDescription = parsedMenuItem[1]

print(wineName)

print(wineDescription)

  
