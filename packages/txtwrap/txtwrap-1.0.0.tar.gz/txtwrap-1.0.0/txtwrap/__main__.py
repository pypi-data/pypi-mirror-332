from argparse import ArgumentParser
from os import get_terminal_size
from txtwrap import wrap, shorten

parser = ArgumentParser(
    description='Command-line tool for wrapping, aligning, or shortening text.'
)

parser.add_argument(
    'text',
    type=str,
    help='Text to be wrapped, aligned, or shorted'
)

try:
    width = get_terminal_size()[0]
except:
    width = 70

parser.add_argument(
    '-w', '--width',
    type=int,
    default=width,
    metavar='<number>',
    help='Width of the text wrapping (default: current width terminal or 70)'
)

parser.add_argument(
    '-m', '--method',
    type=str,
    choices={'word', 'mono', 'shorten'},
    default='word',
    metavar='{word|mono|shorten}',
    help='Method to be applied to the text (default: word)'
)

parser.add_argument(
    '-a', '--alignment',
    type=str,
    choices={'left', 'center', 'right', 'fill'},
    default='left',
    metavar='{left|center|right|fill}',
    help='Alignment of the text (default: left)'
)

parser.add_argument(
    '-ne', '--neglect-empty',
    action='store_false',
    help='Neglect empty lines in the text'
)

parser.add_argument(
    '-s', '--start',
    type=int,
    default=0,
    metavar='<number>',
    help='start index of the text to be shorten (default: 0)'
)

parser.add_argument(
    '-ph', '--placeholder',
    type=str,
    default='...',
    metavar='<str>',
    help='Placeholder to be used when shortening the text (default: ...)'
)

args = parser.parse_args()

if args.method == 'shorten':
    print(shorten(args.text, args.width, args.start, placeholder=args.placeholder))
else:
    wrapped = wrap(args.text, args.width, method=args.method, preserve_empty=args.neglect_empty)

    if args.alignment == 'left':
        print('\n'.join(wrapped))
    elif args.alignment == 'center':
        print('\n'.join(line.center(args.width) for line in wrapped))
    elif args.alignment == 'right':
        print('\n'.join(line.rjust(args.width) for line in wrapped))
    elif args.alignment == 'fill':
        justified_lines = ''

        for line in wrapped:
            words = line.split()
            total_words = len(words)
            total_words_width = sum(len(w) for w in words)
            extra_space = args.width - total_words_width

            if total_words > 1:
                space_between_words = extra_space // (total_words - 1)
                extra_padding = extra_space % (total_words - 1)
            else:
                space_between_words = extra_space
                extra_padding = 0

            justified_line = ''
            for i, word in enumerate(words):
                justified_line += word
                if i < total_words - 1:
                    justified_line += ' ' * (space_between_words + (1 if i < extra_padding else 0))

            justified_lines += justified_line + '\n'

        print(justified_lines, end='')