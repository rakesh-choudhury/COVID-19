import streamlit as st
import analysis
import map_vis
import race_plots
import covid_usa
import per_mil_case
import overview


MENU = {
    "COVID-19 Overview": overview,
    "Global Cases Over Time" : race_plots,
    "Global Total and Daily Cases" : analysis,
    "Cases per Million": per_mil_case,
    "COVID-19 Global Map" : map_vis,
    "COVID-19 USA": covid_usa
}
def main():
    st.sidebar.title("CORONAVIRUS PANDEMIC")
    menu_selection = st.sidebar.radio("So What would you like to see?", list(MENU.keys()))
    write = st.sidebar.markdown('⚠️Tip: Close this side bar to get a better view of the page.')
    write = st.sidebar.markdown('[<img src="http://pngimg.com/uploads/github/github_PNG40.png" width="50" height="50">](https://github.com/rakesh-choudhury/COVID-19)', unsafe_allow_html=True)
    write = st.sidebar.markdown('Dataset Sources:')
    write = st.sidebar.markdown('''[<img src="https://pbs.twimg.com/profile_images/1235299549637496832/qiK2pu1-_400x400.jpg" width="50" height="50">](https://ourworldindata.org/coronavirus-source-data) 
                                   [<img src="https://data.humdata.org/image/2017-12-13-140635.234944download.png" width="100" height="50">](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases)
                                   [<img src="https://yhs.apsva.us/wp-content/uploads/sites/41/2018/06/new-york-times-logo.png" width="100" height="50">](https://github.com/nytimes/covid-19-data)''', 
                                   unsafe_allow_html=True)
    write = st.sidebar.markdown('©Rakesh Choudhury')
    menu = MENU[menu_selection]

    if menu_selection=='Global Total and Daily Cases':
        menu.analysis()
    if menu_selection=='COVID-19 Global Map':
        menu.map()
    if menu_selection=='Global Cases Over Time':
        menu.race()
    if menu_selection=='COVID-19 USA':
        menu.usa()
    if menu_selection=='Cases per Million':
        menu.mil()
    if menu_selection=='COVID-19 Overview':
        menu.ove()
    
    

    

if __name__ == "__main__":
    main()