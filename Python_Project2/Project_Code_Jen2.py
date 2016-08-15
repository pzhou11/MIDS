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
