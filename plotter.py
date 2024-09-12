import os
import pandas as pd
import matplotlib.pyplot as plt
import requests


class Plotter:
    def __init__(self, plot_dir='plots'):
        self.plot_dir = plot_dir
        if not os.path.exists(plot_dir):
            os.makedirs(plot_dir)

    def draw_plots(self, json_url):
        response = requests.get(json_url)
        response.raise_for_status()  # Check if the request was successful
        df = pd.read_json(response.text)

        columns = df.columns.tolist()
        paths = []

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                x_col = columns[i]
                y_col = columns[j]
                plt.figure(figsize=(10, 6))
                plt.scatter(df[x_col], df[y_col], alpha=0.7)
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.title(f'{x_col} vs {y_col}')
                plot_path = os.path.join(self.plot_dir, f'{x_col}_vs_{y_col}.png')
                plt.savefig(plot_path)
                plt.close()
                paths.append(plot_path)

        return paths
