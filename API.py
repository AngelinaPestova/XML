from urllib.request import urlopen
from json import loads
from itertools import groupby
from collections import OrderedDict


def date_key(revision):
    return revision['timestamp'][:10]


def group_by_date(revisions):
    return list((date, len(list(records))) for date, records in groupby(revisions, key=date_key))


def main():
    url_Gradsky = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    number_Gradsky = '183903'
    url_Belmondo = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
    number_Belmondo = '192203'
    revisions = loads(urlopen(url_Belmondo).read().decode('utf8'))['query']['pages'][number_Belmondo]['revisions']
    grouped_revisions = sorted(group_by_date(revisions), key=lambda d: -d[1])
    for record in grouped_revisions:
        print(record[0], record[1])


if __name__ == '__main__':
    main()

