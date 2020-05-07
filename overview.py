
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import datetime

def ove():
    st.title('CORONAVIRUS PANDEMIC OVERVIEW')
    url_pop = 'https://covid.ourworldindata.org/data/ecdc/locations.csv'
    world_pop = pd.read_csv(url_pop,sep=",")
    url = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
    covid_new = pd.read_csv(url, sep=",")
    covid_new_plot = covid_new
    covid_pop = (covid_new.merge(world_pop, left_on='location', right_on='location')
                  .reindex(columns=['location', 'date', 'new_cases', 'new_deaths', 'total_cases',
               'total_deaths','population']))
    covid_pop['per_mil_cases'] = (covid_pop['total_cases']/covid_pop['population'])*1000000
    covid_pop['per_mil_deaths'] = (covid_pop['total_deaths']/covid_pop['population'])*1000000
    df  = covid_pop[covid_pop['date']==covid_pop.date.max()]
    df = df.sort_values(by=['total_cases'], ascending=False)
    cases= df.total_cases.sum()
    deaths = df.total_deaths.sum()
    df = df.fillna(0)
    df = df.astype({'per_mil_cases':'int64','per_mil_deaths':'int64'})
    df = df.rename(columns={'location':'Country','date':'Date','new_cases':'New Cases','total_cases':'Total Cases',
                        'new_deaths':'New Deaths','total_deaths':'Total Deaths','per_mil_cases':'Confirmed Cases Per Million',
                        'per_mil_deaths':'Deaths Per Million'})
    df= df[['Country','New Cases','Total Cases','New Deaths','Total Deaths','Confirmed Cases Per Million','Deaths Per Million']]
    url_rec = 'https://data.humdata.org/hxlproxy/data/download/time_series_covid19_recovered_global_narrow.csv?dest=data_edit&filter01=merge&merge-url01=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D1326629740%26single%3Dtrue%26output%3Dcsv&merge-keys01=%23country%2Bname&merge-tags01=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&filter02=merge&merge-url02=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D398158223%26single%3Dtrue%26output%3Dcsv&merge-keys02=%23adm1%2Bname&merge-tags02=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&merge-replace02=on&merge-overwrite02=on&filter03=explode&explode-header-att03=date&explode-value-att03=value&filter04=rename&rename-oldtag04=%23affected%2Bdate&rename-newtag04=%23date&rename-header04=Date&filter05=rename&rename-oldtag05=%23affected%2Bvalue&rename-newtag05=%23affected%2Binfected%2Bvalue%2Bnum&rename-header05=Value&filter06=clean&clean-date-tags06=%23date&filter07=sort&sort-tags07=%23date&sort-reverse07=on&filter08=sort&sort-tags08=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv'
    covid_rec = pd.read_csv(url_rec, sep=",")
    covid_rec = covid_rec.iloc[1:,:] #removing the redundant first row
    covid_rec = covid_rec.rename(columns={'ISO 3166-1 Alpha 3-Codes':'iso_alpha','Country/Region':'Country','Value':'Cases','Lat':'lat','Long':'lon'})
    covid_rec = covid_rec.astype({'Cases':'int64','lat':'float64','lon':'float64'}) #changing data type
    recover = covid_rec[covid_rec['Date']==covid_rec.Date.max()].Cases.sum()
    date = pd.to_datetime(covid_rec['Date'])
    date= date.max().strftime('%d %b %Y')
    st.markdown('# Total Coronavirus Cases: '+str(cases))
    st.markdown('# Total Death Cases: '+str(deaths))
    st.markdown('# Total Recovery: ' +str(recover))
    st.markdown('## Last Updated: **' +date+'**')
    st.table(df.style.hide_index())
    st.write('©Rakesh Choudhury')