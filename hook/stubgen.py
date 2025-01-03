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
    output_dir = os.path.join(package_dir, 'flame-stubs')
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
    output_path = os.path.join(output_dir, '__init__.pyi')

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

    hint = ''
    if value is None:
        value = 'None'
    elif type(value) in (str, int, float, bool):
        value = repr(value)
    else:
        type_name = value.__class__.__name__
        if type_name and type_name[0].isupper():
            hint = f': {type_name}'
        value = '...'

    output = ''
    if inspect.isclass(obj):
        output += '    '
    output += f'{name}{hint} = {value}\n'
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
    if not (doc := func.__doc__):
        return ''

    # Signatures
    signatures = []
    matches = re.findall(r'\w+\(.*\)\s*->\s*\w+\s*:?$', doc.strip(), re.MULTILINE)
    for signature in matches:
        doc = doc.replace(signature, '')
        signature = format_signature(signature)
        signatures.append(signature)

    # Write
    output = ''
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


def decode_value(value: str) -> Any:
    value = value.strip()
    if value.lower() == 'none':
        return

    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value.replace('"', '').replace("'", '')


def format_signature(signature: str) -> str:
    signature = signature.replace('[]', 'None')
    signature = signature.replace('[', '').replace(']', '')
    signature = signature.strip(': \t\n\r')
    signature = re.sub(r'(->.*)object', r'\1Any', signature)

    if match := re.search(r'\((.*)\)', signature):
        # NOTE: Assume that there are no commas in arg defaults
        args = match.group(1).split(',')

        formatted_args = []
        is_default = False
        for arg in args:
            formatted_arg = arg

            # Format type hints
            if m := re.search(r'\((\w+)\)(\w+)', formatted_arg):
                name = m.group(2)
                hint = m.group(1).replace('object', 'Any')
                formatted_arg = arg.replace(m.group(0), f'{name}: {hint}')

            # Format default values
            if m := re.search(r'=\s*(.*)', formatted_arg):
                is_default = True
                default = repr(decode_value(m.group(1)))
            elif is_default:
                # HACK: There are signatures where non-default parameters follow
                # default.
                default = repr(None)
            else:
                default = None

            if default is not None:
                formatted_arg = re.sub(r'(\s*=.*)?$', '', formatted_arg)
                formatted_arg += f' = {default}'

            formatted_args.append(formatted_arg.strip())

        signature = signature.replace(match.group(1), ', '.join(formatted_args))

    signature = f'def {signature}:\n'
    return signature
