from bs4 import BeautifulSoup
import requests
import json
import time

repo = "pyserial/pyserial"
PAUSE_BEFORE_NEXT_PAGE = 0.3
PAGE_NUM = 300
url = 'https://github.com/{}/network/dependents'.format(repo)

repo_list = list()

for i in range(PAGE_NUM):
    print("GET " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    for t in soup.findAll("div", {"class": "Box-row"}):
        stargazers = t.find('svg', {'class': 'octicon-star'}).parent.text
        data = {
            'repo': "{}/{}".format(
                t.find('a', {"data-repository-hovercards-enabled": ""}).text,
                t.find('a', {"data-hovercard-type": "repository"}).text
            ),
            'stargazers': int(f"{''.join(e for e in stargazers if e.isalnum())}"),

        }

        repo_list.append(data)

    next_page = soup.find_all("a", string="Next")

    if next_page:
        url = next_page[0]["href"]
    else:
        break
    time.sleep(PAUSE_BEFORE_NEXT_PAGE)

repo_list_sorted = sorted(repo_list, key=lambda d: d['stargazers'])
print('Total items:', len(repo_list), '\n', 'Objects:', repo_list_sorted)

with open(f'{repo.split("/")[1]}_stargazers.json', 'a+') as f:
    f.write(json.dumps(repo_list_sorted, indent=4, ensure_ascii=False))
