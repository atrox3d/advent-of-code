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
TOTAL_CHARS = 23
TOTAL_MEM = 11

def get_file_from_text(text):
    return io.StringIO(text)

def get_lines(text):
    with text as fp:
        lines = fp.read()
        return([s for s in lines.split()])

STATS = list(zip(
        get_lines(get_file_from_text(TEXT)), CHARS, DATAS
))

@pytest.mark.parametrize(
        'string,chars,data',
        STATS
)
def test_get_total_chars_per_string(string, chars, data):
    assert chars == compute.get_total_chars(string)

def test_get_total_chars():
    with get_file_from_text(TEXT) as fp:
        lines = fp.read()
    assert compute.get_total_chars(lines) == TOTAL_CHARS

@pytest.mark.parametrize(
        'string,chars,data',
        STATS
)
def test_get_total_mem_per_string(
        string, chars, data
):
    print(string, chars, data)
    assert data == compute.get_total_mem(string)

def test_get_total_mem():
    with get_file_from_text(TEXT) as fp:
        lines = fp.read()
    # print(lines)
    assert compute.get_total_mem(lines) == TOTAL_MEM
