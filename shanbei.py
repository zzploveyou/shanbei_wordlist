# coding:utf-8
import re
from urllib import urlopen
from time import sleep


def get_words(wordlist_url):
    words = []
    num = 1
    while True:
        if num == 1:
            purl = wordlist_url
        else:
            purl = wordlist_url + "?page={}".format(num)
        num += 1
        print("Crawl from: {}".format(purl))
        content = urlopen(purl).read()
        pwords = re.findall("<strong>(.*?)</strong>", content)
        if pwords != []:
            words += pwords
        else:
            break
        sleep(0.5)
    return words


def wordlist_urls(wordbook_url, filename):
    content = urlopen(wordbook_url).read()
    urls = re.findall('<a href="(/wordlist/[0-9].*?)">', content)
    urls = ["https://www.shanbay.com" + i for i in urls]
    fw = open(filename, 'w')
    for wordlist_url in urls:
        ws = get_words(wordlist_url)
        fw.write("".join([word + "\n" for word in ws]))
    fw.close()


if __name__ == '__main__':
    # wordlist_urls("https://www.shanbay.com/wordbook/4168/",
                  # filename="50天征服雅思词汇.txt")
    # wordlist_urls("https://www.shanbay.com/wordbook/176896/",
                  # filename="雅思阅读必备词汇.txt")
    # wordlist_urls("https://www.shanbay.com/wordbook/176899/",
                  # filename="雅思考试必备词组.txt")
    # wordlist_urls("https://www.shanbay.com/wordbook/176902/",
                  # filename="雅思听力精选词汇.txt")
    # wordlist_urls("https://www.shanbay.com/wordbook/176905/",
                  # filename="雅思口语必备词.txt")
    # wordlist_urls("https://www.shanbay.com/wordbook/176911/",
                  # filename="雅思写作精选词汇.txt")
    # wordlist_urls("https://www.shanbay.com/wordbook/7/",
                  # filename="IELTS精选词表.txt")
    wordlist_urls("https://www.shanbay.com/wordbook/134146/",
                  filename="托福中级词汇.txt")
    wordlist_urls("https://www.shanbay.com/wordbook/134149/",
                  filename="托福高级词汇.txt")
