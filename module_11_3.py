from pprint import pprint


def introspection_info(obj):
    intro = {
        'type': type(obj).__name__,
        'dir': dir(obj),
        'attributes': [item for item in dir(obj) if not callable(getattr(type(obj), item))],
        'methods': [item for item in dir(obj) if callable(getattr(type(obj), item))],
        'module': obj.__class__.__module__,

    }

    return intro


number_info = introspection_info(42)

pprint(number_info)
