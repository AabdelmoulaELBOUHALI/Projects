from google.colab import files
uploaded= files.upload()
!pip install -q pulp
import pandas as pd
import pulp
from pandas import ExcelWriter
from pandas import ExcelFile
Param= pd.read_excel('MineScheduling_smallDataSet.xlsx',sheet_name=0)
Job= pd.read_excel('MineScheduling_smallDataSet.xlsx',sheet_name=1)
JobMachine= pd.read_excel('MineScheduling_smallDataSet.xlsx',sheet_name=2)
Switching= pd.read_excel('MineScheduling_smallDataSet.xlsx',sheet_name=3)
is_over={}
start={}
for j in range(len(Job.index)):
  over='over'+str(j+1)
  s='start'+str(j+1)
  is_over[over]=pulp.LpVariable(over,cat='Binary')
  start[s]= pulp.LpVariable(s,lowBound=0,upBound= Param.loc[Param.index[0],Param.columns[0]],cat='Continuous')
allocation={}
for j in range (len(Job.index)):
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      allocation[x]= pulp.LpVariable(x,cat='Binary')
is_first={}
for j in range (len(Job.index)):
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='is_first'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      is_first[x]= pulp.LpVariable(x,cat='Binary')
is_Successory={}
for j1 in range(len(Job.index)):
  for j2 in range (len(Job.index)):
    if j1!=j2:
      mj1 = set()
      mj2 = set()
      for i in range(len(JobMachine.index)):
        if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j1+1):
          mj1.add(JobMachine.loc[JobMachine.index[i],'Machine'])
        if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j2+1):
          mj2.add(JobMachine.loc[JobMachine.index[i],'Machine'])
      m=mj1 & mj2
      for i in m:
        x='is_Successory'+str(i)+','+str(j1+1)+','+str(j2+1)
        is_Successory[x]= pulp.LpVariable(x,cat='Binary')
objectif=None
for j in range(len(Job.index)):
  objectif=objectif+(is_over['over'+str(j+1)]*Job.loc[Job.index[j],'Production'])
my_LP= pulp.LpProblem("my_LP",pulp.LpMaximize)                                                              
my_LP+=objectif, "objectif"                                                                                  
#1
for j in range(len(Job.index)):
  con1= None
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      con1= con1+ allocation[x]
  my_LP+=con1<=1
#2
for m in range (len(Param.index)):
  con2= None
  for l in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[l],'Machine']==m+1:
      con2= con2+ is_first['is_first'+str(JobMachine.loc[JobMachine.index[l],'Job'])[3:]+str(m+1)]
  my_LP+= con2<=1
#3
for j1 in range(len(Job.index)):
  for j2 in range (len(Job.index)):
    if j1!=j2:
      mj1 = set()
      mj2 = set()
      for i in range(len(JobMachine.index)):
        if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j1+1):
          mj1.add(JobMachine.loc[JobMachine.index[i],'Machine'])
        if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j2+1):
          mj2.add(JobMachine.loc[JobMachine.index[i],'Machine'])
      m=mj1 & mj2
      for i in m:
        a=start['start'+str(j1+1)]
        b=start['start'+str(j2+1)]
        BigM= 100
        for k in range(len(JobMachine.index)):
            if JobMachine.loc[JobMachine.index[k],'Machine']==i and JobMachine.loc[JobMachine.index[k],'Job']=='Job'+str(j1+1):
              d=JobMachine.loc[JobMachine.index[k],'Duration']
        for l in range(len(Switching.index)):
            if Switching.loc[Switching.index[l],'Job1']=='Job'+str(j1+1):
              if Switching.loc[Switching.index[l],'Job2']=='Job'+str(j2+1):
                if Switching.loc[Switching.index[l],'Machine']==Param.loc[Param.index[i-1],'Machine']:
                  x=Switching.loc[Switching.index[l],'SwitchingTime (day)']
        my_LP+= d+a+x<=b+BigM*(1-is_Successory['is_Successory'+str(i)+','+str(j1+1)+','+str(j2+1)])
#4
BigM=100
for j in range(len(Job.index)):
  con4=start['start'+str(j+1)]
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      con4= con4+ allocation[x]*JobMachine.loc[JobMachine.index[i],'Duration']
  my_LP+=con4<=Param.loc[Param.index[0],Param.columns[0]]+BigM*(1-is_over['over'+str(j+1)])
#5
for j in range(len(Job.index)):
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      a= None
      for l in range(len(JobMachine.index)):
        if JobMachine.loc[JobMachine.index[l],'Machine']==JobMachine.loc[JobMachine.index[i],'Machine']:
          if JobMachine.loc[JobMachine.index[l],'Job'][3:]!=str(j+1):
            a= a+ is_Successory['is_Successory'+str(JobMachine.loc[JobMachine.index[i],'Machine'])+','+str(JobMachine.loc[JobMachine.index[l],'Job'][3:])+','+str(j+1)]
      my_LP+= allocation['allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])]<= is_first['is_first'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])]+a
#6
for j in range(len(Job.index)):
  con6= None
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      con6= con6+ allocation[x]
  my_LP+=con6>=is_over['over'+str(j+1)]
#7
for j in range(len(Job.index)):
  a= 0
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      for l in range(len(JobMachine.index)):
        if JobMachine.loc[JobMachine.index[l],'Machine']==JobMachine.loc[JobMachine.index[i],'Machine']:
          if JobMachine.loc[JobMachine.index[l],'Job'][3:]!= str(j+1):
            a=a+ is_Successory['is_Successory'+str(JobMachine.loc[JobMachine.index[i],'Machine'])+','+str(j+1)+','+str(JobMachine.loc[JobMachine.index[l],'Job'][3:])]
      my_LP+= a<=1
#8.1
for j in range(len(Job.index)):
  a= 0
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      for l in range(len(JobMachine.index)):
        if JobMachine.loc[JobMachine.index[l],'Machine']==JobMachine.loc[JobMachine.index[i],'Machine']:
          if JobMachine.loc[JobMachine.index[l],'Job'][3:]!= str(j+1):
            a=a+ is_Successory['is_Successory'+str(JobMachine.loc[JobMachine.index[i],'Machine'])+','+str(j+1)+','+str(JobMachine.loc[JobMachine.index[l],'Job'][3:])]
      my_LP+= a<=allocation['allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])]
#8.2
for j2 in range(len(Job.index)):
  a= 0
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j2+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      for l in range(len(JobMachine.index)):
        if JobMachine.loc[JobMachine.index[l],'Machine']==JobMachine.loc[JobMachine.index[i],'Machine']:
          if JobMachine.loc[JobMachine.index[l],'Job'][3:]!= str(j2+1):
            a=a+ is_Successory['is_Successory'+str(JobMachine.loc[JobMachine.index[i],'Machine'])+','+str(JobMachine.loc[JobMachine.index[l],'Job'][3:])+','+str(j2+1)]
      my_LP+= a<=allocation['allocation'+str(j2+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])]
#9
for j in range(len(Job.index)):
  a= None
  con9=start['start'+str(j+1)]
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      a= a+ allocation[x]
  my_LP+=con9<=a*100
#10
for j in range(len(Job.index)):
  con10= None
  for i in range(len(JobMachine.index)):
    if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
      if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
        JobMachine.loc[JobMachine.index[i],'Machine']=1
      if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=2
      if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
        JobMachine.loc[JobMachine.index[i],'Machine']=3
      x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
      con10= con10+ allocation[x]
  my_LP+=con10<=start['start'+str(j+1)]
#11
for j in range(len(Job.index)):
  if j!=0 and j!=6 and j!=10 and j!=16:
    jpred='over'+str(Job.loc[Job.index[j],'PredecessorId'])[3:]
    p=is_over[str(jpred)]
    k=is_over['over'+str(j+1)]
    my_LP+= k<=p
#12
for j in range(len(Job.index)):
  con12= None
  if j!=0 and j!=6 and j!=10 and j!=16:
    jpred=str(Job.loc[Job.index[j],'PredecessorId'])[3:]
    a=0
    for i in range(len(JobMachine.index)):
      if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(jpred):
        if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
          JobMachine.loc[JobMachine.index[i],'Machine']=1
        if JobMachine.loc[JobMachine.index[i],'Machine']=='SmallDragline':
          JobMachine.loc[JobMachine.index[i],'Machine']=2
        if JobMachine.loc[JobMachine.index[i],'Machine']=='BigDragline':
          JobMachine.loc[JobMachine.index[i],'Machine']=3
        x='allocation'+str(jpred)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
        a= a+ allocation[x]*JobMachine.loc[JobMachine.index[i],'Duration']
    b=0
    for i in range(len(JobMachine.index)):
      if JobMachine.loc[JobMachine.index[i],JobMachine.columns[0]]=='Job'+str(j+1):
        if JobMachine.loc[JobMachine.index[i],'Machine']=='Bull':
          JobMachine.loc[JobMachine.index[i],'Machine']=1
        if JobMachine.loc[JobMachine.index[i],'Machine']=='Dragline':
          JobMachine.loc[JobMachine.index[i],'Machine']=2
        x='allocation'+str(j+1)+str(JobMachine.loc[JobMachine.index[i],'Machine'])
        b= b+ allocation[x]
    con12= con12+ start['start'+str(jpred)]+a
    my_LP+= con12<=start['start'+str(j+1)]+100*(1-b)