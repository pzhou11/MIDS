##DATA LOADER
#############

import csv 
import pandas as pd
import matplotlib.pyplot as plt
import re
%matplotlib inline  

with open('Data/2015.tsv','r') as tsv:
    data = [line.strip().split('\t') for line in tsv]
    
col_names = data[0]
df = pd.DataFrame(data, columns=col_names)
df = df[1:]

#open code_sex.csv and convert it to a DataFrame
with open('Data/code_sex.csv','r') as csv:
    sex_descrip = [line.strip().split(',') for line in csv]

sex_header = sex_descrip[0]
df_sex = pd.DataFrame(sex_descrip, columns=sex_header)
df_sex = df_sex[1:]
indexed_df_sex = df_sex.set_index('Code')

#open code_body_part.csv and convert it to a DataFrame
with open('Data/code_body_part.csv','r') as csv:
    body_part_descrip = [line.strip().split(',') for line in csv]

body_part_header = body_part_descrip[0]
df_body_part = pd.DataFrame(body_part_descrip, columns=body_part_header)
df_body_part = df_body_part[1:]
indexed_df_body_part = df_body_part.set_index('Code')

#open code_diagnosis.csv and convert it to a DataFrame
with open('Data/code_diagnosis.csv','r') as csv:
    diagnosis_descrip = [line.strip().split(',') for line in csv]

diagnosis_header = diagnosis_descrip[0]
df_diagnosis = pd.DataFrame(diagnosis_descrip, columns=diagnosis_header)
df_diagnosis = df_diagnosis[1:]
indexed_df_diagnosis = df_diagnosis.set_index('Code')

#open code_disposition.csv and convert it to a DataFrame
with open('Data/code_disposition.csv','r') as csv:
    disposition_descrip = [line.strip().split(',') for line in csv]

disposition_header = disposition_descrip[0]
df_disposition = pd.DataFrame(disposition_descrip, columns=disposition_header)
df_disposition = df_disposition[1:]
indexed_df_disposition = df_disposition.set_index('Code')

#open code_fire.csv and convert it to a DataFrame
with open('Data/code_fire.csv','r') as csv:
    fire_descrip = [line.strip().split(',') for line in csv]

fire_header = fire_descrip[0]
df_fire = pd.DataFrame(fire_descrip, columns=fire_header)
df_fire = df_fire[1:]
indexed_df_fire = df_fire.set_index('Code')

#open code_locale.csv and convert it to a DataFrame
with open('Data/code_locale.csv','r') as csv:
    locale_descrip = [line.strip().split(',') for line in csv]

locale_header = locale_descrip[0]
df_locale = pd.DataFrame(locale_descrip, columns=locale_header)
df_locale = df_locale[1:]
indexed_df_locale = df_locale.set_index('Code')

#open code_product.csv and convert it to a DataFrame
with open('Data/code_product.csv','r') as csv:
    product_descrip = [line.strip().split(',',1) for line in csv]

product_header = product_descrip[0]
df_product = pd.DataFrame(product_descrip, columns=product_header)
df_product = df_product[1:]
indexed_df_product = df_product.set_index('Code')

#open code_race.csv and convert it to a DataFrame
with open('Data/code_race.csv','r') as csv:
    race_descrip = [line.strip().split(',') for line in csv]

race_header = race_descrip[0]
df_race = pd.DataFrame(race_descrip, columns=race_header)
df_race = df_race[1:]
indexed_df_race = df_race.set_index('Code')

#merge all the codes
df['sex_descrip']=df.sex.map(indexed_df_sex.Description)
df['body_part_descrip']=df.body_part.map(indexed_df_body_part.Description)
df['diag_descrip']=df.diag.map(indexed_df_diagnosis.Description)
df['disposition_descrip']=df.disposition.map(indexed_df_disposition.Description)
df['fire_descrip']=df.fmv.map(indexed_df_fire.Description)
df['locale_descrip']=df.location.map(indexed_df_locale.Description)
df['product1_descrip']=df.prod1.map(indexed_df_product.Description)
df['product2_descrip']=df.prod2.map(indexed_df_product.Description)
df['race_descrip']=df.race.map(indexed_df_race.Description)

#combine the 2 narr fields into 1
df['Notes'] = df['narr1'].map(str) + df['narr2'].map(str)

df1 = df[['CPSC Case #', 
         'trmt_date', 
         'psu', 
         'weight', 
         'age', 
         'sex_descrip', 
         'race_descrip',
         'body_part_descrip', 
         'diag_descrip', 
         'disposition_descrip', 
         'fire_descrip', 
         'locale_descrip', 
         'product1_descrip', 
         'product2_descrip', 
         'Notes']]

#convert numerical columns to numeric data type
df1 = df1.apply(lambda x: pd.to_numeric(x,errors="ignore"))

#convert 'trmt_date' column to datetime type
df1['trmt_date'] = df1['trmt_date'].apply(lambda x: pd.to_datetime(x,format='%m/%d/%Y'))

<<<<<<< HEAD
#adjust ages >120yo
def age_filter(age):
    if age > 120:
        return 1
    else:
        return age
=======
#remove quotation marks from product1_desrip field
df1['product1_descrip'] = df1['product1_descrip'].apply(lambda x: re.sub('"','',str(x)))
>>>>>>> 1cb177202ab4b134bd7c0f8b7b3393a5cc8dcca3

df1['age'] = df1['age'].astype(int).map(age_filter)

#extra functions
def textfind(dataframe, field, string):
    """ Takes dataframe, field (column in the dataframe), and a string to search
    Allow for use of regular expressions.
    Returns a dataframe of the records where the string is found"""
    import re
    a = [dataframe.loc[i] for i in dataframe.index \
         if re.search(string, dataframe[field][i])]
    return pd.DataFrame(a)
    
def notereader(dataframe):
    """ Takes a dataframe that contains the 'Notes' field and prints it out in a
    readable fashion.
    Returns a dictionary of Index (integer): Note (string) pairs"""
    output_dict ={}
    for i in dataframe.index:           
        output_dict[i] = dataframe.Notes[i]
        print ("INDEX", i,"\n", dataframe.Notes[i],"\n")
    return output_dict

pd.options.display.max_colwidth = 1000

# OMAR'S CODE
#############

#                                  NEW Jupyter Notebook Cell
#creating dfjunk dataframe, for "junk in the trunk" injuries
dfjunk = textfind(df1, 'Notes', '\sRECTUM\s(?!TO STOP|TO PUSH|NOTED|DX|S/P FALLING|WITH VERY)')
len(dfjunk)

#                                  NEW Jupyter Notebook Cell
#plotting histogram of Junk in the Trunk Injuries vs Age by sex
junk_M_plot = dfjunk[dfjunk.sex_descrip == 'MALE'].age
junk_F_plot =dfjunk[dfjunk.sex_descrip == 'FEMALE'].age
junk_m = plt.hist(junk_M_plot,alpha=0.5, bins = 14, color = 'blue',label='MALE')
junk_f = plt.hist(junk_F_plot,alpha=0.5, bins = 10,color = 'red',label='FEMALE')
plt.legend()
plt.title('Number of "Junk in the Trunk" Injuries \nby Age')
plt.xlabel('Age')
plt.ylabel('Number of Injuries')
plt.show

#creating and displaying df of Junk in the Trunk Injuries average age and percentage of 
#total injuries
junk_sort = {'CPSC Case #':['count'], 'age':['mean']}
junk_table = pd.DataFrame(dfjunk.groupby('sex_descrip').agg(junk_sort))
junk_table['percentage'] = junk_table['CPSC Case #'].apply(lambda x: 100*x/float(x.sum()))
junk_table[['age','percentage']]
junk_table

#                                  NEW Jupyter Notebook Cell
#Plotting "junk in the trunk" injuries vs product1_descrip
dfjunk.groupby('product1_descrip')['age'].count().sort_values(ascending=False).head(10).plot.bar()

#                                  NEW Jupyter Notebook Cell
#Plotting "junk in the trunk" injuries vs categories defined by me
dfjunk_in = pd.Series({'Sex Toy' : textfind(dfjunk,'Notes','\sVIBRATOR\s|\sTOY\s|DILDO')['age'].count(),
             'Writing Instrument': textfind(dfjunk,'Notes','\sPENCIL\s|\sPEN\s|\sDAUBER\s')['age'].count(),
              'Flashlight': textfind(dfjunk,'Notes','\sFLASHLIGHT\s')['age'].count(),
              'Brush': textfind(dfjunk,'Notes','BRUSH')['age'].count(),
              'Spherical Object': textfind(dfjunk,'Notes','\sBEAD\s|\sMARBLE|BALL\s')['age'].count(),
              'Tool': textfind(dfjunk,'Notes','\sSCREWDRIVER\s|\sHAMMER\s')['age'].count(),
              'Bottle': textfind(dfjunk,'Notes','\sBOTTLE\s')['age'].count(),
              'Drugs': textfind(dfjunk,'Notes','\sMETHAMPHETAMINE\s|MJ')['age'].count()
             })

dfjunk_in.sort_values(ascending=False).plot.bar()
plt.xlabel('Object Causing Injury')
plt.ylabel('Number of Injuries')
plt.title('Number of Junk in the Trunk Injuries\nby Object')

#                                  NEW Jupyter Notebook Cell
#creating dfsadness dataframe, for Sadness injuries
dfsadness = textfind(df1, 'Notes', '\sSAD\s|\sSADNESS\s|\sUNHAPPY\s|(?<!SKULL|SCULL)\sDEPRESSED\s(?!SKULL|SCULL|FX|RIGHT|RSKULL)')[df1['age'] < 121]
len(dfsadness)

#                                  NEW Jupyter Notebook Cell
#plotting histogram of Sadness Injuries vs Age by sex
sadness_M_plot = dfsadness[dfsadness.sex_descrip == 'MALE'].age
sadness_F_plot =dfsadness[dfsadness.sex_descrip == 'FEMALE'].age
sadness_m = plt.hist(sadness_M_plot,alpha=0.5, bins = 10, color = 'blue',label='MALE')
sadness_f = plt.hist(sadness_F_plot,alpha=0.5, bins = 8,color = 'red',label='FEMALE')
plt.legend()
plt.title('Number of "Sadness" Injuries \nby Age')
plt.xlabel('Age')
plt.ylabel('Number of Injuries')
plt.show

#creating and displaying df of Sadness Injuries average age and percentage of 
#total injuries
sadness_sort = {'CPSC Case #':['count'], 'age':['mean']}
sadness_table = pd.DataFrame(dfsadness.groupby('sex_descrip').agg(sadness_sort))
sadness_table['percentage'] = sadness_table['CPSC Case #'].apply(lambda x: 100*x/float(x.sum()))
sadness_table[['age','percentage']]

#                                  NEW Jupyter Notebook Cell
#Plotting Sadness injuries vs product1_descrip
sadness = dfsadness.groupby('product1_descrip')['age'].count().sort_values(ascending=False).head(5).plot.bar()
plt.xlabel('Product Description')
plt.ylabel('Number of Injuries')
plt.title('Number of Sadness Injuries\nby Product Description')

sadness.set_xticklabels(['Floors','Knives','Ceilings and Walls','Windows',\
             'Televisions'])

#                                  NEW Jupyter Notebook Cell
#creating dfexcite dataframe, for Excitement injuries
dfexcite = textfind(df1, 'Notes', '\sEXCITED\s|\sEXCITEMENT\s')
len(dfexcite)

#                                  NEW Jupyter Notebook Cell
#plotting histogram of Excitement Injuries vs Age by sex
excite_M_plot = dfexcite[dfexcite.sex_descrip == 'MALE'].age
excite_F_plot =dfexcite[dfexcite.sex_descrip == 'FEMALE'].age
excite_m = plt.hist(excite_M_plot,alpha=0.5, bins = 10, color = 'blue',label='MALE')
excite_f = plt.hist(excite_F_plot,alpha=0.5, bins = 8,color = 'red',label='FEMALE')
plt.legend()
plt.title('Number of "Excitement" Injuries \nby Age')
plt.xlabel('Age')
plt.ylabel('Number of Injuries')
plt.show

#creating and displaying df of Excitement Injuries average age and percentage of 
#total injuries
excite_sort = {'CPSC Case #':['count'], 'age':['mean']}
excite_table = pd.DataFrame(dfexcite.groupby('sex_descrip').agg(excite_sort))
excite_table['percentage'] = excite_table['CPSC Case #'].apply(lambda x: 100*x/float(x.sum()))
#pd.set_option('float_format', '{:.1f}'.format)
excite_table[['age','percentage']]

#                                  NEW Jupyter Notebook Cell
#Plotting Excitement injuries vs categories defined by me
dfexcite_at = pd.Series({'Dog' : textfind(dfexcite,'Notes','\sDOG\s|\sDOGS\s')['age'].count(),
             'Swimming Pool': textfind(dfexcite,'Notes','\sPOOL')['age'].count(),
              'Watching Sports': textfind(dfexcite,'Notes','\sFIGHT\s|\sFOOTBALL\s')['age'].count(),
              'Pizza': textfind(dfexcite,'Notes','\sPIZZA\s')['age'].count(),
              'Fish Catching': textfind(dfexcite,'Notes','\sFISH\s')['age'].count(),
              'Seeing Family': textfind(dfexcite,'Notes','\sGRANDDAUGHTER\s|\sFAMILY\s(?!DOG)')['age'].count()
             })

dfexcite_at.sort_values(ascending=False).plot.bar()
plt.xlabel('Category')
plt.ylabel('Number of Injuries')
plt.title('Number of Excitement Injuries\nby Category')

#                                  NEW Jupyter Notebook Cell
#creating dffear dataframe, for Fear injuries
dffear = textfind(df1, 'Notes', '\sFEAR\s|\sAFRAID\s|\sSCARED\s|\sFRIGHT')[df1['age'] < 121]
len(dffear)

#                                  NEW Jupyter Notebook Cell
#plotting histogram of Fear Injuries vs Age by sex
fear_M_plot = dffear[dffear.sex_descrip == 'MALE'].age
fear_F_plot = dffear[dffear.sex_descrip == 'FEMALE'].age
fear_m = plt.hist(fear_M_plot,alpha=0.5, bins = 10, color = 'blue',label='MALE')
fear_f = plt.hist(fear_F_plot,alpha=0.5, bins = 10,color = 'red',label='FEMALE')
plt.legend()
plt.title('Number of "Fear" Injuries \nby Age')
plt.xlabel('Age')
plt.ylabel('Number of Injuries')
plt.show

#creating and displaying df of Fear Injuries average age and percentage of 
#total injuries
fear_sort = {'CPSC Case #':['count'], 'age':['mean']}
fear_table = pd.DataFrame(dffear.groupby('sex_descrip').agg(fear_sort))
fear_table['percentage'] = fear_table['CPSC Case #'].apply(lambda x: 100*x/float(x.sum()))
fear_table[['age','percentage']]

#                                  NEW Jupyter Notebook Cell
#Plotting Fear injuries vs product1_descrip
fear = dffear.groupby('product1_descrip')['age'].count().sort_values(ascending=False).head(6).plot.bar()
plt.xlabel('Product Description')
plt.ylabel('Number of Injuries')
plt.title('Number of Fear Injuries\nby Product Description')
fear.set_xticklabels(['Beds and Bedframes','Horseback Riding Equipment','Knives','Bicycles',\
             'Ceilings and Walls','Fireworks'])

#                                  NEW Jupyter Notebook Cell
#Plotting Fear injuries vs categories defined by me
dffear_at = pd.Series({'Spider (fake)' : textfind(dffear,'Notes','SPIDER')['age'].count(),
             'Horse': textfind(dffear,'Notes','\sHORSE|\sPONY\s')['age'].count(),
              'Dog': textfind(dffear,'Notes','\sDOG\s')['age'].count(),
              'Cat': textfind(dffear,'Notes','\sCAT')['age'].count(),
              'Friend': textfind(dffear,'Notes','\sFRIEND\s|\sFRIENDS\s')['age'].count(),
              'Dragonfly': textfind(dffear,'Notes','\sDRAGONFLY\s|\sDRAGON FLY')['age'].count(),
              'Cousin': textfind(dffear,'Notes','\sCOUSIN\s|\sCOUSINS\s')['age'].count()
             })

plt.xlabel('Category')
plt.ylabel('Number of Injuries')
plt.title('Number of Fear Injuries\nby Category')
dffear_at.sort_values(ascending=False).plot.bar()

#                                  NEW Jupyter Notebook Cell
#creating dfanger dataframe, for Anger injuries
dfanger = textfind(df1, 'Notes', '\sANGRY\s|\sANGER\s|\sMAD\s|FRUSTRATED|UPSET')[df1['age'] < 121]
len(dfanger)

#                                  NEW Jupyter Notebook Cell
#plotting histogram of Junk in the Trunk Injuries vs Age by sex
anger_M_plot = dfanger[dfanger.sex_descrip == 'MALE'].age
anger_F_plot =dfanger[dfanger.sex_descrip == 'FEMALE'].age
anger_m = plt.hist(anger_M_plot,alpha=0.5, bins = 10, color = 'blue',label='MALE')
anger_f = plt.hist(anger_F_plot,alpha=0.5, bins = 8,color = 'red',label='FEMALE')
plt.legend()
plt.title('Number of "Angry" Injuries \nby Age')
plt.xlabel('Age')
plt.ylabel('Number of Injuries')
plt.show

#creating and displaying df of Anger Injuries average age and percentage of 
#total injuries
anger_sort = {'CPSC Case #':['count'], 'age':['mean']}
anger_table = pd.DataFrame(dfanger.groupby('sex_descrip').agg(anger_sort))
anger_table['percentage'] = anger_table['CPSC Case #'].apply(lambda x: 100*x/float(x.sum()))
anger_table[['age','percentage']]

#                                  NEW Jupyter Notebook Cell
#Plotting Anger injuries vs categories defined by me
dfanger_at = pd.Series({'Mother' : textfind(dfanger,'Notes','\sMOM\s|\sMOTHER\s')['age'].count(),
             'Father': textfind(dfanger,'Notes','\sDAD\s|\sFATHER\s')['age'].count(),
              'Sibling': textfind(dfanger,'Notes','\sBROTHER\s|\sSISTER\s|\sBRO\s|\sSIS\s')['age'].count(),
              'Partner': textfind(dfanger,'Notes','\sGF\s|\sGIRLFRIEND\s|\sWIFE\s|\sHUSBAND\s|\sBOYFRIEND\s|\sBF\s')['age'].count(),
              'Friend': textfind(dfanger,'Notes','\sFRIEND\s')['age'].count(),
              'Teacher': textfind(dfanger,'Notes','\sTEACHER\s')['age'].count(),
              'In-law': textfind(dfanger,'Notes','\sIN LAW\s|\sIN LAWS\s|\sIN-LAW\s|\sIN-LAWS\s')['age'].count()
             })
plt.xlabel('Category')
plt.ylabel('Number of Injuries')
plt.title('Number of Anger Injuries\nby Category')
dfanger_at.sort_values(ascending=False).plot.bar()

#                                  NEW Jupyter Notebook Cell
#creating dfpunch dataframe, for punch injuries
dfpunch = textfind(dfanger,'Notes','(?<!WAS|GOT|GET)\sPUNCHED\s(?!BY\s|IN)|\sPUNCH\s(?!TO)')
dfkick = textfind(dfanger,'Notes','(?<!WAS|GOT|GET)\sKICKED\s(?!BY\s|IN)|\sKICK\s(?!TO)')

#                                  NEW Jupyter Notebook Cell
#Plotting Angry Punch injuries vs product1_descrip
punch = dfpunch.groupby('product1_descrip')['age'].count().sort_values(ascending=False).head(10).plot.bar()
plt.xlabel('Product Description')
plt.ylabel('Number of Injuries')
plt.title('Number of Angry Punch Injuries\nby Product Description') 
punch.set_xticklabels(['Ceilings and Walls','Windows','Doors','Mirrors',\
             'Refrigerators','Tables','Floors','Lockers', 'Televisions','Glass Doors'])

#                                  NEW Jupyter Notebook Cell
#plotting histogram of Angry Punch Injuries vs Age by sex
punch_M_plot = dfpunch[dfpunch.sex_descrip == 'MALE'].age
punch_F_plot =dfpunch[dfpunch.sex_descrip == 'FEMALE'].age
punch_m = plt.hist(punch_M_plot,alpha=0.5, bins = 10, color = 'blue',label='MALE')
punch_f = plt.hist(punch_F_plot,alpha=0.5, bins = 8,color = 'red',label='FEMALE')
plt.legend()
plt.title('Number of "Punch" Injuries \nby Age')
plt.xlabel('Age')
plt.ylabel('Number of Injuries')
plt.show

#creating and displaying df of Angry Punch Injuries average age and percentage of 
#total injuries
punch_sort = {'CPSC Case #':['count'], 'age':['mean']}
punch_table = pd.DataFrame(dfpunch.groupby('sex_descrip').agg(punch_sort))
punch_table['percentage'] = punch_table['CPSC Case #'].apply(lambda x: 100*x/float(x.sum()))
punch_table[['age','percentage']]

#                                  NEW Jupyter Notebook Cell
# summarizing number of injuries related to each emotion
dfemotions = pd.Series({'Fear' : len(dffear),
             'Excitement': len(dfexcite),
              'Sadness': len(dfsadness),
              'Happiness': 0,
              'Anger': len(dfanger)
             })


dfemotions.sort_values(ascending=False).plot.bar()
plt.title('Number of Injuries\nby Emotion')
plt.xlabel('Emotion')
plt.ylabel('Number of Injuries')

#                                  NEW Jupyter Notebook Cell

#load census data into dfcensus
dfcensus = pd.read_csv('Data/census.csv',header = 2)

#data cleansing
dfcensus['Male'] = dfcensus['Male'].apply(lambda x: re.sub("%","",str(x)))
dfcensus['Female'] = dfcensus['Female'].apply(lambda x: re.sub("%","",str(x)))
dfcensus = dfcensus.apply(lambda x: pd.to_numeric(x,errors="ignore"))

# Add census records with age 0 to age 1 line, to correspond with injury df1 convention
dfcensus['Male'].iloc[1] = dfcensus['Male'].iloc[1]+dfcensus['Male'].iloc[0]
dfcensus['Female'].iloc[1] = dfcensus['Female'].iloc[1]+dfcensus['Female'].iloc[0]

#                                  NEW Jupyter Notebook Cell
#create dfinjuries, which shows, by age, the percentage of injuroes for that age 
#in relation to the total injuries in the dataser 
M_injuries = 100*pd.Series(df1[df.sex_descrip == 'MALE'].groupby('age')['age'].count())/len(df1)
F_injuries = 100*pd.Series(df1[df.sex_descrip == 'FEMALE'].groupby('age')['age'].count())/len(df1)
dfinjuries = pd.concat([M_injuries, F_injuries], axis=1)
dfinjuries.columns = (['Male_Inj_Age','Female_Inj_Age'])

#                                  NEW Jupyter Notebook Cell
#create dfoverunder dataframe showing for each age: percentage of population and percentage
#of the injury dataset, for both males and females.
#overunder_plot will plot the "score" for each age by sex
dfoverunder = dfcensus.join(dfinjuries) 
dfoverunder = dfoverunder.drop(0)
dfoverunder['Male_Score'] = dfoverunder['Male_Inj_Age']/dfoverunder['Male']
dfoverunder['Female_Score'] = dfoverunder['Female_Inj_Age']/dfoverunder['Female']
overunder_plot = dfoverunder.plot('Age',['Male_Score','Female_Score'],color = ['blue','red'],label=['Male','Female'])
plt.plot([1, 100], [1, 1], color='g', linestyle='--', linewidth=2)
plt.legend(['Male','Female'])
plt.title('Prevalence of Injury vs. Proportion of US Population\nby Age')
plt.ylabel('Injury Prevalence Score')
plt.text(84,1.1,"Score = 1", color ='g')
plt.show


# JENJEN"S CODE
###############

#INJURIES BY MONTH
#reindex to have dates as index
indexed_time = df1.set_index('trmt_date')
indexed_time['Count'] = 1

#group dates by months
month_index = indexed_time['Count'].groupby(indexed_time.index.month).count()
month_graph = month_index.plot(title = "Injuries by month")
month_graph.set_xlabel("Month")
month_graph.set_ylabel("Number of injuries")



#INJURIES ON HOLIDAYS
#reindex to set time as index
time = df1.set_index('trmt_date')

#valentine's day injury count
valentines = time['2015-02-14']
valentines['Count'] = 1
val_count = valentines['Count'].count()

#valentines product related injuries males vs females
val_graphF = valentines[valentines.sex_descrip == 'FEMALE'].product1_descrip.value_counts().head(10)
val_graphF = pd.DataFrame(val_graphF)
val_graphF.columns = ['Injuries']

val_graphM = valentines[valentines.sex_descrip == 'MALE'].product1_descrip.value_counts().head(10)
val_graphM = pd.DataFrame(val_graphM)
val_graphM.columns = ['Injuries']
val_graphM


#christmas injury count
christmas = time['2015-12-24']
christmas['Count'] = 1
christmas_count = christmas['Count'].count()

#christmas product related injuries males vs females
xmas_graphF = christmas[christmas.sex_descrip == 'FEMALE'].product1_descrip.value_counts().head(10)
xmas_graphF = pd.DataFrame(xmas_graphF)
xmas_graphF.columns = ['Injuries']
xmas_graphF

xmas_graphM = christmas[christmas.sex_descrip == 'MALE'].product1_descrip.value_counts().head(10)
xmas_graphM = pd.DataFrame(xmas_graphM)
xmas_graphM.columns = ['Injuries']
xmas_graphM


#nye injury count
nye = time['2015-12-31']
nye['Count'] = 1
nye_count = nye['Count'].count()

#nye product related injuries males vs females
nye_graphF = nye[nye.sex_descrip == 'FEMALE'].product1_descrip.value_counts().head(10)
nye_graphF = pd.DataFrame(nye_graphF)
nye_graphF.columns = ['Injuries']
nye_graphF

nye_graphM = nye[nye.sex_descrip == 'MALE'].product1_descrip.value_counts().head(10)
nye_graphM = pd.DataFrame(nye_graphM)
nye_graphM.columns = ['Injuries']
nye_graphM


#halloween injury count
halloween = time['2015-10-31']
halloween['Count'] = 1
hallow_count = halloween['Count'].count()

#halloween product related injuries males vs females
hallow_graphF = halloween[halloween.sex_descrip == 'FEMALE'].product1_descrip.value_counts().head(10)
hallow_graphF = pd.DataFrame(hallow_graphF)
hallow_graphF.columns = ['Injuries']
hallow_graphF

hallow_graphM = halloween[halloween.sex_descrip == 'MALE'].product1_descrip.value_counts().head(10)
hallow_graphM = pd.DataFrame(hallow_graphM)
hallow_graphM.columns = ['Injuries']
hallow_graphM


#thanksgiving injury count
thanksgiving = time['2015-11-25']
thanksgiving['Count'] = 1
thanks_count = thanksgiving['Count'].count()

#thanksgiving product related injuries males vs females
thanks_graphF = thanksgiving[thanksgiving.sex_descrip == 'FEMALE'].product1_descrip.value_counts().head(10)
thanks_graphF = pd.DataFrame(thanks_graphF)
thanks_graphF.columns = ['Injuries']
thanks_graphF

thanks_graphM = thanksgiving[thanksgiving.sex_descrip == 'MALE'].product1_descrip.value_counts().head(10)
thanks_graphM = pd.DataFrame(thanks_graphM)
thanks_graphM.columns = ['Injuries']
thanks_graphM

#july4 injury count
independence = time['2015-7-4']
independence['Count'] = 1
indep_count = independence['Count'].count()


#july4 product related injuries males vs females
indep_graphF = independence[independence.sex_descrip == 'FEMALE'].product1_descrip.value_counts().head(10)
indep_graphF = pd.DataFrame(indep_graphF)
indep_graphF.columns = ['Injuries']
indep_graphF

indep_graphM = independence[independence.sex_descrip == 'MALE'].product1_descrip.value_counts().head(10)
indep_graphM = pd.DataFrame(indep_graphM)
indep_graphM.columns = ['Injuries']
indep_graphM


#Combined holiday graph
holiday_data = {'Holiday': ['Valentines','Fourth of July', 'Halloween', 'Thanksgiving', 'Christmas', 'NYE'],
               'Injuries': [val_count, indep_count, hallow_count, thanks_count, christmas_count, nye_count]}

df_holiday = pd.DataFrame(holiday_data)
holiday_graph = df_holiday.plot(kind = 'bar', x = 'Holiday', y = 'Injuries', title = "Injuries During the Holidays")
holiday_graph.set_ylabel("Number of Injuries")

#move legend outside of graph
holiday_graph.legend(loc = 'center left', bbox_to_anchor=(1, 0.5))



#DRUGS VS ALCOHOL VS plot

#DRUGS
#value counts by age containing cocaine/heroin
doped_af = df1[df1['Notes'].str.contains('COCAINE|HEROIN')]
age_doped = doped_af['age'].value_counts(sort = False)

#bin ages into groups of 10 years and sums value counts per bin
bins = np.arange(age_doped.index.min(), age_doped.index.max(), 10)
doped_age_groups = age_doped.groupby(pd.cut(age_doped.index, bins))
drug_bins = doped_age_groups.sum()
drug_graph = drug_bins.plot(kind = 'bar', title = "Injuries whilst on cocaine or heroin")

drug_graph.set_xlabel("Age range")
drug_graph.set_ylabel("Injury count")


#ALCOHOL
#value counts by age containing alcohol-related terms
drunk_af = df1[df1['Notes'].str.contains('DRUNK|ALCOHOL|ETOH|INTOXICATED')]
drunk_af = drunk_af['age'].value_counts(sort = False)

#bin ages
drunk_age_groups = drunk_af.groupby(pd.cut(drunk_af.index, bins))
drunk_bins = drunk_age_groups.sum()
drunk_graph = drunk_bins.plot(kind = 'bar', title = "Injuries whilst on Alcohol")

#for labeling bar graphs
drunk_graph.set_xlabel("Age range")
drunk_graph.set_ylabel("Injury count")


#MARIJUANA
#value counts by age containing marijuana-related terms
high_filter = df1[df1['Notes'].str.contains('HIGH|MARIJUANA')]

high_filter = high_filter[high_filter['Notes'].str.contains('HEELED|CARBON|MILAGE|HIGHWAY|TOO|FX') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('CHAIR|BP|FIVE|ANKLE|SHOT|SWING') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('HEELS|FLOWER') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('THIGH|POTATOES|POTHOLE|HOLE|SPILL|STOVE') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('BED|HIGHEST|HIGHER') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('BAR|HOT|FALL') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('SHELF') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('HEEL') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('STEPS') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('POWERED') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('STOOL') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('FT') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('FEET') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('UP') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('INTENSITY') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('HEEL') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('SCHOOL') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('SPEED') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('PRESSURE') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('CABINET') == False]
high_filter = high_filter[high_filter['Notes'].str.contains('JUMP') == False]
high_af = high_filter[high_filter['Notes'].str.contains('TOP') == False]

#checking filtered out notes
# pd.options.display.max_colwidth = 1000
# high_af['Notes']

#value counts by age containing high-related terms
high_af = high_af['age'].value_counts(sort = False)
high_age_groups = high_af.groupby(pd.cut(high_af.index, bins))
high_bins = high_age_groups.sum()
high_graph = high_bins.plot(kind = 'bar')

high_graph.set_title("Injuries whilst on Marijuana")
high_graph.set_xlabel("Age range")
high_graph.set_ylabel("Injury count")


#COMBINED ALCOHOL, DRUGS, AND MARIJUANA
df_influenced = pd.concat([drug_bins, high_bins, drunk_bins], axis = 1)
df_influenced.columns = ['Drugs', 'Marijuana', 'Alcohol']
influenced_graph = df_influenced.plot(kind = 'area')

influenced_graph.set_title("Injuries whilst on Drugs vs Marijuana vs Alcohol")
influenced_graph.set_xlabel("Age range")
influenced_graph.set_ylabel("Injury count")

#move legend outside of plot
influenced_graph.legend(loc = 'center left', bbox_to_anchor=(1, 0.5))

# PETER"S CODE
##############


# coding: utf-8

# In[ ]:

import csv 
import pandas as pd
import matplotlib.pyplot as plt
import re
get_ipython().magic('matplotlib inline')

with open('Data/2015.tsv','r') as tsv:
    data = [line.strip().split('\t') for line in tsv]
    
col_names = data[0]
df = pd.DataFrame(data, columns=col_names)
df = df[1:]

#open code_sex.csv and convert it to a DataFrame
with open('Data/code_sex.csv','r') as csv:
    sex_descrip = [line.strip().split(',') for line in csv]

sex_header = sex_descrip[0]
df_sex = pd.DataFrame(sex_descrip, columns=sex_header)
df_sex = df_sex[1:]
indexed_df_sex = df_sex.set_index('Code')

#open code_body_part.csv and convert it to a DataFrame
with open('Data/code_body_part.csv','r') as csv:
    body_part_descrip = [line.strip().split(',') for line in csv]

body_part_header = body_part_descrip[0]
df_body_part = pd.DataFrame(body_part_descrip, columns=body_part_header)
df_body_part = df_body_part[1:]
indexed_df_body_part = df_body_part.set_index('Code')

#open code_diagnosis.csv and convert it to a DataFrame
with open('Data/code_diagnosis.csv','r') as csv:
    diagnosis_descrip = [line.strip().split(',') for line in csv]

diagnosis_header = diagnosis_descrip[0]
df_diagnosis = pd.DataFrame(diagnosis_descrip, columns=diagnosis_header)
df_diagnosis = df_diagnosis[1:]
indexed_df_diagnosis = df_diagnosis.set_index('Code')

#open code_disposition.csv and convert it to a DataFrame
with open('Data/code_disposition.csv','r') as csv:
    disposition_descrip = [line.strip().split(',') for line in csv]

disposition_header = disposition_descrip[0]
df_disposition = pd.DataFrame(disposition_descrip, columns=disposition_header)
df_disposition = df_disposition[1:]
indexed_df_disposition = df_disposition.set_index('Code')

#open code_fire.csv and convert it to a DataFrame
with open('Data/code_fire.csv','r') as csv:
    fire_descrip = [line.strip().split(',') for line in csv]

fire_header = fire_descrip[0]
df_fire = pd.DataFrame(fire_descrip, columns=fire_header)
df_fire = df_fire[1:]
indexed_df_fire = df_fire.set_index('Code')

#open code_locale.csv and convert it to a DataFrame
with open('Data/code_locale.csv','r') as csv:
    locale_descrip = [line.strip().split(',') for line in csv]

locale_header = locale_descrip[0]
df_locale = pd.DataFrame(locale_descrip, columns=locale_header)
df_locale = df_locale[1:]
indexed_df_locale = df_locale.set_index('Code')

#open code_product.csv and convert it to a DataFrame
with open('Data/code_product.csv','r') as csv:
    product_descrip = [line.strip().split(',',1) for line in csv]

product_header = product_descrip[0]
df_product = pd.DataFrame(product_descrip, columns=product_header)
df_product = df_product[1:]
indexed_df_product = df_product.set_index('Code')

#open code_race.csv and convert it to a DataFrame
with open('Data/code_race.csv','r') as csv:
    race_descrip = [line.strip().split(',') for line in csv]

race_header = race_descrip[0]
df_race = pd.DataFrame(race_descrip, columns=race_header)
df_race = df_race[1:]
indexed_df_race = df_race.set_index('Code')

#merge all the codes
df['sex_descrip']=df.sex.map(indexed_df_sex.Description)
df['body_part_descrip']=df.body_part.map(indexed_df_body_part.Description)
df['diag_descrip']=df.diag.map(indexed_df_diagnosis.Description)
df['disposition_descrip']=df.disposition.map(indexed_df_disposition.Description)
df['fire_descrip']=df.fmv.map(indexed_df_fire.Description)
df['locale_descrip']=df.location.map(indexed_df_locale.Description)
df['product1_descrip']=df.prod1.map(indexed_df_product.Description)
df['product2_descrip']=df.prod2.map(indexed_df_product.Description)
df['race_descrip']=df.race.map(indexed_df_race.Description)

#combine the 2 narr fields into 1
df['Notes'] = df['narr1'].map(str) + df['narr2'].map(str)

df1 = df[['CPSC Case #', 
         'trmt_date', 
         'psu', 
         'weight', 
         'age', 
         'sex_descrip', 
         'race_descrip',
         'body_part_descrip', 
         'diag_descrip', 
         'disposition_descrip', 
         'fire_descrip', 
         'locale_descrip', 
         'product1_descrip', 
         'product2_descrip', 
         'Notes']]

#convert numerical columns to numeric data type
df1 = df1.apply(lambda x: pd.to_numeric(x,errors="ignore"))

#convert 'trmt_date' column to datetime type
df1['trmt_date'] = df1['trmt_date'].apply(lambda x: pd.to_datetime(x,format='%m/%d/%Y'))

#remove quotation marks from product1_desrip field
df1['product1_descrip'] = df1['product1_descrip'].apply(lambda x: re.sub('"','',str(x)))

def textfind(dataframe, field, string):
    """ Takes dataframe, field (column in the dataframe), and a string to search
    Allow for use of regular expressions.
    Returns a dataframe of the records where the string is found"""
    import re
    a = [dataframe.loc[i] for i in dataframe.index          if re.search(string, dataframe[field][i])]
    return pd.DataFrame(a)
    
def notereader(dataframe):
    """ Takes a dataframe that contains the 'Notes' field and prints it out in a
    readable fashion.
    Returns a dictionary of Index (integer): Note (string) pairs"""
    output_dict ={}
    for i in dataframe.index:           
        output_dict[i] = dataframe.Notes[i]
        print ("INDEX", i,"\n", dataframe.Notes[i],"\n")
    return output_dict

pd.options.display.max_colwidth = 1000


#Injuries by Body Part

body_part = df1['body_part_descrip'].value_counts().head(10).plot(kind = 'bar', legend = None, title = '2015 ER Injuries by Body Part')
body_part.set_xlabel('Body Part')
body_part.set_ylabel('Number of People')                                    
plt.show()

body_part_table = {'CPSC Case #':['count'], 'age':['median']}

body_part_table2 = df1.groupby('body_part_descrip').agg(body_part_table).sort_values([('CPSC Case #', 'count')], ascending=False).head(10)
body_part_table2

#Injuries on the Farm
farm_locale = df1[df1['locale_descrip'].str.contains('FARM')]
farm_table = {'CPSC Case #':['count'], 'age':['median']}
farm_table2 = farm_locale.groupby('product1_descrip').agg(farm_table).sort_values([('CPSC Case #', 'count')], ascending=False).head(10)

farm = farm_locale['product1_descrip'].value_counts().head(10).plot(kind = 'bar', legend = None, title = '2015 ER Injuries on the Farm')
farm.set_xlabel('Product')
farm.set_ylabel('Number of People')
plt.show()

farm_table2

#Injuries by Sport
sports_locale = df1[df1['locale_descrip'].str.contains('SPORT')]
sports_table = {'CPSC Case #':['count'], 'age':['median']}
sports_table2 = sports_locale.groupby('product1_descrip').agg(sports_table).sort_values([('CPSC Case #', 'count')], ascending=False).head(10)

sport = sports_locale['product1_descrip'].value_counts().head(10).plot(kind = 'bar', legend = None, title = '2015 ER Injuries by Sport')
sport.set_xlabel('Product')
sport.set_ylabel('Number of People')
plt.show()

sports_table2

#Injuries by Sport by top body parts
sports_locale = df1[df1['locale_descrip'].str.contains('SPORT')]
sports_table = {'CPSC Case #':['count'], 'age':['median']}
sports_table3 = sports_locale.groupby(['product1_descrip', 'body_part_descrip']).agg(sports_table).sort_values([('CPSC Case #', 'count')], ascending=False).head(10)
sports_table3

#Animal Injuries

dog_filter = df1[df1['Notes'].str.contains('DOG|PUPPY|ROTTWEILER|POODLE|GOLDEN RETRIEVER')]
cat_filter = df1[df1['Notes'].str.contains(' CAT |KITTEN')]
cat_filter = cat_filter[cat_filter['product1_descrip'].str.contains('FISHING') == False]
fish_filter = df1[df1['product1_descrip'].str.contains('FISHING') == True]
horse_filter = df1[df1['Notes'].str.contains('HORSE')]
chicken_filter = df1[df1['Notes'].str.contains('CHICKEN')]
chicken_filter = chicken_filter[chicken_filter['Notes'].str.contains('WIRE|DANCE|KNIFE|FRY') == False]
chicken_filter = chicken_filter[chicken_filter['product1_descrip'].str.contains('COOKWARE|KNIVES|REFRIGERATORS|HOT WATER|OVEN|TABLE') == False]
pig_filter = df1[df1['Notes'].str.contains(' PIG ')]
pig_filter = pig_filter[pig_filter['Notes'].str.contains('KNIFE|FRY') == False]
pig_filter = pig_filter[pig_filter['product1_descrip'].str.contains('COOKWARE|KNIVES|REFRIGERATORS|HOT WATER|OVEN|TABLE|TOYS|CHARCOAL') == False]
shark_filter = df1[df1['Notes'].str.contains('SHARK')]
shark_filter = shark_filter[shark_filter['Notes'].str.contains('PLAYING') == False]
sheep_filter = df1[df1['Notes'].str.contains(' SHEEP ')]
cow_filter = df1[df1['Notes'].str.contains(' COW | BULL |CATTLE')]
cow_filter = cow_filter[cow_filter['product1_descrip'].str.contains('ATTRACTIONS|TOYS') == False]
cow_filter = cow_filter[cow_filter['Notes'].str.contains('PIT|DOG') == False]
spider_filter = df1[df1['Notes'].str.contains('SPIDER')]
snake_filter = df1[df1['Notes'].str.contains('SNAKE')]
snake_filter = snake_filter[snake_filter['product1_descrip'].str.contains('DRAIN SNAKES') == False]
snake_filter = snake_filter[snake_filter['Notes'].str.contains('PLUMBING') == False]
bird_filter = df1[df1['Notes'].str.contains('BIRD')]

animal_injuries = [['Dog', len(dog_filter)], ['Cat', len(cat_filter)], ['Fish', len(fish_filter)], ['Horse', len(horse_filter)],
                  ['Chicken', len(chicken_filter)], ['Pig', len(pig_filter)], ['Shark', len(shark_filter)], ['Sheep', len(sheep_filter)],
                  ['Cows and Bulls', len(cow_filter)], ['Snake', len(snake_filter)], ['Bird', len(bird_filter)]]

animals = pd.DataFrame(animal_injuries, columns=('Animals', 'Count')).sort_values('Count', ascending = False)
animals_graph = animals['Count'].plot(kind = 'bar', legend = None, title = '2015 ER Injuries by Animal')
animals_graph.set_xticklabels(animals['Animals'])

plt.show()

animal_injuries







