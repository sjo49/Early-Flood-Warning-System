from Task1A import run


def test_1A():
    if 'Number of stations: 2105' in run():
        return True
    else:
        raise ValueError('not printing correctly')

test_1A()