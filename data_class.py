
'''
File for holding data class variables
'''
## paquages
import matplotlib.pyplot as plt
import pandas as pd
import inquirer

from scipy import stats


class graph:
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


    
    '''
    def plot(self):
        print("Hello my name is " + self.name)
    '''



## Run 
print("Hello don't forget to put all data in columns")
p1 = graph()


questions = [
    
    ## Ask file to open
    inquirer.Path('file_path',
                    message="Put the path of your file?",
                    path_type=inquirer.Path.FILE,
                    )]


## Launch questions and hold anwsers
anwsers = inquirer.prompt(questions)

p1.file = anwsers['file_path']
## TO REMOVE
p1.file = '/home/yam/Downloads/TD3_etudiant.xls'



## Get excel file class
full_data = pd.ExcelFile(p1.file)


## Ask if use selected sheet
questions = [
    # Ask for sheet to use
    inquirer.List('sheet',
                message="Choose the sheet to use ",
                choices=full_data.sheet_names,
            )
]


## Launch questions and hold anwsers
anwsers = inquirer.prompt(questions)

p1.sheet = anwsers['sheet']





## Select data sheet and create df
p1.df = pd.read_excel(p1.file, sheet_name=p1.sheet)
print('\nThis is your data : \n \n',p1.df)


## Ask type of test
questions = [
    inquirer.List('test_type',
                message="Choose the statistic test you want to use",
                choices=['Idependant T-Test',
                        'Dependant T-Test',
                        'ANOVA',
                        'Reapeated mesures ANOVA',
                        'No one'],
            )
]


## Launch questions and hold anwsers
p1.test_type = inquirer.prompt(questions)
p1.test_type = p1.test_type['test_type']


## Statistical test choice
if p1.test_type == 'Idependant T-Test':
    print('oui')

elif p1.test_type == 'Dependant T-Test':
    print('oui')

elif p1.test_type == 'ANOVA':
    print('oui')

elif p1.test_type == 'Reapeated mesures ANOVA':
    print('oui')

    ## Focus on this part for now
    '''
    class method for each statistic test ? 
    class method for plotting data (grouping or solo vars etc)

    class method for drawing significative bracket 1 to 1or 2 to 2 or 1 to 2 etc

    gitignore to removve some file of github git push ect

    '''
else:
    print('choose how to plot var and var ')


#get the list of variables
columns_name = p1.df.columns.values.tolist()


## Ask for variables
questions = [
inquirer.Checkbox('variables',
                    message="Choose the variables (press space to select one or more)",
                    choices=columns_name,
                    ),
]

## Launch questions and hold anwsers
p1.variables = inquirer.prompt(questions)
p1.variables = p1.variables['variables']

print(p1.variables)
print(columns_name)


## Remove item from list choice
for item in p1.variables:
    print(item)
    columns_name.remove(item)


## Ask grouping variable
questions = [
    inquirer.Checkbox('grouping_variable',
                message="If you have grouping variables, please select one or more",
                choices=columns_name,
            ),
]

## Launch questions and hold anwsers
p1.grouping_variables = inquirer.prompt(questions)
p1.grouping_variables = p1.grouping_variables['grouping_variable']


## If there are no grouping variables, basic plot
if not p1.grouping_variables:
    print('p')










'''
## if 'grouping_variables'not empty, ...
answers.update(inquirer.prompt(questions))

# Remove first choice from list



## Create group from the anwser
grouped = data.groupby(answers['grouping_variable'])
#grouped.group to obtain list of groups
    #print(grouped.get_grou



'''


















# Do you want an descriptive plot ? 
'''
EXEMPLE OF MULTIPLE QUESTIONS
## Ask if use selected sheet or not (all)
questions = [

    
    ## Ask file to open
    inquirer.Path('file_path',
                    message="Put the path of your file?",
                    path_type=inquirer.Path.FILE,
                    ),
    

    # Ask for sheet to use
    inquirer.List('sheet',
                message="Choose the sheet to use ",
                choices=full_data.sheet_names,
            ),
]
'''