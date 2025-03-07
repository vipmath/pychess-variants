from itertools import product

"""
We use the simplest compression method for moves here: 2 byte sqare to 1 byte ascii.
For better result consider compressing moves using indexes in valid move lists.
For more sophisticated encoding consider using lichess method described at:
https://lichess.org/blog/Wqa7GiAAAOIpBLoY/developer-update-275-improved-game-compression
"""

# Create mappings to compress variant, result and uci/usi move lists a little
V2C = {
    "chess": "n",
    "antichess": "n0",    
    "kingofthehill": "n1", 
    "racingkings": "n2",
    "capablanca": "c",
    "capahouse": "i",
    "crazyhouse": "h",
    "atomic": "A",
    "makruk": "m",
    "placement": "p",
    "seirawan": "s",
    "shogi": "g",
    "minishogi": "a",
    "shouse": "z",
    "sittuyin": "y",
    "xiangqi": "x",
    "grand": "q",
    "grandhouse": "r",
    "gothic": "o",
    "gothhouse": "t",
    "embassy": "E",
    "cambodian": "b",
    "shako": "d",
    "minixiangqi": "e",
    "kyotoshogi": "k",
    "shogun": "u",
    "janggi": "j",
    "check3janggi": "J0", 
    "check3janggihouse": "J1",     
    "atomicjanggi": "j7",  
    "atomicjanggihouse": "j8",
    "nudejanggi": "j9",   
    "nudejanggihouse": "j10",
    "pocketjanggi": "j11", 
    "pocketjanggil": "j13",  
    "pocketjanggip": "j14",     
    "pocketjanggihouse": "j12",   
    "pocketjanggilhouse": "j15",      
    "minijanggi": "j0", 
    "minijanggihouse": "j5",    
    "changgi": "j3", 
    "centerjanggi": "j17",
    "racingjanggi": "j23", 
    "allracingjanggi": "j25",   
    "promojanggi": "j26", 
    "komajanggi": "j27",     
    "komajanggihouse": "j28",       
    "janggimodern": "j24",    
    "chessjanggi": "j21",  
    "chessjanggihouse": "j22",     
    "racingkingsjanggi": "j4",     
    "coffeejanggi": "j2",  
    "coffeejanggihouse": "j6",     
    "janggihouse": "j1",  
    "janggilhouse": "j16", 
    "hpjanggi": "j18",
    "nzjanggi": "j19",
    "nnjanggi": "j20",    
    "makpong": "l",
    "orda": "f",
    "synochess": "v",
    "hoppelpoppel": "w",
    "manchu": "M",
    "dobutsu": "D",
    "gorogoroplus": "G",
    "shinobi": "J",
    "empire": "P",
    "ordamirror": "O",
    "torishogi": "T",
    "pandemonium": "U", 
    "parahouse": "U1",    
    "asean": "S",
    "chak": "C",
    "chennis": "H",
}
C2V = {v: k for k, v in V2C.items()}

R2C = {"1-0": "a", "0-1": "b", "1/2-1/2": "c", "*": "d"}
C2R = {v: k for k, v in R2C.items()}

# Create square to int mapping
M2C = dict(zip([a + b for a, b in product("abcdefghij", "0123456789")], list(range(34, 256))))

# Add possible from parts of drop moves
PIECES = "PNBRQKFGSLACHE"
m2c_len = len(M2C) + 34
for piece in PIECES:
    M2C["%s@" % piece] = m2c_len
    m2c_len += 1

# Kyoto Shogi drop moves can start with extra "+"
for piece in "PLNS":
    M2C["+%s" % piece] = m2c_len
    m2c_len += 1

# More droppable pieces
#   The variant that uses these pieces (shinobi) was added after kyotoshogi
#   so these letters need to be here to be backward compatible
PIECES = "MDJ"
for piece in PIECES:
    M2C["%s@" % piece] = m2c_len
    m2c_len += 1

# pandemonium pieces
PIECES = "UV"
for piece in PIECES:
    M2C["%s@" % piece] = m2c_len
    m2c_len += 1

# Chennis drop moves can start with extra "+" as well (P and S are already added above for Kyoto Shogi)
for piece in "FM":
    M2C["+%s" % piece] = m2c_len
    m2c_len += 1

C2M = {v: k for k, v in M2C.items()}


def encode_moves(moves, variant):
    if variant in ("kyotoshogi", "chennis"):
        return [
            chr(M2C[move[0:2]]) + chr(M2C[move[3:5]]) + "@"
            if move[0] == "+"
            else chr(M2C[move[0:2]]) + chr(M2C[move[2:4]]) + (move[4] if len(move) == 5 else "")
            for move in moves
        ]
    return [
        chr(M2C[move[0:2]]) + chr(M2C[move[2:4]]) + (move[4] if len(move) == 5 else "")
        for move in moves
    ]


def decode_moves(moves, variant):
    if variant in ("kyotoshogi", "chennis"):
        return [
            C2M[ord(move[0])] + "@" + C2M[ord(move[1])]
            if move[-1] == "@"
            else C2M[ord(move[0])] + C2M[ord(move[1])] + (move[2] if len(move) == 3 else "")
            for move in moves
        ]
    return [
        C2M[ord(move[0])] + C2M[ord(move[1])] + (move[2] if len(move) == 3 else "")
        for move in moves
    ]
