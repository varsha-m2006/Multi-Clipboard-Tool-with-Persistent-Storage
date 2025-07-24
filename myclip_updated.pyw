#Updated version of Multi-Clipboard-Tool, using shelve to, store all copied texts that can be accesed based on users preference

#importing rquired modules
import sys
import pyperclip
import shelve

#opening shelve file that acts like a persistant dictionary
shelveFile=shelve.open('mcb')

#save command
if(len(sys.argv)==3 and sys.argv[1]=='save'):
    shelveFile[sys.argv[2]]=pyperclip.paste()

#if only two items
elif(len(sys.argv)==2):
    #list command
    if(sys.argv[1]=='list'):
        pyperclip.copy(str(list(shelveFile.keys())))
    #load/copy command based on keyword
    else:
        pyperclip.copy(shelveFile[sys.argv[1]])

#delete keyword command
elif(len(sys.argv)==3 and sys.argv[1]=='delete'):
    #if keyword found
    if sys.argv[2] in shelveFile:
        del shelveFile[sys.argv[2]]
    #if it doesn't exist
    else:
        print(f"Keyword '{sys.argv[2]}' not found.")

#delete all keywords command
elif(len(sys.argv)==2 and sys.argv[1]=='delete-all'):
    for i in list(shelveFile.keys()):
        del shelveFile[i]
    
#closing file is always a good practice. it frees up software systems
shelveFile.close()