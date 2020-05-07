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