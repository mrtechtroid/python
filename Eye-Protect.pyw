
# Github: MrTechtroid 
from tkinter import *
import time
import random
a = 0
def alert_popup(title, message, path):
    root = Tk()
    root.title(title)
    w = 400     
    h = 200     
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w-100)
    y = (sh - h-100)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    c = Button(root, text="EXIT",width = 10,command = varassign)
    c.pack()
    root.lift()
    mainloop()
def varassign():
    a = 1
    exit()

list = ["Your eyes focus on 50 different objects every second.",
"The only organ more complex than the eye is the brain.",
"Your eyes can distinguish approximately 10 million different colors.",
"It is impossible to sneeze with your eyes open.",
"Ommatophobia is a fear of the eyes.",
"80 percent of all learning comes through the eyes.",
"Your eyes can detect a candle flame 1.7 miles away.",
"Your iris (the colored part of your eye) has 256 unique characteristics; your fingerprint has just 40.",
"Heterochromia is the medical term for having two different colored eyes.",
"Only 1/6 of your eyeball is visible.",
"Your eyes are comprised of rods and cones. Rods allow you to see shapes, while cones are responsible for detecting and deciphering colors.",
"The average person blinks 12 times a minute (bet you just blinked!).",
"The shark cornea is nearly identical to the human cornea, and has even been used in human eye surgery!",
"Your eye is the fastest contracting muscle in the body, contracting in less than 1/100th of a second.",
"The optic nerve contains more than one million nerve cells.",
"In a very basic form, eyes are thought to have first developed in animals around 550 million years ago! ",
"You actually see with your brain, not your eyes. Our eyes function like a camera, capturing light and sending data back to the brain.",
"You see things upside down - it is your brain which turns the image the right way up. ",
"In a single second, it’s possible to blink five times.",
"You are likely to blink more often when you are talking.",
"The eye is the fastest muscle in your body – hence why when something happens quickly, we say ‘in the blink of an eye!’ ",
"A blink typically lasts 100-150 milliseconds. ",
"The human eye can function at 100 percent at any given moment, without needing to rest.",
"Red-eye in photos is caused by light from the flash bouncing off the capillaries in your eyes.",
"If the human eye was a digital camera, it would have 576 megapixels.Photograph of camera",
"On average, you will blink approximately 4,200,000 times in a single year. ",
"We have two eyeballs in order to give us depth perception – comparing two images allows us to determine how far away an object is from us. ",
"Eyes heal quickly. With proper care, it takes only about 48 hours to repair a minor corneal scratch.",
"The world’s most common eye colour is brown. ",
"The first blue-eyed person is said to have lived 6,000-10,000 years ago. ",
"Even if no one in the past few generations of your family had blue or green eyes, these recessive traits can still appear in later generations.",
"Blue-eyed people share a common ancestor with every other blue-eyed person in the world. ",
"During a sight test, health conditions including diabetes and high blood pressure can be detected.",
"Diabetes is the number one cause of blindness in adults in the UK. ",
"Research has found that a tie tied too tightly can increase the risk of glaucoma in men.Photo of eyes",
"In the right conditions and lighting, humans can see the light of a candle from 14 miles away. ",
"Heterochromia refers to a condition where eyes are two different colours. ",
"Contrary to urban myth, contact lenses cannot become ‘lost’ behind your eye due to the structure of your eyeball. ",
"Your eyes start to develop just two weeks after conception. ",
"Although our nose and ears keep growing throughout our lives, our eyes remain the same size from birth. ",
"All babies are colour blind at birth. ",
"Colour blindness is more common in males. ",
"A newborn baby will cry, but not produce any tears. Babies do not produce tears until they are around six weeks old. ",
"Newborn babies can see objects about 8-15 inches away most clearly.",
"The older we get, the less tears we produce. Photo of baby",
"Blind people can see their dreams as long as they weren’t born blind.",
"80 percent of our memories are determined by what we see. ",
"The only cells that survive from the time you are born until death are in your eyes.",
"Eyelashes have an average lifespan of five months. ",
"If you lined up all the eyelashes shed during one human life, they would measure 98 feet long. ",
"Your eyelashes keep dirt out of your eyes. ",
"We have all have unseen, harmless microscopic creatures living in our eyelashes. ",
"Your eyebrows prevent sweat dripping into your eyes. ",
"The space between your eyebrows is called the Glabella. ",
"It’s impossible to sneeze with your eyes open. Photo of person with eyes shut",
"One of the most common cosmetic injuries is poking the eyeball with a mascara wand. ",
"Our eyes close automatically to protect us from perceived dangers.",
"About half of the human brain is dedicated to vision and seeing. ",
"People generally read 25 percent slower on screen than on paper. ",
"When you read or stare at a computer, you blink less often resulting in tired eyes.",
"94 percent of visible premature-aging around the eyes is caused by UV damage.",
"Reading in dim lighting does not damage your eyes, but it may tire them out. ",
"Dogs can’t distinguish between red and green.",
"An ostriches eye is bigger than its brain. ",
"A shark's cornea is used in human eye surgery, as it is the most similar to the human cornea. Photo of camel",
"Scorpions can have as many as 12 eyes and the box jellyfish has 24! ",
"Camel's eyelashes can measure up to 10cm long to protect its eyelashes from blowing sand and debris in the desert. ",
"As well as super long eyelashes, camels also have three eyelids to protect their eyes from sand.",
"Bees have 5 eyes.",
"The eyes of a chameleon are independent from each other, allowing it to look in two different directions at once. ",
"Geckos can see colours around 350 times better than a human, even in dim lighting.",
"The cornea is the only tissue in the human body that doesn’t contain blood vessels. ",
"Dolphins sleep with one eye open. ",
"The largest eye on the planet belongs to the Colossal Squid, and measures around 27cm across. ",
"Snakes have two sets of eyes – one set used to see, and the other to detect heat and movement. Photo of chameleon",
"A dragonfly has 30,000 lenses in its eyes, assisting them with motion detection and making them very difficult for predators to kill. ",
"The four-eyed fish can see both above and below water at the same time. ",
"Snakes have no eyelids, just a thin membrane covering the eye. ",
"Goats have rectangular pupils to give them a wide field of vision. ",
"Owls are the only bird which can see the colour blue. ",
"Most hamsters only blink one eye at a time. ",
"Guinea pigs are born with their eyes open! ",
"A worm has no eyes at all. ",
"An owl can see a moving mouse more than 150 feet away.",
"A scallop has an average of 100 eyes around the edge of its shell to detect predators. Photo of eyes",
"Owls cannot move their eyeballs – which has led to the distinctive way they turn their heads almost all the way around. ",
"Some people have a fear of eyes; it’s called ommatophobia.",
"The muscles in the eye are 100 times stronger than they need to be to perform their function. ",
"Eyes are the second most complex organ after the brain. ",
"Only one sixth of the human eyeball is exposed. ",
"Eyes are able to process 36,000 pieces of information in a single hour.",
"In an average life, your eyes will see 24 million different images. ",
"The human eye only sees three colours: red, blue and green. All other colours are combination of these. ",
"The human eye can see 500 shades of grey.",
"The cornea is the transparent covering of the iris and pupil. Photo of eye with colours",
"Our eyes have small blind spots where the optic nerve passes through the retina, and our brains use the information from the other eye to fill this gap. ",
"Smoking reduces your night vision. ",
"Our eyes are positioned in a hollowed eye socket, to protect the eye. ",
"80 percent of vision impairment worldwide is curable. ",
"Our eyes are made up of over 2 million working parts. ",
"The eyeball weighs around 28 grams.",
"The eye muscles are the most active muscles in the human body.",
"Eye transplants are currently impossible due to the sensitivity of the optic nerve. ",
"Everyone has one eye that is slightly stronger than the other. ",
"Just behind our pupil is the lens - which is round, flat and thicker toward the middle. Photo of woman with blue eyes",
"While a fingerprint has 40 unique characteristics, an iris has 256. This is why retina scans are increasingly being used for security purposes.",
"When working at a computer, you should follow the 20-20-20 rule – look at something twenty feet away from your computer every twenty minutes for twenty seconds.",
"Astigmatism refers to a curvature of the cornea or lens and toric lenses are prescribed to aid the individual’s vision. ",
"When your eyes are watering it may be a sign of dry-eye, and your eyes are producing more moisture to compensate. ",
"Oily fish, vitamin A and vitamin C can all help to preserve good eyesight. ",
"Although the function of tears is to keep eyes clean, scientists don’t understand why we cry when we are upset. ",
"Albinism affects melanin production; perhaps resulting in extra sensitivity to light and a red-eyed appearance. ",
"Your nose gets runny when you cry as the tears drain into your nasal passages. ",
"The Mayans believe that cross-eyes are attractive and so they would make efforts to ensure their children became cross-eyed.",
"Pirates believed that wearing gold earrings improved their eyesight. ",
"The phrase ‘it’s all fun and games until someone loses an eye’ comes from Ancient Rome, as the only rule for their bloody wrestling matches was ‘no eye gouging’. ",
"Your eyes are about 1 inch across and weigh about 0.25 ounce.",
"The human eye can differentiate approximately 10 million different colors.",
"Our eyes remain the same size throughout life, whereas our nose and ears never stop growing.",
"The human eye blinks an average of 4,200,000 times a year. This means if you were given a nickel for every time you blinked you would make $210,000 annually.",
"Eyes are made up of over 2 million working parts.",
"Each individual eye contains 107 million cells and all are light sensitive",
"Your eye is the fastest muscle in your body. Hence, the phrase: “In the blink of an eye.”",
"The world’s most common eye color is brown.",
"Brown eyes are blue eyes underneath. Consequently, a person can receive surgery in order to make their brown eyes blue.",
"“Don’t It Make My Brown Eyes Blue” is a song recorded by American country music artist Crystal Gayle.",
"The night vision of tigers is six times better than that of humans.",
"Ommetaphobia is the fear of eyes.",
"Pirates wore earrings because they believed it improved their eyesight.",
"The average blink lasts for about 1/10th of a second. ",
"While it takes some time for most parts of your body to warm up to their full potential, your eyes are on their “A game” 24/7. ",
"Eyes heal quickly. With proper care, it only takes about 48 hours for the eye to repair a corneal scratch. ",
"Seeing is such a big part of everyday life that it requires about half of the brain to get involved. ",
"Newborns don’t produce tears. They make crying sounds, but the tears don’t start flowing until they are about 4-13 weeks old. ",
"Around the world, about 39 million people are blind and roughly 6 times that many have some kind of vision impairment. ",
"Doctors have yet to find a way to transplant an eyeball. The optic nerve that connects the eye to the brain is too sensitive to reconstruct successfully. ",
"The cells in your eye come in different shapes. Rod-shaped cells allow you to see shapes, and cone-shaped cells allow you to see color. ",
"You blink about 12 times every minute. ",
"Your eyes are about 1 inch across and weigh about 0.25 ounce. ",
"Some people are born with two differently colored eyes. This condition is heterochromia. ",
"Even if no one in the past few generations of your family had blue or green eyes, these recessive traits can still appear in later generations. ",
"Each of your eyes has a small blind spot in the back of the retina where the optic nerve attaches. You don’t notice the hole in your vision because your eyes work together to fill in each other’s blind spot. ",
"Out of all the muscles in your body, the muscles that control your eyes are the most active. ",
"80 percent of vision problems worldwide are avoidable or even curable. ",
"Did you know that the average blink takes 1/3 of a second?",
"Seeing is so important that it takes up more than 50 percent of the brain’s functionality.",
"Newborns don’t shed tears, though they do know how to cry.",
"You blink about 15-20 times in a minute.",
"The most active muscles in your body are in your eyes.",
"Your eyes can get sunburned.",
"Blue eyed people are more tolerant of alcohol and less tolerant of the sun",
"If the human eye were a digital camera it would have 576 megapixels.",
"We spend about 10 percent of our wake time with our eyes closed.",
"An ostrich’s eye is bigger than its brain.",
"Chameleons can move their eyes in two directions at once.",
"A single scallop can possess over a hundred eyes",
"Your eyes contain around 107 million light sensitive cells.",
"Dolphins can sleep with one eye open.",
"Birds, cats and dogs have three eyelids.",
"Yes, you can sneeze with your eyes open and no, your eyes won’t fall out.",
"Ommatophobia is the fear of eyes.",
"Humans can see more shades of green than any other colour.",
"The world’s most common eye colour is brown.",
"Dogs cannot distinguish between red and green.",
"The lifespan of the average eyelash is 5 months, the rest of your hair will last 2-4 years.",
"The eye has over 2 million moving parts.",
"Your eyes contain 7 million cones which help you see colour and detail and 100 million cells called rods which help you to see better in the dark.",
]
def countdown():
    t = 900
    while t > 0:
        t -= 1
        time.sleep(1)
        alert_popup("Alert", "Hey Its 15 min since you didnt take a rest for your eyes.", list[random. randint(0,165)])
        countdown()


countdown()
