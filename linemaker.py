import matplotlib.pyplot as plt

# フォントの設定
plt.rcParams['font.family'] = 'meiryo'  # 例: IPAGothicは日本語フォントの一つです

# データポイントの座標を定義
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# プロット
plt.plot(x, y, label='線の例')

# プロットの装飾
plt.xlabel('X軸')
plt.ylabel('Y軸')
plt.title('線の描画サンプル')
plt.legend()

# グラフを表示
plt.show()
