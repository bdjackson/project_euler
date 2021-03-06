#!/usr/bin/env python
# =============================================================================
import sys
import math
import operator

import primes_pp

# =============================================================================
# = http://projecteuler.net/problem=46                                        =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the smallest odd composite that cannot be written as the sum of a    =
# = prime and twice a square                                                  =
# =============================================================================

# -----------------------------------------------------------------------------
def findSpecialOdd(upper_limit = 1000):
    # Generate prime sieve and list of values that are twice a square
    prime_seive = primes_pp.primeSeive(int(2*upper_limit))
    list_of_2_square = [2*x*x for x in xrange(int(math.sqrt(upper_limit)+1))]

    # variables to keep track of whether we found the result
    found_special_odd = False
    special_odd = -1

    # Loop over values 2-upper limit
    for i in xrange(2, upper_limit):
        # trial will be the odd number generated by taking i*2+1
        trial = (2*i) + 1

        # trial will be flagged as "normal" if it can be written as a prime +
        # twice a square
        is_normal = False
        
        # Check list of 2*squares
        for twice_square in list_of_2_square:
            if twice_square > trial:
                break

            # if trial - twice_square = prime, we found our special odd!
            if prime_seive.isPrime(trial - twice_square):
                is_normal = True

        # Stop looking if we found the result
        if not is_normal:
            found_special_odd = True
            special_odd = trial
            break

    # Print result
    if found_special_odd:
        print "Found odd that cannot be written as the sum of prime and twice a square!"
        print '\t%d' % special_odd
    else:
        print "Did not find odd that cannot be written as the sum of prime and twice a square!"

    return special_odd

# =============================================================================
def main():
    findSpecialOdd(10000)

# =============================================================================
if __name__ == "__main__":
    sys.exit( main() )

# =============================================================================
# ============
# = solution =
# ============
# Found odd that cannot be written as the sum of prime and twice a square!
# 	5777
# 
# real	0m0.127s
# user	0m0.111s
# sys	0m0.014s
