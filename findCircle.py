import cv2 as cv
import numpy as np
'''
:param
image为输入图像，要求是灰度图像

circles为输出圆向量，每个向量包括三个浮点型的元素——圆心横坐标，圆心纵坐标和圆半径

method为使用霍夫变换圆检测的算法，Opencv2.4.9只实现了2-1霍夫变换，它的参数是CV_HOUGH_GRADIENT

dp为第一阶段所使用的霍夫空间的分辨率，dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推

minDist为圆心之间的最小距离，如果检测到的两个圆心之间距离小于该值，则认为它们是同一个圆心

param1为边缘检测时使用Canny算子的高阈值

param2为步骤1.5和步骤2.5中所共有的阈值

minRadius和maxRadius为所检测到的圆半径的最小值和最大值

'''

src = cv.imread('./circle.jpg', cv.IMREAD_COLOR)
img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(img, 5)
cimg = src.copy()
font = cv.FONT_HERSHEY_SIMPLEX
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1,20, np.array([]),100,12, 10, 20)
if circles is not None:
    a, b, c = circles.shape
    print(str(circles))
    for i in range(b):
        cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 2, cv.LINE_AA)
        cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 2, cv.LINE_AA)  # draw center of circle
        x_1= str(circles[0][i][0])
        y_1= str(circles[0][i][1])
        c = x_1+y_1
        d= str(i)
        cv.putText(cimg, d, (circles[0][i][0], circles[0][i][1]), font, 0.5, (255, 255, 255), 1)
    cv.imshow("detected circles", cimg)

    cv.imwrite('./result.jpg', cimg)
cv.waitKey(0)
