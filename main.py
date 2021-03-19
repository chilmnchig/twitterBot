import twitter
import requests
import bs4


# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(
    consumer_key="秘密",
    consumer_secret="秘密",
    token="秘密",
    token_secret="秘密")

t = twitter.Twitter(auth=auth)


url = 'https://ameblo.jp/ohioelitejp'
diff_file_path = 'text.txt'


res = requests.get(url)
res.raise_for_status()  # エラーチェック


soup = bs4.BeautifulSoup(res.text)
title = soup.find("a", attrs={"class", "skinArticleTitle"}).text

diff_file = open(diff_file_path)
past_title = diff_file.read()

if title == past_title:
    pass

else:
    diff_file = open(diff_file_path, 'w')
    diff_file.writelines(title)
    diff_file.close()
    t.statuses.update(
        status="【幅Bot】{}\n{}".format(title, url))
