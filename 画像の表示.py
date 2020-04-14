import cv2

#画像を読み込み　(3channelsで表示）
img = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/lunar.jpg", cv2.IMREAD_ANYCOLOR)

#画像の表示
cv2.imshow("Moon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

