import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.hid import HIDModes

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (board.A1, board.A2, board.A3, board.A4, board.A5, board.D5, board.D6, board.A0)
keyboard.row_pins = (board.D9, board.D10, board.D11, board.D2, board.D13, board.D12)
keyboard.diode_orientation = DiodeOrientation.ROW2COL
keyboard.debug_enabled = False

keyboard.coord_mapping = [
       0,    1,    2,    3,   4,   5,   6,       8,   9,  10,  11,  12,  13,  14,
     256,  257,  258,  259, 260, 261, 262,     264, 265, 266, 267, 268, 269, 270,
     512,  513,  514,  515, 516, 517, 518,     520, 521, 522, 523, 524, 525, 526,
     768,  769,  770,  771, 772, 773,               777, 778, 779, 780, 781, 782,
    1024, 1025, 1026, 1027,                                  1035,1036,1037,1038,
                         1287, 1031,            15,1295,
                            7,  775,           271,1039,
                          263,  519,           527, 783,
]

keyboard.keymap = [
    [
        KC.ESC,         KC.N1,      KC.N2,                  KC.N3,              KC.N4,      KC.N5,      KC.N6,                              KC.N7,      KC.N8,      KC.N9,   KC.N0,      KC.MINUS,   KC.EQUAL,   KC.BSPC,
        KC.TAB,         KC.Q,       KC.W,                   KC.E,               KC.R,       KC.T,       KC.BSLASH,                          KC.QUOTE,   KC.Y,       KC.U,    KC.I,       KC.O,       KC.P,       KC.RALT,
        KC.LCTRL,       KC.A,       KC.S,                   KC.D,               KC.F,       KC.G,       KC.NO,                              KC.MINUS,   KC.H,       KC.J,    KC.K,       KC.L,       KC.RGUI,    KC.RCTRL,
        KC.LSHIFT,      KC.Z,       KC.X,                   KC.C,               KC.V,       KC.B,                                                       KC.N,       KC.M,    KC.COMMA,   KC.DOT,     KC.SLASH,   KC.RSHIFT,
        KC.AUDIO_MUTE,  KC.LGUI,    KC.AUDIO_VOL_DOWN,      KC.AUDIO_VOL_UP,                                                                                                 KC.LEFT,    KC.UP,      KC.DOWN,    KC.RIGHT,
                                                                                            KC.MO(1), KC.B,                                 KC.H, KC.MO(1),
                                                                                            KC.SPACE, KC.D,                                 KC.I, KC.SPACE,
                                                                                            KC.ENTER, KC.F,                                 KC.K, KC.ENTER,
    ],
    [
        KC.TRNS,        KC.TRNS,    KC.TRNS,                KC.TRNS,            KC.TRNS,    KC.TRNS,    KC.TRNS,                            KC.TRNS,    KC.TRNS,    KC.TRNS, KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS, 
        KC.TRNS,        KC.HOME,    KC.UP,                  KC.END,             KC.PGUP,    KC.TRNS,    KC.TRNS,                            KC.TRNS,    KC.TRNS,    KC.TRNS, KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,        KC.LEFT,    KC.DOWN,                KC.RIGHT,           KC.PGDOWN,  KC.TRNS,    KC.TRNS,                            KC.TRNS,    KC.TRNS,    KC.TRNS, KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS, 
        KC.TRNS,        KC.TRNS,    KC.TRNS,                KC.TRNS,            KC.TRNS,    KC.TRNS,                                                    KC.TRNS,    KC.TRNS, KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS, 
        KC.TRNS,        KC.TRNS,    KC.TRNS,                KC.TRNS,                                                                                                         KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS, 
                                                                                            KC.TRNS,    KC.TRNS,                            KC.TRNS,    KC.TRNS,
                                                                                            KC.TRNS,    KC.TRNS,                            KC.TRNS,    KC.TRNS,
                                                                                            KC.TRNS,    KC.TRNS,                            KC.TRNS,    KC.TRNS,
    ]
]

split = Split(
    split_flip=False,
    split_side=SplitSide.LEFT,
    split_type=SplitType.BLE,
    split_target_left=True,
    debug_enabled=False,
)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()