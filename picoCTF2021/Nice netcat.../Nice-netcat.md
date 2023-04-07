### Description
- There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 49039, but it doesn't speak English...

### Category
= General Skills 

### Approach 
- Run the aforementioned command in a console `nc mercury.picoctf.net 49039`. 
- In doing so, it prompts various numbers. Upon closer inspection, I realized that these are ASCII values in decimal. 
- Thus, I used an ASCII to Text Converter online such as https://codebeautify.org/ascii-to-text. 
- Once I entered the ASCII values from the program, it revealed the flag. 

### Flag 
- picoCTF{g00d_k1tty!_n1c3_k1tty!_3d84edc8}
