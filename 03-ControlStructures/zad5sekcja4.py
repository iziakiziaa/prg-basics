### Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # Sprawdzamy, czy znak jest literą (wielką lub małą)
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        # 1. Odczytaj kod znaku (użyj ord())
        char_code = ord(char)
        
        # 2. Dodaj jeden do kodu znaku
        new_char_code = char_code + 1
        
        # Obsługa "zawijania" z Z na A lub z z na a (przesunięcie o 1)
        # Jeśli pierwotny znak to 'Z', a nowy kod to [ (kod 'Z' + 1)
        if char == 'Z':
            new_char_code = ord('A')
        # Jeśli pierwotny znak to 'z', a nowy kod to { (kod 'z' + 1)
        elif char == 'z':
            new_char_code = ord('a')
        
        # 3. Zamień nowy kod znaku na odpowiadający mu znak (użyj chr())
        encrypted_char = chr(new_char_code)
    else:
        # Znak nie jest literą (np. spacja, cyfra, interpunkcja) - zostawiamy bez zmian
        encrypted_char = char
    
    # 4. Dodaj zaszyfrowany znak do zaszyfrowanego tekstu
    encrypted_text += encrypted_char

print("Tekst jawny:", plain_text)
print("Tekst zaszyfrowany:", encrypted_text)