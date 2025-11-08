import matplotlib.pyplot as plt

def plot_relationship(data, x_col, y_col):
    plt.figure(figsize=(8,5))
    plt.scatter(data[x_col], data[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{x_col} vs {y_col}')
    plt.show()
