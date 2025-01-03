from __future__ import annotations

import inspect
import os.path
import re
from collections.abc import Callable
from functools import partial
from typing import Any

import flame


def app_initialized(project_name: str) -> None:
    package_dir = os.path.dirname(os.path.dirname(__file__))
    output_dir = os.path.join(package_dir, 'stubs')
    generate_stub(flame, output_dir)


def sort_key(obj: Any, attr: str) -> tuple:
    try:
        value = getattr(obj, attr)
    except AttributeError:
        return ()

    if isinstance(value, type):
        return 1, attr
    elif callable(value):
        return 2, attr
    return 0, attr


def generate_stub(module, output_dir: str) -> None:
    output_path = os.path.join(output_dir, f'{module.__name__}.pyi')

    with open(output_path, 'w') as f:
        f.write('from typing import Any, overload\n\n\n')

        attrs = dir(module)
        attrs.sort(key=partial(sort_key, module))
        for attr in attrs:
            f.write(decode_attribute(module, attr))


def decode_attribute(obj: Any, name: str, decode_types: bool = True) -> str:
    try:
        value = getattr(obj, name)
    except AttributeError:
        return ''

    if isinstance(value, type):
        if decode_types:
            return decode_class(value)
    elif callable(value):
        return decode_function(obj, value)

    if name.startswith('_'):
        return ''

    if value is None:
        value = 'None'
    elif type(value) in (str, int, float, bool):
        value = repr(value)
    else:
        value = '...'

    output = ''
    if inspect.isclass(obj):
        output += '    '
    output += f'{name} = {value}\n'
    return output


def decode_class(cls: type) -> str:
    output = '\n'

    name = cls.__name__
    base_names = (
        c.__name__ for c in cls.__bases__ if c.__name__ not in ('instance', 'object')
    )
    bases = ','.join(base_names)
    output += f'class {name}'
    if bases:
        output += f'({bases})'
    output += ':\n'

    if doc := cls.__doc__:
        if doc_string := str(doc).strip():
            output += f'    """\n'
            output += f'    {doc_string}\n'
            output += f'    """\n'

    properties = ''

    attrs = dir(cls)
    attrs.sort(key=partial(sort_key, cls))
    for attr in attrs:
        properties += decode_attribute(cls, attr, decode_types=False)

    if properties:
        output += properties
    else:
        output += f'    ...\n'

    output += '\n'

    return output


def decode_function(obj: Any, func: Callable) -> str:
    output = ''

    if not (doc := func.__doc__):
        return output

    # Signatures
    signatures = []
    matches = re.findall(r'\w+\(.*\)\s*->\s*\w+\s*:?$', doc.strip(), re.MULTILINE)
    for signature in matches:
        doc = doc.replace(signature, '')

        def sub_arg(m: re.Match) -> str:
            argument = m.group(2)
            hint = m.group(1).replace('object', 'Any')
            return f'{argument}: {hint}'

        signature = re.sub(r'\((\w+)\)(\w+)', sub_arg, signature)
        signature = re.sub(r'->\s*object', '-> Any', signature)
        signature = re.sub(r'\d+:\d+:\d+:\d+', '...', signature)
        signature = signature.replace('[]', 'None')
        signature = signature.replace('[', '').replace(']', '')
        signature = signature.strip(': \t\n\r')

        # HACK: There are signatures where non-default parameters follow default.
        if match := re.search(r'\((.*)\)\s*->', signature):
            args = match.group(1).split(',')
            fixed_args = []
            default = False
            for arg in args:
                if '=' in arg:
                    default = True
                elif default:
                    arg += ' = None'
                fixed_args.append(arg.strip())

            args_string = ', '.join(fixed_args)
            signature = signature.replace(match.group(1), args_string)

        signatures.append(f'def {signature}:\n')

    # Write
    doc_string = doc.strip()

    for i, signature in enumerate(signatures):
        output += '\n'
        if i > 0:
            output += '@overload\n'
        output += signature
        if i == 0 and doc_string:
            output += f'    """\n'
            output += f'    {doc_string}\n'
            output += f'    """\n'
        output += '    ...\n'

    # Indent
    if inspect.isclass(obj):
        lines = output.split('\n')
        output = '\n'.join(f'    {line}' if line else '' for line in lines)

    return output
