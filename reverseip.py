## REVERSE IP LOOKUP - TOR
## WIBU HEKER
## run apt install tor
## run tor
## edit ur /etc/hosts
## add this "199.102.45.110  viewdns.info"
## without "
## open new terminal
## and start this script
## python file.py YOURLIST.txt
import random, requests, re, sys
from multiprocessing import Pool
lists = [i.strip() for i in open(sys.argv[1], 'r').readlines()]
def get_ip(url):
    try:
        session = requests.Session()
        creds = str(random.randint(10000,0x7fffffff)) + ":" + "foobar"
        session.proxies = {'http': 'socks5://{}@localhost:9050'.format(creds), 'https': 'socks5://{}@localhost:9050'.format(creds)}
        session.get('https://viewdns.info/')
        p = session.get('https://viewdns.info/reverseip/?host={}&t=1&submit'.format(url), headers={'User-Agent': 'Mozilla'})
        regex = re.findall('<td>([a-zA-Z0-9-.]+)<\/td>', p.text)
        for site in regex:
            if site == "Domain":
                pass
            print(site)
            f = open('result.txt', 'a+')
            f.write(site  + "\n")
            f.close()
    except:
        print(url + " ERROR!")
pool = Pool(8)
pool.map(get_ip, lists)
pool.close()
pool.join()
