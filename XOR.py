''' XOR encryption by siroyasha '''
class XOR_encryptor:
    def __init__(self,message):
        # converts message to ASCII character 
        # if yu are using uppercase then make the key also uppercase 
        self.message=[ord(m) for m in message.upper() ]
        self.ciphertext=[] # the encrypted text after xor operatrion
        self.key_str=[] # holds the ascii values of self.key synced with self.message 
        self.key="KEY"
        # choose a complex key for the message i have chosen 'key' for clarity  
    def _xor(self):
     
        key_str=self.key+"".join([self.key[i] for i in range(len(self.message)-len(self.key))])
        self.key_str=[ord(i) for i in key_str]
        
        self.ciphertext=[self.message[i]^self.key_str[i] for i in range(len(self.message))]
        return self.ciphertext
    def decryption(self):
        # this methods the encrypted ciphertext 
        decrypt="".join([chr(self.key_str[i]^self.ciphertext[i]) for i in range(len(self.key_str))])
        return decrypt
        
if __name__=="__main__":
  A=XOR_encryptor("hello")
  A._xor()
  A.decryption()