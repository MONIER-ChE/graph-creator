import matplotlib.pyplot as plt
import numpy as np




## Plot style
plt.style.use('bmh') ## ggplot

## Global matplotlib param Edit the font, font size, and axes width
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['lines.linewidth'] = 1.5

## Legend
plt.rcParams['legend.facecolor'] = '#FFFAFA'

## Grid

plt.rcParams['grid.linestyle'] = '--' # linestyle


## to define
plt.rcParams['axes.labelsize']= 8
plt.rcParams['legend.fontsize']= 10
plt.rcParams['xtick.labelsize']= 10
plt.rcParams['ytick.labelsize']= 10
#plt.rcParams['text.usetex']= False

plt.rcParams['figure.figsize'] = 5, 10



'''
step

for bar in chart (working for 1, 2, 3 groupin plot (pre/post training | base, pre, post))
'''


## class for hold graph
class plot:

    def __init__(self, df):

        self.df = df


    def bar_plot(self):
        
        ## play xith descibe df because it's more ez and load less ressources
        test = self.df.describe()
        print(test)
        print(test.loc['mean'])
        
        ax = self.df.plot.bar(rot=0,               # rot = text rot
                            yerr=self.df.std(),   # error bar
                            capsize = 10,       # add limit to error bars == width /2 is better
                            alpha=0.8)          # transparency


        #print(ax.bar)
        ax.xaxis.grid() # only x axis grid
        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylabel('Values')
        #ax.set_xlabel('Variables')
        ax.set_title('Title to define')

        i = 0
        x_pos = {}



        print(test['Age']['mean'])


        ## detect if dataframes is grouped or not
        if test.groups:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
            print(test)
            print(test['mean'])



        else:
            ## get x values of each bar
            for p in ax.patches:

                x_pos[self.df.columns[i]] = p.get_x() + p.get_width() /2
                i += 1
        

        
        
        ''' # for grouped values
        # here for assing number for group + columns
        for group,variable in self.df:
            print(group) #1st
            print(variable) # vars
            names = {group : variable}
        #print(self.df.groups)
        '''       
        
        


        ## link two plot
        def statistical_bracket(df, x_pos, bar1, bar2):

            
            ## check if columns are side to side or separated
            if max(df.columns.get_loc(bar1), df.columns.get_loc(bar2)) - min(df.columns.get_loc(bar1), df.columns.get_loc(bar2)) == 1:
            
                y_max = max(df[bar1]['mean'] + df[bar1]['std'], df[bar2]['mean'] + df[bar2]['std'])
            
            else:
                y_max = []

                ## For index beginning columns to end columns, find the maximum 
                for i in range(min(df.columns.get_loc(bar1), df.columns.get_loc(bar2)), max(df.columns.get_loc(bar1), df.columns.get_loc(bar2))):
                    
                    y_max.append(df.loc['mean'][i] + df.loc['std'][i]) 

                y_max = max(y_max)

            ## adjust values for being above std bar and create x y coordinate
            y_max *= 1.2
            x = [x_pos[bar1], x_pos[bar1], x_pos[bar2], x_pos[bar2]]
            y = [(df[bar1]['mean'] + df[bar1]['std'])*1.1, y_max, y_max, (df[bar2]['mean'] + df[bar2]['std'])*1.1]

            # plotting the line 
            plt.plot(x, y)

        statistical_bracket(test, x_pos,  'Force max de grip (N)', 'Age')


        # pts 1 above error bar 
        # pts 2 x point above
        # pts 3 horizontal line by adjusting x value
        # pts 4 down x points

        # + 2 hline for good looking or grouping bar ### plt.axhline(y=60, xmin=0.1, xmax=0.9) # horizontal line

   

        #plt.axhline(y=60, xmin=0.1, xmax=0.9) # horizontal line

        #plt.axvline(x=0.5, ymin=0.1, ymax=0.9) # vertical line




        # adjust staring point and length for matching with 2 bar plot

        plt.ylim(0, 200) # def lim depending of size of bar

        plt.tight_layout()
        plt.show() 
        #savefig("1.svg") # or: "1.pdf" (depending on a backend)

        
