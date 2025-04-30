import matplotlib.pyplot as plt
import pandas as pd

def plot_bar():
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    plt.bar(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()

def plot_scatter():
    df = pd.read_csv('Data.csv')
    plt.pie(df['Value'], labels=df['Products'])
    plt.show()

def plot_scatter_xls():
    df = pd.read_csv('Data.xlsx')
    x = df['X']
    y = df['Y']
    plt.scatter(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()

#plot_scatter_xls()
plot_scatter()
#plot_bar()
