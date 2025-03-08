class EnoCmd:

    cmd = None

    def on_cmd(self, args, context):
        pass

    def on_token(self, token, context):
        pass

    def on_snippet(self, snippet, context):
        pass


class Beg(EnoCmd):

    cmd = 'beg'

    def on_cmd(self, args, context):
        cmd = args[0]
        args = args[1:]
        eno_cmds[cmd].on_cmd(args, context)


class End(EnoCmd):

    cmd = 'end'

    def on_cmd(self, args, context):
        # TODO: general cmd beg/end
        cmd = args[0]
        if cmd == 'math':
            context['math'] = False


class ImageWidth(EnoCmd):

    cmd = 'img-width'

    def on_cmd(self, args, context):
        context['default_image_width'] = int(args[0])

    def on_snippet(self, snippet, context):
        if snippet['type'] == 'eno.img':
            img = snippet
            unset = img.get('width') is None and img.get('height') is None
            if unset and context.get('default_image_width'):
                img['width'] = context['default_image_width']


class ImageHeight(EnoCmd):

    cmd = 'img-height'

    def on_cmd(self, args, context):
        context['default_image_height'] = int(args[0])

    def on_snippet(self, snippet, context):
        if snippet['type'] == 'eno.img':
            img = snippet
            unset = img.get('width') is None and img.get('height') is None
            if unset and context.get('default_image_height'):
                img['height'] = context['default_image_height']


class Math(EnoCmd):

    cmd = 'math'

    def on_cmd(self, args, context):
        if args and args[0] == 'end':
            context['math'] = False
        else:
            context['math'] = True

    def on_token(self, token, context):
        if not context.get('math'):
            return
        match token['type']:
            case 'codespan':
                text = token['text']
                if text.startswith('$') and text.endswith('$'):
                    token['type'] = 'inline-display-math'
                    token['text'] = f'$${text}$$'
                elif not text.startswith('eno.'):
                    token['type'] = 'inline-math'
                    token['text'] = f'${text}$'
            case 'code':
                token['type'] = 'block-math'
                text = token['text']
                if not text.startswith('\\begin{'):
                    lines = text.split('\n')
                    token['text'] = '\n'.join([
                        '\\begin{align*}',
                        *[line + ' \\\\' for line in lines],
                        '\\end{align*}',
                    ])


class Demo(EnoCmd):

    cmd = 'demo'

    def on_cmd(self, args, context):
        context['demo'] = True

    def on_token(self, token, context):
        if context.get('demo'):
            context['demo'] = False
            text = token['text']
            return 'div', 'horz space', [
                token,
            ]


eno_cmds = {d.cmd: d for d in [
    Beg(),
    End(),
    ImageWidth(),
    ImageHeight(),
    Math(),
    Demo(),
]}
