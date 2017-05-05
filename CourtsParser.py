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
content = get_data(os.path.join(directory, "N-1-за-12-месяцев-2015-г.xlsx"))
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
        #ищем таблицы по признаку наличия ячейки "№ стр"
        if count_No > 0:
            top = i #top = верхняя строка каждой таблицы
            for k, d1 in enumerate(data):
                if k>i and d1.count(1): #ищем левую границу данных в таблице - там должна быть записана единица
                    print(("{0}: всего: {1} {2}").format(str(c[0]), count_No, str(d)))
                    print(("{0}: {1}").format(str(c[0]), str(d1)))
                    first_datacol_id = [l for l, x in enumerate(d1) if isint((x))] #строка таблицы с номерами строк
                    first_datacol = [x for x, x in enumerate(d1) if isint((x))] #номера ячеек с номерами строк
                    ones = [l for l, x in enumerate(first_datacol) if x==1] #номера по горизонтали ячеек, содержащих "1"
                    print(first_datacol_id)
                    print(first_datacol)
                    print(ones)
                    for l, one in enumerate(ones):
                        #определяем левую и правую границы данных (цифра "1" и последняя цифра в той же строке
                        left = first_datacol_id[one]
                        try:
                            right = first_datacol_id[ones[l + 1] - 1]
                        except:
                            right = first_datacol_id[len(first_datacol_id) - 1]
                        #определяем нижнюю границу таблицы: от "1" по горизонтали сместиться на одну позицию
                        #влево и вниз (это kk > k) и перебирать столбец, пока в нем есть цифра.
                        #последняя цифра и есть нижняя граница таблицы
                        for kk, d2 in enumerate(data):
                            if kk > k:
                                if len(d2) >= left and isint(d2[left - 1]):
                                    bottom = kk
                                else:
                                    break


                        lst = list()
                        lst.append(left)
                        lst.append(top)
                        lst.append(right)
                        lst.append(bottom)
                        list_A.append(lst)
                        print(("left ({0},{1}), right ({2}, {3}), top {4}, bottom {5}").format(left, d1[left], right, d1[right], top, bottom))
                    break
            #ищем нижние строки таблиц


            #print(type(d).__name__ + " " + str(d))

#найти пары "Наименование показателя" - № строки

#worksheets = list(data.items())[2]
#worksheets = list(data.items())[1]
#print(worksheets)
#jsondata = json.dumps(data)