import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,2*np.pi,9) #4/2=2 2个完整的正弦波波形   4*8代表一共生成的点数量
y=1.5*np.sin(x)  #调整43这个值可以调整波峰值
#y1=y.astype(int)   #把y值转换成整数
z=np.linspace(0,0.001,9)
for i in range(0,9):
    print("%f "%y[i],"%f "%z[i])
plt.plot(x,y,'bp--') #绘制成图表
plt.show()

#先把生成两个正弦波数据存入txt文件
np.savetxt("data.txt",(y),delimiter=',',fmt="%d",newline=',')

# #读取正弦波数据，共包含两个正弦波，32个点
# fileH=open("data.txt")
# fileData=fileH.read()
# fileH.close()
#
# #以写方式打开文件，以之前的两个正弦波的数据做拷贝
# fileH=open("data-500.txt",'w')
# for i in range(2000):
#     fileH.write("\n")
#     fileH.writelines(fileData)
# fileH.close()