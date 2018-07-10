import bs4
import urllib.request

while True:
    toSearch = input("Enter Movie Name : ")
    webpage = urllib.request.urlopen('https://www.imdb.com/find?ref_=nv_sr_fn&q='+toSearch)

    soup = bs4.BeautifulSoup(webpage, 'lxml')
    link = soup.find('td', class_='result_text')

    new_webpage = link.a['href']

    new_webpage = urllib.request.urlopen('https://www.imdb.com'+new_webpage)

    soup_2 = bs4.BeautifulSoup(new_webpage, 'lxml')

    summary = soup_2.find_all('div', class_='summary_text')

    castList = soup_2.find('table', class_='cast_list')

    for s in summary:
        print(s.text.strip())

    castList = castList.text.strip()
    castList = castList.replace("  ","")
    print(castList)
