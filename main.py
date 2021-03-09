import discord
from discord.ext import commands


bot = commands.Bot(command_prefix= "?", description= "Cerberus by 7empest15.")




@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
async def botinfo(ctx):
    await ctx.send("Bot crée par 7empest15!")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong")


@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDesc = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur {serverName} contient {numberOfPerson} personnes. \n La description du serveur {serverDesc}. \n Ce serveur contient {numberOfTextChannels} salons textuels ainsi que {numberOfVoiceChannels} channel vocaux."
    await ctx.send(message)


@bot.command()
async def say(ctx, *text):
    await ctx.send(" ".join(text))


@bot.command()
@commands.has_permissions(ban_members=True)
async def clear(ctx, number : int):
    messages = await ctx.channel.history(limit = number + 1).flatten()
    for message in messages:
        await message.delete()


@bot.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick du serveur pour {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} à été banni pour {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} a été debanni")
            return
    await ctx.send(f"L'utilisateur {user} ne fait pas parti de la liste des malfrats...")


async def createMuteRole(ctx):
    muteRole = await ctx.guild.create_role(name = "Mute",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Mute pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(muteRole, send_messages = False, speak = False)
    return muteRole


async def getMuteRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Mute":
            return role



@bot.command()
@commands.has_permissions(manage_guild = True)
async def announce(ctx, *message):
    channel = bot.get_channel(#id of channel)
    await channel.send(" ".join(message))
    await ctx.message.delete()


def isOwner(ctx):
	return ctx.message.author.id == #your discord id



@bot.command()
async def ms(ctx):
    await ctx.send('**Latence:** {0}'.format(round(bot.latency, 1)))
    await ctx.message.delete()


@bot.command()
@commands.check(isOwner)
async def off(ctx):
    await ctx.send("Arret du bot...")
    exit()




bot.run("Your token")
