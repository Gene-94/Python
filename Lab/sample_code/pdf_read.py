from pdfminer.high_level import extract_text

with extract_text('/home/yevheniy/Documents/Social.pdf') as file:
    for page in file.pages:
        print(page)
