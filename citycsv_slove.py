import csv
import collections

origin_f='F:\\毕业论文\\数据\\全国空气质量\\城市_20170101-20171231\\china_cities_20170430.csv'
new_f='F:\\biyedata\\tmp.csv'
coord_f='F:\\毕业论文\\数据\\全国空气质量\\全国城市坐标.csv'
newcoor_f='F:\\biyedata\\coordinate.csv'
final_f='F:\\biyedata\\cities_20170430.csv'

list=[]
newlist=[]
finallist=[]
address=[]
coorlist=[]
llist=[]


#读取csv文件,筛选需要的数据
with open(origin_f,'r',encoding='UTF-8') as o_f:
    #reader=csv.reader(f)
    #for row in reader:
    num=0
    listreader=csv.reader(o_f)
    for i,rows in enumerate(listreader):
        if i==0:
            address = rows

#坐标文件
with open(newcoor_f,'r',encoding='gbk') as ncoor_f:
    coorreader=csv.DictReader(ncoor_f)
    for rows in coorreader:
        dic = collections.OrderedDict()
        dic['province']=rows['province']
        dic['cityname']=rows['cityname']
        dic['lon']=rows['lon']
        dic['lat']=rows['lat']
        coorlist.append(dic)

with open(origin_f,'r',encoding='UTF-8') as o_f:
    reader=csv.DictReader(o_f)
    for rows in reader:
        #只要AQI数据，筛选行
        if rows['type']=='AQI':
            list.append(rows)

    for rows in list:
        dic = collections.OrderedDict()
        for field in address:
            dic[field]=rows[field]
        newlist.append(dic)

#重新拼接
    idnum=0
    for field in address[3:]:
        for rows in newlist:
            dic=collections.OrderedDict()
            dic['id']=idnum
            dic['date'] = rows['date']
            dic['hour'] = rows['hour']
            dic['type'] = rows['type']
            dic['name']=field
            dic['value']=rows[field]
            finallist.append(dic)
            idnum=idnum+1

#筛选出新的csv文件
with open(new_f,'w',newline='') as n_f:
    writer=csv.writer(n_f)
    for i,row in enumerate(finallist):
        if i==0:
            writer.writerow(row.keys())
            writer.writerow(row.values())
        else:
            writer.writerow(row.values())


with open(new_f,'r',encoding='gbk') as n_f:
    reader=csv.DictReader(n_f)
    for rows in reader:
        dic = collections.OrderedDict()
        dic['id'] = rows['id']
        dic['date'] = rows['date']
        dic['hour'] = rows['hour']
        dic['type'] = rows['type']
        dic['name'] = rows['name']
        dic['value'] = rows['value']
        for coor in coorlist:
            if rows['name'] in coor['cityname']:
                dic['province']=coor['province']
                dic['name']=coor['cityname']
                dic['lon']=coor['lon']
                dic['lat']=coor['lat']
        llist.append(dic)
#删除没有经纬度坐标的记录
    for i,rows in enumerate(llist):
        if 'lon' not in rows.keys():
            rows.clear()

#筛选出新的csv文件
with open(final_f,'w',newline='') as fin_f:
    writer=csv.writer(fin_f)
    for i,row in enumerate(llist):
        if i==0:
            writer.writerow(row.keys())
            writer.writerow(row.values())
        elif 'lon' in row.keys():
            writer.writerow(row.values())








