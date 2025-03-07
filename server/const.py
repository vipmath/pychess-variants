from settings import static_url

SCHEDULE_MAX_DAYS = 7
TOURNAMENT_SPOTLIGHTS_MAX = 4

# Max number of lobby chat lines (deque limit)
MAX_CHAT_LINES = 100

# Minimum number of rated games needed
HIGHSCORE_MIN_GAMES = 10

# Show the number of spectators only after this limit
MAX_NAMED_SPECTATORS = 20

# tournament status
T_CREATED, T_STARTED, T_ABORTED, T_FINISHED, T_ARCHIVED = range(5)

# tournament frequency
HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY, MARATHON, SHIELD = "h", "d", "w", "m", "y", "a", "s"

# tournament pairing
ARENA, RR, SWISS = range(3)

# translations
LANGUAGES = [
    "de",
    "en",
    "es",
    "gl_ES",
    "fr",
    "hu",
    "it",
    "ja",
    "ko",
    "nl",
    "pl",
    "pt",
    "ru",
    "th",
    "tr",
    "zh_CN",
    "zh_TW",
]

# fishnet work types
MOVE, ANALYSIS = 0, 1

# game types
CASUAL, RATED, IMPORTED = 0, 1, 2

# game status
(
    CREATED,
    STARTED,
    ABORTED,
    MATE,
    RESIGN,
    STALEMATE,
    TIMEOUT,
    DRAW,
    FLAG,
    ABANDONE,
    CHEAT,
    BYEGAME,
    INVALIDMOVE,
    UNKNOWNFINISH,
    VARIANTEND,
    CLAIM,
) = range(-2, 14)

LOSERS = {
    "abandone": ABANDONE,
    "abort": ABORTED,
    "resign": RESIGN,
    "flag": FLAG,
}

GRANDS = ("xiangqi", "manchu", "grand", "grandhouse", "shako", "janggi", "promojanggi", "janggimodern", "racingjanggi", "allracingjanggi", "hpjanggi", "nzjanggi", "nnjanggi", "chessjanggi", "chessjanggihouse", "centerjanggi", "nudejanggi", "nudejanggihouse", "pocketjanggi", "pocketjanggil", "pocketjanggip", "pocketjanggihouse", "pocketjanggilhouse", "check3janggi", "check3janggihouse", "atomicjanggi", "atomicjanggihouse", "changgi", "racingkingsjanggi", "coffeejanggi", "coffeejanggihouse", "janggihouse", "janggilhouse")

CONSERVATIVE_CAPA_FEN = "arnbqkbnrc/pppppppppp/10/10/10/10/PPPPPPPPPP/ARNBQKBNRC w KQkq - 0 1"

VARIANTS = (
    "chess",
    "antichess",    
    "chess960",
    "kingofthehill",
    "racingkings",
    "crazyhouse",
    "crazyhouse960",
    "placement",
    "atomic",
    "atomic960",
    "makruk",
    "makpong",
    "cambodian",
    "sittuyin",
    "asean",
    "shogi",
    "minishogi",
    "kyotoshogi",
    "dobutsu",
    # Gorogoro is superseded by Gorogoro Plus
    # "gorogoro",
    "gorogoroplus",
    "torishogi",
    "xiangqi",
    "manchu",
    "janggi",
    "komajanggi",   
    "komajanggihouse",     
    "promojanggi",    
    "janggimodern",    
    "racingjanggi",   
    "allracingjanggi",      
    "hpjanggi",
    "nzjanggi",
    "nnjanggi",    
    "chessjanggi",  
    "chessjanggihouse",      
    "centerjanggi",       
    "nudejanggi",    
    "nudejanggihouse", 
    "pocketjanggi", 
    "pocketjanggil", 
    "pocketjanggip",     
    "pocketjanggihouse",   
    "pocketjanggilhouse",      
    "check3janggi",  
    "check3janggihouse",      
    "atomicjanggi",  
    "atomicjanggihouse",     
    "minijanggi", 
    "minijanggihouse",     
    "changgi",
    "racingkingsjanggi",    
    "coffeejanggi", 
    "coffeejanggihouse",     
    "janggihouse",   
    "janggilhouse",       
    "minixiangqi",
    "capablanca",
    "capablanca960",
    "capahouse",
    "capahouse960",
    # We support to import/store/analyze these variants
    # but don't support to add them to leaderboard page
    # "gothic",
    # "gothhouse",
    # "embassy",
    "seirawan",
    "seirawan960",
    "shouse",
    "grand",
    "grandhouse",
    "shogun",
    "shako",
    "hoppelpoppel",
    "orda",
    "synochess",
    "shinobi",
    "empire",
    "ordamirror",
    "pandemonium",   
    "parahouse",     
    "chak",
    "chennis",
)

VARIANT_ICONS = {
    "makruk": "Q",
    "makpong": "O",
    "sittuyin": ":",
    "shogi": "K",
    "janggi": "=",
    "promojanggi": "=",    
    "janggimodern": "=",    
    "racingjanggi": "=",    
    "allracingjanggi": "=",       
    "hpjanggi": "=",
    "nzjanggi": "=",
    "nnjanggi": "=",    
    "centerjanggi": "=",    
    "chessjanggi": "=",  
    "chessjanggihouse": "=",        
    "nudejanggi": "=",    
    "nudejanggihouse": "=",
    "pocketjanggi": "=",   
    "pocketjanggil": "=",  
    "pocketjanggip": "=",     
    "pocketjanggihouse": "=",    
    "pocketjanggilhouse": "=",        
    "check3janggi": "=",  
    "check3janggihouse": "=",      
    "atomicjanggi": "=", 
    "atomicjanggihouse": "=",     
    "minijanggi": "7",  
    "minijanggihouse": "7",    
    "komajanggi": "7",      
    "komajanggihouse": "7",         
    "changgi": "=",
    "racingkingsjanggi": "=",    
    "coffeejanggi": "=", 
    "coffeejanggihouse": "=",      
    "janggihouse": "=", 
    "janggilhouse": "=",    
    "xiangqi": "|",
    "chess": "M",
    "antichess": "M",
    "kingofthehill": "M",
    "racingkings": "M",
    "crazyhouse": "+",
    "placement": "S",
    "capablanca": "P",
    "capahouse": "&",
    "seirawan": "L",
    "seirawan960": "}",
    "shouse": "$",
    "grand": "(",
    "grandhouse": "*",
    "gothic": "P",
    "gothhouse": "&",
    "embassy": "P",
    "minishogi": "6",
    "dobutsu": "8",
    "gorogoro": "🐱",
    "gorogoroplus": "🐱",
    "torishogi": "🐦",
    "cambodian": "!",
    "shako": "9",
    "minixiangqi": "7",
    "chess960": "V",
    "capablanca960": ",",
    "capahouse960": "'",
    "crazyhouse960": "%",
    "kyotoshogi": ")",
    "shogun": "-",
    "orda": "R",
    "synochess": "_",
    "hoppelpoppel": "`",
    "manchu": "{",
    "atomic": "~",
    "atomic960": "\\",
    "shinobi": "🐢",
    "empire": "♚",
    "ordamirror": "◩",
    "pandemonium": "F",    
    "parahouse": "F",        
    "asean": "♻",
    "chak": "🐬",
    "chennis": "🎾",
}

VARIANT_960_TO_PGN = {
    "chess": "Chess960",
    #"antichess": "Antichess960",    
    "capablanca": "Caparandom",
    "capahouse": "Capahouse960",
    "crazyhouse": "Crazyhouse",  # to let lichess import work
    "atomic": "Atomic",  # to let lichess import work
    "seirawan": "Seirawan960",
    # some early game is accidentally saved as 960 in mongodb
    "shogi": "Shogi",
    "sittuyin": "Sittuyin",
    "makruk": "Makruk",
    "placement": "Placement",
    "grand": "Grand",
}

CATEGORIES = {
    "chess": (
        "chess",
        "chess960",
        "crazyhouse",
        "crazyhouse960",
        "placement",
        "atomic",
        "atomic960",
    ),
    "fairy": (
        "capablanca",
        "capablanca960",
        "capahouse",
        "capahouse960",
        "seirawan",
        "seirawan960",
        "shouse",
        "grand",
        "grandhouse",
        "shako",
        "shogun",
        "hoppelpoppel",
    ),
    "army": ("orda", "synochess", "shinobi", "empire", "ordamirror", "chak", "chennis"),
    "makruk": ("makruk", "makpong", "cambodian", "sittuyin", "asean"),
    "shogi": (
        "shogi",
        "minishogi",
        "kyotoshogi",
        "dobutsu",
        "gorogoroplus",
        "torishogi",
    ),
    "xiangqi": ("xiangqi", "manchu", "janggi", "minixiangqi"),
}

VARIANT_GROUPS = {}
for categ in CATEGORIES:
    for variant in CATEGORIES[categ]:
        VARIANT_GROUPS[variant] = categ

TROPHIES = {
    "top1": (static_url("images/trophy/Big-Gold-Cup.png"), "Champion!"),
    "top10": (static_url("images/trophy/Big-Silver-Cup.png"), "Top 10!"),
    "top50": (static_url("images/trophy/Fancy-Gold-Cup.png"), "Top 50!"),
    "top100": (static_url("images/trophy/Gold-Cup.png"), "Top 100!"),
    "shield": (static_url("images/trophy/shield-gold.png"), "Shield"),
    # some example custom trophy from lichess
    "acwc19": (static_url("images/trophy/acwc19.png"), "World Champion 2019"),
    "3wc21": (static_url("images/trophy/3wc21.png"), "World Champion 2021"),
}


def variant_display_name(variant):
    if variant == "seirawan":
        return "S-CHESS"
    elif variant == "seirawan960":
        return "S-CHESS960"
    elif variant == "shouse":
        return "S-HOUSE"
    elif variant == "cambodian":
        return "OUK CHAKTRANG"
    elif variant == "ordamirror":
        return "ORDA MIRROR"
    elif variant == "gorogoroplus":
        return "GOROGORO+"
    elif variant == "kyotoshogi":
        return "KYOTO SHOGI"
    elif variant == "torishogi":
        return "TORI SHOGI"
    else:
        return variant.upper()


#  Deferred translations!


def _(message):
    return message


TRANSLATED_PAIRING_SYSTEM_NAMES = {
    0: _("Arena"),
    1: _("Round-Robin"),
    2: _("Swiss"),
}

TRANSLATED_FREQUENCY_NAMES = {
    "h": _("Hourly"),
    "d": _("Daily"),
    "w": _("Weekly"),
    "m": _("Monthly"),
    "y": _("Yearly"),
    "a": _("Marathon"),
    "s": _("Shield"),
    "S": _("SEAturday"),
}

TRANSLATED_VARIANT_NAMES = {
    "chess": _("Chess"),
    "antichess": _("Antichess"),  
    #"antichess960": _("Antichess960"),  
    "kingofthehill": _("Kingofthehill"), 
    "racingkings": _("Racingkings"),  
    "chess960": _("Chess960"),
    "crazyhouse": _("Crazyhouse"),
    "crazyhouse960": _("Crazyhouse960"),
    "placement": _("Placement"),
    "atomic": _("Atomic"),
    "atomic960": _("Atomic960"),
    "makruk": _("Makruk"),
    "makpong": _("Makpong"),
    "cambodian": _("Ouk Chaktrang"),
    "sittuyin": _("Sittuyin"),
    "asean": _("ASEAN"),
    "shogi": _("Shogi"),
    "minishogi": _("Minishogi"),
    "kyotoshogi": _("Kyoto Shogi"),
    "dobutsu": _("Dobutsu"),
    # Gorogoro is superseded by Gorogoro Plus
    # "gorogoro",
    "gorogoroplus": _("Gorogoro+"),
    "torishogi": _("Tori Shogi"),
    "xiangqi": _("Xiangqi"),
    "manchu": _("Manchu"),
    "hpjanggi": _("Hpjanggi"),
    "nzjanggi": _("Nzjanggi"),
    "nnjanggi": _("Nnjanggi"),
    "janggi": _("Janggi"), 
    "promojanggi": _("Promojanggi"),     
    "janggimodern": _("Janggimodern"),    
    "racingjanggi": _("Racingjanggi"),    
    "allracingjanggi": _("Allracingjanggi"),      
    "chessjanggi": _("Chessjanggi"),  
    "chessjanggihouse": _("Chessjanggihouse"),      
    "centerjanggi": _("Centerjanggi"),    
    "nudejanggi": _("Nudejanggi"),   
    "nudejanggihouse": _("Nudejanggihouse"),   
    "pocketjanggi": _("Pocketjanggi"),
    "pocketjanggil": _("Pocketjanggil"),    
    "pocketjanggip": _("Pocketjanggip"),      
    "pocketjanggihouse": _("Pocketjanggihouse"), 
    "pocketjanggilhouse": _("Pocketjanggilhouse"),     
    "check3janggi": _("Check3janggi"),  
    "check3janggihouse": _("Check3janggihouse"),      
    "atomicjanggi": _("Atomicjanggi"),
    "atomicjanggihouse": _("Atomicjanggihouse"),    
    "changgi": _("Changgi"),
    "racingkingsjanggi": _("Racingkingsjanggi"),    
    "coffeejanggi": _("Coffeejanggi"),   
    "coffeejanggihouse": _("Coffeejanggihouse"),      
    "janggihouse": _("Janggihouse"), 
    "janggilhouse": _("Janggilhouse"),     
    "minijanggi": _("Minijanggi"), 
    "minijanggihouse": _("Minijanggihouse"),  
    "komajanggi": _("Komajanggi"),   
    "komajanggihouse": _("Komajanggihouse"),       
    "minixiangqi": _("Minixiangqi"),
    "capablanca": _("Capablanca"),
    "capablanca960": _("Capablanca960"),
    "capahouse": _("Capahouse"),
    "capahouse960": _("Capahouse960"),
    # We support to import/store/analyze these variants
    # but don't support to add them to leaderboard page
    # "gothic",
    # "gothhouse",
    # "embassy",
    "seirawan": _("S-Chess"),
    "seirawan960": _("S-Chess960"),
    "shouse": _("S-House"),
    "grand": _("Grand"),
    "grandhouse": _("Grandhouse"),
    "shogun": _("Shogun"),
    "shako": _("Shako"),
    "hoppelpoppel": _("Hoppel-Poppel"),
    "orda": _("Orda Chess"),
    "synochess": _("Synochess"),
    "shinobi": _("Shinobi"),
    "empire": _("Empire"),
    "ordamirror": _("Orda Mirror"),
    "pandemonium": _("Pandemonium"),  
    "parahouse": _("Parahouse"),    
    "chak": _("Chak"),
    "chennis": _("Chennis"),
}

del _
