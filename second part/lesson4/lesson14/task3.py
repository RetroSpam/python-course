def report_page_generator(pages):
    return (f"Page {i+1}: {page}" for i, page in enumerate(pages))

pages = ["Introduction", "Methodology", "Results", "Discussion", "Conclusion"]
report_generator = report_page_generator(pages)

for page in report_generator:
    print(page)