import csv
import collections

origin_f='F:\\毕业论文\\数据\\全国空气质量\\站点_20170101-20171231\\china_sites_20170101.csv'
new_f='F:\\毕业论文\\数据\\全国空气质量\\站点_20170101-20171231\\wuhan_20170101.csv'

list=[]
newlist=[]
finallist=[]


#读取csv文件,筛选需要的数据
with open(origin_f) as o_f:
    #reader=csv.reader(f)
    #for row in reader:
    num=0
    reader=csv.DictReader(o_f)
    for rows in reader:
        #只要AQI数据，筛选行
        if rows['type']=='AQI':
            list.append(rows)
    for rows in list:
        #筛选列
        dic = collections.OrderedDict()
        dic['date']=rows['date']
        dic['hour']=rows['hour']
        dic['type']=rows['type']
        dic['1325A']=rows['1325A']
        dic['1326A']=rows['1326A']
        dic['1327A']=rows['1327A']
        dic['1328A']=rows['1328A']
        dic['1329A']=rows['1329A']
        dic['1330A']=rows['1330A']
        dic['1331A']=rows['1331A']
        dic['1332A']=rows['1332A']
        dic['1333A']=rows['1333A']
        dic['1334A']=rows['1334A']
        newlist.append(dic)
    #重新拼接
    for i in range(25,35):
        for rows in newlist:
            dic=collections.OrderedDict()
            dic['id']='13'+str(i)+'A'
            dic['date'] = rows['date']
            dic['hour'] = rows['hour']
            dic['type'] = rows['type']
            dic['value']=rows['13'+str(i)+'A']
            finallist.append(dic)
    print(finallist)


#筛选出新的csv文件
with open(new_f,'w',newline='') as n_f:
    writer=csv.writer(n_f)
    for i,row in enumerate(finallist):
        if i==0:
            writer.writerow(row.keys())
            writer.writerow(row.values())
        else:
            writer.writerow(row.values())




