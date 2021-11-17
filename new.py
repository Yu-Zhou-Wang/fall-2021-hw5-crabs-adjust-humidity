import cProfile

def f (a):
  for i in range(a):
    print("fuck you")

cProfile.run('f(a)')
