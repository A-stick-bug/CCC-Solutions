# large part of this problem is input processing, after that, simple BFS
# note: URLs do not always start with http://

import re
from collections import defaultdict, deque

websites = int(input())
graph = defaultdict(list)
site = ""
i = 0
line = input()  # special case: first website

while i <= websites:  # create the graph of website links
    prev = line  # keep track of previous input
    line = input()

    if line.startswith("<HTML>"):
        site = prev
        i += 1
    elif line.endswith("</HTML>") and i == websites:  # last website input
        break
    else:
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', line, flags=re.IGNORECASE)  # 🤓 method to extract links
        for url in urls:
            print(f"Link from {site} to {url}")
        graph[site].extend(urls)


# print(graph)
def bfs(start, end):  # check is it is possible to go from one website to another
    q = deque([start])
    visited = set()
    while q:
        website = q.popleft()
        if website == end:
            return True
        if website in visited:
            continue
        visited.add(website)
        for link in graph[website]:
            q.append(link)
    return False


while True:
    link1 = input()
    if link1 == "The End":
        break
    link2 = input()
    if bfs(link1, link2):
        print(f"Can surf from {link1} to {link2}.")
    else:
        print(f"Can't surf from {link1} to {link2}.")
