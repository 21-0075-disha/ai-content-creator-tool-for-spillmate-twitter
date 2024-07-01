### Generate keys
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Alicia Sierra", "Monica Gaztambide","Bonnie Palermo"]
usernames = ["a-sierra", "monica","bonnie_palermo"]
passwords = ["a2h8.kJbH_u", "R#1102t","mxe4529G.Uyp"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
