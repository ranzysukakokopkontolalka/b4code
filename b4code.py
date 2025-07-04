import base64

# String Base64 yang ingin didekode
encoded_string = "MPA5NPI5PLY2ER=="

# Dekode string
decoded_bytes = base64.b64decode(encoded_string)

# Konversi byte ke integer
black = int(decoded_bytes)

print(black)
