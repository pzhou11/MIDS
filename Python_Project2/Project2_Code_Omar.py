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





