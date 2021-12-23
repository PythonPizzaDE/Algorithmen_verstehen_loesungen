'''Achtung! Funktioniert nicht!'''
def to_ascii(char):
    return chr(int(char, 2))

# öffnet die datei mit dem cyber märchen
with open('1.txt') as file:
    text = file.read()

words = text.split(' ')

cyber_words = [w for w in words if 'Cyber' in w]

binary = ''.join(['1' if '-' in c else '0' for c in cyber_words])

binary = ''.join([c+' ' if i % 7 == 0 and i >= 7 else c for i, c in enumerate(binary)])

binary_chars = binary.split(' ')
password = ''.join([to_ascii(bc) for bc in binary_chars])
print(f'the password: {password}')
