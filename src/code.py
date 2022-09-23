from bs4 import BeautifulSoup
from requests import get

base_url = 'https://www.cnnindonesia.com'

class Script:

    def query(self, url):
        """
        It takes a URL as an argument, then it scrapes the page and returns a list of dictionaries
        
        :param url: The URL of the page you want to scrape
        :return: A list of dictionaries.
        """
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        parent_tag = soup.find('div', class_="media_rows")
        tag = parent_tag.find_all("article")
        data = []

        for i in tag:
            try:
                title = i.find("h2", attrs={'class':'title'}).text.strip()
                link = i.find('a')['href'].strip()
                gambar = i.find('img')['src'].strip()
                # tipe = i.find('span', attrs={'class':'kanal'}).text
                # waktu = i.find('span', attrs={'class':'date'}).text
                data.append({
                    "judul": title,
                    "link": link,
                    "poster": gambar,
                    # "tipe": tipe,
                    # "waktu": waktu
                })
            except:
                pass

        return data

    def index(self):
        """
        It returns the result of the query of the home news from cnn's site
        :return: The response object.
        """
        return self.query('{}/'.format(base_url))

    def nasional(self):
        """
        Mengambil berita nasional

        :return: list dictionary
        """
        return self.query('{}/nasional'.format(base_url))

    def internasional(self):
        """
        Mengambil berita internasional / luar negeri
        
        :return: list dictionary
        """
        return self.query('{}/internasional'.format(base_url))

    def ekonomi(self):
        """
        Mengambil berita ekonomi
        
        :return: list dictionary
        """
        return self.query('{}/ekonomi'.format(base_url))

    def olahraga(self):
        """
        Mengambil berita olahraga
        
        :return: list dictionary
        """
        return self.query('{}/olahraga'.format(base_url))

    def teknologi(self):
        """
        Mengambil berita teknologi
        
        :return: list dictionary
        """
        return self.query('{}/teknologi'.format(base_url))

    def hiburan(self):
        """
        Mengambil berita hiburan
        
        :return: list dictionary
        """
        return self.query('{}/hiburan'.format(base_url))

    def social(self):
        """
        Mengambil berita sosial
        
        :return: list dictionary
        """
        return self.query('{}/gaya-hidup'.format(base_url))

    def detail(self, url):
        """
        Mengambil detail berita
        :args:
            url : string -> url berita
        :example:
            url : string -> https://www.cnnindonesia.com/teknologi/20220921153459-190-850830/cara-menghapus-data-iphone-sebelum-dijual
        :return: list dictionary
        """
        data = []
        try:
            req = get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            tag = soup.find('div', class_="detail_text")
            gambar = soup.find('div', class_='media_artikel').find('img').get('src')
            judul = soup.find('h1', class_='title').text
            body = tag.text
            data.append({
                "judul": judul,
                "poster": gambar,
                "body": body,
            })
        except:
            data.append({
                "message": "network error",
            })

        return data

    def search(self,q):
        """
        Mencari berita spesifik berdasarkan query

        :args:
            q : string -> query atau berita yang ingin dicari
        :returns: list dictionary
        """
        
        return self.query('{}/search/?query={}'.format(base_url, q))

if __name__ != '__main__':
    Code = Script()