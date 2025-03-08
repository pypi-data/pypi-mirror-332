class Base:

    def process(self, eno, meta):
        eno['template'] = meta['template']

    def iter_blocks(self, eno):
        cur = eno['tokens'][0]

        # descend into blocks
        parent = cur
        while True:
            if cur.get('block_start'):
                cur = parent
                break
            elif 'tokens' in cur:
                parent = cur
                cur = cur['tokens'][0]

        for token in cur['tokens']:
            yield token


base_impl = Base()
