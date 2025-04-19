import streamlit as st

def main():
    st.set_page_config(page_title="4imprint Scraper", layout="wide")
    st.title("4imprint Product Data Extractor")

    url = st.text_input("Paste 4imprint category URL:")
    if url:
        st.write(f"You entered: {url}")
        # Add scraping logic here later

if __name__ == "__main__":
    main()
