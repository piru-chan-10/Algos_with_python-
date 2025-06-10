''' RSA by priyanshu Rawat aka siroyasha'''
import random
class RSA:
    def __init__(self,message): # example message="hello world"
        self.message=message
        self.e=65537
        self.e_inv=0 
        self.values={
            
        }   # empty dictionary stores (p,q,phi,e,d,e_inverse)
    def gcd(self,num1,num2):
        if num1==0:
            return num2
        if num2==0:
            return num1
        if num1>num2:  
            return self.gcd(num1%num2,num2) # call recursively gcd for remainder 
        else:
            return self.gcd(num2%num1,num1) # call recursively gcd for remainder 
    def is_prime(self,num):
        is_true=True
        x=[i for i in range(2,num) if num%i==0]
        if x==[]:
            return True
        else:
            return False
      # generate random primes 
    def initiallize(self):
        t1,t2=random.randint(1000,4000),random.randint(1000,4000)
        while(self.is_prime(t1)!=True):
            t1=random.randint(1000,4000)
        while (self.is_prime(t2)!=True):
            t2=random.randint(1000,4000)
        self.p,self.q=t1,t2
        self.phi=(self.p-1)*(self.q-1)
        self.values.update({
            "P":self.p,"Q":self.q,"phi":self.phi
        })
        return self.p,self.q,self.phi
    # private and public keys 
    def keys(self):
        # self.e=[i for i in range(self.phi//2,self.phi) if self.gcd(i,self.phi)==1]
        self.e_inv=[ i for i in range(2,self.phi) if (i*self.e)%self.phi==1 ]
        self.values.update({
            "E":self.e,"E_INV":self.e_inv[0]
        }) 
        return self.e,self.e_inv
    # ciphertext encryption
    def encryption(self):
        self.plaintext=[ord(i) for i in self.message]
        self.ciphertext=[pow(m,self.e,(self.p*self.q) )for m in self.plaintext]
        self.values.update({"ciphertext":self.ciphertext})
        return self.plaintext,self.ciphertext
    # decryption
    def decryption(self):
        n=self.p*self.q
        val=[pow(c,self.e_inv[0],n) for c in self.ciphertext]
        self.decrypt="".join(chr(m) for m in val)
        self.values.update({
          "decryption":self.decrypt
        })
        return self.decrypt
        
        
s=RSA("hell0") 
s.initiallize()
s.keys()
s.encryption()
s.decryption()
for key,val in s.values.items():
  print(key,'->',val)
  
