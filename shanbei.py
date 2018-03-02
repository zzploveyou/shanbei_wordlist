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
    wordlist_urls("https://www.shanbay.com/wordbook/4168/",
                  filename="words.txt")
