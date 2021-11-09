import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd 
import csv 
df=pd.read_csv("StudentsPerformance.csv")
result=df["reading score"]
mean=sum(result)/len(result)
sd=statistics.stdev(result)
median=statistics.median(result)
mode=statistics.mode(result)
print(mean)
print(sd)
print(mode)
print(median)
sd1start,sd1end=mean-sd, mean+sd
sd2start,sd2end=mean-(2*sd), mean+(2*sd)
sd3start,sd3end=mean-(3*sd), mean+(3*sd)
fig=ff.create_distplot([result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1start"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1end"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2start"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2end"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.17],mode="lines",name="sd3start"))
fig.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.17],mode="lines",name="sd3end"))
fig.show()
listwwithinsd1=[r for r in result if r>sd1start and r< sd1end]
listwwithinsd2=[r for r in result if r>sd2start and r< sd2end]
listwwithinsd3=[r for r in result if r>sd3start and r< sd3end]
print("% of data within sd1",str(len(listwwithinsd1)*100/len(result)))
print("% of data within sd2",str(len(listwwithinsd2)*100/len(result)))
print("% of data within sd3",str(len(listwwithinsd3)*100/len(result)))