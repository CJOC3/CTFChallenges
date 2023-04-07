### Description 
- Can you look at the data in this binary: <a href="static"> static? </a>  This BASH <a href="ltdis.sh">script</a> might help!

### Category 
- General Skills 

### Approach 
- I opted first to determine the file types of the given files using `file`. As a result, I learned that they were executable files. 
- I first executed static by `./static`. It printed a statement hinting that the flag is in the file somewhere. 
- Next, I execufted ltdis.sh `./ltdis.sh` however it prompted that the static file must be included. Thus, `./ltdis.sh static` prompted that the disassembly of the file 
`static` was successful. 
- The previous command produced two text files, namely `static.ltdis.strings.txt` and `static.ltdis.x86_64.txt`. 
- I had a hunch to look for the flag first at `static.ltdis.strings.txt` by  `cat static.ltdis.strings.txt | grep pico` since I know the format of the flag includes 
the word pico. Hence, the flag is revealed. 

### Flag 
- picoCTF{d15a5m_t34s3r_ae0b3ef2}
