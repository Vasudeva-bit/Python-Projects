import hashlib
import sys
import requests
def list_of_hash(first5) :
url='https://api.pwnedpasswords.com/range/' +first5
hash_res=requests.get(url)
return hash_res
def check_hash(hashlist,checkhash) :
hashlist=(line.split(':') for line in hashlist.text.splitlines())
for hashcheck,counter in hashlist:
if checkhash==hashcheck:
return counter
return 0
def pass_to_hash(password) :
hashpass=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
first5_char,rest=hashpass[:5],hashpass[5:]
hashlist=list_of_hash(first5_char)
return check_hash(hashlist,rest)
def main(arg) :
for i in arg :
count=pass_to_hash(i)
if count:
print(f'your pass was {count} times hacked...please change it')
else :
print(f'your pass is good :) use it....')
return 'okay'
if __name__=='__main__' :
sys.exit(main(sys.argv[1:]))