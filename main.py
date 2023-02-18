from http.cookies import SimpleCookie
from urllib import parse


def parsed(query: str) -> dict:
    parse.urlsplit(query)
    parse.parse_qs(parse.urlsplit(query).query)
    return dict(parse.parse_qsl(parse.urlsplit(query).query))


if __name__ == '__main__':
    assert parsed('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parsed('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parsed('http://example.com/') == {}
    assert parsed('http://example.com/?') == {}
    assert parsed('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parsed('http://example.com/?name=Ivan%20Muratov') == {'name': 'Ivan Muratov'}
    assert parsed('https://elmir.ua/?module=compare') == {'module': 'compare'}
    assert parsed('https://elmir.ua/ua/?q=intel%20core%20i9') == {'q': 'intel core i9'}
    assert parsed('https://www.google.com/search?q=being+a+developer&oq=be') == {'q': 'being a developer', 'oq': 'be'}
    assert parsed('https://dictionary.cambridge.org/advanced?utm_source=cdo') == {'utm_source': 'cdo'}
    assert parsed('https://epicentrk.ua/ua/actions/?SECTION_ID=5417') == {'SECTION_ID': '5417'}
    assert parsed('https://www.codewars.com/join?country=us') == {'country': 'us'}
    assert parsed('https://github.com/MKD/pro/issues?q=is%3Aissue+is%3A') == {'q': 'is:issue is:'}
    assert parsed('https://twitter.com/intent/tweet?text=Separate%20receipts') == {'text': 'Separate receipts'}
    assert parsed('https://github.blog/?s=tkinter') == {'s': 'tkinter'}


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    return {k: v.value for k, v in cookie.items()}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
