import cv2

#画像を読み込み　(3channelsで表示)
img = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/Duck.jpg", cv2.IMREAD_ANYCOLOR)

#二値化を適用するために、グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#閾値の設定
threshold = 100

#二値化(閾値100を超えた画素を255にする)
ret, dst = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

#画像を保存する
cv2.imwrite("C:/Users/cho hyeonwoo/Desktop/data/Duck2.jpg", dst)