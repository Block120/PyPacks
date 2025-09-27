import pypacks

mcmeta = pypacks.Mcmeta(pack_format=81, description="An example datapack")

dp = pypacks.Datapack("example", mcmeta)

@dp.mcfunction("example:greet")
def greet():
    "Say 'Hello, World!' in the game chat."
    pypacks.say("Hello, World!")

dp.gen()
