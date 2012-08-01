#!/usr/bin/env python 
# ============================================================================
import sys
# import math

#  ===========================================================================
#  = http://projecteuler.net/problem=375                                     =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  =                                                                         =
#  ===========================================================================

# ----------------------------------------------------------------------------
def constructSequence(num_entries):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sequence = [290797]
  for i in xrange(num_entries):
    # pass
    sequence.append(((sequence[-1])**2)%50515093)
  return sequence

# ----------------------------------------------------------------------------
def findAij(sequence, i, j):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # print '----------------------------------'
  # print 'A(%d,%d): %d' % (i, j, min(sequence[i:j+1]))
  # print '\tsequence: %s' % sequence
  # print '\tsequence[i:j]: %s' % sequence[i:j+1]
  # if i == j:
  #   return 0
  return min(sequence[i:j+1])

# ----------------------------------------------------------------------------
def findSumOfMins(max_n):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sequence = constructSequence(max_n)
  sum_of_mins = 0
  for i in xrange(1, max_n+1):
    for j in xrange(i, max_n+1):
      # pass
      # print 'A(%d,%d): %d' % (i, j, findAij(sequence, i, j))
      sum_of_mins += findAij(sequence, i, j)
  print 'M(%d): %d' % (max_n, sum_of_mins)
  return sum_of_mins

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  print findSumOfMins(10) - 432256955
  # me:      432256955
  # correct: 432256955
  print '========================================'
  # print findSumOfMins(10000) - 3264567774119
  # me:      ---
  # correct: 3264567774119
  print '========================================'
  # findSumOfMins(2000000000)
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 