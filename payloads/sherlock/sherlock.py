"""
Made by adjidev 2024
Hapus watermark lu jadi orang terkontol di seluruh dunia
"""

import argparse
import shutil
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
import urllib.request
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup4 module not found. Installing...")
    subprocess.check_call(["pip", "install", "bs4"])
    from bs4 import BeautifulSoup
import ssl
import threading
from datetime import datetime

red = '\033[31m'       
green = '\033[32m'     
yellow = '\033[33m'    
blue = '\033[34m'      
magenta = '\033[35m'   
cyan = '\033[36m'      
white = '\033[37m'     
black = '\033[30m'     
bright_red = '\033[91m' 
bright_green = '\033[92m'
bright_yellow = '\033[93m' 
bright_blue = '\033[94m'   
bright_magenta = '\033[95m' 
bright_cyan = '\033[96m'    
bright_white = '\033[97m'   
bg_black = '\033[40m'    
bg_red = '\033[41m'      
bg_green = '\033[42m'    
bg_yellow = '\033[43m'   
bg_blue = '\033[44m'     
bg_magenta = '\033[45m'  
bg_cyan = '\033[46m'     
bg_white = '\033[47m'    
reset = '\033[0m'

def TheBanner():
    banner = f""" _____ _____ _____ _____ __    _____ _____ _____ 
|   __|  |  |   __| __  |  |  |     |     |  |  |
|__   |     |   __|    -|  |__|  |  |   --|    -|
|_____|__|__|_____|__|__|_____|_____|_____|__|__|
@adjisan"""
    
    width, _ = shutil.get_terminal_size()
    
    lines = banner.split('\n')
    
    for line in lines:
        spaces = (width - len(line)) // 2
        print(cyan + ' ' * spaces + line + reset)

ingfo = f"""Sherlock Project made by @adjisan\n{yellow}TELEGRAM{reset} :  https://t.me/adjidev\n"""

sslContent = ssl._create_unverified_context()

# facebook and vk is not allowed due to security reason
medsos = [
    {"url": "https://www.twitter.com/{}", "name": "Twitter"},
    {"url": "https://www.instagram.com/{}", "name": "Instagram"},
    {"url": "https://www.github.com/{}", "name": "GitHub"},
    {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
    {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
    {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
    {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
    {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
    {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
    {"url": "https://www.behance.net/{}", "name": "Behance"},
    {"url": "https://www.medium.com/@{}", "name": "Medium"},
    {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
    {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
    {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
    {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
    {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
    {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
    {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
    {"url": "https://www.telegram.me/{}", "name": "Telegram"},
    {"url": "https://www.weheartit.com/{}", "name": "We Heart It"},
    {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
    {"url": "https://www.discord.com/{}", "name": "Discord"},
    {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
    {"url": "https://www.clubhouse.com/@{}", "name": "Clubhouse"},
    {"url": "https://www.mix.com/{}", "name": "Mix"},
    {"url": "https://www.yelp.com/user_details?userid={}", "name": "Yelp"},
    {"url": "https://www.reverbnation.com/{}", "name": "ReverbNation"},
    {"url": "https://www.soundcloud.com/{}", "name": "SoundCloud"},
    {"url": "https://www.foursquare.com/{}", "name": "Foursquare"},
    {"url": "https://www.meetup.com/members/{}", "name": "Meetup"},
    {"url": "https://www.slack.com/{}", "name": "Slack"},
    {"url": "https://www.goodreads.com/{}", "name": "Goodreads"},
    {"url": "https://hackaday.io/{}", "name": "Hackaday"},
    {"url": "https://gitlab.com/{}", "name": "Gitlab"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Connection": "keep-alive",
}

def Loading(delay=0.012):
    spinner = ['|', '/', '-', '\\']
    while not stop_loading[0]:  
        for symbol in spinner:
            sys.stdout.write(f'\rSearching . . . {symbol}')  
            sys.stdout.flush()  
            time.sleep(delay)
    sys.stdout.write(f'\r                                                                \n')

def CheckPages(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        adjisan = urllib.request.urlopen(req, context=sslContent)
        PagesContent = adjisan.read()

        if adjisan.getcode() == 404:
            return True

        soup = BeautifulSoup(PagesContent, 'html.parser')

        not_found_texts = [
            "This page doesn’t exist", "Page not found", 
            "Sorry, we couldn’t find that page", 
            "We’re sorry. Something went wrong on this page.",
            "404",
            "The requested URL was not found"
        ]
        
        for text in not_found_texts:
            if soup.body and text.lower() in soup.body.get_text().lower():
                return True
        return False
    except HTTPError as e:
        if e.code == 404:
            return True
        pass
        return True
    except URLError as e:
        pass
        return True
    except Exception as e:
        pass
        return True

def sherlock(username, simpan=None):
    data = []
    TheBanner()
    print(ingfo)
    print(f"[{yellow}INFO{reset}] Searching username: {username}")
    total_found = 0
    for platform in medsos:
        profile_url = platform["url"].format(username)
        
        stop_loading[0] = False
        loading_thread = threading.Thread(target=Loading, args=(0.1,))
        loading_thread.start()

        try:
            if CheckPages(profile_url):
                stop_loading[0] = True
                loading_thread.join()
                print(f"[{red}BAD{reset}] {platform['name']}: {yellow}{profile_url}{reset}")
            else:
                stop_loading[0] = True 
                loading_thread.join()
                rslt = f"Type: {platform['name']}\nName: {username}\nUrl     : {profile_url}\n"
                print(f"[{green}OK{reset}] {platform['name']}: {yellow}{profile_url}{reset}")
                data.append(rslt)
                total_found += 1
        except KeyboardInterrupt:
            stop_loading[0] = True
            loading_thread.join()
            print(f'[{yellow}INFO{reset}] Interrupted by users.')
            sys.exit(1)
        except Exception as e:
            stop_loading[0] = True 
            loading_thread.join()
            pass

    print(f"\n[{yellow}INFO{reset}] Showing {green}{total_found}{yellow} results{reset}, do you want to save result? ({yellow}Y{reset}/{yellow}N{reset})")
    question = input('> ')
    if question.lower() == 'y':
        if simpan:
            with open(simpan, 'w') as f:
                f.writelines(data)
                print(f'[{yellow}INFO{reset}] Data saved to \'{simpan}\'')
        else:
            files = 'results.txt'
            with open(files, 'w') as f:
                f.writelines(data)
                print(f'[{yellow}INFO{reset}] Data saved to \'{files}\'')
    else:
        print(f'[{yellow}INFO{reset}] Exiting without saving.')
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Search for a username across various social media platforms.')
    parser.add_argument('--search', type=str, required=True, help='The username to search for on social media.')
    parser.add_argument('--save', type=str, help='File to save the result')

    args = parser.parse_args()
    sherlock(args.search, args.save)

stop_loading = [False]

if __name__ == "__main__":
    main()
