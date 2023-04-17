# Dolan, Austin
# ICS 110P Assignment 12
# November 29 2022
# A program that displays multiple characters that could be warriors, mages, or rangers
# Characters can attack each other: fights will start with the character who attacks first getting the first attack
# Characters attack lvl will be compared with other characters defence lvl to determine effectiveness of attack
# RNG will be used to determine attack damage as well as style where-as warriors are 1.25 times effective against rangers
# Mages are 1.25 times effective against warriors and rangers are 1.25 times effective against mages
# A character will be defeated when their HP reaches 0

from time import sleep
import random

# Character Classes
class Warrior():
	def __init__(self, name, att_lvl, def_lvl, hp_lvl, style_lvl, has_weapon = False, has_armor = False, fav_monster = 'Troll', style = 'melee'):
		self.name = name
		self.att_lvl = att_lvl
		self.def_lvl = def_lvl
		self.hp_lvl = hp_lvl
		self.style_lvl = style_lvl
		self.fav_monster = fav_monster
		self.style = style
		self.has_weapon = has_weapon
		self.has_armor = has_armor	

	def __str__(self):
		print_stats = '\n\n *** Warrior Stats *** '
		print_stats += '\nCharacter Name: ' + (self.name).capitalize()
		print_stats += '\nAttack Level: ' + str(self.att_lvl)
		print_stats += '\nDefence Levle: ' + str(self.def_lvl)
		print_stats += '\nHealth Points: ' + str(self.hp_lvl)
		print_stats += '\nStrength Level: ' + str(self.style_lvl)
		print_stats += '\nHas Weapon: ' + str(self.has_weapon)
		print_stats += '\nHas Armor: ' + str(self.has_armor)		
		print_stats += '\nFavorite Monster: ' + (self.fav_monster)
		print_stats += '\nCharacter Style: ' + str(self.style).capitalize()
		return print_stats

	# Displays monster that player is most effective against	
	def display_fav_monster(self):
		print(f'\n{self.name} says:\nI am a Warrior and I use the {self.style} style, so my favorite monster to attack is the {self.fav_monster}')

	# Armor and Weapon functions: If equiped will add 20 points to respective attribute
	def equip_armor(self):
		if self.has_armor:
			print(f'\n{self.name} says:\nI recently acquired Masterwork Armor, seems like a good time to put it on.\n{self.name} equips Masterwork armor!')
			armor_bonus = 20
		else:
			print(f'\n{self.name} says:\nI have no armor to equip!')
			armor_bonus = 0
		return armor_bonus

	def equip_weapon(self):
		if self.has_weapon:
			print(f'\n{self.name} says:\nMy Zaros Godsword would probably help me with this fight.\n{self.name} equips the Zaros Godsword!')
			weapon_bonus = 20
		else:
			print(f'\n{self.name} says:\nI have no weapon to equip!')
			weapon_bonus = 0
		return weapon_bonus

class Mage:
	def __init__(self, name, att_lvl, def_lvl, hp_lvl, style_lvl, has_weapon = False, has_armor = False, fav_monster = 'Orc', style = 'magic'):
		self.name = name
		self.att_lvl = att_lvl
		self.def_lvl = def_lvl
		self.hp_lvl = hp_lvl
		self.style_lvl = style_lvl
		self.fav_monster = fav_monster
		self.style = style
		self.has_weapon = has_weapon
		self.has_armor = has_armor

	def __str__(self):
		print_stats = '\n\n *** Mage Stats *** '
		print_stats += '\nCharacter Name: ' + (self.name).capitalize()
		print_stats += '\nAttack Level: ' + str(self.att_lvl)
		print_stats += '\nDefence Levle: ' + str(self.def_lvl)
		print_stats += '\nHealth Points: ' + str(self.hp_lvl)
		print_stats += '\nMagic Level: ' + str(self.style_lvl)
		print_stats += '\nHas Weapon: ' + str(self.has_weapon)
		print_stats += '\nHas Armor: ' + str(self.has_armor)		
		print_stats += '\nFavorite Monster: ' + (self.fav_monster)		
		print_stats += '\nCharacter Style: ' + str(self.style).capitalize()
		return print_stats

	# Displays monster that player is most effective against
	def display_fav_monster(self):
		print(f'\n{self.name} says: \nI am a Mage and I use the {self.style} style, so my favorite monster to attack is the {self.fav_monster}')

	# Armor and Weapon functions: If equiped will add 20 points to respective attribute
	def equip_armor(self):
		if self.has_armor:
			print(f'\n{self.name} says:\nI recently acquired Elite Tectonic Armor, seems like a good time to put it on.\n{self.name} equips Elite Tectonic Armor!')
			armor_bonus = 20
		else:
			print(f'\n{self.name} says:\nI have no armor to equip!')
			armor_bonus = 0
		return armor_bonus

	def equip_weapon(self):
		if self.has_weapon:
			print(f'\nMy Fractured Staff of Armadyl would probably help me with this fight.\n{self.name} equips the Fractured Staff of Armadyl!')
			weapon_bonus = 20
		else:
			print(f'\n{self.name} says:\nI have no weapon to equip!')
			weapon_bonus = 0
		return weapon_bonus					

class Ranger:
	def __init__(self, name, att_lvl, def_lvl, hp_lvl, style_lvl, has_weapon = False, has_armor = False, fav_monster = 'Goblin', style = 'range'):
		self.name = name
		self.att_lvl = att_lvl
		self.def_lvl = def_lvl
		self.hp_lvl = hp_lvl
		self.style_lvl = style_lvl
		self.fav_monster = fav_monster
		self.style = style
		self.has_weapon = has_weapon
		self.has_armor = has_armor

	def __str__(self):
		print_stats = '\n\n *** Ranger Stats *** '
		print_stats += '\nCharacter Name: ' + (self.name).capitalize()
		print_stats += '\nAttack Level: ' + str(self.att_lvl)
		print_stats += '\nDefence Levle: ' + str(self.def_lvl)
		print_stats += '\nHealth Points: ' + str(self.hp_lvl)
		print_stats += '\nRange Level: ' + str(self.style_lvl)
		print_stats += '\nHas Weapon: ' + str(self.has_weapon)
		print_stats += '\nHas Armor: ' + str(self.has_armor)		
		print_stats += '\nFavorite Monster: ' + (self.fav_monster)	
		print_stats += '\nCharacter Style: ' + str(self.style).capitalize()
		return print_stats

	# Displays monster that player is most effective against
	def display_fav_monster(self):
		print(f'\n{self.name} says:\nI am a Ranger and I use the {self.style} style, so my favorite monster to attack is the {self.fav_monster}')

	# Armor and Weapon functions: If equiped will add 20 points to respective attribute
	def equip_armor(self):
		if self.has_armor:
			print(f'\n{self.name} says:\nI recently acquired Elite Sirenic Armour, seems like a good time to put it on.\n{self.name} equips Elite Sirenic Armour!')
			armor_bonus = 20
		else:
			print(f'\n{self.name} says:\nI have no armor to equip!')
			armor_bonus = 0
		return armor_bonus

	def equip_weapon(self):
		if self.has_weapon:
			print(f'\n{self.name} says:\nMy Eldritch Crossbow would probably help me with this fight.\n{self.name} equips the Eldritch Crossbow!')
			weapon_bonus = 20
		else:
			print(f'\n{self.name} says:\nI have no weapon to equip!')
			weapon_bonus = 0
		return weapon_bonus

# Monster Class

class Monster:
	def __init__(self, mon_breed, mon_att_lvl, mon_def_lvl, mon_hp_lvl, mon_style):
		self.mon_breed = mon_breed
		self.mon_att_lvl = mon_att_lvl
		self.mon_def_lvl = mon_def_lvl
		self.mon_hp_lvl = mon_hp_lvl
		self.mon_style = mon_style		

	def __str__(self):
		print_stats = '\n\n *** Monster Stats *** '
		print_stats += '\nMonster Breed: ' + (self.mon_breed)
		print_stats += '\nAttack Level: ' + str(self.mon_att_lvl)
		print_stats += '\nDefence Level: ' + str(self.mon_def_lvl)
		print_stats += '\nHealth Points: ' + str(self.mon_hp_lvl)
		print_stats += '\nMonster Style: ' + str(self.mon_style).capitalize()
		return print_stats	

# Function that determines damage_done to monster by player1: Affected by player1 style and difference in attribute values
def damage_monster(player1, opponent):
	dmg_monster = 0
	dmg_multiplier = random.random() + 1
	if getattr(player1, 'att_lvl') > getattr(opponent, 'mon_def_lvl'):
		dmg_monster = ((((getattr(player1, 'att_lvl') + getattr(player1, 'style_lvl')) / 2) - getattr(opponent, 'mon_def_lvl')) + 4)
	elif getattr(player1, 'att_lvl') < getattr(opponent, 'mon_def_lvl'):
		dmg_diff = getattr(opponent, 'mon_def_lvl') - getattr(player1, 'att_lvl')
		dmg_monster = (25 + dmg_diff) * (1 / dmg_diff) * random.randint(0,1)
	else:
		dmg_monster = random.randint(5,15)
	if (getattr(player1, 'style') == 'melee' and getattr(opponent, 'mon_style') == 'magic') or (getattr(player1, 'style') == 'range' and getattr(opponent, 'mon_style') == 'melee') or (getattr(player1, 'style') == 'magic' and getattr(opponent, 'mon_style') == 'range'):
		damage_done = int((dmg_multiplier * dmg_monster) * .8)
	elif (getattr(player1, 'style') == 'melee' and getattr(opponent, 'mon_style') == 'range') or (getattr(player1, 'style') == 'magic' and getattr(opponent, 'mon_style') == 'melee') or (getattr(player1, 'style') == 'range' and getattr(opponent, 'mon_style') == 'magic'):
		damage_done = int((dmg_multiplier * dmg_monster) * 1.25)
	else:
		damage_done = int(dmg_multiplier * dmg_monster)
	return damage_done

# Function that determines damage_done to player1 by monster: Affected by monster style and difference in attribute values
def damage_player(opponent, player1):
	dmg_player = 0
	dmg_multiplier = random.random() + 1
	if getattr(opponent, 'mon_att_lvl') < getattr(player1, 'def_lvl'):
		dmg_diff = getattr(player1, 'def_lvl') - getattr(opponent, 'mon_att_lvl')
		dmg_player = (25 + dmg_diff) * (1 / dmg_diff) * random.randint(0,1)
	elif getattr(opponent, 'mon_att_lvl') > getattr(player1, 'def_lvl'):
		dmg_player = ((getattr(opponent, 'mon_att_lvl') - getattr(player1, 'def_lvl')) + 4)
	else:
		dmg_player = random.randint(5,15)
	if (getattr(opponent, 'mon_style') == 'magic' and getattr(player1, 'style') == 'melee') or (getattr(opponent, 'mon_style') == 'melee' and getattr(player1, 'style') == 'range') or (getattr(opponent, 'mon_style') == 'range' and getattr(player1, 'style') == 'magic'):
		damage_done = int((dmg_multiplier * dmg_player) * 1.25)
	elif (getattr(opponent, 'mon_style') == 'melee' and getattr(player1, 'style') == 'magic') or (getattr(opponent, 'mon_style') == 'range' and getattr(player1, 'style') == 'melee') or (getattr(opponent, 'mon_style') == 'magic' and getattr(player1, 'style') == 'range'):
		damage_done = int((dmg_multiplier * dmg_player) * .8)
	else:
		damage_done = int(dmg_multiplier * dmg_player)
	return damage_done

# Function to determine outcome of battle: When one of the fighters HP hits 0 battle_continues set to False and battle ends
def player_vs_monster(player1, opponent):
	damage = damage_monster(player1, opponent)
	print(f"\n{getattr(player1, 'name')} hits the {getattr(opponent, 'mon_breed')} for {damage} damage!")
	mon_hp_remaining = int(getattr(opponent, 'mon_hp_lvl')) - damage
	setattr(opponent, 'mon_hp_lvl', mon_hp_remaining)
	if int(getattr(opponent, 'mon_hp_lvl')) <= 0:
		battle_continues = False
	else:
		print(f"The {getattr(opponent, 'mon_breed')} has {getattr(opponent, 'mon_hp_lvl')} HP remaining.")
		sleep(.6)
		battle_continues = True
	if battle_continues:
		damage = damage_player(opponent, player1)
		print(f"\n{getattr(opponent, 'mon_breed')} hits {getattr(player1, 'name')} for {damage} damage!")
		player_hp_remaining = int(getattr(player1, 'hp_lvl')) - damage
		setattr(player1, 'hp_lvl', player_hp_remaining)
		if int(getattr(player1, 'hp_lvl')) <= 0:
			print(f"{getattr(player1, 'name')} was defeated by the {getattr(opponent, 'mon_breed')}")
			battle_continues = False
		else:
			print(f"{getattr(player1, 'name')} has {getattr(player1, 'hp_lvl')} HP remaining.")
			sleep(.6)
			battle_continues = True
	else:
		print(f"The {getattr(opponent, 'mon_breed')} was defeated by {getattr(player1,'name')}")
		battle_continues = False
	return battle_continues

def main():
	# Variables
	play = 'yes'
	player1 = ''
	opponent = ''

	# Warriors attributes: name, att_lvl, def_lvl, hp_lvl, style_lvl, has_weapon = False, has_armor = False, fav_monster = 'Troll', style = 'melee'
	warrior1 = Warrior('Austin', random.randint(75,99), random.randint(75,99), random.randint(75,99), random.randint(75,99))
	warrior2 = Warrior('Edward', random.randint(60,85), random.randint(60,85), random.randint(75,99), random.randint(75,99), True, True)

	# Mages attributes: name, att_lvl, def_lvl, hp_lvl, style_lvl, has_weapon = False, has_armor = False, fav_monster = 'Orc', style = 'magic
	mage1 = Mage('Mary', random.randint(75,99), random.randint(75,99), random.randint(75,99), random.randint(75,99))
	mage2 = Mage('Destiny', random.randint(60,85), random.randint(60,85), random.randint(75,99), random.randint(75,99), True, True)

	# Rangers attributes: name, att_lvl, def_lvl, hp_lvl, style_lvl, has_weapon = False, has_armor = False, fav_monster = 'Goblin', style = 'range'
	ranger1 = Ranger('Mike', random.randint(75,99), random.randint(75,99), random.randint(75,99), random.randint(75,99))
	ranger2 = Ranger('Rob', random.randint(60,85), random.randint(60,85), random.randint(75,99), random.randint(75,99), True, True)

	# Monsters attributes: mon_breed, mon_att_lvl, mon_def_lvl, mon_hp_lvl, mon_style
	goblin = Monster('Goblin', random.randint(75,99), random.randint(75,99), random.randint(75,99), 'magic')
	orc = Monster('Orc', random.randint(75,99), random.randint(75,99), random.randint(75,99), 'melee')
	troll = Monster('Troll', random.randint(75,99), random.randint(75,99), random.randint(75,99), 'range')

	# Display Characters and Monsters available
	print('\n***Characters***')
	print(warrior1)
	print(warrior2)
	print(mage1)
	print(mage2)
	print(ranger1)
	print(ranger2)
	print('\n***Monsters***')
	print(goblin)
	print(orc)
	print(troll)

	# Begin game loop
	play = input('\nWould you like to play? (yes or no) ').lower()
	while play != 'no':
		if play == 'yes':
			print('\nMy game is a battle game where you select a player and a monster to fight.\n\nEach player has a style like Melee, Magic, or Range.\n\nMagic is more effective against Melee, Melee is more effective against Range, and Range is more effective against Magic.\n\nThe character you choose strikes first and the battle ends when either you or the monster\'s HP reaches 0.\n\nHave fun!')
			
			while player1 != 'Austin' and player1 != 'Edward' and player1 != 'Mary' and player1 != 'Destiny' and player1 != 'Mike' and player1 != 'Rob':
				# Character Selection and player1 assignment
				player1 = input('\nSelect a character: (Austin, Edward, Mary, Destiny, Mike, or Rob) ').capitalize()

			
			if player1 == 'Austin':
				player1 = warrior1
			elif player1 == 'Edward':
				player1 = warrior2
			elif player1 == 'Mary':
				player1 = mage1
			elif player1 == 'Destiny':
				player1 = mage2
			elif player1 == 'Mike':
				player1 = ranger1
			else:
				player1 = ranger2

			
			# Variables for Attack and Defence before equiping armor and weapon: Reset data after fight
			starting_p1_att = getattr(player1, 'att_lvl')
			starting_p1_def = getattr(player1, 'def_lvl')
			starting_p1_style_lvl = getattr(player1, 'style_lvl')

			# Var for HP stats at the beginning of the fight
			starting_p1_hp = getattr(player1, 'hp_lvl')
			
			# If wearing armor and weapon equip now and up stats
			armor_bonus = player1.equip_armor()
			setattr(player1, 'def_lvl', getattr(player1, 'def_lvl') + armor_bonus)
			weapon_bonus = player1.equip_weapon()
			setattr(player1, 'att_lvl', getattr(player1, 'att_lvl') + weapon_bonus)
			setattr(player1, 'style_lvl', getattr(player1, 'style_lvl') + weapon_bonus)
			print(player1)

			# Most desirable monster to fight based on effectiveness
			print('\nNow the character you choose will tell you their favorite type of monster to battle!\n(hint: Their attacks are more effective against this type of monster!)')
			player1.display_fav_monster()

			# Choose monster to fight
			while opponent != 'Goblin' and opponent != 'Orc' and opponent != 'Troll':
				opponent = input('\nSelect an monster to attack: (Goblin, Orc, or Troll) ').capitalize()	

			if opponent == 'Goblin': 
				opponent = goblin
			elif opponent == 'Orc':
				opponent = orc
			else:
				opponent = troll	

			# Starting HP of Monster: Reset data after fight
			starting_mon_hp = getattr(opponent, 'mon_hp_lvl')

			print(opponent)
			sleep(2)
			print('\n\n***Fight!***')

			
			# Reset battle_continues Begin Battle player_vs_monster()
			battle_continues = True
			while battle_continues:
				battle_continues = player_vs_monster(player1, opponent)

			# Reset player1 and opponent HP stats
			setattr(player1, 'hp_lvl', starting_p1_hp)
			setattr(opponent, 'mon_hp_lvl', starting_mon_hp)
			
			# Reset att_lvl, def_lvl, and style_lvl stats
			setattr(player1, 'att_lvl', starting_p1_att)
			setattr(player1, 'def_lvl', starting_p1_def)
			setattr(player1, 'style_lvl', starting_p1_style_lvl)

			# Prompt user to play again	
			play = input('\nPlay again?(yes or no) ')
		# If user doesn't enter yes or no prompt them to enter yes or no again
		else:
			play = input('That\'s not one of my response options.\nWould you like to play? (yes or no) ')
	print('Goodbye!')

main()
