import discord

class World():
   """A representation of a WoC world inside a server."""

   commands = {

   }

   def __init__(self, guild):
      self.guildID = guild.id
      self.name = guild.name
      self.prefix = "!"

      self.enabled = {command:True for command in self.commands.keys()}

      print(f"Creating a new world for {self.name} guild")

   def run(self, command):
      if command.content.startswith(self.prefix):
         comDiagram = command.content[len(self.prefix):].split()
         if comDiagram[0] in self.commands.keys():
            self.commands[comDiagram[0]]
