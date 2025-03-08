class Impl:

    yaml = False

    def parse(self, snippet: dict, context: dict):
        """
        snippet: dict - {
            'type': str - snippet type (e.g. "eno.js"/"eno.use")
            'args': List[arg] - snippet args
            'attrs': dict[str, arg] - snippet attrs
            'context': dict - context
            'text': str - snippet text (code body)
            'inline': bool - inline snippet or not
            'data': any - snippet text parsed yaml/json
        }
        context: dict - {
            'path': PurePosixPath - path of the eno
        }

        where

        arg: {
            'type': 'path'/'string'/'number' - type of the arg
            'value': any - value of the arg
            'quoted': str - as True if the arg is quoted string
        }
        """
        pass
