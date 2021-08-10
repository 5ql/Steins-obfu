import sys
import os

def main():
  
	if len(sys.argv) < 2:
		print("Usage: python3 {} `your input`".format(os.path.basename(__file__)))
	else:
       	        sc = "\\x" + "\\x".join("{0:x}".format(ord(c)) for c in sys.argv[1])
	        shellcode =f'"{sc}"'
		print("[*] Here is the encoded string:\n {}".format(shellcode))

if __name__ == “main”:
	main()

