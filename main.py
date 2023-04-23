import argparse
import gen

parser = argparse.ArgumentParser(
    prog="PyGen", description="Simplist Python password generator")

parser.add_argument("usec", help="Name of game platform, of mail, etc... (in one word)")
parser.add_argument("code", help="Code of the chosen string collections. Options: l: lc, u: uc, d: digits, p: punct")
parser.add_argument("length", help="Length of the desired pw", type=int)
parser.add_argument("-file_path", help="File dest")
args = parser.parse_args()

pw = gen.gen(args.code, args.length)

if args.file_path != None: # was specified
    with open(args.file_path, "a") as f:
        f.write(f"{args.usec}: {pw}\n")
else:
    print(pw)