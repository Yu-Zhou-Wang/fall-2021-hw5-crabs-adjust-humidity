import cProfile

def f ():
  a = 10
  for i in range(a):
    print("fuck you")

cProfile.run('f()')
