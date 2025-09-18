import requests

def request(url):
    try:
        ty=requests.get("http://" + url)
        if(result):
            print("[+] subdomin  discovered ---->" + url)
    except:
        pass


def main():
    tc = "googlo.com"

    with open ("text.txt" , "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            test_url = word + "." + tc 
            request(test_url)

main()

