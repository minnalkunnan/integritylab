Minnal Kunnan
Cody Thompson

Integritylab


Task 1 - Can be found in CBC-PaddingOracle directory
	A. Proof of concept of a padding oracle attack. We eavesdrop a ciphertext, then continually guess valid paddings for it (in the form of the PKCS#7 padding scheme). When we get a guess correct we can decipher the plaintext value of that character. Doing this repeatedly we can decipher the entire ciphertext.

Task 2 - In integrityLab directory
	A. sha1.py is our implementation of sha1
	B. findcollision.py - Found a collision on bottom 50 bits using the values
	23612730 -> 48cf792af65204f61439c92df40eb77a7129a491
	72349653 -> 58c955b55efe3cfe3a1b0c7b2a5eb77a7129a491

Task 3 - In KeyedHash-LengthExtension directory
	A. We take a message given to us from a post, and modify it by adding padding to fill up an exact multiple of 512 bit blocks. Given the secret length of 40 bytes and the message length, we can do this. We then hash our message with the given h0, ... , h4 from the tag, along with the size of the message with our added padding that the original post had. We use that hash with the entire message ({secret}{original message}{added padding}{our message}). To do this, replace in lengthExtensionAttack.py in the appropriate places the original message, the new message, and the original tag in the constant spots.
	B. We implemented this within task3b in the main folder.

Task 4 In HMAC-Timing directory
	A. Since the server doesn't use a time constant function to check whether our mac correct we created a timing attack against it by slowly guessing each character of the tag string. We compile the elapsed time each on each attempt at guessing a character of the tag string. We choose the three tag strings that took the longest amount time as our candidate tags and use them to test all possibilities of the next character in each tag string. Based on which tag string took the longest, we can confirm which of our three initial tag strings had a valid character at that index in the string. We continue to do this for the rest of the string. 

	Unfortunately our implementation still ran into errors with variation in the time it took to verify a tag string. Increasing the sleep time between verifications to .02 allowed us to guess around 12 characters consistently correctly before the random variation disrupted our attack. We might be able to better improve our attack by running it on a non-personal machine with no background tasks running or in a virtual machine.

	B. We could not correctly guess the entire string with a sleep of .02 or .01 but we consistently got 12 characters of the string correct. So we then tested with a sleep of .007 and got only 3 characters correct. Even with .008 we got around 12 characters so we determined the cutoff for our implementation guessing 12 characters correctly was .007
	
	C. Again, as with Part B, we could not correctly guess the entire string with a sleep of .02 or .01 but we consistently got 12 characters of the string correct. Therefore we came up with an algorithm to break our crack consistently at .01 seconds, where our crack would not even be able to predict the first character with over 1 / 256 chance of certainty. Instead of breaking on each character, we check every one before returning false, sleeping at each check.
