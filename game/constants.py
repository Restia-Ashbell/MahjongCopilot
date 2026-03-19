from common.mj_helper import MjaiType, MSType

class Positions:
    """ Screen coordinates constants. in 16 x 9 resolution"""
    TEHAI_X = [
        2.23125,    3.021875,   3.8125,     4.603125,   5.39375,    6.184375,   6.975,
        7.765625,   8.55625,    9.346875,   10.1375,    10.928125,  11.71875,   12.509375]
    TEHAI_Y = 8.3625
    TRUMO_SPACE = 0.246875
    BUTTONS:list[tuple] = [
        (10.875, 7),        # 0 (None)
        (8.6375, 7),        # 1
        (6.4   , 7),        # 2
        (10.875, 5.9),      # 3
        (8.6375, 5.9),      # 4
        (6.4   , 5.9),      # 5
        (10.875, 4.8),      # Not used
        (8.6375, 4.8),      # Not used
        (6.4   , 4.8),      # Not used
    ]
    """ button layout:
    5   4   3
    2   1   0
    where action with higher priority takes lower position
    None is always at 0
    """

    CANDIDATES:list[tuple] = [
        (3.6625,  6.3),         # 
        (4.49625, 6.3),
        (5.33 ,   6.3),
        (6.16375, 6.3),
        (6.9975,  6.3),
        (7.83125, 6.3),         # 5 mid
        (8.665,   6.3),
        (9.49875, 6.3),
        (10.3325, 6.3),
        (11.16625,6.3),
        (12,      6.3),
    ]
    """ chi/pon/daiminkan candidates (combinations) positions
    index = (-(len/2)+idx+0.5)*2+5 """
    
    CANDIDATES_KAN:list[tuple] = [
        (4.325,   6.3),         #
        (5.4915,  6.3),
        (6.6583,  6.3),
        (7.825,   6.3),         # 3 mid
        (8.9917,  6.3),
        (10.1583, 6.3),
        (11.325,  6.3),
    ]
    """ kakan/ankan candidates (combinations) positions
    idx_kan = int((-(len/2)+idx+0.5)*2+3)"""
    
    EMOJI_BUTTON = (15.675, 4.9625)
    EMOJIS = [
        (12.4, 3.5), (13.65, 3.5), (14.8, 3.5),    # 1 2 3
        (12.4, 5.0), (13.65, 5.0), (14.8, 5.0),    # 4 5 6
        (12.4, 6.5), (13.65, 6.5), (14.8, 6.5),    # 7 8 9
    ]
    """ emoji positions
    0 1 2
    3 4 5
    6 7 8"""
    
    
    GAMEOVER = [
        (14.35, 8.12),    # OK button 确定按钮
        (6.825, 6.8),     # 点击好感度礼物?
    ]
    MENUS = [
        (11.5, 2.75),   # Ranked 段位场
    ]
    
    LEVELS = [
        (11.5, 3.375),  # Bronze 铜之间
        (11.5, 4.825),  # Silver 银之间
        (11.5, 6.15),   # Gold 金之间
        (11.5, 5.425),  # Jade 玉之间    滚轮    
        (11.5, 6.825),  # Throne 王座之间  滚轮
    ]
    
    MODES = [
        (11.6, 3.325), # 4E 四人东
        (11.6, 4.675), # 4S 四人南
        (11.6, 6.1),   # 3E 三人东
        (11.6, 7.35),  # 3S 三人南
    ]


MJAI_2_MS_TYPE = {
    MjaiType.NONE: MSType.none,
    
    MjaiType.CHI: MSType.chi,
    MjaiType.PON: MSType.pon,
    MjaiType.DAIMINKAN: MSType.daiminkan,
    MjaiType.HORA: MSType.hora,        # MJAI hora might also be mapped to zimo

    MjaiType.ANKAN: MSType.ankan,
    MjaiType.KAKAN: MSType.kakan,
    MjaiType.REACH: MSType.reach,
    MjaiType.RYUKYOKU: MSType.ryukyoku,
    MjaiType.NUKIDORA: MSType.nukidora,
}
""" Map mjai type to Majsoul operation type """

ACTION_PIORITY = [
    0,  # none      #
    99, # Discard   # There is no discard button. Make it off the chart and positioned last in the operation list
    4,  # Chi       # Opponent Discard
    3,  # Pon       # Opponent Discard
    3,  # Ankan     # Self Discard      # If Ankan and Kakan are both available, use only kakan.
    2,  # Daiminkan # Opponent Discard
    3,  # Kakan     # Self Discard
    2,  # Reach     # Self Discard
    1,  # Zimo      # Self Discard
    1,  # Rong      # Opponent Discard
    5,  # Ryukyoku  # Self Discard
    4,  # Nukidora  # Self Discard
]
""" Priority of the actions when allocated to buttons in Majsoul
None is always the lowest, at bottom-right corner"""

def cvt_type_mjai_2_ms(mjai_type, tsumohai:str) -> MSType:
    """ Convert mjai type str to MSType enum"""
    if tsumohai and mjai_type == MjaiType.HORA:
        return MSType.zimo
    else:
        return MJAI_2_MS_TYPE.get(mjai_type)
