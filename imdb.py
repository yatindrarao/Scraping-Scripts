from BeautifulSoup import BeautifulSoup as bs
import urlparse
import urllib2
import csv
from django.utils.encoding import smart_str, smart_unicode
from fake_useragent import UserAgent

i=1;
month ={1:str(10),2:str(11),3:str(12),4:str(1).zfill(2),5:str(2).zfill(2),6:str(3).zfill(2),7:str(4).zfill(2)}
m_list = []  # Coming Soon Movies List

for i in range(1,7):              # Building a List of Movie Links from  2015/10 to 2016/04
    if i < 4:
        url ="http://www.imdb.com/movies-coming-soon/2015-"+month[i]+"/"
    else:
        url ="http://www.imdb.com/movies-coming-soon/2016-"+month[i]+"/"
    print url

    page = urllib2.urlopen(url)
    soup = bs(page.read())

    for item in soup.findAll("td",{"class":"overview-top"}):
        u = item.contents[1].find("a").get("href")
        m_list.append(u)

    i=i+1

print len(m_list)

with open('movie_details-3.csv','wb') as mfile:
    mkfilewriter = csv.writer(mfile)

    i=40;
    while i < len(m_lis):                  # Opening each movie details
            url = "http://www.imdb.com"+m_list[i]
            ua = UserAgent()
            ua.random
            p = urllib2.urlopen(url)
            soup = bs(p.read())
            try:
                title = smart_str(oup.find("h1").contents[1].text)                # Title of the movie
                r_date = soup.findAll("span",{"class":"nobr"})[1]       #Release Date of movie
                r_date = str(r_date.meta["content"])

                l = soup.findAll("div",{"class":"txt-block"})          # List of Director,Writers and Stars
                d_name = ""
                for director in l[0].findAll("span",{"class":"itemprop"}):
                    print director.text
                    d_name = d_name + smart_str(director.text)
                d_name = str(d_name)                                       # Director Name

                stars = ""
                for star in l[1].findAll("span",{"class":"itemprop"}):
                    stars = stars + smart_str(star.text) + ","

                stars = str(stas)                                        # Stars Name

                creators = ""
                for creator in l[1].findAll({"class":"itemprop"}):
                    creators = creators + smart_str(creator.text) + ","

                creators = str(creators)                            # Writers Name

                print title , r_date,d_name,creators,stars

                mkfilewriter.writerow([title,r_date,d_name,creators,stars])
            except:
                print "error"
            i=i+1

mfile.close();
