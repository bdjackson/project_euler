#!/usr/bin/env python 
# ============================================================================
import sys
import math

#  ===========================================================================
#  = http://projecteuler.net/problem=20                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of digits of 100!                                          =
#  ===========================================================================

# ----------------------------------------------------------------------------
def sumOfDigits(num):
  """
  Returns the sum of digits
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num_str = str(num)
  sum = 0
  for digit in num_str:
    sum += int(digit)
  return sum

# ----------------------------------------------------------------------------
def sumOfFactorialDigits(num):
  """
  Get the factorial of num and return the sum of those digits
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  fact = math.factorial(num)
  sum_of_digits = sumOfDigits(fact)
  print "%d! = %d -- sum of digits = %d" % (num, fact, sum_of_digits)
  return sum_of_digits

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sumOfFactorialDigits(100)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 648
