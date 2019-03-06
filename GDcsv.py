import csv
import collections


targetlist=['东莞','佛山','广州','河源','惠州','江门','清远','汕尾','韶关','深圳','阳江','云浮','肇庆','中山']
#datelist=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20',
#         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
datelist=['01','02','03','04','05']
gdlist=[]


for i in range(len(datelist)):
    origin_f='F:\\biyedata\\cities_201707'+datelist[i]+'.csv'
    final_f='F:\\biyedata\\GD_201707'+datelist[i]+'.csv'
    gdlist = []
    citylist = []
    # 读取csv文件,筛选需要的数据
    with open(origin_f, 'r', encoding='gbk') as o_f:
        # reader=csv.reader(f)
        # for row in reader:
        num = 0
        listreader = csv.DictReader(o_f)
        for rows in listreader:
            if rows['name'] in targetlist:
                dic = collections.OrderedDict()
                dic['date'] = rows['date']
                dic['name'] = rows['name']
                dic['value'] = rows['value']
                gdlist.append(dic)

        citydic = collections.OrderedDict()
        for j in range(len(targetlist)):
            val=0
            flag=0
            for rows in gdlist:
                if rows['name']==targetlist[j] and rows['value']is not "":
                    val=val+int(rows['value'])
                    flag=flag+1
            if flag!=0:
                citydic[targetlist[j]] = val/flag
                citylist.append(citydic)

    # 筛选出新的csv文件
    with open(final_f, 'w', newline='') as n_f:
        writer = csv.writer(n_f)
        for i, row in enumerate(citylist):
            if i == 0:
                writer.writerow(row.keys())
                writer.writerow(row.values())
            else:
                writer.writerow(row.values())

