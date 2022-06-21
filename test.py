import xlrd
from xlwt import Workbook


def get_list(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rank_list = []
    for i in range(1, worksheet.nrows):
        rank_list.append(worksheet.cell_value(i, 1))
    return rank_list


def get_rank(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rank_list = []
    for i in range(1, worksheet.nrows):
        rank_list.append(int(worksheet.cell_value(i, 3)))
    return rank_list


bonus_list1 = get_rank("data1.xls")
bonus_list2 = get_rank("data2.xls")


def get_result(rank_list1, rank_list2):
    flag = False
    for j in range(len(rank_list1)):
        if rank_list1[j] in rank_list2:
            break
        if j == len(rank_list1) - 1 or len(rank_list1) + len(rank_list2) <= 100:
            flag = True
    if flag:
        return rank_list1, rank_list2
    else:
        for i in range(max(len(rank_list1), len(rank_list2))):
            if i < min(len(rank_list1), len(rank_list2)) and rank_list1[i] == rank_list2[i]:
                if bonus_list1[i] >= bonus_list2[i]:
                    rank_list2.pop(i)
                else:
                    rank_list1.pop(i)
                break
            if rank_list1[i] in rank_list2:
                index = rank_list2.index(rank_list1[i])
                if bonus_list1[i] > bonus_list2[index]:
                    rank_list2.pop(index)
                else:
                    rank_list1.pop(i)
                break
        print("改造后list1：", rank_list1, " 长度：", len(rank_list1))
        print("改造后list2：", rank_list2, " 长度：", len(rank_list2))
        print("\n")
        return get_result(rank_list1, rank_list2)


def get_excel(result):
    wb = Workbook(encoding='utf-8')
    sheet1 = wb.add_sheet('人气激励榜')
    sheet1.write(0, 0, "排名")
    sheet1.write(0, 1, "主播昵称")
    sheet1.write(0, 2, "奖励")
    sheet2 = wb.add_sheet('勤奋主播榜')
    sheet2.write(0, 0, "排名")
    sheet2.write(0, 1, "主播昵称")
    sheet2.write(0, 2, "奖励")
    popularity_csv = []
    diligent_csv = []
    for i in range(0, len(result[0])):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, result[0][i])
        sheet1.write(i + 1, 2, bonus_list1[i])
        popularity_csv.append([i + 1, result[0][i], bonus_list1[i]])
    for i in range(0, len(result[1])):
        sheet2.write(i + 1, 0, i + 1)
        sheet2.write(i + 1, 1, result[1][i])
        sheet2.write(i + 1, 2, bonus_list2[i])
        diligent_csv.append([i + 1, result[1][i], bonus_list2[i]])
    print(popularity_csv)
    print(diligent_csv)
    wb.save('result.xls')


if __name__ == '__main__':
    data_list1 = get_list("data1.xls")
    data_list2 = get_list("data2.xls")
    print("改造前list1：", data_list1)
    print("改造前list2：", data_list2)
    print("\n")
    res = get_result(data_list1, data_list2)
    print("人气激励榜: ", res[0])
    print("勤奋主播榜: ", res[1])
    print("\n")
    get_excel(res)
