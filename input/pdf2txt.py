import pdfplumber

# PDFファイルのパス
pdf_path = "./input/令和6年度国土地理院関係当初予算.pdf"

# pdfplumberを使ってPDFからテキストを抽出
with pdfplumber.open(pdf_path) as pdf:
    text_plumber = ""
    for page in pdf.pages:
        # ページごとのテキストを抽出し、改行をスペースに置き換える
        page_text = page.extract_text().replace("\n", " ")
        text_plumber += page_text

# 改行を取り除いたテキストをファイルに保存
output_text_plumber_path = "./input/令和6年度国土地理院関係当初予算.txt"
with open(output_text_plumber_path, "w", encoding="utf-8") as text_file:
    text_file.write(text_plumber)

print(f"抽出されたテキストが {output_text_plumber_path} に保存されました")
