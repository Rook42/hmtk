class CurrencyConverter(object):
    """Houserule currency converter"""
    #Nothing was easy in medieval times, not even money.
    #Why simplify for the sake of your players? It's immersive.

    #Coinage system:
    #Coin      Material     Value                     Weight Abb

    #Sovereign Gold,        20s   or 1L      or 2880n 1/32lb L
    #Angel     Gold,        6s 8d or 1/3L    or  960n 1/96lb a
    #Shilling  Silver,      12d   or 1/20L   or  144n 1/32lb s
    #Groat     Base Silver, 4d    or 1/60L   or   48n 1/32lb g
    #Penny     Base Silver, 1d    or 1/240L  or   12n 1/96lb d
    #Farthing  Copper,      1/4d  or 1/960L  or    3n 1/32lb q
    #Mite      Various,     1/12d or 1/2880L or    1n 1/96lb n

    #Abbreviations were extended to cover real coins used in medieval
    #England for ease of use. New abbreviations attempt to follow the
    #original Carolingian naming scheme;
    #L is for libra,
    #s for solidus,
    #d for denarius.
    #New:
    #a for aureus (gold), a Roman gold coin.
    #g for gros (large), many medieval coins had this name.
    #q for quadrans (quarter), a Roman copper coin of little value.
    #n for nummus (coin), a tiny Roman bronze coin of very little value.

    #Units of Account:
    #Unit             Abb  Value
    #Pound Sterling   L1    20s
    #Shilling         1s    12d
    #Penny            1d    12n
    #Mite             1n     1n

    #Classically, d would be the smallest unit of measure, and any smaller
    #divisions would be rendered fractionally. However, since
    #mites are closest to tc, and it's more trouble than it's worth to
    #support fractional text displays, we're settling for n as mite's
    #abbreviation in account units to fill the gap.

    #Conversion Rates:
    #1pp = 10000n = L3  9s  5d  4n = 3L 1a 2s 2g 1d 1q 1n
    #1gp = 1000n  =     6s 11d  4n =    1a       3d 1q 1n
    #1sp = 100n   =         8d  4n =          2g    1q 1n
    #1cp = 10n    =            10n =                3q 1n
    #1tc = 1n     =             1n =                   1n


