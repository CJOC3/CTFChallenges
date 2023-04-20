### Description 
- I've hidden a flag in this file. Can you find it? <a href="Forensics is fun.pptm">Forensics is fun.pptm</a> 

### Category 
- Forensics 

### Approach 
- First instinct is to run the file by the command `file` to check whether the extension is appropriate to the file type. As a result, it is indeed a PowerPoint file
but with enabled macro (.pptm)
- After that, I checked the file using `binwalk` to see if there are any archived files. It did have archived files. 
- Then, I opted to extract all of the archive files using `binwalk -e`.
- Changing directory to the extracted files, we are presented with different files and directories. 
- Checking the directories one-by-one manually can be time-consuming. I opted to use the command `ls -l` on a specific directory to let me see the summary of contents of that particular directory. 
- The directory that piqued my interest was the `slideMasters` as it has a `hidden` file.
<img src=mhwe1.png>
- I then checked `hidden`'s file type, with is just an ASCII text. 
- `cat hidden` reveals a base-64 string `Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q`.
- I chose to save this string to a text file so that I can use this command to remove whitespaces and newlines of a text just to be sure 
`cat hidden.txt | tr -d " \t\n\r`
Decoding the base64 string reveals the flag.

### Flag 
- picoCTF{D1d_u_kn0w_ppts_r_z1p5}
