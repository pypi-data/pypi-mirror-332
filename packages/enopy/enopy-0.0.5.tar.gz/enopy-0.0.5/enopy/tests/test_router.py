from pathlib import PurePosixPath

from fans.testutil import Meta

from enopy.router import follow_alias, find_eno_target


class Test_follow_alias:

    def test_no_follow(self):
        assert follow_alias(
            PurePosixPath('books'),
            {
                PurePosixPath('foo'): PurePosixPath('bar'),
            },
        ) == PurePosixPath('books')

    def test_single_follow(self):
        assert follow_alias(
            PurePosixPath('books'),
            {
                PurePosixPath('books'): PurePosixPath('apps/books'),
            },
        ) == PurePosixPath('apps/books')

    def test_multi_follow(self):
        assert follow_alias(
            PurePosixPath('a'),
            {
                PurePosixPath('a'): PurePosixPath('b'),
                PurePosixPath('b'): PurePosixPath('c'),
            },
        ) == PurePosixPath('c')


class Test_find_eno_target(metaclass = Meta):

    testcases = [
        # normal cases
        {
            'name': 'found file',
            'path': 'foo.eno',
            'enos': [
                'foo.eno',
            ],
            'expected': {'type': 'eno', 'path': 'foo.eno'},
        },
        {
            'name': 'found dir',
            'path': 'foo',
            'enos': [
                'foo/',
            ],
            'expected': {'type': 'dir', 'path': 'foo'},
        },
        {
            'name': 'auto adding suffix',
            'path': 'foo.bar',
            'enos': [
                'foo.bar.yaml',
            ],
            'expected': {'type': 'yaml', 'path': 'foo.bar.yaml'},
        },

        # corner cases
        {
            'name': 'given suffix first',
            'path': 'foo.yaml',
            'enos': [
                'foo.eno',
                'foo.yaml',
            ],
            'expected': {'type': 'yaml', 'path': 'foo.yaml'},
        },
        {
            'name': 'given suffix mismatch',
            'path': 'foo.yaml',
            'enos': [
                'foo.eno',
            ],
            'expected': None,
        },

        # real world
        {
            'name': 'get t.py when t.eno exists',
            'path': 't.py',
            'enos': [
                't.eno',
                't.py',
            ],
            'expected': {'type': 'py', 'path': 't.py'},
        },
    ]

    @staticmethod
    def make_testcase(testcase):
        def method(self):
            path = PurePosixPath(testcase['path'])
            expected = testcase['expected']

            eno_paths = {PurePosixPath(p) for p in testcase['enos']}
            path_to_type = {
                PurePosixPath(p): 'dir' if p.endswith('/') else 'file' for p in testcase['enos']
            }

            assert find_eno_target(
                path,
                suffixes = ['.eno', '.js', '.py', '.yaml'],
                is_path_exists = lambda path: path in eno_paths,
                is_file = lambda path: path_to_type[path] == 'file',
                is_dir = lambda path: path_to_type[path] == 'dir',
            ) == ({**expected, 'path': PurePosixPath(expected['path'])} if expected else None)
        return method
