def greek_comparator(lhs, rhs):
    greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    
    if greek_alphabet.index(lhs) < greek_alphabet.index(rhs): 
        return -1
    elif greek_alphabet.index(lhs) == greek_alphabet.index(rhs):
        return 0
    else:
        return 1
    
print(greek_comparator('alpha', 'beta'))