import unicodedata

def normalize_and_check(normalization_form, target_char):
    for codepoint in range(0x110000):
        char = chr(codepoint)
        normalized_char = unicodedata.normalize(normalization_form, char)
        if normalized_char == target_char:
            print(f"U+{codepoint:04X}: {char} -> {normalized_char}")

def main():
    print("Available normalization forms:")
    print("1. NFD (Normalization Form Decomposed)")
    print("2. NFC (Normalization Form Composed)")
    print("3. NFKD (Normalization Form Compatibility Decomposed)")
    print("4. NFKC (Normalization Form Compatibility Composed)")

    form_choice = input("Select a normalization form (1-4): ")
    normalization_forms = ['NFD', 'NFC', 'NFKD', 'NFKC']
    normalization_form = normalization_forms[int(form_choice) - 1]

    target_char = input("Enter the target character to check (e.g., '.'): ")

    print(f"Checking for characters that normalize to '{target_char}' using {normalization_form}...")

    normalize_and_check(normalization_form, target_char)

if __name__ == "__main__":
    main()
