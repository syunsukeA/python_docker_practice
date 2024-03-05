import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_data(data, save_path):
    # Plotting
    plt.scatter(data['X'], data['Y'])
    plt.title('Scatter Plot of Generated Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig(f"{save_path}/main01.png")
    plt.show()
