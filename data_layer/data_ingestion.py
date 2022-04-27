import pandas as pd

#skus = pd.read_csv("data/global_sku.csv")
#recipes = pd.read_csv("data/recipes.csv")
#volume = pd.read_csv("data/productionVolume.csv")


class dataReader:
    file_name = "data/productionVolume.csv"
    file = ''

    def get_data(self):
        file_name = self.file_name
        file = pd.read_csv(file_name)
        self.file = file

    def subset_data(self):
        file = self.file
        file = file[["Material", "Syrup #Components", "SetupMin", "SetupMax"]]
        file = file.dropna()
        self.file = file

    def __init__(self):
        self.get_data()
        self.subset_data()








