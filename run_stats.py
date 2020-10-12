






class grouped_plot(plot):
    """
    class build from plot class for grouped graph
    """
    
    def bar_plot(a_mean, b_mean, a_std, b_std, groups_labels, variables_labels, grouped_describe):
    '''
    function for build grouped bar plot 
    '''
        print('a')

    

    
    def statistic(bars, variables_labels):
        '''
        Create data of position
        '''
        for var in variables_labels:
            
            grouped_describe[var, 'x_pos'] = ['NaN','NaN']


        a = 0
        ## Find each values for group A then group B
        for bar in bars:
            pos = []
            
            for data in bar:
                pos.append(data.get_x()+0.25/2) # mid width size
                
            
            i=0
            ## Fill values with good variables
            for var in variables_labels:
                
                grouped_describe[var,'x_pos'][a] = pos[i]
                i+=1
            a +=1
            


    
class basic_plot(plot):
    """
    class build from plot class
    """
    def bar_plot(self):
        print("Hello my name is " + self.name)

    def line_plot(self):
        print("Hello my name is " + self.name)






def grouped_bar_plot(a_mean, b_mean, a_std, b_std, groups_labels, variables_labels, grouped_describe):
    '''
    function for build grouped bar plot 
    '''

    x = np.arange(len(variables_labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    
    a_bar = ax.bar(x - width/2, 
                    a_mean, width, 
                    label=groups_labels[0], 
                    yerr=a_std, 
                    align='center', 
                    capsize = 10, 
                    alpha=0.8) #capsize = limit to error bar

                    

    b_bar = ax.bar(x + width/2, 
                    b_mean, width, 
                    label=groups_labels[1], 
                    yerr=b_std, 
                    align='center', 
                    capsize = 10,
                    alpha=0.8) # trasnparency

    


    # Add some text for labels, title and custom x-axis tick labels, etc.
    #ax.set_ylabel('Values')
    #ax.set_xlabel('Variables')
    ax.set_title('Title to define')
    ax.set_xticks(x)
    ax.set_xticklabels(variables_labels)
    ax.legend()


    
    def statistic(bars, variables_labels):
        '''
        Create data of position
        '''
        for var in variables_labels:
            
            grouped_describe[var, 'x_pos'] = ['NaN','NaN']


        a = 0
        ## Find each values for group A then group B
        for bar in bars:
            pos = []
            
            for data in bar:
                pos.append(data.get_x()+0.25/2) # mid width size
                
            
            i=0
            ## Fill values with good variables
            for var in variables_labels:
                
                grouped_describe[var,'x_pos'][a] = pos[i]
                i+=1
            a +=1
            

    
    def draw(label, grouped_describe):
        '''
        create braket stats
        '''

        ylim = max(grouped_describe[label,'max'].iloc[0], grouped_describe[label,'max'].iloc[1])
        length = grouped_describe[label,'x_pos'].iloc[0] + grouped_describe[label,'x_pos'].iloc[1]
        
        test = ax.annotate("", 
                    xy=(grouped_describe[label,'x_pos'].iloc[0], ylim), 
                    xycoords='data',
                    xytext=(grouped_describe[label,'x_pos'].iloc[1],ylim), 
                    textcoords='data',
                    arrowprops=dict(arrowstyle="-",
                                    ec='#aaaaaa',
                                    connectionstyle="bar,fraction=0.2",
                                    linewidth=2))

        #print(test) #Hold data if 2 take the same origin, put it higher ? 

        # 0.5 is position of asterix
        ax.text(length/2,
                ylim + 5 ,
                '*',
                zorder=10,#order in z axis, so draw above all
                horizontalalignment='center',
                verticalalignment='center')



        plt.ylim(0, ylim+50) # def lim depending of size of bar
        


    def draw_different(label1,label2, grouped_describe):
        '''
        create braket stars above all other because he link long distance bar
        '''

        ylim = max(grouped_describe[label1,'max'].iloc[0], grouped_describe[label2,'max'].iloc[1])
        length = grouped_describe[label1,'x_pos'].iloc[0] + grouped_describe[label2,'x_pos'].iloc[1]
        
        ax.annotate("", 
                    xy=(grouped_describe[label2,'x_pos'].iloc[0], ylim), 
                    xycoords='data',
                    xytext=(grouped_describe[label1,'x_pos'].iloc[1],ylim), 
                    textcoords='data',
                    arrowprops=dict(arrowstyle="-",
                                    ec='#aaaaaa',
                                    connectionstyle="bar,fraction=0.2",
                                    linewidth=2))


        # 0.5 is position of asterix
        testo = ax.text(length/2,
                ylim + 7,
                '*',
                zorder=10,#order in z axis, so draw above all
                horizontalalignment='center',
                verticalalignment='center')

        print(testo)

        plt.ylim(0, ylim+50) # def lim depending of size of bar
        
    statistic([a_bar, b_bar], variables_labels)
    


    #draw('Age', grouped_describe)
    #draw('Force max de grip (N)', grouped_describe)

    draw_different('Force max de grip (N)','Age', grouped_describe)

    
    





    '''
    def barplot_annotate_brackets(num1, num2, data, center, height, yerr=None, dh=.05, barh=.05, fs=None, maxasterix=None):
        """ 
        Annotate barplot with p-values.
        https://stackoverflow.com/questions/11517986/indicating-the-statistically-significant-difference-in-bar-graph

        :param num1: number of left bar to put bracket over
        :param num2: number of right bar to put bracket over
        :param data: string to write or number for generating asterixes
        :param center: centers of all bars (like plt.bar() input)
        :param height: heights of all bars (like plt.bar() input)
        :param yerr: yerrs of all bars (like plt.bar() input)
        :param dh: height offset over bar / bar + yerr in axes coordinates (0 to 1)
        :param barh: bar height in axes coordinates (0 to 1)
        :param fs: font size
        :param maxasterix: maximum number of asterixes to write (for very small p-values)
        """

        if type(data) is str:
            text = data
        else:
            # * is p < 0.05
            # ** is p < 0.005
            # *** is p < 0.0005
            # etc.
            text = ''
            p = .05

            while data < p:
                text += '*'
                p /= 10.

                if maxasterix and len(text) == maxasterix:
                    break

            if len(text) == 0:
                text = 'n. s.'

        lx, ly = center[num1], height[num1]
        rx, ry = center[num2], height[num2]

        if yerr:
            ly += yerr[num1]
            ry += yerr[num2]

        ax_y0, ax_y1 = plt.gca().get_ylim()
        dh *= (ax_y1 - ax_y0)
        barh *= (ax_y1 - ax_y0)

        y = max(ly, ry) + dh

        barx = [lx, lx, rx, rx]
        bary = [y, y+barh, y+barh, y]
        mid = ((lx+rx)/2, y+barh)

        plt.plot(barx, bary, c='grey')

        kwargs = dict(ha='center', va='bottom')
        if fs is not None:
            kwargs['fontsize'] = fs

        plt.text(*mid, text, **kwargs)


    bars = np.arange(len(b_mean))
    barplot_annotate_brackets(0, 1, '*', bars, b_mean)


    bars = np.arange(len(a_mean))
    barplot_annotate_brackets(0, 1, '*', bars, a_mean)
    '''











    '''
    ##### EDIT THIS TO MAKE A FUNCTION MATCHING WITH
    def correlation_bracket(pos_bar_1, pos_bar_2):
        y_max = np.max(np.concatenate((a_mean, b_mean)))
        y_min = np.min(np.concatenate((a_mean, b_mean)))
        
        # xy is the fist columns
        # xytest is the second problem
        # But here the columns are one for 2 (groued bar consider like 1)
        # for xytext 2nd data is th offset

        ax.annotate("", 
                    xy=(0, y_max), 
                    xycoords='data',
                    xytext=(1, y_max), 
                    textcoords='data',
                    arrowprops=dict(arrowstyle="-",
                                    ec='#aaaaaa',
                                    connectionstyle="bar,fraction=0.2"))

        # 0.5 is position of asterix
        ax.text(0.5,
                y_max + abs(y_max - y_min)*0.1,
                '*',
                horizontalalignment='center',
                verticalalignment='center')



        plt.ylim(0, 100) # def lim depending of size of bar
    '''



    fig.tight_layout()
    plt.show()    
    #savefig("1.svg") # or: "1.pdf" (depending on a backend)
'''