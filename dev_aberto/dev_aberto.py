import requests
from babel.dates import format_datetime
import datetime

def hello():
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    commit_info = info[0]['commit']['author']
    d = commit_info['date'].replace('T', '-').replace(':', '-').replace('Z', '').split("-")
    date = datetime.datetime(int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]))
    return format_datetime(date), commit_info['name']
