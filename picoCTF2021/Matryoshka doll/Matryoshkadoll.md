### Description
- Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: <a href="dolls.jpg">this</a>

### Category 
- Forensics 

### Approach 
- The name of the challenge gives us a hint that there may be something stored in the given file. First, I checked the file type of the first image. 
- It has an extension of `.jpg` but according to the `file` command, it should be a PNG file. Thus, I changed its extension to `.png`. 
- To check if there is something stored in the given file, I used the command `binwalk dolls.png`. It showed that there are zip archives within the png image. 
- Running `binwalk -e dolls.png` will extract the files in a new folder. 
- Change directory to `base images` and it shows another file that has `.jpg` extension but upon closer inspection with `file` command again, it is supposed 
to be a PNG. Hence, its extension must be changed to `.png`. 
- The previous steps can just be repeated in order to arrive to the final directory with the flag text document, simulating a matryoshka doll.

### Flag
- picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}
