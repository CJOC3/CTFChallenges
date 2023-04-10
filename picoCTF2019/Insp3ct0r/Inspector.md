### Description
- Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/9670/

### Category 
- Web Exploitation 

### Approach
- Based on the description of the challenge, the `Web Developer Tools` of Mozilla Firefox browser can be utilized again to inspect the webpage. 
- Looking at the `How` part of the webpage, it gives us a clue that the flag may be found in three parts, in the sequence of HTML, CSS, and JS components. 
- The HTML component can be inspected by navigating to the `Inspector` tab. The first part of the flag can be found at the body. 
- The CSS component can be inspected by navigating to the `Style Editor` tab. The second part of the flag can be found at the css file `mycss.css`.
- The JS compnent can be inspected by navigating to the `Debugger` tab. The final part of the flag can befound at the js file `myjs.js`.

### Flag
- picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}
