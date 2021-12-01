# coding: utf-8
"""
散点图（Scatter plot）

 散点图是用于研究两个变量之间关系的经典的和基本的图表。
 如果数据中有多个组，则可能需要以不同颜色可视化每个组。 
 在 matplotlib 中，您可以使用 plt.scatter() 方便地执行此操作。

 matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None,
  vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

  x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。
  s：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。
  c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
  marker：点的样式，默认小圆圈 'o'。
  cmap：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap
  norm：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。
  vmin，vmax：：亮度设置，在 norm 参数存在时会忽略。
  alpha：：透明度设置，0-1 之间，默认 None，即不透明。
  linewidths：：标记点的长度。
  edgecolors：：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。
  plotnonfinite：：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。
  **kwargs：：其他参数。
"""

from common.index import *

# 准备数据
midwest = pd.read_csv("./common/midwest_filter.csv")
categories = np.unique(midwest['category'])     # numpy.ndarray
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]     # list(rgba)

# 设置图形大小
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

for i, category in enumerate(categories):
    # 使用scatter方法绘制散点图，x轴描述为area，y轴描述为poptotal
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category == category, :],
                s=20, cmap=colors[i], label=str(category))

# 设置x,y轴的相关属性
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000), xlabel='Area', ylabel='Population')


# 调整x,y轴的刻度
plt.xticks(fontsize=12)     # 设置x轴的刻标字体大小
plt.yticks(fontsize=12)     # 设置y轴的刻标字体大小

# 添加描述信息
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)     # 设置标题内容及大小
# plt.xlabel("X-demo", fontsize=20)   # fontname='SimHei'
# plt.ylabel("Y-demo", fontsize=20)   # fontname='SimHei',

# 添加图例
plt.legend(fontsize=12)     # loc="upper left",

# 展示
plt.show()
