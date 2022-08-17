import discord


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('727wysi'):
    await message.channel.send('WYSI?!?!?!')

client.run('MTAwOTMwNTYyNzcxNTE5NDg5MQ.GLr6N3.XNVDeujM3jsBqIYZ9YECDk7DYnuqnf6-DbNTek')
