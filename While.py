#This code produces an error, but otherwise works as designed. Currently debugging.

templateHeader = []
with open('Template.txt') as templateFile:
    templateHeader = templateFile.readlines()




cars = ['Ford', 'BMW', 'Volvo', 'stop', 'Audi']
keyWord = 'stop\n'
matched_indexes = [] #rename this variable
i = 0
templateLength = len(templateHeader)

while i < templateLength and keyWord !=templateHeader[i]:
    matched_indexes.append(i)
    print(templateHeader[i])
    i += 1

print('Count is', i)
    
contentByTheGlass = []
with open('Content.txt') as contentFile:
    contentByTheGlass = contentFile.readlines()    
    
contentKeyWord = 'FOOD\n'
j = 0
templateLength = len(contentByTheGlass)

while j < templateLength and keyWord !=contentByTheGlass[j]:

    print(contentByTheGlass[j])
    j += 1
    
    
print('Count is', i)  
#i += 1
#print('Count is', i)


while i < templateLength: # and keyWord !=templateHeader[i]:
    matched_indexes.append(i)
    print(templateHeader[i])
    print('Count is', i)
    i += 1    

print('Count is', i)    
    
    
print(f'{keyWord} is not present in {templateHeader} at indexes {matched_indexes}')


  
