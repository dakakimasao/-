from pandas import DataFrame
import pandas as pd
import plotly.express as px
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=18
matplotlib.rcParams['axes.unicode_minus']=False

def msg(x:DataFrame,home,away):
    x.columns = x.columns.str.strip()

    homecols = ['HS', 'HST', 'HF', 'HC', 'HY']
    awaycols = ['AS', 'AST', 'AF', 'AC', 'AY']
    theta=['슈팅','유효슈팅','파울','코너킥 수','옐로카드 횟수']

    homedata = x[x['HomeTeam'] == home]
    awaydata = x[x['AwayTeam'] == away]

    dataa=homedata[homecols].mean().fillna(0).round(0).astype(int)
    datab=awaydata[awaycols].mean().fillna(0).round(0).astype(int)

    dataa=pd.DataFrame({'Category': theta, 'Value': dataa.values, 'Team': 'Home Team 평균'})
    datab   = pd.DataFrame({'Category': theta, 'Value': datab.values, 'Team': 'Away Team 평균'})

    df=pd.concat([dataa,datab],ignore_index=True)

    fig=px.line_polar(df,r='Value',theta='Category',color='Team',line_close=True,title=f'{home}VS{away} 팀 의 스탯 비교')
    fig.update_traces(fill='toself',opacity=0.3)

    fig.show()