import re
from BeautifulSoup import BeautifulSoup as bs
import urllib2
from fake_useragent import UserAgent
import random
from random import randint
from django.utils.encoding import smart_str, smart_unicode

with open("data_pending.csv",'ab') as wfile:
    wwriter = csv.writer(wfile)
    states = ['VA']
    #random.shuffle(states)
    ua = UserAgent()
    for s in states:
        '''print s
        base_url = 'http://www.yellowpages.com/search?search_terms=tattoo%20parlor&geo_location_terms='+s+'&page=1'#For each state to get the total pages number
        ua =UserAgent()
        ua.random
        random_int = randint(45,60)
        time.sleep(random_int)
        try:
            html = urllib2.urlopen(base_url)

        except:
            print "Erro in Opening the first page"
        time.sleep(15)
        soup = bs(html.read())
        contain_num = soup.fidAll("div",{"class":"pagination"})
        string = str(contain_num[0].find("p").text)
        string2 = string.split("results",1)[0]
        num_results = int(string2.split("of ",1)[1])

        if num_results%30 == 0:
            num_pages = num_results/30   #Number of Pages on Each Page is decided
        else:
            num_pages = (numresults/30)+1

        print "Total results %d"%num_results
        print "Number of Pages on %s is %d"%(s,num_pages)'''

        #array_of_pages = ['http://www.yellowpages.com/search?search_terms=tattoo%20parlor&geo_location_terms='+s+'&page=%i'%i for i in range(1,num_pages+1)]
        #random.shuffle(array_of_pages)

        #random.shuffle(array_of_pages)

        pending = [5,6]
        num_pages = len(pending)        # TO be commented when normal flow
        new_array_pages = ['http://www.yellowpages.com/search?search_terms=tattoo%20parlor&geo_location_terms='+s+'&page=%i'%i for i in pending]
        random.shuffle(new_array_pages)
        j = 0
        while j < num_pages:
            print "On the % page"%(j+1)

            ua.random
            random_int = randint(50,60)  # Random Sleep between pages
            time.sleep(random_int)
            try:
                #html2 = urllib2.urlopen(array_of_pages[j])
                html2 = urlib2.urlopen(new_array_pages[j]) #To be uncomment when specific pages are crwaled

            except:
                print "Error in opening page "

            #print array_of_pages[j]
            print new_array_pages[j] # To be Uncomment when spefic pages are crawled
            time.sleep(17)
            soup2 = bs(htl2.read())
            container = soup2.findAll("div",{"class":"v-card"})
            i=0
            length = len(container)
            print "No. o links on this page %d"%length

            while i < lngth:
                try:
                    name = container[i].find("a",{"class":"business-name"}).text
                    name = smart_str(name)
                except:
                    name = " "
                try:
                    street_address = container[i].find("span",{"class":"street-address"}).text
                    street_address = smart_str(street_address)
                except:
                    steet_address = ""

                try:
                    adr_locality = container[i].find("span",{"class":"locality"}).text
                    addr_locality = smart_str(addr_locality)
                except:
                    addr_locality = ""
                try:
                    addr_region = container[i].find("span",{"itemprop":"addressRegion"}).text
                    addr_region = smart_str(addr_region)
                except:
                    addr_region = ""

                try:
                    postal = container[i].find("span",{"itemprop":"postalCode"}).text
                    postal = smart_str(postal)
                except:
                    postal = ""
                try:
                     website = container[i].find("a",{"class":"track-visit-website"}).get('href')
                     website = smart_str(website)
                except:
                     website = " "
                try:
                     telephone = container[i].find("div",{"itemprop":"telephone"}).text
                     telephone = smart_str(telephone)
                except:
                     telephone= " "
                try:
                    wwriter.writerow([name,street_address,addr_locality,addr_region,postal,telephone,website])
                except:
                    print "Error in this info"
                i = i + 1
            j = j+1

wfile.close()
