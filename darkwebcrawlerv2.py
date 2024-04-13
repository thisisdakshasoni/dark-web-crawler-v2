import subprocess
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import random
import re
import csv
import time
import dns.resolver
import sys
from time import sleep
from pprint import pprint
import concurrent.futures

class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)

def entryy():
    x = color_random[0] + """
          _____                   _______                   _____                    _____                    _____                    _____          
         /\    \                 /::\    \                 /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\               /::::\    \               /::\____\                /::\    \                /::\    \                /::\    \        
       /:::/    /              /::::::\    \             /::::|   |               /::::\    \              /::::\    \              /::::\    \       
      /:::/    /              /::::::::\    \           /:::::|   |              /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/    /              /:::/~~\:::\    \         /::::::|   |             /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/____/              /:::/    \:::\    \       /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \    
   /::::\    \             /:::/    / \:::\    \     /:::/ |::|   |            \:::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \   
  /::::::\    \   _____   /:::/____/   \:::\____\   /:::/  |::|   | _____    ___\:::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \  
 /:::/\:::\    \ /\    \ |:::|    |     |:::|    | /:::/   |::|   |/\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \ 
/:::/  \:::\    /::\____\|:::|____|     |:::|    |/:: /    |::|   /::\____\/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/____/     \:::\____\
\::/    \:::\  /:::/    / \:::\    \   /:::/    / \::/    /|::|  /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\:::\    \      \::/    /
 \/____/ \:::\/:::/    /   \:::\    \ /:::/    /   \/____/ |::| /:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \:::\    \      \/____/ 
          \::::::/    /     \:::\    /:::/    /            |::::::/    /    \:::\   \:::\    \       \:::\   \:::\    \       \:::\    \             
           \::::/    /       \:::\__/:::/    /             |:::::/    /      \:::\   \:::\____\       \:::\   \:::\____\       \:::\    \            
           /:::/    /         \::::::::/    /              |::::/    /        \:::\  /:::/    /        \:::\   \::/    /        \:::\    \           
          /:::/    /           \::::::/    /               /:::/    /          \:::\/:::/    /          \:::\   \/____/          \:::\    \          
         /:::/    /             \::::/    /                /:::/    /            \::::::/    /            \:::\    \               \:::\    \         
        /:::/    /               \::/____/                /:::/    /              \::::/    /              \:::\____\               \:::\____\        
        \::/    /                 ~~                      \::/    /                \::/    /                \::/    /                \::/    /        
         \/____/                                           \/____/                  \/____/                  \/____/                  \/____/         

\n"""
    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in oo:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    tt = " " * 6 + "░⣿" + " " * 18 + "DEEP-WEB GUARDIAN" + " " * 11 + "░⣿" + "\n\n"
    for c in tt:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in xx:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

def choose_option():
    """
    Presents options for different functionalities.
    """
    print('[+] Choose an Option:')
    print('[1] Scrape from Single URL')
    print('[2] Onion Link Finder')
    print('[3] Vulnerability Scanning (XSS)')
    print('[4] Extract Emails')
    print('[5] Link Analysis')
    print('[6] Website Scanning')
    print('[0] Exit')
    option = input('[+] Enter Option No. -> ')
    return option

def scrape_single_url(url):
    """
    Scrapes website URL provided by the user.
    """
    try:
        # Check if the URL starts with http:// or https://, if not, add it
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url

        response = session.get(url).text
        soup = bs(response, 'html.parser')
        extract_and_analyze_links(url, soup)  # Perform link analysis
    except requests.exceptions.RequestException as e:
        print('[!] Error scraping URL {}: {}'.format(url, e))
    except Exception as e:
        print('[!] An error occurred during scraping:', e)

def extract_and_analyze_links(url, soup):
    """
    Extracts links from the webpage and performs link analysis.
    """
    links = soup.find_all('a', href=True)
    internal_links = []
    external_links = []
    broken_links = []

    for link in links:
        href = link['href']
        full_url = urljoin(url, href)
        try:
            response = session.head(full_url, allow_redirects=True)
            status_code = response.status_code
            if 200 <= status_code < 400:
                if full_url.startswith('http://' + url) or full_url.startswith('https://' + url):
                    internal_links.append(full_url)
                else:
                    external_links.append(full_url)
            else:
                broken_links.append((full_url, status_code))
        except requests.exceptions.RequestException:
            broken_links.append((full_url, 'Error'))

    display_link_analysis(internal_links, external_links, broken_links)

def display_link_analysis(internal_links, external_links, broken_links):
    """
    Displays the results of link analysis.
    """
    print('[+] Link Analysis Results:')
    print('Internal Links:')
    for link in internal_links:
        print('  -', link)
    print('External Links:')
    for link in external_links:
        print('  -', link)
    print('Broken Links:')
    for link, status_code in broken_links:
        print('  -', link, '[Status Code:', status_code, ']')

def onion_link_finder():
    """
    Scrapes onion links from ahmia.fi search results.
    """
    user_query = input("[+] Enter your query: ")
    scraper(user_query)

def scan_xss(url):
    """
    Given a `url`, it prints all XSS vulnerable forms and
    returns True if any is vulnerable, False otherwise
    """
    try:
        response = session.get(url)
        soup = bs(response.content, 'html.parser')
        forms = soup.find_all('form')
        
        if forms:  # Check if forms exist before processing
            js_script = "<script>alert('XSS')</script>"
            is_vulnerable = False

            for form in forms:
                form_html = str(form)
                if js_script in form_html:
                    print(f"[+] XSS Detected on {url}")
                    print(f"[*] Form HTML:")
                    print(form_html)
                    is_vulnerable = True

            if not is_vulnerable:
                print(f"[+] No XSS Vulnerabilities detected on {url}")
            
            return is_vulnerable
        else:
            print("[+] No forms found on the webpage. Skipping XSS scanning.")
            return False

    except requests.exceptions.RequestException as e:
        print("[!] An error occurred during XSS scanning:", e)
        return False

def website_scanning(url=None):
    """
    Scans the specified website URL for specific keywords.
    """
    try:
        if url is None:
            url = input('[+] Enter the website URL to scan: ')

        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            keywords = ['vulnerability', 'security', 'attack', 'exploit']  # Add more keywords as needed
            found_keywords = []

            # Check for presence of keywords in the webpage content
            for keyword in keywords:
                if re.search(r'\b{}\b'.format(keyword), html_content, re.IGNORECASE):
                    found_keywords.append(keyword)

            if found_keywords:
                print('[+] Found the following keywords on {}:'.format(url))
                for keyword in found_keywords:
                    print('- {}'.format(keyword))
            else:
                print('[+] No relevant keywords found on {}'.format(url))
        else:
            print('[!] Failed to fetch webpage content from {}'.format(url))
    except Exception as e:
        print('[!] An error occurred during website scanning:', e)

def scraper(query):
    if " " in query:
        query = query.replace(" ", "+")

    url = "https://ahmia.fi/search/?q={}&uio=mt&sort=time".format(query)

    page = session.get(url).text
    soup = bs(page, 'html.parser')
    links = soup.find_all("a")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scraper_job, links)

def scraper_job(link):
    try:
        href = link.get("href")
        if href and href.startswith("/"):
            link = f"https://ahmia.fi{href}"
            page = session.get(link).text
            soup = bs(page, 'html.parser')
            title = soup.find("title")
            if title:
                title = title.text
                if "not found" in title.lower():
                    return
                print(link)
                print(title)
                print("="*50)
    except Exception as e:
        pass

def extract_emails_from_url(url):
    """
    Extracts emails from the HTML content of a given URL.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            emails = set()
            # Regular expression pattern for email addresses
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
            # Find all text containing potential email addresses
            matches = email_pattern.findall(html_content)
            for match in matches:
                emails.add(match)
            return emails
        else:
            print('[!] Failed to fetch webpage content from', url)
            return set()  # Return an empty set in case of errors
    except Exception as e:
        print('[!] An error occurred during email extraction:', e)
        return set()  # Return an empty set in case of errors

def main():
    try:
        entryy()
        while True:
            option = choose_option()
            if option == '1':
                url = input('[+] Enter the URL to scrape: ')
                scrape_single_url(url)
            elif option == '2':
                onion_link_finder()
            elif option == '3':
                url = input('[+] Enter the URL to scan for XSS vulnerability: ')
                scan_xss(url)  # Remove `proxies` argument
            elif option == '4':
                url = input('[+] Enter the URL to extract emails from: ')
                extracted_emails = extract_emails_from_url(url)
                if extracted_emails:
                    print('Extracted Emails:')
                    for email in extracted_emails:
                        print(email)
                else:
                    print('No emails found on the webpage.')
            elif option == '5':
                # Add option to perform link analysis
                print("Option 5 selected - Link Analysis")
            elif option == '6':
                website_scanning()
            elif option == '0':
                print('[+] Exiting...')
                break
            else:
                print('[!] Invalid Option. Please choose a valid option.')
    except KeyboardInterrupt:
        print('\n[+] Exiting...')


if __name__ == "__main__":
    main()
