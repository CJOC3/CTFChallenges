### Description
- Figure out how they moved the flag.

### Category 
- Forensics 

### Approach 
- Upon opening the pcap file in Wireshark, the names of certain files `instructions.txt` and `plan` can be seen immediately.
- Checking their corresponding data packets shows us two strings that are encrypted in ROT13.
- For `instructions.txt`, I copied the data `GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA` as a printed as a printable text so that I can paste it to a rot13 ciper such as https://rot13.com.
- As for `plan`, I did the same thing with its associated data packet. Its string is `VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF` 
- Naturally, `instructions.txt` gave me an instinct to check it first because of its name. 
- Decoding the string from `instructions.txt` said that `TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`
- It mentioned something about the plan. Decoding the string from `plan` stated 
`IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS`
- It wants us to check some photos. I exported the objects from TFTP in Wireshark and checked out the photos one by one. 
- At first, I ran the photos through the commands `strings`, `exiftool`, `binwalk` and `zsteg`. These didn't give me anything at first which is why I was stuck for a while.
- Then I checked the photos again using `steghide info`. However, using this tool requires us to input a passphrase. From the decoded string of `plan`, it mentioned
that the person hid the flag with `DUEDILIGENCE`. This is what I entered for the passphrase of each. 
- Nothing came out of the first 2 bmp pictures. However, the third bmp picture `picture3.bmp` revealed that it had an embedded file `flag.txt`. 
- I extracted the file using `steghide extract -sf picture3.bmp` and entered the same passphrase again. 
- `flag.txt` was successfully extracted. 

### Flag 
- picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
