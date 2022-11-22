import pytest

from qpyone.validation import url
from qpyone.validation.utils import ValidationFailure


@pytest.mark.parametrize(
    "address",
    [
        "http://foobar.dk",
        "http://foobar.museum/foobar",
        "http://fo.com",
        "http://FOO.com",
        "http://foo.com/blah_blah",
        "http://foo.com/blah_blah/",
        "http://foo.com/blah_blah_(wikipedia)",
        "http://foo.com/blah_blah_(wikipedia)_(again)",
        "http://www.example.com/wpstyle/?p=364",
        "https://www.example.com/foo/?bar=baz&inga=42&quux",
        "https://www.example.com?bar=baz",
        "http://✪df.ws/123",
        "http://userid:password@example.com:8080",
        "http://userid:password@example.com:8080/",
        "http://userid@example.com",
        "http://userid@example.com/",
        "http://userid@example.com:8080",
        "http://userid@example.com:8080/",
        "http://userid:password@example.com",
        "http://userid:password@example.com/",
        "http://142.42.1.1/",
        "http://142.42.1.1:8080/",
        "http://➡.ws/䨹",
        "http://⌘.ws",
        "http://⌘.ws/",
        "http://foo.com/blah_(wikipedia)#cite-1",
        "http://foo.com/blah_(wikipedia)_blah#cite-1",
        "http://foo.com/unicode_(✪)_in_parens",
        "http://foo.com/(something)?after=parens",
        "http://☺.damowmow.com/",
        "http://code.google.com/events/#&product=browser",
        "http://j.mp",
        "ftp://foo.bar/baz",
        "http://foo.bar/?q=Test%20URL-encoded%20stuff",
        "http://مثال.إختبار",
        "http://例子.测试",
        "http://उदाहरण.परीक्षा",
        "http://www.😉.com",
        "http://😉.com/😁",
        "http://উদাহরণ.বাংলা",
        "http://xn--d5b6ci4b4b3a.xn--54b7fta0cc",
        "http://дом-м.рф/1/asdf",
        "http://xn----gtbybh.xn--p1ai/1/asdf",
        "http://-.~_!$&'()*+,;=:%40:80%2f::::::@example.com",
        "http://1337.net",
        "http://a.b-c.de",
        "http://223.255.255.254",
        "http://10.1.1.0",
        "http://10.1.1.1",
        "http://10.1.1.254",
        "http://10.1.1.255",
        "http://127.0.0.1:8080",
        "http://127.0.10.150",
        "http://localhost",
        "http://localhost:8000",
        "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html",
        "http://[1080:0:0:0:8:800:200C:417A]/index.html",
        "http://[3ffe:2a00:100:7031::1]",
        "http://[1080::8:800:200C:417A]/foo",
        "http://[::192.9.5.5]/ipng",
        "http://[::FFFF:129.144.52.38]:80/index.html",
        "http://[2010:836B:4179::836B:4179]",
    ],
)
def test_returns_true_on_valid_url(address):
    assert url(address)


@pytest.mark.parametrize(
    "address, public",
    [
        ("http://foo.bar", True),
        ("http://username:password@example.com:4010/", False),
        ("http://username:password@112.168.10.10:4010/", True),
        ("http://username:password@192.168.10.10:4010/", False),
        ("http://10.0.10.1", False),
        ("http://127.0.0.1", False),
    ],
)
def test_returns_true_on_valid_public_url(address, public):
    assert url(address, public=public)


@pytest.mark.parametrize(
    "address",
    [
        "http://foobar",
        "foobar.dk",
        "http://127.0.0/asdf",
        "http://foobar.d",
        "http://foobar.12",
        "http://foobar",
        "htp://foobar.com",
        "http://foobar..com",
        "http://fo..com",
        "http://",
        "http://.",
        "http://..",
        "http://../",
        "http://?",
        "http://??",
        "http://??/",
        "http://#",
        "http://##",
        "http://##/",
        "http://foo.bar?q=Spaces should be encoded",
        "//",
        "//a",
        "///a",
        "///",
        "http:///a",
        "foo.com",
        "rdar://1234",
        "h://test",
        "http:// shouldfail.com",
        ":// should fail",
        "http://foo.bar/foo(bar)baz quux",
        "ftps://foo.bar/",
        "http://-error-.invalid/",
        "http://a.b--c.de/",
        "http://-a.b.co",
        "http://a.b-.co",
        "http://0.0.0.0",
        "http://224.1.1.1",
        "http://1.1.1.1.1",
        "http://123.123.123",
        "http://3628126748",
        "http://.www.foo.bar/",
        "http://www.foo.bar./",
        "http://.www.foo.bar./",
        "http://127.12.0.260",
        'http://example.com/">user@example.com',
        "http://[2010:836B:4179::836B:4179",
        "http://2010:836B:4179::836B:4179",
        "http://2010:836B:4179::836B:4179:80/index.html",
    ],
)
def test_returns_failed_validation_on_invalid_url(address):
    assert isinstance(url(address), ValidationFailure)


@pytest.mark.parametrize(
    "address, public",
    [
        ("http://username:password@192.168.10.10:4010/", True),
        ("http://10.0.10.1", True),
        ("http://127.0.0.1", True),
        ("foo://127.0.0.1", True),
        ("http://username:password@127.0.0.1:8080", True),
        ("http://localhost", True),
        ("http://localhost:8000", True),
    ],
)
def test_returns_failed_validation_on_invalid_public_url(address, public):
    assert isinstance(url(address, public=public), ValidationFailure)
