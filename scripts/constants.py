import sys

CLIENT_VERSION = '0.0.1'
PACKAGE_VERSION = '0.0.1rc4'
PACKAGE_NAME = 'claircontroller'


# If called directly, return the constant value given
# its name. Useful in bash scripts.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python constant.py CONSTANT_NAME")
        sys.exit(1)

    if sys.argv[1] in globals():
        print(globals()[sys.argv[1]])
    else:
        print("Cannot find constant %s" % sys.argv[1])
        sys.exit(1)

