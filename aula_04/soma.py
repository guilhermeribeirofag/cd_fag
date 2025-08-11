import argparse

p = argparse.ArgumentParser()
p.add_argument("--a", type=int, required=True)
p.add_argument("--b", type=int, required=True)
args = p.parse_args()

print(args.a + args.b)