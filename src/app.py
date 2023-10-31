#required for manipulating data
import pandas as pd
import numpy as np 


#required for building the interactive dashboard
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')


#banking data
df = pd.read_csv('/workspaces/Python-Interactive-Finance-Dashboard/src/Chase_Activity_jan_thru_oct.CSV', delimiter=',')

#cleaning/arranging  df
df=df.rename(columns={'Details': 'Date','Posting Date': 'Description','Description': 'Amount','Amount': 'Type','Type': 'Balance'})

#cleaning df

df=df[['Date','Description','Amount',]]
df['Description']=df['Description'].map(str.upper)
df['Category']='unassigned'

#define all categories

df['Category']=np.where(df['Description'].str.contains(
    'WARRIOR GUN RANGE|SMOKE SHOP|CHANDI LIQUORS|El Gato Tuerto|EL GATO TUERTO|CMX BRICKELL CITY|CMX CINEMAS|CMX|Xsolla|Groupon|GROUPON, INC|EXXEL GAS|Batch Gastropub|BATCH GASTROPUB|FLIFF|DOLORES BUT YOU CA|SUNSHINE|Casa Tiki|CASA TIKI |UNDERDOG SPORTS|CAELI SMOKE & VAPE|CIRCLE K|CAELI SMOKE & VAPE|DC TRAIL GLADES RANGE|THE QUICK SPOT|BLUE MARTINI|XSOLLA|ALPHAPLYMOUTH'),
    'Self-Care',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'PUBLIX|CVS/PHARMACY|7-ELEVEN|WALGREENS STORE|CVS/PHARM'),
    'Groceries',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'CHIPOTLE|ROSETTA BAKERY|BURGER KING|LITTLE CAESARS|TACO BELL|TRUBAR JUICE BAR|MILLER S ALE HOUSE|Vale Food Co|VALE FOOD CO|TALKINTACOS|TALKIN TACOS|COYO TACO|RAW JUCE|APOCALYPSE BBQ|Casa Tua Cucina|CASA TUA CUCINA|Pepitos Plaza|PEPITOS PLAZA|MCDONALD S|MCDONALDS|MCDONALD|WENDY|A TRIBUTE TO TOBAC|Latin Cafe|LATIN CAFE 2000|HIBACHI GRILL|SANPOCHO|STARBUCKS|CHIPOTLE ONLINE|RAISING CANE|107 TASTE|Sproutz|SPROUTZ - BRICKELL|HIBACHI GR|Stanzione 87|STANZIONE 87|FLANIGANS|Coyo Taco|BOLAY|CHICK-FIL-A|MIDNIGHT COOKIES & CREA|MAURO S PIZZA INC|MAURO PIZZA INC|WINGSTOP|GELATO & CAFE|CHINA WOK|SENOR CAFE|CABANAS RESTAURANT|PDLJ-LUNGOS SABOR|MAUROS PIZZA|CHILI|NATHANS HOT DOGS|VICKY BAKERY'),
    'Restaurants',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'DPT OF TRANSPORTATION|BRIGHTLINE TRAINS|MDC TRANSIT|UBER TRIP HELP|UBER|MIAMI PARKING|HOLLYWD BCH PKG-ON STRE|BRIGHTLINE E-COMM |MDC TRANSIT AUTOMATED'),
    'Transport',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'APPLE.COM/BILL|DOORDASH DASHPASS|METRO BY T-MOBILE|Microsoft*Store|Microsoft*Xbox|Microsoft*Subscription|SL.NORD|MICROSOFT*PC 1 MONTH|NNT MICROSOFT*PC|MICROSOFT'),
    'Subscriptions',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'ZELLE PAYMENT FROM|APPLE CASH INST'),
    'Incoming Zelle',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'ZELLE PAYMENT TO'),
    'Out Going Zelle',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'ATM WITHDRAWAL|WITHDRAWAL|NON-CHASE ATM WITHDRAW'),
    'WITHDRAWALS',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'DIRECT DEP|EQUINOX HOLDINGS PAYMENT|REMOTE ONLINE DEPOSIT|DEPOSIT|Bill.com|REAL TIME TRANSFER RECD FROM ABA/322271627 FROM: BILL.COM REF|REAL TIME PAYMENT CREDIT RECD FROM ABA/CONTR BNK|CASH OUT'),
    'Deposits',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'APPLE STORE|EQUINOX SHOP|BESTBUYCOM|USPS|OTTERBOX/LIFEPROOF|OSPREY PACKS INC|AAA ACG'),
    'Shopping',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'AIRBNB|TURKISH AIRL|WWW.2C2P|TRIP.COM'),
    'Travel',df['Category'])

df['Category']=np.where(df['Description'].str.contains(
    'FOREIGN EXCHANGE RATE ADJUSTMENT FEE|NON-CHASE ATM FEE'),
    'Fees',df['Category'])

df['Date']=pd.to_datetime(df['Date'])

df['Month']=df['Date'].dt.month
df['Year']=df['Date'].dt.year

pd.options.display.max_rows=999

# #checking unassigned category 
# unassigned = df.loc[df['Category'] == 'unassigned']
# unassigned

## Creating Top Banner for a summary of last month's income, recurring expenses, non-recurring expenses and savings

# Get the latest month and year

latest_month = df['Month'].max()
latest_year = df['Year'].max()

#filter the DF to only include transaction for the latest month

last_month_expenses=df[(df['Month']==latest_month)&(df['Year']==latest_year)]


# from pickle import FALSE
last_month_expenses= last_month_expenses.groupby('Category')['Amount'].sum().reset_index()

last_month_expenses['Amount']=last_month_expenses['Amount'].astype('str')
last_month_expenses['Amount']=last_month_expenses['Amount'].str.replace('-','')
last_month_expenses['Amount']=last_month_expenses['Amount'].astype('float')  #get absolutee figures

last_month_expenses=last_month_expenses[last_month_expenses['Category'].str.contains("unassigned")==False] #leaving out all unassigned category
last_month_expenses=last_month_expenses.sort_values(by='Amount',ascending=False) #sorting valuess
last_month_expenses['Amount']=last_month_expenses['Amount'].round().astype(int)#rounding values

#last_month_expenses


#caculating sum of last_month_expenses

last_month_expenses_tot=last_month_expenses['Amount'].sum()
# last_month_expenses_tot


#creating top bar 
def calculate_difference(event):
  income=float(income_widget.value)
  recurring_expenses=float(recurring_expenses_widget.value)
  monthly_expenses=float(monthly_expenses.widget.value)
  difference=income-recurring_expenses-monthly_expenses
  difference_widget.value=str(difference)

income_widget=pn.widgets.TextInput(name='Income',value='0')
recurring_expenses_widget=pn.widgets.TextInput(name='Recurring Expenses' ,value='0')
monthly_expenses_widget =pn.widgets.TextInput(name='Monthly Expenses',value=str(last_month_expenses_tot))
difference_widget=pn.widgets.TextInput(name="Last Month's Savings" ,value='0')

income_widget.param.watch(calculate_difference, "value")
recurring_expenses_widget.param.watch(calculate_difference, 'value')
monthly_expenses_widget.param.watch(calculate_difference, "value")


# pn.Row(income_widget,recurring_expenses_widget,monthly_expenses_widget,difference_widget).show()

## Creating last month expenses bar chart 

last_month_expenses_chart = last_month_expenses.hvplot.bar(
    x='Category', 
    y='Amount', 
    height=250, 
    width=850, 
    title="Last Month Expenses",
    ylim=(0, 500))

# last_month_expenses_chart


## Creating  monthly expenses trend bar chart 

df['Date']=pd.to_datetime(df['Date']) #converting the 'Date' column to a datetime object
df['Month-Year'] = df['Date'].dt.to_period('M') #extracting the month and year from the 'Date' column and create a new column 'Month-Year'
monthly_expenses_trend_by_cat=df.groupby(['Month-Year','Category'])['Amount'].sum().reset_index()

monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('str')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].str.replace('-','')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('float')
monthly_expenses_trend_by_cat=monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat["Category"].str.contains("Excluded|unassigned")== False]

monthly_expenses_trend_by_cat=monthly_expenses_trend_by_cat.sort_values(by='Amount',ascending=False)
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].round().astype(int)
monthly_expenses_trend_by_cat['Month-Year']=monthly_expenses_trend_by_cat['Month-Year'].astype(str)
monthly_expenses_trend_by_cat=monthly_expenses_trend_by_cat.rename(columns={'Amount':'Amount'})

# monthly_expenses_trend_by_cat

#Defining Panel widgets

select_category1=pn.widgets.Select(name='Select_Category',options=[
#   'All',
  'Self-Care',
#   'Fines', 
  'Groceries',
  'Shopping', 
  'Restaurants',
  'Transport',
  'Travel', 
  'Subscriptions', 
  'Incoming Zelle', 
  'Out Going Zelle', 
  'WITHDRAWALS', 
  'Deposits', 
])
# select_category1

#defining plot function
 
def plot_expenses(category):
  if category == 'ALL':
    plot_df = monthly_expenses_trend_by_cat.groupby('Month-year').sum()
  else:
    plot_df=monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat['Category']==category].groupby('Month-Year').sum()
  plot =plot_df.hvplot.bar(x='Month-Year', y='Amount')
  return plot


  #define callback function

@pn.depends(select_category1.param.value)
def update_plot(category):
    plot = plot_expenses(category)
    return plot

#create layout
monthly_expenses_trend_by_cat_chart=pn.Row(select_category1,update_plot)
monthly_expenses_trend_by_cat_chart[1].width=600


# ALL and Fines not functioning 
# monthly_expenses_trend_by_cat_chart

##creating summary table
df=df[['Date', 'Category','Description','Amount']]
df['Amount']=df['Amount'].astype('str')
df['Amount']=df['Amount'].str.replace('-','')
df['Amount']=df['Amount'].astype('float') #get absolute figures

# df=df[df["Category"].str.contains("Excluded|unassigned")==False] #leaving out all unassigned category
df['Amount']=df['Amount'].round().astype(int)#rounding values


# Define a function to filter the dataframe based on the selected category

def filter_df(category):
  if category =='ALL':
    return df
  return df[df['Category'] == category]

# Create a DataFrame widget that updates based on the category filter

summary_table= pn.widgets.DataFrame(filter_df('ALL'),height = 300, width=400)

# Define a callback that updates the dataframe widget when the category filter is changed

def update_summary_table(event):
    summary_table.value=filter_df(event.new)

# Add the callback function to the category widget

select_category1.param.watch(update_summary_table, 'value')

# summary_table


## Creatting Final Dashboard

template=pn.template.FastListTemplate(
    title="Personal Finances Summary",
    sidebar=[
        pn.pane.Markdown("## *If you can't manage your money, making more won't help*"),
        pn.pane.PNG('/workspaces/Python-Interactive-Finance-Dashboard/src/financial-investment-png-image.png', sizing_mode='scale_both'),
        pn.pane.Markdown(""),
        pn.pane.Markdown(""),
        select_category1
    ],
    main=[
        pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget, width=950),
        pn.Row(last_month_expenses_chart, height=240),
        pn.GridBox(
            monthly_expenses_trend_by_cat_chart[1],
            summary_table,
            ncols=2,
            width=500,
            align='start',
            sizing_mode='stretch_width'

        )
    ]
)

template.show()