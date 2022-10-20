import pyttsx3


assistantVoice = int(input('''Select you assistants Voice 
  [1] Male 
  [2] Female : '''))


if assistantVoice == 1:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
elif assistantVoice == 2:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
else:
    print("Invalid Input")



'''-----------------------------------------------------------------------------------------------------------'''
file = open("story1.txt","w+")#The Cursed Man or King?
s1 = """For several generations, stories from Africa have traditionally been passed down by word of mouth. Often, after a hard day’s work, the adults would gather the children together by moonlight, around a village fire and tell stories. This was traditionally called 'Tales by Moonlight'. Usually, the stories are meant to prepare young people for life, and so each story taught a lesson or moral
In the African folktales, the stories reflect the culture where diverse types of animals abound. The animals and birds are often accorded human attributes, so it is not uncommon to find animals talking, singing, or demonstrating other human characteristics such as greed, jealousy, honesty, etc. The setting in many of the stories exposes the reader to the land form and climate within that region of Africa. References are often made to different seasons such as the 'dry' or 'rainy' season and their various effects on the surrounding vegetation and animal life.""""
file.write(s1)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file1 = open("story2.txt","w+")#Lion & rat
s2="""A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her.
"Spare me!" begged the poor Mouse. "Please let me go and some day I will surely repay you."
The Lion was much amused to think that a Mouse could ever help him. But he was generous and finally let the Mouse go.
Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net. Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free.
"You laughed when I said I would repay you," said the Mouse. "Now you see that even a Mouse can help a Lion."""
file1.write(s2)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file2 = open("story3.txt","w+")#two goats
s3="""An orphan, and possessed of an adequate income, he cut a dash, as the saying is. He had a good figure and a good carriage, a sufficient flow of words to pass for wit, a certain natural grace, an air of nobility and pride, a gallant moustache and an eloquent eye, attributes which women like.

He was in demand in drawing-rooms, sought after for valses, and in men he inspired that smiling hostility which is reserved for vital and attractive rivals. He had been suspected of several love-affairs of a sort calculated to create a good opinion of a youngster. He lived a happy, care-free life, in the most complete well-being of body and mind. He was known to be a fine swordsman and a still finer shot with the pistol."""
file2.write(s3)
'''-----------------------------------------------------------------------------------------------------------'''


'''-----------------------------------------------------------------------------------------------------------'''
file3 = open("story4.txt","w+")#Handful of Grain and Coins
s4="""The answer: “A Thousand Grandparents; all different, some intense, some playful and all with different experience and wisdom to share. A thousand beautiful awakened souls sharing the gift of presence, truth and intimacy of spirit.”

This is a film based project, a heritage collection of wisdom, inspiration, delight and love freely accessible by all.  The project starts by asking storyteller’s the question,

“If you had one story to tell, as a gift of consciousness, a story that could change a child’s life, open their minds and hearts, help them to find their inner light, what would it be?”

Or, “If you could go back to the younger you and tell that younger you one story of inspiration or wisdom, what would it be?”"""
file3.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''




'''-----------------------------------------------------------------------------------------------------------'''
file4 = open("story5.txt","w+")#Saluting the Donkeys
s5= """Our longer range vision is to create mobile cinema, and street cinema packs to take to impoverished areas, orphanages, refugee camps. We want to reach a grand scale and provide a robust web service, providing stories in multiple languages. Once fully developed the maintenance of that system would be relatively low, easily managed by the Foundation, and freely available to all.

The beauty of this project is that we can develop flexibly in increments, building into the global service, and yet still bringing benefit to children globally, through the internet, from the very start.
"""
file4.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''
choice="""Which story you want to hear
1)The Cursed Man or King?
2)Lion & Rat
3)Two Goats
4)Handful of Grain and Coins
5)Saluting the Donkeys
"""
file.close()
file1.close()
file2.close()
file3.close()
file4.close()
r1= open("story1.txt","r")
r2= open("story2.txt","r")
r3= open("story3.txt","r")
r4= open("story4.txt","r")
r5= open("story5.txt","r")
engine.say(choice)
engine.runAndWait()
inp = int(input("1/2/3/4/5 :- "))
if(inp == 1):
    for x in r1:
        print(x)
        engine.say(x)
        engine.runAndWait()
        r1.close()
elif(inp == 2):
    for x in r2:
        engine.say(x)
        engine.runAndWait()
        r2.close()
elif(inp == 3):
    for x in r3:
        engine.say(x)
        engine.runAndWait()
        r3.close()
elif(inp == 4):
    for x in r4:
        engine.say(x)
        engine.runAndWait()
        r4.close()
elif(inp == 5):
    for x in r5:
        engine.say(x)
        engine.runAndWait()
        r5.close()
else:
    print("Invalid Input")
