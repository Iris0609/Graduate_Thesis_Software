import sqlite3
import os
import pandas
import math
'''
file="F:/biyedata/Guangdong_AMJ.csv"

path1=os.path.abspath('.')
print(path1)
cx = sqlite3.connect(path1+'/test.db')
insert_data=pandas.read_csv(file,encoding='gbk',header=1,sep=',')
insert_data.to_sql('aoi',cx,if_exists='append',index=False)
'''
pre=[26.50671683,27.96757992,36.19277327,39.77996851,32.66898299,24.63529224,60.57262014,34.54553236,40.52905031,17.43274696,20.36465156,24.20805742,34.67572224,16.7036298]
real=[39.625,42.91666667,40.16666667,32.33333333,22.70833333,40.54166667,47.79166667,22.875,38.95833333,20.41666667,26,46.75,60.70833333,22.5]
mre_list=[]
rmse=0
for i in range(14):
    mre=(pre[i]-real[i])/real[i]
    mre_list.append(mre)
    rmse+=(pre[i]-real[i])*(pre[i]-real[i])
final=math.sqrt(rmse/14)
print(mre_list)
print(final)
