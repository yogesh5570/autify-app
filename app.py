import argparse
from pywebcopy import save_webpage
from pywebcopy.parsers import MultiParser
import requests
from datetime import datetime
import json

def split_url(url):
    if 'http' in url:
        project_name = url.split('//')[1]
    else:
        project_name = url

    return project_name

def save_all_webpage_assets(project_name):
    save_webpage(
        url=url,
        project_folder="./clone",
        project_name=project_name,
        bypass_robots=True,
        debug=False,
        open_in_browser=False,
        delay=None,
        threaded=False,
    )

def save_metadata(wp, filename):
    imgs = []
    href_list = []
    obj.update({'site': url})
    
    for link in wp.bs4.find_all('a'):
        temp = link.get('href')
        if 'http' in temp:
            href_list.append(temp)
    obj.update({'num_links': len(href_list)})

    for img in wp.bs4.find_all('img'):
        imgs.append(img.get('src'))
    obj.update({'images': len(imgs)})

    utc_time = datetime.utcnow()
    obj.update({'last_fetch': utc_time.strftime('%a %b %d %Y %H:%M UTC')})

    data = {}
    try:
        with open('metadata.json', 'rb') as f:
            data = json.load(f)
    except Exception as e:
        pass

    with open('metadata.json', 'wb') as f:
        site = {url: obj}
        for key in data.keys():
            site.update({key: data[key]})
        temp = json.dumps(site, indent=2).encode('utf-8')
        f.write(temp)

def save_html_file(filename):
    with open(f'{filename}.html', 'wb') as f:
        f.write(html)

def get_metadata(url):
    try:
        with open('metadata.json', 'rb') as f:
            data = json.load(f)
            for key in data.keys():
                if url in key:
                    return data[key]

            return f"No metadata found for {url}"
    except Exception as e:
        print(e)

parser = argparse.ArgumentParser(description="Clone Websites")

parser.add_argument('Websites', metavar="URL", type=str, nargs="*", help="Website URL to Fetch data")
parser.add_argument('--metadata', action='store', default="", nargs="*", help="Fetch Meta Data of URL passed")

args = parser.parse_args()
if args.metadata:
    res = []
    for url in args.metadata:
        result = get_metadata(url)
        res.append(result)
    print(res)

else:
    print("Processing...")
    for url in args.Websites:
        try:
            project_name = split_url(url)
            req = requests.get(url)
            html = req.content
            filename = project_name
            obj = {}
            encoding = req.encoding
            wp = MultiParser(html, encoding)

            save_all_webpage_assets(project_name)
            save_metadata(wp, filename)
            save_html_file(filename)
    
        except Exception as e:
            print(e)
    print("Process Completed")