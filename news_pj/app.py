from flask import Flask, render_template, request
import crawl
naver = crawl.naver()
daum = crawl.daum()
nate = crawl.nate()

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/naver', methods=['POST'])
def naver_crawl():
    naver_titles = naver.news_title()
    naver_links = naver.news_link()

    return render_template('naver.html',
                           naver_titles=naver_titles,
                           naver_links=naver_links,
                           enumerate=enumerate,
                           zip=zip)


@app.route('/daum', methods=['POST'])
def daum_crawl():
    daum_titles = daum.news_title()
    daum_links = daum.news_link()

    return render_template('daum.html',
                           daum_titles=daum_titles,
                           daum_links=daum_links,
                           enumerate=enumerate,
                           zip=zip)


@app.route('/nate', methods=['POST'])
def nate_crawl():
    nate_titles = nate.news_title()
    nate_links = nate.news_link()

    return render_template('nate.html',
                           nate_titles=nate_titles,
                           nate_links=nate_links,
                           enumerate=enumerate,
                           zip=zip)


if __name__ == '__main__':
    app.run()
