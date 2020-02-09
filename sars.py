#! /usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib import rcParams
#from matplotlib.font_manager import FontProperties

#plt.rcParams['font.family']='simhei'
#plt.rcParams['axes.unicode_minus']=False
font = {'family':'Microsoft YaHei',
'weight':'bold',
'size':'16'
}
plt.rc('font',**font)
plt.rc('axes',unicode_minus = False)
province_pinyin = np.array(['GuangDong',
                     'JiangSu',
                     'ShanDong',
                     'ZheJiang',
                     'HeNan',
                     'SiChuan',
                     'Hubei',
                     'Fujian',
                     'HuNan',
                     'ShangHai',
                     'AnHui',
                     'BeiJing',
                     'HeBei',
                     'ShanXi',
                     'LiaoNing',
                     'Jiangxi',
                     'ChongQing',
                     'YunNan',
                     'GuangXi',
                     'NeiMenggu',
                     'ShanXi',
                     'GuiZhou',
                     'TianJin',
                     'HeiLongJiang',
                     'XinJiang',
                     'JiLin',
                     'GanSu',
                     'HaiNan',
                     'NingXia',
                     'QingHai',
                     'XiZang'])
province_hanzi = np.array([
'广东',
'江苏',
'山东',
'浙江',
'河南',
'四川',
'湖北',
'福建',
'湖南',
'上海',
'安徽',
'北京',
'河北',
'陕西',
'辽宁',
'江西',
'重庆',
'云南',
'广西',
'内蒙古',
'山西',
'贵州',
'天津',
'黑龙江',
'新疆',
'吉林',
'甘肃',
'海南',
'宁夏',
'青海',
'西藏'
])
DISTANCE = np.array([
995.6,
700,
862.19,
773,
510,
1148,
0,
909,
344,
836,
380,
1225,
896,
740.7,
1864,
355,
867,
1558,
1196,
1381,
1044,
1328,
1151,
2408,
3268,
2140,
1359,
1508,
1424,
1579,
3485
])
GDP = np.array([107671.07,
                 99631.52,
                 71067.5,
                 62352,
                 54259.2,
                 46615.82,
                 45828.31,
                 42395,
                 39752.12,
                 38155.12,
                 37114,
                 35371.3,
                 35104.5,
                 25793.17,
                 24909.5,
                 24757.5,
                 23605.77,
                 23223.75,
                 21237.14,
                 17212.5,
                 17026.68,
                 16769.34,
                 14104.28,
                 13612.7,
                 13597.11,
                 11726.8,
                  8718.3,
                  5308.94,
                  3748.48,
                  2965.95,
                  1697.82])
sars = np.array([632,
                 236,
                 230,
                 661,
                 493,
                 231,
                 0,
                 159,
                 463,
                 182,
                 340,
                 191,
                 104,
                 116,
                 69,
                 333,
                 275,
                 105,
                 111,
                 27,
                 56,
                 38,
                 48,
                 95,
                 21,
                 23,
                 40,
                 64,
                 28,
                 11,
                 1,             
])
#average_dist = 500
fig1 = plt.figure(1,dpi = 120)
plt.plot(province_hanzi,GDP/100,color = 'blue',label='GDP')
plt.plot(province_hanzi,sars,color = 'red',label='SARs')
plt.plot(province_hanzi,DISTANCE/3,color = 'green',label='DISTANCE')
#plt.plot(province_hanzi,average_dist/3,color = 'brown',label = '500')
plt.xlabel('省份',fontsize=18)
my_x_ticks = np.arange(0,31,1)
plt.xticks(my_x_ticks,province_hanzi,fontsize=10)
#font = FontProperties(fname=r'/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf')
#plt.legend(prop=font)
#plt.figure(dpi = 200)
plt.legend()
plt.show()
