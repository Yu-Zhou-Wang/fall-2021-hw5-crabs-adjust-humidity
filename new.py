import cProfile

def f (a):
  for i in range(a):
    print("fuck you")

tmp = 10
cProfile.run('f(tmp)')
