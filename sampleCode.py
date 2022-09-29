#file1 = open("SkinContactMenu.txt", "w")
#L = ["Wine \n", "Beer \n", "Food"]
#file1.writelines(L)
#file1.close()
 
# Append-adds at last
file1 = open("SkinContactMenu.txt", "a")  # append mode
file1.write("</HTML> \n")
file1.close()
 
file1 = open("SkinContactMenu.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
 
# Write-Overwrites
#file1 = open("myfile.txt", "w")  # write mode
#file1.write("Tomorrow \n")
#file1.close()
 
#file1 = open("myfile.txt", "r")
#print("Output of Readlines after writing")
#print(file1.read())
#print()
#file1.close()