### Description 
- Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:64944/

### Category 
- Web Exploitation 

### Approach 
- As the title of the challenge suggests, we must focus on the cookies provided by the url. 
- This can be done by using the `Web Developer Tools` of the Mozilla Firefox browser, located in the Storage tab. 
- Instead of searching what cookies can be entered in the webpage, the `value` of the cookie with a name of `name` can be changed instead. As a result, 
a new cookie is entered upon refreshing the page. 
- So, we have to keep changing the value of the cookie until we stumble upon the right one that will give us the flag. The magic number is 18.

### Flag 
- picoCTF{3v3ry1_l0v3s_c00k135_cc9110ba}
