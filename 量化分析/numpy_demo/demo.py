# coding:utf-8

"""
实例分析：假设股票收益率服从正态分布，使用numpy产生正态分布随机数，模拟股票收益率，并采用正态分布策略进行交易。

假设有2000只股票，一年股市共250个交易日。
一年365天-全民法定节假日=365-每周双休日*52-节日放假日  （国庆3天+春节3天+劳动节、元旦、清明、端午、中秋共11天）
=365-104-11=250日,产生2000x500的数组。
"""
import numpy as np

stocks = 2000   # 2000支股票
days = 500  # 两年大约500个交易日

# 生成服从正态分布：均值期望＝0，标准差＝1的序列
# 正态生成2000行500列的二维数组
stock_day = np.random.standard_normal((stocks, days))   # 只需要一个参数即可
# stock_day = np.random.normal(1.5, 3, (3, 4))  #正态生成3行4列的二维数组,均值为1.5，标准差为3

# print(stock_day)
print(stock_day.shape)   # 打印数据组结构

# 打印出前五只股票，头五个交易日的涨跌幅情况
print(stock_day[0:5, :5])

"""
正态分布买入策略:
"""
keep_days = 250     # 保留后250天的随机数据作为策略验证数据
stock_day_train = stock_day[:, 0:days - keep_days]       # 统计前250天, 切片切出0-250day，days = 500

# 打印出前250天跌幅最大的三支，总跌幅通过np.sum计算，np.sort对结果排序
print(np.sort(np.sum(stock_day_train, axis=1))[:3])     # axis=1代表行,axis=0代表列

# 使用np.argsort针对股票跌幅进行排序，返回序号，即符合买入条件的股票序号
stock_lower = np.argsort(np.sum(stock_day_train, axis=1))[:3]
print(stock_lower)     # 输出符合买入条件的股票序号


"""
封装函数plot_buy_lower()可视化选中的前3只跌幅最大的股票前450走势以及从第454日买入后的走势
"""
import matplotlib.pyplot as plt  # 引入画图库


def buy_lower(stock):
    # 设置一个一行两列的可视化图表
    _, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 5))

    # 绘制前250天的股票走势图，np.cumsum():序列连续求和
    axs[0].plot(np.arange(0, days - keep_days), stock_day_train[stock].cumsum())

    # 从第250天开始到500天的股票走势
    buy = stock_day[stock][days - keep_days:days].cumsum()

    # 绘制从第250天到500天中股票的走势图
    axs[1].plot(np.arange(days - keep_days, days), buy)
    plt.show()

    # 返回从第450天开始到第500天计算盈亏的盈亏序列的最后一个值
    return buy[-1]


# 假设等权重地买入3只股票
profit = 0  # 盈亏比例
# 遍历跌幅最大的3只股票序列序号序列
for stock in stock_lower:
    # profit即三只股票从第250天买入开始计算，直到最后一天的盈亏比例
    profit += buy_lower(stock)
    print("买入第{}只股票，从第250个交易日开始持有盈亏：{:.2f}%".format(stock,profit))