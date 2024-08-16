import streamlit as st
from streamlit_option_menu import option_menu
import pdf1,url_data,content_mcq

st.set_page_config(
    page_title="Interview ChatBot"
)

class multiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='MENU',
                options=['PDF','URL','MCQ'],
                default_index=1,
                 styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#85929E"},
                    "nav-link-selected": {"background-color": "blue"},}
            )
        if app == 'PDF':
            pdf1.app()
        if app == 'URL':
            url_data.app()
        if app == 'MCQ':
            content_mcq.app()


app = multiApp()
app.run()
