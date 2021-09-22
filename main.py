from passlib.hash import bcrypt
passwd = b'password-goes-here'
hashed = bcrypt.using(rounds=10, ident="2y").hash(passwd)
print(hashed)
