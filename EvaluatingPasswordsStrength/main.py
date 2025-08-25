# main.py
from getpass import getpass
from checker import score_password

def main():
    pw = getpass("Enter password to test: ")
    score, suggestions = score_password(pw)
    print(f"\nScore: {score}/100")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(" -", s)
    else:
        print("Looks strong!")

if __name__ == "__main__":
    main()
