import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import csv
from checker import check_password

# 🚨 Issue: Users may accidentally enter real credentials
# ✅ Fix: Clear warning banner at top of GUI
DISCLAIMER = "⚠️ Do NOT enter real account passwords. Use only test examples."


def mask_password(pwd: str) -> str:
    """
    Mask password for display/export.
    Shows only first/last 2 chars. Prevents full exposure in logs/exports.
    """
    if len(pwd) <= 4:
        return "*" * len(pwd)
    return pwd[:2] + "*" * (len(pwd) - 4) + pwd[-2:]


def check_single_password():
    pwd = password_entry.get()
    result = check_password(pwd)

    # 🚨 Issue: Password shown in clear text in results
    # ✅ Fix: Mask password in popup display
    masked = mask_password(result["password"])
    feedback = f"Password: {masked}\nScore: {result['score']}/100\nStrength: {result['strength']}\n"
    if result['suggestions']:
        feedback += "Suggestions:\n - " + "\n - ".join(result['suggestions'])
    messagebox.showinfo("Password Check Result", feedback)


def check_batch_passwords():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filepath:
        return

    results = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            pwd = line.strip()
            if pwd:
                results.append(check_password(pwd))

    # Display results in scrollable window
    top = tk.Toplevel(root)
    top.title("Batch Password Results")
    text_area = scrolledtext.ScrolledText(top, wrap=tk.WORD, width=80, height=25)
    text_area.pack(padx=10, pady=10)

    for r in results:
        text_area.insert(tk.END, f"Password: {mask_password(r['password'])}\n")
        text_area.insert(tk.END, f"Score: {r['score']}/100\n")
        text_area.insert(tk.END, f"Strength: {r['strength']}\n")
        if r['suggestions']:
            text_area.insert(tk.END, "Suggestions:\n - " + "\n - ".join(r['suggestions']) + "\n")
        text_area.insert(tk.END, "-"*50 + "\n")

    # 🚨 Issue: Exported reports contain raw passwords
    # ✅ Fix: Mask passwords in CSV export too
    def export_csv():
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if save_path:
            with open(save_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Password (masked)", "Score", "Strength", "Suggestions"])
                for r in results:
                    writer.writerow([mask_password(r['password']), r['score'], r['strength'], "; ".join(r['suggestions'])])
            messagebox.showinfo("Export Complete", f"Results saved to {save_path}")

    export_btn = tk.Button(top, text="Export to CSV (masked)", command=export_csv)
    export_btn.pack(pady=5)


# GUI Setup
root = tk.Tk()
root.title("Scale - Password Strength Checker")

tk.Label(root, text=DISCLAIMER, fg="red", wraplength=400).pack(pady=5)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Enter password to check:").grid(row=0, column=0, padx=5, pady=5)
password_entry = tk.Entry(frame, show="*", width=40)
password_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Check Password", command=check_single_password).grid(row=1, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Batch Test from File", command=check_batch_passwords).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Quit", command=root.quit).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

