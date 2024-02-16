thirdOutput = """-.....-.
-..-.---
--..-.-.
--..---.
-....-.-
-.-.....
--..-.-.
--..-...
--..--..
-..----.
-.-.....
-.---.--
-.--.---
-.-.....
--..-..-
-..---.-
-.-.....
-...--..
-..---..
-..-.-.-
--..----
-...-.-.
-.-.....
-..-.-.-
--..----
-..-...-
-.-.....
--..-.-.
-...--..
-..---..
-..-.-.-
--..----
-..--...
-.-.....
-.--...-
-..---..
--..-.--
-..---.-
-.-.....
-..--...
--..--..
--..-...
-...-.-.
-.------
-....-..
-.-.-.-.
-.--.--.
-.-.--.-
-...-.--
-..-.-..
-..--.--
-.-----."""

possibilities = [('0', '1'), ('1', '0')]
for possible in possibilities :
    try :
        result = bytes([int(line.replace('-', possible[0]).replace('.', possible[1]), 2) for line in thirdOutput.split('\n')])
        print(result.decode())
    except :
        pass