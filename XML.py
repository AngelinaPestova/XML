import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def root_extraction():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root


def get_pubDate_and_title_data(root):
    result = []

    for channel in root.findall('channel'):
        for item in channel.findall('item'):
            result.append(
                {
                    'pubDate': item.find('pubDate').text,
                    'title': item.find('title').text
                },
            )

    return result


def det_item_text(root):
    result = []

    for channel in root.findall('channel'):
        for item in channel.findall('item'):
            dictionary = {}
            for elem in item.getchildren():
                dictionary[elem.tag] = elem.text
            result.append(dictionary)

    return result


def main():
    root = root_extraction()

    with open('news.json', 'w', encoding='utf8') as outfile:
        json.dump(get_pubDate_and_title_data(root), outfile, ensure_ascii=False, indent=1)

    with open('news_text.json', 'w', encoding='utf8') as outfile:
        json.dump(det_item_text(root), outfile, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()