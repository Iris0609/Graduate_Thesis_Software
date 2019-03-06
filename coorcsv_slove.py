import csv
import collections

origin_f='F:\\毕业论文\\数据\\全国空气质量\\城市_20170101-20171231\\china_cities_20170101.csv'
new_f='F:\\biyedata\\cities_20170101.csv'
coord_f='F:\\毕业论文\\数据\\全国空气质量\\全国城市坐标.csv'
newcoor_f='F:\\biyedata\\coordinate.csv'

list=[]
newlist=[]
finallist=[]
address=[]
coorlist=[]


#读取csv文件,筛选需要的数据
with open(origin_f,'r',encoding='UTF-8') as o_f:
    #reader=csv.reader(f)
    #for row in reader:
    num=0
    listreader=csv.reader(o_f)
    for i,rows in enumerate(listreader):
        if i==0:
            address = rows

with open(coord_f,'r',encoding='gbk') as coor_f:
    coorreader=csv.DictReader(coor_f)
    for rows in coorreader:
        for add in address[3:]:
            city=rows['city']

            if str(add) in city:
                dic = collections.OrderedDict()
                dic['province']=rows['province']
                dic['cityname']=rows['city1']
                dic['lon']=rows['lon']
                dic['lat']=rows['lat']
                coorlist.append(dic)

with open(newcoor_f,'w',newline='') as ncoor_f:
    writer=csv.writer(ncoor_f)
    for i,row in enumerate(coorlist):
        if i==0:
            writer.writerow(row.keys())
            writer.writerow(row.values())
        else:
            writer.writerow(row.values())



