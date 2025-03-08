from ..img import Img


def test_img():
    s = {'args': [{'value': ''}, {'value': 300}]}
    Img().parse(s, {})
    assert s.get('width') == 300

    s = {'args': [{'value': ''}, {'value': 'h100'}]}
    Img().parse(s, {})
    assert s.get('height') == 100

    s = {'args': [{'value': ''}, {'value': 'x100'}]}
    Img().parse(s, {})
    assert s.get('height') == 100

    s = {'args': [{'value': ''}, {'value': 'link'}]}
    Img().parse(s, {})
    assert s.get('show') == 'link'
