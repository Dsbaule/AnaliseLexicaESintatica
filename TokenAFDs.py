from AFD import AFD
import CharClasses

def ifAFD():
    ifAFD = AFD()
    ifAFD.addState('', False, True)
    ifAFD.addState('i')
    ifAFD.addState('if', True)
    ifAFD.setTransition('', 'i', 'i')
    ifAFD.setTransition('i', 'f', 'if')
    return ifAFD

def idAFD():
    idAFD = AFD()
    idAFD.addState('', False, True)
    idAFD.addState('char', True)
    idAFD.setTransitions('', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.digits(), 'char')

def whileAFD():
    whileAFD = AFD()
    whileAFD.addState('', False, True)
    whileAFD.addState('w')
    whileAFD.addState('wh')
    whileAFD.addState('whi')
    whileAFD.addState('whil')
    whileAFD.addState('while', True)
    whileAFD.setTransition('', 'w', 'w')
    whileAFD.setTransition('w', 'h', 'wh')
    whileAFD.setTransition('wh', 'i', 'whi')
    whileAFD.setTransition('whi', 'l', 'whil')
    whileAFD.setTransition('whil', 'e', 'while')
    return whileAFD
