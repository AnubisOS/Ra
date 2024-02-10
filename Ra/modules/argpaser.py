from argparse import ArgumentParser, Action

class NegateAction(Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != 'un')
        setattr(ns, self.dest, option[2:4] != 'no')

parser = ArgumentParser()
parser.prog = "Ra"

#* General
parser.add_argument(
    "-V",
    "--version",
    help="Displays current version",
    action="version",
    version='Ra v0.1.0'
)

#* Brightness
bright = parser.add_argument_group('Brightness')
bright.add_argument(
    '-b',
    "--brightness",
    dest="bright",
    help="Sets a brightness value",
    metavar="Value",
    type=int
)
bright.add_argument(
    "-ib",
    "--inc-bright",
    dest="brightness_up",
    help="Increses Brightness by percentage",
    metavar="Percentage",
    type=int
)
bright.add_argument(
    "-db",
    "--dec-bright",
    dest="brightness_down",
    help="decreses Brightness by percentage",
    metavar="Percentage",
    type=int
)
bright.add_argument(
    "--night-mode",
    "--no-night-mode",
    dest="night_mode",
    help="Toggles night mode (Blue light filter)",
    action=NegateAction,
    nargs=0
)

#* Volume
volume = parser.add_argument_group('Volume')
volume.add_argument(
    '-v',
    "--volume",
    dest="volume",
    help="Sets a volume value",
    metavar="Value",
    type=int
)
volume.add_argument(
    "-iv",
    "--inc-volume",
    dest="volume_up",
    metavar="Percentage",
    help="Increses Volume by percentage",
    type=int
)
volume.add_argument(
    "-dv",
    "--dec-volume",
    dest="volume_down",
    metavar="Percentage",
    help="decreses Volume by percentage",
    type=int
)
volume.add_argument(
    "--deafen",
    "--undeafen",
    action=NegateAction,
    help="Toggle Deafen",
    dest="deafen",
    nargs=0
)
volume.add_argument(
    "--mute",
    "--unmute",
    action=NegateAction,
    help="Toggle Mic",
    dest="mute",
    nargs=0
)

#* Network
network = parser.add_argument_group('Network')
network.add_argument(
    "--ethernet",
    "--no-ethernet",
    action=NegateAction,
    help="Toggle Ethernet",
    dest="ether",
    nargs=0
)
network.add_argument(
    "--wifi",
    "--no-wifi",
    action=NegateAction,
    help="Toggle WiFi",
    dest="wifi",
    nargs=0
)
# TODO: NEED FIXES
network.add_argument(
    "--show-wlans",
    action="store_true",
    help="Show available networks",
    dest="wlans"
)
network.add_argument(
    "--show-connected",
    action="store_true",
    help="Show connected network",
    dest="connected"
)