import streamlit as st
import os
from backend.ocr_engine import extract_text
from backend.text_comparator import compare_texts
from backend.summarizer import summarize_text
from backend.bulletizer import convert_to_bullets

st.set_page_config(page_title="MultiDoc AI", layout="wide")
st.title("📄 MultiDoc AI")

mode = st.radio("Choose Mode", ["Single Document Summary", "Compare Two Documents"], horizontal=True)

def get_text(uploaded_file):
    if uploaded_file:
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        return extract_text(uploaded_file, ext)
    return ""

if mode == "Single Document Summary":
    uploaded = st.file_uploader("Upload a document", type=["pdf", "docx", "png", "jpg", "jpeg"])
    if uploaded:
        text = get_text(uploaded)

        st.subheader("📜 Extracted Text")
        st.text_area("Text", text, height=300)

        if text:
            st.subheader("🧠 AI Summary")
            summary = summarize_text(text)
            st.success(summary)

            st.subheader("📌 Bullet Points")
            bullets = convert_to_bullets(text)
            for bullet in bullets:
                st.markdown(f"• {bullet}")

elif mode == "Compare Two Documents":
    col1, col2 = st.columns(2)
    with col1:
        doc1 = st.file_uploader("Upload Document 1", type=["pdf", "docx", "png", "jpg", "jpeg"], key="doc1")
    with col2:
        doc2 = st.file_uploader("Upload Document 2", type=["pdf", "docx", "png", "jpg", "jpeg"], key="doc2")

    if doc1 and doc2:
        text1 = get_text(doc1)
        text2 = get_text(doc2)

        left, right = compare_texts(text1, text2)

        diff_html = """
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 8px;
                vertical-align: top;
                font-family: monospace;
                font-size: 14px;
            }
            .left {
                background-color: #fef9e7;
            }
            .right {
                background-color: #e8f8f5;
            }
        </style>
        <table>
            <tr><th>Document 1</th><th>Document 2</th></tr>
        """

        for l, r in zip(left, right):
            diff_html += f"<tr><td class='left'>{l}</td><td class='right'>{r}</td></tr>"

        diff_html += "</table>"

        st.components.v1.html(diff_html, height=600, scrolling=True)
