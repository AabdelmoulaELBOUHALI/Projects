# -*- coding: utf-8 -*-
#Packages
import streamlit as st
from datetime import datetime as dt
import datetime 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

#Set a configuraation for the web app page
st.set_page_config(layout="wide")

#Load the datas files
features=pd.read_csv('features.csv')
stores=pd.read_csv('stores.csv')
DataTrain=pd.read_csv('TrainData.csv')

#Split the data for the Machine learning model 
x_train=DataTrain.drop(columns=['A','Weekly_Sales','Year'],axis=1)
y_train=DataTrain['Weekly_Sales']



stor = 1
departm=1
List_store= range(1,46)
List_dept = range(1,100)
Weeks=[]
holiday=[]
storetype_values = {'A':3, 'B':2, 'C':1}
ListeDate=[]

st.sidebar.header('What do you want to do ?' )
st.title('Walmart weekly Stores Sales ')


st.warning("This app allow you to do two things. Check the sidebar to choose what you want")
Thing=st.sidebar.selectbox('',['Visualize the previous datas','Make a prediction'])

#Defin a function that will return the data for prediction using the input parameters
def user_input():
	global stor,departm
#input parameters
	st.sidebar.header('Input parameters for the prediction ')
	start = dt.strptime('2012-01-06', '%Y-%m-%d') # set default value
	end = dt.strptime('2012-06-22', '%Y-%m-%d') # set default value
	Start = st.sidebar.date_input('Start Date', value = start)
	End = st.sidebar.date_input("End Date", value = end)

	store=st.sidebar.selectbox(("Select the Store"),List_store)
	stor=int(store)
	dept=st.sidebar.selectbox("Select the departement",(List_dept))
	departm=int(dept)

#Create a list of date between the start date and the end date 
	from_date = Start
	while from_date <= End:
	  	ListeDate.append(from_date.strftime("%d-%m-%Y"))
	  	from_date = from_date + datetime.timedelta(weeks=1)
	 
	dat ={'Date':Start}
	dat= pd.DataFrame(dat,index=[0])
	dat2={'Date':End}
	dat2=pd.DataFrame(dat2,index=[0])
	dat=pd.concat([dat,dat2],ignore_index=True)
	dat['Wks']=pd.to_datetime(dat['Date']).dt.week

#Get the weeks number for each date
	if (dat["Wks"][0]) > (dat["Wks"][1]):
	 	for i in range((dat["Wks"][0]), 53):
	 		Weeks.append(i)
	 	for i in range (1,(dat["Wks"][1]) + 1):
	 		Weeks.append(i)
	elif (dat["Wks"][0]) == (dat["Wks"][1]):
		Weeks.append(int(dat["Wks"][0]))
	else:
		for i in range((dat["Wks"][0]),(dat["Wks"][1]) + 1):
			Weeks.append(i)

#Get the store size and type 
	for i in stores.index:
		if stores['Store'][i] == store :
			size= stores['Size'][i]
			type_store=stores['Type'][i]

#Check for each date if there is holiday in this week or no based on previous datas
	features['Week'] = pd.to_datetime(features['Date']).dt.week
	for i in Weeks:
		for j in features.index:
			if features['Week'][j]== i :
				holiday.append(bool(features['IsHoliday'][j]))
				break

#Create the dataframe wich will be the input for the model prediction
	data =pd.DataFrame({"Store":int(store),
                "Dept":int(dept),
                "IsHoliday":holiday[0],
                "Type": storetype_values[type_store],
                "Size": size,
                "Week":Weeks[0]},index=[0])

	for i in range(1,len(Weeks)):
		data1=pd.DataFrame({"Store":int(store),
                "Dept":int(dept),
                "IsHoliday":holiday[i],
                "Type": storetype_values[type_store],
                "Size": size,
                "Week":Weeks[i]},index=[0])
		data=pd.concat([data,data1],ignore_index=True)

	return data


if Thing=='Make a prediction':

	df=user_input()
	Datapredict=pd.DataFrame({'Date': ListeDate[0], 'IsHoliday':holiday[0]},index=[0])
	for i in range(1,len(ListeDate)):
		datapred2=pd.DataFrame({'Date': ListeDate[i],'IsHoliday':holiday[i]},index=[0])
		Datapredict = pd.concat([Datapredict,datapred2],ignore_index=True)

	if st.sidebar.button('Predict'):

		Model = RandomForestRegressor(n_estimators = 100,random_state=0)
		Model.fit(x_train,y_train)
		y_pred =Model.predict(df)
		Datapredict['Weekly_Sales']=y_pred

		st.warning('Sales prediction for Store: '+str(stor)+' Dept: '+str(departm)+' between '+ str(ListeDate[0]) + ' and '+ str(ListeDate[len(ListeDate)-1]))

		st.write(Datapredict)
		st.write('')

		Datapredict['Index']= Datapredict.index
		st.write('')
		st.write('')
		st.write('Visualize the predictions with graphs ')
		st.write('')
		basic_chart = alt.Chart(Datapredict).mark_line().encode(x='Index',y='Weekly_Sales').interactive().properties(
		    width=800,
		    height=400
		)
		st.altair_chart(basic_chart)
		st.write('')
		st.write('')
		stacked_bar = alt.Chart(Datapredict).mark_bar().encode(x='Index',y='Weekly_Sales',color='IsHoliday').interactive().properties(
		    width=1000,
		    height=600
		)
		st.altair_chart(stacked_bar)

else:
	st.markdown('''<h2 style="color:blue;">Data Visualization for previous Years </h2>''',unsafe_allow_html=True)
	st.markdown('''<h3 style="color:red;">Years = 2010 and 2011</h3>''',unsafe_allow_html=True)
	col1, col2= st.beta_columns(2)
	Viz = col1.selectbox("Select the graph you want",['Graph : weekly sales per Stores','Graph : weekly sales per Types','Graph : weekly sales per departments'])
	
	if  Viz == "Graph : weekly sales per Stores" :
		st.write('')
		st.markdown('''<h3 style="color:red;">Graph : weekly sales per Stores</h3>''',unsafe_allow_html=True)
		AvgSalesStore=pd.DataFrame(DataTrain.groupby('Store')['Weekly_Sales'].mean())
		AvgSalesStore['Index']=AvgSalesStore.index
		bar1 = alt.Chart(AvgSalesStore).mark_bar().encode(x='Index',y='Weekly_Sales').interactive().properties(
		    width=800,
		    height=600
		)
		st.altair_chart(bar1)

	elif Viz == 'Graph : weekly sales per Types':
		st.write('')
		st.write('')
		st.markdown('''<h3 style="color:red;">Graph : weekly sales per Types</h3>''',unsafe_allow_html=True)
		st.write('')
		st.write(" Stores types :  Type A = 1,		Type B = 2,		Ty C = 3")
		AvgSalesType = DataTrain.groupby('Type')['Weekly_Sales'].mean().to_dict()
		AvgSalesType = pd.DataFrame(list(AvgSalesType.items()), columns=['Store_Type', 'AvgWeeklySales'])
		bar2 = alt.Chart(AvgSalesType).mark_bar().encode(x='Store_Type',y='AvgWeeklySales').interactive().properties(
		    width=800,
		    height=600
		)
		st.altair_chart(bar2)
	else:
		st.write('')
		st.write('')
		st.markdown('''<h3 style="color:red;">Graph : weekly sales per departements</h3>''',unsafe_allow_html=True)
		

		Nb_Store=col1.selectbox(("Select the N° of the Store"),List_store)
		Dt =DataTrain[DataTrain.Store == Nb_Store]

		AvgSalesDept = Dt.groupby('Dept')['Weekly_Sales'].mean().to_dict()
		AvgSalesDept = pd.DataFrame(list(AvgSalesDept.items()), columns=['Store_Dept', 'AvgWeeklySales'])
		bar3 = alt.Chart(AvgSalesDept).mark_bar().encode(x='Store_Dept',y='AvgWeeklySales').interactive().properties(
		    width=800,
		    height=600
		)
		st.altair_chart(bar3)