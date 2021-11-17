import cProfile

def f (a):
  for i in range(a):
    print("fuck you")

val tmp = 10
cProfile.run('f(tmp)')
