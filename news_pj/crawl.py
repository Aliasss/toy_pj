# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# from requests.api import head

# 네이버 뉴스 크롤링
# 네이버의 경우 robot.txt가 뉴스 크롤링 막음.
# 브라우저 콘솔창에서 navigator.userAgent로 유저 에이전트 스트링 확인 후 헤더 전송
naver_url = "https://news.naver.com"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

class naver:
    req = requests.get(naver_url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    def news_title(self):
        titles = []
        for title in self.soup.select("ul.hdline_article_list > li > div.hdline_article_tit > a"):
            titles.append(title.text)

        return titles

    def news_link(self):
        links = []
        for link in self.soup.select("ul.hdline_article_list > li > div.hdline_article_tit > a"):
            url = "https://news.naver.com"+link['href']
            links.append(url)

        return links
        
# naver = naver()
# print(naver.news_link())

#다음 뉴스 크롤링
daum_url = "https://news.daum.net"
class daum:
    req = requests.get(daum_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    def news_title(self):
        titles = []
        for title in self.soup.select("ul.list_issue > li > div.item_issue > div > strong > a"):
            titles.append(title.text)
            
        return titles

    def news_link(self):
        links = []
        for link in self.soup.select("ul.list_issue > li > div.item_issue > div > strong > a"):
            links.append(link['href'])

        return links
        

# 네이트 뉴스 크롤링
nate_url = "https://news.nate.com/total"
class nate:
    req = requests.get(nate_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    def news_title(self):
        titles = []
        for title in self.soup.select("div.newsMainPhoto > ul a > span.subject"):
            titles.append(title.text)
        
        return titles

    def news_link(self):
        links = []
        for link in self.soup.select("div.newsMainPhoto > ul a"):
            links.append(link['href'])
        
        return links

