## This challenge was given by a mentor to train us for the upcoming Hack For Gov.

Task: Decode the secret word!

`R00yRE1OSlRHNFpUR01aWUdZWlRNTUpUR1VaVEtNWldHTVpUTU1aVEdBWlRNTlJUR1kzRE1OQlRHQVpUQU1aUkdNNERHTVJUSEVaVFNNWlpHTVpUR01aV0dRWlRLTVpZR1kyRE1NUlRHRTNESU5SVUdNNERNTVJXR1laVFNNWlhHWTNER05SVEhFWlRPTVpUR1kyRE1NWlRIRVpUU05SU0dZM0RHTlJXR00zRElOUlRHTTNER05CV0dJWlRLTVpWR00yVEdNQldHSTNEST09PQ%3D%3D`

Looking at the nature of this value, it can be concluded that a URL Decoder must be used because of the presence of `%` symbols. 
- Using https://meyerweb.com/eric/tools/dencoder/, it outputs a new string `R00yRE1OSlRHNFpUR01aWUdZWlRNTUpUR1VaVEtNWldHTVpUTU1aVEdBWlRNTlJUR1kzRE1OQlRHQVpUQU1aUkdNNERHTVJUSEVaVFNNWlpHTVpUR01aV0dRWlRLTVpZR1kyRE1NUlRHRTNESU5SVUdNNERNTVJXR1laVFNNWlhHWTNER05SVEhFWlRPTVpUR1kyRE1NWlRIRVpUU05SU0dZM0RHTlJXR00zRElOUlRHTTNER05CV0dJWlRLTVpWR00yVEdNQldHSTNEST09PQ==`

At this point, the presence of upper-case characters, lower-case characters, message padding, and numbers give away that this is encoded in a base-64 scheme. 
- Using https://simplycalc.com/base64-decode.php, it now outputs a new string `GM2DMNJTG4ZTGMZYGYZTMMJTGUZTKMZWGMZTMMZTGAZTMNRTGY3DMNBTGAZTAMZRGM4DGMRTHEZTSMZZGMZTGMZWGQZTKMZYGY2DMMRTGE3DINRUGM4DMMRWGYZTSMZXGY3DGNRTHEZTOMZTGY2DMMZTHEZTSNRSGY3DGNRWGM3DINRTGM3DGNBWGIZTKMZVGM2TGMBWGI3DI===`

The string at this point has identifying characteristics such as the presence of only upper-case characters, message padding and numbers. Thus, it is encoded in a base-32 scheme.
- Using https://simplycalc.com/base32-decode.php, it outputs `34653733386361353536336330366366643030313832393939333364353864623164643862663937663639373364633939626636636463363462353535306264`

The resulting string is encoded in base-16 since it uses the hexadecimal number system (0123456789ABCDEF). There is also no more padding present. 
- Using https://simplycalc.com/base16-decode.php, it now outputs a hash `4e738ca5563c06cfd0018299933d58db1dd8bf97f6973dc99bf6cdc64b5550bd`.

Using https://hashes.com/en/decrypt/hash and ticking the option to `show algorithm of founds`, the secret word is revealed: `s3cr3t` decrypted with SHA256PLAIN.
