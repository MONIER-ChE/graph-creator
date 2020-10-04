#!/usr/bin/env python

import matplotlib as mpl
import pandas as pd
import inquirer

from scipy import stats

# Create variable to hold anwsers
answers = {}

## Ask file to open
questions = [
  inquirer.Path('file_path',
                 message="Put the path of your file?",
                 path_type=inquirer.Path.FILE,
                ),
]
answers.update(inquirer.prompt(questions))


#file_path = '/home/yam/Downloads/TD3_etudiant.xls'


## Get excel file class
full_data = pd.ExcelFile(answers['file_path'])


## Ask if use selected sheet or not (all)
questions = [
    inquirer.List('spreadsheet',
                message="Choose the spreadsheet to use ",
                choices=full_data.sheet_names,
            ),
]

answers.update(inquirer.prompt(questions))



## Select data spreadsheet
data = pd.read_excel(answers['file_path'], sheet_name=answers['spreadsheet'])


print('This is your data :\n \n',data)


columns = data.columns.values.tolist()

## Independent samples t-test ################################################

## Ask grouping variable
questions = [
    inquirer.List('grouping_variable',
                message="Choose the grouping variable",
                choices=columns,
            ),
]

answers.update(inquirer.prompt(questions))
print('You choose :', answers['grouping_variable'])

# Remove first choice from list
columns.remove(answers['grouping_variable'])


## Create group from the anwser
grouped = data.groupby(answers['grouping_variable'])
#grouped.group to obtain list of groups
#print(grouped.get_group('Jeune'))## Obtain data of only one group

print(grouped)

'''
## Statistical test
for group in grouped:
    print(group)
'''

tStat, pValue = stats.ttest_ind([grouped], equal_var = False) #run independent sample T-Test
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat)) #print the P-Value and the T-Statistic

## Levene Test for Equal Variances check random population choice in grouping before do statistics
#stat, p = stats.levene(grouped) 




'''
Do the same for all the variables selected with for loop
'''












## Ask for dependent variables
questions = [
  inquirer.Checkbox('dependent_variables',
                    message="Choose the dependent variables (press space to select one or more)",
                    choices=columns,
                    ),
]

answers.update(inquirer.prompt(questions))
print('You choose :', answers['dependent_variables'])




################################################
## Ask for descriptive statistics
descriptive = describe(v) # where v is the data columns

print(answers)




'''
questions = [
    inquirer.List('graph_type',
                message="Chose the spreadshit  ",
                choices=['bar plot', 'line'],
            ),
]
answers = inquirer.prompt(questions)



## Dependent samples t-test ################################################

## ANOVA ################################################





## Ask wich column have to use
choice = input("Type 1 for bar plot:")

questions = [
    inquirer.List('graph_type',
                message="Which type of graph you want ? ",
                choices=['bar plot', 'line'],
            ),
]
answers = inquirer.prompt(questions)
print(answers)





## Ask for bar plot
confirm = {
    inquirer.Confirm('error-bar',
                     message="Do you want to plot error bars ?" ,
                     default=True),
}
confirmation = inquirer.prompt(confirm)
print (confirmation['error-bar'])






print(data)
'''