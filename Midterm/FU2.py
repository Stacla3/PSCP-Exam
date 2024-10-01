"""Nickel"""
def mainf(tiger):
    """One"""
    return 2*tiger

def maing(lion):
    """Two"""
    return (3*(lion**4))-(lion**3)+(2*(lion**2))+10

def mainh(nick, nickel, plam):
    """Three"""
    return ((plam+nick)**2)-(nick*nickel)+(nickel**2)

def maini(pet, jury, yuri, dee):
    """Last"""
    return ((pet**2)+(jury**2)-(yuri**2))/((dee**2)-(2*pet*dee)+(2*pet))
_LILLY = float(input())
_TULIP = float(input())
_SHILY = float(input())
_POPPY = float(input())
print(mainf(mainf(_LILLY)))
print(maing(mainf(_LILLY-_TULIP)))
print(mainh((mainf(_LILLY+_TULIP)), mainf(_LILLY+_SHILY), maing(mainf(_POPPY**2))))
print(maini((mainh(((mainf(_LILLY+_TULIP))), (mainf(_LILLY-_SHILY)), (maing(mainf(_POPPY**2))))),
            maing(mainf(_LILLY-_TULIP)), mainf(mainf(mainf(mainf(mainf(_SHILY))))), _POPPY**8))
