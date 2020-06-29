import requests

def getHTMLTest(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding        #apparent可以手动分析，节省时间
        return r.text
    except:
        return ''

if __name__ == '__main__':
    txt = getHTMLTest('https://www.tianyancha.com/search?key=中国华戎科技集团有限公司')
    print(len(txt))
    print(type(txt))
    with open('temp.txt', 'w') as f:
        f.write(txt)