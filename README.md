# unicodenormalizationcharfinder
A Python tool to check which Unicode characters normalize to a specified character using various Unicode normalization forms (NFD, NFC, NFKD, NFKC).

Can be helpful in identifying which Unicode characters normalize to a dot "." character. For example, it can be used to identify unicode character which will help to bypass LFI filters that block the dot character. If it normalizes user input through forms like NFKC, an attacker may bypass the filter by providing a Unicode character that normalizes into the dot "." character.
