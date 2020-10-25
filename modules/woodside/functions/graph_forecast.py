import matplotlib.pyplot as plt
import numpy as np


def graph_forecast(woodside_data, woodside_forecast):

    x1 = np.arange(55)
    y1 = woodside_data[-55:]

    plt.plot(x1, y1, label="Weeks Past")
    plt.legend()

    x2 = [54, 55, 56, 57, 58]
    y2 = np.concatenate((woodside_data[-1:], woodside_forecast))

    plt.plot(x2, y2, label="Forecast")
    plt.legend()

    plt.savefig('./images/brent_forecast.png')
    plt.show()