import xlrd


def get_list(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rank_list = []
    for i in range(1, worksheet.nrows):
        rank_list.append(worksheet.cell_value(i, 1))
    return rank_list


def get_result(rank_list1, rank_list2):
    flag = False
    for j in range(len(rank_list1)):
        if rank_list1[j] in rank_list2:
            break
        if j == len(rank_list1) - 1:
            flag = True
    if flag:
        return rank_list1, rank_list2
    else:
        for i in range(max(len(rank_list1), len(rank_list2))):
            if i < min(len(rank_list1), len(rank_list2)) and rank_list1[i] == rank_list2[i]:
                rank_list2.pop(i)
                break
            if rank_list1[i] in rank_list2:
                if rank_list2.index(rank_list1[i]) > i:
                    rank_list2.pop(rank_list2.index(rank_list1[i]))
                else:
                    rank_list1.pop(i)
                break
        print(len(rank_list1), ", 改造后：", rank_list1)
        print(len(rank_list2), ", 改造后：", rank_list2)
        print("\n")
        return get_result(rank_list1, rank_list2)


if __name__ == '__main__':
    data_list1 = get_list("data1.xls")
    data_list2 = get_list("data2.xls")
    res = get_result(data_list1, data_list2)
    print("人气激励榜: ", res[0])
    print("勤奋主播榜: ", res[1])
