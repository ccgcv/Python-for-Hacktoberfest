#!/usr/bin/env python
# coding: utf-8

# <h2>Importing useful Libraries</h2>

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot
from plotly.subplots import make_subplots

import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


import warnings
warnings.filterwarnings("ignore")


# <h2> Reading Given Data </h2>

# In[2]:


df_matches = pd.read_csv('/kaggle/input/ipl/matches.csv')
df_deliveries = pd.read_csv('/kaggle/input/ipl/deliveries.csv')


# <h3> Understanding The Given Data </h3>

# <h4> Matches Dataframe </h4>

# In[3]:


df_matches.head()


# In[4]:


#checking info
df_matches.info()


# In[5]:


#describing the data
df_matches.describe()


# In[6]:


#visuvalising the  null values
plt.figure(figsize=(10,8))
sns.heatmap(df_matches.isnull())
plt.title('Heatmap for checking Null Values')
plt.show()


# In[7]:


# checking for any NaN values in rows
df_matches.isna().any()


# In[8]:


#getting sum of null values
df_matches.isnull().sum().sort_values(ascending=False)


# In[9]:


# get the number of missing data points per column
missing_values_count = df_matches.isnull().sum()
total_cells = np.product(df_matches.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing

percent_missing = (total_missing/total_cells) * 100
print("Percentage of missing : {}".format(percent_missing))


# <h4>Deliveries Data Frame </h4>

# In[10]:


#checking head
df_deliveries.head()


# In[11]:


#checking info
df_deliveries.info()


# In[12]:


df_deliveries.describe()


# In[13]:


#visuvalising the  null values
plt.figure(figsize=(10,8))
sns.heatmap(df_deliveries.isnull())
plt.title('Heatmap for checking Null Values')
plt.show()


# In[14]:


# checking for any NaN values
df_deliveries.isna().any()


# In[15]:


#getting sum of null values
df_deliveries.isnull().sum().sort_values(ascending=False)


# In[16]:


# get the number of missing data points per column
missing_values_count = df_deliveries.isnull().sum()
total_cells = np.product(df_deliveries.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing

percent_missing = (total_missing/total_cells) * 100
print("Percentage of missing : {}".format(percent_missing))


# <h2>Checking variables behaviour</h2>

# <h4> checking Teams </h4>

# In[17]:


df_matches['team1'].value_counts()


# In[18]:


df_matches['team2'].value_counts()


# In[19]:


px.bar(df_matches['team1'].value_counts(),template = "plotly_dark")


# In[20]:


px.bar(df_matches['team2'].value_counts(),template = "ggplot2")


# **NOTE** : Rising Pune Supergiant and Rising Pune Supergiants are Same </br>
# so Replacing Rising Pune Supergiant with Rising Pune Supergiants (two teams are same)

# checking all countries columns in data frames

# In[21]:


df_matches.columns


# In[22]:


df_deliveries.columns


# In[23]:


df_matches['team1'].replace({"Rising Pune Supergiant":"Rising Pune Supergiants"},inplace = True)
df_matches['team2'].replace({"Rising Pune Supergiant":"Rising Pune Supergiants"},inplace = True)

df_matches['winner'].replace({"Rising Pune Supergiant":"Rising Pune Supergiants"},inplace = True)
df_matches['toss_winner'].replace({"Rising Pune Supergiant":"Rising Pune Supergiants"},inplace = True)

df_deliveries['batting_team'].replace({"Rising Pune Supergiant":"Rising Pune Supergiants"},inplace = True)
df_deliveries['bowling_team'].replace({"Rising Pune Supergiant":"Rising Pune Supergiants"},inplace = True)


# <h2></h2>

# <h4> Checking Seasons : </h4>

# In[24]:


df_matches['season'].value_counts()


# The Given Data is about 10 seasons

# In[25]:


px.bar(df_matches['season'].value_counts(),template = "ggplot2")


# <h4> Checking Venues : </h4>

# In[26]:


df_matches['venue'].value_counts()


# In[27]:


#method for getting values for pie chart
def pie_chart_values(df,col):
    vals = []
    nam = []
    t = df[col].values
    t = set(t)
    nam = list(t)
    for i in nam:
        x = df[df[col]==i][col].count()
        vals.append(x)
        
    return vals,nam


# In[28]:


#plot code
values , names = pie_chart_values(df_matches,'venue')
fig = px.pie(data_frame=df_matches,names= names,values = values,
       title='Number of matches in different venues')
fig.update_traces(hovertemplate='venue: %{label}'+'<br>matches: %{value}')
fig.show()


# <h4> Now let us see how venues are changing every year </h4>

# In[29]:


#method for getting venues year wise
def year_wise_venues(df,col,year):
    vals = []
    nams = []
    t = df[df['season']==year][col].values
    t = set(t)
    nam = list(t)
    for i in nam:
        x = df[(df[col]==i) & (df['season'] == year)][col].count()
        vals.append(x)
        
    return vals,nam


# In[30]:


for i in range(2008,2018):
    values,names = year_wise_venues(df_matches,'venue',i)
    graph_title = "Number of matches in different venues in year {}".format(i)
    fig = px.pie(data_frame=df_matches,names=names,values = values,
       title = graph_title,template='ggplot2')
    fig.update_traces(hovertemplate = 'venue: %{label}'+'<br>matches: %{value}')
    fig.show()


# <h4>let us add venue section for deliveries data frame so that we can get runs and wickets of players in different venues</h4>

# In[31]:


def venue(id):
    return(df_matches[df_matches['id'] == id]['venue'].values[0])

df_deliveries['venue'] = df_deliveries['match_id'].apply(venue)


# <h2></h2>

# <h4>Checking Number of matches every season </h4>

# In[32]:


years = list(range(2008,2018))
years_count = [df_matches[df_matches['season']==x]['season'].count() for x in years]


# In[33]:


#same plot using seaborn
sns.set(style='darkgrid',rc = {'figure.figsize':(15,8)})
sns.countplot(data=df_matches,x= 'season').set(title = 'year wise matches')


# In[34]:


fig = px.bar(x=years,y = years_count,template='plotly_dark',title='Number of matches Every year')
fig.update_xaxes(title='years')
fig.update_yaxes(title='Number of matches')
fig.update_traces(hovertemplate='Num of matches:%{y}'+'<br>year: %{x}',marker_color = 'white' )
fig.show()


# <h4>In 2013 we have more Number of matches so let us check about Number of teams every season</h4></br>
# <h4> Checking Number of Teams (in Each Season) </h4>

# In[35]:


#method  for getting number of teams each year
def number_of_teams(y):
    t= df_matches[df_matches['season'] == y]['team1'].values
    return(len(set(t)))
coun = [number_of_teams(x) for x in years]


# In[36]:


#plot using plotly
fig = px.bar(x=years,y = coun,title='Number of teams in Each Season',template='simple_white')
fig.update_xaxes(title='years')
fig.update_yaxes(title='number of teams')
fig.update_traces(hovertemplate='Num of teams:%{y}'+'<br>year: %{x}',marker_color = 'skyblue' )
fig.show()


# <h4> In 2011 we have More Number of teams </h4>

# In[37]:


df_matches[df_matches['season'] == 2011]['team1'].value_counts()


# In[38]:


df_matches[df_matches['season'] == 2013]['team1'].value_counts()


# <h4> Now let us check most succesful teams in 10 seasons</h4>

# In[39]:


df_matches['winner'].value_counts()[:5]


# In[40]:


fig = px.bar(df_matches, x=df_matches['winner'].value_counts().keys()[:5],
             y=df_matches['winner'].value_counts()[:5],
             color=df_matches['winner'].value_counts().keys()[:5],
             title='Top five most succesful Teams',
             template = "ggplot2"
                    )
fig.update_xaxes(title = "Team Names")
fig.update_yaxes(title="Number of Wins")
fig.update_traces(hovertemplate='Num of wins:%{y}'+'<br>Team: %{x}' )
fig.show()


# <h4> Let us check Result types (tie or match cancelled) </h4> </br>
# <h4> Checking Reults tpye : </h4>

# In[41]:


df_matches['result'].value_counts()


# In[42]:


fig = px.pie(values=df_matches['result'].value_counts(),
             names=df_matches['result'].value_counts().keys(),
             title='Results type in all seasons')
fig.update_traces(hovertemplate = 'Type: %{label}'+'<br>matches: %{value}')
fig.show()


# most of the matches have normal resluts 

# <h4> Now let us check about Number of players </h4> </br>
# <h4> checking players:</h4>

# In[43]:


df_deliveries['batsman'].nunique()


# In[44]:


df_deliveries['bowler'].nunique()


# Now let us find total Number of players

# In[45]:


v1 = list(df_deliveries['batsman'].values)
v2 = list(df_deliveries['non_striker'].values)
v3 = list(df_deliveries['bowler'].values)
v = v1+v2+v3
v = set(v)
print("Number of players : {}".format(len(v)))


# <h4> let us check players who has more number of player of match </h4>

# In[46]:


df_matches['player_of_match'].value_counts()[:10]


# player with more number of player_of_matches is valuable  

# In[47]:


#most valuable player plot
fig = px.bar(df_matches, x=df_matches['player_of_match'].value_counts().keys()[:10],
             y=df_matches['player_of_match'].value_counts()[:10],
             color=df_matches['player_of_match'].value_counts().keys()[:10],
            title='Ten most valuable players',
            template='plotly_dark')
fig.update_xaxes(title = "player Names")
fig.update_yaxes(title="Number of player of the matches")
fig.update_traces(hovertemplate='Num of poms:%{y}'+'<br>player: %{x}' )
fig.show()


# <h4> let us see Number of different umpiers </h4>

# In[48]:


df_matches['umpire1'].value_counts()


# In[49]:


df_matches['umpire2'].value_counts()


# In[50]:


df_matches['umpire3'].value_counts()


# umpire 3 has null values completly

# <h4> Now let us try to create a Summary for every team in a particular season </h4>
# 
# <h2>Team Summary Function for getting all details about team in a particular Season</h2>

# In[51]:


def team_summary(team,year):
    df_team = pd.DataFrame()
    
    df_team['team1'] = df_matches[df_matches['season'] == year]['team1']
    df_team['team2'] = df_matches[df_matches['season'] == year]['team2']
    
    df_team['winner'] = df_matches[df_matches['season'] == year]['winner']
    df_team['venue'] = df_matches[df_matches['season']==year]['venue']
    
    df_team['toss_winner'] = df_matches[df_matches['season'] == year]['toss_winner']
    df_team['toss_decision'] = df_matches[df_matches['season'] == year]['toss_decision']
    
    df = df_team[(df_team['team1']== team) | (df_team['team2']== team)]
    
    df['team'] = [team]*len(df)
    
    li = []
    
    
    for i in range(len(df)):
        if df.iloc[i]['team1']==team:
            li.append(df.iloc[i]['team2'])
        else:
            li.append(df.iloc[i]['team1'])
    df['oponent team'] = li
    
    
    li = []
    count = 0
    
    
    for i in range(len(df)):
        if df.iloc[i]['winner'] == team:
            li.append(team)
            count+=1
        else:
            li.append('team')
    df['winners'] = li
    
    
    df.drop(['team1','team2'],axis=1,inplace = True)
    
    
    print("Team Summary :")
    print("\n")
   
    print("Team Name:{}".format(team))
    print("\n")
    
    print("year : {}".format(year))
    print("\n")
    
    print("Number of matches {}".format(len(df)))
    print("\n")
    
    print("Number of wins : {}".format(count))
    print("\n")
    
    print("winning percentage : {}".format((count/len(df)*100)))
    print("\n")
    
    print("Differnt venues for {} in {}".format(team,year))
    print("\n")
    
    #plot for venues
    values,names = pie_chart_values(df,'venue')
    fig = px.pie(data_frame=df_matches,names=names,values = values,title='Number of matches in different venues',template='plotly_dark')
    fig.update_traces(hovertemplate = 'venue: %{label}'+'<br>matches: %{value}')
    fig.show()
    
    print("\n")
    print("Toss wins for {} in {}:".format(team,year))
    print("\n")
    
    #plot for toss winners
    values,names = pie_chart_values(df,'toss_winner')
    fig = px.pie(data_frame=df_matches,names=names,values = values,title='toss_winners %',template='ggplot2')
    fig.update_traces(hovertemplate = 'Team: %{label}'+'<br>matches: %{value}')
    fig.show()
    
    print("\n")
    print("Toss descisons for {} in {}:".format(team,year))
    print("\n")
    
    
    #plot for toss descion
    values,names = pie_chart_values(df,'toss_decision')
    fig = px.pie(data_frame=df_matches,names=names,values = values,title='toss_descion %',template='simple_white')
    fig.update_traces(hovertemplate = 'Type: %{label}'+'<br>matches: %{value}')
    fig.show()
    
    print("\n") 
    print("wins for {} in {}:".format(team,year))
    print("\n")
    
    #plot for number of wins aganist different teams      
    fig = px.bar(data_frame=df,x='oponent team',color='winners',
                 barmode='group',
                 template='plotly_dark',
                 title="Number of wins aganist other teams")
    fig.show() 


# In[52]:


team_summary('Mumbai Indians',2008)


# Now let us see Chennai Super kings team in season 2014

# In[53]:


team_summary('Chennai Super Kings',2014)


# Royal Challengers Bangalore in 2017

# In[54]:


team_summary('Royal Challengers Bangalore',2017)


# Mumbai Indians In 2017

# In[55]:


team_summary('Mumbai Indians',2017)


# <h4>Now let us try to create a player profile class where we can get everything about player </h4>

#  For creating player profile we need player scores and wickets aganist each team and in each venue
# ,now let us create data frames for getting information 
# <h2> creating Data frames</h2>

# In[56]:


def number_of_wickets(name):
    li = list(df_deliveries[(df_deliveries['bowler']==name)]['dismissal_kind'])
    wickets = 0
    for i in li:
        if i in['caught','bowled','lbw','stumped','caught and bowled']:
            wickets+=1
    return wickets


# <h4> Data Frame for getting runs aganist each team </h4>

# In[57]:


player_scores =  pd.DataFrame()


li = []
#getting players names
li1 = list(df_deliveries['batsman'].values)
li2 = list(df_deliveries['non_striker'].values)
li3 = list(df_deliveries['bowler'].values)
li = li1+li2+li3
names = set(li)


player_scores['Names'] = list(names)


li=[]
#getting team names
li1 = []
li2 = []
li1 = list(df_matches['team1'].values)
li2 = list(df_matches['team2'].values)
li = li1+li2
li = set(li)
teams = list(li)


for i in range(len(teams)):
    player_scores.insert(i+1, teams[i], [0]*len(player_scores), True)

    
player_scores = player_scores.set_index('Names')


for i in player_scores.index:
    for j in player_scores.columns:
        s = sum(df_deliveries[(df_deliveries['batsman']==i) & (df_deliveries['bowling_team'] == j)]['batsman_runs'])
        player_scores.loc[i,j] = s



player_scores.head()


# <h4> Data Frame for getting runs in each venue </h4>

# In[58]:


player_scores_venues = pd.DataFrame()

#getting venues
venues = set(df_matches['venue'])
venues = list(venues)

player_scores_venues['Names'] = list(names)

for i in range(len(venues)):
    player_scores_venues.insert(i+1, venues[i], [0]*len(player_scores_venues), True)



player_scores_venues = player_scores_venues.set_index('Names')


for i in player_scores_venues.index:
    for j in player_scores_venues.columns:
        s = sum(df_deliveries[(df_deliveries['batsman']==i) & (df_deliveries['venue'] == j)]['batsman_runs'])
        player_scores_venues.loc[i,j] = s


player_scores_venues.head()


# <h4>Data Frame for getting wickets aganist each team</h4>

# wickets only counts when it is bowled,caught,lbw,stumped and caught and bowled

# In[59]:


player_wickets = pd.DataFrame()

player_wickets['Names'] = list(names)

for i in range(13):
    player_wickets.insert(i+1, teams[i], [0]*len(player_scores), True)
    
    
player_wickets = player_wickets.set_index('Names')


for i in player_scores.index:
    for j in player_scores.columns:
        wickets = 0
        s = list(df_deliveries[(df_deliveries['bowler']==i) & (df_deliveries['batting_team'] == j)]['dismissal_kind'])
        for k in s:
            if k in['caught','bowled','lbw','stumped','caught and bowled']:
                wickets+=1
        player_wickets.loc[i,j] = wickets


player_wickets.head()


# <h4> Data Frame for getting wickets in  each venue </h4>

# In[60]:


player_wickets_venues = pd.DataFrame()

player_wickets_venues['Names'] = list(names)

for i in range(len(venues)):
    player_wickets_venues.insert(i+1, venues[i], [0]*len(player_wickets_venues), True)
    
player_wickets_venues = player_wickets_venues.set_index('Names')

for i in player_wickets_venues.index:
    for j in player_wickets_venues.columns:
        wickets = 0
        s = list(df_deliveries[(df_deliveries['bowler']==i) & (df_deliveries['venue'] == j)]['dismissal_kind'])
        for k in s:
            if k in['caught','bowled','lbw','stumped','caught and bowled']:
                wickets+=1
        player_wickets_venues.loc[i,j] = wickets

        
player_wickets_venues.head()


# Let us create some plots using created Data frames

# <h4>plots using created Data Frames</h4>

# In[61]:


li = []
for i in player_scores.index:
    li.append(sum(player_scores.loc[i]))
player_scores["total_runs"] = li
player_scores = player_scores.sort_values(by = 'total_runs',ascending=False)


# In[62]:


fig = px.bar(data_frame=player_scores,x = player_scores.index[:11],
             y = player_scores['total_runs'][:11],
             title = "Top 10 highest runs",
            template='ggplot2')
fig.update_yaxes(title = "Runs")
fig.update_xaxes(title = "player Nmaes")
fig.update_traces(marker_color = "brown")
fig.update_traces(hovertemplate = 'Player: %{x}'+'<br> Runs: %{y}')
fig.show()


# In[63]:


player_scores.drop('total_runs',axis = 1,inplace = True)


# In[64]:


li = []
for i in player_wickets.index:
    li.append(sum(player_wickets.loc[i]))
player_wickets["total_wickets"] = li
player_wickets = player_wickets.sort_values(by = 'total_wickets',ascending=False)


# In[65]:


fig = px.bar(data_frame=player_wickets,x = player_wickets.index[:11],
             y = player_wickets['total_wickets'][:11],
             title = "Top 10 wicket takers",
            template='ggplot2')
fig.update_yaxes(title = "Runs")
fig.update_xaxes(title = "player Nmaes")
fig.update_traces(marker_color = "blue")
fig.update_traces(hovertemplate = 'Player: %{x}'+'<br> wickets: %{y}')
fig.show()


# In[66]:


player_wickets.drop('total_wickets',axis = 1,inplace = True)


# <h2>Creating Class for getting all plots of player profile </h2>

# In[67]:


class player_stats:
    
    def __init__(self,name):
        self.name = name
        self.total_runs = sum(df_deliveries[df_deliveries['batsman']== self.name]['batsman_runs'])
        self.total_wickets = number_of_wickets(self.name)
        
    def player_information(self):
        print("Name : {}".format(self.name))
        print("Total runs {}".format(self.total_runs))
        print("TOtal wickets :{}".format(self.total_wickets))
    
    def player_runs(self):
        title = "{} runs ".format(self.name)
        sns.set(style='darkgrid',rc = {'figure.figsize':(15,8)})
        sns.countplot(df_deliveries[df_deliveries['batsman']==self.name]['batsman_runs']).set(title = title)
    
    def player_scatter_runs(self):
        title = "{} runs ".format(self.name)
        fig = px.scatter(df_deliveries[df_deliveries['batsman']==self.name]['batsman_runs'],template='ggplot2',title=title)
        fig.update_xaxes(title = "count")
        fig.update_yaxes(title = "Index")
        fig.update_traces(marker_color = 'black')
        fig.show()
    
    def player_dismmisals(self):
        title = "Dissmisal Types of {}".format(self.name)
        (df_deliveries[df_deliveries['batsman']==self.name]['dismissal_kind']).iplot(kind = "histogram",title = title,
                                                                             xTitle="Dismissal types",yTitle="count",color = "red")
    def super_over_runs(self):
        title = "Super over Runs of {}".format(self.name)
        sns.set(style='darkgrid',rc = {'figure.figsize':(15,8)})
        sns.countplot(df_deliveries[(df_deliveries['batsman']==self.name) & (df_deliveries['is_super_over']==1)]['batsman_runs']).set(title = title)
    
    def player_scores_innings1(self):
        title = "{} Runs in innings 1 ".format(self.name)
        sns.set(style='darkgrid',rc = {'figure.figsize':(15,8)})
        sns.countplot(df_deliveries[(df_deliveries['batsman']==self.name) & (df_deliveries['inning']==1)]['batsman_runs']).set(title = title)
    
    def player_scores_innings2(self):
        title = "{} Runs in innings 2".format(self.name)
        sns.set(style='darkgrid',rc = {'figure.figsize':(15,8)})
        sns.countplot(df_deliveries[(df_deliveries['batsman']==self.name) & (df_deliveries['inning']==1)]['batsman_runs']).set(title = title)
    
        
    def player_wicket_types(self):
        title = "{}wicket types".format(self.name)
        (df_deliveries[(df_deliveries['bowler']==self.name)]['dismissal_kind']).iplot(kind='histogram',xTitle = "wicket type",
                                                                             yTitle="number of wickets",
                                                                             title = title,
                                                                             color = "black")
    def player_runs_given(self):
        title = "Runs given by {}".format(self.name)
        (df_deliveries[(df_deliveries['bowler']==self.name)]['total_runs']).iplot(kind="histogram",title = title,xTitle="Runs types",yTitle="count",
                                                                         color = "skyblue")
    
    def player_extra_runs_given(self):
        title = "extra _runs _given by {}".format(self.name)
        sns.set(style='darkgrid',rc = {'figure.figsize':(15,8)})
        sns.countplot(df_deliveries[(df_deliveries['bowler']==self.name)]['extra_runs']).set(title = title)
        
    def team_wise_runs(self):
        title = "{} runs aganist other teams".format(self.name)
        fig = px.bar(x = teams ,y = player_scores.loc[self.name].values,template = "ggplot2",title = title)
        fig.update_xaxes(title="Teams")
        fig.update_yaxes(title='Runs')
        fig.update_traces(hovertemplate = 'Team: %{x}'+'<br> Runs: %{y}')
        fig.show()
    
    def venue_wise_runs(self):
        title = "{} runs in different venues".format(self.name)
        fig = px.bar(x = venues ,y =player_scores_venues.loc[self.name].values,template = "plotly_dark",title = title)
        fig.update_xaxes(title="Venues")
        fig.update_yaxes(title='Runs')
        fig.update_traces(hovertemplate = 'venue: %{x}'+'<br> Runs: %{y}')
        fig.show()
    
    def team_wise_wickets(self):
        title = "{} wickets aganist other teams".format(self.name)
        fig = px.bar(x = teams ,y =player_wickets.loc[self.name].values,template = "ggplot2",title = title)
        fig.update_xaxes(title = "Teams")
        fig.update_yaxes(title = "Wickets")
        fig.update_traces(hovertemplate = 'Team: %{x}'+'<br> Wickets: %{y}')
        fig.show()
        
    def venue_wise_wickets(self):
        title = "{} wickets in different venues".format(self.name)
        fig = px.bar(x = venues ,y =player_wickets_venues.loc[self.name].values,template = "plotly_dark",title = title)
        fig.update_xaxes(title = "venues")
        fig.update_yaxes(title = "Wickets")
        fig.update_traces(hovertemplate = 'venue : %{x}'+'<br> Wickets : %{y}')
        fig.show()
        
    def box_team_wise_scores(self):
        for i in teams:
            fig = px.box(df_deliveries[(df_deliveries['batsman'] == self.name) & (df_deliveries['bowling_team']==i)]['batsman_runs'],template = "ggplot2",)
            fig.update_xaxes(title = "runs aganist {}".format(i))
            fig.update_yaxes(title = self.name)
            fig.show()
            print("\n")
            
            
    def box_venue_wise_scores(self):
        for i in venues:
            fig = px.box(df_deliveries[(df_deliveries['batsman'] == self.name) & (df_deliveries['venue']==i)]['batsman_runs'],template = "plotly_dark",)
            fig.update_xaxes(title = "runs in {}".format(i))
            fig.update_yaxes(title = self.name)
            fig.show()
            print("\n")
            
    def violin_team_wise_scores(self):
        for i in teams:
            fig = px.violin(df_deliveries[(df_deliveries['batsman'] == self.name) & (df_deliveries['bowling_team']==i)]['batsman_runs'],template = "ggplot2",)
            fig.update_xaxes(title = "runs aganist {}".format(i))
            fig.update_yaxes(title = self.name)
            fig.show()
            print("\n")
            
    def violin_venue_wise_scores(self):
        for i in venues:
            fig = px.violin(df_deliveries[(df_deliveries['batsman'] == self.name) & (df_deliveries['venue']==i)]['batsman_runs'],template = "plotly_dark")
            fig.update_xaxes(title = "runs in {}".format(i))
            fig.update_yaxes(title = self.name)
            fig.show()
            print("\n")
            
        
        
        


# In[68]:


p = player_stats("V Kohli")


# <h4> Player information </h4>

# In[69]:


p.player_information()


# <h4> Player runs (different runs: singles,doubles...) </h4>

# In[70]:


p.player_runs()


# <h4> Player Runs in total seasons </h4>

# In[71]:


p.player_scatter_runs()


# <h4> count for different type of dismmisals in all seasons </h4>

# In[72]:


p.player_dismmisals()


# <h4> players super over runs (if played super over) </h4>

# In[73]:


p.super_over_runs()


# <h4> Player scores in innings 1 </h4>

# In[74]:


p.player_scores_innings1()


# <h4> Player scores in innings 2 </h4>

# In[75]:


p.player_scores_innings2()


# <h4> Player's Number of different wickets </h4>

# In[76]:


p.player_wicket_types()


# <h4> Number of runs given Player </h4>

# In[77]:


p.player_runs_given()


# <h4> Number of extra runs given Player </h4>

# In[78]:


p.player_extra_runs_given()


# <h4> player runs aganist other teams </h4>

# In[79]:


p.team_wise_runs()


# for getting clear understanding about players scores aganist each team 

# In[80]:


p.box_team_wise_scores()


# In[81]:


p.violin_team_wise_scores()


# <h4> player runs in different venues </h4>

# In[82]:


p.venue_wise_runs()


# for getting clear understanding about players runs in different venues

# In[83]:


p.box_venue_wise_scores()


# In[84]:


p.violin_venue_wise_scores()


# <h4> player wickets aganist other teams </h4>

# In[85]:


p.team_wise_wickets()


# <h4> player wickets in different venues</h4>

# In[86]:


p.venue_wise_wickets()


# <h4> Now let us see the Hardik pandya stats </h4>

# In[87]:


h = player_stats('HH Pandya')


# In[88]:


h.player_information()


# In[89]:


h.player_runs()


# In[90]:


h.player_wicket_types()


# In[91]:


h.player_scores_innings1()


# In[92]:


h.player_scores_innings2()


# In[93]:


h.player_dismmisals()


# In[94]:


h.player_runs_given()


# In[95]:


h.player_extra_runs_given()


# In[96]:


h.team_wise_runs()


# In[97]:


h.venue_wise_runs()


# In[98]:


h.team_wise_wickets()


# In[99]:


h.venue_wise_wickets()

