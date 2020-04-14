import cv2
import numpy as np

#画像を読み込み　(3channelsで表示）
img = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/lunar.jpg", cv2.IMREAD_ANYCOLOR)

#画像に文字を追加する
img2 = cv2.putText(img, "Moon", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0))

#画像を保存する
cv2.imwrite("C:/Users/cho hyeonwoo/Desktop/data/lunar6.jpg", img2)

#文字が追加された画像を読み込み
imgwithtext = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/lunar6.jpg")

#画像の表示
cv2.imshow("Moonwithtext", imgwithtext)
cv2.waitKey(0)
cv2.destroyAllWindows()

#元のイメージと一致するか確認
print(np.array_equal(img, imgwithtext))

#二つの画像に対する差分の絶対値を出す
img_difference = imgwithtext.astype(int)-img.astype(int)
img_diff_abs = np.abs(img_difference)
img_diff_abs_norm = img_diff_abs / img_diff_abs.max() * 3

#差分画像の表示
cv2.imshow("Moondiff", img_diff_abs_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()
