
'''
File for holding data class variables
'''
## paquages
import matplotlib.pyplot as plt
import pandas as pd


from scipy import stats

## other script
import graph_creator


class data:
  def __init__(self, file_path = '',
                sheet = '',
                test_type = None,
                df = None,
                grouping_variables = [],
                variables = []):
    
    self.file = file_path
    self.sheet = sheet

    self.df = df
    self.grouping_variables = grouping_variables
    self.variables = variables
    
    self.test_type = test_type



