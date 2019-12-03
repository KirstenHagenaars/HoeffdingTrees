import pandas as pd
import os


def load_data():
    data = pd.read_csv("dataset_24_mushrooms.csv")
    print(data.head())


def main():
    #load_data()
    print("a")
    #print(os.getcwd())
