import pandas as pd


def load_data():
    data = pd.read_csv("dataset_24_mushroom.csv")
    print(data.head())


def main():
    load_data()

main()