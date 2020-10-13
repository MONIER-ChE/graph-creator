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

    def __init__(self, df=None, ax=None, grouped=True):

        self.df = df
        self.ax = ax
        self.grouped = grouped



    ## link two plot
    def statistical_bracket(self, bar1=[], bar2=[]):


        x_pos = {}
        i = 0

        ## For grouped var
        if self.grouped == True:

            df = self.df.mean()
            x_pos = {}
            for row in df.index:
                
                x_pos[row] = {}
                for variable in df:
                    
                    # get x value value position of bars
                    x_pos[row][variable] = self.ax.patches[i].get_x() + self.ax.patches[i].get_width() /2
                    i += 1


        ## For non-grouped var
        else:

            for p in self.ax.patches:
                
                # get x value position of bars
                x_pos[self.df.columns[i]] = p.get_x() + p.get_width() /2
                i += 1

            print(x_pos)

            
            df = self.df.describe()
            
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


        plt.tight_layout()
        plt.show() 
            

    # pts 1 above error bar 
    # pts 2 x point above
    # pts 3 horizontal line by adjusting x value
    # pts 4 down x points

    # + 2 hline for good looking or grouping bar ### plt.axhline(y=60, xmin=0.1, xmax=0.9) # horizontal line



    #plt.axhline(y=60, xmin=0.1, xmax=0.9) # horizontal line
    #plt.axvline(x=0.5, ymin=0.1, ymax=0.9) # vertical line


    # adjust staring point and length for matching with 2 bar plot

    plt.ylim(0, 200) # def lim depending of size of bar
    




    def bar_plot(self):
        
        df = self.df.mean()
        yerr = self.df.std()

        self.ax = df.plot.bar(rot=0,            # rot = text rot
                            yerr=yerr,          # error bar
                            capsize = 10,       # add limit to error bars == width /2 is better
                            alpha=0.8)          # transparency


        #print(ax.bar)
        
        ## ask later
        self.ax.xaxis.grid() # only x axis grid
        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylabel('Values')
        #ax.set_xlabel('Variables')
        #self.ax.set_title('Title to define')
        


        #savefig("1.svg") # or: "1.pdf" (depending on a backend)

        
