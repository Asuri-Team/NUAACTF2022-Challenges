import math
import sys

def check_cong(k, p, q, n, xored=None):
    kmask = (1 << k) - 1
    p &= kmask
    q &= kmask
    n &= kmask
    pqm = (p*q) & kmask
    return pqm == n and (xored is None or (p^q) == (xored & kmask))

def extend(k, a):
    kbit = 1 << (k-1)
    assert a < kbit
    yield a
    yield a | kbit

def factor(n, p_xor_q):
    tracked = set([(p, q) for p in [0, 1] for q in [0, 1]
                   if check_cong(1, p, q, n, p_xor_q)])

    PRIME_BITS = int(math.ceil(math.log(n, 2)/2))

    maxtracked = len(tracked)
    for k in range(2, PRIME_BITS+1):
        newset = set()
        for tp, tq in tracked:
            for newp_ in extend(k, tp):
                for newq_ in extend(k, tq):
                    newp, newq = sorted([newp_, newq_])
                    if check_cong(k, newp, newq, n, p_xor_q):
                        newset.add((newp, newq))

        tracked = newset
        if len(tracked) > maxtracked:
            maxtracked = len(tracked)
    print('Tracked set size: {} (max={})'.format(len(tracked), maxtracked))

    for p, q in tracked:
        if p != 1 and p*q == n:
            return p, q

n = 95562862201427823336067582946015664592322094165595564734633544688981046852555011419775655956374062008786746746891813021004709042123448569672651054374497117781385077761604798008040559786965945283482187568723860843102761550095675462113034490834106391146206127719571788775471987423072874061061356320902761206747
p_xor_q = 222698508797767721110391484298656215822060469539734106657369897669776822548641301202460186331633383845935831146767129439812408208215003896191936416553098
p, q = factor(n, p_xor_q)
print(p)
print(q)
