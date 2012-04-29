"""Python wrapper for dmenu

http://tools.suckless.org/dmenu/

"""
from subprocess import Popen, PIPE

def build_commandline(
    bottom=False,
    ignorecase=False,
    lines=None,
    monitor=None,
    prompt=None,
    font=None,
    normal_background=None,
    normal_foreground=None,
    selected_background=None,
    selected_foreground=None):
    """Build the dmenu command line

    See Documentation for func:`dmenu`
    """

    #I considered using a mapping {"bottom":"-b"} etc and passing **kwargs, but
    #that makes the function signature vague.

    args = ["dmenu"]
    if bottom:
        args.append("-b")
    if ignorecase:
        args.append("-i")
    if lines:
        args.extend(("-l", str(lines)))
    if monitor:
        args.extend(("-m", str(monitor)))
    if prompt:
        args.extend(("-p", prompt))
    if font:
        args.extend(("-fn", font))
    if normal_background:
        args.extend(("-nb", normal_background))
    if normal_foreground:
        args.extend(("-nf", normal_foreground))
    if selected_background:
        args.extend(("-sb", selected_background))
    if selected_foreground:
        args.extend(("-sf", selected_foreground))

    return args


def dmenu(items,
    bottom=False,
    ignorecase=False,
    lines=None,
    monitor=None,
    prompt=None,
    font=None,
    normal_background=None,
    normal_foreground=None,
    selected_background=None,
    selected_foreground=None):
    """
    Open a dmenu to select an item
    :param items: A list of strings to choose from.
    :param bottom: dmenu appears at the bottom of the screen.
    :param ignorecase: dmenu matches menu items case insensitively.
    :param lines: 
    :param monitor: dmenu appears on the given Xinerama screen.
    :param prompt: defines the prompt to be displayed to the left of the input field.
    :param font: defines the font or font set used.
    :param normal_background: defines  the  normal background color.
    :param normal_foreground: defines the normal foreground color.
    :param selected_background: defines the selected background color.
    :param selected_foreground: defines the selected foreground color.

    For colors #RGB, #RRGGBB, and color names are supported.
    """

    cli = build_commandline(bottom, ignorecase, lines, monitor,
                            prompt, font, normal_background, normal_foreground,
                            selected_background, selected_foreground)


    input_str = "\n".join(items) + "\n"

    proc = Popen(cli, stdout=PIPE, stdin=PIPE)
    return proc.communicate(input_str)[0]
