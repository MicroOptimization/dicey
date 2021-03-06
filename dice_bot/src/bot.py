"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import discord
import key_retriever
import functions

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        self.text_channel_names = []
        self.text_channels = []
        
        for i in client.get_all_channels():
            self.text_channel_names.append(str(i))
            self.text_channels.append(i)
        
        await client.change_presence(activity=discord.Game(name="with Luck"))
        
    async def on_message(self, message):    
        print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
        text = message.content
        words = text.split(" ")
        
        if words[0].lower() == "dicey,":
            if len(words) >= 2 and words[1].lower() == "roll":
                if len(words) >= 3 and words[2].isdigit():
                    faces = int(words[2])
                else:
                    faces = 6
                
                value = functions.roll_dice(faces)
                
                await message.channel.send("Dicey rolled...")
                await message.channel.send("...{}!".format(value))
            elif len(words) >= 2 and words[1].lower() == "flip":
                faces = 2
                value = functions.roll_dice(faces)
                
                if value == 1:
                    side = "Heads"
                else:
                    side = "Tails"
                
                await message.channel.send("Dicey flipped...")
                await message.channel.send("...{}!".format(side))
            elif len(words) >= 2 and (words[1].lower() == "draw" or words[1].lower() == "deal"):
                card = functions.draw_card()
                
                await message.channel.send("Dicey drew...")
                await message.channel.send("...{} of {}!".format(card.rank, card.suit))
                
client = MyClient()

key = key_retriever.get_key() #Insert your key here

client.run(key)
