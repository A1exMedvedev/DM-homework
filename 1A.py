import hashlib

s = 'DM Fall 2024 HW3'

hash_object = hashlib.sha256(s.encode('utf-8'))
hex_hash = hash_object.hexdigest()
binary_hash = bin(int(hex_hash, 16))[2:].zfill(256)
slices = []
for i in range(0, 256, 32):
    slices.append(binary_hash[i:i + 32])

d = 0
for slice in slices:
    d ^= int(slice, 2)

w = d ^ 0x7613a0ca

print("hash:", binary_hash)
print("d:", bin(d)[2:])
print("w:", hex(w))