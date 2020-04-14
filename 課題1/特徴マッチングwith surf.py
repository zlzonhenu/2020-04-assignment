import cv2

#画像を読み込み
img1 = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/real_dollar.png")
img2 = cv2.imread("C:/Users/cho hyeonwoo/Desktop/data/dollar.jpg")

#特徴抽出機の生成
detector = cv2.xfeatures2d.SURF_create()

#kpは特徴的な点の位置、desは特徴を表すベクトル
#desはkeypointの周辺の情報を表現した128次元ベクトル
kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)
#特徴点の比較機
bf = cv2.BFMatcher()

#それぞれの画像の特徴量記述子(128次元ベクトル)を渡すと、距離を計算する
#k=2とすると、des1のそれぞれの点に対する、最も近いdes2の点2つ選び、マッチングインスタンスを出力します
matches = bf.knnMatch(des1, des2, k=2)

#割合試験を適用
#最も近い点が2番目に近い点の距離の0.4倍の場合良い結果を出す
good = []
match_parameter = 0.5
for m, n in matches:
    if m.distance < match_parameter*n.distance:
        good.append([m])

#cv2.drawMatchesKnnは適合している点を結ぶ画像を生成する
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
cv2.imshow("a", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


