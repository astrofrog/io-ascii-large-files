from io import TextIOWrapper


class LineList:

    def __init__(self, fileobj):

        self.io_wrapper = TextIOWrapper(fileobj, line_buffering=True)
        self.lines = []

    def __getitem__(self, item):
        # For now just assume scalar item
        while item >= len(self.lines):
            self._read_block()
        return self.lines[item]

    def _read_block(self, blocksize=100000):
        self.lines += [x.strip() for x in self.io_wrapper.readlines(blocksize)]


with open('large_withnewlines', 'rb') as f:

    ll = LineList(f)

    print(ll[1000])
