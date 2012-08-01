#!/usr/bin/env python 
# ============================================================================
import sys
import math
import operator
import collections

import primes

#  ===========================================================================
#  = http://projecteuler.net/problem=12                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the first triangular number with over 500 divisors. A triangular   =
#  = number is one generated by taking the sum of natural numbers            =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getPrimeFactors(num, primes_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  test_num = num
  prime_factors = []
  for p in primes_list:
    while test_num % p == 0:
      prime_factors.append(p)
      test_num /= p
    if test_num == 1: 
      break 
  return prime_factors

# ----------------------------------------------------------------------------
def getNumDivisorsFromPrimes(prime_factors):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num_primes = len(prime_factors)
  # print '%s - num_primes: %d' % ( prime_factors
  #                               , num_primes
  #                               )
  # print '\tnum_factors: %d' % (math.factorial(num_primes+1)/(2*math.factorial(num_primes-1)))
  num_divisors = 1
  prime_counter = collections.Counter(prime_factors)

  for elt,count in prime_counter.most_common():
    num_divisors *= (count+1)
  return num_divisors
  # return math.factorial(num_primes+1)/(2*math.factorial(num_primes-1))

# ----------------------------------------------------------------------------
def getDivisorsFromPrimes(prime_factors):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  divisors = []
  # for i in 
  # not finished!

  return divisors

# ----------------------------------------------------------------------------
def findTriangularNumberWithNDivisors(num_divisors):
  """
  Find the first triangular with at least num_divisors divisors
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  number_found = False
  triangular_num = 1
  next_num = 1
  list_of_primes = primes.primeSeive(1e6)
  while not number_found:
    next_num += 1
    triangular_num += next_num
  
    # print triangular_num
    prime_factors = getPrimeFactors(triangular_num, list_of_primes)
    num_factors = getNumDivisorsFromPrimes(prime_factors)
    divisors = getDivisorsFromPrimes(prime_factors)
    # divisors = getDivisors(triangular_num)
    if next_num%1000 == 0:
      print '%d - %d' % (triangular_num, num_factors)
    if num_factors >= num_divisors:
      print 'Found %d with %d divisors' % (triangular_num, num_factors)
      number_found = True

  print '---------------------------------------------------------------------'
  print 'The first triangular number with at least %d divisors is %d ' % ( num_divisors
                                                                         , triangular_num
                                                                         )

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findTriangularNumberWithNDivisors(5.)
  # 28
  print '====================================================================='
  findTriangularNumberWithNDivisors(10.)
  # 120
  # 120
  print '====================================================================='
  findTriangularNumberWithNDivisors(50.)
  # 25200
  # 25200
  print '====================================================================='
  findTriangularNumberWithNDivisors(100.)
  # 73920
  # 73920
  print '====================================================================='
  findTriangularNumberWithNDivisors(200.)
  # 2031120
  # 2031120
  print '====================================================================='
  findTriangularNumberWithNDivisors(500.)
  # 76576500

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 76576500