from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    main_headings = soup.find_all('h2')
    for heading in main_headings:
        print(heading.text)