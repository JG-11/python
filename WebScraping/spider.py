from bs4 import BeautifulSoup
import urllib.request

URL = 'http://theleanstartup.com/'

def spider():
    response = urllib.request.urlopen(URL)
    soup = BeautifulSoup(response.read(), 'html.parser')

    data = {}
    data['title'] = soup.title.string

    links = set()
    for link in soup.find_all('a'):
        aux = link.get('href')
        links.add(aux)

    data['links'] = links

    with open('result.txt', 'w') as f:
        f.write('Website title: {}'.format(data['title']))
        
        f.write('\nLinks\n')
        i = 1
        for link in data['links']:
            f.write('{}: {}\n'.format(i, link))
            i += 1


if __name__ == '__main__':
    spider()