
def intermediate(list1,sym_table,label_table,lit_table):
    list2 = list1 
    reg32 = ['eax','ecx','edx','ebx','esp','ebp','esi','edi']
    reg32_1 = ['eax,','ecx,','edx,','ebx,','esp,','ebp,','esi,','edi,']
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            temp = list2[i][j]
            if temp in reg32:
                list2[i][j] = 'reg#' + str(reg32.index(temp) + 1)
            if temp in reg32_1:
                list2[i][j] = 'reg#' + str(reg32_1.index(temp) + 1) + ','
            for k in range(len(sym_table)):
                if temp == sym_table[k][1]:
                    list2[i][j] = 'sym#' + str(k+1)
            for k in range(len(label_table)):
                if (temp == label_table[k][2]) or (temp == label_table[k][2] + ':'):
                    list2[i][j] = label_table[k][1]
            for k in range(len(lit_table)):
                if temp == lit_table[k][2]:
                    list2[i][j] = lit_table[k][1]
    
    with open('intermediate.txt','w+') as f:
        for i in range(len(list2)):
            list2[i] = ' '.join(list2[i])  + '\n'
            f.write(list2[i])
