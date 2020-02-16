import random
lower =('abcdefghijklmnopqrstuvwxyz')
upper =('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numb = ('0123456789')
lowerr =''.join(random.sample(lower,len(lower)))
upperr =''.join(random.sample(upper,len(upper)))
numbr = ''.join(random.sample(numb,len(numb)))
print(str(lowerr)+str(upper)+str(numbr))
