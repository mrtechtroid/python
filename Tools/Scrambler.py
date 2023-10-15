# Github: Mr Techtroid
import random
sampletext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc fermentum, turpis vel aliquet imperdiet, velit sapien viverra est, at tempor massa sapien hendrerit felis. Curabitur fringilla, ante id vulputate elementum, mauris magna fermentum velit, in tempor orci ante et magna. Suspendisse cursus, purus sed dictum ullamcorper, urna mi egestas nisl, sit amet iaculis libero lorem eget neque. In imperdiet tempor sagittis. Sed lobortis sagittis blandit. Fusce convallis commodo accumsan. Quisque maximus ligula augue, ut ultrices neque fermentum sit amet. Nam vitae dolor iaculis, pharetra risus in, vehicula ligula. Aenean sit amet diam bibendum, blandit sapien sollicitudin, consectetur neque."

def wordscramble():
	words = sampletext.split(" ")
	newstring = ""
	for _ in range(0,len(words)):
		terms = len(words)
		a = random.randint(0,terms-1)
		newstring +=  words[a] + " "
		words.pop(a)
	print(newstring)

wordscramble()

def sentencescramble():
	sentences = sampletext.split(".")
	newsentences = ""
	for _ in range(0,len(sentences)):
		nosent = len(sentences)
		a = random.randint(0,nosent-1)
		newsentences +=  sentences[a] + "."
		sentences.pop(a)

	print(newsentences)



sentencescramble()
