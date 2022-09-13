from passlib.context import CryptContext

# fajl za kriptovanje password-a
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# huzima plain text password i hesira ga
class HashPassword:
    def create_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    # uporedjuje plain text i hesiran password, i vraca true ili false vrednost u zavisnosti od toga da li se poklapaju
    def verify_hash(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
