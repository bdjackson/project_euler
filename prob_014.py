#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=14                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Following the sequence:                                                 =
#  =   n -> n/2 (n is even)                                                  =
#  =   n -> 3n+1 (n is odd)                                                  =
#  = What starting number under 1e6 produces the longest chain               =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getNextValue(value):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  return int(value/2. if value%2 == 0 else 3*value+1)

# ----------------------------------------------------------------------------
def findChainLength(start, chain_length):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  if start == 1: 
    chain_length[1] = 1
    return 1

  if not start in chain_length:
    chain_length[start] = 0

  length = chain_length[start]
  if length == 0:
    next_value = getNextValue(start)
    length = findChainLength(next_value, chain_length) + 1
    chain_length[start] = length

  return length

# ----------------------------------------------------------------------------
def dumpChainLengths(chain_length, max_value):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  for i in xrange(1, max_value):
    print '%d - %d' % (i, chain_length[i])

# ----------------------------------------------------------------------------
def printLongestChain(chain_length, max_value):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  max_start = 0
  max_length = 0

  for key in chain_length:
    if key > max_value:
      continue
    if chain_length[key] > max_length:
      max_start = key
      max_length = chain_length[key]
  print 'Longest chain is generated by %d, and has a length of %d' % ( max_start
                                                                     , max_length
                                                                     )

# ----------------------------------------------------------------------------
def findLongestChain(max_value):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  max_value = int(max_value)
  # chain_length = [0]*(max_value*1000)
  # chain_length = [0]*(max_value**2)
  chain_length = {}
  for i in xrange(max_value+1): 
    chain_length[i] = 0
  for i in xrange(1, max_value+1):
    # print i
    findChainLength(i, chain_length)

  print '-----------------------------------------------------------'
  # dumpChainLengths(chain_length,max_value)
  printLongestChain(chain_length, max_value)

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # findLongestChain(1e5+1)
  findLongestChain(1e+6+1)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 