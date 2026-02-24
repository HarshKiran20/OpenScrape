from fpdf import FPDF
import io

def clean_text_for_pdf(text):
    """
    Replaces common problematic Unicode characters with ASCII equivalents
    to avoid FPDF encoding errors.
    """
    replacements = {
        "\u2013": "-", # en dash
        "\u2014": "-", # em dash
        "\u2018": "'", # left single quote
        "\u2019": "'", # right single quote
        "\u201c": '"', # left double quote
        "\u201d": '"', # right double quote
        "\u2022": "*", # bullet point
        "\u2026": "...", # ellipsis
    }
    for unicode_char, ascii_char in replacements.items():
        text = text.replace(unicode_char, ascii_char)
    
    # Final fallback: encode to latin-1 and ignore anything else
    return text.encode('latin-1', 'ignore').decode('latin-1')

def generate_pdf(dataframe):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)
    
    pdf.cell(200, 10, txt="Scraped Data Report", ln=True, align='C')
    pdf.ln(10)

    for index, row in dataframe.iterrows():
        # Clean the text before adding to PDF
        raw_text = str(row['Content'])
        safe_text = clean_text_for_pdf(raw_text)
        
        pdf.multi_cell(0, 8, txt=f"- {safe_text}")
        pdf.ln(2)
        
    return bytes(pdf.output())

def generate_csv(dataframe):
    return dataframe.to_csv(index=False).encode('utf-8')