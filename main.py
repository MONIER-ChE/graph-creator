
## external paquages
import inquirer
import pandas as pd
import matplotlib.pyplot as plt

## internal paquages
import data_class
import graph_creator



## Run 
print("Hello don't forget to put all data in columns")
p1 = data_class.data()


questions = [
    
    ## Ask file to open
    inquirer.Path('file_path',
                    message="Put the path of your file?",
                    path_type=inquirer.Path.FILE,
                    )]


## Launch questions and hold answers
answers = inquirer.prompt(questions)

p1.file = answers['file_path']
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


## Launch questions and hold answers
answers = inquirer.prompt(questions)

p1.sheet = answers['sheet']





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


## Launch questions and hold answers
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


## Ask for variables (min 1)
while not p1.variables :
    questions = [
    inquirer.Checkbox('variables',
                        message="Choose the variables (press space to select one or more)",
                        choices=columns_name,
                        ),
    ]

    ## Launch questions and hold answers
    p1.variables = inquirer.prompt(questions)
    p1.variables = p1.variables['variables']


## Remove item from list choice
for item in p1.variables:
    columns_name.remove(item)


## Ask grouping variable
questions = [
    inquirer.Checkbox('grouping_variable',
                message="If you have grouping variables, please select one or more",
                choices=columns_name,
            ),
]

## Launch questions and hold answers
p1.grouping_variables = inquirer.prompt(questions)
p1.grouping_variables = p1.grouping_variables['grouping_variable']


## remove usless columns from df
for var in p1.df.columns:
    if var not in p1.variables + p1.grouping_variables:
        del p1.df[var]


## If there are no grouping variables, basic plot
if not p1.grouping_variables:
    
    plot = graph_creator.plot()
    plot.grouped = False

    ## Else create grouping df
else:
    
    #create custom column from all grouping vars
    if len(p1.grouping_variables) > 1:
        
        #create custom column from all grouping vars
        p1.df['group'] = p1.df[p1.grouping_variables].agg('-'.join, axis=1)

        ## remove usless columns from df
        for var in p1.df.columns:
            if var not in p1.variables and var != 'group':
                del p1.df[var]
    
        p1.df = p1.df.groupby(p1.df['group'])
        #print(p1.df.describe
    
    #group data from the column
    else: 
        p1.df = p1.df.groupby(p1.grouping_variables)


    plot = graph_creator.plot()

## assign df
plot.df = p1.df


## create bar plot using grouping parameter
plot.bar_plot()


## ask if he want to draw stars (waiting the automatisation process)
questions = [
    inquirer.Confirm('stars',
                  message='Do you want to draw statistical bracket between bars ?')
]

answers = inquirer.prompt(questions)
while answers['stars'] == True:

    ##create dict for holding answers for further link
    link = {}

    if plot.grouped == True:

        
        ## Use step by step awnser to use result in text like 'in groupe "Age", wich variables
        ## While loop of 1 associate to 2 or 1+ to 2 etc while the user don't check FINISH
        questions = [
            inquirer.List('group_link_A',
                        message="Please select The A group",
                        choices=p1.df.groups,
                    ),
            inquirer.List('stars_link_A',
                        message="Please select one or more A values to link to B",
                        choices=p1.variables,
                    ),
            inquirer.List('group_link_B',
                        message="Please select the B group",
                        choices=p1.df.groups,
                    ),
            inquirer.List('stars_link_B',
                        message="Please select one or more B values to get linked",
                        choices=p1.variables,
                    ),
        ]

        answers = inquirer.prompt(questions)
        print(answers)
        plot.grouped_statistical_bracket(answers['group_link_A'], answers['stars_link_A'], answers['group_link_B'], answers['stars_link_B'])


    else:


                ## While loop of 1 associate to 2 or 1+ to 2 etc while the user don't check FINISH
        questions = [

            inquirer.List('stars_link_A',
                        message="Please select one or more A values to link to B",
                        choices=p1.variables,
                    ),

            inquirer.List('stars_link_B',
                        message="Please select one or more B values to get linked",
                        choices=p1.variables,
                    ),
        ]

        answers = inquirer.prompt(questions)


        plot.statistical_bracket(answers['stars_link_A'], answers['stars_link_B'])

    ## ask if he want to draw stars (waiting the automatisation process)
    questions = [
    inquirer.Confirm('stars',
                  message='Do you want to draw statistical bracket between bars ?')
    ]
    
    answers = inquirer.prompt(questions)

plt.tight_layout()
plt.show() 


'''
# adjust staring point and length for matching with 2 bar plot

#plt.ylim(0, 200) # def lim depending of size of bar
plt.tight_layout()
plt.show() 
'''







## create stats test part

## use function to draw statistical bracket using dict (key 1 (Age)) link to 1 or more vars or 2 list ? idk for now$
# like choose one ore more var to link (1link) ? 
# choose the var linked 
# ex : age + force link taille + poid (large hoizontal line)






















'''
# no grouping var = index
#print(describe.loc['mean'])


# x group var (index = Jeune/vieux or jeune-H, Jeune, F, Vieux-F,...)
print(describe.index)
print(describe.columns) # to use


print(describe['Taille']['mean'])
for var, test in describe:
    print(var, test)
'''



## create descriptive table with LaTeX | render if from calling pdflatex from console or find pther way
'''
with open('mytable.tex', 'w') as tf:
     tf.write(df.to_latex())
     ## + generate pdf or vector image
'''



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