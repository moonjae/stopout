
import re
import requests
from bs4 import BeautifulSoup, NavigableString



class WebtoonCrawler:


    def get_episode_list(self, webtoon_id, page):
        """
        고유ID(URL에서 titleId값)에 해당하는 웹툰의
        특정 page에 있는 에피소드 목록을 리스트로 리턴
        """
        url = "http://comic.naver.com/webtoon/list.nhn"
        params = { 'titleId': webtoon_id, 'page': page}
        source = requests.get(url,params)
        soup = BeautifulSoup(source.text, 'lxml')


        tr_list = soup.find('table', class_="viewList").find_all('tr')[1:]
        PATTERN_EPISODE_ID = re.compile(r'no=(\d*?)&')


        episode_list = []

        for tr in tr_list:


            episode_id_match = re.search(PATTERN_EPISODE_ID,str(tr))
            episode_id = episode_id_match.group(1)
            url_thumbnail = tr.find('img')['src']
            title = tr.find('td', class_="title").a.text
            rating = tr.find('div', class_="rating_type").find("strong").text
            created_date = tr.find('td', class_="num").text

            episode = EpisodeData(episode_id, url_thumbnail, title,rating,created_date)
            episode_list.append(episode)

        return episode_list



class EpisodeData:
    """
    하나의 에피소드에 대한 정보를 갖도록 함
    """

    def __init__(self, episode_id, url_thumbnail, title, rating, created_date):
        self.episode_id = episode_id
        self.url_thumbnail = url_thumbnail
        self.title = title
        self.rating = rating
        self.created_date = created_date

    def __str__(self):
        return('episode_id: {}, title: {}, url_thumbnail: {}, rating: {}, created_date: {}'.format(
            self.episode_id, self.title, self.url_thumbnail, self.rating,self.created_date ))

