export const variantsIni = `
[changgi]
variantTemplate = changgi
pieceToCharTable = .N.R.AB.P..C.........K.n.r.ab.p..c.........k
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
maxFile = 9
maxRank = 10
soldier = p
fers = a
horse = n
janggiElephant = b
janggiCannon = c
rook = r
king = k
promotionPieceTypes = -
doubleStep = false
castling = false
stalemateValue = loss
perpetualCheckIllegal = true
soldierPromotionRank = 1
flyingGeneral = false
bikjangRule = false
materialCounting = janggi
#diagonalLines = 
pass = true
moveRepetitionIllegal = true 
nFoldRule = 4
nMoveRule = 100

[racingjanggi:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
flagPiece = k
whiteFlag = *10
blackFlag = *1 
flagMove = true
checking = false

[allracingjanggi:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
king = -
commoner = k
extinctionValue = loss
extinctionPieceTypes = k
extinctionPseudoRoyal = true
flagPiece = k
promotionPieceTypes = -
promotedPieceType = a:k r:k b:k n:k p:k c:k
mandatoryPiecePromotion = true
promotionRank = 10
whiteFlag = *10
blackFlag = *1

[promojanggi:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
knight = s
bishop = t
cannon = u
queen = q
promotionPieceTypes = -
promotedPieceType = b:t n:s c:u p:q r:q
mandatoryPiecePromotion = true
promotionRank = 10

[chessjanggi:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
horse = -
janggiElephant = -
knight = n
bishop = b

[chessjanggihouse:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
horse = -
janggiElephant = -
knight = n
bishop = b
pieceDrops = true
capturesToHand = true
dropChecks = true

[centerjanggi:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
flagPiece = k
flagMove = false
whiteFlag = d6 e6 f6
blackFlag = d5 e5 f5

[hpjanggi:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
horse = -
janggiElephant = -
biskni = b
knibis = n

[nzjanggi:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
horse = -
rook = -
rookni = r
kniroo = n

[nnjanggi:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
horse = -
customPiece1 = n:NN

[pandemonium]
variantTemplate = shogi
pieceToCharTable = PNBRFSA.UV.++++++++.++Kpnbrfsa.uv.++++++++.++k
maxFile = 9
maxRank = 9
pocketSize = 9
startFen = rnbsksbnr/2+f1+u1+a2/p1p1p1p1p/4v4/9/4V4/P1P1P1P1P/2+F1+U1+A2/RNBSKSBNR[] w - - 0 1
customPiece1 = o:NA
customPiece2 = s:WF
customPiece3 = u:D
customPiece4 = w:DWF
castling = false
pieceDrops = true
capturesToHand = true
immobilityIllegal = true
soldier = p
knight = n
bishop = b
rook = r
king = k
queen = q
commoner = g
dragonHorse = h
bers = d
alfil = a
archbishop = c
chancellor = m
fers = f
wazir = v
centaur = t
promotionRank = 7
promotedPieceType = p:g n:o b:h r:d a:c v:m f:q s:w u:t
doubleStep = false
perpetualCheckIllegal = true
nMoveRule = 0
nFoldValue = loss
stalemateValue = loss
flagPiece = k
whiteFlag = *9
blackFlag = *1

[parahouse]
variantTemplate = shogi
pieceToCharTable = PNBR.Q.HD..++++.+.++Kpnbr.q.hd..++++.+.++k
maxFile = 9
maxRank = 9
pocketSize = 7
startFen = rnbdkhbnr/4q4/ppppppppp/9/9/9/PPPPPPPPP/4Q4/RNBHKDBNR[] w - - 0 1
customPiece1 = a:QN
customPiece2 = t:BNW
customPiece3 = s:RNF
castling = false
capturesToHand = true
pieceDrops = true
dropNoDoubled = p
immobilityIllegal = true
shogiPawn = p
knight = n
bishop = b
rook = r
queen = q
dragonHorse = h
bers = d
king = k
commoner = g
centaur = j
archbishop = c
chancellor = m
promotionRank = 7
promotedPieceType = p:g n:j b:c r:m q:a h:t d:s
doubleStep = false
perpetualCheckIllegal = true
nMoveRule = 0
nFoldValue = loss
stalemateValue = loss
flagPiece = k
whiteFlag = *9
blackFlag = *1

[atomicjanggi:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
king = -
commoner = k
blastOnCapture = true
extinctionValue = loss
extinctionPieceTypes = k
extinctionPseudoRoyal = true

[atomicjanggihouse:changgi]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 0 1
pieceDrops = true
capturesToHand = true
#dropChecks = false
king = -
commoner = k
blastOnCapture = true
extinctionValue = loss
extinctionPieceTypes = k
extinctionPseudoRoyal = true
whiteDropRegion = *1 *2 *3 *4 *5
blackDropRegion = *6 *7 *8 *9 *10

[racingkingsjanggi:changgi]
startFen = 9/9/9/9/9/9/9/9/krnb1BNRK/crnc1CNRC w - - 0 1
flagPiece = k
whiteFlag = *10
blackFlag = *10 
flagMove = true
checking = false

[minijanggi:minixiangqi]
startFen = rcnkncr/p1ppp1p/7/7/7/P1PPP1P/RCNKNCR w - - 0 1
maxRank = 7
maxFile = 7
cannon = -
janggiCannon = c
flyingGeneral = false
bikjangRule = false
materialCounting = janggi
pass = true
moveRepetitionIllegal = true 
nFoldRule = 4
nMoveRule = 100
diagonalLines = c1 e1 d2 c3 e3 c5 e5 d6 c7 e7

[komajanggi:minijanggi]
startFen = rn1nr/2k2/p1p1p/5/P1P1P/2K2/RN1NR w - - 0 1
maxRank = 7
maxFile = 5
janggiCannon = -
mobilityRegionWhiteKing = b1 c1 d1 b2 c2 d2 b3 c3 d3 
mobilityRegionBlackKing = b5 c5 d5 b6 c6 d6 b7 c7 d7
diagonalLines = b1 d1 c2 b3 d3 b5 d5 c6 b7 d7
#mobilityRegionBlackCustomPiece1 = *1 *2 *3 *4 *5

[komajanggihouse:komajanggi]
startFen = rn1nr/2k2/p1p1p/5/P1P1P/2K2/RN1NR w - - 0 1
pieceDrops = true
capturesToHand = true

[minijanggihouse:minijanggi]
startFen = rcnkncr/p1ppp1p/7/7/7/P1PPP1P/RCNKNCR[] w - - 0 1
pieceDrops = true
capturesToHand = true

# Hybrid variant of janggi and crazyhouse
[janggihouse:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 0 1
pieceDrops = true
capturesToHand = true

[janggilhouse:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 0 1
pieceDrops = true
capturesToHand = true
dropChecks = false

[check3janggi:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 3+3 0 1
checkCounting = true

[check3janggihouse:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 3+3 0 1
checkCounting = true
dropChecks = false
pieceDrops = true
capturesToHand = true

[coffeejanggi:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR w - - 0 1
mustCapture = true

[coffeejanggihouse:janggimodern]
startFen = rnba1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 0 1
mustCapture = true
pieceDrops = true
capturesToHand = true

[nudejanggi:janggimodern]
startFen = 9/4k4/9/9/9/9/9/9/4K4/9[RRNNBBCCAAPPPPPrrnnbbccaappppp] w - - 0 1
pieceDrops = true
capturesToHand = false
dropChecks = false

[nudejanggihouse:janggimodern]
startFen = 9/4k4/9/9/9/9/9/9/4K4/9[RRNNBBCCAAPPPPPrrnnbbccaappppp] w - - 0 1
pieceDrops = true
capturesToHand = true
dropChecks = false

[zombijanggi:janggimodern]
startFen = 3a1a3/4k4/ppp3ppp/pnpnpnpnp/ppppppppp/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 0 1
pieceDrops = true
capturesToHand = false
dropChecks = true

[zombijanggihouse:janggimodern]
startFen = 3a1a3/4k4/ppp3ppp/pnpnpnpnp/ppppppppp/9/P1P1P1P1P/1C5C1/4K4/RNBA1ABNR[] w - - 0 1
pieceDrops = true
capturesToHand = true
dropChecks = true

[pocketjanggi:janggimodern]
startFen = 3a1a3/4k4/9/p1p1p1p1p/9/9/P1P1P1P1P/9/4K4/3A1A3[RRNNBBCCrrnnbbcc] w - - 0 1
pieceDrops = true
capturesToHand = false
dropChecks = true

[pocketjanggil:janggimodern]
startFen = 3a1a3/4k4/9/p1p1p1p1p/9/9/P1P1P1P1P/9/4K4/3A1A3[RRNNBBCCrrnnbbcc] w - - 0 1
pieceDrops = true
capturesToHand = false
dropChecks = false

[pocketjanggip:janggimodern]
startFen = 3a1a3/4k4/9/2p1p1p2/9/9/2P1P1P2/9/4K4/3A1A3[RRNNBBCCPPrrnnbbccpp] w - - 0 1
pieceDrops = true
capturesToHand = false
dropChecks = false

[pocketjanggihouse:janggimodern]
startFen = 3a1a3/4k4/9/p1p1p1p1p/9/9/P1P1P1P1P/9/4K4/3A1A3[RRNNBBCCrrnnbbcc] w - - 0 1
pieceDrops = true
capturesToHand = true
dropChecks = true

[pocketjanggilhouse:janggimodern]
startFen = 3a1a3/4k4/9/p1p1p1p1p/9/9/P1P1P1P1P/9/4K4/3A1A3[RRNNBBCCrrnnbbcc] w - - 0 1
pieceDrops = true
capturesToHand = true
dropChecks = false

# Hybrid variant of Grand-chess and crazyhouse, using Grand-chess as a template
[grandhouse:grand]
startFen = r8r/1nbqkcabn1/pppppppppp/10/10/10/10/PPPPPPPPPP/1NBQKCABN1/R8R[] w - - 0 1
pieceDrops = true
capturesToHand = true

# Hybrid variant of Gothic-chess and crazyhouse, using Capablanca as a template
[gothhouse:capablanca]
startFen = rnbqckabnr/pppppppppp/10/10/10/10/PPPPPPPPPP/RNBQCKABNR[] w KQkq - 0 1
pieceDrops = true
capturesToHand = true

[gorogoroplus:gorogoro]
startFen = sgkgs/5/1ppp1/1PPP1/5/SGKGS[LNln] w 0 1
lance = l
shogiKnight = n
promotedPieceType = l:g n:g

[shogun:crazyhouse]
startFen = rnb+fkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNB+FKBNR[] w KQkq - 0 1
commoner = c
centaur = g
archbishop = a
chancellor = m
fers = f
promotionRank = 6
promotionLimit = g:1 a:1 m:1 q:1
promotionPieceTypes = -
promotedPieceType = p:c n:g b:a r:m f:q
mandatoryPawnPromotion = false
firstRankPawnDrops = true
promotionZonePawnDrops = true
whiteDropRegion = *1 *2 *3 *4 *5
blackDropRegion = *4 *5 *6 *7 *8
immobilityIllegal = true

[orda:chess]
centaur = h
knibis = a
kniroo = l
silver = y
promotionPieceTypes = qh
startFen = lhaykahl/8/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR w KQ - 0 1
flagPiece = k
whiteFlag = *8
blackFlag = *1

[synochess:pocketknight]
janggiCannon = c
soldier = s
horse = h
fersAlfil = e
commoner = a
startFen = rneakenr/8/1c4c1/1ss2ss1/8/8/PPPPPPPP/RNBQKBNR[ss] w KQ - 0 1
stalemateValue = loss
perpetualCheckIllegal = true
flyingGeneral = true
blackDropRegion = *5
flagPiece = k
whiteFlag = *8
blackFlag = *1

[shinobi:crazyhouse]
commoner = c
bers = d
archbishop = j
fers = m
shogiKnight = h
lance = l
promotionRank = 7
promotionPieceTypes = -
promotedPieceType = p:c m:b h:n l:r
mandatoryPiecePromotion = true
stalemateValue = loss
nFoldRule = 4
perpetualCheckIllegal = true
startFen = rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/LH1CK1HL[LHMMDJ] w kq - 0 1
capturesToHand = false
whiteDropRegion = *1 *2 *3 *4
immobilityIllegal = true
flagPiece = k
whiteFlag = *8
blackFlag = *1

[ordamirror:chess]
centaur = h
knibis = a
kniroo = l
customPiece1 = f:mQcN
promotionPieceTypes = lhaf
startFen = lhafkahl/8/pppppppp/8/8/PPPPPPPP/8/LHAFKAHL w - - 0 1
flagPiece = k
whiteFlag = *8
blackFlag = *1

[empire:chess]
customPiece1 = e:mQcN
customPiece2 = c:mQcB
customPiece3 = t:mQcR
customPiece4 = d:mQcK
soldier = s
promotionPieceTypes = q
startFen = rnbqkbnr/pppppppp/8/8/8/PPPSSPPP/8/TECDKCET w kq - 0 1
stalemateValue = loss
nFoldValue = loss
flagPiece = k
whiteFlag = *8
blackFlag = *1
flyingGeneral = true

[chak]
maxRank = 9
maxFile = 9
rook = r
knight = v
centaur = j
immobile = o
customPiece1 = s:FvW
customPiece2 = q:pQ
customPiece3 = d:mQ2cQ2
customPiece4 = p:fsmWfceF
customPiece5 = k:WF
customPiece6 = w:FvW
startFen = rvsqkjsvr/4o4/p1p1p1p1p/9/9/9/P1P1P1P1P/4O4/RVSJKQSVR w - - 0 1
mobilityRegionWhiteCustomPiece6 = *5 *6 *7 *8 *9
mobilityRegionWhiteCustomPiece3 = *5 *6 *7 *8 *9
mobilityRegionBlackCustomPiece6 = *1 *2 *3 *4 *5
mobilityRegionBlackCustomPiece3 = *1 *2 *3 *4 *5
promotionRank = 5
promotionPieceTypes = -
mandatoryPiecePromotion = true
promotedPieceType = p:w k:d
extinctionValue = loss
extinctionPieceTypes = kd
extinctionPseudoRoyal = true
flagPiece = d
whiteFlag = e8
blackFlag = e2
nMoveRule = 50
nFoldRule = 3
nFoldValue = draw
stalemateValue = loss

[chennis]
maxRank = 7
maxFile = 7
mobilityRegionWhiteKing = b1 c1 d1 e1 f1 b2 c2 d2 e2 f2 b3 c3 d3 e3 f3 b4 c4 d4 e4 f4
mobilityRegionBlackKing = b4 c4 d4 e4 f4 b5 c5 d5 e5 f5 b6 c6 d6 e6 f6 b7 c7 d7 e7 f7
customPiece1 = p:fmWfceF
cannon = c
commoner = m
fers = f
soldier = s
king = k
bishop = b
knight = n
rook = r
promotionPieceTypes = -
promotedPieceType = p:r f:c s:b m:n
promotionRank = 1
startFen = 1fkm3/1p1s3/7/7/7/3S1P1/3MKF1[] w - 0 1
pieceDrops = true
capturesToHand = true
pieceDemotion = true
mandatoryPiecePromotion = true
dropPromoted = true
castling = false
stalemateValue = loss`
