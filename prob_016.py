#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=16                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of digits of 2^1000                                        =
#  ===========================================================================

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sum = 0
  for digit in str(2**1000):
    print digit
    sum += int(digit)
  print sum

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 