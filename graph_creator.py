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

    def __init__(self, df=None, ax=None, grouped=True, width=None):

        self.df = df
        self.ax = ax
        self.grouped = grouped
        self.width = width



    ## link two plot For non-grouped var
    def statistical_bracket(self, bar1, bar2):

        x_pos = {}
        i = 0

        ## get x pos of bars
        for p in self.ax.patches:
            
            # get x value position of bars
            x_pos[self.df.columns[i]] = p.get_x() + p.get_width() /2
            i += 1
            self.width = p.get_width()


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



        ## draw bracket using line pos
        ## adjust values for being above std bar and create x y coordinate
        y_max *= 1.2
        x = [x_pos[bar1], x_pos[bar1], x_pos[bar2], x_pos[bar2]]
        y = [(df[bar1]['mean'] + df[bar1]['std'])*1.1, y_max, y_max, (df[bar2]['mean'] + df[bar2]['std'])*1.1]

        # plotting the line 
        plt.plot(x, y)
    
        ## draw end of lines
        plt.hlines(y=y[0], xmin=x[0]-self.width/4, xmax=x[0]+self.width/4)
        plt.hlines(y=y[-1], xmin=x[-1]-self.width/4, xmax=x[-1]+self.width/4)

        ## plot text, for now just a star
        plt.text((x[-1]+x[0])/2, y_max, '*')
        

        # + 2 hline for good looking or grouping bar ### plt.axhline(y=60, xmin=0.1, xmax=0.9) # horizontal line



        #plt.axhline(y=60, xmin=0.1, xmax=0.9) # horizontal line
        #plt.axvline(x=0.5, ymin=0.1, ymax=0.9) # vertical line


        # adjust staring point and length for matching with 2 bar plot

        #plt.ylim(0, 200) # def lim depending of size of bar
        plt.tight_layout()
        plt.show() 


    ## link two plot For grouped var
    def grouped_statistical_bracket(self, bar1_group, bar1_var, bar2_group, bar2_var):

        x_pos = {}
        i = 0
        
        df_mean = self.df.mean()
        df_std = self.df.std()

        
        # init the row dict
        for row in df_mean.index:   
            x_pos[row] = {} 
        
        ## get x pos of bars and y max (mean + std)
        for variable in df_mean.columns:
            
            for row in df_mean.index:   
                x_pos[row][variable] = {} 
                # get x value value position of bars and 
                x_pos[row][variable]['x_pos'] = self.ax.patches[i].get_x() + self.ax.patches[i].get_width() /2
                x_pos[row][variable]['y_max'] = df_mean[variable][row] + df_std[variable][row] 
                x_pos[row][variable]['var'] = variable
                x_pos[row][variable]['group'] = row
                self.width = self.ax.patches[i].get_width()
                i += 1
        

        #plt.tight_layout()
        #plt.show() 

        order = {}
        i = 0
        for group in x_pos:
    
            for var in x_pos[group]:
                
                x_pos[group][var]['order'] = i
                order[i] = x_pos[group][var]

                i += 1

    
        ## check how many values are in [] and get the max
        i = 0
        y = []

        begin = min(x_pos[bar1_group][bar1_var]['order'], x_pos[bar2_group][bar2_var]['order'])
        end = max(x_pos[bar1_group][bar1_var]['order'], x_pos[bar2_group][bar2_var]['order'])

        ## get all the values between var
        for i in range(begin, end+1):
        
            y.append(order[i]['y_max'])


        ## draw bracket using line pos
        ## adjust values for being above std bar and create x y coordinate$
        y_max = max(y)
        y_max *= 1.2
        x = [order[begin]['x_pos'], order[begin]['x_pos'], order[end]['x_pos'], order[end]['x_pos']]
        y = [y[0]*1.1, y_max, y_max, y[-1]*1.1] # -1 == last element of list

        # plotting the line 
        plt.plot(x, y)
        
        ## draw end of lines
        plt.hlines(y=y[0], xmin=x[0]-self.width/4, xmax=x[0]+self.width/4)
        plt.hlines(y=y[-1], xmin=x[-1]-self.width/4, xmax=x[-1]+self.width/4)

        ## plot text, for now just a star
        plt.text((x[-1]+x[0])/2, y_max, '*')


        plt.tight_layout()
        plt.show() 



























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

        
