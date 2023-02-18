from http.cookies import SimpleCookie


def parsed(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parsed('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parsed('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parsed('http://example.com/') == {}
    assert parsed('http://example.com/?') == {}
    assert parsed('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    return {k: v.value for k, v in cookie.items()}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
