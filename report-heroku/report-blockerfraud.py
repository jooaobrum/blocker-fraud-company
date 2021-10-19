# Import libraries
import streamlit as st
import source.pages.home
import source.pages.results
import source.pages.ceo_questions
import source.pages.top_insights
import source.pages.demo_app
import source.pages.contact


PAGES = {
    "Home": source.pages.home,
    "Results": source.pages.results,
    "CEO Questions": source.pages.ceo_questions,
    "Top Insights": source.pages.top_insights,
    "Demo Web App": source.pages.demo_app,
    "Contact": source.pages.contact,
}


def main():
    # Navigation bar
    st.sidebar.title("Blocker Fraud Report")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Choose the page", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f'Loading {selection} ...'):
    	page.write()

    st.sidebar.image("source/images/blocker-nobg.png", use_column_width=True)
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

    st.sidebar.image("source/images/joao-nobg.png", use_column_width=True)


if __name__ == "__main__":
    main()
