
from sys import argv
from validate import *
from symbol_table import *
from literal_table import *

script,action,filename = argv
#-----------------------------------------------------------------------
validate(action)
#-----------------------------------------------------------------------

with open(filename,'r') as f:
    list1 = []
    for line in f:
        line = line.strip()
        line = line.split(' ')
        list1.append(line)
for i in range(len(list1)):
    if (len(list1[i])>2):
        if list1[i][1] == 'db':
            list1[i][2] = " ".join(list1[i][2:])
            list1[i] = list1[i][:3]
        if list1[i][1] in data_type:
            list1[i][2] = "".join(list1[i][2:])
            list1[i] = list1[i][:3]
#--------------------------------------------------------------------------------------------------------------------------------------------------
#symbol table
(sym_table,label_table) = symbol_table(list1)
if (action == '-s'):
    print('\n')
    print("                                                          ** SYMBOL TABLE **                                                          ")
    print("======================================================================================================================================")
    print('lineNo.        name            size        No.ofElem           S/L             D/U              addr              value')
    print("======================================================================================================================================")
    for i in sym_table:
        for j in i:
            print(j,end='\t\t')
        print('\n')
    print('\n')
    print("                       ** LABEL TABLE **                ")
    print("========================================================")
    print("lineNo.         labelNo         name           D/U      ")
    print("========================================================")
    for i in label_table:
        for j in i:
            print(j, end='\t\t')
        print('\n')
#-------------------------------------------------------------------------------------------------------------------------------------------------
#literal table
lit_table = literal_table(list1)
if (action == '-l'): 
    print('\n')
    print("                                                    ** LITERAL TABLE **                                                ")
    print("=======================================================================================================================")
    print("lineNo               literalNo                 value(actual)                 value(in hex)")
    print("=======================================================================================================================")
    for i in lit_table:
        for j in i:
            print(j, end='\t\t\t')
        print('\n')






