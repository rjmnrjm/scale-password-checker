import base64

with open("scale.png", "rb") as f:   # change if your file is .gif
    encoded = base64.b64encode(f.read())

# Save the output into a text file so you can copy easily
with open("icon_base64.txt", "w") as out:
    out.write(encoded.decode("utf-8"))

print("✅ Conversion complete! Base64 string saved in icon_base64.txt")
