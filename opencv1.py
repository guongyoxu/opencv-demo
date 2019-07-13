import cv2 as  cv
import numpy as np
"""
你将要学习如下函数：
cv.imread()  arg：图像地址
cv.imshow()  arg ：winname,mat(cv.imread返回值)
cv.imwrite() 
"""
def image():
    img=cv.imread("C:/Users/Administrator/Desktop/lhb.jpg")
    cv.imshow("dog",img)
    print(img.shape)
    print(img.size)
    print("图像像素类型",img.dtype)
    print("图像类型",type(img))
    pixel_data = np.array(img)  # 将图片转换成数组
    print("像素大小：", pixel_data)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imwrite("C:/Users/Administrator/Desktop/test1.jpg",gray)
    print("gray",type(gray))
    cv.imwrite("C:/Users/Administrator/Desktop/test1.jpg", gray)
    cv.waitKey(0)  # 等待按键响应（x ms）如果x==0 无限等待直到按键响应

def video():
    pass








image()
