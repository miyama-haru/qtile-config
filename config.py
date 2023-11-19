# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

# AUTOSTART PROGRAMS

@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.Popen([home])


mod = "mod4"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Rofi integration
    Key([mod], "p", lazy.spawn("rofi -show run")),

    # dmenu integration
    # Key(['mod4'], 'p', lazy.run_extension(extension.DmenuRun(
    #     dmenu_prompt="$",
    #     background=colors[0],
    #     foreground=colors[1],
    #     selected_background=colors[7],
    #     selected_foreground=colors[1],
    #     dmenu_bottom=False,
    #     font="Hack Nerd Font",
    #     font_size=14,
    #     dmenu_lines=25,
    # ))),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# COLORS

DoomOne = [
    ["#282c34", "#282c34"], # bg
    ["#bbc2cf", "#bbc2cf"], # fg
    ["#1c1f24", "#1c1f24"], # color01
    ["#ff6c6b", "#ff6c6b"], # color02
    ["#98be65", "#98be65"], # color03
    ["#da8548", "#da8548"], # color04
    ["#51afef", "#51afef"], # color05
    ["#c678dd", "#c678dd"], # color06
    ["#46d9ff", "#46d9ff"]  # color15
    ]

Dracula  = [
    ["#282a36", "#282a36"], # bg
    ["#f8f8f2", "#f8f8f2"], # fg
    ["#000000", "#000000"], # color01
    ["#ff5555", "#ff5555"], # color02
    ["#50fa7b", "#50fa7b"], # color03
    ["#f1fa8c", "#f1fa8c"], # color04
    ["#bd93f9", "#bd93f9"], # color05
    ["#ff79c6", "#ff79c6"], # color06
    ["#9aedfe", "#9aedfe"]  # color15
    ]

GruvboxDark  = [
    ["#282828", "#282828"], # bg
    ["#ebdbb2", "#ebdbb2"], # fg
    ["#000000", "#000000"], # color01
    ["#fb4934", "#fb4934"], # color02
    ["#98971a", "#98971a"], # color03
    ["#d79921", "#d79921"], # color04
    ["#83a598", "#83a598"], # color05
    ["#d3869b", "#d3869b"], # color06
    ["#b8bb26", "#b8bb26"], # color11
    ]
MonokaiPro = [
    ["#2D2A2E", "#2D2A2E"], # bg
    ["#FCFCFA", "#FCFCFA"], # fg
    ["#403E41", "#403E41"], # color01
    ["#FF6188", "#FF6188"], # color02
    ["#A9DC76", "#A9DC76"], # color03
    ["#FFD866", "#FFD866"], # color04
    ["#FC9867", "#FC9867"], # color05
    ["#AB9DF2", "#AB9DF2"], # color06
    ["#78DCE8", "#78DCE8"]  # color07
    ]

Nord = [
    ["#2E3440", "#2E3440"], # bg
    ["#D8DEE9", "#D8DEE9"], # fg
    ["#3B4252", "#3B4252"], # color01
    ["#BF616A", "#BF616A"], # color02
    ["#A3BE8C", "#A3BE8C"], # color03
    ["#EBCB8B", "#EBCB8B"], # color04
    ["#81A1C1", "#81A1C1"], # color05
    ["#B48EAD", "#B48EAD"], # color06
    ["#88C0D0", "#88C0D0"]  # color07
    ]

OceanicNext = [
    ["#1b2b34", "#1b2b34"], # bg
    ["#d8dee9", "#d8dee9"], # fg
    ["#29414f", "#29414f"], # color01
    ["#ec5f67", "#ec5f67"], # color02
    ["#99c794", "#99c794"], # color03
    ["#fac863", "#fac863"], # color04
    ["#6699cc", "#6699cc"], # color05
    ["#c594c5", "#c594c5"], # color06
    ["#5fb3b3", "#5fb3b3"]  # color07
    ]

Palenight = [
    ["#292d3e", "#292d3e"], # bg
    ["#d0d0d0", "#d0d0d0"], # fg
    ["#434758", "#434758"], # color01
    ["#f07178", "#f07178"], # color02
    ["#c3e88d", "#c3e88d"], # color03
    ["#ffcb6b", "#ffcb6b"], # color04
    ["#82aaff", "#82aaff"], # color05
    ["#c792ea", "#c792ea"], # color06
    ["#89ddff", "#89ddff"]  # color15
    ]

SolarizedDark = [
    ["#002b36", "#002b36"], # bg
    ["#839496", "#839496"], # fg
    ["#073642", "#073642"], # color01
    ["#dc322f", "#dc322f"], # color02
    ["#859900", "#859900"], # color03
    ["#b58900", "#b58900"], # color04
    ["#268bd2", "#268bd2"], # color05
    ["#d33682", "#d33682"], # color06
    ["#2aa198", "#2aa198"]  # color15
    ]

SolarizedLight = [
    ["#fdf6e3", "#fdf6e3"], # bg
    ["#657b83", "#657b83"], # fg
    ["#ece5ac", "#ece5ac"], # color01
    ["#dc322f", "#dc322f"], # color02
    ["#859900", "#859900"], # color03
    ["#b58900", "#b58900"], # color04
    ["#268bd2", "#268bd2"], # color05
    ["#d33682", "#d33682"], # color06
    ["#2aa198", "#2aa198"]  # color15
    ]

TomorrowNight = [
    ["#1d1f21", "#1d1f21"], # bg
    ["#c5c8c6", "#c5c8c6"], # fg
    ["#373b41", "#373b41"], # color01
    ["#cc6666", "#cc6666"], # color02
    ["#b5bd68", "#b5bd68"], # color03
    ["#e6c547", "#e6c547"], # color04
    ["#81a2be", "#81a2be"], # color05
    ["#b294bb", "#b294bb"], # color06
    ["#70c0ba", "#70c0ba"]  # color15
    ]

colors = DoomOne

### LAYOUTS ###

layouts = [
    layout.Columns(
        cont = "Hack Nerd Font",
        fontsize = 11,
        border_width = 3,
        border_normal = colors[2],
        border_focus = colors[3],
        bg_color = colors[0],
        active_bg = colors[8],
        active_fg = colors[2],
        inactive_bg = colors[1],
        inactive_fg = colors[0],
        margin=7,
        padding_left = 8,
        padding_x = 8,
        padding_y = 6,
        sections = ["ONE", "TWO", "THREE"],
        section_fontsize = 10,
        section_fg = colors[7],
        section_top = 15,
        section_bottom = 15,
        level_shift = 8,
        vspace = 3,
        panel_width = 240
    ),
    layout.Max(),
]

# Some settings that I use on almost every widget, which saves us
# from having to type these out for each individual widget.
widget_defaults = dict(
    font="Hack Nerd Font Bold",
    fontsize = 12,
    padding = 1,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename = "~/.config/qtile/icons/kitty.png",
                    scale = "False",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)},
                    ),
                widget.Prompt(
                    font = "Hack Nerd Font",
                    fontsize = 14,
                    foreground = colors[1]
                    ),
                widget.GroupBox(
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 4,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[8],
                    inactive = colors[1],
                    rounded = False,
                    highlight_color = colors[2],
                    highlight_method = "line",
                    this_current_screen_border = colors[7],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[7],
                    other_screen_border = colors[4],
                    ),
                widget.TextBox(
                    fmt = '|',
                    font = "Hack Nerd Font",
                    foreground = colors[1],
                    padding = 2,
                    fontsize = 14
                    ),
                widget.WindowName(
                        foreground = colors[6],
                        max_chars = 40
                        ),
                widget.GenPollText(
                        update_interval = 300,
                        func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                        foreground = colors[3],
                        fmt = '❤  {}',
                        ),
                widget.Spacer(length = 8),
                widget.CPU(
                        format = '▓  Cpu: {load_percent}%',
                        foreground = colors[4],
                        ),
                widget.Spacer(length = 8),
                widget.Memory(
                        foreground = colors[8],
                        format = '{MemUsed: .0f}{mm}{MemTotal: .0f}{mm}',
                        fmt = '🖥  Mem: {} used',
                        ),
                widget.Spacer(length = 8),
                widget.DF(
                        update_interval = 60,
                        foreground = colors[5],
                        partition = '/',
                        #format = '[{p}] {uf}{m} ({r:.0f}%)',
                        format = '{uf}{m} free',
                        fmt = '🖴  Disk: {}',
                        visible_on_warn = False,
                        ),
                widget.Spacer(length = 8),
                widget.Volume(
                        foreground = colors[7],
                        fmt = '🕫  Vol: {}',
                        ),
                widget.Spacer(length = 8),
                widget.KeyboardLayout(
                        foreground = colors[4],
                        fmt = '⌨  Kbd: {}',
                        ),
                widget.Spacer(length = 8),
                widget.Clock(
                        foreground = colors[8],
                        format = "⏱  %a, %b %d - %H:%M",
                        ),
                widget.Spacer(length = 8),
                widget.Systray(padding = 3),
                widget.Spacer(length = 8),
            ],
            30,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename = "~/.config/qtile/icons/kitty.png",
                    scale = "False",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)},
                    ),
                widget.Prompt(
                    font = "Hack Nerd Font",
                    fontsize = 14,
                    foreground = colors[1]
                    ),
                widget.GroupBox(
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 4,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[8],
                    inactive = colors[1],
                    rounded = False,
                    highlight_color = colors[2],
                    highlight_method = "line",
                    this_current_screen_border = colors[7],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[7],
                    other_screen_border = colors[4],
                    ),
                widget.TextBox(
                    fmt = '|',
                    font = "Hack Nerd Font",
                    foreground = colors[1],
                    padding = 2,
                    fontsize = 14
                    ),
                widget.WindowName(
                        foreground = colors[6],
                        max_chars = 40
                        ),
                widget.GenPollText(
                        update_interval = 300,
                        func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                        foreground = colors[3],
                        fmt = '❤  {}',
                        ),
                widget.Spacer(length = 8),
                widget.CPU(
                        format = '▓  Cpu: {load_percent}%',
                        foreground = colors[4],
                        ),
                widget.Spacer(length = 8),
                widget.Memory(
                        foreground = colors[8],
                        format = '{MemUsed: .0f}{mm}{MemTotal: .0f}{mm}',
                        fmt = '🖥  Mem: {} used',
                        ),
                widget.Spacer(length = 8),
                widget.DF(
                        update_interval = 60,
                        foreground = colors[5],
                        partition = '/',
                        #format = '[{p}] {uf}{m} ({r:.0f}%)',
                        format = '{uf}{m} free',
                        fmt = '🖴  Disk: {}',
                        visible_on_warn = False,
                        ),
                widget.Spacer(length = 8),
                widget.Volume(
                        foreground = colors[7],
                        fmt = '🕫  Vol: {}',
                        ),
                widget.Spacer(length = 8),
                widget.KeyboardLayout(
                        foreground = colors[4],
                        fmt = '⌨  Kbd: {}',
                        ),
                widget.Spacer(length = 8),
                widget.Clock(
                        foreground = colors[8],
                        format = "⏱  %a, %b %d - %H:%M",
                        ),
                widget.Spacer(length = 8),
            ],
            30,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
