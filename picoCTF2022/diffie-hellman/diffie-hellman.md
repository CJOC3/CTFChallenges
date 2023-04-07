# Description
Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. 
Can you figure out the contents of the message?

Ciphertext: `H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_7IGK58KC`

I entered the given information in https://www.dcode.fr/diffie-hellman-key-exchange, which in turn gives me the secret key `(a,b) = 5`
- 5 could be interpreted as a key for the Caesar cipher

Using https://cryptii.com/pipes/caesar-cipher and an alphabet of `abcdefghijklmnopqrstuvwxyz0123456789`, the flag is revealed: `C4354R_C1PH3R_15_4_817_0U7D473D_2DBF03F7`

