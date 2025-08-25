# batch_test.py
from checker import score_password
from test_passwords import test_passwords

def run_batch():
    print("Batch Password Strength Test (Aligned with NIST/OWASP)\n" + "-"*50)

    for pw in test_passwords:
        score, suggestions = score_password(pw)
        print(f"\nPassword: {pw}")
        print(f"Score: {score}/100")
        print("Strength:",
              "Very Weak" if score < 25 else
              "Weak" if score < 50 else
              "Fair" if score < 70 else
              "Strong" if score < 85 else "Very Strong")

        if suggestions:
            print("Suggestions:")
            for s in suggestions:
                print(" -", s)

if __name__ == "__main__":
    run_batch()
