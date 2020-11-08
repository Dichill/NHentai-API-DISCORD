import pyautogui
import discord
import wikipedia
from googletrans import Translator
from discord.ext import commands
import importlib
import os

api = importlib.import_module('nhentaiapi')
nhentai = api.nhentai()

client = commands.Bot(command_prefix= '.')
livestream = 'False (Automatic)'

@client.event
async def on_ready():
    print('[DrX] Bot is now Online')
    await client.change_presence(activity=discord.Game(name=".cmds for Commands | Dichill"))

@client.command(aliases=['nh'], pass_context=True)
async def _nh(ctx, *, code):
    loadingembed = discord.Embed(title="⌛ Please wait!",
                                 description="I have a shit laptop and a shit wifi. Please wait for it to search <3",
                                 color=0xe10e0e)
    loadingembed.set_author(name="DrX | NHentai")
    await ctx.send(embed=loadingembed)
    status = nhentai.check(code)
    title = nhentai.getTitle(code)
    #tag = ", ".join(map(str, nhentai.getTags(code)))
    thumbnail = nhentai.getThumbnail(code)
    if status == True:
        nhentai.getTags(code)
        embed = discord.Embed(title=title, description="Tags: ", color=0xe10e0e)
        embed.set_author(name="DrX | NHentai", url=nhentai.source)
        embed.set_thumbnail(url=thumbnail)
        await ctx.send(embed=embed)
    elif status == False:
        embed = discord.Embed(title="No certain language exist!", description="Unfortunately the code does not exist or has been taken down.", color=0xe10e0e)
        embed.set_author(name="DrX | NHentai")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Oops! An Error has occured",
                              description="It seems like theres a problem between Dichill's PC and NHentai's server.",
                              color=0xe10e0e)
        embed.set_author(name="DrX | NHentai")
        await ctx.send(embed=embed)

@client.command(aliases=['nhqprev'], pass_context=True)
async def _nhqprev(ctx, *, code):
    title = nhentai.getTitle(code)
    title = title.replace('|', '')
    status = nhentai.check(code)

    cwd = os.getcwd()  # get the current path
    prevpath = cwd + "\\image\\preview\\"

    try:
        if status == True:
            loadingembed = discord.Embed(title="⌛ Please wait!",
                                         description="Downloading Pictures and sending em here~",
                                         color=0xe10e0e)
            loadingembed.set_author(name="DrX | NHentai")
            await ctx.send(embed=loadingembed)
            prevembed = discord.Embed(title=title,
                                         description="Previews for " + title,
                                         color=0xe10e0e)
            prevembed.set_author(name="DrX | NHentai")
            await ctx.send(embed=prevembed)
            for i in range(10):
                if os.path.exists(prevpath + title):
                    await ctx.send(file=discord.File(prevpath + title + "/" + " " + str(i + 1) + ".png"))
                else:
                    nhentai.getPreviews(code, 10)
                    await ctx.send(file=discord.File(prevpath + title + "/" + " " + str(i + 1) + ".png"))
        else:
            embed = discord.Embed(title="Oops! An Error has occured",
                                  description="Either the code doesn't exist or the connection between the server is very slow.",
                                  color=0xe10e0e)
            embed.set_author(name="DrX | NHentai")
            await ctx.send(embed=embed)

    except Exception as e:
        errorembed = discord.Embed(title="⌛ An Error has occured!",
                                     description="Please message me the details about the error: " + str(e) + " if it talks about the directory not existing. Ignore this error.",
                                     color=0xe10e0e)
        errorembed.set_author(name="DrX | NHentai")
        await ctx.send(embed=errorembed)

@client.command(aliases=['nhfprev'], pass_context=True)
async def _nhfprev(ctx, *, code):
    title = nhentai.getTitle(code)
    title = title.replace('|', '')
    status = nhentai.check(code)

    cwd = os.getcwd()  # get the current path
    prevpath = cwd + "\\image\\preview\\"

    try:
        if status == True:
            loadingembed = discord.Embed(title="⌛ Please wait!",
                                         description="Downloading Pictures and sending em here~ This will take a while ^.^",
                                         color=0xe10e0e)
            loadingembed.set_author(name="DrX | NHentai")
            await ctx.send(embed=loadingembed)
            prevembed = discord.Embed(title=title,
                                         description="Previews for " + title,
                                         color=0xe10e0e)
            prevembed.set_author(name="DrX | NHentai")
            await ctx.send(embed=prevembed)
            for i in range(50):
                if os.path.exists(prevpath + title):
                    await ctx.send(file=discord.File(prevpath + title + "/" + " " + str(i + 1) + ".png"))
                else:
                    try:
                        nhentai.getPreviews(code, 50)
                        await ctx.send(file=discord.File(prevpath + title + "/" + " " + str(i + 1) + ".png"))
                    except Exception:
                        await ctx.send(file=discord.File(prevpath + title + "/" + " " + str(i + 1) + ".png"))

        else:
            embed = discord.Embed(title="Oops! An Error has occured",
                                  description="Either the code doesn't exist or the connection between the server is very slow.",
                                  color=0xe10e0e)
            embed.set_author(name="DrX | NHentai")
            await ctx.send(embed=embed)

    except Exception as e:
        errorembed = discord.Embed(title="⌛ An Error has occured!",
                                     description="Please message me the details about the error: " + str(e) + " if it talks about the directory not existing. Ignore this error.",
                                     color=0xe10e0e)
        errorembed.set_author(name="DrX | NHentai")
        await ctx.send(embed=errorembed)


@client.command()
async def nhelp(ctx):
    embed = discord.Embed(title="📓 NHentai Code Searcher", description="Found some codes? How about share it with us and read it together <3~")
    embed.add_field(name="MODE", value="``.nh <code>`` Search the specified code and browse it! Can be previewed\n``.nhqprev <code>`` 1 - 10 quick preview of the piece <3\n``.nhprev <code> <page>`` someone mentioned a page? Lets get to it~\n``.nhfprev <code>`` full preview of the doujin! if it exceeds 50+ it will stop.")
    await ctx.send(embed=embed)


client.run('NjUwMjkxMjM2MjEyNzAzMjMz.XeJM6A.DUEENU7ynWwjxly5fFW3vzYQcYw')