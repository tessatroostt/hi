# import packages
import pandas as pd
import plotly as plt
import plotly.express as px
import streamlit as st

# Page config
st.set_page_config(
  page_title='Delays at Schiphol Airport',
  menu_items={
    'Get Help': None,
    'Report a bug': None
  }
)


# read in files
weerdata = pd.read_excel('weerdata.xlsx')
delay = pd.read_excel('delays.xlsx')

#delay file is exported from notebook after cleaning etc because original file is too big to put into github, cleaning steps are down below:
# delay['FLT_DATE'] = pd.to_datetime(delay['FLT_DATE'], format = '%Y%m%d') -> to datetime
# delay = delay[(delay.APT_ICAO == "EHAM")] -> only EHAM 
# delayreason = delayreason.rename(columns = {'DLY_APT_ARR_A_1':'Disruptions',
                                          #'DLY_APT_ARR_C_1':'Capacity (ATC)',
                                         #'DLY_APT_ARR_D_1': 'Weather',
                                         #'DLY_APT_ARR_E_1':'Disruptions',
                                         #'DLY_APT_ARR_G_1':'Capacity',
                                         #'DLY_APT_ARR_I_1':'Disruptions',
                                         #'DLY_APT_ARR_M_1':'Capacity',
                                         #'DLY_APT_ARR_N_1':'Disruptions',
                                         #'DLY_APT_ARR_O_1':'Disruptions',
                                         #'DLY_APT_ARR_P_1':'Events',
                                         #'DLY_APT_ARR_R_1':'Capacity',
                                         #'DLY_APT_ARR_S_1':'Staffing',
                                         #'DLY_APT_ARR_T_1':'Disruptions (ATC)',
                                         #'DLY_APT_ARR_V_1':'Capacity',
                                         #'DLY_APT_ARR_W_1':'Weather',
                                         #'DLY_APT_ARR_NA_1':'Disruptions'}) 
# delayreason = delayreason.drop(['YEAR','MONTH_NUM','MONTH_MON','APT_ICAO','APT_NAME','STATE_NAME','FLT_ARR_1','DLY_APT_ARR_1','FLT_ARR_1_DLY','FLT_ARR_1_DLY_15','ATFM_VERSION','Pivot Label'],1)
# delay['Disruptions sum'] = delay['Disruptions']+delay['Disruptions.1'] + delay['Disruptions.2'] + delay['Disruptions.3']+ delay['Disruptions.4'] + delay['Disruptions.5] -> create one column for all disruption values
# delay['Capacity sum'] = delay['Capacity'] + delay['Capacity.1'] + delay['Capacity.2'] + delay['Capacity.3'] -> create one column for all capacity values
# delay['Weather sum'] = delay['Weather'] + delay['Weather.1'] -> create one column for all weather values
# delay = delay.drop(['Disruptions','Disruptions.1','Disruptions.2','Disruptions.3','Disruptions.4','Disruptions.5','Capacity','Capacity.1','Capacity.2','Capacity.3','Weather','Weather.1'],1) -> drop previous disruption etc columns
# delay.rename(columns = {'Disruptions sum':'Disruptions','Capacity sum':'Capacity','Weather sum':'Weather'}, inplace = True) -> rename columns

#set to datetime
weerdata['YYYYMMDD'] = pd.to_datetime(weerdata['YYYYMMDD'],format='%Y%m%d')

# delay reason 2018-2021
delayyears = delay[(delay['FLT_DATE'] > '2018-01-01') & (delay['FLT_DATE'] <= '2021-12-31')]
delayyears = pd.melt(delayyears, id_vars=['FLT_DATE'],var_name= 'reasons',value_name = 'disruption')

#delay reason 2018
delay2018 = delay[(delay['FLT_DATE'] > '2018-01-01') & (delay['FLT_DATE'] <= '2018-12-31')]
delay2018 = pd.melt(delay2018, id_vars=['FLT_DATE'],var_name= 'reasons',value_name = 'disruption')

#delay reason 2019
delay2019 = delay[(delay['FLT_DATE'] > '2019-01-01') & (delay['FLT_DATE'] <= '2019-12-31')]
delay2019 = pd.melt(delay2019, id_vars=['FLT_DATE'],var_name= 'reasons',value_name = 'disruption')

#delay reason 2020
delay2020 = delay[(delay['FLT_DATE'] > '2020-01-01') & (delay['FLT_DATE'] <= '2020-12-31')]
delay2020 = pd.melt(delay2020, id_vars=['FLT_DATE'],var_name= 'reasons',value_name = 'disruption')

#delay reason 2021
delay2021 = delay[(delay['FLT_DATE'] > '2021-01-01') & (delay['FLT_DATE'] <= '2021-12-31')]
delay2021 = pd.melt(delay2021, id_vars=['FLT_DATE'],var_name= 'reasons',value_name = 'disruption')

with st.sidebar:
  sidebar_keuze= st.radio('Chapters:', ['Reasons of delay at Schiphol','Sources'])
  
if sidebar_keuze == 'Reasons of delay at Schiphol':
  st.markdown('***')
  st.markdown("<h3 style='text-align: center; color: black;'>Reasons of delay at Schiphol Airport Amsterdam 2018-2021</h3>", unsafe_allow_html=True)
  st.markdown('***')
  
  col1, col2 = st.columns(2)
  
  # barplots with different year
  with col1:
    barplot_opties = st.selectbox('Choose a year:', ['2018-2021','2018','2019','2020','2021'])
    if barplot_opties == '2018-2021':
      fig = px.histogram(delayyears, x="reasons", y = 'disruption').update_layout(title = 'Reasons of delay Schiphol Aiport Amsterdam 2018-2021 ', xaxis_title = 'Delay reasons', yaxis_title = 'Delay time????')
      st.write(fig)
    if barplot_opties == '2018':
      fig = px.histogram(delay2018, x="reasons", y = 'disruption').update_layout(title = 'Reasons of delay Schiphol Aiport Amsterdam 2018', xaxis_title = 'Delay reasons', yaxis_title = 'Delay time????')
      st.write(fig)
    if barplot_opties == '2019':
      fig = px.histogram(delay2019, x="reasons", y = 'disruption').update_layout(title = 'Reasons of delay Schiphol Aiport Amsterdam 2019', xaxis_title = 'Delay reasons', yaxis_title = 'Delay time????')
      st.write(fig)
    if barplot_opties == '2020':
      fig = px.histogram(delay2020, x="reasons", y = 'disruption').update_layout(title = 'Reasons of delay Schiphol Aiport Amsterdam 2020', xaxis_title = 'Delay reasons', yaxis_title = 'Delay time????')
      st.write(fig)
    if barplot_opties == '2021':
      fig = px.histogram(delay2021, x="reasons", y = 'disruption').update_layout(title = 'Reasons of delay Schiphol Aiport Amsterdam 2021', xaxis_title = 'Delay reasons', yaxis_title = 'Delay time????')
      st.write(fig)
    
  with col2:
    st.markdown("""
    The different delay reasons are categorized into 7 groups:
    - Capacity ATC
    - Events
    - Staffing
    - Disruptions (ATC)
      - Industrial Action
      - Equipment
    - Disruptions
      - Accident/Incident
      - Equipment (non ATC)
      - Industrial Action
      - Other
      - Not specified
    - Capacity
      - Aerodrome Capacity
      - Airspace Management
      - ATC Routeing
      - Environmental Issues
    - Weather
      - De-icing
      - Weather
      """)
    
  #fill in na values in delay dataset with 0 to make lineplot
  delayna = delay.fillna(0)
