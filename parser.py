# coding: utf-8
import urllib
from bs4 import BeautifulSoup
import re

def genHTML(content, fn):
   fout = open(fn, "w")
   fout.write("<html lang=\"zh-cn\">\n<head>\n<meta charset=\"utf-8\"/>\n");
   fout.write(content)
   fout.write("\n</html>");
   fout.close()


def getPostDetails(content):
   soup = BeautifulSoup(content, 'html.parser')
   div_content = soup.find('div', {'class' : 'post'})
   new_div = re.sub(".*leetcode.com/problem.*\n?","", str(div_content))
   return new_div

def truncatePost(post):
   paras = re.split(str, post.decode('utf-8'))
   print len(paras)
   return paras[0].encode('utf-8')
      
def getRefFromPage(content):
#   fin = open(problem_page, "r");
#   content = fin.read();
#   fin.close();
#   soup = BeautifulSoup(content, 'html.parser')
#   links = soup.find_all(href=re.compile("https://www.cnblogs.com/grandyang/p/[0-9]+.html"))
   pattern = re.compile("http[s]*://www.cnblogs.com/grandyang/p/[0-9]+.html")
   
   return re.findall(pattern, content)

def getPage(url):
    page = urllib.urlopen(url);
    return page.read();

#content = getPage("http://www.cnblogs.com/grandyang/p/4606334.html")
#fout = open("./index.html", "w");
#fout.write(content);
#fout.close();
#links = getRefFromPage(content);
#fout = open("problems.txt", "w");
#fout.write("\n".join(links));
#fout.close();
content = ""
cnt = 0
with open("problems.txt", "r") as fp:
    for line in fp.readlines():
        print(cnt)
        if cnt < 500:
            cnt += 1
            continue
        if cnt % 100 == 0:
            genHTML(content, "leet%d.html" % cnt)
            content = ""
        content += getPostDetails(getPage(line))
        import random
        import time
        cnt += 1
        time.sleep(random.randint(2,6))  

genHTML(content, "leet%d.html" % cnt)
