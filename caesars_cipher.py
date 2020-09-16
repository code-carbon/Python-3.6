coded = input("Enter the script: ")
condition = input("Enter the condition:[decrypt, encrypt]: ")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if condition == "decrypt":
  for a in coded:
    if(a in alphabet):
      coded = coded.replace(a,alphabet[alphabet.index(a)-2])
  print("Decrypted:",coded)
elif condition == "encrypt":
  for a in coded:
    if(a in alphabet):
      coded = coded.replace(a,alphabet[alphabet.index(a)+2])
  print("Encrypted:",coded)

