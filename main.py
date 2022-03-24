import manual
from common import write_file, read_file
import json
from diceroller import roll_cmd

class Campaign:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Campaign: " + self.name

	def deserialize(self, json_obj):
		self.name = json_obj['name']

	def serialize(self):
		return json.dumps(self.__dict__)
	
	def save(self):
		write_file(self.name + ".json", serialize)

def create(cmd):
	if(len(cmd) < 2):
		object_name = input("What would you like to create: ")
	else:
		object_name = cmd[1]

	while(True):
		if object_name == "campaign":
			global campaign
			if('campaign' in locals()):
				campaign.save()
			
			name = "\n"
			while name == "\n":
				name = input("Name your new campaign: ")
			campaign = Campaign(name)

			print(str(campaign))
			
			break
		else:
			print("Cannot create:", object_name, "try again.")

def prompt_cmd():
	cmd = []
	while len(cmd) < 1:
		cmd = input("> ").lower().split(' ')
		while "" in cmd:
			cmd.remove("")

		if len(cmd) < 1:
			print("Please enter a command or enter help for help.")

	return cmd

if __name__ == "__main__":
	global campaign
	print("D&D ttrpg v1")
	cmd = prompt_cmd()

	if len(cmd) < 1:
		print("Please enter a command")
	
	while(cmd[0] != "quit" and cmd[0] != "q"):
		if cmd[0] == "help":
			manual.help()
		elif cmd[0] == "create":
			create(cmd)
		elif cmd[0] == "save":
			if('campaign' in locals()):
				campaign.save()
			else:
				print("Cannot save the campaign. There is no campaign loaded! Use 'create campaign' to make a campaign")
		elif cmd[0] == "load":
			json_serialization = json.loads(read_file(cmd[1] + ".json"))
			campaign = Campaign("")
			campaign.deserialize(json_serialization)
		elif cmd[0] == "info":
			if('campaign' in locals()):
				print(str(campaign))
			else:
				print("No campaign has been loaded. Create or load a campaign first!")
		elif cmd[0] == "roll":
			roll_cmd(cmd)
		else:
			print("Unknown command:", ' '.join(cmd))
		
		cmd = prompt_cmd()
	
	print("Quitting and saving state!")
	if('campaign' in locals()):
				campaign.save()

