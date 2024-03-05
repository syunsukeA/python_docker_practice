import numpy as np
import pandas as pd
from plotter import plot_data
import os

def generate_data(num_samples):
    data = {
        'X': np.random.rand(num_samples),
        'Y': np.random.randn(num_samples)
    }
    return pd.DataFrame(data)

def main():
    num_samples = 1000
    data = generate_data(num_samples)

    # Save data to CSV (optional)
    save_path = os.getcwd()+"/data"
    os.makedirs(f'{save_path}', exist_ok=True)
    data.to_csv(f'{save_path}/generated_data.csv', index=False)

    # Plot data using the plotter module
    plot_data(data, save_path)

if __name__ == "__main__":
    main()
