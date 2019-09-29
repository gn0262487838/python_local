# -*- UTF-8 -*- #
import cv2
import numpy as np

### start ###

# load
v = cv2.VideoCapture("homework3.mp4")

# vars
result, move = v.read()
last_move = move.copy()

# for i in range(10000):
#     result, move = v.read()
#     cv2.imshow("haha", move)
#     cv2.waitKey(1)

# 物件定位
while result:

        # 分別轉灰階
        move_gray = cv2.cvtColor(move,cv2.COLOR_BGR2GRAY)
        last_move_gray = cv2.cvtColor(last_move,cv2.COLOR_BGR2GRAY)
        
        # 高斯模糊化
        move_gray_gau = cv2.GaussianBlur(move_gray,(3,3),2)
        last_move_gray_gau = cv2.GaussianBlur(last_move_gray,(3,3),2)

        # 後前模糊影像相減
        move_diff = cv2.absdiff(move_gray_gau,last_move_gray_gau)

        # 極值化
        value, move_diff_bin = cv2.threshold(move_diff,17,255,cv2.THRESH_BINARY)
        
        # 擴張
        move_diff_bin_r = cv2.dilate(move_diff_bin, np.ones((3,3)),iterations=5)
        # 侵蝕
        move_diff_bin_r= cv2.erode(move_diff_bin_r,np.ones((3,3)),iterations=5)
        # 擴張
        move_diff_bin_r_i = cv2.dilate(move_diff_bin_r, np.ones((3,3)),iterations=3)
        
        # 尋找輪廓點
        point , data= cv2.findContours(move_diff_bin,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for i in point:
            # 篩選掉不要的小區塊
            if cv2.contourArea(i) < 100 * 100:
                continue
            elif cv2.contourArea(i) > 640 * 360 // 8:
                continue
            else:
                # 取min矩形座標
                x, y, w, h = cv2.boundingRect(i)
                # 在原圖上直接繪製矩形，不用在指派到m上。
                cv2.rectangle(move,(x,y),(x+w,y+h),(0,0,255),2)
                # show
                cv2.imshow("Show time", move)

                # delayTime
                cv2.waitKey(1000//33)
        
        last_move = move
        result, move = v.read()

cv2.destroyAllWindows()

### over ###