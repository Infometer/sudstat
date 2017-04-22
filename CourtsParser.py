from pyexcel_xlsx import get_data, save_data
import json
import os

def isint(s):
    try:
        int(s)
        return True
    except:
        return False

directory = "d:/WorkDir2/Python3/CourtsParser"
content = get_data(os.path.join(directory, "Копия F1-ug_pr-vo_1_inst-2015.xlsx"))
table_top = 0
table_right = 0
table_left = 0
table_bottom = 0
table_valuecols = list()
list_A = list()
#цикл по листам книги
for c in list(content.items()):
    data = c[1]
    #цикл по строкам листа. в одной строке может быть несколько таблиц
    for i, d in enumerate(data):
        count_No = str(d).replace(r"\n","").replace(" ", "").lower().count("№стр")
        #count_A = d.count("А")
        #ищем таблицы по признаку наличия ячейки "№ стр"
        if count_No > 0:
            table_top = i #верхняя строка таблицы
            for k, d1 in enumerate(data):
                if k>i and d1.count(1): #ищем левую границу таблиц - там должна быть записана единица
                    print(("{0}: всего: {1} {2}").format(str(c[0]), count_No, str(d)))
                    print(("{0}: {1}").format(str(c[0]), str(d1)))
                    first_datacol_id = [l for l, x in enumerate(d1) if isint((x))]
                    first_datacol = [x for x, x in enumerate(d1) if isint((x))]
                    print(first_datacol_id)
                    #first_datacol.append(1)
                    print(first_datacol)
                    #for n, nc in enumerate(first_datacol):
                     #   if nc[n] == 1:
                      #      if n > 0:
                       #         print (("id for 1={0}, id for last={1}, last={2}").format(first_datacol_id[n], first_datacol_id[n-1], first_datacol[]))
                        #elif nc[n] > nc[n-1]

                    #for n, nc in enume
                    # for n, nc in enumerate(d1):
                    #         if n >= first_datacol_id:
                    #             if isint(nc):
                    #                 table_right = int(nc)
                    #             else:
                    #                 print (table_right)
                    #                 break



                    #print(str(d).replace(r"\n","").replace(" ", ""))
                    break

            #print(type(d).__name__ + " " + str(d))

#найти пары "Наименование показателя" - № строки

#worksheets = list(data.items())[2]
#worksheets = list(data.items())[1]
#print(worksheets)
#jsondata = json.dumps(data)