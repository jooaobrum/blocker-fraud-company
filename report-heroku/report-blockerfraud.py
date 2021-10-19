# Import libraries
import streamlit as st
import src.pages.home
import src.pages.results
import src.pages.ceo_questions
import src.pages.top_insights
import src.pages.demo_app
import src.pages.contact


PAGES = {
    "Home": src.pages.home,
    "Results": src.pages.results,
    "CEO Questions": src.pages.ceo_questions,
    "Top Insights": src.pages.top_insights,
    "Demo Web App": src.pages.demo_app,
    "Contact": src.pages.contact,
}


def main():
    # Navigation bar
    st.sidebar.title("Blocker Fraud Report")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Choose the page", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f'Loading {selection} ...'):
    	page.write()

    st.sidebar.image("src/images/blocker-nobg.png", use_column_width=True)
    st.sidebar.title("About")
    st.sidebar.info(
        """
        My name is João Paulo Sales Brum, I was born in Santiago - RS, Brazil and I'm actually 24 years old. I am a data science enthusiast and currently I am doing an exchange in France. Also, in my free time, i like to play sports, go out with friends and travel the world.
        If you want to know more about my projects, you can acess my social medias.

        Github: [github.com/jooaobrum](https://github.com/jooaobrum)
        Linkedin: [linkedin.com/jooaobrum](https://www.linkedin.com/in/jooaobrum/)

        This report was generated using Streamlit.
	"""
    )

    st.sidebar.image("src/images/joao-nobg.png", use_column_width=True)


if __name__ == "__main__":
    main()
