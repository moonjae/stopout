from django.db import models

from crawler import main


# Create your models here.




class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_episode_list(self):
        naver_webtoon_crawler = main.WebtoonCrawler()
        episode_list = naver_webtoon_crawler.get_episode_list(self.webtoon_id, 1)
        for episode in episode_list:
            self.episode_set.create(episode_id = episode.episode_id, title = episode.title, rating = episode.rating,
                                    created_date = episode.created_date)
        return self.episode_set.all()




class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)

    def __str__(self):
        return ('episode_id: {}, title: {}, rating: {}, created_date: {}'.format(
            self.episode_id, self.title, self.rating, self.created_date))

