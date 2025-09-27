import requests

def request(url, output_file):
    try:
        response = requests.get("https://" + url)
        if response.status_code == 200:
            print("[+] subdomain discovered ----> " + url)
            output_file.write(url + "\n")
    except requests.RequestException:
        pass

def main():
    tc = "youtube.com"
    with open("text.txt", "r") as wordlist, open("domain.txt", "a") as output_file:
        for line in wordlist:
            word = line.strip()
            test_url = word + "." + tc
            request(test_url, output_file)

main()