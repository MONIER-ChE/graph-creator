#!/usr/bin/env python


## local paquages
import graph_creator
import run_stats


## paquages
import matplotlib.pyplot as plt
import pandas as pd
import inquirer

from scipy import stats



## Create dict to hold anwsers
answers = {}


# remove it later
answers.update(file_path = '/home/yam/Downloads/TD3_etudiant.xls')



'''
## Ask file to open
questions = [
  inquirer.Path('file_path',
                 message="Put the path of your file?",
                 path_type=inquirer.Path.FILE,
                ),
]
answers.update(inquirer.prompt(questions))
'''



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


## Select data spreadsheet and create df
data = pd.read_excel(answers['file_path'], sheet_name=answers['spreadsheet'])
print('This is your data :\n \n',data)


#get the list of variables
columns = data.columns.values.tolist()


## Ask type of test
questions = [
    inquirer.List('test_type',
                message="Choose the statistic test you want to use",
                choices=['Idependant T-Test', 'Dependant T-Test', 'No one'],
            ),
]

answers.update(inquirer.prompt(questions))
#print('You choose :', answers['test_type'])


## Option for just create braket (add grouping or not variables)
if answers['test_type'] == 'No one':
    ## Ask type of test
    questions = [
        inquirer.Checkbox('correlation_bracket',
                    message="Choose a pair of variables you want to link",
                    choices=columns
                ),
    ] 


    answers.update(inquirer.prompt(questions))

    ## Running steps using test choice
elif answers['test_type'] == 'Idependant T-Test':


    ## Ask grouping variable
    questions = [
        inquirer.List('grouping_variable',
                    message="Choose the grouping variable",
                    choices=columns,
                ),
    ]

    answers.update(inquirer.prompt(questions))

    # Remove first choice from list
    columns.remove(answers['grouping_variable'])


    ## Create group from the anwser
    grouped = data.groupby(answers['grouping_variable'])
    #grouped.group to obtain list of groups
    #print(grouped.get_group('Jeune'))## Obtain data of only one group



    ## Ask type of relation (≠ or > or <)
    questions = [
        inquirer.List('relation',
                    message="Choose the relation",
                    choices=['A ≠ B', 'A > B', 'B < A'],
                ),
    ]

    answers.update(inquirer.prompt(questions))




    ## Ask wich one is group A and wich one is group B 
    questions = [
        inquirer.List('a_group',
                    message="Choose the groupe A",
                    choices=grouped.groups.keys(),
                ),
    ]

    answers.update(inquirer.prompt(questions))




    ## Ask for dependent variables
    questions = [
    inquirer.Checkbox('dependent_variables',
                        message="Choose the dependent variables (press space to select one or more)",
                        choices=columns,
                        ),
    ]

    answers.update(inquirer.prompt(questions))


    ## Create b group label from the A choose
    b_group = list(grouped.groups.keys())
    b_group.remove(answers['a_group'])

    ## Get separate data from the result
    a_group = grouped.get_group(answers['a_group'])
    b_group = grouped.get_group(b_group[0])


    ## T- Test
    test_results = {}

    test_results['a_mean'] = []
    test_results['b_mean'] = []
    test_results['a_std'] = []
    test_results['b_std'] = []

    for variable in answers['dependent_variables']:
        
        # T-Test
        test_results[variable] = stats.ttest_ind(a_group[variable], b_group[variable])

        ## mean and std hand
        test_results['a_mean'].append(a_group[variable].mean())
        test_results['b_mean'].append(b_group[variable].mean())
        test_results['a_std'].append(a_group[variable].std())
        test_results['b_std'].append(b_group[variable].std())


    graph_creator.grouped_bar_plot(test_results['a_mean'], 
                                    test_results['b_mean'], 
                                    test_results['a_std'], 
                                    test_results['b_std'], 
                                    list(grouped.groups), 
                                    list(answers['dependent_variables']),
                                    grouped.describe())
    #
    #graph_creator.grouped_bar_plot(test_results['mean'], test_results['std'], a_group.columns.values.tolist())




    ## Levene Test for Equal Variances check random population choice in grouping before do statistics
    #stat, p = stats.levene(grouped) 




    ################################################
    ## Ask for descriptive statistics
    # Do you want an descriptive tables ? 
    # if yes, wich data you want ? (mean, std, quartiles, etc)

    ## Directly create descriptive stats image
    describe = grouped.describe()















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