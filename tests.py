'''tests.py'''
from sys import argv

def p_eq():
  print('='*64)

def default():
  p_eq()
  print('''main test-bed. other tests should be moved off to other test functions,
  after they are satisfactory.''')

  p_eq()
  print('example test: print function works(probably)')
  p_eq()

def parse_args(args): # placeholder
  if args[1:]==[]: args=[ [], 'default' ]
  for i in args[1:]:
    if i=='default':
      default()

def main(args=None):
  if args==None:
    print('''Welcome to tests.py. This is a self-test of the test script,
  written in Python, which in order to be more suitable to rapid tests,
  is typically less efficient than c programming language.''')
  
  parse_args(args)
  
if __name__ == '__main__':
    main(argv)
