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
    assert parse_cookie('yummy_cookie=choco;') == {'yummy_cookie': 'choco'}
    assert parse_cookie('id=a3fWa;expire=Wed;') == {'id': 'a3fWa', 'expire': 'Wed'}
    assert parse_cookie('mykey=myval; same=strict;') == {'mykey': 'myval', 'same': 'strict'}
    assert parse_cookie('#=.') == {'#': '.'}
    assert parse_cookie('dev=%IvanMuratov//') == {'dev': '%IvanMuratov//'}
    assert parse_cookie('tasty_cookie=strawberry') == {'tasty_cookie': 'strawberry'}
    assert parse_cookie('sessionToken=abc123;expire=wed') == {'sessionToken': 'abc123', 'expire': 'wed'}
    assert parse_cookie('restricted_cookie=cookie_value; Domain=PyMOTW') == {'restricted_cookie': 'cookie_value'}
    assert parse_cookie('with_quotes=he/said/Hello/World!')
    assert parse_cookie('USERNAME=foo;PASSWORD=bar') == {'USERNAME': 'foo', 'PASSWORD': 'bar'}
    assert parse_cookie('Content-type=application/x-www-form-urlencoded') == \
           {'Content-type': 'application/x-www-form-urlencoded'}



