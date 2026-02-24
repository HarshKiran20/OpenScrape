import streamlit as st
import pandas as pd
from scraper import fetch_html, parse_content
from utils import generate_csv, generate_pdf

st.set_page_config(page_title="OpenScrape Pro", layout="wide")

# Initialize session state for data persistence
if 'scraped_df' not in st.session_state:
    st.session_state.scraped_df = None

st.title("🕸️ OpenScrape: Managed Web Scraper")

with st.sidebar:
    st.header("Control Panel")
    url = st.text_input("Enter URL", placeholder="https://example.com")
    option = st.selectbox("Extract Type", ("Paragraphs (Text)", "Headings", "Links"))
    
    tag_map = {"Paragraphs (Text)": "p", "Headings": "headings", "Links": "a"}
    
    if st.button("Start Scraping"):
        with st.spinner("Processing..."):
            html = fetch_html(url)
            if "Error" in html:
                st.error(html)
            else:
                results = parse_content(html, tag=tag_map[option])
                # Data Management: Remove duplicates and empty rows
                df = pd.DataFrame(results, columns=["Content"]).drop_duplicates().dropna()
                st.session_state.scraped_df = df

# --- Main Display Logic ---
if st.session_state.scraped_df is not None:
    df = st.session_state.scraped_df
    
    st.subheader("🛠️ Data Management & Filters")
    
    # Live Filter
    search_query = st.text_input("🔍 Search/Filter content by keyword:", "")
    
    filtered_df = df.copy()
    if search_query:
        filtered_df = df[df["Content"].str.contains(search_query, case=False, na=False)]
    
    st.write(f"Showing {len(filtered_df)} unique results.")
    st.dataframe(filtered_df, use_container_width=True)

    # --- Downloads ---
    st.divider()
    c1, c2 = st.columns(2)
    
    with c1:
        csv = generate_csv(filtered_df)
        st.download_button("📥 Download CSV", data=csv, file_name="data.csv", mime="text/csv")
        
    with c2:
        # Pass the filtered data to the PDF generator
        pdf_data = generate_pdf(filtered_df)
        st.download_button(
            label="📄 Download PDF",
            data=pdf_data,
            file_name="scraped_data.pdf",
            mime="application/pdf"
        )
else:
    st.info("Paste a URL and click 'Start Scraping' to see data here.")