import pytest
import io

try:
    import compute
except:
    from . import compute

TEXT = \
r'''""
"abc"
"aaa\"aaa"
"\x27"
'''

CHARS = (2, 5, 10, 6)
DATAS = (0, 3, 7, 1)
ENCODES = (6, 9, 16, 11)
TOTAL_CHARS = sum(CHARS)
TOTAL_MEM = sum(DATAS)
TOTAL_ENCODES = sum(ENCODES)

def get_file_from_text(text):
    return io.StringIO(text)

def get_lines(text):
    with text as fp:
        lines = fp.read()
        return([s for s in lines.split()])

STATS = list(zip(
        get_lines(get_file_from_text(TEXT)), CHARS, DATAS, ENCODES
))

@pytest.mark.parametrize(
        'string,chars,data, encodes',
        STATS
)
def test_get_total_chars_per_string(string, chars, data, encodes):
    assert chars == compute.get_total_chars(string)

def test_get_total_chars():
    with get_file_from_text(TEXT) as fp:
        lines = fp.read()
    assert compute.get_total_chars(lines) == TOTAL_CHARS

@pytest.mark.parametrize(
        'string,chars,data,encodes',
        STATS
)
def test_get_total_mem_per_string(
        string, chars, data, encodes
):
    print(string, chars, data)
    assert data == compute.get_total_mem(string)

def test_get_total_mem():
    with get_file_from_text(TEXT) as fp:
        lines = fp.read()
    # print(lines)
    assert compute.get_total_mem(lines) == TOTAL_MEM


@pytest.mark.parametrize(
        'string,chars,data,encodes',
        STATS
)
def test_get_total_encode_per_string(
        string, chars, data, encodes
):
    print(string, chars, data, encodes)
    assert encodes == compute.get_total_encoded(string)


def test_get_total_encode():
    with get_file_from_text(TEXT) as fp:
        lines = fp.read()
    # print(lines)
    assert compute.get_total_encoded(lines) == TOTAL_ENCODES
