class DHProtocol:

    def __init__(self):
        self.p = None
        self.g = None

    def dh_calculate(self, p, g):
        self.p = p
        self.g = g

        print("The value of P:", self.p)
        print("The value of G:", self.g)

        # It is the chosen Alise private key
        a = 4
        print("The private key a for Alice:", a)

        # Gets the generated key
        x = pow(g, a, p)

        # It is the chosen Bob private key
        b = 3
        print("The private key b for Bob:", b)

        # Gets the generated key
        y = pow(g, b, p)

        # Generating the secret key after the exchange of keys
        ka = pow(y, a, p)  # Secret key for Alice
        kb = pow(x, b, p)  # Secret key for Bob

        print("Secret key for Alice is:", ka)
        print("Secret key for Bob is:", kb)
