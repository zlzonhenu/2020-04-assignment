import cv2

#画像を読み込み　(3channelsで表示）
img = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/lunar.jpg", cv2.IMREAD_ANYCOLOR)

#高さと幅の定義
height = img.shape[0]
width = img.shape[1]

#画像をリサイズする

#縮小する(x0.3)場合
img2 = cv2.resize(img, (int(width*0.3), int(height*0.3)))

#拡大する(x1.5)場合
img3 = cv2.resize(img, (int(width*1.5),int(height*1.5)))

#画像を回転させる
#回転の中心の定義
center = (int(width/2), int(height/2))
#回転角を指定
angle = 60.0
#スケールを指定
scale = 1.0
#getRotationMatrix2D関数を使用
transform = cv2.getRotationMatrix2D(center, angle, scale)
#変換
img4 = cv2.warpAffine(img, transform, (width, height))


#編集後、画像を保存する
cv2.imwrite("C:/Users/cho hyeonwoo/Desktop/data/lunar2.jpg", img2)
cv2.imwrite("C:/Users/cho hyeonwoo/Desktop/data/lunar3.jpg", img3)
cv2.imwrite("C:/Users/cho hyeonwoo/Desktop/data/lunar4.jpg", img4)