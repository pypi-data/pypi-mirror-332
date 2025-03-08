import json
import types

from deepmerge import always_merger


def to_snippet(value):
    # TODO: support nested values
    # e.g. ['# heading', [('eno.plot', ...), ('eno.plot', ...), 'paragraph']]
    """
    dict - raw:

        return {'foo': 3, 'bar': 5}

    types.Generator - list of snippet:

        yield '# heading'
        yield 'eno.plot', ...

    list - list of snippet:

        return [
            '# heading',
            ('eno.plot', ...),
        ]
    """
    if isinstance(value, dict):
        # dict value is returned directly as json response
        # usage: get data from js page
        return value
    elif isinstance(value, (list, types.GeneratorType)):
        # already a "list" of values to be converted
        pass
    elif is_single_convertable_value(value):
        # construct a list of values to be converted
        value = [value]
    else:
        raise ValueError(f"unsupported return type {type(value)}")
    return [converted(d) for d in value]


def converted(ret: any):
    """
    Convert value into frontend renderable data.
    """
    # e.g. ('eno.table', {...})
    if isinstance(ret, tuple):
        if len(ret) == 2:
            lang, data = ret
        elif len(ret) > 2:
            lang = ret[0]
            data = ret[1:]
        else:
            raise ValueError(f"unsupported eno: {ret}, length {len(ret)}")
        convert = lang_to_convert.get(lang)
        if convert:
            _data = convert(data, lang = lang)
            if isinstance(_data, tuple):
                lang, data = _data
            else:
                data = _data
        elif lang.startswith('eno.'):
            pass
        else:
            try:
                lang, data = convert_elem(data, lang = lang)
            except Exception:
                raise ValueError(f"unsupported eno: {ret}")
        return {'lang': lang, 'data': data}
    # e.g. "# hello"
    elif isinstance(ret, str):
        if not ret: # yield '' for <br/>
            return {'lang': 'eno.wrap', 'data': {'type': 'br', 'props': {}}}
        return {'lang': 'eno.md', 'data': ret} # TODO: parse as eno
    elif is_pandas_dataframe(ret):
        return converted(('eno.table', ret))
    elif isinstance(ret, dict):
        return ret
    else:
        raise ValueError(f"unsupported py provided value of type {type(ret)}: {ret}")


def convert_eno_plot(data, **_):
    return always_merger.merge({
        'layout': {
            'title': {'font': {'size': 12, 'color': '#aaa'}, 'y': 0.98},
            'width': 600,
            'height': 300,
            'margin': {'l': 40, 'r': 40, 't': 20, 'b': 30},
        },
        'config': {
            'displayModeBar': False,
        },
    }, data)


def convert_eno_table(data, **_):
    if isinstance(data, list):
        return {'data': data}
    elif isinstance(data, tuple):
        if len(data) == 2:
            return {'data': data[0], 'cols': data[1]}
        elif len(data) == 3:
            return {'data': data[0], 'cols': data[1], 'props': data[2]}
        else:
            raise ValueError(f"unsupported eno.table {data}")
    elif is_pandas_dataframe(data):
        return {'data': json.loads(data.to_json(orient = 'records'))}
    else:
        return data


def convert_elem(data, lang):
    if isinstance(data, tuple):
        assert len(data) == 2, f"unsupported wrap {lang} {data}"
        props = data[0]
        if isinstance(props, str):
            props = {'className': props}
        elif isinstance(props, dict):
            pass
        else:
            raise ValueError(f"unsupported wrap {lang} {data}")
        children = data[1]
        if not isinstance(children, list):
            children = [children]
    elif isinstance(data, list):
        props = {}
        children = data
    else:
        raise ValueError(f"unsupported wrap {lang} {data}")
    return 'eno.wrap', {
        'type': lang,
        'props': props,
        'children': [converted(c) for c in children],
    }


def is_single_convertable_value(value):
    return str(value.__class__) in single_convertable_classnames


def is_pandas_dataframe(value):
    return str(value.__class__) == pandas_dataframe_classname


# NOTE: not using `isinstance` as import pandas takes a lot mem
pandas_dataframe_classname = "<class 'pandas.core.frame.DataFrame'>"
single_convertable_classnames = {
    "<class 'str'>",
    "<class 'tuple'>",
    pandas_dataframe_classname,
}

lang_to_convert = {
    'eno.plot': convert_eno_plot,
    'eno.table': convert_eno_table,
}
