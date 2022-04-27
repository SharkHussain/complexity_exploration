import numpy as np
import pandas as pd
from data_layer import data_ingestion


class complexityCalculator:
    complexity = ""
    data = ""
    result = ""

    def __init__(self):
        dr = data_ingestion.dataReader()
        data = dr.file
        self.data = data

    def __calculate_log_complexity(self):
        data = self.data
        complexity = np.log(data['SetupMin']+1)+np.log(data['SetupMax']-data['SetupMin']+1) + \
            np.log(data['SetupMax']-data['SetupMin']+1) + \
            np.log(data['Syrup #Components']+1)
        self.complexity = complexity
        return complexity

    def __calculate_changeover_complexity(self):
        data = self.data

    def __merge_with_data(self):
        data = self.data
        complexity = self.complexity
        result = pd.concat([data, complexity], axis=1)
        self.result = result

    def get_complexity(self):
        self.__calculate_log_complexity()
        self.__merge_with_data()
        return self.result




