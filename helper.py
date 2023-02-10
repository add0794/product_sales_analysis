from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def get_basic_info(df):
    
    print(f'The dataframe has {len(df)} rows and {len(df.columns)} columns. Its columns and data types are:\n{df.dtypes}.')
    print(f"Here's a hint at what's to come: {df.head()}")


def rename(df, column, *args):

    """
    args[0] = 'email' or 'em + call'
    args[1] = 'Email' or 'Email + Call'
    """

    df[column] = df[column].replace(args[0], args[1])
    return df


def remove(df):

    df = df.dropna()
    return df


def unique_values(df, column):

    return df[column].unique()


def my_fmt(x, total):
    
    return '{:.1f}% \n({:.0f})'.format(x, total*x/100)


def show_pie_chart(df, my_fmt, *args):
    
    """
    args[0] = 'sales_method'
    args[1] = 'customer_id'
    """

    fig = plt.gcf()
    fig.set_facecolor('black')

    v_counts = df.groupby(args[0])[[args[1]]].count()
    v_counts = v_counts.reset_index()
    labels = v_counts[args[0]].tolist()    
    v_counts = v_counts[args[1]].values
    total = len(df)
    plt.pie(v_counts, labels = labels, autopct = lambda x: my_fmt(x, total), shadow = True, textprops = {'color': 'white'})
    plt.suptitle('Customers for Each Approach', fontsize = 16, color = 'white')

    plt.show()


def count_proportions(df, *args):
    
    """
    args[0] = 'sales_method'
    args[1] = 'Email' or 'Call' or 'Email + Call'
    args[2] = 'state
    args[3] = 'customer_id'
    """

    total = df[df[args[0]] == args[1]]
    total = total.groupby(args[2])[args[3]].count()
    total = {key: round(value/total.sum(), 4) for (key, value) in total.items()}

    keys = df[args[2]].unique()
    sorted_keys = sorted(keys)

    result = []
    for i in sorted_keys:
        if i in df[args[2]].unique() and i not in total.keys():
            total[i] = 0
        result.append(total[i])

    return result


def hist(df, *args):

    """
    args[0] = 'revenue'
    args[1] = df[args[0]].min()
    args[2] = df[args[0].max()
    """

    value = round((args[2] - args[1]) / 10, 2)
    bins = np.arange(args[1], (args[2] + value), value)
    plt.hist(df[args[0]], color = 'purple', edgecolor = 'black')
    plt.xlim(args[1], args[2])
    plt.xlabel(f'{args[0].title()} Per Customer', color = 'white')
    plt.ylabel('Count', color = 'white')
    plt.xticks(bins, color = 'white')
    plt.yticks(color = 'white')  
    plt.title(f'Spread of {args[0].title()} by Count of Approximate Sales', color = 'white')

    plt.style.use('dark_background')

    plt.show()


def bar_chart(df, *args):

    """
    args[0] = 'sales_method'
    args[1] = 'revenue'
    """

    values = df.groupby(args[0])[args[1]].sum().to_dict()
    plt.bar(*zip(*values.items()), align = 'center', edgecolor = 'black')
    plt.xlabel(f'{args[0]} Per Customer', color = 'white')
    plt.ylabel(f'{args[1].title()}', color = 'white')
    plt.xticks(color = 'white')
    plt.yticks(color = 'white')  
    plt.title(f'{args[1].title()} by Sales Method', color = 'white')

    plt.style.use('dark_background')

    plt.show()
    
    
def line_chart(df, *args):

    """
    args[0] = 'sales_method'
    args[1] = ['Email', 'Email + Call', 'Call']
    args[2] = 'week'
    args[3] = 'revenue'
    """

    fig, ax = plt.subplots()

    for method in args[1]:
        plot = df[df[args[0]] == method]
        grouped_plots = plot.groupby(args[2])[args[3]].sum()

        ax.plot(grouped_plots, label = method)

    ax.set_xlabel(f'{args[2].title()}', fontsize = 12, color = 'white')
    ax.set_ylabel(f'{args[3].title()}', fontsize = 12, color = 'white')
    ax.set_title(f'Weekly {args[3].title()} by Sales Method', fontsize = 12, color = 'white')
    ax.set_facecolor('black')

    ax.xaxis.set_tick_params(color = 'white')
    ax.yaxis.set_tick_params(color = 'white')

    plt.legend(loc = 'upper right', frameon = True)

    plt.style.use('dark_background')

    plt.show()


def bar_chart_comparison(df, *args):

    """
    args[0] = 'sales_method'
    args[1] = 'week'
    args[2] = 'customer_id'
    """

    v_counts = df.groupby([args[0], args[1]])[args[2]].count().unstack()
    ax = v_counts.plot(kind = 'bar')

    fig = plt.gcf()
    fig.set_facecolor('black')

    ax.set_facecolor('black')
    ax.set_xlabel(f'{args[0]}', color = 'white')
    ax.set_ylabel('Count', color = 'white')
    ax.set_xticklabels(ax.get_xticklabels(), color = 'white', rotation = 90)
    ax.set_yticklabels(ax.get_yticklabels(), color = 'white')
    ax.set_title(f'Count of Sales by {args[0]}', color = 'white')

    plt.style.use('dark_background')

    plt.show()


def sales_summary(df, *args):

    """
    args[0] = 'sales_method'
    args[1] = 'week'
    args[2] = 'customer_id'
    args[3] = 'revenue'
    """

    v_counts_1 = df.groupby([args[0], args[1]])[args[2]].count().unstack()
    v_counts_2 = df.groupby(args[1])[args[3]].sum().reset_index()
    print(f'Sales by {args[0]} \n {v_counts_1}\n Revenue by week\n {v_counts_2}')
