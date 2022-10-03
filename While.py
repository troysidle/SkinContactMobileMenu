#This code produces an error, but otherwise works as designed. Currently debugging.

#This code reads in two documents as arrays and creates a third file that combines them.


#designate the array for the HTML code.
templateHeader = ['<HTML>', 'line1', 'line2', '<p>', 'stop', '</p>', '<!--end-->', '</HTML>']
#with open('Template.txt') as templateFile:
#    templateHeader = templateFile.readlines()


#Define the key word to look for within the HTML file.
keyWord = 'stop'

#define an array to show what is happening at the end.
resultContent = [] 

i = 0
templateLength = len(templateHeader)

#Print all the elements of the array until the keyword is reached.
#Add those elements to the results array.
while i < templateLength and keyWord !=templateHeader[i]:
    resultContent.append(i)
    print(templateHeader[i])
    #print('Count is', i)
    i += 1

print('    ')
#print('		After loop, count is', i)
    
contentByTheGlass = ['FOOD', 'Almonds', 'Pickles', 'Cheese']
#with open('Content.txt') as contentFile:
#    contentByTheGlass = contentFile.readlines()    

#not yet using contentKeyWord
contentKeyWord = 'FOOD'
j = 0
contentLength = len(contentByTheGlass)

while j < contentLength:

    print(contentByTheGlass[j])
    resultContent.append(i+j)
    j += 1
    
    
print('    ')
    
#print('			J count is', j)  
i += 1
#print('		Count is', i)


while i < templateLength: # and keyWord !=templateHeader[i]:
    #matched_indexes.append(i)
    print(templateHeader[i])
    #print('		Count is', i)
    i += 1    


print('    ')
print('I count is', i)    
    
    
print(f'{keyWord} is not present in {templateHeader} at indexes {resultContent}')


  
