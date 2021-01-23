import matplotlib.pyplot as plt
import numpy as np

def loadData(flieName):
    '''
    从.txt文件中读取数据
    可选择读取所有数据也可选择读取选定行数据
    '''
    lnum = 0
    lot = []  # 创建空表存放lot数据
    lat = []  # 创建空表存放lat数据
    sub = []  # 创建空表存放sub数据
    with open(flieName, 'r') as f:  # 以只读形式打开某.txt文件
        for line in f:
            lnum += 1
            if (lnum >= 1):  # 从第1行开始添加数据
                line = line.strip('\n')  # 去掉换行符
                line = line.split('\t')  # 分割掉两列数据之间的制表符
                lot.append(line[0])
                lat.append(line[1])
                sub.append(line[2])
    # NOTE：此时所得到的x列表中的数据类型是str类型，因此需要进行转换，转换为float类型
    lot = np.array(lot)
    lot = lot.astype(np.float).tolist()

    lat = np.array(lat)
    lat = lat.astype(np.float).tolist()

    sub = np.array(sub)
    sub = sub.astype(np.float).tolist()

    return (lot,lat,sub)

if __name__ == "__main__":
    lot,lat,sub=loadData('data_sub')
    plt.scatter(lot, lat, c=sub)
    plt.title('result')
    plt.show()
