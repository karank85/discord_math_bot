import discord 
from discord.ext import commands

from sympy import *


client = commands.Bot(command_prefix="%")

@client.event
async def on_ready():
    print("Math bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def sine(ctx, *, question):
    x = symbols('x')
    answer = sin(question)
    await ctx.send(f'Question: {question}\nAnswer: {answer}')

@client.command()
async def tangent(ctx, *, question):
    x = symbols('x')
    answer = tan(question)
    await ctx.send(f'Question: {question}\nAnswer: {answer}')

@client.command()
async def cosine(ctx, *, question):
    x = symbols('x')
    answer = cos(question)
    await ctx.send(f'Question: {question}\nAnswer: {answer}')

@client.command(aliases=['integrate'])
async def int(ctx, *, question):
    x = symbols('x')
    answer = integrate(question)
    await ctx.send(f'Question: {"Integrate " + question + " dx"}\nAnswer: {answer}')
@client.command(aliases=['solve'])
async def calc(ctx, question):
    answer = solve(question)
    await ctx.send(f'Question: {question}\n Answer: {answer}')





client.run('ITS A SECRET :D')


