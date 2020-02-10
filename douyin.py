import requests


def handle_douyin_share(id):
    share_url = f'https://www.douyin.com/share/user/{id}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    response = requests.get(share_url, headers=headers)
    print(response)


if __name__ == '__main__':
    handle_douyin_share('57720812347')
