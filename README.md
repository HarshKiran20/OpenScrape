# 🕸️ OpenScrape: Managed Web Scraper
OpenScrape is a universal web scraping tool designed to extract, manage, and export data from any static website. Built with a modular architecture, it provides a user-friendly interface to preview scraped content, apply keyword filters, and download data in structured formats.

# 🚀 Features
Universal Scraping: Input any valid URL to extract paragraphs, headings, or links.

Managed Data: Automatically cleans the scraped content by removing duplicates and empty rows.

Live Preview & Filtering: Interactive data table that allows real-time keyword filtering using Streamlit Session State.

Multi-Format Export: Download your managed data as a CSV for data analysis or a PDF for reporting.

Encoding Safety: Custom utility logic to handle complex Unicode characters (like smart quotes and dashes) for crash-free PDF generation.

## 🛠️ Tech Stack
Frontend: Streamlit (Python-based UI framework)

Scraping Engine: BeautifulSoup4 with lxml parser

Data Handling: Pandas

PDF Generation: FPDF2

Environment: Python venv (Virtual Environment)

Hosting: Hugging Face Spaces

## 📂 Project Structure
OpenScrape/
├── app.py              # Main Streamlit UI and Session State management
├── scraper.py          # Core scraping logic and HTML parsing
├── utils.py            # Data cleaning and file export (CSV/PDF) logic
├── requirements.txt    # Project dependencies
├── .gitignore          # Excludes venv and cache files
└── README.md           # Project documentation

## ⚙️ Local Installation
1.Clone the repository:

git clone https://github.com/YOUR_USERNAME/OpenScrape.git
cd OpenScrape

2.Set up the Virtual Environment:

python -m venv venv
Activate on Windows:
.\venv\Scripts\activate

3.Install Dependencies:

pip install -r requirements.txt

4.Run the Application:

streamlit run app.py

# #🌐 Deployment
This project is configured for seamless deployment on Hugging Face Spaces. Simply connect your GitHub repository to a new Streamlit Space on Hugging Face, and it will auto-install the requirements and host the app.



