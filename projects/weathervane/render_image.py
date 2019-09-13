import matplotlib.pyplot as plt
# import datetime
# import numpy as np
def render_static_img():
    # x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(12)])
    # y = np.random.randint(100, size=x.shape)
    x = [10,2,3,4,5]
    y = [2,4,6,8,10]
    # print('Hi there')
    plt.plot(x,y)
    plt.savefig('./static/img.png')
    plt.close()
    return 
# render_static_img()