import string

alphas = string.ascii_letters + '_'
nums = string.digits
inp = input('Identifier to test? ')
if len(inp) == 1:
    if inp[0] not in alphas:
        print('invalid: first symbol must bealphabetic')
    else:
        print("okay as an identifier")
elif len(inp) > 1:
    if inp[0] not in alphas:
        print('invalid: first symbol must bealphabetic')
    else:
        for otherChar in inp[1:]:
            if otherChar not in alphas + nums:
                print('invalid: remaining symbols must be alphanumeric')
                break
        print("okay as an identifier")
