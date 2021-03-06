import pprint
import sys
import json

from st2actions.runners.pythonrunner import Action

__all__ = [
    'AssertObjectEquals'
]


def cmp(x, y):
    x = json.dumps(x, sort_keys=True)
    y = json.dumps(y, sort_keys=True)

    return (x == y)


class AssertObjectEquals(Action):
    def run(self, object, expected):
        ret = cmp(object, expected)

        if ret:
            sys.stdout.write('EQUAL.')
        else:
            pprint.pprint('Input: \n%s' % object, stream=sys.stderr)
            pprint.pprint('Expected: \n%s' % expected, stream=sys.stderr)
            raise ValueError('Objects not equal. Input: %s, Expected: %s.' % (object, expected))
