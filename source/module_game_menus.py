# -*- coding: utf-8 -*-
from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [

	("start_game_0", menu_text_color(0xff000000), "Welcome to the Mount and Blade: Warband mod - Anno Domini 1257. This mod attempts to reflect the reality of 13th century Europe. Before starting your game you need to choose the recruitment type for your game. Choose wisely, as you will not be able to change it after you start the game!",
"none",
	[],
	[
		("continue_feudal",
		[],
		"Start a new game, with the lance recruitment system",
		[
			(assign, "$use_feudal_lance", 1),
			(jump_to_menu, "mnu_start_game_1")
		], "."),

		("continue",
		[],
		"Start a new game, with the native Warband recruitment system",
		[
			(assign, "$use_feudal_lance", 0),
			(jump_to_menu, "mnu_start_game_1")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("start_phase_2", 0, "You hear about Europe, a land torn between rival kingdoms battling each other for supremacy, a haven for knights and mercenaries, cutthroats and adventurers, all willing to risk their lives in pursuit of fortune, power, or glory... In this land which holds great dangers and even greater opportunities, you believe you may leave your past behind and start a new life. You feel that finally, you hold the key of your destiny in your hands, free to choose as you will, and that whatever course you take, great adventures will await you. Drawn by the stories you hear about Europe and its kingdoms, you...",
"none",
	[],
	[
		("town_quest",
		[
			(eq, "$current_startup_quest_phase", 0)
		],
		"join a merchant caravan to travel to your destination.",
		[
			(try_begin),
				(eq, "$g_start_faction", "fac_kingdom_1"),
				(assign, "$current_town", "p_town_1_1"),
			(else_try),
				(this_or_next|eq, "$g_start_faction", "fac_kingdom_2"),
				(eq, "$g_start_faction", "fac_kingdom_2"),
				(assign, "$current_town", "p_town_2_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_3"),
				(assign, "$current_town", "p_town_3_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_4"),
				(assign, "$current_town", "p_town_4_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_5"),
				(assign, "$current_town", "p_town_5_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_6"),
				(assign, "$current_town", "p_town_6_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_7"),
				(assign, "$current_town", "p_town_7_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_8"),
				(assign, "$current_town", "p_town_8_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_9"),
				(assign, "$current_town", "p_town_9_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_10"),
				(assign, "$current_town", "p_town_10_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_11"),
				(assign, "$current_town", "p_town_11_2"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_12"),
				(assign, "$current_town", "p_town_12_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_13"),
				(assign, "$current_town", "p_town_13_2"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_14"),
				(assign, "$current_town", "p_town_14_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_15"),
				(assign, "$current_town", "p_town_15_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_16"),
				(assign, "$current_town", "p_town_16_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_17"),
				(assign, "$current_town", "p_town_17_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_18"),
				(assign, "$current_town", "p_town_18_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_19"),
				(assign, "$current_town", "p_town_19_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_20"),
				(assign, "$current_town", "p_town_20_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_papacy"),
				(assign, "$current_town", "p_town_21_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_22"),
				(assign, "$current_town", "p_town_22_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_23"),
				(assign, "$current_town", "p_town_23_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_24"),
				(assign, "$current_town", "p_town_24_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_25"),
				(assign, "$current_town", "p_town_25_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_26"),
				(assign, "$current_town", "p_town_26_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_27"),
				(assign, "$current_town", "p_town_27_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_28"),
				(assign, "$current_town", "p_town_28_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_29"),
				(assign, "$current_town", "p_town_29_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_30"),
				(assign, "$current_town", "p_town_30_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_31"),
				(assign, "$current_town", "p_town_31_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_32"),
				(assign, "$current_town", "p_town_32_1"),
			(else_try),
				(this_or_next|eq, "$g_start_faction", "fac_kingdom_34"),
				(this_or_next|eq, "$g_start_faction", "fac_kingdom_35"),
				(this_or_next|eq, "$g_start_faction", "fac_kingdom_36"),
				(eq, "$g_start_faction", "fac_kingdom_33"),
				(assign, "$current_town", "p_town_2_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_37"),
				(assign, "$current_town", "p_town_37_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_38"),
				(assign, "$current_town", "p_town_38_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_39"),
				(assign, "$current_town", "p_town_39_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_40"),
				(assign, "$current_town", "p_town_40_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_41"),
				(assign, "$current_town", "p_town_41_1"),
			(else_try),
				(eq, "$g_start_faction", "fac_kingdom_42"),
				(assign, "$current_town", "p_town_42_1"),
			(else_try),
				(store_random_in_range, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(try_end),
			(assign, "$g_starting_town", "$current_town"),
			(jump_to_menu, "mnu_start_phase_2_5")
		], "."),

		("tutorial_cheat",
		[
			(eq, "$quickstart", 1)
		],
		"{!}CHEAT! (Quickstart)",
		[
			(assign, "$cheat_mode", 1),
			(change_screen_map),
			(set_show_messages, 0),
			(troop_raise_skill, "trp_player", 1, 10),
			(party_add_members, "p_main_party", "trp_mamluke_heavy_horse_archer", 100),
			(party_add_members, "p_main_party", "trp_cuman_horse_archer", 60),
			(troop_add_gold, "trp_player", 300000),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(set_show_messages, 1),
			(try_for_range, ":scene", "scn_town_arab_center", "scn_castle_walls_euro"),
				(scene_set_slot, ":scene", slot_scene_visited, 1),
			(try_end),
			(call_script, "script_get_player_party_morale_values"),
			(party_set_morale, "p_main_party", reg0)
		], ".")
	]
	),

	("start_game_3", 0, "Choose your scenario:",
"none",
	[
		(assign, "$g_custom_battle_scenario", 0),
		(assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario")
	],
	[
		("go_back",
		[],
		"Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("tutorial", 0, "You approach a field where the locals are training with weapons. You can practice here to improve your combat skills.",
"none",
	[
		(try_begin),
			(eq, "$g_tutorial_entered", 1),
			(change_screen_quit),
		(else_try),
			(set_passage_menu, "mnu_tutorial"),
			(assign, "$g_tutorial_entered", 1),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(modify_visitors_at_site, "scn_tutorial_training_ground"),
			(reset_visitors, 0),
			(set_player_troop, "trp_player"),
			(assign, "$g_player_troop", "trp_player"),
			(troop_raise_attribute, "$g_player_troop", 0, 12),
			(troop_raise_attribute, "$g_player_troop", 1, 9),
			(troop_raise_attribute, "$g_player_troop", 3, 5),
			(troop_raise_skill, "$g_player_troop", 26, 3),
			(troop_raise_skill, "$g_player_troop", 25, 2),
			(troop_raise_skill, "$g_player_troop", 24, 3),
			(troop_raise_skill, "$g_player_troop", 35, 1),
			(troop_raise_skill, "$g_player_troop", 33, 5),
			(troop_raise_skill, "$g_player_troop", 27, 4),
			(troop_raise_skill, "$g_player_troop", 36, 1),
			(troop_raise_skill, "$g_player_troop", 23, 6),
			(troop_raise_proficiency_linear, "$g_player_troop", 0, 70),
			(troop_raise_proficiency_linear, "$g_player_troop", 1, 70),
			(troop_raise_proficiency_linear, "$g_player_troop", 2, 70),
			(troop_raise_proficiency_linear, "$g_player_troop", 4, 70),
			(troop_raise_proficiency_linear, "$g_player_troop", 5, 70),
			(troop_clear_inventory, "$g_player_troop"),
			(troop_add_item, "$g_player_troop", "itm_leather_jerkin", 0),
			(troop_add_item, "$g_player_troop", "itm_leather_boots", 0),
			(troop_add_item, "$g_player_troop", "itm_practice_sword", 0),
			(troop_add_item, "$g_player_troop", "itm_quarter_staff", 0),
			(troop_equip_items, "$g_player_troop"),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 32, "trp_tutorial_fighter_1"),
			(set_visitor, 33, "trp_tutorial_fighter_2"),
			(set_visitor, 34, "trp_tutorial_fighter_3"),
			(set_visitor, 35, "trp_tutorial_fighter_4"),
			(set_visitor, 40, "trp_tutorial_master_archer"),
			(set_visitor, 41, "trp_tutorial_archer_1"),
			(set_visitor, 42, "trp_tutorial_archer_1"),
			(set_visitor, 60, "trp_tutorial_master_horseman"),
			(set_visitor, 61, "trp_tutorial_rider_1"),
			(set_visitor, 62, "trp_tutorial_rider_1"),
			(set_visitor, 63, "trp_tutorial_rider_2"),
			(set_visitor, 64, "trp_tutorial_rider_2"),
			(set_jump_mission, "mt_tutorial_training_ground"),
			(jump_to_scene, "scn_tutorial_training_ground"),
			(change_screen_mission)
		], "."),

		("choose_scene",
		[],
		"Scene Chooser",
		[
			(jump_to_menu, "mnu_choose_scenes_0")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("reports", 0, "Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
"none",
	[
		(call_script, "script_game_get_party_companion_limit"),
		(assign, ":var_1", reg0),
		(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		(assign, reg5, ":player_renown"),
		(assign, reg6, "$player_honor"),
		(assign, reg7, ":var_1"),
		(party_get_morale, reg8, "p_main_party")
	],
	[
		("cheat_faction_orders",
		[
			(ge, "$cheat_mode", 1)
		],
		"{!}Cheat: Faction orders.",
		[
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("view_character_report",
		[],
		"View character report.",
		[
			(jump_to_menu, "mnu_character_report")
		], "."),

		("view_party_size_report",
		[],
		"View party size report.",
		[
			(jump_to_menu, "mnu_party_size_report")
		], "."),

		("view_npc_mission_report",
		[],
		"View companion mission report.",
		[
			(jump_to_menu, "mnu_companion_report")
		], "."),

		("view_weekly_budget_report",
		[],
		"View weekly budget report.",
		[
			(assign, "$g_apply_budget_report_to_gold", 0),
			(start_presentation, "prsnt_budget_report")
		], "."),

		("view_morale_report",
		[],
		"View party morale report.",
		[
			(jump_to_menu, "mnu_morale_report")
		], "."),

		("lord_relations",
		[],
		"View list of known lords by relation.",
		[
			(jump_to_menu, "mnu_lord_relations")
		], "."),

		("courtship_relations",
		[],
		"View courtship relations.",
		[
			(jump_to_menu, "mnu_courtship_relations")
		], "."),

		("status_check",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}NPC status check.",
		[
			(try_for_range, ":troop", "trp_npc1", "trp_kingdom_1_lord"),
				(main_party_has_troop, ":troop"),
				(str_store_troop_name, 4, ":troop"),
				(troop_get_slot, reg3, ":troop", slot_troop_morality_state),
				(troop_get_slot, reg4, ":troop", slot_troop_2ary_morality_state),
				(troop_get_slot, reg5, ":troop", slot_troop_personalityclash_state),
				(troop_get_slot, reg6, ":troop", slot_troop_personalityclash2_state),
				(troop_get_slot, reg7, ":troop", slot_troop_personalitymatch_state),
				(display_message, "@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
			(try_end)
		], "."),

		("view_faction_relations_report",
		[],
		"View faction relations report.",
		[
			(jump_to_menu, "mnu_faction_relations_report")
		], "."),

		("resume_travelling",
		[],
		"Resume travelling.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("custom_battle_scene", menu_text_color(0xff000000), "(NO TRANS)",
"none",
	[],
	[
		("quick_battle_scene_1",
		[],
		"{!}quick battle scene 1",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_1"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_2",
		[],
		"{!}quick battle scene 2",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_2"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_3",
		[],
		"{!}quick battle scene 3",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_3"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_4",
		[],
		"{!}quick battle scene 4",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_4"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_5",
		[],
		"{!}quick battle scene 5",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_5"),
			(change_screen_mission)
		], "."),

		("go_back",
		[],
		"{!}Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("custom_battle_end", 0, "The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} men in the fighting.",
"none",
	[
		(music_set_situation, 0),
		(assign, reg5, "$g_custom_battle_team2_death_count"),
		(assign, reg6, "$g_custom_battle_team1_death_count"),
		(get_player_agent_kill_count, ":player_agent_kill_count"),
		(get_player_agent_kill_count, ":player_agent_kill_count_1", 1),
		(store_add, reg7, ":player_agent_kill_count", ":player_agent_kill_count_1"),
		(try_begin),
			(eq, "$g_battle_result", 1),
			(str_store_string, 1, "str_battle_won"),
		(else_try),
			(str_store_string, 1, "str_battle_lost"),
		(try_end),
		(try_begin),
			(ge, "$g_custom_battle_team2_death_count", 100),
			(unlock_achievement, 4),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue.",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("start_game_1", menu_text_color(0xff000000), "Select your character's gender.",
"none",
	[
		(try_begin),
			(eq, "$culture_pool_initialized", 0),
			(call_script, "script_initialize_culture_pools"),
			(assign, "$culture_pool_initialized", 1),
		(try_end),
		(try_begin),
			(eq, "$culture_pool", 0),
			(assign, "$culture_pool", 1),
			(call_script, "script_rebalance_troops_by_culture"),
		(try_end)
	],
	[
		("start_male",
		[],
		"Male",
		[
			(troop_set_type, "trp_player", 0),
			(assign, "$character_gender", 0),
			(try_begin),
				(eq, "$quickstart", 0),
				(jump_to_menu, "mnu_start_character_1"),
			(else_try),
				(jump_to_menu, "mnu_start_phase_2"),
			(try_end)
		], "."),

		("start_female",
		[],
		"Female",
		[
			(troop_set_type, "trp_player", 1),
			(assign, "$character_gender", 1),
			(try_begin),
				(eq, "$quickstart", 0),
				(jump_to_menu, "mnu_start_character_1"),
			(else_try),
				(jump_to_menu, "mnu_start_phase_2"),
			(try_end)
		], "."),

		("enable_quickstart",
		[
			(eq, "$quickstart", 0),
			(eq, 0, 1)
		],
		"Enable quickstart (this is useful for debugging only)",
		[
			(assign, "$quickstart", 1),
			(jump_to_menu, "mnu_start_game_1")
		], "."),

		("disable_quickstart",
		[
			(gt, "$quickstart", 0)
		],
		"Disable quickstart (this is useful for debugging only)",
		[
			(assign, "$quickstart", 0),
			(jump_to_menu, "mnu_start_game_1")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "mnu_start_game_0")
		], ".")
	]
	),

	("start_character_1", 0, "You were born years ago, in a land far away. Your father was...",
"none",
	[
		(str_clear, 10),
		(str_clear, 11),
		(str_clear, 12),
		(str_clear, 13),
		(str_clear, 14),
		(str_clear, 15)
	],
	[
		("start_noble",
		[],
		"An impoverished noble.",
		[
			(assign, "$background_type", 1),
			(assign, reg3, "$character_gender"),
			(str_store_string, 10, "@You came into the world a {reg3?daughter:son} of declining nobility, owning only the house in which they lived. However, despite your family's hardships, they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
			(jump_to_menu, "mnu_start_character_2")
		], "."),

		("start_merchant",
		[],
		"A travelling merchant.",
		[
			(assign, "$background_type", 2),
			(assign, reg3, "$character_gender"),
			(str_store_string, 10, "@You were born the {reg3?daughter:son} of travelling merchants, always moving from place to place in search of a profit. Although your parents were wealthier than most and educated you as well as they could, you found little opportunity to make friends on the road, living mostly for the moments when you could sell something to somebody."),
			(jump_to_menu, "mnu_start_character_2")
		], "."),

		("start_guard",
		[],
		"A veteran warrior.",
		[
			(assign, "$background_type", 3),
			(assign, reg3, "$character_gender"),
			(str_store_string, 10, "@As a child, your family scrabbled out a meagre living from your father's wages as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
			(jump_to_menu, "mnu_start_character_2")
		], "."),

		("start_forester",
		[],
		"A hunter.",
		[
			(assign, "$background_type", 4),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@{reg3?daughter:son}"),
			(str_store_string, 10, "@You were the {reg3?daughter:son} of a family who lived off the woods, doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows, even a spot of poaching whenever things got tight. Winter was never a good time for your family as the cold took animals and people alike, but you always lived to see another dawn, though your brothers and sisters might not be so fortunate."),
			(jump_to_menu, "mnu_start_character_2")
		], "."),

		("start_nomad",
		[],
		"A steppe nomad.",
		[
			(assign, "$background_type", 5),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@{reg3?daughter:son}"),
			(str_store_string, 10, "@You were a child of the steppe, born to a tribe of wandering nomads who lived in great camps throughout the arid grasslands. Like the other tribesmen, your family revered horses above almost everything else, and they taught you how to ride almost before you learned how to walk. "),
			(jump_to_menu, "mnu_start_character_2")
		], "."),

		("start_thief",
		[],
		"A thief.",
		[
			(assign, "$background_type", 6),
			(assign, reg3, "$character_gender"),
			(str_store_string, 10, "@As the {reg3?daughter:son} of a thief, you had very little 'formal' education. Instead you were out on the street, begging until you learned how to cut purses, cutting purses until you learned how to pick locks, all the way through your childhood. Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
			(jump_to_menu, "mnu_start_character_2")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "mnu_start_game_1")
		], ".")
	]
	),

	("start_character_2", 0, "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
"none",
	[],
	[
		("page",
		[],
		"A page at a nobleman's court.",
		[
			(assign, "$background_answer_2", 0),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@As a {reg3?girl:boy} growing out of childhood, you were sent to live in the court of one of the nobles of the land. There, your first lessons were in humility, as you waited upon the lords and ladies of the household. But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
			(jump_to_menu, "mnu_start_character_3")
		], "."),

		("apprentice",
		[],
		"A craftsman's apprentice.",
		[
			(assign, "$background_answer_2", 1),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@As a {reg3?girl:boy} growing out of childhood, you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as you wished to stay."),
			(jump_to_menu, "mnu_start_character_3")
		], "."),

		("stockboy",
		[],
		"A shop assistant.",
		[
			(assign, "$background_answer_2", 4),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@As a {reg3?girl:boy} growing out of childhood, you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans. You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd got the better deal."),
			(jump_to_menu, "mnu_start_character_3")
		], "."),

		("urchin",
		[],
		"A street urchin.",
		[
			(assign, "$background_answer_2", 2),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@As a {reg3?girl:boy} growing out of childhood, you took to the streets, doing whatever you must to survive. Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world, always one step ahead of the law and those who wished you ill."),
			(jump_to_menu, "mnu_start_character_3")
		], "."),

		("nomad",
		[],
		"A steppe child.",
		[
			(assign, "$background_answer_2", 3),
			(assign, reg3, "$character_gender"),
			(str_store_string, 11, "@As a {reg3?girl:boy} growing out of childhood, you rode the great steppes on a horse of your own, learning the ways of the grass and the desert. Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country. Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
			(jump_to_menu, "mnu_start_character_3")
		], "."),

		("go_back",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_start_character_1")
		], ".")
	]
	),

	("start_character_3", 0, "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
"none",
	[
		(assign, reg3, "$character_gender")
	],
	[
		("squire",
		[
			(eq, "$character_gender", 0)
		],
		"A squire.",
		[
			(assign, "$background_answer_3", 8),
			(str_store_string, 14, "@{reg3?daughter:man}"),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you. When you were named squire to a noble at court, you practiced long hours with weapons, learning how to deal out hard knocks and how to take them, too. You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals. But in addition to learning the chivalric ideal, you also learned about the less uplifting side -- old warriors' stories of ruthless power politics, of betrayals and usurpations, of men who used guile as well as valor to achieve their aims."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("lady",
		[
			(eq, "$character_gender", 1)
		],
		"A lady-in-waiting.",
		[
			(assign, "$background_answer_3", 9),
			(str_store_string, 14, "@{reg3?daughter:man}"),
			(str_store_string, 13, "@{reg3?woman:man}"),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things, the wives and mistresses of noble men as well as maidens who had yet to find a husband. However, even here you found politics at work as the ladies schemed for prominence and fought each other bitterly to catch the eye of whatever unmarried man was in fashion at court. You soon learned ways of turning these situations and goings-on to your advantage. With it came the realisation that you yourself could wield great influence in the world, if only you applied yourself with a little bit of subtlety."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("troubadour",
		[],
		"A troubadour.",
		[
			(assign, "$background_answer_3", 7),
			(str_store_string, 14, "@{reg3?daughter:man}"),
			(str_store_string, 13, "@{reg3?woman:man}"),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You set out on your own with nothing except the instrument slung over your back and your own voice. It was a poor existence, with many a hungry night when people failed to appreciate your play, but you managed to survive on your music alone. As the years went by you became adept at playing the drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("student",
		[],
		"A university student.",
		[
			(assign, "$background_answer_3", 10),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you. You found yourself as a student in the university of one of the great cities, where you studied theology, philosophy, and medicine. But not all your lessons were learned in the lecture halls. You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight. However, you certainly were able to observe how a broken jaw is set, or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("peddler",
		[],
		"A goods peddler.",
		[
			(assign, "$background_answer_3", 5),
			(str_store_string, 14, "@{reg3?daughter:man}"),
			(str_store_string, 13, "@{reg3?woman:man}"),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. Heeding the call of the open road, you travelled from village to village buying and selling what you could. It was not a rich existence, but you became a master at haggling even the most miserly elders into giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("craftsman",
		[],
		"A smith.",
		[
			(assign, "$background_answer_3", 4),
			(str_store_string, 14, "@{reg3?daughter:man}"),
			(str_store_string, 13, "@{reg3?woman:man}"),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You pursued a career as a smith, crafting items of function and beauty out of simple metal. As time wore on you became a master of your trade, and fine work started to fetch fine prices. With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("poacher",
		[],
		"A game poacher.",
		[
			(assign, "$background_answer_3", 3),
			(str_store_string, 14, "@{reg3?daughter:man}"),
			(str_store_string, 13, "@{reg3?woman:man}"),
			(str_store_string, 12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
			(jump_to_menu, "mnu_start_character_4")
		], "."),

		("go_back",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_start_character_2")
		], ".")
	]
	),

	("start_character_4", 0, "{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
"none",
	[],
	[
		("revenge",
		[],
		"Personal revenge.",
		[
			(assign, "$background_answer_4", 1),
			(str_store_string, 13, "@Only you know exactly what caused you to give up your old life and become an adventurer. Still, it was not a difficult choice to leave, with the rage burning brightly in your heart. You want vengeance. You want justice. What was done to you cannot be undone, and these debts can only be paid in blood..."),
			(jump_to_menu, "mnu_pick_nation")
		], "."),

		("death",
		[],
		"The loss of a loved one.",
		[
			(assign, "$background_answer_4", 2),
			(str_store_string, 13, "@Only you know exactly what caused you to give up your old life and become an adventurer. All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so painful. Perhaps your new life will let you forget, or honour the name that you can no longer bear to speak..."),
			(jump_to_menu, "mnu_pick_nation")
		], "."),

		("wanderlust",
		[],
		"Wanderlust.",
		[
			(assign, "$background_answer_4", 3),
			(str_store_string, 13, "@Only you know exactly what caused you to give up your old life and become an adventurer. You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
			(jump_to_menu, "mnu_pick_nation")
		], "."),

		("disown",
		[],
		"Being forced out of your home.",
		[
			(assign, "$background_answer_4", 5),
			(str_store_string, 13, "@Only you know exactly what caused you to give up your old life and become an adventurer. However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
			(jump_to_menu, "mnu_pick_nation")
		], "."),

		("greed",
		[],
		"Lust for money and power.",
		[
			(assign, "$background_answer_4", 6),
			(str_store_string, 13, "@Only you know exactly what caused you to give up your old life and become an adventurer. To everyone else, it's clear that you're now motivated solely by personal gain. You want to be rich, powerful, respected, feared. You want to be the one whom others hurry to obey. You want people to know your name, and tremble whenever it is spoken. You want everything, and you won't let anyone stop you from having it..."),
			(jump_to_menu, "mnu_pick_nation")
		], "."),

		("go_back",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_start_character_3")
		], ".")
	]
	),

	("choose_skill", 0, "{s13}",
"none",
	[
		(assign, "$current_string_reg", 10),
		(assign, ":var_1", 0),
		(try_begin),
			(eq, "$character_gender", 1),
			(str_store_string, 14, "str_woman"),
			(val_add, ":var_1", 1),
		(else_try),
			(str_store_string, 14, "str_man"),
		(try_end),
		(try_begin),
			(eq, "$background_type", 1),
			(str_store_string, 15, "str_noble"),
			(val_sub, ":var_1", 1),
		(else_try),
			(str_store_string, 15, "str_common"),
		(try_end),
		(try_begin),
			(eq, ":var_1", -1),
			(str_store_string, 16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
		(else_try),
			(eq, ":var_1", 0),
			(str_store_string, 16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
		(else_try),
			(eq, ":var_1", 1),
			(str_store_string, 16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
		(try_end)
	],
	[
		("begin_adventuring",
		[],
		"Become an adventurer and ride to your destiny.",
		[
			(set_show_messages, 0),
			(try_begin),
				(eq, "$character_gender", 0),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 3, 1),
			(else_try),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
			(try_end),
			(troop_raise_attribute, "trp_player", 0, 1),
			(troop_raise_attribute, "trp_player", 1, 1),
			(troop_raise_attribute, "trp_player", 3, 1),
			(troop_raise_skill, "trp_player", "skl_leadership", 1),
			(troop_raise_skill, "trp_player", "skl_riding", 1),
			(try_begin),
				(eq, "$background_type", 1),
				(eq, "$character_gender", 0),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_attribute, "trp_player", 3, 2),
				(troop_raise_skill, "trp_player", 27, 1),
				(troop_raise_skill, "trp_player", 35, 1),
				(troop_raise_skill, "trp_player", 24, 1),
				(troop_raise_skill, "trp_player", 15, 1),
				(troop_raise_skill, "trp_player", 1, 1),
				(troop_raise_proficiency, "trp_player", 0, 10),
				(troop_raise_proficiency, "trp_player", 1, 10),
				(troop_raise_proficiency, "trp_player", 2, 10),
				(troop_add_item, "trp_player", "itm_tab_shield_round_a", 5),
				(troop_set_slot, "trp_player", slot_troop_renown, 100),
				(call_script, "script_change_player_honor", 3),
				(troop_add_gold, "trp_player", 100),
			(else_try),
				(eq, "$background_type", 1),
				(eq, "$character_gender", 1),
				(troop_raise_attribute, "trp_player", 2, 2),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_skill, "trp_player", 11, 1),
				(troop_raise_skill, "trp_player", 24, 2),
				(troop_raise_skill, "trp_player", 9, 1),
				(troop_raise_skill, "trp_player", 1, 1),
				(troop_raise_proficiency, "trp_player", 0, 20),
				(troop_set_slot, "trp_player", slot_troop_renown, 50),
				(troop_add_item, "trp_player", "itm_tab_shield_round_a", 5),
				(troop_add_gold, "trp_player", 100),
			(else_try),
				(eq, "$background_type", 2),
				(troop_raise_attribute, "trp_player", 2, 2),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_skill, "trp_player", 24, 1),
				(troop_raise_skill, "trp_player", 1, 1),
				(troop_raise_skill, "trp_player", 0, 2),
				(troop_raise_skill, "trp_player", 12, 1),
				(troop_raise_proficiency, "trp_player", 1, 10),
				(troop_add_gold, "trp_player", 250),
				(troop_set_slot, "trp_player", slot_troop_renown, 20),
			(else_try),
				(eq, "$background_type", 3),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_skill, "trp_player", "skl_ironflesh", 1),
				(troop_raise_skill, "trp_player", "skl_power_strike", 1),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
				(troop_raise_skill, "trp_player", "skl_leadership", 1),
				(troop_raise_skill, "trp_player", "skl_trainer", 1),
				(troop_raise_proficiency, "trp_player", 0, 10),
				(troop_raise_proficiency, "trp_player", 1, 15),
				(troop_raise_proficiency, "trp_player", 2, 20),
				(troop_raise_proficiency, "trp_player", 5, 10),
				(troop_add_item, "trp_player", "itm_tab_shield_kite_c", 5),
				(troop_add_gold, "trp_player", 50),
				(troop_set_slot, "trp_player", slot_troop_renown, 10),
			(else_try),
				(eq, "$background_type", 4),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 2),
				(troop_raise_skill, "trp_player", "skl_power_draw", 1),
				(troop_raise_skill, "trp_player", "skl_tracking", 1),
				(troop_raise_skill, "trp_player", "skl_pathfinding", 1),
				(troop_raise_skill, "trp_player", "skl_spotting", 1),
				(troop_raise_skill, "trp_player", "skl_athletics", 1),
				(troop_raise_proficiency, "trp_player", 1, 10),
				(troop_raise_proficiency, "trp_player", 3, 30),
				(troop_add_gold, "trp_player", 30),
			(else_try),
				(eq, "$background_type", 5),
				(eq, "$character_gender", 0),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_power_draw", 1),
				(troop_raise_skill, "trp_player", "skl_horse_archery", 1),
				(troop_raise_skill, "trp_player", "skl_pathfinding", 1),
				(troop_raise_skill, "trp_player", "skl_riding", 2),
				(troop_raise_proficiency, "trp_player", 0, 10),
				(troop_raise_proficiency, "trp_player", 3, 30),
				(troop_raise_proficiency, "trp_player", 5, 10),
				(troop_add_item, "trp_player", "itm_tab_shield_small_round_a", 5),
				(troop_add_gold, "trp_player", 15),
				(troop_set_slot, "trp_player", slot_troop_renown, 10),
			(else_try),
				(eq, "$background_type", 5),
				(eq, "$character_gender", 1),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
				(troop_raise_skill, "trp_player", "skl_first_aid", 1),
				(troop_raise_skill, "trp_player", "skl_pathfinding", 1),
				(troop_raise_skill, "trp_player", "skl_riding", 2),
				(troop_raise_proficiency, "trp_player", 0, 5),
				(troop_raise_proficiency, "trp_player", 3, 20),
				(troop_raise_proficiency, "trp_player", 5, 5),
				(troop_add_item, "trp_player", "itm_tab_shield_small_round_a", 5),
				(troop_add_gold, "trp_player", 20),
			(else_try),
				(eq, "$background_type", 6),
				(troop_raise_attribute, "trp_player", 1, 3),
				(troop_raise_skill, "trp_player", "skl_athletics", 2),
				(troop_raise_skill, "trp_player", "skl_power_throw", 1),
				(troop_raise_skill, "trp_player", "skl_inventory_management", 1),
				(troop_raise_skill, "trp_player", "skl_looting", 1),
				(troop_raise_proficiency, "trp_player", 0, 20),
				(troop_raise_proficiency, "trp_player", 5, 20),
				(troop_add_item, "trp_player", "itm_throwing_knives", 0),
				(troop_add_gold, "trp_player", 25),
			(try_end),
			(try_begin),
				(eq, "$background_answer_2", 0),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_skill, "trp_player", "skl_power_strike", 1),
				(troop_raise_skill, "trp_player", "skl_persuasion", 1),
				(troop_raise_proficiency, "trp_player", 0, 15),
				(troop_raise_proficiency, "trp_player", 2, 5),
			(else_try),
				(eq, "$background_answer_2", 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_skill, "trp_player", "skl_engineer", 1),
				(troop_raise_skill, "trp_player", "skl_trade", 1),
			(else_try),
				(eq, "$background_answer_2", 2),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_spotting", 1),
				(troop_raise_skill, "trp_player", "skl_looting", 1),
				(troop_raise_proficiency, "trp_player", 0, 15),
				(troop_raise_proficiency, "trp_player", 5, 5),
			(else_try),
				(eq, "$background_answer_2", 3),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_skill, "trp_player", "skl_horse_archery", 1),
				(troop_raise_skill, "trp_player", "skl_power_throw", 1),
				(troop_raise_proficiency, "trp_player", 3, 15),
				(call_script, "script_change_troop_renown", "trp_player", 5),
			(else_try),
				(eq, "$background_answer_2", 4),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_skill, "trp_player", "skl_inventory_management", 1),
				(troop_raise_skill, "trp_player", "skl_trade", 1),
			(try_end),
			(try_begin),
				(eq, "$background_answer_3", 3),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_skill, "trp_player", "skl_power_draw", 1),
				(troop_raise_skill, "trp_player", "skl_tracking", 1),
				(troop_raise_skill, "trp_player", "skl_spotting", 1),
				(troop_raise_skill, "trp_player", "skl_athletics", 1),
				(troop_add_gold, "trp_player", 10),
				(troop_raise_proficiency, "trp_player", 2, 10),
				(troop_raise_proficiency, "trp_player", 3, 35),
				(troop_add_item, "trp_player", "itm_raf_two_handed_axe_a", 4),
				(troop_add_item, "trp_player", "itm_rawhide_coat", 0),
				(troop_add_item, "trp_player", "itm_hunting_bow", 0),
				(troop_add_item, "trp_player", "itm_barbed_arrows", 0),
				(troop_add_item, "trp_player", "itm_sumpter_horse", 18),
				(troop_add_item, "trp_player", "itm_dried_meat", 0),
				(troop_add_item, "trp_player", "itm_dried_meat", 0),
				(troop_add_item, "trp_player", "itm_furs", 0),
				(troop_add_item, "trp_player", "itm_furs", 0),
			(else_try),
				(eq, "$background_answer_3", 4),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
				(troop_raise_skill, "trp_player", "skl_engineer", 1),
				(troop_raise_skill, "trp_player", "skl_tactics", 1),
				(troop_raise_skill, "trp_player", "skl_trade", 1),
				(troop_raise_proficiency, "trp_player", 0, 15),
				(troop_add_gold, "trp_player", 100),
				(troop_add_item, "trp_player", "itm_leather_boots", 22),
				(troop_add_item, "trp_player", "itm_coarse_tunic", 0),
				(troop_add_item, "trp_player", "itm_sword_type_xiii", 13),
				(troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
				(troop_add_item, "trp_player", "itm_bolts", 0),
				(troop_add_item, "trp_player", "itm_tools", 0),
				(troop_add_item, "trp_player", "itm_saddle_horse", 0),
				(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(else_try),
				(eq, "$background_answer_3", 5),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_riding", 1),
				(troop_raise_skill, "trp_player", "skl_trade", 1),
				(troop_raise_skill, "trp_player", "skl_pathfinding", 1),
				(troop_raise_skill, "trp_player", "skl_inventory_management", 1),
				(troop_add_item, "trp_player", "itm_leather_gloves", 0),
				(troop_add_gold, "trp_player", 90),
				(troop_raise_proficiency, "trp_player", 2, 15),
				(troop_add_item, "trp_player", "itm_leather_jacket", 0),
				(troop_add_item, "trp_player", "itm_leather_boots", 22),
				(troop_add_item, "trp_player", "itm_fur_hat", 0),
				(troop_add_item, "trp_player", "itm_staff", 0),
				(troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
				(troop_add_item, "trp_player", "itm_bolts", 0),
				(troop_add_item, "trp_player", "itm_saddle_horse", 0),
				(troop_add_item, "trp_player", "itm_sumpter_horse", 0),
				(troop_add_item, "trp_player", "itm_linen", 0),
				(troop_add_item, "trp_player", "itm_pottery", 0),
				(troop_add_item, "trp_player", "itm_wool", 0),
				(troop_add_item, "trp_player", "itm_wool", 0),
				(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(else_try),
				(eq, "$background_answer_3", 7),
				(troop_raise_attribute, "trp_player", 3, 2),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
				(troop_raise_skill, "trp_player", "skl_persuasion", 1),
				(troop_raise_skill, "trp_player", "skl_leadership", 1),
				(troop_raise_skill, "trp_player", "skl_pathfinding", 1),
				(troop_add_gold, "trp_player", 80),
				(troop_raise_proficiency, "trp_player", 0, 25),
				(troop_raise_proficiency, "trp_player", 4, 10),
				(troop_add_item, "trp_player", "itm_archer_a", 24),
				(troop_add_item, "trp_player", "itm_leather_boots", 22),
				(troop_add_item, "trp_player", "itm_sword_type_xii", 2),
				(troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
				(troop_add_item, "trp_player", "itm_bolts", 0),
				(troop_add_item, "trp_player", "itm_saddle_horse", 31),
				(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(else_try),
				(eq, "$background_answer_3", 8),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_skill, "trp_player", "skl_riding", 1),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
				(troop_raise_skill, "trp_player", "skl_power_strike", 1),
				(troop_raise_skill, "trp_player", "skl_leadership", 1),
				(troop_add_gold, "trp_player", 20),
				(troop_raise_proficiency, "trp_player", 0, 30),
				(troop_raise_proficiency, "trp_player", 1, 30),
				(troop_raise_proficiency, "trp_player", 2, 30),
				(troop_raise_proficiency, "trp_player", 3, 10),
				(troop_raise_proficiency, "trp_player", 4, 10),
				(troop_raise_proficiency, "trp_player", 5, 10),
				(troop_add_item, "trp_player", "itm_leather_jerkin", 22),
				(troop_add_item, "trp_player", "itm_leather_boots", 21),
				(troop_add_item, "trp_player", "itm_sword_type_xii", 2),
				(troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
				(troop_add_item, "trp_player", "itm_bolts", 0),
				(troop_add_item, "trp_player", "itm_saddle_horse", 31),
				(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(else_try),
				(eq, "$background_answer_3", 9),
				(eq, "$character_gender", 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_attribute, "trp_player", 3, 1),
				(troop_raise_skill, "trp_player", "skl_persuasion", 2),
				(troop_raise_skill, "trp_player", "skl_riding", 1),
				(troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
				(troop_add_item, "trp_player", "itm_dagger", 0),
				(troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
				(troop_add_item, "trp_player", "itm_bolts", 0),
				(troop_add_item, "trp_player", "itm_courser", 35),
				(troop_add_item, "trp_player", "itm_arming_cap", 24),
				(troop_add_item, "trp_player", "itm_peasant_dress", 24),
				(troop_add_gold, "trp_player", 100),
				(troop_raise_proficiency, "trp_player", 0, 10),
				(troop_raise_proficiency, "trp_player", 4, 15),
				(troop_add_item, "trp_player", "itm_smoked_fish", 0),
			(else_try),
				(eq, "$background_answer_3", 10),
				(troop_raise_attribute, "trp_player", 2, 2),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
				(troop_raise_skill, "trp_player", "skl_surgery", 1),
				(troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
				(troop_raise_skill, "trp_player", "skl_persuasion", 1),
				(troop_add_gold, "trp_player", 80),
				(troop_raise_proficiency, "trp_player", 0, 20),
				(troop_raise_proficiency, "trp_player", 4, 20),
				(troop_add_item, "trp_player", "itm_linen_tunic", 24),
				(troop_add_item, "trp_player", "itm_woolen_hose", 0),
				(troop_add_item, "trp_player", "itm_sword_type_xii", 2),
				(troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
				(troop_add_item, "trp_player", "itm_bolts", 0),
				(troop_add_item, "trp_player", "itm_saddle_horse", 31),
				(troop_add_item, "trp_player", "itm_smoked_fish", 0),
				(store_random_in_range, ":random_in_range_book_tactics_spice", "itm_book_tactics", "itm_spice"),
				(troop_add_item, "trp_player", ":random_in_range_book_tactics_spice", 0),
			(try_end),
			(try_begin),
				(eq, "$background_answer_4", 1),
				(troop_raise_attribute, "trp_player", 0, 2),
				(troop_raise_skill, "trp_player", "skl_power_strike", 1),
			(else_try),
				(eq, "$background_answer_4", 2),
				(troop_raise_attribute, "trp_player", 3, 2),
				(troop_raise_skill, "trp_player", "skl_ironflesh", 1),
			(else_try),
				(eq, "$background_answer_4", 3),
				(troop_raise_attribute, "trp_player", 1, 2),
				(troop_raise_skill, "trp_player", "skl_pathfinding", 1),
			(else_try),
				(eq, "$background_answer_4", 5),
				(troop_raise_attribute, "trp_player", 0, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
			(else_try),
				(eq, "$background_answer_4", 6),
				(troop_raise_attribute, "trp_player", 1, 1),
				(troop_raise_attribute, "trp_player", 2, 1),
				(troop_raise_skill, "trp_player", "skl_looting", 1),
			(try_end),
			(try_begin),
				(eq, "$background_type", 1),
				(jump_to_menu, "mnu_auto_return"),
				(start_presentation, "prsnt_banner_selection"),
			(else_try),
				(change_screen_return, 0),
			(try_end),
			(troop_add_gold, "trp_player", 1000),
			(try_begin),
				(gt, "$g_start_faction", 0),
				(call_script, "script_player_join_faction", "$g_start_faction"),
				(assign, "$player_has_homage", 1),
				(try_begin),
					(call_script, "script_cf_select_random_village_with_faction", "$g_start_faction"),
					(call_script, "script_give_center_to_lord", reg0, "trp_player", 0),
					(faction_get_slot, ":g_start_faction_leader", "$g_start_faction", slot_faction_leader),
					(call_script, "script_add_log_entry", 22, ":g_start_faction_leader", reg0, "trp_player", "$g_start_faction"),
				(try_end),
				(try_begin),
					(troop_add_gold, "trp_player", 5000),
					(faction_get_slot, ":g_start_faction_culture", "$g_start_faction", slot_faction_culture),
					(faction_get_slot, ":g_start_faction_culture_101", ":g_start_faction_culture", 101),
					(call_script, "script_equip_companion", "trp_player", ":g_start_faction_culture_101"),
					(troop_add_item, "trp_player", "itm_bread"),
					(troop_add_item, "trp_player", "itm_butter"),
				(try_end),
			(try_end),
			(set_show_messages, 1)
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_start_character_4")
		], ".")
	]
	),

	("past_life_explanation", 0, "{s3}",
"none",
	[
		(try_begin),
			(gt, "$current_string_reg", 14),
			(assign, "$current_string_reg", 10),
		(try_end),
		(str_store_string_reg, 3, "$current_string_reg"),
		(try_begin),
			(ge, "$current_string_reg", 14),
			(str_store_string, 5, "@Back to the beginning..."),
		(else_try),
			(str_store_string, 5, "@View next segment..."),
		(try_end)
	],
	[
		("view_next",
		[],
		"{s5}",
		[
			(val_add, "$current_string_reg", 1),
			(jump_to_menu, "mnu_past_life_explanation")
		], "."),

		("continue",
		[],
		"Continue...",
		[], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_choose_skill")
		], ".")
	]
	),

	("auto_return", 0, "{!}This menu automatically returns to caller.",
"none",
	[
		(change_screen_return, 0)
	],
	[]
	),

	("morale_report", 0, "{s1}",
"none",
	[
		(call_script, "script_get_player_party_morale_values"),
		(assign, ":var_1", reg0),
		(assign, reg1, "$g_player_party_morale_modifier_party_size"),
		(try_begin),
			(gt, reg1, 0),
			(str_store_string, 2, "@{!} -"),
		(else_try),
			(str_store_string, 2, "str_space"),
		(try_end),
		(assign, reg2, "$g_player_party_morale_modifier_leadership"),
		(try_begin),
			(gt, reg2, 0),
			(str_store_string, 3, "@{!} +"),
		(else_try),
			(str_store_string, 3, "str_space"),
		(try_end),
		(try_begin),
			(gt, "$g_player_party_morale_modifier_no_food", 0),
			(assign, reg7, "$g_player_party_morale_modifier_no_food"),
			(str_store_string, 5, "@^No food:  -{reg7}"),
		(else_try),
			(str_store_string, 5, "str_space"),
		(try_end),
		(assign, reg3, "$g_player_party_morale_modifier_food"),
		(try_begin),
			(gt, reg3, 0),
			(str_store_string, 4, "@{!} +"),
		(else_try),
			(str_store_string, 4, "str_space"),
		(try_end),
		(try_begin),
			(gt, "$g_player_party_morale_modifier_debt", 0),
			(assign, reg6, "$g_player_party_morale_modifier_debt"),
			(str_store_string, 6, "@^Wage debt:  -{reg6}"),
		(else_try),
			(str_store_string, 6, "str_space"),
		(try_end),
		(party_get_morale, reg5, "p_main_party"),
		(store_sub, reg4, reg5, ":var_1"),
		(try_begin),
			(gt, reg4, 0),
			(str_store_string, 7, "@{!} +"),
		(else_try),
			(str_store_string, 7, "str_space"),
		(try_end),
		(assign, reg6, 50),
		(str_store_string, 1, "str_current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("courtship_relations", 0, "{s1}",
"none",
	[
		(str_store_string, 1, "str_courtships_in_progress_"),
		(try_for_range, ":troop", "trp_knight_1_1_wife", "trp_heroes_end"),
			(troop_slot_eq, ":troop", slot_troop_met, 2),
			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop"),
			(gt, reg0, 0),
			(assign, reg3, reg0),
			(str_store_troop_name, 2, ":troop"),
			(store_current_hours, ":current_hours"),
			(troop_get_slot, ":troop_last_talk_time", ":troop", slot_troop_last_talk_time),
			(val_sub, ":current_hours", ":troop_last_talk_time"),
			(store_div, ":value", ":current_hours", 24),
			(assign, reg4, ":value"),
			(str_store_string, 1, "str_s1_s2_relation_reg3_last_visit_reg4_days_ago"),
		(try_end),
		(str_store_string, 1, "str_s1__poems_known"),
		(try_begin),
			(gt, "$allegoric_poem_recitations", 0),
			(str_store_string, 1, "str_s1_storming_the_castle_of_love_allegoric"),
		(try_end),
		(try_begin),
			(gt, "$tragic_poem_recitations", 0),
			(str_store_string, 1, "str_s1_kais_and_layali_tragic"),
		(try_end),
		(try_begin),
			(gt, "$comic_poem_recitations", 0),
			(str_store_string, 1, "str_s1_a_conversation_in_the_garden_comic"),
		(try_end),
		(try_begin),
			(gt, "$heroic_poem_recitations", 0),
			(str_store_string, 1, "str_s1_helgered_and_kara_epic"),
		(try_end),
		(try_begin),
			(gt, "$mystic_poem_recitations", 0),
			(str_store_string, 1, "str_s1_a_hearts_desire_mystic"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("lord_relations", 0, "{s1}",
"none",
	[
		(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
			(troop_set_slot, ":troop", slot_troop_temp_slot, 0),
		(try_end),
		(str_clear, 1),
		(try_for_range, ":unused", "trp_npc1", "trp_knight_1_1_wife"),
			(assign, ":value", -100),
			(assign, ":value_2", -1),
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_temp_slot, 0),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_slot_ge, ":troop", 5, 1),
				(call_script, "script_troop_get_player_relation", ":troop"),
				(assign, ":var_5", reg0),
				(ge, ":var_5", ":value"),
				(assign, ":value", ":var_5"),
				(assign, ":value_2", ":troop"),
			(try_end),
			(gt, ":value_2", -1),
			(str_store_troop_name_link, 4, ":value_2"),
			(assign, reg4, ":value"),
			(str_store_string, 1, "@{!}{s1}^{s4}: {reg4}"),
			(troop_set_slot, ":value_2", slot_troop_temp_slot, 1),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("companion_report", 0, "{s7}{s1}",
"none",
	[
		(str_clear, 1),
		(str_store_string, 7, "str_no_companions_in_service"),
		(try_begin),
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(try_begin),
				(troop_get_type, ":type_player", "trp_player"),
				(eq, ":type_player", 1),
				(str_store_string, 8, "str_husband"),
			(else_try),
				(str_store_string, 8, "str_wife"),
			(try_end),
			(try_begin),
				(le, ":player_spouse", 0),
				(troop_get_slot, ":player_spouse", "trp_player", slot_troop_betrothed),
				(str_store_string, 8, "str_betrothed"),
			(try_end),
			(gt, ":player_spouse", 0),
			(str_store_troop_name, 4, ":player_spouse"),
			(troop_get_slot, ":player_spouse_cur_center", ":player_spouse", slot_troop_cur_center),
			(try_begin),
				(is_between, ":player_spouse_cur_center", "p_town_1_1", "p_salt_mine"),
				(str_store_party_name, 5, ":player_spouse_cur_center"),
			(else_try),
				(troop_slot_eq, ":player_spouse", slot_troop_occupation, 2),
				(str_store_string, 5, "str_leading_party"),
			(else_try),
				(str_store_string, 5, "str_whereabouts_unknown"),
			(try_end),
			(str_store_string, 3, "str_s4_s8_s5"),
			(str_store_string, 2, 1),
			(str_store_string, 1, "str_s2_s3"),
		(try_end),
		(try_begin),
			(ge, "$cheat_mode", 1),
			(ge, "$npc_to_rejoin_party", 0),
			(str_store_troop_name, 5, "$npc_to_rejoin_party"),
			(str_store_string, 1, "@{!}DEBUG -- {s1}^NPC in rejoin queue: {s5}^"),
		(try_end),
		(try_for_range, ":troop", "trp_npc1", "trp_kingdom_1_lord"),
			(str_clear, 2),
			(str_clear, 3),
			(try_begin),
				(troop_get_slot, ":troop_current_mission", ":troop", slot_troop_current_mission),
				(try_begin),
					(troop_slot_eq, ":troop", 400, 1),
					(neg|troop_slot_eq, ":troop", slot_troop_occupation, 5),
					(assign, ":value", -1),
					(assign, ":value_2", -1),
					(assign, ":value_3", -1),
					(try_for_parties, ":var_9"),
						(party_slot_eq, ":var_9", slot_party_type, 26),
						(assign, ":value", ":var_9"),
						(party_get_slot, ":value_2", ":var_9", slot_party_ai_object),
						(party_get_slot, ":value_3", ":var_9", slot_party_home_center),
					(try_end),
					(try_begin),
						(gt, ":value", 0),
						(eq, ":value_2", ":value_3"),
						(str_store_string, 8, "@is traveling to"),
						(str_store_party_name, 5, ":value_3"),
						(str_store_troop_name, 4, ":troop"),
						(display_message, "@{s4} {s8} to {s5}"),
					(else_try),
						(lt, ":value", 0),
						(troop_get_slot, ":troop_cur_center", ":troop", slot_troop_cur_center),
						(gt, ":troop_cur_center", 0),
						(party_slot_eq, ":troop_cur_center", slot_party_type, 3),
						(str_store_string, 8, "@Awaiting your arrival"),
						(str_store_party_name, 5, ":troop_cur_center"),
						(str_store_troop_name, 4, ":troop"),
						(display_message, "@{s4} - {s8} in {s5} tavern"),
					(else_try),
						(gt, ":value", 0),
						(str_store_string, 8, "@is awaiting your messenger in"),
						(str_store_party_name, 5, ":value_2"),
						(str_store_troop_name, 4, ":troop"),
						(display_message, "@{s4} {s8} to {s5}"),
					(try_end),
					(str_store_string, 3, "str_s4_s8_s5"),
					(str_store_string, 2, 1),
					(str_store_string, 1, "str_s2_s3"),
				(try_end),
				(troop_slot_eq, ":troop", slot_troop_occupation, 5),
				(str_store_troop_name, 4, ":troop"),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_mission_object, 1),
					(str_store_string, 8, "str_gathering_support"),
					(try_begin),
						(eq, ":troop_current_mission", 1),
						(str_store_string, 5, "str_expected_back_imminently"),
					(else_try),
						(assign, reg3, ":troop_current_mission"),
						(str_store_string, 5, "str_expected_back_in_approximately_reg3_days"),
					(try_end),
				(else_try),
					(troop_slot_eq, ":troop", slot_troop_mission_object, 2),
					(troop_get_slot, ":troop_town_with_contacts", ":troop", slot_troop_town_with_contacts),
					(str_store_party_name, 11, ":troop_town_with_contacts"),
					(str_store_string, 8, "str_gathering_intelligence"),
					(try_begin),
						(eq, ":troop_current_mission", 1),
						(str_store_string, 5, "str_expected_back_imminently"),
					(else_try),
						(assign, reg3, ":troop_current_mission"),
						(str_store_string, 5, "str_expected_back_in_approximately_reg3_days"),
					(try_end),
				(else_try),
					(troop_slot_ge, ":troop", 152, 3),
					(neg|troop_slot_ge, ":troop", 152, 8),
					(troop_get_slot, ":troop_recent_offense_time", ":troop", slot_troop_recent_offense_time),
					(str_store_faction_name, 9, ":troop_recent_offense_time"),
					(str_store_string, 8, "str_diplomatic_embassy_to_s9"),
					(try_begin),
						(eq, ":troop_current_mission", 1),
						(str_store_string, 5, "str_expected_back_imminently"),
					(else_try),
						(assign, reg3, ":troop_current_mission"),
						(str_store_string, 5, "str_expected_back_in_approximately_reg3_days"),
					(try_end),
				(else_try),
					(eq, ":troop", "$g_player_minister"),
					(str_store_string, 8, "str_serving_as_minister"),
					(try_begin),
						(is_between, "$g_player_court", "p_town_1_1", "p_salt_mine"),
						(str_store_party_name, 9, "$g_player_court"),
						(str_store_string, 5, "str_in_your_court_at_s9"),
					(else_try),
						(str_store_string, 5, "str_whereabouts_unknown"),
					(try_end),
				(else_try),
					(main_party_has_troop, ":troop"),
					(str_store_string, 8, "str_under_arms"),
					(str_store_string, 5, "str_in_your_party"),
				(else_try),
					(troop_slot_eq, ":troop", slot_troop_mission_object, 8),
					(str_store_string, 8, "str_attempting_to_rejoin_party"),
					(str_store_string, 5, "str_whereabouts_unknown"),
				(else_try),
					(troop_slot_ge, ":troop", 12, 1),
					(str_store_string, 8, "str_separated_from_party"),
					(str_store_string, 5, "str_whereabouts_unknown"),
				(else_try),
					(try_begin),
						(check_quest_active, "qst_lend_companion"),
						(quest_slot_eq, "qst_lend_companion", slot_quest_target_troop, ":troop"),
						(str_store_string, 8, "@On loan,"),
					(else_try),
						(troop_set_slot, ":troop", slot_troop_mission_object, 8),
						(str_store_string, 8, "str_attempting_to_rejoin_party"),
					(try_end),
					(str_store_string, 5, "str_whereabouts_unknown"),
					(try_begin),
						(ge, "$cheat_mode", 1),
						(troop_get_slot, reg2, ":troop", slot_troop_mission_object),
						(troop_get_slot, reg3, ":troop", slot_troop_current_mission),
						(troop_get_slot, reg4, ":troop", slot_troop_prisoner_of_party),
						(troop_get_slot, reg4, ":troop", slot_troop_playerparty_history),
						(display_message, "@{!}DEBUG: {s4} current mission: {reg2}, days on mission: {reg3}, prisoner: {reg4}, pphistory: {reg5}"),
					(try_end),
				(try_end),
				(str_store_string, 3, "str_s4_s8_s5"),
				(str_store_string, 2, 1),
				(str_store_string, 1, "str_s2_s3"),
				(str_clear, 7),
			(else_try),
				(neg|troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_slot_ge, ":troop", 8, "p_town_1_1"),
				(str_store_troop_name, 4, ":troop"),
				(str_store_string, 8, "str_missing_after_battle"),
				(str_store_string, 5, "str_whereabouts_unknown"),
				(str_store_string, 3, "str_s4_s8_s5"),
				(str_store_string, 2, 1),
				(str_store_string, 1, "str_s2_s3"),
				(str_clear, 7),
			(try_end),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("faction_orders", 0, "{!}{s9}",
"none",
	[
		(str_clear, 9),
		(store_current_hours, ":current_hours"),
		(try_for_range, ":faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(faction_slot_eq, ":faction", slot_faction_state, 0),
			(neq, ":faction", "fac_player_supporters_faction"),
			(faction_get_slot, ":faction_ai_state", ":faction", slot_faction_ai_state),
			(try_begin),
				(faction_get_slot, ":faction_marshall", ":faction", slot_faction_marshall),
				(gt, ":faction_marshall", -1),
				(assign, ":value", ":faction_marshall"),
			(else_try),
				(faction_get_slot, ":value", ":faction", slot_faction_leader),
			(try_end),
			(call_script, "script_npc_decision_checklist_faction_ai_alt", ":value"),
			(assign, ":var_6", reg0),
			(str_store_string, 26, 14),
			(faction_get_slot, ":faction_ai_state_2", ":faction", slot_faction_ai_state),
			(faction_get_slot, ":faction_ai_object", ":faction", slot_faction_ai_object),
			(faction_get_slot, ":faction_marshall_2", ":faction", slot_faction_marshall),
			(faction_get_slot, ":faction_ai_offensive_max_followers", ":faction", slot_faction_ai_offensive_max_followers),
			(str_store_faction_name, 10, ":faction"),
			(try_begin),
				(faction_get_slot, ":faction_political_issue", ":faction", slot_faction_political_issue),
				(try_begin),
					(eq, ":faction_political_issue", 1),
					(str_store_string, 11, "@Appoint next marshal"),
				(else_try),
					(is_between, ":faction_political_issue", "p_town_1_1", "p_salt_mine"),
					(str_store_party_name, 12, ":faction_political_issue"),
					(str_store_string, 11, "@Award {s12} as fief"),
				(else_try),
					(eq, ":faction_political_issue", 0),
					(str_store_string, 11, "@None"),
				(else_try),
					(assign, reg3, ":faction_political_issue"),
					(str_store_string, 11, "@{!}Error ({reg3})"),
				(try_end),
				(store_current_hours, reg4),
				(faction_get_slot, ":faction_political_issue_time", ":faction", slot_faction_political_issue_time),
				(val_sub, reg4, ":faction_political_issue_time"),
				(str_store_string, 10, "@{!}{s10}^Faction political issue: {s11}"),
				(try_begin),
					(faction_slot_ge, ":faction", 64, 1),
					(str_store_string, 10, "@{!}{s10} (on agenda {reg4} hours)"),
				(try_end),
			(try_end),
			(assign, reg2, ":faction_ai_offensive_max_followers"),
			(try_begin),
				(eq, ":faction_ai_state_2", 0),
				(str_store_string, 11, "@{!}Defending"),
			(else_try),
				(eq, ":faction_ai_state_2", 1),
				(str_store_string, 11, "@{!}Gathering army"),
			(else_try),
				(eq, ":faction_ai_state_2", 2),
				(str_store_party_name, 11, ":faction_ai_object"),
				(str_store_string, 11, "@{!}Besieging {s11}"),
			(else_try),
				(eq, ":faction_ai_state_2", 3),
				(str_store_party_name, 11, ":faction_ai_object"),
				(str_store_string, 11, "@{!}Raiding {s11}"),
			(else_try),
				(eq, ":faction_ai_state_2", 4),
				(str_store_party_name, 11, ":faction_ai_object"),
				(str_store_string, 11, "str_attacking_enemy_army_near_s11"),
			(else_try),
				(eq, ":faction_ai_state_2", 6),
				(str_store_party_name, 11, ":faction_ai_object"),
				(str_store_string, 11, "str_holding_feast_at_s11"),
			(else_try),
				(eq, ":faction_ai_state_2", 5),
				(str_store_party_name, 11, ":faction_ai_object"),
				(str_store_string, 11, "@{!}Attacking enemies around {s11}"),
			(else_try),
				(assign, reg4, ":faction_ai_state_2"),
				(str_store_string, 11, "str_sfai_reg4"),
			(try_end),
			(try_begin),
				(lt, ":faction_marshall_2", 0),
				(str_store_string, 12, "@No one"),
			(else_try),
				(str_store_troop_name, 12, ":faction_marshall_2"),
				(troop_get_slot, reg21, ":faction_marshall_2", slot_troop_days_on_mission),
				(str_store_string, 12, "@{!}{s12} (controversy: {reg21})"),
			(try_end),
			(try_for_parties, ":var_13"),
				(party_slot_eq, ":var_13", slot_party_ai_state, 12),
				(store_faction_of_party, ":faction_of_party_var_13", ":var_13"),
				(eq, ":faction_of_party_var_13", ":faction"),
				(str_store_party_name, 38, ":var_13"),
				(str_store_string, 12, "@{!}{s12}^Screening party: {s38}"),
			(try_end),
			(try_begin),
				(this_or_next|eq, ":var_6", 0),
				(eq, ":var_6", 6),
				(store_current_hours, ":current_hours_2"),
				(faction_get_slot, ":faction_ai_current_state_started", ":faction", slot_faction_ai_current_state_started),
				(val_sub, ":current_hours_2", ":faction_ai_current_state_started"),
				(ge, ":current_hours_2", 18),
				(store_current_hours, ":current_hours_3"),
				(faction_set_slot, ":faction", slot_faction_ai_last_rest_time, ":current_hours_3"),
			(try_end),
			(try_begin),
				(neq, ":var_6", ":faction_ai_state"),
				(store_current_hours, ":current_hours_3"),
				(faction_set_slot, ":faction", slot_faction_ai_current_state_started, ":current_hours_3"),
			(try_end),
			(call_script, "script_evaluate_realm_stability", ":faction"),
			(assign, ":var_18", reg0),
			(assign, ":var_19", reg1),
			(faction_get_slot, ":faction_last_feast_concluded", ":faction", slot_faction_last_feast_concluded),
			(store_sub, ":value_2", ":current_hours", ":faction_last_feast_concluded"),
			(val_sub, ":value_2", 72),
			(faction_get_slot, ":faction_ai_current_state_started", ":faction", slot_faction_ai_current_state_started),
			(store_sub, ":current_hours_2", ":current_hours", ":faction_ai_current_state_started"),
			(faction_get_slot, ":faction_ai_last_offensive_time", ":faction", slot_faction_ai_last_offensive_time),
			(store_sub, ":value_3", ":current_hours", ":faction_ai_last_offensive_time"),
			(faction_get_slot, ":faction_ai_last_rest_time", ":faction", slot_faction_ai_last_rest_time),
			(store_sub, ":value_4", ":current_hours", ":faction_ai_last_rest_time"),
			(faction_get_slot, ":faction_ai_last_decisive_event", ":faction", slot_faction_ai_last_decisive_event),
			(store_sub, ":value_5", ":current_hours", ":faction_ai_last_decisive_event"),
			(assign, reg3, ":current_hours_2"),
			(assign, reg4, ":value_3"),
			(assign, reg5, ":value_2"),
			(assign, reg7, ":var_18"),
			(assign, reg8, ":var_19"),
			(assign, reg9, ":value_4"),
			(assign, reg10, ":value_5"),
			(str_store_string, 14, 26),
			(str_store_string, 9, "str_s9s10_current_state_s11_hours_at_current_state_reg3_current_strategic_thinking_s14_marshall_s12_since_the_last_offensive_ended_reg4_hours_since_the_decisive_event_reg10_hours_since_the_last_rest_reg9_hours_since_the_last_feast_ended_reg5_hours_percent_disgruntled_lords_reg7_percent_restless_lords_reg8__"),
		(try_end),
		(try_begin),
			(neg|is_between, "$g_cheat_selected_faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(call_script, "script_get_next_active_kingdom", "fac_kingdoms_end"),
			(assign, "$g_cheat_selected_faction", reg0),
		(try_end),
		(str_store_faction_name, 10, "$g_cheat_selected_faction"),
		(str_store_string, 9, "@Selected faction is: {s10}^^{s9}")
	],
	[
		("faction_orders_next_faction",
		[],
		"{!}Select next faction.",
		[
			(call_script, "script_get_next_active_kingdom", "$g_cheat_selected_faction"),
			(assign, "$g_cheat_selected_faction", reg0),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_political_collapse",
		[],
		"{!}CHEAT - Cause all lords in faction to fall out with their liege.",
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$g_cheat_selected_faction"),
				(faction_get_slot, ":faction_of_troop_troop_leader", ":faction_of_troop_troop", slot_faction_leader),
				(call_script, "script_troop_change_relation_with_troop", ":troop", ":faction_of_troop_troop_leader", -200),
			(try_end)
		], "."),

		("faction_orders_defend",
		[],
		"{!}Force defend.",
		[
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, 0),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_feast",
		[],
		"{!}Force feast.",
		[
			(assign, ":value", 0),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(neg|party_slot_ge, ":party", 54, 1),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$g_cheat_selected_faction"),
				(party_get_slot, ":party_town_lord", ":party", slot_town_lord),
				(troop_get_slot, ":party_town_lord_renown", ":party_town_lord", slot_troop_renown),
				(store_random_in_range, ":random_in_range_0_1000", 0, 1000),
				(val_add, ":party_town_lord_renown", ":random_in_range_0_1000"),
				(gt, ":party_town_lord_renown", ":value"),
				(assign, ":value", ":party_town_lord_renown"),
				(assign, ":var_7", ":party"),
			(try_end),
			(try_begin),
				(gt, ":var_7", "p_town_1_1"),
				(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, 6),
				(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, ":var_7"),
				(try_begin),
					(eq, "$g_player_eligible_feast_center_no", ":var_7"),
					(assign, "$g_player_eligible_feast_center_no", -1),
				(try_end),
				(store_current_hours, ":current_hours"),
				(faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_feast_concluded, ":current_hours"),
			(try_end),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_gather",
		[],
		"{!}Force gather army.",
		[
			(store_current_hours, ":current_hours"),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, 1),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time, ":current_hours"),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_offensive_max_followers, 1),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_increase_time",
		[],
		"{!}Increase last offensive time by 24 hours.",
		[
			(faction_get_slot, ":g_cheat_selected_faction_ai_last_offensive_time", "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time),
			(val_sub, ":g_cheat_selected_faction_ai_last_offensive_time", 24),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time, ":g_cheat_selected_faction_ai_last_offensive_time"),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_rethink",
		[],
		"{!}Force rethink.",
		[
			(call_script, "script_init_ai_calculation"),
			(call_script, "script_decide_faction_ai", "$g_cheat_selected_faction"),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_rethink_all",
		[],
		"{!}Force rethink for all factions.",
		[
			(call_script, "script_recalculate_ais"),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("enable_alt_ai",
		[
			(eq, "$g_use_alternative_ai", 2)
		],
		"{!}CHEAT! - enable alternative ai",
		[
			(assign, "$g_use_alternative_ai", 1),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("disable_alt_ai",
		[
			(eq, "$g_use_alternative_ai", 2)
		],
		"{!}CHEAT! - disable alternative ai",
		[
			(assign, "$g_use_alternative_ai", 0),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("faction_orders_init_econ",
		[],
		"{!}Initialize economic stats.",
		[
			(call_script, "script_initialize_economic_information"),
			(jump_to_menu, "mnu_faction_orders")
		], "."),

		("go_back_dot",
		[],
		"{!}Go back.",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("character_report", 0, "{s9}",
"none",
	[
		(try_begin),
			(gt, "$g_player_reading_book", 0),
			(player_has_item, "$g_player_reading_book"),
			(str_store_item_name, 8, "$g_player_reading_book"),
			(str_store_string, 9, "@You are currently reading {s8}."),
		(else_try),
			(assign, "$g_player_reading_book", 0),
			(str_store_string, 9, "@You are not reading any books."),
		(try_end),
		(assign, ":var_1", 0),
		(assign, ":var_2", 0),
		(str_store_string, 6, "@none"),
		(str_store_string, 8, "@none"),
		(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
			(this_or_next|troop_slot_eq, ":troop", slot_troop_occupation, 2),
			(troop_slot_eq, ":troop", slot_troop_occupation, 9),
			(call_script, "script_troop_get_player_relation", ":troop"),
			(assign, ":var_4", reg0),
			(try_begin),
				(gt, ":var_4", 20),
				(try_begin),
					(eq, ":var_1", 0),
					(str_store_troop_name, 8, ":troop"),
				(else_try),
					(eq, ":var_1", 1),
					(str_store_troop_name, 7, ":troop"),
					(str_store_string, 8, "@{s7} and {s8}"),
				(else_try),
					(str_store_troop_name, 7, ":troop"),
					(str_store_string, 8, "@{!}{s7}, {s8}"),
				(try_end),
				(val_add, ":var_1", 1),
			(else_try),
				(lt, ":var_4", -20),
				(try_begin),
					(eq, ":var_2", 0),
					(str_store_troop_name, 6, ":troop"),
				(else_try),
					(eq, ":var_2", 1),
					(str_store_troop_name, 5, ":troop"),
					(str_store_string, 6, "@{s5} and {s6}"),
				(else_try),
					(str_store_troop_name, 5, ":troop"),
					(str_store_string, 6, "@{!}{s5}, {s6}"),
				(try_end),
				(val_add, ":var_2", 1),
			(try_end),
		(try_end),
		(str_clear, 12),
		(try_begin),
			(gt, "$player_right_to_rule", 0),
			(assign, reg12, "$player_right_to_rule"),
			(str_store_string, 12, "str__right_to_rule_reg12"),
		(try_end),
		(str_clear, 15),
		(try_begin),
			(this_or_next|gt, "$claim_arguments_made", 0),
			(this_or_next|gt, "$ruler_arguments_made", 0),
			(this_or_next|gt, "$victory_arguments_made", 0),
			(this_or_next|gt, "$lords_arguments_made", 0),
			(eq, 1, 0),
			(assign, reg3, "$claim_arguments_made"),
			(assign, reg4, "$ruler_arguments_made"),
			(assign, reg5, "$victory_arguments_made"),
			(assign, reg6, "$lords_arguments_made"),
			(assign, reg7, "$benefit_arguments_made"),
			(str_store_string, 15, "str_political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7"),
		(try_end),
		(assign, reg3, "$player_honor"),
		(troop_get_slot, reg2, "trp_player", slot_troop_renown),
		(str_store_string, 9, "str_renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9"),
		(call_script, "script_get_number_of_hero_centers", "trp_player"),
		(assign, ":var_5", reg0),
		(try_begin),
			(gt, ":var_5", 0),
			(try_for_range, ":localvariable", 0, ":var_5"),
				(call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":localvariable"),
				(assign, ":var_7", reg0),
				(try_begin),
					(eq, ":localvariable", 0),
					(str_store_party_name, 8, ":var_7"),
				(else_try),
					(eq, ":localvariable", 1),
					(str_store_party_name, 7, ":var_7"),
					(str_store_string, 8, "@{s7} and {s8}"),
				(else_try),
					(str_store_party_name, 7, ":var_7"),
					(str_store_string, 8, "@{!}{s7}, {s8}"),
				(try_end),
			(try_end),
			(str_store_string, 9, "@Your estates are: {s8}.^{s9}"),
		(try_end),
		(try_begin),
			(gt, "$players_kingdom", 0),
			(str_store_faction_name, 8, "$players_kingdom"),
			(try_begin),
				(this_or_next|is_between, "$players_kingdom", "fac_kingdom_1", "fac_kingdoms_end"),
				(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				(str_store_string, 9, "str_you_are_a_lord_lady_of_s8_s9"),
			(else_try),
				(str_store_string, 9, "str_you_are_king_queen_of_s8_s9"),
			(try_end),
		(try_end)
	],
	[
		("continue",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! - increase Right to Rule",
		[
			(val_add, "$player_right_to_rule", 10),
			(jump_to_menu, "mnu_character_report")
		], "."),

		("continue",
		[
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, 14, "$g_talk_troop")
		],
		"{!}CHEAT! - increase your relation with {s14}",
		[
			(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
			(jump_to_menu, "mnu_character_report")
		], "."),

		("continue",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! - increase honor",
		[
			(val_add, "$player_honor", 10),
			(jump_to_menu, "mnu_character_report")
		], "."),

		("continue",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! - increase renown",
		[
			(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
			(val_add, ":player_renown", 50),
			(troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
			(jump_to_menu, "mnu_character_report")
		], "."),

		("continue",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! - increase persuasion",
		[
			(troop_raise_skill, "trp_player", "skl_persuasion", 1),
			(jump_to_menu, "mnu_character_report")
		], "."),

		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("party_size_report", 0, "{s1}",
"none",
	[
		(call_script, "script_game_get_party_companion_limit"),
		(assign, ":var_1", reg0),
		(store_skill_level, ":skill_level_leadership_player", "skl_leadership", "trp_player"),
		(val_mul, ":skill_level_leadership_player", 5),
		(store_attribute_level, ":attribute_level_player_3", "trp_player", 3),
		(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		(val_div, ":player_renown", 25),
		(try_begin),
			(gt, ":skill_level_leadership_player", 0),
			(str_store_string, 2, "@{!} +"),
		(else_try),
			(str_store_string, 2, "str_space"),
		(try_end),
		(try_begin),
			(gt, ":attribute_level_player_3", 0),
			(str_store_string, 3, "@{!} +"),
		(else_try),
			(str_store_string, 3, "str_space"),
		(try_end),
		(try_begin),
			(gt, ":player_renown", 0),
			(str_store_string, 4, "@{!} +"),
		(else_try),
			(str_store_string, 4, "str_space"),
		(try_end),
		(assign, reg5, ":var_1"),
		(assign, reg1, ":skill_level_leadership_player"),
		(assign, reg2, ":attribute_level_player_3"),
		(assign, reg3, ":player_renown"),
		(str_store_string, 1, "@Current party size limit is {reg5}.^Current party size modifiers are:^^Base size:  +70^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^TOTAL:  {reg5}")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("faction_relations_report", 0, "{s1}",
"none",
	[
		(str_clear, 2),
		(try_for_range, ":faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(faction_slot_eq, ":faction", slot_faction_state, 0),
			(neq, ":faction", "fac_player_supporters_faction"),
			(store_relation, ":relation_player_supporters_faction_faction", "fac_player_supporters_faction", ":faction"),
			(try_begin),
				(ge, ":relation_player_supporters_faction_faction", 90),
				(str_store_string, 3, "@Loyal"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 80),
				(str_store_string, 3, "@Devoted"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 70),
				(str_store_string, 3, "@Fond"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 60),
				(str_store_string, 3, "@Gracious"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 50),
				(str_store_string, 3, "@Friendly"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 40),
				(str_store_string, 3, "@Supportive"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 30),
				(str_store_string, 3, "@Favorable"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 20),
				(str_store_string, 3, "@Cooperative"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 10),
				(str_store_string, 3, "@Accepting"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", 0),
				(str_store_string, 3, "@Indifferent"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -10),
				(str_store_string, 3, "@Suspicious"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -20),
				(str_store_string, 3, "@Grumbling"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -30),
				(str_store_string, 3, "@Hostile"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -40),
				(str_store_string, 3, "@Resentful"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -50),
				(str_store_string, 3, "@Angry"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -60),
				(str_store_string, 3, "@Hateful"),
			(else_try),
				(ge, ":relation_player_supporters_faction_faction", -70),
				(str_store_string, 3, "@Revengeful"),
			(else_try),
				(str_store_string, 3, "@Vengeful"),
			(try_end),
			(str_store_faction_name, 4, ":faction"),
			(assign, reg1, ":relation_player_supporters_faction_faction"),
			(str_store_string, 2, "@{!}{s2}^{s4}: {reg1} ({s3})"),
		(try_end),
		(str_store_string, 1, "@Your relation with the factions are:^{s2}")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("camp", 0, "You set up camp. What do you want to do?",
"none",
	[
		(assign, "$g_player_icon_state", 0),
		(set_background_mesh, "mesh_pic_camp")
	],
	[
		("camp_action_1",
		[],
		"Walk around.",
		[
			(set_jump_mission, "mt_ai_training"),
			(call_script, "script_setup_random_scene"),
			(change_screen_mission)
		], "."),

		("camp_disband_lances",
		[
			(eq, "$use_feudal_lance", 1)
		],
		"Disband lance forces.",
		[
			(assign, "$g_next_menu", "mnu_camp"),
			(jump_to_menu, "mnu_disband_lances")
		], "."),

		("camp_reblance",
		[],
		"Troop rebalancing options",
		[
			(jump_to_menu, "mnu_mod_troop_rebalance")
		], "."),

		("action_export_import",
		[],
		"Export/Import NPCs.",
		[
			(assign, "$g_player_troop", "trp_player"),
			(jump_to_menu, "mnu_export_import_npcs")
		], "."),

		("action_mod_options",
		[],
		"Mod Options",
		[
			(start_presentation, "prsnt_mod_options")
		], "."),

		("action_faction_colours",
		[],
		"Change faction colours",
		[
			(start_presentation, "prsnt_change_all_factions_color")
		], "."),

		("camp_manage_inventory",
		[
			(assign, ":var_1", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(is_between, ":party_stack_troop_id_main_party_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(val_add, ":var_1", 1),
			(try_end),
			(gt, ":var_1", 0)
		],
		"Manage your party's inventory.",
		[
			(troop_clear_inventory, "trp_temp_troop"),
			(assign, "$return_menu", "mnu_camp"),
			(assign, "$inventory_menu_offset", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(is_between, ":party_stack_troop_id_main_party_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(call_script, "script_transfer_inventory", ":party_stack_troop_id_main_party_localvariable", "trp_temp_troop", 0),
			(try_end),
			(troop_sort_inventory, "trp_temp_troop"),
			(jump_to_menu, "mnu_manage_loot_pool")
		], "."),

		("camp_action",
		[],
		"Take an action.",
		[
			(jump_to_menu, "mnu_camp_action")
		], "."),

		("camp_wait_here",
		[],
		"Wait here for some time.",
		[
			(assign, "$g_camp_mode", 1),
			(assign, "$g_infinite_camping", 0),
			(assign, "$g_player_icon_state", 1),
			(rest_for_hours_interactive, 8760, 5, 1),
			(try_begin),
				(party_is_active, "p_main_party"),
				(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
				(try_begin),
					(eq, ":current_terrain_main_party", 5),
					(unlock_achievement, 28),
				(try_end),
			(try_end),
			(change_screen_return)
		], "."),

		("camp_cheat",
		[
			(ge, "$cheat_mode", 1)
		],
		"CHEAT MENU!",
		[
			(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("resume_travelling",
		[],
		"Resume travelling.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("mod_troop_rebalance", 0, "This was a feature for vanilla 1257. {s10}^^  It serves no purpose for modded 1257.^^ Be sure to disable this option as well as shield bashing.^^ To turn off this feature you need to reload the game (it will not affect the save game in any way). It's required you to do so, in order for the game engine to reload the troop equipment from the mod files. Leave this off.",
"none",
	[
		(try_begin),
			(eq, "$culture_pool", 0),
			(str_store_string, 10, "@Currently this feature is turned off. "),
		(else_try),
			(str_store_string, 10, "@Currently this feature is turned on. "),
		(try_end)
	],
	[
		("turn_on",
		[
			(eq, "$culture_pool", 0)
		],
		"Turn troop rebalancing on",
		[
			(try_begin),
				(eq, "$culture_pool_initialized", 0),
				(call_script, "script_initialize_culture_pools"),
				(assign, "$culture_pool_initialized", 1),
			(try_end),
			(assign, "$culture_pool", 1),
			(call_script, "script_rebalance_troops_by_culture")
		], "."),

		("turn_off",
		[
			(eq, "$culture_pool", 1)
		],
		"Turn troop rebalancing off (You will need to reload the game for this to take effect)",
		[
			(assign, "$culture_pool", 0)
		], "."),

		("back_to_camp_menu",
		[],
		"Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("camp_cheat", 0, "Select a cheat:",
"none",
	[],
	[
		("camp_cheat_find_item",
		[],
		"Find an item...",
		[
			(jump_to_menu, "mnu_cheat_find_item")
		], "."),

		("camp_cheat_find_item",
		[],
		"Change weather..",
		[
			(jump_to_menu, "mnu_cheat_change_weather")
		], "."),

		("camp_cheat_1",
		[],
		"{!}Increase player renown.",
		[
			(str_store_string, 1, "@Player renown is increased by 100. "),
			(call_script, "script_change_troop_renown", "trp_player", 100),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("camp_cheat_2",
		[],
		"{!}Increase player honor.",
		[
			(assign, reg7, "$player_honor"),
			(val_add, reg7, 1),
			(display_message, "@Player honor is increased by 1 and it is now {reg7}."),
			(val_add, "$player_honor", 1),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("camp_cheat_3",
		[],
		"{!}Update political notes.",
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(call_script, "script_update_troop_political_notes", ":troop"),
			(try_end),
			(try_for_range, ":faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(call_script, "script_update_faction_political_notes", ":faction"),
			(try_end)
		], "."),

		("camp_cheat_4",
		[],
		"{!}Update troop notes.",
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(call_script, "script_update_troop_notes", ":troop"),
			(try_end),
			(try_for_range, ":troop_2", "trp_knight_1_1_wife", "trp_heroes_end"),
				(call_script, "script_update_troop_notes", ":troop_2"),
				(call_script, "script_update_troop_political_notes", ":troop_2"),
				(call_script, "script_update_troop_location_notes", ":troop_2", 0),
			(try_end)
		], "."),

		("camp_cheat_5",
		[],
		"{!}Scramble minstrels.",
		[
			(call_script, "script_update_tavern_minstrels")
		], "."),

		("camp_cheat_6",
		[],
		"{!}Infinite camp",
		[
			(assign, "$g_camp_mode", 1),
			(assign, "$g_infinite_camping", 1),
			(assign, "$g_player_icon_state", 1),
			(rest_for_hours_interactive, 87600, 60),
			(change_screen_return)
		], "."),

		("cheat_faction_orders",
		[
			(ge, "$cheat_mode", 1)
		],
		"{!}Cheat: Set Debug messages to All.",
		[
			(assign, "$cheat_mode", 1),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("cheat_faction_orders",
		[
			(ge, "$cheat_mode", 1),
			(neq, "$cheat_mode", 3)
		],
		"{!}Cheat: Set Debug messages to Econ Only.",
		[
			(assign, "$cheat_mode", 3),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("cheat_faction_orders",
		[
			(ge, "$cheat_mode", 1),
			(neq, "$cheat_mode", 4)
		],
		"{!}Cheat: Set Debug messages to Political Only.",
		[
			(assign, "$cheat_mode", 4),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("back_to_camp_menu",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("cheat_find_item", 0, "{!}Current item range: {reg5} to {reg6}",
"none",
	[
		(assign, reg5, "$cheat_find_item_range_begin"),
		(store_add, reg6, "$cheat_find_item_range_begin", 96),
		(val_min, reg6, "itm_items_end_"),
		(val_sub, reg6, 1)
	],
	[
		("cheat_find_item_next_range",
		[],
		"{!}Move to next item range.",
		[
			(val_add, "$cheat_find_item_range_begin", 96),
			(try_begin),
				(ge, "$cheat_find_item_range_begin", "itm_items_end_"),
				(assign, "$cheat_find_item_range_begin", 0),
			(try_end),
			(jump_to_menu, "mnu_cheat_find_item")
		], "."),

		("cheat_find_item_choose_this",
		[],
		"{!}Choose from this range.",
		[
			(troop_clear_inventory, "trp_find_item_cheat"),
			(store_add, ":value", "$cheat_find_item_range_begin", 96),
			(val_min, ":value", "itm_items_end_"),
			(store_sub, ":value_2", ":value", "$cheat_find_item_range_begin"),
			(try_for_range, ":localvariable", 0, ":value_2"),
				(store_add, ":value_3", "$cheat_find_item_range_begin", ":localvariable"),
				(troop_add_items, "trp_find_item_cheat", ":value_3", 1),
			(try_end),
			(change_screen_trade, "trp_find_item_cheat")
		], "."),

		("camp_action_4",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("cheat_change_weather", 0, "{!}Current cloud amount: {reg5}^Current Fog Strength: {reg6}",
"none",
	[
		(get_global_cloud_amount, reg5),
		(get_global_haze_amount, reg6)
	],
	[
		("cheat_increase_cloud",
		[],
		"{!}Increase Cloud Amount.",
		[
			(get_global_cloud_amount, ":global_cloud_amount"),
			(val_add, ":global_cloud_amount", 5),
			(val_min, ":global_cloud_amount", 100),
			(set_global_cloud_amount, ":global_cloud_amount")
		], "."),

		("cheat_decrease_cloud",
		[],
		"{!}Decrease Cloud Amount.",
		[
			(get_global_cloud_amount, ":global_cloud_amount"),
			(val_sub, ":global_cloud_amount", 5),
			(val_max, ":global_cloud_amount", 0),
			(set_global_cloud_amount, ":global_cloud_amount")
		], "."),

		("cheat_increase_fog",
		[],
		"{!}Increase Fog Amount.",
		[
			(get_global_haze_amount, ":global_haze_amount"),
			(val_add, ":global_haze_amount", 5),
			(val_min, ":global_haze_amount", 100),
			(set_global_haze_amount, ":global_haze_amount")
		], "."),

		("cheat_decrease_fog",
		[],
		"{!}Decrease Fog Amount.",
		[
			(get_global_haze_amount, ":global_haze_amount"),
			(val_sub, ":global_haze_amount", 5),
			(val_max, ":global_haze_amount", 0),
			(set_global_haze_amount, ":global_haze_amount")
		], "."),

		("camp_action_4",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("camp_action", 0, "Choose an action:",
"none",
	[],
	[
		("camp_recruit_prisoners",
		[
			(troops_can_join, 1),
			(store_current_hours, ":current_hours"),
			(val_sub, ":current_hours", 24),
			(gt, ":current_hours", "$g_prisoner_recruit_last_time"),
			(try_begin),
				(gt, "$g_prisoner_recruit_last_time", 0),
				(assign, "$g_prisoner_recruit_troop_id", 0),
				(assign, "$g_prisoner_recruit_size", 0),
				(assign, "$g_prisoner_recruit_last_time", 0),
			(try_end)
		],
		"Recruit some of your prisoners to your party.",
		[
			(jump_to_menu, "mnu_camp_recruit_prisoners")
		], "."),

		("action_read_book",
		[],
		"Select a book to read.",
		[
			(jump_to_menu, "mnu_camp_action_read_book")
		], "."),

		("action_rename_kingdom",
		[
			(eq, "$players_kingdom_name_set", 1),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, 0),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player")
		],
		"Rename your kingdom.",
		[
			(start_presentation, "prsnt_name_kingdom")
		], "."),

		("action_modify_banner",
		[],
		"{!}Modify your banner.",
		[
			(start_presentation, "prsnt_banner_selection")
		], "."),

		("action_retire",
		[],
		"Retire from adventuring.",
		[
			(jump_to_menu, "mnu_retirement_verify")
		], "."),

		("camp_action_4",
		[],
		"Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("camp_recruit_prisoners", 0, "You offer your prisoners freedom if they agree to join you as soldiers. {s18}",
"none",
	[
		(assign, ":value", 0),
		(party_get_num_prisoner_stacks, ":num_prisoner_stacks_main_party", "p_main_party"),
		(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_main_party"),
			(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
			(neg|troop_is_hero, ":party_prisoner_stack_troop_id_main_party_localvariable"),
			(val_add, ":value", 1),
		(try_end),
		(try_begin),
			(eq, ":value", 0),
			(jump_to_menu, "mnu_camp_no_prisoners"),
		(else_try),
			(eq, "$g_prisoner_recruit_troop_id", 0),
			(store_current_hours, "$g_prisoner_recruit_last_time"),
			(store_random_in_range, ":random_in_range_11_100", 11, 100),
			(store_skill_level, ":skill_level_persuasion_player", "skl_persuasion", "trp_player"),
			(store_sub, ":value_2", 15, ":skill_level_persuasion_player"),
			(val_mul, ":value_2", 4),
			(try_begin),
				(lt, ":random_in_range_11_100", ":value_2"),
				(assign, "$g_prisoner_recruit_troop_id", -7),
			(else_try),
				(assign, ":value", 0),
				(party_get_num_prisoner_stacks, ":num_prisoner_stacks_main_party", "p_main_party"),
				(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_main_party"),
					(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
					(neg|troop_is_hero, ":party_prisoner_stack_troop_id_main_party_localvariable"),
					(val_add, ":value", 1),
				(try_end),
				(store_random_in_range, ":random_in_range_0_value", 0, ":value"),
				(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_main_party"),
					(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
					(neg|troop_is_hero, ":party_prisoner_stack_troop_id_main_party_localvariable"),
					(val_sub, ":random_in_range_0_value", 1),
					(lt, ":random_in_range_0_value", 0),
					(assign, ":num_prisoner_stacks_main_party", 0),
					(assign, "$g_prisoner_recruit_troop_id", ":party_prisoner_stack_troop_id_main_party_localvariable"),
					(party_prisoner_stack_get_size, "$g_prisoner_recruit_size", "p_main_party", ":localvariable"),
				(try_end),
			(try_end),
			(try_begin),
				(gt, "$g_prisoner_recruit_troop_id", 0),
				(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
				(val_min, "$g_prisoner_recruit_size", ":free_companions_capacity_main_party"),
				(assign, reg1, "$g_prisoner_recruit_size"),
				(gt, "$g_prisoner_recruit_size", 0),
				(try_begin),
					(gt, "$g_prisoner_recruit_size", 1),
					(assign, reg2, 1),
				(else_try),
					(assign, reg2, 0),
				(try_end),
				(str_store_troop_name_by_count, 1, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
				(str_store_string, 18, "@{reg1} {s1} {reg2?accept:accepts} the offer."),
			(else_try),
				(str_store_string, 18, "@No one accepts the offer."),
			(try_end),
		(try_end)
	],
	[
		("camp_recruit_prisoners_accept",
		[
			(gt, "$g_prisoner_recruit_troop_id", 0)
		],
		"Take them.",
		[
			(remove_troops_from_prisoners, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
			(party_add_members, "p_main_party", "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
			(store_mul, ":value", -1, "$g_prisoner_recruit_size"),
			(call_script, "script_change_player_party_morale", ":value"),
			(jump_to_menu, "mnu_camp")
		], "."),

		("camp_recruit_prisoners_reject",
		[
			(gt, "$g_prisoner_recruit_troop_id", 0)
		],
		"Reject them.",
		[
			(jump_to_menu, "mnu_camp"),
			(assign, "$g_prisoner_recruit_troop_id", 0),
			(assign, "$g_prisoner_recruit_size", 0)
		], "."),

		("continue",
		[
			(le, "$g_prisoner_recruit_troop_id", 0)
		],
		"Go back.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("camp_no_prisoners", 0, "You have no prisoners to recruit from.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("camp_action_read_book", 0, "Choose a book to read:",
"none",
	[],
	[
		("action_read_book_1",
		[
			(player_has_item, "itm_book_tactics"),
			(item_slot_eq, "itm_book_tactics", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_tactics")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_tactics"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("action_read_book_2",
		[
			(player_has_item, "itm_book_persuasion"),
			(item_slot_eq, "itm_book_persuasion", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_persuasion")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_persuasion"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("action_read_book_3",
		[
			(player_has_item, "itm_book_leadership"),
			(item_slot_eq, "itm_book_leadership", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_leadership")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_leadership"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("action_read_book_4",
		[
			(player_has_item, "itm_book_intelligence"),
			(item_slot_eq, "itm_book_intelligence", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_intelligence")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_intelligence"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("action_read_book_5",
		[
			(player_has_item, "itm_book_trade"),
			(item_slot_eq, "itm_book_trade", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_trade")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_trade"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("action_read_book_6",
		[
			(player_has_item, "itm_book_weapon_mastery"),
			(item_slot_eq, "itm_book_weapon_mastery", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_weapon_mastery")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_weapon_mastery"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("action_read_book_7",
		[
			(player_has_item, "itm_book_engineering"),
			(item_slot_eq, "itm_book_engineering", slot_item_book_read, 0),
			(str_store_item_name, 1, "itm_book_engineering")
		],
		"{s1}.",
		[
			(assign, "$temp", "itm_book_engineering"),
			(jump_to_menu, "mnu_camp_action_read_book_start")
		], "."),

		("camp_action_4",
		[],
		"Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("camp_action_read_book_start", 0, "{s1}",
"none",
	[
		(assign, ":var_1", "$temp"),
		(str_store_item_name, 2, ":var_1"),
		(try_begin),
			(store_attribute_level, ":attribute_level_player_2", "trp_player", 2),
			(item_get_slot, ":var_1_intelligence_requirement", ":var_1", slot_item_intelligence_requirement),
			(le, ":var_1_intelligence_requirement", ":attribute_level_player_2"),
			(str_store_string, 1, "@You start reading {s2}. After a few pages, you feel you could learn a lot from this book. You decide to keep it close by and read whenever you have the time."),
			(assign, "$g_player_reading_book", ":var_1"),
		(else_try),
			(str_store_string, 1, "@You flip through the pages of {s2}, but you find the text confusing and difficult to follow. Try as you might, it soon gives you a headache, and you're forced to give up the attempt."),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("retirement_verify", 0, "You are at day {reg0}. Your current luck is {reg1}. Are you sure you want to retire?",
"none",
	[
		(store_current_day, reg0),
		(assign, reg1, "$g_player_luck")
	],
	[
		("retire_yes",
		[],
		"Yes.",
		[
			(start_presentation, "prsnt_retirement")
		], "."),

		("retire_no",
		[],
		"No.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("end_game", 0, "The decision is made, and you resolve to give up your adventurer's life and settle down. You sell off your weapons and armour, gather up all your money, and ride off into the sunset....",
"none",
	[],
	[
		("end_game_bye",
		[],
		"Farewell.",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("cattle_herd", 0, "You encounter a herd of cattle.",
"none",
	[
		(play_sound, "snd_cow_moo"),
		(set_background_mesh, "mesh_pic_cattle")
	],
	[
		("cattle_drive_away",
		[],
		"Drive the cattle onward.",
		[
			(party_set_slot, "$g_encountered_party", slot_town_lord, 1),
			(party_set_ai_behavior, "$g_encountered_party", 10),
			(party_set_ai_object, "$g_encountered_party", "p_main_party"),
			(change_screen_return)
		], "."),

		("cattle_stop",
		[],
		"Bring the herd to a stop.",
		[
			(party_set_slot, "$g_encountered_party", slot_town_lord, 0),
			(party_set_ai_behavior, "$g_encountered_party", 0),
			(change_screen_return)
		], "."),

		("cattle_kill",
		[
			(assign, ":value", 1),
			(try_begin),
				(check_quest_active, "qst_move_cattle_herd"),
				(quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, "$g_encountered_party"),
				(assign, ":value", 0),
			(try_end),
			(eq, ":value", 1)
		],
		"Slaughter some of the animals.",
		[
			(jump_to_menu, "mnu_cattle_herd_kill")
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("cattle_herd_kill", 0, "How many animals do you want to slaughter?",
"none",
	[
		(party_get_num_companions, reg5, "$g_encountered_party")
	],
	[
		("cattle_kill_1",
		[
			(ge, reg5, 1)
		],
		"One.",
		[
			(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 1),
			(jump_to_menu, "mnu_cattle_herd_kill_end"),
			(change_screen_loot, "trp_temp_troop"),
			(play_sound, "snd_cow_slaughter")
		], "."),

		("cattle_kill_2",
		[
			(ge, reg5, 2)
		],
		"Two.",
		[
			(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 2),
			(jump_to_menu, "mnu_cattle_herd_kill_end"),
			(change_screen_loot, "trp_temp_troop"),
			(play_sound, "snd_cow_slaughter")
		], "."),

		("cattle_kill_3",
		[
			(ge, reg5, 3)
		],
		"Three.",
		[
			(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 3),
			(jump_to_menu, "mnu_cattle_herd_kill_end"),
			(change_screen_loot, "trp_temp_troop"),
			(play_sound, "snd_cow_slaughter")
		], "."),

		("cattle_kill_4",
		[
			(ge, reg5, 4)
		],
		"Four.",
		[
			(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 4),
			(jump_to_menu, "mnu_cattle_herd_kill_end"),
			(change_screen_loot, "trp_temp_troop"),
			(play_sound, "snd_cow_slaughter")
		], "."),

		("cattle_kill_5",
		[
			(ge, reg5, 5)
		],
		"Five.",
		[
			(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 5),
			(jump_to_menu, "mnu_cattle_herd_kill_end"),
			(change_screen_loot, "trp_temp_troop"),
			(play_sound, "snd_cow_slaughter")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_cattle_herd")
		], ".")
	]
	),

	("cattle_herd_kill_end", 0, "{!}You shouldn't be reading this.",
"none",
	[
		(change_screen_return)
	],
	[]
	),

	("arena_duel_fight", 0, "You and your opponent prepare to duel.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_leave_encounter", 0),
			(try_begin),
				(is_between, "$g_encountered_party", "p_town_1_1", "p_castle_1_1"),
				(party_get_slot, ":g_encountered_party_town_arena", "$g_encountered_party", slot_town_arena),
			(else_try),
				(eq, "$g_start_arena_fight_at_nearest_town", 1),
				(assign, ":value", -1),
				(assign, ":value_2", 10000),
				(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_party_g_encountered_party", ":party", "$g_encountered_party"),
					(lt, ":distance_to_party_from_party_party_g_encountered_party", ":value_2"),
					(assign, ":value_2", ":distance_to_party_from_party_party_g_encountered_party"),
					(assign, ":value", ":party"),
				(try_end),
				(try_begin),
					(ge, ":value", 0),
					(party_get_slot, ":g_encountered_party_town_arena", ":value", slot_town_arena),
				(try_end),
				(assign, "$g_start_arena_fight_at_nearest_town", 0),
			(else_try),
				(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
				(eq, ":current_terrain_main_party", 4),
				(assign, ":g_encountered_party_town_arena", "scn_training_ground_ranged_melee_3"),
			(else_try),
				(eq, ":current_terrain_main_party", 5),
				(assign, ":g_encountered_party_town_arena", "scn_training_ground_ranged_melee_4"),
			(else_try),
				(assign, ":g_encountered_party_town_arena", "scn_training_ground_ranged_melee_1"),
			(try_end),
			(modify_visitors_at_site, ":g_encountered_party_town_arena"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "$g_duel_troop"),
			(set_jump_mission, "mt_duel_with_lord"),
			(jump_to_scene, ":g_encountered_party_town_arena"),
			(jump_to_menu, "mnu_arena_duel_conclusion"),
			(change_screen_mission)
		], ".")
	]
	),

	("arena_duel_conclusion", 0, "{!}{s11}",
"none",
	[
		(try_begin),
			(eq, "$g_leave_encounter", 1),
			(change_screen_return),
		(try_end),
		(str_store_troop_name, 10, "$g_duel_troop"),
		(try_begin),
			(quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_failed, "qst_duel_for_lady"),
			(str_store_string, 11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_succeeded, "qst_duel_for_lady"),
			(str_store_string, 11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_failed, "qst_duel_courtship_rival"),
			(str_store_string, 11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_succeeded, "qst_duel_courtship_rival"),
			(str_store_string, 11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_succeeded, "qst_duel_avenge_insult"),
			(str_store_string, 11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_failed, "qst_duel_avenge_insult"),
			(str_store_string, 11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_succeeded, "qst_denounce_lord"),
			(str_store_string, 11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
		(else_try),
			(quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
			(check_quest_failed, "qst_denounce_lord"),
			(str_store_string, 11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
		(else_try),
			(str_store_troop_name, 10, "$g_duel_troop"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(call_script, "script_get_meeting_scene"),
			(assign, ":var_1", reg0),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 17, "$g_duel_troop"),
			(set_jump_mission, "mt_conversation_encounter"),
			(jump_to_scene, ":var_1"),
			(assign, "$talk_context", 17),
			(change_screen_map_conversation, "$g_duel_troop")
		], ".")
	]
	),

	("simple_encounter", 0, "{s2} You have {reg10} troops fit for battle against their {reg11}.",
"none",
	[
		(assign, "$g_enemy_party", "$g_encountered_party"),
		(assign, "$g_ally_party", -1),
		(call_script, "script_encounter_calculate_fit"),
		(try_begin),
			(eq, "$new_encounter", 1),
			(assign, "$new_encounter", 0),
			(assign, "$g_encounter_is_in_village", 0),
			(assign, "$g_encounter_type", 0),
			(try_begin),
				(party_slot_eq, "$g_enemy_party", slot_party_ai_state, 5),
				(party_get_slot, ":g_enemy_party_ai_object", "$g_enemy_party", slot_party_ai_object),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_g_enemy_party_ai_object_g_enemy_party", ":g_enemy_party_ai_object", "$g_enemy_party"),
				(try_begin),
					(lt, ":distance_to_party_from_party_g_enemy_party_ai_object_g_enemy_party", 4),
					(assign, "$g_encounter_is_in_village", ":g_enemy_party_ai_object"),
					(assign, "$g_encounter_type", 1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, "$g_player_sallies", "$g_encountered_party"),
				(assign, "$g_encounter_type", 3),
			(try_end),
			(try_begin),
				(gt, "$g_player_raiding_village", 0),
				(assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
				(assign, "$g_encounter_type", 2),
				(party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1),
				(str_store_string, 1, "@Villagers"),
				(display_message, "str_s1_joined_battle_enemy"),
			(else_try),
				(eq, "$g_encounter_type", 1),
				(party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0),
				(str_store_string, 1, "@Villagers"),
				(display_message, "str_s1_joined_battle_friend"),
			(else_try),
				(eq, "$g_encounter_type", 3),
				(party_quick_attach_to_current_battle, "$g_player_sally_town", 0),
				(str_store_string, 1, "@The garrison"),
				(display_message, "str_s1_joined_battle_friend"),
			(try_end),
			(try_begin),
				(call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
				(call_script, "script_encounter_init_variables"),
			(try_end),
			(assign, "$encountered_party_hostile", 0),
			(assign, "$encountered_party_friendly", 0),
			(try_begin),
				(gt, "$g_encountered_party_relation", 0),
				(assign, "$encountered_party_friendly", 1),
			(try_end),
			(try_begin),
				(lt, "$g_encountered_party_relation", 0),
				(assign, "$encountered_party_hostile", 1),
				(try_begin),
					(encountered_party_is_attacker),
					(assign, "$cant_leave_encounter", 1),
				(try_end),
			(try_end),
			(assign, "$talk_context", 2),
			(call_script, "script_setup_party_meeting", "$g_encountered_party"),
		(else_try),
			(try_begin),
				(eq, "$cant_leave_encounter", 1),
				(call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
				(assign, ":var_3", reg0),
				(call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
				(val_add, ":var_3", reg0),
				(call_script, "script_party_count_members_with_full_health", "p_main_party"),
				(assign, ":var_4", reg0),
				(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
				(val_add, ":var_4", reg0),
				(store_sub, ":value", ":var_3", 10),
				(lt, ":var_4", ":value"),
				(assign, "$cant_leave_encounter", 0),
			(try_end),
			(eq, "$g_leave_encounter", 1),
			(change_screen_return),
		(try_end),
		(try_begin),
			(party_is_active, "$g_encountered_party"),
			(str_store_party_name, 1, "$g_encountered_party"),
			(try_begin),
				(eq, "$g_encounter_type", 0),
				(str_store_string, 2, "@You have encountered {s1}."),
			(else_try),
				(eq, "$g_encounter_type", 1),
				(str_store_party_name, 3, "$g_encounter_is_in_village"),
				(str_store_string, 2, "@You have engaged {s1} while they were raiding {s3}."),
			(else_try),
				(eq, "$g_encounter_type", 2),
				(str_store_party_name, 3, "$g_encounter_is_in_village"),
				(str_store_string, 2, "@You were caught by {s1} while your forces were raiding {s3}."),
			(else_try),
				(eq, "$g_encounter_type", 3),
				(str_store_party_name, 3, "$g_player_sally_town"),
				(str_store_string, 2, "@You rally your forces and sally against {s1} to defend {s3}."),
			(try_end),
		(try_end),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
			(assign, ":var_6", reg0),
			(assign, ":value_2", 0),
			(try_begin),
				(eq, "$g_battle_result", 1),
				(this_or_next|le, ":var_6", 0),
				(le, ":var_6", "$num_routed_enemies"),
				(assign, ":value_2", 1),
			(else_try),
				(eq, "$g_engaged_enemy", 1),
				(this_or_next|le, ":var_6", 0),
				(le, "$g_enemy_fit_for_battle", "$num_routed_enemies"),
				(ge, "$g_friend_fit_for_battle", 1),
				(assign, ":value_2", 1),
			(try_end),
			(this_or_next|eq, ":value_2", 1),
			(eq, "$g_enemy_surrenders", 1),
			(assign, "$g_next_menu", -1),
			(jump_to_menu, "mnu_total_victory"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(assign, ":var_8", reg0),
			(assign, ":value_3", 0),
			(try_begin),
				(eq, "$g_battle_result", -1),
				(le, ":var_8", "$num_routed_us"),
				(assign, ":value_3", 1),
			(else_try),
				(eq, "$g_engaged_enemy", 1),
				(ge, "$g_enemy_fit_for_battle", 1),
				(le, "$g_friend_fit_for_battle", 0),
				(assign, ":value_3", 1),
			(try_end),
			(this_or_next|eq, ":value_3", 1),
			(eq, "$g_player_surrenders", 1),
			(assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
			(jump_to_menu, "mnu_total_defeat"),
		(try_end),
		(try_begin),
			(eq, "$g_encountered_party_template", "pt_looters"),
			(set_background_mesh, "mesh_pic_encounter_looters_new"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_mountain_bandits"),
			(set_background_mesh, "mesh_pic_encounter_mountain_bandits_new"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_steppe_bandits"),
			(set_background_mesh, "mesh_pic_steppe_bandits"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_robber_knights"),
			(set_background_mesh, "mesh_pic_roving_knights"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_desert_bandits"),
			(set_background_mesh, "mesh_pic_desert_bandits"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_taiga_bandits"),
			(set_background_mesh, "mesh_pic_tundra_bandits"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_sea_raiders"),
			(set_background_mesh, "mesh_pic_sea_raiders"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_forest_bandits"),
			(set_background_mesh, "mesh_pic_forest_bandits"),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_deserters"),
			(set_background_mesh, "mesh_pic_deserters"),
		(else_try),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(is_between, ":faction_of_party_g_encountered_party", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(faction_get_slot, ":faction_of_party_g_encountered_party_culture", ":faction_of_party_g_encountered_party", slot_faction_culture),
			(try_begin),
				(eq, ":faction_of_party_g_encountered_party_culture", 19),
				(set_background_mesh, "mesh_pic_encounter_iberians"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 20),
				(set_background_mesh, "mesh_pic_encounter_leuro"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 13),
				(set_background_mesh, "mesh_pic_encounter_rus"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 11),
				(set_background_mesh, "mesh_pic_encounter_teutonic"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 27),
				(set_background_mesh, "mesh_pic_encounter_mongol"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 15),
				(set_background_mesh, "mesh_pic_encounter_balt"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 14),
				(set_background_mesh, "mesh_pic_encounter_scand"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 10),
				(set_background_mesh, "mesh_pic_encounter_welsh"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 22),
				(set_background_mesh, "mesh_pic_encounter_irish"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 25),
				(set_background_mesh, "mesh_pic_encounter_scot"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 17),
				(set_background_mesh, "mesh_pic_encounter_mamluk"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 21),
				(set_background_mesh, "mesh_pic_encounter_andalus"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 18),
				(set_background_mesh, "mesh_pic_encounter_byz"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 9),
				(set_background_mesh, "mesh_pic_encounter_serbs"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 12),
				(set_background_mesh, "mesh_pic_encounter_bulgars"),
			(else_try),
				(eq, ":faction_of_party_g_encountered_party_culture", 16),
				(set_background_mesh, "mesh_pic_encounter_marrinid"),
			(else_try),
				(set_background_mesh, "mesh_pic_encounter_weuro"),
			(try_end),
		(try_end)
	],
	[
		("encounter_attack",
		[
			(eq, "$encountered_party_friendly", 0),
			(neg|troop_is_wounded, "trp_player"),
			(assign, ":value", 0),
			(try_begin),
				(call_script, "script_cf_is_party_on_water", "p_main_party"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 0)
		],
		"Charge the enemy.",
		[
			(assign, "$g_battle_result", 0),
			(assign, "$g_engaged_enemy", 1),
			(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
			(try_begin),
				(eq, ":template_id_l_g_encountered_party", "pt_village_farmers"),
				(unlock_achievement, 27),
			(try_end),
			(call_script, "script_calculate_renown_value"),
			(call_script, "script_calculate_battle_advantage"),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(try_begin),
				(eq, "$g_encounter_type", 1),
				(assign, "$g_village_raid_evil", 0),
				(set_jump_mission, "mt_village_raid"),
				(party_get_slot, ":g_encounter_is_in_village_town_center", "$g_encounter_is_in_village", slot_town_center),
				(jump_to_scene, ":g_encounter_is_in_village_town_center"),
			(else_try),
				(eq, "$g_encounter_type", 2),
				(assign, "$g_village_raid_evil", 0),
				(set_jump_mission, "mt_village_raid"),
				(party_get_slot, ":g_encounter_is_in_village_town_center", "$g_encounter_is_in_village", slot_town_center),
				(jump_to_scene, ":g_encounter_is_in_village_town_center"),
			(else_try),
				(eq, "$g_encounter_type", 3),
				(set_jump_mission, "mt_castle_attack_walls_defenders_sally_player"),
				(try_begin),
					(party_slot_eq, "$g_player_sally_town", slot_party_type, 3),
					(party_get_slot, ":g_encounter_is_in_village_town_center", "$g_player_sally_town", slot_town_walls),
				(else_try),
					(party_get_slot, ":g_encounter_is_in_village_town_center", "$g_player_sally_town", slot_town_center),
				(try_end),
				(assign, "$g_player_sally_town", -1),
				(assign, "$g_player_sallies", -1),
				(jump_to_scene, ":g_encounter_is_in_village_town_center"),
			(else_try),
				(set_jump_mission, "mt_lead_charge"),
				(call_script, "script_setup_random_scene"),
			(try_end),
			(assign, "$g_next_menu", "mnu_simple_encounter"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("encounter_attack",
		[
			(eq, "$encountered_party_friendly", 0),
			(neg|troop_is_wounded, "trp_player"),
			(call_script, "script_cf_is_party_on_water", "p_main_party")
		],
		"Close in and board the enemy.",
		[
			(assign, "$g_battle_result", 0),
			(assign, "$g_engaged_enemy", 1),
			(call_script, "script_calculate_renown_value"),
			(call_script, "script_calculate_battle_advantage"),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(set_jump_mission, "mt_ship_battle"),
			(assign, "$g_next_menu", "mnu_simple_encounter"),
			(jump_to_menu, "mnu_battle_debrief"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(call_script, "script_raf_aor_faction_to_region", ":faction_of_party_g_encountered_party"),
			(assign, ":var_2", reg0),
			(call_script, "script_raf_aor_faction_to_region", "$players_kingdom"),
			(assign, ":var_3", reg0),
			(assign, ":value", "scn_scene_sea"),
			(try_begin),
				(this_or_next|eq, ":var_2", 10),
				(this_or_next|eq, ":var_2", 12),
				(this_or_next|eq, ":var_2", 14),
				(eq, ":var_2", 11),
				(eq, ":var_3", 2),
				(assign, ":value", "scn_scene_sea_player_nord_vs_eastern"),
			(else_try),
				(this_or_next|eq, ":var_3", 10),
				(this_or_next|eq, ":var_3", 12),
				(this_or_next|eq, ":var_3", 14),
				(eq, ":var_3", 11),
				(eq, ":var_2", 2),
				(assign, ":value", "scn_scene_sea_player_eastern_vs_nordic"),
			(else_try),
				(eq, ":var_2", 2),
				(this_or_next|eq, ":var_3", 13),
				(this_or_next|eq, ":var_3", -1),
				(this_or_next|eq, ":var_3", 3),
				(this_or_next|eq, ":var_3", 15),
				(this_or_next|eq, ":var_3", 1),
				(this_or_next|eq, ":var_3", 5),
				(this_or_next|eq, ":var_3", 6),
				(this_or_next|eq, ":var_3", 7),
				(this_or_next|eq, ":var_3", 16),
				(eq, ":var_3", 8),
				(assign, ":value", "scn_scene_sea_player_generic_vs_nordic"),
			(else_try),
				(eq, ":var_3", 2),
				(this_or_next|eq, ":var_2", 13),
				(this_or_next|eq, ":var_2", -1),
				(this_or_next|eq, ":var_2", 3),
				(this_or_next|eq, ":var_2", 1),
				(this_or_next|eq, ":var_2", 5),
				(this_or_next|eq, ":var_2", 6),
				(this_or_next|eq, ":var_2", 7),
				(this_or_next|eq, ":var_2", 16),
				(eq, ":var_2", 8),
				(assign, ":value", "scn_scene_sea_player_nord_vs_generic"),
			(else_try),
				(this_or_next|eq, ":var_2", 10),
				(this_or_next|eq, ":var_2", 12),
				(this_or_next|eq, ":var_2", 14),
				(eq, ":var_2", 11),
				(this_or_next|eq, ":var_3", 13),
				(this_or_next|eq, ":var_3", -1),
				(this_or_next|eq, ":var_3", 3),
				(this_or_next|eq, ":var_3", 1),
				(this_or_next|eq, ":var_3", 5),
				(this_or_next|eq, ":var_3", 6),
				(this_or_next|eq, ":var_3", 7),
				(this_or_next|eq, ":var_3", 16),
				(eq, ":var_3", 8),
				(assign, ":value", "scn_scene_sea_player_generic_vs_eastern"),
			(else_try),
				(this_or_next|eq, ":var_3", 10),
				(this_or_next|eq, ":var_3", 12),
				(this_or_next|eq, ":var_3", 14),
				(eq, ":var_3", 11),
				(this_or_next|eq, ":var_2", 13),
				(this_or_next|eq, ":var_2", -1),
				(this_or_next|eq, ":var_2", 3),
				(this_or_next|eq, ":var_2", 1),
				(this_or_next|eq, ":var_2", 5),
				(this_or_next|eq, ":var_2", 6),
				(this_or_next|eq, ":var_2", 7),
				(this_or_next|eq, ":var_2", 16),
				(eq, ":var_2", 8),
				(assign, ":value", "scn_scene_sea_player_eastern_vs_generic"),
			(else_try),
				(assign, ":value", "scn_scene_sea"),
			(try_end),
			(jump_to_scene, ":value"),
			(change_screen_mission)
		], "."),

		("encounter_order_attack",
		[
			(eq, "$encountered_party_friendly", 0),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(ge, reg0, 4)
		],
		"Order your troops to attack without you.",
		[
			(jump_to_menu, "mnu_order_attack_begin")
		], "."),

		("encounter_leave",
		[
			(eq, "$cant_leave_encounter", 0)
		],
		"Leave.",
		[
			(try_begin),
				(eq, "$encountered_party_friendly", 0),
				(encountered_party_is_attacker),
				(call_script, "script_objectionable_action", 1, "str_flee_battle"),
			(try_end),
			(try_begin),
				(eq, "$encountered_party_friendly", 0),
				(party_get_num_companion_stacks, ":num_companion_stacks_encountered_party_backup", "p_encountered_party_backup"),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_encountered_party_backup"),
					(party_stack_get_troop_id, ":party_stack_troop_id_encountered_party_backup_localvariable", "p_encountered_party_backup", ":localvariable"),
					(is_between, ":party_stack_troop_id_encountered_party_backup_localvariable", "trp_npc1", "trp_knight_1_1_wife"),
					(troop_slot_eq, ":party_stack_troop_id_encountered_party_backup_localvariable", slot_troop_occupation, 2),
					(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_encountered_party_backup_localvariable", ":party_stack_troop_id_encountered_party_backup_localvariable"),
					(call_script, "script_add_log_entry", 15, "trp_player", -1, ":party_stack_troop_id_encountered_party_backup_localvariable", ":faction_of_troop_party_stack_troop_id_encountered_party_backup_localvariable"),
				(try_end),
			(try_end),
			(leave_encounter),
			(change_screen_return)
		], "."),

		("encounter_retreat",
		[
			(eq, "$cant_leave_encounter", 1),
			(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
			(assign, ":var_1", reg0),
			(val_add, ":var_1", 4),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
			(assign, ":var_2", reg0),
			(val_div, ":var_2", 2),
			(val_div, ":var_2", ":var_1"),
			(val_max, ":var_2", 1),
			(call_script, "script_party_count_fit_regulars", "p_main_party"),
			(assign, ":var_3", reg0),
			(ge, ":var_3", ":var_2")
		],
		"Pull back, leaving some soldiers behind to cover your retreat.",
		[
			(jump_to_menu, "mnu_encounter_retreat_confirm")
		], "."),

		("encounter_surrender",
		[
			(eq, "$cant_leave_encounter", 1)
		],
		"Surrender.",
		[
			(assign, "$g_player_surrenders", 1)
		], ".")
	]
	),

	("encounter_retreat_confirm", 0, "As the party member with the highest tactics skill, ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives, but you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase.",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
		(assign, ":var_1", reg0),
		(assign, ":var_2", reg1),
		(assign, reg2, ":var_1"),
		(val_add, ":var_1", 4),
		(call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
		(assign, ":var_3", reg0),
		(val_div, ":var_3", 2),
		(store_div, reg4, ":var_3", ":var_1"),
		(val_max, reg4, 1),
		(try_begin),
			(eq, ":var_2", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 3, ":var_2"),
		(try_end)
	],
	[
		("leave_behind",
		[],
		"Go on. The sacrifice of these men will save the rest.",
		[
			(assign, ":var_1", reg4),
			(try_for_range, ":unused", 0, ":var_1"),
				(call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
				(assign, ":var_3", reg0),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(ge, ":random_in_range_0_100", 30),
				(party_add_prisoners, "$g_encountered_party", ":var_3", 1),
			(try_end),
			(call_script, "script_change_player_party_morale", -20),
			(jump_to_menu, "mnu_encounter_retreat")
		], "."),

		("dont_leave_behind",
		[],
		"No. We leave no one behind.",
		[
			(jump_to_menu, "mnu_simple_encounter")
		], ".")
	]
	),

	("encounter_retreat", 0, "You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(call_script, "script_objectionable_action", 1, "str_flee_battle"),
			(party_get_num_companion_stacks, ":num_companion_stacks_encountered_party_backup", "p_encountered_party_backup"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_encountered_party_backup"),
				(party_stack_get_troop_id, ":party_stack_troop_id_encountered_party_backup_localvariable", "p_encountered_party_backup", ":localvariable"),
				(is_between, ":party_stack_troop_id_encountered_party_backup_localvariable", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":party_stack_troop_id_encountered_party_backup_localvariable", slot_troop_occupation, 2),
				(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_encountered_party_backup_localvariable", ":party_stack_troop_id_encountered_party_backup_localvariable"),
				(call_script, "script_add_log_entry", 16, "trp_player", -1, ":party_stack_troop_id_encountered_party_backup_localvariable", ":faction_of_troop_party_stack_troop_id_encountered_party_backup_localvariable"),
			(try_end),
			(party_ignore_player, "$g_encountered_party", 1),
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("order_attack_begin", 0, "Your troops prepare to attack the enemy.",
"none",
	[],
	[
		("order_attack_begin",
		[],
		"Order the attack to begin.",
		[
			(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
			(try_begin),
				(eq, ":template_id_l_g_encountered_party", "pt_village_farmers"),
				(unlock_achievement, 27),
			(try_end),
			(assign, "$g_engaged_enemy", 1),
			(jump_to_menu, "mnu_order_attack_2")
		], "."),

		("call_back",
		[],
		"Call them back.",
		[
			(jump_to_menu, "mnu_simple_encounter")
		], ".")
	]
	),

	("order_attack_2", 0, "{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}",
"none",
	[
		(set_background_mesh, "mesh_pic_charge"),
		(call_script, "script_party_calculate_strength", "p_main_party", 1),
		(assign, ":var_1", reg0),
		(call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
		(assign, ":var_2", reg0),
		(party_collect_attachments_to_party, "p_main_party", "p_collective_ally"),
		(call_script, "script_party_calculate_strength", "p_collective_ally", 1),
		(assign, ":var_3", reg0),
		(try_begin),
			(le, ":var_3", ":var_2"),
			(assign, ":value", ":var_3"),
		(else_try),
			(assign, ":value", ":var_2"),
		(try_end),
		(try_begin),
			(le, ":value", 5),
			(assign, ":value_2", 1),
		(else_try),
			(le, ":value", 10),
			(assign, ":value_2", 2),
		(else_try),
			(le, ":value", 25),
			(assign, ":value_2", 3),
		(else_try),
			(le, ":value", 500),
			(assign, ":value_2", 40),
		(else_try),
			(le, ":value", 1000),
			(assign, ":value_2", 50),
		(else_try),
			(le, ":value", 2000),
			(assign, ":value_2", 60),
		(else_try),
			(le, ":value", 4000),
			(assign, ":value_2", 70),
		(else_try),
			(le, ":value", 8000),
			(assign, ":value_2", 80),
		(else_try),
			(le, ":value", 16000),
			(assign, ":value_2", 90),
		(else_try),
			(le, ":value", 32000),
			(assign, ":value_2", 100),
		(else_try),
			(le, ":value", 64000),
			(assign, ":value_2", 110),
		(else_try),
			(le, ":value", 128000),
			(assign, ":value_2", 120),
		(else_try),
			(le, ":value", 256000),
			(assign, ":value_2", 130),
		(else_try),
			(le, ":value", 512000),
			(assign, ":value_2", 140),
		(else_try),
			(le, ":value", 1024000),
			(assign, ":value_2", 150),
		(else_try),
			(assign, ":value_2", 160),
		(try_end),
		(val_div, ":var_1", ":value_2"),
		(val_max, ":var_1", 1),
		(val_div, ":var_2", ":value_2"),
		(val_max, ":var_2", 1),
		(val_div, ":var_3", ":value_2"),
		(val_max, ":var_3", 1),
		(store_mul, "$g_strength_contribution_of_player", ":var_1", 100),
		(val_div, "$g_strength_contribution_of_player", ":var_3"),
		(inflict_casualties_to_party_group, "p_main_party", ":var_2", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 8, 0),
		(try_begin),
			(ge, "$g_ally_party", 0),
			(inflict_casualties_to_party_group, "$g_ally_party", ":var_2", "p_temp_casualties"),
			(str_store_string_reg, 8, 0),
		(try_end),
		(inflict_casualties_to_party_group, "$g_encountered_party", ":var_3", "p_temp_casualties"),
		(party_get_num_companion_stacks, ":num_companion_stacks_temp_casualties", "p_temp_casualties"),
		(try_for_range, ":localvariable", 0, ":num_companion_stacks_temp_casualties"),
			(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
			(try_begin),
				(party_stack_get_size, ":party_stack_size_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
				(gt, ":party_stack_size_temp_casualties_localvariable", 0),
				(party_add_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_casualties_localvariable", ":party_stack_size_temp_casualties_localvariable"),
				(party_stack_get_num_wounded, ":party_stack_num_wounded_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
				(gt, ":party_stack_num_wounded_temp_casualties_localvariable", 0),
				(party_wound_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_casualties_localvariable", ":party_stack_num_wounded_temp_casualties_localvariable"),
			(try_end),
		(try_end),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 9, 0),
		(party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),
		(assign, "$no_soldiers_left", 0),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(assign, ":var_11", reg0),
			(store_add, ":value_3", "$num_routed_us", 1),
			(le, ":var_11", ":value_3"),
			(assign, "$no_soldiers_left", 1),
			(str_store_string, 4, "str_order_attack_failure"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
			(assign, ":var_13", reg0),
			(this_or_next|le, ":var_13", 0),
			(le, ":var_13", "$num_routed_enemies"),
			(assign, ":value_4", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_collective_enemy", "p_collective_enemy"),
			(try_begin),
				(eq, ":num_companion_stacks_collective_enemy", 0),
				(assign, ":value_4", 1),
			(else_try),
				(party_stack_get_troop_id, ":party_stack_troop_id_collective_enemy_0", "p_collective_enemy", 0),
				(try_begin),
					(neg|troop_is_hero, ":party_stack_troop_id_collective_enemy_0"),
					(assign, ":value_4", 1),
				(else_try),
					(troop_is_wounded, ":party_stack_troop_id_collective_enemy_0"),
					(assign, ":value_4", 1),
				(try_end),
			(try_end),
			(eq, ":value_4", 1),
			(assign, "$g_battle_result", 1),
			(assign, "$no_soldiers_left", 1),
			(str_store_string, 4, "str_order_attack_success"),
		(else_try),
			(str_store_string, 4, "str_order_attack_continue"),
		(try_end)
	],
	[
		("order_attack_continue",
		[
			(eq, "$no_soldiers_left", 0)
		],
		"Order your soldiers to continue the attack.",
		[
			(jump_to_menu, "mnu_order_attack_2")
		], "."),

		("order_retreat",
		[
			(eq, "$no_soldiers_left", 0)
		],
		"Call your soldiers back.",
		[
			(jump_to_menu, "mnu_simple_encounter")
		], "."),

		("continue",
		[
			(eq, "$no_soldiers_left", 1)
		],
		"Continue...",
		[
			(jump_to_menu, "mnu_simple_encounter")
		], ".")
	]
	),

	("battle_debrief", 0, "{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}",
"none",
	[
		(set_fixed_point_multiplier, 100),
		(set_shader_param_float, "@vFresnelMultiplier", 15),
		(try_begin),
			(eq, "$auxilary_player_active", 1),
			(party_get_num_companion_stacks, ":num_companion_stacks_temp_casualties_3", "p_temp_casualties_3"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_temp_casualties_3"),
				(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_3_localvariable", "p_temp_casualties_3", ":localvariable"),
				(neq, ":party_stack_troop_id_temp_casualties_3_localvariable", "trp_player"),
				(neg|troop_is_hero, ":party_stack_troop_id_temp_casualties_3_localvariable"),
				(party_count_members_of_type, ":var_4", "p_main_party", ":party_stack_troop_id_temp_casualties_3_localvariable"),
				(party_count_members_of_type, ":var_5", "p_temp_casualties_3", ":party_stack_troop_id_temp_casualties_3_localvariable"),
				(try_begin),
					(gt, ":var_5", ":var_4"),
					(store_sub, ":value", ":var_5", ":var_4"),
					(party_add_members, "p_main_party", ":party_stack_troop_id_temp_casualties_3_localvariable", ":value"),
				(else_try),
					(lt, ":var_5", ":var_4"),
					(store_sub, ":value", ":var_4", ":var_5"),
					(party_remove_members, "p_main_party", ":party_stack_troop_id_temp_casualties_3_localvariable", ":value"),
				(try_end),
				(party_stack_get_num_wounded, ":party_stack_num_wounded_temp_casualties_3_localvariable", "p_temp_casualties_3", ":localvariable"),
				(party_stack_get_num_wounded, ":party_stack_num_wounded_main_party_localvariable", "p_main_party", ":localvariable"),
				(try_begin),
					(gt, ":party_stack_num_wounded_temp_casualties_3_localvariable", ":party_stack_num_wounded_main_party_localvariable"),
					(store_sub, ":value", ":party_stack_num_wounded_temp_casualties_3_localvariable", ":party_stack_num_wounded_main_party_localvariable"),
					(party_wound_members, "p_main_party", ":party_stack_troop_id_temp_casualties_3_localvariable", ":value"),
				(try_end),
			(try_end),
			(party_get_num_companion_stacks, ":num_companion_stacks_player_casualties", "p_player_casualties"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_player_casualties"),
				(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_3_localvariable", "p_player_casualties", ":localvariable"),
				(neq, ":party_stack_troop_id_temp_casualties_3_localvariable", "trp_player"),
				(neg|troop_is_hero, ":party_stack_troop_id_temp_casualties_3_localvariable"),
				(party_stack_get_size, ":party_stack_size_player_casualties_localvariable", "p_player_casualties", ":localvariable"),
				(party_stack_get_num_wounded, ":party_stack_num_wounded_player_casualties_localvariable", "p_player_casualties", ":localvariable"),
				(val_sub, ":party_stack_size_player_casualties_localvariable", ":party_stack_num_wounded_player_casualties_localvariable"),
				(party_remove_members, "p_main_party", ":party_stack_troop_id_temp_casualties_3_localvariable", ":party_stack_size_player_casualties_localvariable"),
				(party_wound_members, "p_main_party", ":party_stack_troop_id_temp_casualties_3_localvariable", ":party_stack_num_wounded_player_casualties_localvariable"),
			(try_end),
			(party_clear, "p_temp_casualties_3"),
			(assign, "$auxilary_player_active", 0),
		(try_end),
		(try_begin),
			(eq, "$g_battle_result", 1),
			(call_script, "script_change_troop_renown", "trp_player", "$battle_renown_value"),
			(try_begin),
				(ge, "$g_encountered_party", 0),
				(party_is_active, "$g_encountered_party"),
				(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
				(eq, ":template_id_l_g_encountered_party", "pt_kingdom_caravan_party"),
				(get_achievement_stat, ":achievement_stat_30_0", 30, 0),
				(get_achievement_stat, ":achievement_stat_30_1", 30, 1),
				(val_add, ":achievement_stat_30_1", 1),
				(set_achievement_stat, 30, 1, ":achievement_stat_30_1"),
				(try_begin),
					(ge, ":achievement_stat_30_0", 3),
					(ge, ":achievement_stat_30_1", 3),
					(unlock_achievement, 30),
				(try_end),
			(try_end),
			(try_begin),
				(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
				(eq, ":current_terrain_main_party", 4),
				(get_achievement_stat, ":achievement_stat_8_0", 8, 0),
				(val_add, ":achievement_stat_8_0", 1),
				(set_achievement_stat, 8, 0, ":achievement_stat_8_0"),
				(try_begin),
					(eq, ":achievement_stat_8_0", 10),
					(unlock_achievement, 8),
				(try_end),
			(try_end),
			(try_begin),
				(ge, "$g_enemy_party", 0),
				(party_is_active, "$g_enemy_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_3_localvariable", "$g_enemy_party", 0),
				(eq, ":party_stack_troop_id_temp_casualties_3_localvariable", "trp_mountain_bandit"),
				(get_achievement_stat, ":achievement_stat_13_0", 13, 0),
				(val_add, ":achievement_stat_13_0", 1),
				(set_achievement_stat, 13, 0, ":achievement_stat_13_0"),
				(try_begin),
					(eq, ":achievement_stat_13_0", 10),
					(unlock_achievement, 13),
				(try_end),
			(try_end),
			(try_begin),
				(is_between, "$g_ally_party", "p_town_1_1", "p_village_1_1"),
				(unlock_achievement, 1),
			(try_end),
			(try_begin),
				(eq, "$g_joined_battle_to_help", 1),
				(unlock_achievement, 34),
			(try_end),
		(try_end),
		(assign, "$g_joined_battle_to_help", 0),
		(call_script, "script_count_casualties_and_adjust_morale"),
		(call_script, "script_encounter_calculate_fit"),
		(call_script, "script_party_count_fit_regulars", "p_main_party"),
		(assign, "$playerparty_postbattle_regulars", reg0),
		(try_begin),
			(eq, "$g_battle_result", 1),
			(eq, "$g_enemy_fit_for_battle", 0),
			(str_store_string, 11, "@You were victorious!"),
			(try_begin),
				(gt, "$g_friend_fit_for_battle", 1),
				(set_background_mesh, "mesh_pic_victory"),
			(try_end),
		(else_try),
			(eq, "$g_battle_result", -1),
			(ge, "$g_enemy_fit_for_battle", 1),
			(this_or_next|le, "$g_friend_fit_for_battle", 0),
			(le, "$playerparty_postbattle_regulars", 0),
			(str_store_string, 11, "@Battle was lost. Your forces were utterly crushed."),
			(set_background_mesh, "mesh_pic_defeat"),
		(else_try),
			(eq, "$g_battle_result", -1),
			(str_store_string, 11, "@Your companions carry you away from the fighting."),
			(troop_get_type, ":type_player", "trp_player"),
			(try_begin),
				(eq, ":type_player", 1),
				(set_background_mesh, "mesh_pic_wounded_fem"),
			(else_try),
				(set_background_mesh, "mesh_pic_wounded"),
			(try_end),
		(else_try),
			(eq, "$g_battle_result", 1),
			(str_store_string, 11, "@You have defeated the enemy."),
			(try_begin),
				(gt, "$g_friend_fit_for_battle", 1),
				(set_background_mesh, "mesh_pic_victory"),
			(try_end),
		(else_try),
			(eq, "$g_battle_result", 0),
			(str_store_string, 11, "@You have retreated from the fight."),
		(try_end),
		(try_begin),
			(gt, "$playerparty_prebattle_regulars", 9),
			(store_add, ":value_2", 3, "$g_battle_result"),
			(store_div, ":value_3", "$playerparty_prebattle_regulars", ":value_2"),
			(lt, "$playerparty_postbattle_regulars", ":value_3"),
			(call_script, "script_objectionable_action", 2, "str_excessive_casualties"),
		(try_end),
		(call_script, "script_print_casualties_to_s0", "p_player_casualties", 0),
		(str_store_string_reg, 8, 0),
		(call_script, "script_print_casualties_to_s0", "p_enemy_casualties", 0),
		(str_store_string_reg, 9, 0),
		(str_clear, 10),
		(try_begin),
			(eq, "$any_allies_at_the_last_battle", 1),
			(call_script, "script_print_casualties_to_s0", "p_ally_casualties", 0),
			(str_store_string, 10, "@^^Ally Casualties:{s0}"),
		(try_end),
		(try_begin),
			(assign, reg20, "$killcount"),
			(assign, "$killcount", 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "$g_next_menu")
		], ".")
	]
	),

	("total_victory", 0, "You shouldn't be reading this... {s9}",
"none",
	[
		(assign, ":value", 0),
		(try_begin),
			(eq, "$routed_party_added", 0),
			(assign, "$routed_party_added", 1),
			(call_script, "script_add_routed_party"),
		(try_end),
		(try_begin),
			(check_quest_active, "qst_track_down_bandits"),
			(neg|check_quest_succeeded, "qst_track_down_bandits"),
			(neg|check_quest_failed, "qst_track_down_bandits"),
			(quest_get_slot, ":track_down_bandits_target_party", "qst_track_down_bandits", slot_quest_target_party),
			(party_is_active, ":track_down_bandits_target_party"),
			(party_get_attached_to, ":party_attached_to"),
			(this_or_next|eq, ":track_down_bandits_target_party", "$g_enemy_party"),
			(eq, ":party_attached_to", "$g_enemy_party"),
			(call_script, "script_succeed_quest", "qst_track_down_bandits"),
		(try_end),
		(try_begin),
			(gt, "$g_private_battle_with_troop", 0),
			(troop_slot_eq, "$g_private_battle_with_troop", slot_troop_leaded_party, "$g_encountered_party"),
			(assign, "$g_private_battle_with_troop", 0),
			(assign, "$g_disable_condescending_comments", 1),
		(try_end),
		(party_get_num_companion_stacks, ":num_companion_stacks_collective_enemy", "p_collective_enemy"),
		(try_for_range, ":localvariable", 0, ":num_companion_stacks_collective_enemy"),
			(party_stack_get_troop_id, ":party_stack_troop_id_collective_enemy_localvariable", "p_collective_enemy", ":localvariable"),
			(is_between, ":party_stack_troop_id_collective_enemy_localvariable", "trp_knight_1_1", "trp_kingdom_2_pretender"),
			(troop_is_wounded, ":party_stack_troop_id_collective_enemy_localvariable"),
			(party_add_members, "p_total_enemy_casualties", ":party_stack_troop_id_collective_enemy_localvariable", 1),
		(try_end),
		(try_begin),
			(eq, "$thanked_by_ally_leader", 0),
			(assign, "$thanked_by_ally_leader", 1),
			(gt, "$g_ally_party", 0),
			(store_add, ":value_2", "$g_starting_strength_friends", "$g_starting_strength_enemy_party"),
			(val_sub, ":value_2", "$g_starting_strength_main_party"),
			(store_sub, ":value_3", "$g_starting_strength_friends", "$g_starting_strength_main_party"),
			(store_mul, ":value_4", ":value_3", 100),
			(val_add, ":value_2", 1),
			(val_div, ":value_4", ":value_2"),
			(store_sub, ":value_5", 100, ":value_4"),
			(store_mul, ":value_6", ":value_5", "$g_starting_strength_enemy_party"),
			(val_div, ":value_6", 3000),
			(val_min, ":value_6", 4),
			(store_mul, "$g_relation_boost", ":value_5", ":value_5"),
			(val_div, "$g_relation_boost", 700),
			(val_clamp, "$g_relation_boost", 0, 20),
			(party_get_num_companion_stacks, ":num_companion_stacks_l_g_ally_party", "$g_ally_party"),
			(gt, ":num_companion_stacks_l_g_ally_party", 0),
			(store_faction_of_party, ":faction_of_party_g_ally_party", "$g_ally_party"),
			(call_script, "script_change_player_relation_with_faction", ":faction_of_party_g_ally_party", ":value_6"),
			(party_stack_get_troop_id, ":party_stack_troop_id_g_ally_party", "$g_ally_party"),
			(party_stack_get_troop_dna, ":party_stack_troop_dna_g_ally_party_0", "$g_ally_party", 0),
			(try_begin),
				(troop_is_hero, ":party_stack_troop_id_g_ally_party"),
				(troop_get_slot, ":party_stack_troop_id_g_ally_party_player_relation", ":party_stack_troop_id_g_ally_party", slot_troop_player_relation),
				(assign, ":var_17", "$g_relation_boost"),
				(try_begin),
					(lt, ":party_stack_troop_id_g_ally_party_player_relation", -5),
					(val_div, ":var_17", 3),
				(try_end),
				(call_script, "script_change_player_relation_with_troop", ":party_stack_troop_id_g_ally_party", ":var_17"),
			(try_end),
			(neq, "$freelancer_state", 1),
			(assign, "$talk_context", 13),
			(call_script, "script_setup_troop_meeting", ":party_stack_troop_id_g_ally_party", ":party_stack_troop_dna_g_ally_party_0"),
		(else_try),
			(neq, "$freelancer_state", 1),
			(assign, ":value", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_collective_enemy", "p_total_enemy_casualties"),
			(try_for_range, ":value_7", "$last_defeated_hero", ":num_companion_stacks_collective_enemy"),
				(eq, ":value", 0),
				(party_stack_get_troop_id, ":party_stack_troop_id_collective_enemy_localvariable", "p_total_enemy_casualties", ":value_7"),
				(party_stack_get_troop_dna, ":party_stack_troop_dna_total_enemy_casualties_value_7", "p_total_enemy_casualties", ":value_7"),
				(troop_is_hero, ":party_stack_troop_id_collective_enemy_localvariable"),
				(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_collective_enemy_localvariable", ":party_stack_troop_id_collective_enemy_localvariable"),
				(try_begin),
					(store_relation, ":relation_faction_of_troop_party_stack_troop_id_collective_enemy_localvariable_player_faction", ":faction_of_troop_party_stack_troop_id_collective_enemy_localvariable", "fac_player_faction"),
					(ge, ":relation_faction_of_troop_party_stack_troop_id_collective_enemy_localvariable_player_faction", 0),
					(str_store_troop_name, 4, ":party_stack_troop_id_collective_enemy_localvariable"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(display_message, "@{!}{s4} skipped in p total enemy casualties capture queue because is friendly"),
					(try_end),
				(else_try),
					(try_begin),
						(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_0", "$g_encountered_party", 0),
						(is_between, ":party_stack_troop_id_g_encountered_party_0", "trp_npc1", "trp_knight_1_1_wife"),
						(troop_slot_eq, ":party_stack_troop_id_g_encountered_party_0", slot_troop_occupation, 2),
						(store_sub, ":value_8", ":party_stack_troop_id_g_encountered_party_0", "trp_npc1"),
						(get_achievement_stat, ":achievement_stat_7_value_8", 7, ":value_8"),
						(eq, ":achievement_stat_7_value_8", 1),
						(unlock_achievement, 7),
					(try_end),
					(store_add, "$last_defeated_hero", ":value_7", 1),
					(call_script, "script_remove_troop_from_prison", ":party_stack_troop_id_collective_enemy_localvariable"),
					(troop_set_slot, ":party_stack_troop_id_collective_enemy_localvariable", slot_troop_leaded_party, -1),
					(call_script, "script_cf_check_hero_can_escape_from_player", ":party_stack_troop_id_collective_enemy_localvariable"),
					(str_store_troop_name, 1, ":party_stack_troop_id_collective_enemy_localvariable"),
					(str_store_faction_name, 3, ":faction_of_troop_party_stack_troop_id_collective_enemy_localvariable"),
					(str_store_string, 17, "@{s1} of {s3} managed to escape."),
					(display_log_message, "@{!}{s17}"),
					(jump_to_menu, "mnu_enemy_slipped_away"),
					(assign, ":value", 1),
				(else_try),
					(store_add, "$last_defeated_hero", ":value_7", 1),
					(call_script, "script_remove_troop_from_prison", ":party_stack_troop_id_collective_enemy_localvariable"),
					(troop_set_slot, ":party_stack_troop_id_collective_enemy_localvariable", slot_troop_leaded_party, -1),
					(assign, "$talk_context", 9),
					(call_script, "script_setup_troop_meeting", ":party_stack_troop_id_collective_enemy_localvariable", ":party_stack_troop_dna_total_enemy_casualties_value_7"),
					(assign, ":value", 1),
				(try_end),
			(try_end),
			(eq, ":value", 1),
		(else_try),
			(neq, "$freelancer_state", 1),
			(assign, ":value", 0),
			(party_get_num_prisoner_stacks, ":num_prisoner_stacks_collective_enemy", "p_collective_enemy"),
			(try_for_range, ":value_7", "$last_freed_hero", ":num_prisoner_stacks_collective_enemy"),
				(eq, ":value", 0),
				(party_prisoner_stack_get_troop_id, ":party_stack_troop_id_collective_enemy_localvariable", "p_collective_enemy", ":value_7"),
				(troop_is_hero, ":party_stack_troop_id_collective_enemy_localvariable"),
				(party_prisoner_stack_get_troop_dna, ":party_stack_troop_dna_total_enemy_casualties_value_7", "p_collective_enemy", ":value_7"),
				(store_add, "$last_freed_hero", ":value_7", 1),
				(assign, "$talk_context", 8),
				(call_script, "script_setup_troop_meeting", ":party_stack_troop_id_collective_enemy_localvariable", ":party_stack_troop_dna_total_enemy_casualties_value_7"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 1),
		(else_try),
			(eq, "$capture_screen_shown", 0),
			(assign, "$capture_screen_shown", 1),
			(party_clear, "p_temp_party"),
			(assign, "$g_move_heroes", 0),
			(call_script, "script_party_add_wounded_members_as_prisoners", "p_temp_party", "p_total_enemy_casualties"),
			(call_script, "script_party_add_party_prisoners", "p_temp_party", "p_collective_enemy"),
			(try_begin),
				(call_script, "script_party_calculate_strength", "p_collective_friends_backup", 0),
				(assign, ":var_26", reg0),
				(gt, ":var_26", 0),
				(call_script, "script_party_calculate_strength", "p_main_party_backup", 0),
				(assign, ":var_27", reg0),
				(store_sub, ":value_9", ":var_26", ":var_27"),
				(store_mul, ":value_10", ":value_9", 1000),
				(val_div, ":value_10", ":var_26"),
				(assign, "$pin_number", ":value_10"),
				(party_clear, "p_temp_party_2"),
				(call_script, "script_move_members_with_ratio", "p_temp_party", "p_temp_party_2"),
				(try_begin),
					(gt, "$g_ally_party", 0),
					(distribute_party_among_party_group, "p_temp_party_2", "$g_ally_party"),
				(try_end),
			(try_end),
			(party_get_num_companions, ":num_companions_temp_party", "p_temp_party"),
			(party_get_num_prisoners, ":num_prisoners_temp_party", "p_temp_party"),
			(store_add, ":value_11", ":num_companions_temp_party", ":num_prisoners_temp_party"),
			(neq, "$freelancer_state", 1),
			(gt, ":value_11", 0),
			(change_screen_exchange_with_party, "p_temp_party"),
		(else_try),
			(eq, "$loot_screen_shown", 0),
			(assign, "$loot_screen_shown", 1),
			(troop_clear_inventory, "trp_temp_troop"),
			(call_script, "script_party_calculate_loot", "p_total_enemy_casualties"),
			(gt, reg0, 0),
			(troop_sort_inventory, "trp_temp_troop"),
			(assign, ":var_33", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_collective_enemy", "p_main_party"),
			(try_for_range, ":value_7", 0, ":num_companion_stacks_collective_enemy"),
				(party_stack_get_troop_id, ":party_stack_troop_id_collective_enemy_localvariable", "p_main_party", ":value_7"),
				(is_between, ":party_stack_troop_id_collective_enemy_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(val_add, ":var_33", 1),
			(try_end),
			(try_begin),
				(gt, ":var_33", 0),
				(assign, "$return_menu", "mnu_total_victory"),
				(jump_to_menu, "mnu_manage_loot_pool"),
			(else_try),
				(change_screen_loot, "trp_temp_troop"),
			(try_end),
		(else_try),
			(try_begin),
				(le, "$g_ally_party", 0),
				(end_current_battle),
			(try_end),
			(call_script, "script_party_give_xp_and_gold", "p_total_enemy_casualties"),
			(try_begin),
				(eq, "$g_enemy_party", 0),
				(display_message, "str_error_string"),
			(try_end),
			(try_begin),
				(party_is_active, "$g_ally_party"),
				(call_script, "script_battle_political_consequences", "$g_enemy_party", "$g_ally_party"),
			(else_try),
				(call_script, "script_battle_political_consequences", "$g_enemy_party", "p_main_party"),
			(try_end),
			(call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
			(call_script, "script_clear_party_group", "$g_enemy_party"),
			(try_begin),
				(eq, "$g_next_menu", -1),
				(call_script, "script_post_battle_personality_clash_check"),
				(party_stack_get_troop_id, ":party_stack_troop_id_encountered_party_backup_0", "p_encountered_party_backup", 0),
				(try_begin),
					(is_between, ":party_stack_troop_id_encountered_party_backup_0", "trp_npc1", "trp_knight_1_1_wife"),
					(neg|is_between, "$g_encountered_party", "p_town_1_1", "p_salt_mine"),
					(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_encountered_party_backup_0", ":party_stack_troop_id_encountered_party_backup_0"),
					(try_begin),
						(eq, "$g_ally_party", 0),
						(call_script, "script_add_log_entry", 11, "trp_player", -1, ":party_stack_troop_id_encountered_party_backup_0", ":faction_of_troop_party_stack_troop_id_encountered_party_backup_0"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(display_message, "@{!}Victory comment. Player was alone"),
						(try_end),
					(else_try),
						(ge, "$g_strength_contribution_of_player", 40),
						(call_script, "script_add_log_entry", 11, "trp_player", -1, ":party_stack_troop_id_encountered_party_backup_0", ":faction_of_troop_party_stack_troop_id_encountered_party_backup_0"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(display_message, "@{!}Ordinary victory comment. The player provided at least 40 percent forces."),
						(try_end),
					(else_try),
						(gt, "$g_starting_strength_enemy_party", 1000),
						(call_script, "script_get_closest_center", "p_main_party"),
						(assign, ":var_36", reg0),
						(call_script, "script_add_log_entry", 19, "trp_player", ":var_36", -1, ":faction_of_troop_party_stack_troop_id_encountered_party_backup_0"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(display_message, "@{!}Player participation comment. The enemy had at least 1k starting strength."),
						(try_end),
					(else_try),
						(eq, "$cheat_mode", 1),
						(display_message, "@{!}No victory comment. The battle was small, and the player provided less than 40 percent of allied strength"),
					(try_end),
				(try_end),
				(val_add, "$g_total_victories", 1),
				(leave_encounter),
				(change_screen_return),
			(else_try),
				(neq, "$freelancer_state", 1),
				(try_begin),
					(eq, "$g_next_menu", "mnu_castle_taken"),
					(call_script, "script_add_log_entry", 10, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
					(store_current_hours, ":current_hours"),
					(faction_set_slot, "$players_kingdom", slot_faction_ai_last_decisive_event, ":current_hours"),
					(try_begin),
						(is_between, "$players_kingdom", "fac_kingdom_1", "fac_kingdoms_end"),
						(try_begin),
							(eq, "$g_encountered_party", "p_town_26_1"),
							(eq, "$players_kingdom", "fac_kingdom_22"),
							(faction_set_name, "fac_kingdom_22", "@Roman Empire"),
							(display_message, "@The Roman Empire has been restored!", 0x00ff0000),
							(party_set_slot, "p_town_26_1", 708, 50),
							(party_set_slot, "p_town_26_1", 710, "pt_company_varangian"),
							(party_set_slot, "p_town_26_1", 709, 1),
						(try_end),
						(jump_to_menu, "$g_next_menu"),
					(else_try),
						(eq, "$players_kingdom", "fac_player_supporters_faction"),
						(assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
						(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
						(faction_get_slot, ":player_supporters_faction_leader", "fac_player_supporters_faction", slot_faction_leader),
						(change_screen_return),
						(start_map_conversation, ":player_supporters_faction_leader", -1),
					(else_try),
						(neg|is_between, "$players_kingdom", "fac_kingdom_1", "fac_kingdoms_end"),
						(assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
						(assign, "$talk_context", 20),
						(change_screen_return),
						(assign, ":value_12", "trp_euro_horse_4"),
						(assign, ":value_13", 0),
						(party_get_num_companion_stacks, ":num_companion_stacks_collective_enemy", "p_main_party"),
						(try_for_range, ":value_7", 0, ":num_companion_stacks_collective_enemy"),
							(party_stack_get_troop_id, ":party_stack_troop_id_collective_enemy_localvariable", "p_main_party", ":value_7"),
							(neq, ":party_stack_troop_id_collective_enemy_localvariable", "trp_player"),
							(party_stack_get_size, ":party_stack_size_main_party_value_7", "p_main_party", ":value_7"),
							(party_stack_get_num_wounded, ":party_stack_num_wounded_main_party_value_7", "p_main_party", ":value_7"),
							(troop_get_slot, ":main_party_player_routed_agents", "p_main_party", slot_troop_player_routed_agents),
							(assign, ":value_14", 0),
							(try_begin),
								(neg|troop_is_hero, ":party_stack_troop_id_collective_enemy_localvariable"),
								(store_add, ":value_15", ":party_stack_num_wounded_main_party_value_7", ":main_party_player_routed_agents"),
								(gt, ":party_stack_size_main_party_value_7", ":value_15"),
								(assign, ":value_14", 1),
							(else_try),
								(troop_is_hero, ":party_stack_troop_id_collective_enemy_localvariable"),
								(neg|troop_is_wounded, ":party_stack_troop_id_collective_enemy_localvariable"),
								(assign, ":value_14", 1),
							(try_end),
							(eq, ":value_14", 1),
							(try_begin),
								(troop_is_hero, ":party_stack_troop_id_collective_enemy_localvariable"),
								(troop_get_slot, ":party_stack_troop_id_collective_enemy_localvariable_renown", ":party_stack_troop_id_collective_enemy_localvariable", slot_troop_renown),
								(store_mul, ":value_16", ":party_stack_troop_id_collective_enemy_localvariable_renown", 100),
								(val_add, ":value_16", 1000),
							(else_try),
								(store_character_level, ":character_level_party_stack_troop_id_collective_enemy_localvariable", ":party_stack_troop_id_collective_enemy_localvariable"),
								(assign, ":value_16", ":character_level_party_stack_troop_id_collective_enemy_localvariable"),
							(try_end),
							(try_begin),
								(gt, ":value_16", ":value_13"),
								(assign, ":value_13", ":value_16"),
								(assign, ":value_12", ":party_stack_troop_id_collective_enemy_localvariable"),
								(party_stack_get_troop_dna, ":party_stack_troop_dna_main_party_value_7", "p_main_party", ":value_7"),
							(try_end),
						(try_end),
						(start_map_conversation, ":value_12", ":party_stack_troop_dna_main_party_value_7"),
					(try_end),
				(try_end),
			(try_end),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[], ".")
	]
	),

	("enemy_slipped_away", 0, "{s17}",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_total_victory")
		], ".")
	]
	),

	("total_defeat", 0, "{!}You shouldn't be reading this...",
"none",
	[
		(play_track, "track_capture", 1),
		(party_get_num_prisoner_stacks, ":num_prisoner_stacks_main_party", "p_main_party"),
		(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_main_party"),
			(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
			(troop_is_hero, ":party_prisoner_stack_troop_id_main_party_localvariable"),
			(call_script, "script_remove_troop_from_prison", ":party_prisoner_stack_troop_id_main_party_localvariable"),
		(try_end),
		(try_begin),
			(party_is_active, "$g_ally_party"),
			(call_script, "script_battle_political_consequences", "$g_ally_party", "$g_enemy_party"),
		(else_try),
			(call_script, "script_battle_political_consequences", "p_main_party", "$g_enemy_party"),
		(try_end),
		(call_script, "script_loot_player_items", "$g_enemy_party"),
		(assign, "$g_move_heroes", 0),
		(party_clear, "p_temp_party"),
		(call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
		(call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
		(distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),
		(assign, "$g_prison_heroes", 1),
		(call_script, "script_party_remove_all_companions", "p_main_party"),
		(assign, "$g_prison_heroes", 0),
		(assign, "$g_move_heroes", 1),
		(call_script, "script_party_remove_all_prisoners", "p_main_party"),
		(val_add, "$g_total_defeats", 1),
		(try_begin),
			(neq, "$g_player_surrenders", 1),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(ge, ":random_in_range_0_100", "$g_player_luck"),
			(jump_to_menu, "mnu_permanent_damage"),
		(else_try),
			(try_begin),
				(eq, "$g_next_menu", -1),
				(leave_encounter),
				(change_screen_return),
			(else_try),
				(jump_to_menu, "$g_next_menu"),
			(try_end),
		(try_end),
		(try_begin),
			(gt, "$g_ally_party", 0),
			(call_script, "script_party_wound_all_members", "$g_ally_party"),
		(try_end),
		(party_get_num_companion_stacks, ":num_companion_stacks_encountered_party_backup", "p_encountered_party_backup"),
		(try_for_range, ":localvariable", 0, ":num_companion_stacks_encountered_party_backup"),
			(party_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_encountered_party_backup", ":localvariable"),
			(is_between, ":party_prisoner_stack_troop_id_main_party_localvariable", "trp_npc1", "trp_knight_1_1_wife"),
			(troop_slot_eq, ":party_prisoner_stack_troop_id_main_party_localvariable", slot_troop_occupation, 2),
			(store_faction_of_troop, ":faction_of_troop_party_prisoner_stack_troop_id_main_party_localvariable", ":party_prisoner_stack_troop_id_main_party_localvariable"),
			(call_script, "script_add_log_entry", 14, "trp_player", -1, ":party_prisoner_stack_troop_id_main_party_localvariable", ":faction_of_troop_party_prisoner_stack_troop_id_main_party_localvariable"),
		(try_end)
	],
	[]
	),

	("permanent_damage", 0, "{s0}",
"none",
	[
		(assign, ":var_1", 1),
		(try_for_range, ":unused", 0, ":var_1"),
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(store_attribute_level, ":attribute_level_player_random_in_range_0_4", "trp_player", ":random_in_range_0_4"),
			(try_begin),
				(gt, ":attribute_level_player_random_in_range_0_4", 3),
				(neq, ":random_in_range_0_4", 3),
				(try_begin),
					(eq, ":random_in_range_0_4", 0),
					(str_store_string, 0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
				(else_try),
					(eq, ":random_in_range_0_4", 1),
					(str_store_string, 0, "@You took a nasty wound which will cause you to limp slightly even after it heals. You lose 1 agility."),
				(else_try),
					(str_store_string, 0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
				(try_end),
			(else_try),
				(lt, ":var_1", 200),
				(val_add, ":var_1", 1),
			(try_end),
		(try_end),
		(try_begin),
			(eq, ":var_1", 200),
			(try_begin),
				(eq, "$g_next_menu", -1),
				(leave_encounter),
				(change_screen_return),
			(else_try),
				(jump_to_menu, "$g_next_menu"),
			(try_end),
		(else_try),
			(troop_raise_attribute, "trp_player", ":random_in_range_0_4", -1),
		(try_end)
	],
	[
		("s0",
		[
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(try_begin),
				(eq, ":random_in_range_0_4", 0),
				(str_store_string, 0, "@Perhaps I'm getting unlucky..."),
			(else_try),
				(eq, ":random_in_range_0_4", 1),
				(str_store_string, 0, "@Retirement is starting to sound better and better."),
			(else_try),
				(eq, ":random_in_range_0_4", 2),
				(str_store_string, 0, "@No matter! I will persevere!"),
			(else_try),
				(eq, ":random_in_range_0_4", 3),
				(troop_get_type, ":type_player", "trp_player"),
				(try_begin),
					(eq, ":type_player", 1),
					(str_store_string, 0, "@What did I do to deserve this?"),
				(else_try),
					(str_store_string, 0, "@I suppose it'll make for a good story, at least..."),
				(try_end),
			(try_end)
		],
		"{s0}",
		[
			(try_begin),
				(eq, "$g_next_menu", -1),
				(leave_encounter),
				(change_screen_return),
			(else_try),
				(jump_to_menu, "$g_next_menu"),
			(try_end)
		], ".")
	]
	),

	("pre_join", 0, "You come across a battle between {s2} and {s1}. You decide to...",
"none",
	[
		(str_store_party_name, 1, "$g_encountered_party"),
		(str_store_party_name, 2, "$g_encountered_party_2"),
		(eq, "$freelancer_state", 1),
		(try_begin),
			(party_get_attached_to, ":attached_to_l_enlisted_party", "$enlisted_party"),
			(this_or_next|eq, "$enlisted_party", "$g_encountered_party_2"),
			(eq, ":attached_to_l_enlisted_party", "$g_encountered_party_2"),
			(select_enemy, 0),
			(assign, "$g_enemy_party", "$g_encountered_party"),
			(assign, "$g_ally_party", "$g_encountered_party_2"),
		(else_try),
			(select_enemy, 1),
			(assign, "$g_enemy_party", "$g_encountered_party_2"),
			(assign, "$g_ally_party", "$g_encountered_party"),
		(try_end),
		(jump_to_menu, "mnu_join_battle")
	],
	[
		("pre_join_help_attackers",
		[
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party_2"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", ":faction_of_party_g_encountered_party_2", "fac_player_supporters_faction"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", 0),
			(lt, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0)
		],
		"Move in to help the {s2}.",
		[
			(select_enemy, 0),
			(assign, "$g_enemy_party", "$g_encountered_party"),
			(assign, "$g_ally_party", "$g_encountered_party_2"),
			(jump_to_menu, "mnu_join_battle")
		], "."),

		("pre_join_help_defenders",
		[
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party_2"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", ":faction_of_party_g_encountered_party_2", "fac_player_supporters_faction"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0),
			(lt, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", 0)
		],
		"Rush to the aid of the {s1}.",
		[
			(select_enemy, 1),
			(assign, "$g_enemy_party", "$g_encountered_party_2"),
			(assign, "$g_ally_party", "$g_encountered_party"),
			(jump_to_menu, "mnu_join_battle")
		], "."),

		("pre_join_leave",
		[],
		"Don't get involved.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("join_battle", 0, "You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}.",
"none",
	[
		(str_store_party_name, 1, "$g_enemy_party"),
		(str_store_party_name, 2, "$g_ally_party"),
		(call_script, "script_encounter_calculate_fit"),
		(try_begin),
			(eq, "$new_encounter", 1),
			(assign, "$new_encounter", 0),
			(try_begin),
				(eq, "$freelancer_state", 1),
				(call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
				(str_store_party_name, 1, "$g_enemy_party"),
			(try_end),
			(call_script, "script_encounter_init_variables"),
		(else_try),
			(eq, "$g_leave_encounter", 1),
			(change_screen_return),
		(try_end),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
			(assign, ":var_1", reg0),
			(assign, ":value", 0),
			(try_begin),
				(eq, "$g_battle_result", 1),
				(this_or_next|le, ":var_1", 0),
				(le, ":var_1", "$num_routed_enemies"),
				(assign, ":value", 1),
			(else_try),
				(eq, "$g_engaged_enemy", 1),
				(le, "$g_enemy_fit_for_battle", 0),
				(ge, "$g_friend_fit_for_battle", 1),
				(assign, ":value", 1),
			(try_end),
			(this_or_next|eq, ":value", 1),
			(eq, "$g_enemy_surrenders", 1),
			(assign, "$g_next_menu", -1),
			(jump_to_menu, "mnu_total_victory"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
			(assign, ":var_3", reg0),
			(assign, ":value_2", 0),
			(try_begin),
				(eq, "$g_battle_result", -1),
				(le, ":var_3", "$num_routed_allies"),
				(assign, ":value_2", 1),
			(try_end),
			(this_or_next|eq, ":value_2", 1),
			(eq, "$g_player_surrenders", 1),
			(leave_encounter),
			(change_screen_return),
		(try_end)
	],
	[
		("join_attack",
		[
			(neg|troop_is_wounded, "trp_player"),
			(assign, ":value", 0),
			(try_begin),
				(call_script, "script_cf_is_party_on_water", "p_main_party"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 0)
		],
		"Charge the enemy.",
		[
			(assign, "$g_joined_battle_to_help", 1),
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(assign, "$g_battle_result", 0),
			(call_script, "script_calculate_renown_value"),
			(call_script, "script_calculate_battle_advantage"),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(set_jump_mission, "mt_lead_charge"),
			(call_script, "script_setup_random_scene"),
			(assign, "$g_next_menu", "mnu_join_battle"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("join_attack",
		[
			(neg|troop_is_wounded, "trp_player"),
			(call_script, "script_cf_is_party_on_water", "p_main_party")
		],
		"Board the enemy.",
		[
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(assign, "$g_battle_result", 0),
			(call_script, "script_calculate_renown_value"),
			(call_script, "script_calculate_battle_advantage"),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(set_jump_mission, "mt_ship_battle"),
			(call_script, "script_setup_random_scene"),
			(assign, "$g_next_menu", "mnu_join_battle"),
			(jump_to_menu, "mnu_battle_debrief"),
			(jump_to_scene, "scn_scene_sea"),
			(change_screen_mission)
		], "."),

		("join_order_attack",
		[
			(neq, "$freelancer_state", 1),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(ge, reg0, 3)
		],
		"Order your troops to attack with your allies while you stay back.",
		[
			(assign, "$g_joined_battle_to_help", 1),
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(jump_to_menu, "mnu_join_order_attack")
		], "."),

		("join_leave",
		[],
		"Leave.",
		[
			(neq, "$freelancer_state", 1),
			(try_begin),
				(neg|troop_is_wounded, "trp_player"),
				(call_script, "script_objectionable_action", 1, "str_flee_battle"),
				(party_stack_get_troop_id, ":party_stack_troop_id_g_enemy_party_0", "$g_enemy_party", 0),
				(is_between, ":party_stack_troop_id_g_enemy_party_0", "trp_npc1", "trp_knight_1_1_wife"),
				(call_script, "script_add_log_entry", 15, "trp_player", -1, ":party_stack_troop_id_g_enemy_party_0", -1),
			(try_end),
			(leave_encounter),
			(change_screen_return)
		], "."),

		("join_wounded",
		[
			(eq, "$freelancer_state", 1),
			(troop_is_wounded, "trp_player")
		],
		"You are too wounded to fight.",
		[
			(leave_encounter),
			(change_screen_map)
		], ".")
	]
	),

	("join_order_attack", 0, "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
"none",
	[
		(call_script, "script_party_calculate_strength", "p_main_party", 1),
		(assign, ":var_1", reg0),
		(val_div, ":var_1", 5),
		(call_script, "script_party_calculate_strength", "p_collective_friends", 0),
		(assign, ":var_2", reg0),
		(val_div, ":var_2", 5),
		(call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
		(assign, ":var_3", reg0),
		(val_div, ":var_3", 5),
		(try_begin),
			(eq, ":var_2", 0),
			(store_div, ":value", ":var_3", 2),
		(else_try),
			(assign, ":value", ":var_3"),
			(val_mul, ":value", ":var_1"),
			(val_div, ":value", ":var_2"),
		(try_end),
		(val_sub, ":var_3", ":value"),
		(inflict_casualties_to_party_group, "p_main_party", ":value", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 8, 0),
		(inflict_casualties_to_party_group, "$g_enemy_party", ":var_2", "p_temp_casualties"),
		(party_get_num_companion_stacks, ":num_companion_stacks_temp_casualties", "p_temp_casualties"),
		(try_for_range, ":localvariable", 0, ":num_companion_stacks_temp_casualties"),
			(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
			(try_begin),
				(party_stack_get_size, ":party_stack_size_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
				(gt, ":party_stack_size_temp_casualties_localvariable", 0),
				(party_add_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_casualties_localvariable", ":party_stack_size_temp_casualties_localvariable"),
				(party_stack_get_num_wounded, ":party_stack_num_wounded_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
				(gt, ":party_stack_num_wounded_temp_casualties_localvariable", 0),
				(party_wound_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_casualties_localvariable", ":party_stack_num_wounded_temp_casualties_localvariable"),
			(try_end),
		(try_end),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 10, 0),
		(call_script, "script_collect_friendly_parties"),
		(inflict_casualties_to_party_group, "$g_ally_party", ":var_3", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 9, 0),
		(party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
		(assign, "$no_soldiers_left", 0),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(assign, ":var_10", reg0),
			(le, ":var_10", "$num_routed_us"),
			(assign, "$no_soldiers_left", 1),
			(str_store_string, 4, "str_join_order_attack_failure"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
			(assign, ":var_11", reg0),
			(this_or_next|le, ":var_11", 0),
			(le, ":var_11", "$num_routed_enemies"),
			(assign, "$g_battle_result", 1),
			(assign, "$no_soldiers_left", 1),
			(str_store_string, 4, "str_join_order_attack_success"),
		(else_try),
			(str_store_string, 4, "str_join_order_attack_continue"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_join_battle")
		], ".")
	]
	),

	("zendar", 0, "You enter the town of Zendar.",
"none",
	[
		(reset_price_rates, 0),
		(set_price_rate_for_item, "itm_tools", 70),
		(set_price_rate_for_item, "itm_salt", 140)
	],
	[
		("zendar_enter",
		[],
		" ",
		[
			(set_jump_mission, "mt_town_default"),
			(jump_to_scene, "scn_zendar_center"),
			(change_screen_mission)
		], "Door_to_the_town_center."),

		("zendar_tavern",
		[],
		" ",
		[
			(set_jump_mission, "mt_town_default"),
			(jump_to_scene, "scn_the_happy_boar"),
			(change_screen_mission)
		], "Door_to_the_tavern."),

		("zendar_merchant",
		[],
		" ",
		[
			(set_jump_mission, "mt_town_default"),
			(jump_to_scene, "scn_zendar_merchant"),
			(change_screen_mission)
		], "Door_to_the_merchant."),

		("zendar_arena",
		[],
		" ",
		[
			(set_jump_mission, "mt_town_default"),
			(jump_to_scene, "scn_zendar_arena"),
			(change_screen_mission)
		], "Door_to_the_arena."),

		("town_1_leave",
		[],
		" ",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("salt_mine", 0, "You enter the salt mine.",
"none",
	[
		(reset_price_rates, 0),
		(set_price_rate_for_item, "itm_salt", 55)
	],
	[
		("enter",
		[],
		"Enter.",
		[
			(set_jump_mission, "mt_town_center"),
			(jump_to_scene, "scn_salt_mine"),
			(change_screen_mission)
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("four_ways_inn", 0, "You arrive at the Four Ways Inn.",
"none",
	[],
	[
		("enter",
		[],
		"Enter.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_four_ways_inn"),
			(change_screen_mission)
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("test_scene", 0, "You enter the test scene.",
"none",
	[],
	[
		("enter",
		[],
		"Enter 1.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_1"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 2.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_2"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 3.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_3"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 4.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_4"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 5.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_5"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 6.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_6"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 7.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_test2"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 8.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_test3"),
			(change_screen_mission)
		], "."),

		("enter",
		[],
		"Enter 9.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_multi_scene_13"),
			(change_screen_mission)
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("battlefields", 0, "{!}Select a field...",
"none",
	[],
	[
		("enter_f1",
		[],
		"{!}Field 1",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_field_1"),
			(change_screen_mission)
		], "."),

		("enter_f2",
		[],
		"{!}Field 2",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_field_2"),
			(change_screen_mission)
		], "."),

		("enter_f3",
		[],
		"{!}Field 3",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_field_3"),
			(change_screen_mission)
		], "."),

		("enter_f4",
		[],
		"{!}Field 4",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_field_4"),
			(change_screen_mission)
		], "."),

		("enter_f5",
		[],
		"{!}Field 5",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_field_5"),
			(change_screen_mission)
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("dhorak_keep", 0, "You enter the Dhorak Keep",
"none",
	[],
	[
		("enter",
		[],
		"Enter.",
		[
			(set_jump_mission, "mt_town_center"),
			(jump_to_scene, "scn_dhorak_keep"),
			(change_screen_mission)
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("join_siege_outside", 0, "{s1} has come under siege by {s2}.",
"none",
	[
		(str_store_party_name, 1, "$g_encountered_party"),
		(str_store_party_name, 2, "$g_encountered_party_2"),
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, "$freelancer_state", 1),
			(try_begin),
				(store_faction_of_troop, ":faction_of_troop_enlisted_lord", "$enlisted_lord"),
				(store_relation, ":relation_faction_of_troop_enlisted_lord_g_encountered_party_faction", ":faction_of_troop_enlisted_lord", "$g_encountered_party_faction"),
				(this_or_next|eq, ":faction_of_troop_enlisted_lord", "$g_encountered_party_faction"),
				(ge, ":relation_faction_of_troop_enlisted_lord_g_encountered_party_faction", 0),
				(jump_to_menu, "mnu_siege_started_defender"),
			(else_try),
				(jump_to_menu, "mnu_besiegers_camp_with_allies"),
			(try_end),
		(else_try),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_siege_sighted_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_siege_sighted"),
		(try_end)
	],
	[
		("approach_besiegers",
		[
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party_2"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", ":faction_of_party_g_encountered_party_2", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", 0),
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", ":faction_of_party_g_encountered_party_2", "fac_player_supporters_faction"),
			(lt, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", 0)
		],
		"Approach the siege camp.",
		[
			(jump_to_menu, "mnu_besiegers_camp_with_allies")
		], "."),

		("pass_through_siege",
		[
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0)
		],
		"Pass through the siege lines and enter {s1}.",
		[
			(jump_to_menu, "mnu_cut_siege_without_fight")
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], ".")
	]
	),

	("cut_siege_without_fight", 0, "The besiegers let you approach the gates without challenge.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
				(eq, "$g_encountered_party_faction", "$players_kingdom"),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_castle_outside"),
			(try_end)
		], ".")
	]
	),

	("besiegers_camp_with_allies", 0, "{s1} remains under siege. The banners of {s2} fly above the camp of the besiegers, where you and your men are welcomed.",
"none",
	[
		(str_store_party_name, 1, "$g_encountered_party"),
		(str_store_party_name, 2, "$g_encountered_party_2"),
		(assign, "$g_enemy_party", "$g_encountered_party"),
		(assign, "$g_ally_party", "$g_encountered_party_2"),
		(select_enemy, 0),
		(call_script, "script_encounter_calculate_fit"),
		(try_begin),
			(eq, "$new_encounter", 1),
			(assign, "$new_encounter", 0),
			(call_script, "script_encounter_init_variables"),
		(try_end),
		(try_begin),
			(eq, "$g_leave_encounter", 1),
			(change_screen_return),
		(else_try),
			(assign, ":value", 0),
			(try_begin),
				(eq, "$g_battle_result", 1),
				(assign, ":value", 1),
			(else_try),
				(le, "$g_enemy_fit_for_battle", 0),
				(ge, "$g_friend_fit_for_battle", 1),
				(assign, ":value", 1),
			(try_end),
			(this_or_next|eq, ":value", 1),
			(eq, "$g_enemy_surrenders", 1),
			(call_script, "script_party_wound_all_members", "$g_enemy_party"),
			(leave_encounter),
			(change_screen_return),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
			(assign, ":var_2", reg0),
			(eq, "$g_battle_result", -1),
			(eq, ":var_2", 0),
			(leave_encounter),
			(change_screen_return),
		(try_end)
	],
	[
		("talk_to_siege_commander",
		[],
		" Request a meeting with the commander.",
		[
			(call_script, "script_get_meeting_scene"),
			(assign, ":var_1", reg0),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_2_0", "$g_encountered_party_2", 0),
			(party_stack_get_troop_dna, ":party_stack_troop_dna_g_encountered_party_2_0", "$g_encountered_party_2", 0),
			(set_visitor, 17, ":party_stack_troop_id_g_encountered_party_2_0", ":party_stack_troop_dna_g_encountered_party_2_0"),
			(set_jump_mission, "mt_conversation_encounter"),
			(jump_to_scene, ":var_1"),
			(assign, "$talk_context", 4),
			(change_screen_map_conversation, ":party_stack_troop_id_g_encountered_party_2_0")
		], "."),

		("join_siege_with_allies",
		[
			(neg|troop_is_wounded, "trp_player")
		],
		"Join the next assault.",
		[
			(assign, "$g_joined_battle_to_help", 1),
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(try_begin),
				(check_quest_active, "qst_join_siege_with_army"),
				(quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
				(add_xp_as_reward, 250),
				(call_script, "script_end_quest", "qst_join_siege_with_army"),
				(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
				(str_store_troop_name_link, 9, ":players_kingdom_marshall"),
				(setup_quest_text, "qst_follow_army"),
				(str_store_string, 2, "@{s9} wants you to follow his army until further notice."),
				(call_script, "script_start_quest", "qst_follow_army", ":players_kingdom_marshall"),
				(assign, "$g_player_follow_army_warnings", 0),
			(try_end),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(party_get_slot, ":g_encountered_party_town_walls", "$g_encountered_party", slot_town_walls),
			(else_try),
				(party_get_slot, ":g_encountered_party_town_walls", "$g_encountered_party", slot_town_center),
			(try_end),
			(call_script, "script_calculate_battle_advantage"),
			(val_mul, reg0, 2),
			(val_div, reg0, 3),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
				(set_jump_mission, "mt_castle_attack_walls_belfry"),
			(else_try),
				(set_jump_mission, "mt_castle_attack_walls_ladder"),
			(try_end),
			(jump_to_scene, ":g_encountered_party_town_walls"),
			(assign, "$g_siege_final_menu", "mnu_besiegers_camp_with_allies"),
			(assign, "$g_siege_battle_state", 1),
			(assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("join_siege_stay_back",
		[
			(neq, "$freelancer_state", 1),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(ge, reg0, 3)
		],
		"Order your soldiers to join the next assault without you.",
		[
			(assign, "$g_joined_battle_to_help", 1),
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(try_begin),
				(check_quest_active, "qst_join_siege_with_army"),
				(quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
				(add_xp_as_reward, 100),
				(call_script, "script_end_quest", "qst_join_siege_with_army"),
				(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
				(str_store_troop_name_link, 9, ":players_kingdom_marshall"),
				(setup_quest_text, "qst_follow_army"),
				(str_store_string, 2, "@{s9} wants you to follow his army until further notice."),
				(call_script, "script_start_quest", "qst_follow_army", ":players_kingdom_marshall"),
				(assign, "$g_player_follow_army_warnings", 0),
			(try_end),
			(jump_to_menu, "mnu_castle_attack_walls_with_allies_simulate")
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(leave_encounter),
			(change_screen_return)
		], "."),

		("join_wounded",
		[
			(eq, "$freelancer_state", 1),
			(troop_is_wounded, "trp_player")
		],
		"You are too wounded to fight.",
		[
			(leave_encounter),
			(change_screen_map)
		], ".")
	]
	),

	("castle_outside", 0, "You are outside {s2}.{s11} {s3} {s4}",
"none",
	[
		(assign, "$g_enemy_party", "$g_encountered_party"),
		(assign, "$g_ally_party", -1),
		(str_store_party_name, 2, "$g_encountered_party"),
		(call_script, "script_encounter_calculate_fit"),
		(assign, "$all_doors_locked", 1),
		(assign, "$current_town", "$g_encountered_party"),
		(try_begin),
			(eq, "$new_encounter", 1),
			(assign, "$new_encounter", 0),
			(call_script, "script_let_nearby_parties_join_current_battle", 1, 0),
			(call_script, "script_encounter_init_variables"),
			(assign, "$entry_to_town_forbidden", 0),
			(assign, "$sneaked_into_town", 0),
			(assign, "$town_entered", 0),
			(assign, "$encountered_party_hostile", 0),
			(assign, "$encountered_party_friendly", 0),
			(try_begin),
				(gt, "$g_player_besiege_town", 0),
				(neq, "$g_player_besiege_town", "$g_encountered_party"),
				(party_slot_eq, "$g_player_besiege_town", slot_center_is_besieged_by, "p_main_party"),
				(call_script, "script_lift_siege", "$g_player_besiege_town", 0),
				(assign, "$g_player_besiege_town", -1),
			(try_end),
			(try_begin),
				(lt, "$g_encountered_party_relation", 0),
				(assign, "$encountered_party_hostile", 1),
				(assign, "$entry_to_town_forbidden", 1),
			(try_end),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
				(assign, "$encountered_party_hostile", 1),
				(assign, "$entry_to_town_forbidden", 1),
			(try_end),
			(assign, "$cant_sneak_into_town", 0),
			(try_begin),
				(eq, "$current_town", "$last_sneak_attempt_town"),
				(store_current_hours, reg2),
				(val_sub, reg2, "$last_sneak_attempt_time"),
				(lt, reg2, 12),
				(assign, "$cant_sneak_into_town", 1),
			(try_end),
		(else_try),
			(eq, "$g_leave_encounter", 1),
			(change_screen_return),
		(try_end),
		(str_clear, 4),
		(try_begin),
			(eq, "$entry_to_town_forbidden", 1),
			(try_begin),
				(eq, "$cant_sneak_into_town", 1),
				(str_store_string, 4, "str_sneaking_to_town_impossible"),
			(else_try),
				(str_store_string, 4, "str_entrance_to_town_forbidden"),
			(try_end),
		(try_end),
		(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
		(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
		(str_store_faction_name, 9, ":faction_of_party_current_town"),
		(try_begin),
			(ge, ":current_town_town_lord", 0),
			(str_store_troop_name, 8, ":current_town_town_lord"),
			(str_store_string, 7, "@{s8} of {s9}"),
		(try_end),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, 2),
			(try_begin),
				(eq, ":current_town_town_lord", "trp_player"),
				(str_store_string, 11, "@ Your own banner flies over the castle gate."),
			(else_try),
				(ge, ":current_town_town_lord", 0),
				(str_store_string, 11, "@ You see the banner of {s7} over the castle gate."),
			(else_try),
				(is_between, ":faction_of_party_current_town", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(str_store_string, 11, "str__this_castle_is_temporarily_under_royal_control"),
			(else_try),
				(str_store_string, 11, "str__this_castle_does_not_seem_to_be_under_anyones_control"),
			(try_end),
		(else_try),
			(try_begin),
				(eq, ":current_town_town_lord", "trp_player"),
				(str_store_string, 11, "@ Your own banner flies over the town gates."),
			(else_try),
				(ge, ":current_town_town_lord", 0),
				(str_store_string, 11, "@ You see the banner of {s7} over the town gates."),
			(else_try),
				(is_between, ":faction_of_party_current_town", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(str_store_string, 11, "str__this_town_is_temporarily_under_royal_control"),
			(else_try),
				(str_store_string, 11, "str__the_townspeople_seem_to_have_declared_their_independence"),
			(try_end),
		(try_end),
		(party_get_num_companions, reg7, "p_collective_enemy"),
		(assign, "$castle_undefended", 0),
		(str_clear, 3),
		(try_begin),
			(eq, reg7, 0),
			(assign, "$castle_undefended", 1),
			(str_store_string, 3, "str_castle_is_abondened"),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(str_store_string, 3, "str_dplmc_place_is_occupied_by_insurgents"),
		(else_try),
			(eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
			(str_store_string, 3, "str_place_is_occupied_by_player"),
		(else_try),
			(lt, "$g_encountered_party_relation", 0),
			(str_store_string, 3, "str_place_is_occupied_by_enemy"),
		(else_try),
		(try_end),
		(try_begin),
			(eq, "$g_leave_town_outside", 1),
			(assign, "$g_leave_town_outside", 0),
			(assign, "$g_permitted_to_center", 0),
			(change_screen_return),
		(else_try),
			(check_quest_active, "qst_escort_lady"),
			(quest_slot_eq, "qst_escort_lady", slot_quest_target_center, "$g_encountered_party"),
			(quest_get_slot, ":escort_lady_object_troop", "qst_escort_lady", slot_quest_object_troop),
			(call_script, "script_get_meeting_scene"),
			(assign, ":value", reg0),
			(modify_visitors_at_site, ":value"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 17, ":escort_lady_object_troop"),
			(set_jump_mission, "mt_conversation_encounter"),
			(jump_to_scene, ":value"),
			(assign, "$talk_context", 10),
			(change_screen_map_conversation, ":escort_lady_object_troop"),
		(else_try),
			(check_quest_active, "qst_kidnapped_girl"),
			(quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_center, "$g_encountered_party"),
			(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
			(call_script, "script_get_meeting_scene"),
			(assign, ":value", reg0),
			(modify_visitors_at_site, ":value"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 17, "trp_kidnapped_girl"),
			(set_jump_mission, "mt_conversation_encounter"),
			(jump_to_scene, ":value"),
			(assign, "$talk_context", 10),
			(change_screen_map_conversation, "trp_kidnapped_girl"),
		(else_try),
			(eq, "$g_town_visit_after_rest", 1),
			(assign, "$g_town_visit_after_rest", 0),
			(jump_to_menu, "mnu_town"),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(try_begin),
				(eq, "$g_player_besiege_town", "$g_encountered_party"),
				(jump_to_menu, "mnu_castle_besiege"),
			(try_end),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 2),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_leader, "trp_player"),
			(jump_to_menu, "mnu_enter_your_own_castle"),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 2),
			(ge, "$g_encountered_party_relation", 0),
			(this_or_next|eq, "$castle_undefended", 1),
			(this_or_next|eq, "$g_permitted_to_center", 1),
			(eq, "$g_encountered_party_faction", "$players_kingdom"),
			(jump_to_menu, "mnu_town"),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
			(ge, "$g_encountered_party_relation", 0),
			(jump_to_menu, "mnu_town"),
		(else_try),
			(eq, "$g_player_besiege_town", "$g_encountered_party"),
			(jump_to_menu, "mnu_castle_besiege"),
		(try_end),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(set_background_mesh, "mesh_pic_townriot"),
		(else_try),
			(call_script, "script_set_town_picture"),
		(try_end)
	],
	[
		("approach_gates",
		[
			(this_or_next|eq, "$entry_to_town_forbidden", 1),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 2)
		],
		"Approach the gates and hail the guard.",
		[
			(jump_to_menu, "mnu_castle_guard")
		], "."),

		("town_sneak",
		[
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(str_store_string, 7, "str_town"),
			(else_try),
				(str_store_string, 7, "str_castle"),
			(try_end),
			(eq, "$entry_to_town_forbidden", 1),
			(eq, "$cant_sneak_into_town", 0)
		],
		"Disguise yourself and try to sneak into the {s7}",
		[
			(faction_get_slot, ":g_encountered_party_faction_player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
			(party_get_num_companions, ":num_companions_main_party", "p_main_party"),
			(party_get_num_prisoners, ":num_prisoners_main_party", "p_main_party"),
			(val_add, ":num_companions_main_party", ":num_prisoners_main_party"),
			(val_mul, ":num_companions_main_party", 2),
			(val_div, ":num_companions_main_party", 3),
			(store_add, ":value", ":g_encountered_party_faction_player_alarm", ":num_companions_main_party"),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(try_begin),
				(this_or_next|ge, ":random_in_range_0_100", ":value"),
				(eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
				(assign, "$g_last_defeated_bandits_town", 0),
				(assign, "$sneaked_into_town", 1),
				(assign, "$town_entered", 1),
				(jump_to_menu, "mnu_sneak_into_town_suceeded"),
				(assign, "$g_mt_mode", 1),
			(else_try),
				(jump_to_menu, "mnu_sneak_into_town_caught"),
			(try_end)
		], "."),

		("dplmc_riot_start_siege",
		[
			(party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(lt, "$g_encountered_party_2", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(gt, reg0, 5),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(assign, reg6, 1),
			(else_try),
				(assign, reg6, 0),
			(try_end)
		],
		"Besiege the {reg6?town:castle} to counter the insurgency.",
		[
			(assign, "$g_player_besiege_town", "$g_encountered_party"),
			(jump_to_menu, "mnu_castle_besiege")
		], "."),

		("dplmc_riot_negotiate",
		[
			(party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(lt, "$g_encountered_party_2", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(gt, reg0, 5),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(assign, reg6, 1),
			(else_try),
				(assign, reg6, 0),
			(try_end)
		],
		"Begin negotiations.",
		[
			(jump_to_menu, "mnu_dplmc_riot_negotiate")
		], "."),

		("castle_start_siege",
		[
			(neg|party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
			(store_relation, ":relation_g_encountered_party_faction_player_supporters_faction", "$g_encountered_party_faction", "fac_player_supporters_faction"),
			(lt, ":relation_g_encountered_party_faction_player_supporters_faction", 0),
			(lt, "$g_encountered_party_2", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(gt, reg0, 5),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(assign, reg6, 1),
			(else_try),
				(assign, reg6, 0),
			(try_end)
		],
		"Besiege the {reg6?town:castle}.",
		[
			(assign, "$g_player_besiege_town", "$g_encountered_party"),
			(store_relation, ":relation_player_supporters_faction_g_encountered_party_faction", "fac_player_supporters_faction", "$g_encountered_party_faction"),
			(val_min, ":relation_player_supporters_faction_g_encountered_party_faction", -40),
			(call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation_player_supporters_faction_g_encountered_party_faction"),
			(call_script, "script_update_all_notes"),
			(jump_to_menu, "mnu_castle_besiege")
		], "."),

		("cheat_castle_start_siege",
		[
			(eq, "$cheat_mode", 1),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
			(store_relation, ":relation_g_encountered_party_faction_player_supporters_faction", "$g_encountered_party_faction", "fac_player_supporters_faction"),
			(ge, ":relation_g_encountered_party_faction_player_supporters_faction", 0),
			(lt, "$g_encountered_party_2", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(gt, reg0, 1),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(assign, reg6, 1),
			(else_try),
				(assign, reg6, 0),
			(try_end)
		],
		"{!}CHEAT: Besiege the {reg6?town:castle}...",
		[
			(assign, "$g_player_besiege_town", "$g_encountered_party"),
			(jump_to_menu, "mnu_castle_besiege")
		], "."),

		("castle_leave",
		[],
		"Leave.",
		[
			(change_screen_return, 0)
		], "."),

		("castle_cheat_interior",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Interior.",
		[
			(set_jump_mission, "mt_ai_training"),
			(party_get_slot, ":current_town_town_castle", "$current_town", slot_town_castle),
			(jump_to_scene, ":current_town_town_castle"),
			(change_screen_mission)
		], "."),

		("castle_cheat_exterior",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Exterior.",
		[
			(set_jump_mission, "mt_ai_training"),
			(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(jump_to_scene, ":current_town_town_center"),
			(change_screen_mission)
		], "."),

		("castle_cheat_town_walls",
		[
			(eq, "$cheat_mode", 1),
			(party_slot_eq, "$current_town", slot_party_type, 3)
		],
		"{!}CHEAT! Town Walls.",
		[
			(party_get_slot, ":current_town_town_walls", "$current_town", slot_town_walls),
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, ":current_town_town_walls"),
			(change_screen_mission)
		], ".")
	]
	),

	("castle_guard", 0, "You approach the gate. The men on the walls watch you closely.",
"none",
	[
		(call_script, "script_set_town_picture")
	],
	[
		("request_shelter",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_type, 2),
			(ge, "$g_encountered_party_relation", 0)
		],
		"Request entry to the castle.",
		[
			(party_get_slot, ":g_encountered_party_town_lord", "$g_encountered_party", slot_town_lord),
			(try_begin),
				(lt, ":g_encountered_party_town_lord", 0),
				(jump_to_menu, "mnu_castle_entry_granted"),
			(else_try),
				(call_script, "script_troop_get_player_relation", ":g_encountered_party_town_lord"),
				(assign, ":var_2", reg0),
				(try_begin),
					(gt, ":var_2", -15),
					(jump_to_menu, "mnu_castle_entry_granted"),
				(else_try),
					(jump_to_menu, "mnu_castle_entry_denied"),
				(try_end),
			(try_end)
		], "."),

		("request_meeting_commander",
		[],
		"Request a meeting with someone.",
		[
			(jump_to_menu, "mnu_castle_meeting")
		], "."),

		("guard_leave",
		[],
		"Leave.",
		[
			(change_screen_return, 0)
		], ".")
	]
	),

	("castle_entry_granted", 0, "After a brief wait, the guards open the gates for you and allow your party inside.",
"none",
	[
		(call_script, "script_set_town_picture")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("castle_entry_denied", 0, "The lord of this castle has forbidden you from coming inside these walls, and the guard sergeant informs you that his men will fire if you attempt to come any closer.",
"none",
	[
		(call_script, "script_set_town_picture")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_castle_guard")
		], ".")
	]
	),

	("castle_meeting", 0, "With whom do you want to meet?",
"none",
	[
		(assign, "$num_castle_meeting_troops", 0),
		(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
			(troop_slot_eq, ":troop", slot_troop_occupation, 2),
			(call_script, "script_get_troop_attached_party", ":troop"),
			(eq, "$g_encountered_party", reg0),
			(troop_set_slot, "trp_temp_array_a", "$num_castle_meeting_troops", ":troop"),
			(val_add, "$num_castle_meeting_troops", 1),
		(try_end),
		(call_script, "script_set_town_picture")
	],
	[
		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 0),
			(troop_get_slot, ":temp_array_a_relations_begin", "trp_temp_array_a", slot_troop_relations_begin),
			(str_store_troop_name, 5, ":temp_array_a_relations_begin")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_relations_begin),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 1),
			(troop_get_slot, ":temp_array_a_1", "trp_temp_array_a", 1),
			(str_store_troop_name, 5, ":temp_array_a_1")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 1),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 2),
			(troop_get_slot, ":temp_array_a_occupation", "trp_temp_array_a", slot_troop_occupation),
			(str_store_troop_name, 5, ":temp_array_a_occupation")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_occupation),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 3),
			(troop_get_slot, ":temp_array_a_state", "trp_temp_array_a", slot_troop_state),
			(str_store_troop_name, 5, ":temp_array_a_state")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_state),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 4),
			(troop_get_slot, ":temp_array_a_last_talk_time", "trp_temp_array_a", slot_troop_last_talk_time),
			(str_store_troop_name, 5, ":temp_array_a_last_talk_time")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_last_talk_time),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 5),
			(troop_get_slot, ":temp_array_a_met", "trp_temp_array_a", slot_troop_met),
			(str_store_troop_name, 5, ":temp_array_a_met")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_met),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 6),
			(troop_get_slot, ":temp_array_a_party_template", "trp_temp_array_a", slot_troop_party_template),
			(str_store_troop_name, 5, ":temp_array_a_party_template")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_party_template),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 7),
			(troop_get_slot, ":temp_array_a_renown", "trp_temp_array_a", slot_troop_renown),
			(str_store_troop_name, 5, ":temp_array_a_renown")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_renown),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 8),
			(troop_get_slot, ":temp_array_a_prisoner_of_party", "trp_temp_array_a", slot_troop_prisoner_of_party),
			(str_store_troop_name, 5, ":temp_array_a_prisoner_of_party")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_prisoner_of_party),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("guard_meet_s5",
		[
			(gt, "$num_castle_meeting_troops", 9),
			(troop_get_slot, ":temp_array_a_present_at_event", "trp_temp_array_a", slot_troop_present_at_event),
			(str_store_troop_name, 5, ":temp_array_a_present_at_event")
		],
		"{s5}.",
		[
			(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", slot_troop_present_at_event),
			(jump_to_menu, "mnu_castle_meeting_selected")
		], "."),

		("forget_it",
		[],
		"Forget it.",
		[
			(jump_to_menu, "mnu_castle_guard")
		], ".")
	]
	),

	("castle_meeting_selected", 0, "Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
"none",
	[
		(str_store_troop_name, 6, "$castle_meeting_selected_troop")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_castle_outside"),
			(modify_visitors_at_site, "scn_conversation_scene"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 17, "$castle_meeting_selected_troop"),
			(set_jump_mission, "mt_conversation_encounter"),
			(jump_to_scene, "scn_conversation_scene"),
			(assign, "$talk_context", 3),
			(change_screen_map_conversation, "$castle_meeting_selected_troop")
		], ".")
	]
	),

	("castle_besiege", 0, "You are laying siege to {s1}. {s2} {s3}",
"none",
	[
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_siege_sighted_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_siege_sighted"),
		(try_end),
		(assign, "$g_siege_force_wait", 0),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(party_set_slot, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
			(store_current_hours, ":current_hours"),
			(party_set_slot, "$g_encountered_party", slot_center_siege_begin_hours, ":current_hours"),
			(assign, "$g_siege_method", 0),
			(assign, "$g_siege_sallied_out_once", 0),
		(try_end),
		(party_get_slot, ":g_encountered_party_food_store", "$g_encountered_party", slot_party_food_store),
		(call_script, "script_center_get_food_consumption", "$g_encountered_party"),
		(assign, ":var_4", reg0),
		(assign, reg7, ":var_4"),
		(assign, reg8, ":g_encountered_party_food_store"),
		(store_div, reg3, ":g_encountered_party_food_store", ":var_4"),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
			(assign, reg6, 1),
		(else_try),
			(assign, reg6, 0),
		(try_end),
		(try_begin),
			(gt, reg3, 0),
			(str_store_string, 2, "@The {reg6?town's:castle's} food stores should last for {reg3} more days."),
		(else_try),
			(str_store_string, 2, "@The {reg6?town's:castle's} food stores have run out and the defenders are starving."),
		(try_end),
		(str_store_string, 3, "str_empty_string"),
		(try_begin),
			(ge, "$g_siege_method", 1),
			(store_current_hours, ":current_hours"),
			(try_begin),
				(lt, ":current_hours", "$g_siege_method_finish_hours"),
				(store_sub, reg9, "$g_siege_method_finish_hours", ":current_hours"),
				(try_begin),
					(eq, "$g_siege_method", 1),
					(str_store_string, 3, "@You're preparing to attack the walls, the work should finish in {reg9} hours."),
				(else_try),
					(eq, "$g_siege_method", 2),
					(str_store_string, 3, "@Your forces are building a siege tower. They estimate another {reg9} hours to complete the build."),
				(try_end),
			(else_try),
				(try_begin),
					(eq, "$g_siege_method", 1),
					(str_store_string, 3, "@You are ready to attack the walls at any time."),
				(else_try),
					(eq, "$g_siege_method", 2),
					(str_store_string, 3, "@The siege tower is built and ready to make an assault."),
				(try_end),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$g_castle_left_to_player", 1),
			(assign, "$g_castle_left_to_player", 0),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(party_set_faction, "$g_encountered_party", "fac_neutral"),
			(party_get_num_attached_parties, ":num_attached_parties_l_g_encountered_party", "$g_encountered_party"),
			(try_for_range_backwards, ":var_7", 0, ":num_attached_parties_l_g_encountered_party"),
				(party_get_attached_party_with_rank, ":attached_party_with_rank_g_encountered_party_var_7", "$g_encountered_party", ":var_7"),
				(party_detach, ":attached_party_with_rank_g_encountered_party_var_7"),
				(party_get_slot, ":attached_party_with_rank_g_encountered_party_var_7_type", ":attached_party_with_rank_g_encountered_party_var_7", slot_party_type),
				(eq, ":attached_party_with_rank_g_encountered_party_var_7_type", 13),
				(store_faction_of_party, ":faction_of_party_attached_party_with_rank_g_encountered_party_var_7", ":attached_party_with_rank_g_encountered_party_var_7"),
				(call_script, "script_get_closest_walled_center_of_faction", ":attached_party_with_rank_g_encountered_party_var_7", ":faction_of_party_attached_party_with_rank_g_encountered_party_var_7"),
				(try_begin),
					(gt, reg0, 0),
					(call_script, "script_party_set_ai_state", ":attached_party_with_rank_g_encountered_party_var_7", 7, reg0),
				(else_try),
					(call_script, "script_party_set_ai_state", ":attached_party_with_rank_g_encountered_party_var_7", 4, "$g_encountered_party"),
				(try_end),
			(try_end),
			(call_script, "script_party_remove_all_companions", "$g_encountered_party"),
			(change_screen_return),
			(party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),
			(call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"),
			(party_set_faction, "$g_encountered_party", ":faction_of_party_g_encountered_party"),
		(try_end),
		(assign, "$g_enemy_party", "$g_encountered_party"),
		(assign, "$g_ally_party", -1),
		(str_store_party_name, 1, "$g_encountered_party"),
		(call_script, "script_encounter_calculate_fit"),
		(assign, reg11, "$g_enemy_fit_for_battle"),
		(assign, reg10, "$g_friend_fit_for_battle"),
		(try_begin),
			(eq, "$g_leave_encounter", 1),
			(change_screen_return),
		(else_try),
			(call_script, "script_party_count_fit_regulars", "p_collective_enemy"),
			(assign, ":value", 0),
			(try_begin),
				(eq, "$g_battle_result", 1),
				(assign, ":value", 1),
			(else_try),
				(le, "$g_enemy_fit_for_battle", 0),
				(ge, "$g_friend_fit_for_battle", 1),
				(assign, ":value", 1),
			(try_end),
			(this_or_next|eq, ":value", 1),
			(eq, "$g_enemy_surrenders", 1),
			(assign, "$g_next_menu", "mnu_castle_taken"),
			(jump_to_menu, "mnu_total_victory"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(assign, ":var_12", reg0),
			(eq, "$g_battle_result", -1),
			(eq, ":var_12", 0),
			(assign, "$g_next_menu", "mnu_captivity_start_castle_defeat"),
			(jump_to_menu, "mnu_total_defeat"),
		(try_end)
	],
	[
		("siege_request_meeting",
		[
			(eq, "$cant_talk_to_enemy", 0)
		],
		"Call for a meeting with the castle commander.",
		[
			(assign, "$cant_talk_to_enemy", 1),
			(assign, "$g_enemy_surrenders", 0),
			(assign, "$g_castle_left_to_player", 0),
			(assign, "$talk_context", 7),
			(party_get_num_attached_parties, ":num_attached_parties_l_g_encountered_party", "$g_encountered_party"),
			(try_begin),
				(gt, ":num_attached_parties_l_g_encountered_party", 0),
				(party_get_attached_party_with_rank, ":attached_party_with_rank_g_encountered_party_0", "$g_encountered_party", 0),
				(call_script, "script_setup_party_meeting", ":attached_party_with_rank_g_encountered_party_0"),
			(else_try),
				(call_script, "script_setup_party_meeting", "$g_encountered_party"),
			(try_end)
		], "."),

		("wait_24_hours",
		[],
		"Wait until tomorrow.",
		[
			(assign, "$auto_besiege_town", "$g_encountered_party"),
			(assign, "$g_siege_force_wait", 1),
			(store_time_of_day, ":time_of_day"),
			(val_add, ":time_of_day", 1),
			(assign, ":var_2", 31),
			(val_sub, ":var_2", ":time_of_day"),
			(val_mod, ":var_2", 24),
			(val_add, ":var_2", 1),
			(rest_for_hours_interactive, ":var_2", 5, 1),
			(assign, "$cant_talk_to_enemy", 0),
			(change_screen_return)
		], "."),

		("castle_lead_attack",
		[
			(neg|troop_is_wounded, "trp_player"),
			(ge, "$g_siege_method", 1),
			(gt, "$g_friend_fit_for_battle", 3),
			(store_current_hours, ":current_hours"),
			(ge, ":current_hours", "$g_siege_method_finish_hours")
		],
		"Lead your soldiers in an assault.",
		[
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(party_get_slot, ":g_encountered_party_town_walls", "$g_encountered_party", slot_town_walls),
			(else_try),
				(party_get_slot, ":g_encountered_party_town_walls", "$g_encountered_party", slot_town_center),
			(try_end),
			(call_script, "script_calculate_renown_value"),
			(call_script, "script_calculate_battle_advantage"),
			(assign, ":var_2", reg0),
			(val_mul, ":var_2", 2),
			(val_div, ":var_2", 3),
			(set_battle_advantage, ":var_2"),
			(set_party_battle_mode),
			(assign, "$g_siege_battle_state", 1),
			(assign, ":value", 0),
			(try_begin),
				(le, ":var_2", -4),
				(eq, "$g_siege_sallied_out_once", 0),
				(set_jump_mission, "mt_castle_attack_walls_defenders_sally"),
				(assign, "$g_siege_battle_state", 0),
				(assign, ":value", 1),
			(else_try),
				(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
				(set_jump_mission, "mt_castle_attack_walls_belfry"),
			(else_try),
				(set_jump_mission, "mt_castle_attack_walls_ladder"),
			(try_end),
			(assign, "$cant_talk_to_enemy", 0),
			(assign, "$g_siege_final_menu", "mnu_castle_besiege"),
			(assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
			(assign, "$g_siege_method", 0),
			(jump_to_scene, ":g_encountered_party_town_walls"),
			(try_begin),
				(eq, ":value", 1),
				(jump_to_menu, "mnu_siege_attack_meets_sally"),
			(else_try),
				(jump_to_menu, "mnu_battle_debrief"),
				(change_screen_mission),
			(try_end)
		], "."),

		("attack_stay_back",
		[
			(ge, "$g_siege_method", 1),
			(gt, "$g_friend_fit_for_battle", 3),
			(store_current_hours, ":current_hours"),
			(ge, ":current_hours", "$g_siege_method_finish_hours")
		],
		"Order your soldiers to attack while you stay back...",
		[
			(assign, "$cant_talk_to_enemy", 0),
			(jump_to_menu, "mnu_castle_attack_walls_simulate")
		], "."),

		("build_ladders",
		[
			(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 0),
			(eq, "$g_siege_method", 0)
		],
		"Prepare ladders to attack the walls.",
		[
			(jump_to_menu, "mnu_construct_ladders")
		], "."),

		("build_siege_tower",
		[
			(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
			(eq, "$g_siege_method", 0)
		],
		"Build a siege tower.",
		[
			(jump_to_menu, "mnu_construct_siege_tower")
		], "."),

		("cheat_castle_lead_attack",
		[
			(eq, "$cheat_mode", 1),
			(eq, "$g_siege_method", 0)
		],
		"{!}CHEAT: Instant build equipments.",
		[
			(assign, "$g_siege_method", 1),
			(assign, "$g_siege_method_finish_hours", 0),
			(jump_to_menu, "mnu_castle_besiege")
		], "."),

		("cheat_conquer_castle",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT: Instant conquer castle.",
		[
			(assign, "$g_next_menu", "mnu_castle_taken"),
			(jump_to_menu, "mnu_total_victory")
		], "."),

		("lift_siege",
		[],
		"Abandon the siege.",
		[
			(call_script, "script_lift_siege", "$g_player_besiege_town", 0),
			(assign, "$g_player_besiege_town", -1),
			(change_screen_return)
		], ".")
	]
	),

	("siege_attack_meets_sally", 0, "The defenders sally out to meet your assault.",
"none",
	[
		(set_background_mesh, "mesh_pic_sally_out")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], ".")
	]
	),

	("siege_attack_meets_sally_player", 0, "Your forces sally out to delay the besiegers.",
"none",
	[
		(set_background_mesh, "mesh_pic_sally_out")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], ".")
	]
	),

	("castle_besiege_inner_battle", 0, "{s1}",
"none",
	[
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_siege_sighted_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_siege_sighted"),
		(try_end),
		(assign, ":var_2", "$g_battle_result"),
		(call_script, "script_encounter_calculate_fit"),
		(str_store_string, 1, "@As a last defensive effort, you retreat to the main hall of the keep. You and your remaining soldiers will put up a desperate fight here. If you are defeated, there's no other place to fall back to."),
		(str_store_string, 1, "@You've been driven away from the walls. Now the attackers are pouring into the streets. IF you can defeat them, you can perhaps turn the tide and save the day."),
		(try_begin),
			(this_or_next|neq, ":var_2", 1),
			(this_or_next|le, "$g_friend_fit_for_battle", 0),
			(le, "$g_enemy_fit_for_battle", 0),
			(jump_to_menu, "$g_siege_final_menu"),
		(else_try),
			(call_script, "script_encounter_calculate_fit"),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
			(try_begin),
				(eq, "$g_siege_battle_state", 0),
				(eq, ":var_2", 1),
				(assign, "$g_battle_result", 0),
				(jump_to_menu, "$g_siege_final_menu"),
			(else_try),
				(eq, "$g_siege_battle_state", 1),
				(eq, ":var_2", 1),
				(str_store_string, 1, "@You've breached the town walls, but the stubborn defenders continue to resist you in the streets! You'll have to deal with them before you can attack the keep at the heart of the town."),
			(else_try),
				(eq, "$g_siege_battle_state", 2),
				(eq, ":var_2", 1),
				(str_store_string, 1, "@The town centre is yours, but the remaining defenders have retreated to the castle. It must fall before you can complete your victory."),
			(else_try),
				(jump_to_menu, "$g_siege_final_menu"),
			(try_end),
		(else_try),
			(try_begin),
				(eq, "$g_siege_battle_state", 0),
				(eq, ":var_2", 1),
				(assign, "$g_battle_result", 0),
				(jump_to_menu, "$g_siege_final_menu"),
			(else_try),
				(eq, "$g_siege_battle_state", 1),
				(eq, ":var_2", 1),
				(str_store_string, 1, "@The remaining defenders have retreated to the castle as a last defense. You must go in and crush any remaining resistance."),
			(else_try),
				(jump_to_menu, "$g_siege_final_menu"),
			(try_end),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(try_begin),
					(eq, "$g_siege_battle_state", 1),
					(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
					(set_jump_mission, "mt_besiege_inner_battle_town_center"),
				(else_try),
					(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_castle),
					(set_jump_mission, "mt_besiege_inner_battle_castle"),
				(try_end),
			(else_try),
				(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_castle),
				(set_jump_mission, "mt_besiege_inner_battle_castle"),
			(try_end),
			(set_party_battle_mode),
			(jump_to_scene, ":g_encountered_party_town_center"),
			(val_add, "$g_siege_battle_state", 1),
			(assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], ".")
	]
	),

	("construct_ladders", 0, "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take {reg4} hours to build enough scaling ladders for the assault.",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		(assign, ":var_1", reg0),
		(assign, ":var_2", reg1),
		(assign, reg2, ":var_1"),
		(store_sub, reg4, 14, ":var_1"),
		(val_mul, reg4, 2),
		(try_begin),
			(eq, ":var_2", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 3, ":var_2"),
		(try_end)
	],
	[
		("build_ladders_cont",
		[],
		"Do it.",
		[
			(assign, "$g_siege_method", 1),
			(store_current_hours, ":current_hours"),
			(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
			(store_sub, ":value", 14, reg0),
			(val_mul, ":value", 2),
			(store_add, "$g_siege_method_finish_hours", ":current_hours", ":value"),
			(assign, "$auto_besiege_town", "$current_town"),
			(rest_for_hours_interactive, 96, 3, 1),
			(change_screen_return)
		], "."),

		("go_back",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_castle_besiege")
		], ".")
	]
	),

	("construct_siege_tower", 0, "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that building a siege tower will take {reg4} hours.",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		(assign, ":var_1", reg0),
		(assign, ":var_2", reg1),
		(assign, reg2, ":var_1"),
		(store_sub, reg4, 15, ":var_1"),
		(val_mul, reg4, 6),
		(try_begin),
			(eq, ":var_2", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 3, ":var_2"),
		(try_end)
	],
	[
		("build_siege_tower_cont",
		[],
		"Start building.",
		[
			(assign, "$g_siege_method", 2),
			(store_current_hours, ":current_hours"),
			(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
			(store_sub, ":value", 15, reg0),
			(val_mul, ":value", 2),
			(store_add, "$g_siege_method_finish_hours", ":current_hours", ":value"),
			(assign, "$auto_besiege_town", "$current_town"),
			(rest_for_hours_interactive, 240, 3, 1),
			(change_screen_return)
		], "."),

		("go_back",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_castle_besiege")
		], ".")
	]
	),

	("castle_attack_walls_simulate", 0, "{s4}^^Your casualties:{s8}^^Enemy casualties were: {s9}",
"none",
	[
		(try_begin),
			(set_background_mesh, "mesh_pic_siege_attack"),
		(try_end),
		(call_script, "script_party_calculate_strength", "p_main_party", 1),
		(assign, ":var_1", reg0),
		(val_div, ":var_1", 10),
		(call_script, "script_party_calculate_strength", "$g_encountered_party", 0),
		(assign, ":var_2", reg0),
		(val_div, ":var_2", 4),
		(inflict_casualties_to_party_group, "p_main_party", ":var_2", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 8, 0),
		(inflict_casualties_to_party_group, "$g_encountered_party", ":var_1", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 9, 0),
		(assign, "$no_soldiers_left", 0),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(le, reg0, 0),
			(assign, "$no_soldiers_left", 1),
			(str_store_string, 4, "str_attack_walls_failure"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "$g_encountered_party"),
			(le, reg0, 0),
			(assign, "$no_soldiers_left", 1),
			(assign, "$g_battle_result", 1),
			(str_store_string, 4, "str_attack_walls_success"),
		(else_try),
			(str_store_string, 4, "str_attack_walls_continue"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_castle_besiege")
		], ".")
	]
	),

	("castle_attack_walls_with_allies_simulate", 0, "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
"none",
	[
		(try_begin),
			(set_background_mesh, "mesh_pic_siege_attack"),
		(try_end),
		(call_script, "script_party_calculate_strength", "p_main_party", 1),
		(assign, ":var_1", reg0),
		(val_div, ":var_1", 10),
		(call_script, "script_party_calculate_strength", "p_collective_friends", 0),
		(assign, ":var_2", reg0),
		(val_div, ":var_2", 10),
		(val_max, ":var_2", 1),
		(call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
		(assign, ":var_3", reg0),
		(val_div, ":var_3", 4),
		(try_begin),
			(eq, ":var_2", 0),
			(store_div, ":value", ":var_3", 2),
		(else_try),
			(assign, ":value", ":var_3"),
			(val_mul, ":value", ":var_1"),
			(val_div, ":value", ":var_2"),
		(try_end),
		(val_sub, ":var_3", ":value"),
		(inflict_casualties_to_party_group, "p_main_party", ":value", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 8, 0),
		(inflict_casualties_to_party_group, "$g_enemy_party", ":var_2", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 10, 0),
		(call_script, "script_collect_friendly_parties"),
		(inflict_casualties_to_party_group, "$g_ally_party", ":var_3", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 9, 0),
		(party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
		(assign, "$no_soldiers_left", 0),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(le, reg0, 0),
			(assign, "$no_soldiers_left", 1),
			(str_store_string, 4, "str_attack_walls_failure"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
			(le, reg0, 0),
			(assign, "$no_soldiers_left", 1),
			(assign, "$g_battle_result", 1),
			(str_store_string, 4, "str_attack_walls_success"),
		(else_try),
			(str_store_string, 4, "str_attack_walls_continue"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_besiegers_camp_with_allies")
		], ".")
	]
	),

	("castle_taken_by_friends", 0, "Nothing to see here.",
"none",
	[
		(party_clear, "$g_encountered_party"),
		(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_2_0", "$g_encountered_party_2", 0),
		(party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, ":party_stack_troop_id_g_encountered_party_2_0"),
		(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_g_encountered_party_2_0", ":party_stack_troop_id_g_encountered_party_2_0"),
		(call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
		(try_begin),
			(assign, ":value", 60),
			(is_between, "$g_encountered_party", "p_town_1_1", "p_castle_1_1"),
			(assign, ":value", 120),
		(try_end),
		(try_begin),
			(neq, ":faction_of_troop_party_stack_troop_id_g_encountered_party_2_0", "$g_encountered_party_faction"),
			(call_script, "script_faction_inflict_war_damage_on_faction", ":faction_of_troop_party_stack_troop_id_g_encountered_party_2_0", "$g_encountered_party_faction", ":value"),
		(try_end),
		(call_script, "script_give_center_to_faction", "$g_encountered_party", ":faction_of_troop_party_stack_troop_id_g_encountered_party_2_0"),
		(call_script, "script_add_log_entry", 18, "trp_player", "$g_encountered_party", 0, "$g_encountered_party_faction"),
		(change_screen_return)
	],
	[]
	),

	("castle_taken", 0, "{s3} has fallen to your troops, and you now have full control of the {reg2?town:castle}.{reg1? You may station troops here to defend it against enemies who may try to recapture it. Also, you should select now whether you will hold the {reg2?town:castle} yourself or give it to a faithful vassal...:}",
"none",
	[
		(party_clear, "$g_encountered_party"),
		(try_begin),
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(party_get_slot, ":g_encountered_party_town_lord", "$g_encountered_party", slot_town_lord),
			(neq, ":g_encountered_party_town_lord", "trp_player"),
			(try_for_range, ":unused", 0, 4),
				(call_script, "script_cf_reinforce_party", "$g_encountered_party"),
			(try_end),
		(try_end),
		(call_script, "script_lift_siege", "$g_encountered_party", 0),
		(assign, "$g_player_besiege_town", -1),
		(party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
		(call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
		(call_script, "script_change_troop_renown", "trp_player", 5),
		(assign, ":value", 60),
		(try_begin),
			(is_between, "$g_encountered_party", "p_town_1_1", "p_castle_1_1"),
			(assign, ":value", 120),
		(try_end),
		(call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", "$g_encountered_party_faction", ":value"),
		(try_begin),
			(is_between, "$players_kingdom", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(neq, "$players_kingdom", "fac_player_supporters_faction"),
			(call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),
			(call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"),
			(jump_to_menu, "mnu_castle_taken_2"),
		(else_try),
			(call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_player_supporters_faction"),
			(call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_player_supporters_faction"),
			(str_store_party_name, 3, "$g_encountered_party"),
			(assign, reg1, 0),
			(try_begin),
				(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				(assign, reg1, 1),
			(try_end),
		(try_end),
		(assign, reg2, 0),
		(try_begin),
			(is_between, "$g_encountered_party", "p_town_1_1", "p_castle_1_1"),
			(assign, reg2, 1),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$auto_enter_town", "$g_encountered_party"),
			(change_screen_return)
		], ".")
	]
	),

	("castle_taken_2", 0, "{s3} has fallen to your troops, and you now have full control of the castle. It is time to send word to {s9} about your victory. {s5}",
"none",
	[
		(str_store_party_name, 3, "$g_encountered_party"),
		(str_clear, 5),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 9, ":players_kingdom_leader"),
		(try_begin),
			(eq, "$player_has_homage", 0),
			(assign, reg8, 0),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_ignore_player_until),
				(assign, reg8, 1),
			(try_end),
			(str_store_string, 5, "@However, since you are not a sworn {man/follower} of {s9}, there is no chance he would recognize you as the {lord/lady} of this {reg8?town:castle}."),
		(try_end)
	],
	[
		("castle_taken_claim",
		[
			(eq, "$player_has_homage", 1)
		],
		"Request that {s3} be awarded to you.",
		[
			(party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
			(assign, "$g_castle_requested_by_player", "$current_town"),
			(assign, "$g_castle_requested_for_troop", "trp_player"),
			(assign, "$auto_enter_town", "$g_encountered_party"),
			(change_screen_return)
		], "."),

		("castle_taken_claim_2",
		[
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(is_between, ":player_spouse", "trp_npc1", "trp_knight_1_1_wife"),
			(troop_slot_eq, ":player_spouse", slot_troop_occupation, 2),
			(store_faction_of_troop, ":faction_of_troop_player_spouse", ":player_spouse"),
			(eq, ":faction_of_troop_player_spouse", "$players_kingdom")
		],
		"Request that {s3} be awarded to your {wife/husband}.",
		[
			(party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
			(assign, "$g_castle_requested_by_player", "$current_town"),
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(assign, "$g_castle_requested_for_troop", ":player_spouse"),
			(assign, "$auto_enter_town", "$g_encountered_party"),
			(change_screen_return)
		], "."),

		("castle_taken_no_claim",
		[],
		"Ask no rewards.",
		[
			(party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
			(assign, "$auto_enter_town", "$g_encountered_party"),
			(change_screen_return)
		], ".")
	]
	),

	("requested_castle_granted_to_player", 0, "You receive a message from your liege, {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to you, with all due incomes and titles, to hold in {reg4?her:his} name for as long as you maintain your oath of homage..",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 3, ":players_kingdom_leader"),
		(str_store_party_name, 2, "$g_center_to_give_to_player"),
		(try_begin),
			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, 2),
			(assign, reg3, 1),
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(party_slot_eq, ":party", slot_village_bound_center, "$g_center_to_give_to_player"),
				(str_store_party_name, 4, ":party"),
			(try_end),
		(else_try),
			(assign, reg3, 0),
		(try_end),
		(troop_get_type, reg4, ":players_kingdom_leader")
	],
	[
		("continue",
		[],
		"Continue.",
		[
			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
			(jump_to_menu, "mnu_give_center_to_player_2")
		], ".")
	]
	),

	("requested_castle_granted_to_player_husband", 0, "You receive a message from your liege, {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to your husband, {s7}.",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 3, ":players_kingdom_leader"),
		(str_store_party_name, 2, "$g_center_to_give_to_player"),
		(try_begin),
			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, 2),
			(assign, reg3, 1),
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(party_slot_eq, ":party", slot_village_bound_center, "$g_center_to_give_to_player"),
				(str_store_party_name, 4, ":party"),
			(try_end),
		(else_try),
			(assign, reg3, 0),
		(try_end),
		(troop_get_type, reg4, ":players_kingdom_leader"),
		(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
		(str_store_troop_name, 11, ":player_spouse"),
		(str_store_string, 7, "str_to_your_husband_s11")
	],
	[
		("continue",
		[],
		"Continue.",
		[
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", ":player_spouse", 0)
		], ".")
	]
	),

	("requested_castle_granted_to_another", 0, "You receive a message from your monarch, {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested me to give you ownership of the castle, but that is a favour which I fear I cannot grant, as you already hold significant estates in my realm. Instead I have sent you {reg6} florins to cover the expenses of your campaign, but {s2} I give to {s5}.' ",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 3, ":players_kingdom_leader"),
		(str_store_party_name, 2, "$g_center_to_give_to_player"),
		(party_get_slot, ":g_center_to_give_to_player_town_lord", "$g_center_to_give_to_player", slot_town_lord),
		(str_store_troop_name, 5, ":g_center_to_give_to_player_town_lord"),
		(assign, reg6, 900),
		(assign, "$g_castle_requested_by_player", -1),
		(assign, "$g_castle_requested_for_troop", -1)
	],
	[
		("accept_decision",
		[],
		"Accept the decision.",
		[
			(call_script, "script_troop_add_gold", "trp_player", reg6),
			(change_screen_return)
		], "."),

		("leave_faction",
		[],
		"You have been wronged! Renounce your oath to your liege! ",
		[
			(jump_to_menu, "mnu_leave_faction"),
			(call_script, "script_troop_add_gold", "trp_player", reg6)
		], ".")
	]
	),

	("requested_castle_granted_to_another_female", 0, "You receive a message from your monarch, {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested me to give ownership of the castle to your husband, but that is a favour which I fear I cannot grant, as he already holds significant estates in my realm. Instead I have sent you {reg6} florins to cover the expenses of your campaign, but {s2} I give to {s5}.' ",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 3, ":players_kingdom_leader"),
		(str_store_party_name, 2, "$g_center_to_give_to_player"),
		(party_get_slot, ":g_center_to_give_to_player_town_lord", "$g_center_to_give_to_player", slot_town_lord),
		(str_store_troop_name, 5, ":g_center_to_give_to_player_town_lord"),
		(assign, reg6, 900),
		(assign, "$g_castle_requested_by_player", -1),
		(assign, "$g_castle_requested_for_troop", -1)
	],
	[
		("accept_decision",
		[],
		"Accept the decision.",
		[
			(call_script, "script_troop_add_gold", "trp_player", reg6),
			(change_screen_return)
		], ".")
	]
	),

	("leave_faction", 0, "Renouncing your oath is a grave act. Your lord may condemn you and confiscate your lands and holdings. However, if you return them of your own free will, he may let the betrayal go without a fight.",
"none",
	[],
	[
		("leave_faction_give_back",
		[],
		"Renounce your oath and give up your holdings.",
		[
			(call_script, "script_player_leave_faction", 1),
			(change_screen_return)
		], "."),

		("leave_faction_hold",
		[
			(str_store_party_name, 2, "$g_center_to_give_to_player")
		],
		"Renounce your oath and rule your lands, including {s2}, in your own name.",
		[
			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
			(call_script, "script_player_leave_faction", 0),
			(call_script, "script_activate_player_faction", "trp_player"),
			(change_screen_return)
		], "."),

		("leave_faction_cancel",
		[],
		"Remain loyal and accept the decision.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("give_center_to_player", 0, "Your lord offers to extend your fiefs! {s1} sends word that he is willing to grant {s2} to you in payment for your loyal service, adding it to your holdings. What is your answer?",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(store_faction_of_party, ":faction_of_party_g_center_to_give_to_player", "$g_center_to_give_to_player"),
		(faction_get_slot, ":faction_of_party_g_center_to_give_to_player_leader", ":faction_of_party_g_center_to_give_to_player", slot_faction_leader),
		(str_store_troop_name, 1, ":faction_of_party_g_center_to_give_to_player_leader"),
		(str_store_party_name, 2, "$g_center_to_give_to_player")
	],
	[
		("give_center_to_player_accept",
		[],
		"Accept the offer.",
		[
			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
			(jump_to_menu, "mnu_give_center_to_player_2")
		], "."),

		("give_center_to_player_reject",
		[],
		"Reject. You have no interest in holding {s2}.",
		[
			(party_set_slot, "$g_center_to_give_to_player", slot_town_lord, -3),
			(change_screen_return)
		], ".")
	]
	),

	("give_center_to_player_2", 0, "With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its bound village {s4}:}. {reg3?They:It} will make a fine part of your fiefdom. You can now claim the rents and revenues from your personal estates there, draft soldiers from the populace, and manage the lands as you see fit. However, you are also expected to defend your fief and your people from harm, as well as maintaining the rule of law and order.",
"none",
	[
		(str_store_party_name, 2, "$g_center_to_give_to_player"),
		(assign, reg3, 0),
		(try_begin),
			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, 2),
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(party_slot_eq, ":party", slot_village_bound_center, "$g_center_to_give_to_player"),
				(str_store_party_name, 4, ":party"),
				(assign, reg3, 1),
			(try_end),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("oath_fulfilled", 0, "You had a contract with {s1} to serve him for a certain duration. Your contract has now expired. What will you do?",
"none",
	[
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 1, ":players_kingdom_leader")
	],
	[
		("renew_oath",
		[
			(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
			(str_store_troop_name, 1, ":players_kingdom_leader")
		],
		"Renew your contract with {s1} for another month.",
		[
			(store_current_day, ":current_day"),
			(store_add, "$mercenary_service_next_renew_day", ":current_day", 30),
			(change_screen_return)
		], "."),

		("dont_renew_oath",
		[],
		"Become free of your bond.",
		[
			(call_script, "script_player_leave_faction", 1),
			(change_screen_return)
		], ".")
	]
	),

	("siege_started_defender", 0, "{s1} is launching an assault against the walls of {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. You decide to...",
"none",
	[
		(select_enemy, 1),
		(assign, "$g_enemy_party", "$g_encountered_party_2"),
		(assign, "$g_ally_party", "$g_encountered_party"),
		(str_store_party_name, 1, "$g_enemy_party"),
		(str_store_party_name, 2, "$g_ally_party"),
		(call_script, "script_encounter_calculate_fit"),
		(try_begin),
			(eq, "$g_siege_first_encounter", 1),
			(call_script, "script_let_nearby_parties_join_current_battle", 0, 1),
			(call_script, "script_encounter_init_variables"),
		(try_end),
		(try_begin),
			(eq, "$g_siege_first_encounter", 0),
			(try_begin),
				(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
				(assign, ":var_1", reg0),
				(call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
				(assign, ":var_2", reg0),
				(assign, ":value", 0),
				(try_begin),
					(eq, "$g_battle_result", 1),
					(eq, ":var_1", 0),
					(assign, ":value", 1),
				(else_try),
					(eq, "$g_engaged_enemy", 1),
					(le, "$g_enemy_fit_for_battle", 0),
					(ge, "$g_friend_fit_for_battle", 1),
					(assign, ":value", 1),
				(try_end),
				(this_or_next|eq, ":value", 1),
				(eq, "$g_enemy_surrenders", 1),
				(assign, "$g_next_menu", -1),
				(jump_to_menu, "mnu_total_victory"),
			(else_try),
				(assign, ":value_2", 0),
				(try_begin),
					(this_or_next|eq, "$g_battle_result", -1),
					(troop_is_wounded, "trp_player"),
					(eq, ":var_2", 0),
					(assign, ":value_2", 1),
				(try_end),
				(this_or_next|eq, ":value_2", 1),
				(eq, "$g_player_surrenders", 1),
				(assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
				(jump_to_menu, "mnu_total_defeat"),
			(else_try),
				(assign, ":value_3", 0),
				(try_begin),
					(eq, "$g_battle_result", 1),
					(assign, ":value_3", 1),
				(else_try),
					(eq, "$g_battle_result", 0),
					(store_div, ":value_4", "$g_enemy_fit_for_battle", 3),
					(lt, ":value_4", "$g_friend_fit_for_battle"),
					(assign, ":value_3", 1),
				(else_try),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(store_mul, ":value_5", ":var_2", 13),
					(val_div, ":value_5", 10),
					(ge, ":value_5", ":var_1"),
					(lt, ":random_in_range_0_100", 10),
					(neq, "$new_encounter", 1),
					(assign, ":value_3", 1),
				(try_end),
				(try_begin),
					(eq, ":value_3", 1),
					(party_get_slot, ":g_encountered_party_center_siege_hardness", "$g_encountered_party", slot_center_siege_hardness),
					(val_add, ":g_encountered_party_center_siege_hardness", 100),
					(party_set_slot, "$g_encountered_party", slot_center_siege_hardness, ":g_encountered_party_center_siege_hardness"),
					(party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),
					(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
						(troop_slot_eq, ":troop", slot_troop_occupation, 2),
						(neg|troop_slot_ge, ":troop", 8, 0),
						(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
						(gt, ":troop_leaded_party", 0),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_state, 1),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_object, "$g_encountered_party"),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_substate, 1),
						(call_script, "script_party_set_ai_state", ":troop_leaded_party", -1, -1),
						(call_script, "script_party_set_ai_state", ":troop_leaded_party", 1, "$g_encountered_party"),
					(try_end),
					(display_message, "@The enemy has been forced to retreat. The assault is over, but the siege continues."),
					(assign, "$g_battle_simulation_cancel_for_party", "$g_encountered_party"),
					(leave_encounter),
					(change_screen_return),
					(assign, "$g_battle_simulation_auto_enter_town_after_battle", "$g_encountered_party"),
				(try_end),
			(try_end),
		(try_end),
		(assign, "$g_siege_first_encounter", 0),
		(assign, "$new_encounter", 0)
	],
	[
		("dplmc_negotiate_with_besieger",
		[
			(neq, "$freelancer_state", 1),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(party_slot_ge, "$current_town", 54, 1)
		],
		"Negotiate with the besieger.",
		[
			(jump_to_menu, "mnu_dplmc_negotiate_besieger")
		], "."),

		("siege_defender_join_battle",
		[
			(neg|troop_is_wounded, "trp_player")
		],
		"Join the battle.",
		[
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(assign, "$g_battle_result", 0),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(party_get_slot, ":g_encountered_party_town_walls", "$g_encountered_party", slot_town_walls),
			(else_try),
				(party_get_slot, ":g_encountered_party_town_walls", "$g_encountered_party", slot_town_center),
			(try_end),
			(call_script, "script_calculate_battle_advantage"),
			(val_mul, reg0, 2),
			(val_div, reg0, 3),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(try_begin),
				(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
				(set_jump_mission, "mt_castle_attack_walls_belfry"),
			(else_try),
				(set_jump_mission, "mt_castle_attack_walls_ladder"),
			(try_end),
			(jump_to_scene, ":g_encountered_party_town_walls"),
			(assign, "$g_next_menu", "mnu_siege_started_defender"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("siege_defender_troops_join_battle",
		[
			(neq, "$freelancer_state", 1),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(this_or_next|troop_is_wounded, "trp_player"),
			(ge, reg0, 3)
		],
		"Order your men to join the battle without you.",
		[
			(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
			(select_enemy, 1),
			(assign, "$g_enemy_party", "$g_encountered_party_2"),
			(assign, "$g_ally_party", "$g_encountered_party"),
			(assign, "$g_siege_join", 1),
			(jump_to_menu, "mnu_siege_join_defense")
		], "."),

		("join_wounded",
		[
			(eq, "$freelancer_state", 1),
			(troop_is_wounded, "trp_player")
		],
		"You are too wounded to fight.",
		[
			(leave_encounter),
			(change_screen_map)
		], ".")
	]
	),

	("siege_join_defense", 0, "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
"none",
	[
		(try_begin),
			(eq, "$g_siege_join", 1),
			(call_script, "script_party_calculate_strength", "p_main_party", 1),
			(assign, ":value", reg0),
			(val_div, ":value", 5),
		(else_try),
			(assign, ":value", 0),
		(try_end),
		(call_script, "script_party_calculate_strength", "p_collective_ally", 0),
		(assign, ":var_2", reg0),
		(val_div, ":var_2", 5),
		(call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
		(assign, ":var_3", reg0),
		(val_div, ":var_3", 10),
		(store_add, ":value_2", ":value", ":var_2"),
		(try_begin),
			(eq, ":value_2", 0),
			(store_div, ":value_3", ":var_3", 2),
		(else_try),
			(assign, ":value_3", ":var_3"),
			(val_mul, ":value_3", ":value"),
			(val_div, ":value_3", ":value_2"),
		(try_end),
		(val_sub, ":var_3", ":value_3"),
		(inflict_casualties_to_party_group, "p_main_party", ":value_3", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 8, 0),
		(inflict_casualties_to_party_group, "$g_ally_party", ":var_3", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 9, 0),
		(party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),
		(inflict_casualties_to_party_group, "$g_enemy_party", ":value_2", "p_temp_casualties"),
		(call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
		(str_store_string_reg, 10, 0),
		(party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
		(try_begin),
			(call_script, "script_party_count_members_with_full_health", "p_main_party"),
			(le, reg0, 0),
			(str_store_string, 4, "str_siege_defender_order_attack_failure"),
		(else_try),
			(call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
			(le, reg0, 0),
			(assign, "$g_battle_result", 1),
			(str_store_string, 4, "str_siege_defender_order_attack_success"),
		(else_try),
			(str_store_string, 4, "str_siege_defender_order_attack_continue"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_siege_started_defender")
		], ".")
	]
	),

	("enter_your_own_castle", 0, "{s10}",
"none",
	[
		(try_begin),
			(neg|is_between, "$players_kingdom", "fac_kingdom_1", "fac_kingdoms_end"),
			(faction_get_slot, ":player_supporters_faction_leader", "fac_player_supporters_faction", slot_faction_leader),
			(eq, ":player_supporters_faction_leader", "trp_player"),
			(str_store_string, 10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {king/queen}."),
		(else_try),
			(str_store_string, 10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {lord/lady}."),
		(try_end),
		(str_store_party_name, 2, "$current_town")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("village", 0, "{s10} {s12}^{s11}^{s6}{s7}",
"none",
	[
		(assign, "$current_town", "$g_encountered_party"),
		(call_script, "script_update_center_recon_notes", "$current_town"),
		(assign, "$g_defending_against_siege", 0),
		(assign, "$g_battle_result", 0),
		(assign, "$qst_collect_taxes_currently_collecting", 0),
		(assign, "$qst_train_peasants_against_bandits_currently_training", 0),
		(try_begin),
			(gt, "$auto_enter_menu_in_center", 0),
			(jump_to_menu, "$auto_enter_menu_in_center"),
			(assign, "$auto_enter_menu_in_center", 0),
		(try_end),
		(try_begin),
			(neq, "$g_player_raiding_village", "$current_town"),
			(assign, "$g_player_raiding_village", 0),
		(else_try),
			(jump_to_menu, "mnu_village_loot_continue"),
		(try_end),
		(try_begin),
			(eq, "$g_town_visit_after_rest", 1),
			(assign, "$g_town_visit_after_rest", 0),
		(try_end),
		(str_store_party_name, 2, "$current_town"),
		(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
		(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
		(str_store_faction_name, 9, ":faction_of_party_current_town"),
		(try_begin),
			(ge, ":current_town_town_lord", 0),
			(str_store_troop_name, 8, ":current_town_town_lord"),
			(str_store_string, 7, "@{s8} of {s9}"),
		(try_end),
		(str_clear, 10),
		(str_clear, 12),
		(try_begin),
			(neg|party_slot_eq, "$current_town", slot_village_state, 2),
			(str_store_string, 60, 2),
			(party_get_slot, ":current_town_town_prosperity", "$current_town", slot_town_prosperity),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(assign, reg4, ":current_town_town_prosperity"),
				(display_message, "@{!}Prosperity: {reg4}"),
			(try_end),
			(store_div, ":value", ":current_town_town_prosperity", 10),
			(val_min, ":value", 9),
			(val_add, ":value", "str_village_prosperity_0"),
			(str_store_string, 10, ":value"),
			(store_div, ":value", ":current_town_town_prosperity", 20),
			(val_min, ":value", 4),
			(store_faction_of_party, ":faction_of_party_current_town_2", "$current_town"),
			(call_script, "script_raf_aor_faction_to_region", ":faction_of_party_current_town_2"),
			(try_begin),
				(this_or_next|eq, reg0, 10),
				(this_or_next|eq, reg0, 11),
				(eq, reg0, 12),
				(val_add, ":value", "str_oasis_village_alt_prosperity_0"),
			(else_try),
				(val_add, ":value", "str_village_alt_prosperity_0"),
			(try_end),
			(str_store_string, 12, ":value"),
		(try_end),
		(str_clear, 11),
		(try_begin),
			(party_slot_eq, "$current_town", slot_village_state, 2),
		(else_try),
			(eq, ":current_town_town_lord", "trp_player"),
			(str_store_string, 11, "@ This village and the surrounding lands belong to you."),
		(else_try),
			(ge, ":current_town_town_lord", 0),
			(str_store_string, 11, "@ You remember that this village and the surrounding lands belong to {s7}."),
		(else_try),
			(str_store_string, 11, "@ These lands belong to no one."),
		(try_end),
		(str_clear, 7),
		(try_begin),
			(neg|party_slot_eq, "$current_town", slot_village_state, 2),
			(party_get_slot, ":current_town_center_player_relation", "$current_town", slot_center_player_relation),
			(call_script, "script_describe_center_relation_to_s3", ":current_town_center_player_relation"),
			(assign, reg9, ":current_town_center_player_relation"),
			(str_store_string, 7, "@{!} {s3} ({reg9})."),
		(try_end),
		(str_clear, 6),
		(try_begin),
			(party_slot_ge, "$current_town", 39, 1),
			(party_get_slot, ":current_town_village_infested_by_bandits", "$current_town", slot_village_infested_by_bandits),
			(store_character_level, ":character_level_player", "trp_player"),
			(store_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":character_level_player", 10),
			(val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 12),
			(val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 10),
			(store_random_in_range, "$qst_eliminate_bandits_infesting_village_num_villagers", 25, 30),
			(assign, reg8, "$qst_eliminate_bandits_infesting_village_num_bandits"),
			(str_store_troop_name_by_count, 35, ":current_town_village_infested_by_bandits", "$qst_eliminate_bandits_infesting_village_num_bandits"),
			(str_store_string, 6, "@ The village is infested by {reg8} {s35}."),
			(assign, "$g_enemy_party", -1),
			(assign, "$g_ally_party", -1),
			(try_begin),
				(eq, ":current_town_village_infested_by_bandits", "trp_forest_bandit"),
				(set_background_mesh, "mesh_pic_forest_bandits"),
			(else_try),
				(eq, ":current_town_village_infested_by_bandits", "trp_steppe_bandit"),
				(set_background_mesh, "mesh_pic_steppe_bandits"),
			(else_try),
				(eq, ":current_town_village_infested_by_bandits", "trp_taiga_bandit"),
				(set_background_mesh, "mesh_pic_steppe_bandits"),
			(else_try),
				(eq, ":current_town_village_infested_by_bandits", "trp_mountain_bandit"),
				(set_background_mesh, "mesh_pic_mountain_bandits"),
			(else_try),
				(eq, ":current_town_village_infested_by_bandits", "trp_sea_raider"),
				(set_background_mesh, "mesh_pic_sea_raiders"),
			(else_try),
				(eq, ":current_town_village_infested_by_bandits", "trp_peasant_woman"),
				(str_store_string, 6, "@ The peasants hired mercenaries and are rebelling against you."),
				(set_background_mesh, "mesh_pic_villageriot"),
			(else_try),
				(set_background_mesh, "mesh_pic_bandits"),
			(try_end),
		(else_try),
			(party_slot_eq, "$current_town", slot_village_state, 2),
			(str_store_string, 6, "@ The village has been looted. A handful of souls scatter as you pass through the burnt out houses."),
			(try_begin),
				(neq, "$g_player_raid_complete", 1),
				(play_track, "track_empty_village", 1),
			(try_end),
			(set_background_mesh, "mesh_pic_looted_village"),
		(else_try),
			(party_slot_eq, "$current_town", slot_village_state, 1),
			(str_store_string, 6, "@ The village is being raided."),
		(else_try),
			(call_script, "script_set_town_picture"),
		(try_end),
		(try_begin),
			(eq, "$g_player_raid_complete", 1),
			(assign, "$g_player_raid_complete", 0),
			(jump_to_menu, "mnu_village_loot_complete"),
		(else_try),
			(party_get_slot, ":current_town_village_raided_by", "$current_town", slot_village_raided_by),
			(gt, ":current_town_village_raided_by", 0),
		(try_end),
		(try_begin),
			(eq, "$g_leave_town", 1),
			(assign, "$g_leave_town", 0),
			(change_screen_return),
		(try_end),
		(try_begin),
			(store_time_of_day, ":time_of_day"),
			(ge, ":time_of_day", 5),
			(lt, ":time_of_day", 21),
			(assign, "$town_nighttime", 0),
		(else_try),
			(assign, "$town_nighttime", 1),
		(try_end)
	],
	[
		("auto_sell",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1)
		],
		"Sell items automatically.",
		[
			(assign, "$g_next_menu", "mnu_village"),
			(jump_to_menu, "mnu_trade_auto_sell_begin")
		], "."),

		("auto_buy_food",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1)
		],
		"Buy food automatically.",
		[
			(assign, "$g_next_menu", "mnu_village"),
			(jump_to_menu, "mnu_trade_auto_buy_food_begin")
		], "."),

		("Meet_with_village_elder",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1)
		],
		"Meet with the elder.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(call_script, "script_start_town_conversation", 25, 11),
			(try_end)
		], "."),

		("village_manage",
		[
			(neg|party_slot_eq, "$current_town", slot_village_state, 2),
			(neg|party_slot_eq, "$current_town", slot_village_state, 1),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player")
		],
		"Manage this village.",
		[
			(assign, "$g_next_menu", "mnu_village"),
			(jump_to_menu, "mnu_center_manage")
		], "."),

		("recruit_volunteers",
		[
			(call_script, "script_cf_village_recruit_volunteers_cond"),
			(assign, ":value", 0),
			(try_begin),
				(eq, "$use_feudal_lance", 1),
				(assign, ":value", 1),
				(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
				(eq, ":current_town_town_lord", "trp_player"),
				(assign, ":value", 0),
			(try_end),
			(eq, ":value", 0)
		],
		"Recruit Volunteers.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(eq, "$use_feudal_lance", 0),
				(jump_to_menu, "mnu_recruit_volunteers"),
			(else_try),
				(eq, "$use_feudal_lance", 1),
				(jump_to_menu, "mnu_lance_recruitment"),
			(try_end)
		], "."),

		("call_retinue",
		[
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(neg|party_slot_eq, "$current_town", slot_village_state, 2),
			(neg|party_slot_eq, "$current_town", slot_village_state, 1),
			(this_or_next|eq, ":current_town_town_lord", "trp_player"),
			(ge, "$cheat_mode", 1)
		],
		"Invite local nobles to a hunt.",
		[
			(set_jump_mission, "mt_visit_town_castle"),
			(mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
			(call_script, "script_get_party_campsite", "$current_town"),
			(assign, ":var_1", reg0),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(faction_get_slot, ":faction_of_party_current_town_guard_troop", ":faction_of_party_current_town", slot_faction_guard_troop),
			(try_begin),
				(le, ":faction_of_party_current_town_guard_troop", 0),
				(assign, ":faction_of_party_current_town_guard_troop", "trp_euro_spearman_3"),
			(try_end),
			(set_visitor, 6, ":faction_of_party_current_town_guard_troop"),
			(set_visitor, 7, ":faction_of_party_current_town_guard_troop"),
			(assign, ":var_4", 16),
			(assign, reg5, 0),
			(party_get_slot, ":current_town_center_culture", "$current_town", slot_center_culture),
			(faction_get_slot, ":current_town_center_culture_101", ":current_town_center_culture", 101),
			(assign, ":value", -1),
			(assign, ":value_2", -1),
			(try_begin),
				(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_3"),
				(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_27"),
				(eq, ":current_town_center_culture", "fac_culture_mongol"),
				(faction_get_slot, ":current_town_center_culture_101", "fac_culture_mongol", 101),
				(assign, reg5, "$retinue_noble_mongol"),
				(val_add, "$retinue_noble_mongol", 1),
				(assign, ":value", "trp_npc13"),
				(assign, ":value_2", "trp_npc16"),
			(else_try),
				(eq, ":current_town_center_culture", "fac_culture_baltic"),
				(neq, ":faction_of_party_current_town", "fac_kingdom_1"),
				(assign, reg5, "$retinue_noble_balt"),
				(val_add, "$retinue_noble_balt", 1),
				(assign, ":value", "trp_npc1"),
				(assign, ":value_2", "trp_npc4"),
			(else_try),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_rus"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_serbian"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_balkan"),
				(eq, ":current_town_center_culture", "fac_culture_byzantium"),
				(assign, reg5, "$retinue_noble_orthodox"),
				(val_add, "$retinue_noble_orthodox", 1),
				(assign, ":value", "trp_npc7"),
				(assign, ":value_2", "trp_npc10"),
			(else_try),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_marinid"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_mamluke"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_andalus"),
				(eq, ":current_town_center_culture", "fac_culture_anatolian"),
				(assign, reg5, "$retinue_noble_muslim"),
				(val_add, "$retinue_noble_muslim", 1),
				(assign, ":value", "trp_npc10"),
				(assign, ":value_2", "trp_npc13"),
			(else_try),
				(assign, reg5, "$retinue_noble_west"),
				(val_add, "$retinue_noble_west", 1),
				(assign, ":value", "trp_npc4"),
				(assign, ":value_2", "trp_npc7"),
				(eq, ":faction_of_party_current_town", "fac_kingdom_1"),
				(faction_get_slot, ":current_town_center_culture_101", "fac_culture_teutonic", 101),
			(try_end),
			(try_for_range, ":var_9", ":value", ":value_2"),
				(neg|troop_slot_eq, ":var_9", 400, 1),
				(troop_slot_eq, ":var_9", slot_troop_current_mission, 0),
				(troop_slot_eq, ":var_9", slot_troop_occupation, 0),
				(neg|troop_slot_ge, ":var_9", 8, 0),
				(neq, ":var_9", "$g_player_minister"),
				(neq, ":var_9", "$g_player_chamberlain"),
				(neq, ":var_9", "$g_player_constable"),
				(set_visitor, ":var_4", ":var_9"),
				(val_add, ":var_4", 1),
				(eq, reg5, 0),
				(call_script, "script_equip_companion", ":var_9", ":current_town_center_culture_101"),
			(try_end),
			(assign, "$talk_context", 1),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("village_center",
		[
			(neg|party_slot_eq, "$current_town", slot_village_state, 2),
			(neg|party_slot_eq, "$current_town", slot_village_state, 1),
			(neg|party_slot_ge, "$current_town", 39, 1)
		],
		"Go to the Village center.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
				(modify_visitors_at_site, ":current_town_town_center"),
				(reset_visitors),
				(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
				(set_visitor, 11, ":current_town_town_elder"),
				(call_script, "script_init_town_walkers"),
				(try_begin),
					(check_quest_active, "qst_hunt_down_fugitive"),
					(neg|is_currently_night),
					(quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
					(neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
					(neg|check_quest_failed, "qst_hunt_down_fugitive"),
					(set_visitor, 45, "trp_fugitive"),
				(try_end),
				(set_jump_mission, "mt_village_center"),
				(jump_to_scene, ":current_town_town_center"),
				(change_screen_mission),
			(try_end)
		], "Door_to_the_village_center."),

		("village_buy_food",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1)
		],
		"Buy supplies from the peasants.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
				(change_screen_trade, ":current_town_town_elder"),
			(try_end)
		], "."),

		("village_attack_bandits",
		[
			(party_slot_ge, "$current_town", 39, 1),
			(neg|party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman")
		],
		"Attack the bandits.",
		[
			(party_get_slot, ":current_town_village_infested_by_bandits", "$current_town", slot_village_infested_by_bandits),
			(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(modify_visitors_at_site, ":current_town_town_center"),
			(reset_visitors),
			(set_visitors, 0, ":current_town_village_infested_by_bandits", "$qst_eliminate_bandits_infesting_village_num_bandits"),
			(set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_village_num_villagers"),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			(assign, "$g_battle_result", 0),
			(set_jump_mission, "mt_village_attack_bandits"),
			(jump_to_scene, ":current_town_town_center"),
			(assign, "$g_next_menu", "mnu_village_infest_bandits_result"),
			(jump_to_menu, "mnu_battle_debrief"),
			(assign, "$g_mt_mode", 1),
			(change_screen_mission)
		], "."),

		("village_wait",
		[
			(party_slot_eq, "$current_town", slot_center_has_manor, 1),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player")
		],
		"Wait here for some time.",
		[
			(assign, "$auto_enter_town", "$current_town"),
			(assign, "$g_last_rest_center", "$current_town"),
			(try_begin),
				(party_is_active, "p_main_party"),
				(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
				(try_begin),
					(eq, ":current_terrain_main_party", 5),
					(unlock_achievement, 28),
				(try_end),
			(try_end),
			(rest_for_hours_interactive, 168, 5, 1),
			(change_screen_return)
		], "."),

		("dplmc_village_counter_insurgency",
		[
			(party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman")
		],
		"Counter the insurgency.",
		[
			(store_random_in_range, ":random_in_range_-10_-5", -10, -5),
			(call_script, "script_change_player_relation_with_center", "$current_town", ":random_in_range_-10_-5"),
			(call_script, "script_calculate_battle_advantage"),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(assign, "$g_battle_result", 0),
			(assign, "$g_village_raid_evil", 1),
			(set_jump_mission, "mt_village_raid"),
			(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(jump_to_scene, ":current_town_town_center"),
			(assign, "$g_next_menu", "mnu_dplmc_village_riot_result"),
			(call_script, "script_objectionable_action", 3, "str_loot_village"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("dplmc_village_negotiate",
		[
			(party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman")
		],
		"Begin negotiations.",
		[
			(jump_to_menu, "mnu_dplmc_riot_negotiate")
		], "."),

		("village_spawn_manor",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(party_get_slot, ":current_town_299", "$current_town", 299),
			(le, ":current_town_299", 0)
		],
		"Invest into regional manor.",
		[
			(assign, "$g_next_menu", "mnu_village"),
			(jump_to_menu, "mnu_center_spawn_manor")
		], "."),

		("collect_taxes_qst",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(check_quest_active, "qst_collect_taxes"),
			(quest_get_slot, ":collect_taxes_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
			(quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
			(neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
			(str_store_troop_name, 1, ":collect_taxes_giver_troop"),
			(quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state)
		],
		"{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
		[
			(jump_to_menu, "mnu_collect_taxes")
		], "."),

		("train_peasants_against_bandits_qst",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(check_quest_active, "qst_train_peasants_against_bandits"),
			(neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
			(quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, "$current_town")
		],
		"Train the peasants.",
		[
			(jump_to_menu, "mnu_train_peasants_against_bandits")
		], "."),

		("village_hostile_action",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(neq, "$players_kingdom", "$g_encountered_party_faction")
		],
		"Take a hostile action.",
		[
			(jump_to_menu, "mnu_village_hostile_action")
		], "."),

		("village_reports",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Show reports.",
		[
			(jump_to_menu, "mnu_center_reports")
		], "."),

		("village_leave",
		[],
		"Leave...",
		[
			(change_screen_return, 0)
		], ".")
	]
	),

	("village_hostile_action", 0, "What action do you have in mind?",
"none",
	[],
	[
		("village_take_food",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
			(assign, ":value", 0),
			(try_for_range, ":number", 10, 106),
				(troop_get_inventory_slot, ":inventory_slot_current_town_town_elder_number", ":current_town_town_elder", ":number"),
				(ge, ":inventory_slot_current_town_town_elder_number", 0),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 1)
		],
		"Force the peasants to give you supplies.",
		[
			(jump_to_menu, "mnu_village_take_food_confirm")
		], "."),

		("village_steal_cattle",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(party_slot_eq, "$current_town", slot_village_player_can_not_steal_cattle, 0),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(party_get_slot, ":current_town_village_number_of_cattle", "$current_town", slot_village_number_of_cattle),
			(neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(gt, ":current_town_village_number_of_cattle", 0)
		],
		"Steal cattle.",
		[
			(jump_to_menu, "mnu_village_steal_cattle_confirm")
		], "."),

		("village_loot",
		[
			(party_slot_eq, "$current_town", slot_village_state, 0),
			(neg|party_slot_ge, "$current_town", 39, 1),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(store_relation, ":relation_player_supporters_faction_faction_of_party_current_town", "fac_player_supporters_faction", ":faction_of_party_current_town"),
			(lt, ":relation_player_supporters_faction_faction_of_party_current_town", 0)
		],
		"Loot and burn this village.",
		[
			(jump_to_menu, "mnu_village_start_attack")
		], "."),

		("forget_it",
		[],
		"Forget it.",
		[
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("recruit_volunteers", 0, "{s18}",
"none",
	[
		(party_get_slot, ":current_town_center_volunteer_troop_type", "$current_town", slot_center_volunteer_troop_type),
		(party_get_slot, ":current_town_center_volunteer_troop_amount", "$current_town", slot_center_volunteer_troop_amount),
		(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
		(val_min, ":current_town_center_volunteer_troop_amount", ":free_companions_capacity_main_party"),
		(store_troop_gold, ":troop_gold_player", "trp_player"),
		(store_div, ":value", ":troop_gold_player", 10),
		(val_min, ":current_town_center_volunteer_troop_amount", ":value"),
		(assign, reg5, ":current_town_center_volunteer_troop_amount"),
		(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
		(try_begin),
			(faction_slot_eq, ":faction_of_party_current_town", 102, 0),
			(try_begin),
				(eq, "$players_kingdom", "fac_kingdom_1"),
				(eq, ":faction_of_party_current_town", "fac_kingdom_6"),
				(try_begin),
					(party_slot_eq, "$current_town", slot_party_type, 2),
					(assign, ":current_town_center_volunteer_troop_type", "trp_teu_horse_1"),
				(else_try),
					(party_slot_eq, "$current_town", slot_party_type, 3),
					(assign, ":current_town_center_volunteer_troop_type", "trp_teu_town_1"),
				(try_end),
			(try_end),
			(party_set_slot, "$current_town", slot_center_volunteer_troop_type, ":current_town_center_volunteer_troop_type"),
		(try_end),
		(try_begin),
			(eq, ":current_town_center_volunteer_troop_amount", 0),
			(str_store_string, 18, "@No one here seems to be willing to join your party."),
		(else_try),
			(assign, ":value_2", 10),
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(assign, ":value_2", 75),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(assign, ":value_2", 12),
			(try_end),
			(store_mul, reg6, ":current_town_center_volunteer_troop_amount", ":value_2"),
			(store_mul, reg7, 1, ":value_2"),
			(str_store_troop_name_by_count, 3, ":current_town_center_volunteer_troop_type", ":current_town_center_volunteer_troop_amount"),
			(try_begin),
				(eq, reg5, 1),
				(str_store_string, 18, "@One {s3} volunteers to follow you."),
			(else_try),
				(str_store_string, 18, "@{reg5} {s3} volunteer to follow you."),
			(try_end),
			(set_background_mesh, "mesh_pic_recruits"),
		(try_end)
	],
	[
		("continue",
		[
			(eq, reg5, 0)
		],
		"Continue...",
		[
			(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("recruit_them",
		[
			(gt, reg5, 0)
		],
		"Recruit all of them ({reg6} florins).",
		[
			(call_script, "script_village_recruit_volunteers_recruit", -1),
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("recruit_one_of_them",
		[
			(gt, reg5, 0)
		],
		"Recruit one of them ({reg7} florins).",
		[
			(call_script, "script_village_recruit_volunteers_recruit", 1),
			(try_begin),
				(party_get_slot, ":current_town_center_volunteer_troop_amount", "$current_town", slot_center_volunteer_troop_amount),
				(gt, ":current_town_center_volunteer_troop_amount", 0),
				(jump_to_menu, "mnu_recruit_volunteers"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("forget_it",
		[
			(gt, reg5, 0)
		],
		"Forget it.",
		[
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], ".")
	]
	),

	("village_hunt_down_fugitive_defeated", 0, "A heavy blow from the fugitive sends you to the ground, and your vision spins and goes dark. Time passes. When you open your eyes again you find yourself battered and bloody, but luckily none of the wounds appear to be lethal.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("village_infest_bandits_result", 0, "{s9}",
"none",
	[
		(try_begin),
			(eq, "$g_battle_result", 1),
			(jump_to_menu, "mnu_village_infestation_removed"),
		(else_try),
			(str_store_string, 9, "@Try as you might, you could not defeat the bandits. Infuriated, they raze the village to the ground to punish the peasants, and then leave the burning wasteland behind to find greener pastures to plunder."),
			(set_background_mesh, "mesh_pic_looted_village"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(call_script, "script_village_set_state", "$current_town", 2),
			(party_set_slot, "$current_town", slot_village_raid_progress, 0),
			(party_set_slot, "$current_town", slot_village_recover_progress, 0),
			(try_begin),
				(check_quest_active, "qst_eliminate_bandits_infesting_village"),
				(quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
				(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),
				(call_script, "script_fail_quest", "qst_eliminate_bandits_infesting_village"),
				(call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
			(else_try),
				(check_quest_active, "qst_deal_with_bandits_at_lords_village"),
				(quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
				(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -4),
				(call_script, "script_fail_quest", "qst_deal_with_bandits_at_lords_village"),
				(call_script, "script_end_quest", "qst_deal_with_bandits_at_lords_village"),
			(else_try),
				(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
			(try_end),
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("village_infestation_removed", 0, "In a battle worthy of song, you and your men drive the bandits out of the village, making it safe once more. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find.",
"none",
	[
		(party_get_slot, ":g_encountered_party_village_infested_by_bandits", "$g_encountered_party", slot_village_infested_by_bandits),
		(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
		(party_clear, "p_temp_party"),
		(party_add_members, "p_temp_party", ":g_encountered_party_village_infested_by_bandits", "$qst_eliminate_bandits_infesting_village_num_bandits"),
		(assign, "$g_strength_contribution_of_player", 50),
		(call_script, "script_party_give_xp_and_gold", "p_temp_party"),
		(try_begin),
			(check_quest_active, "qst_eliminate_bandits_infesting_village"),
			(quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
			(call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 5),
		(else_try),
			(check_quest_active, "qst_deal_with_bandits_at_lords_village"),
			(quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
			(call_script, "script_succeed_quest", "qst_deal_with_bandits_at_lords_village"),
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
		(else_try),
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
		(try_end),
		(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
		(try_for_range, ":number", 10, 106),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(lt, ":random_in_range_0_100", 70),
			(troop_set_inventory_slot, ":current_town_town_elder", ":number", -1),
		(try_end)
	],
	[
		("village_bandits_defeated_accept",
		[],
		"Take it as your just due.",
		[
			(jump_to_menu, "mnu_village"),
			(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
			(troop_sort_inventory, ":current_town_town_elder"),
			(change_screen_loot, ":current_town_town_elder")
		], "."),

		("village_bandits_defeated_cont",
		[],
		"Refuse, stating that they need these items more than you do.",
		[
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
			(call_script, "script_change_player_honor", 1),
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("center_manage", 0, "{s19}^{reg6?^^You are currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}",
"none",
	[
		(assign, ":var_1", 0),
		(str_clear, 18),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(assign, ":value", 130),
			(assign, ":value_2", 135),
			(str_store_string, 17, "@village"),
		(else_try),
			(assign, ":value", 134),
			(assign, ":value_2", 136),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
			(str_store_string, 17, "@town"),
		(else_try),
			(str_store_string, 17, "@castle"),
		(try_end),
		(try_for_range, ":var_4", ":value", ":value_2"),
			(party_slot_ge, "$g_encountered_party", ":var_4", 1),
			(val_add, ":var_1", 1),
			(call_script, "script_get_improvement_details", ":var_4"),
			(try_begin),
				(eq, ":var_1", 1),
				(str_store_string, 18, "@{!}{s0}"),
			(else_try),
				(str_store_string, 18, "@{!}{s18}, {s0}"),
			(try_end),
		(try_end),
		(try_begin),
			(eq, ":var_1", 0),
			(str_store_string, 19, "@The {s17} has no improvements."),
		(else_try),
			(str_store_string, 19, "@The {s17} has the following improvements:{s18}."),
		(try_end),
		(assign, reg6, 0),
		(try_begin),
			(party_get_slot, ":g_encountered_party_center_current_improvement", "$g_encountered_party", slot_center_current_improvement),
			(gt, ":g_encountered_party_center_current_improvement", 0),
			(call_script, "script_get_improvement_details", ":g_encountered_party_center_current_improvement"),
			(str_store_string, 7, 0),
			(assign, reg6, 1),
			(store_current_hours, ":current_hours"),
			(party_get_slot, ":g_encountered_party_center_improvement_end_hour", "$g_encountered_party", slot_center_improvement_end_hour),
			(val_sub, ":g_encountered_party_center_improvement_end_hour", ":current_hours"),
			(store_div, reg8, ":g_encountered_party_center_improvement_end_hour", 24),
			(val_max, reg8, 1),
			(store_sub, reg9, reg8, 1),
		(try_end)
	],
	[
		("center_build_manor",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(party_slot_eq, "$g_encountered_party", slot_center_has_manor, 0)
		],
		"Build a manor house.",
		[
			(assign, "$g_improvement_type", 130),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_castle_1",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(party_slot_eq, "$g_encountered_party", slot_center_has_manor, 1),
			(neg|party_is_active, "p_castle_player")
		],
		"Fortify your manor house.",
		[
			(assign, "$g_improvement_type", 248),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_fish_pond",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(party_slot_eq, "$g_encountered_party", slot_center_has_fish_pond, 0)
		],
		"Build a mill.",
		[
			(assign, "$g_improvement_type", 131),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_watch_tower",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(party_slot_eq, "$g_encountered_party", slot_center_has_watch_tower, 0)
		],
		"Build a watch tower.",
		[
			(assign, "$g_improvement_type", 132),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_school",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(party_slot_eq, "$g_encountered_party", slot_center_has_school, 0)
		],
		"Build a school.",
		[
			(assign, "$g_improvement_type", 133),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_messenger_post",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_center_has_messenger_post, 0)
		],
		"Build a messenger post.",
		[
			(assign, "$g_improvement_type", 134),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_prisoner_tower",
		[
			(eq, reg6, 0),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, 3),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 2),
			(party_slot_eq, "$g_encountered_party", slot_center_has_prisoner_tower, 0)
		],
		"Build a prisoner tower.",
		[
			(assign, "$g_improvement_type", 135),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_fortifications_1",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 2),
			(neg|party_slot_eq, "$g_encountered_party", 252, 1),
			(neg|party_slot_eq, "$g_encountered_party", 253, 1),
			(eq, "$g_encountered_party", "p_castle_player"),
			(display_message, "@fort castle player")
		],
		"Improve the fortifications.",
		[
			(assign, "$g_improvement_type", 252),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("center_build_fortifications_2",
		[
			(eq, reg6, 0),
			(party_slot_eq, "$g_encountered_party", 252, 1),
			(neg|party_slot_eq, "$g_encountered_party", 253, 1),
			(eq, "$g_encountered_party", "p_castle_player")
		],
		"Improve the fortifications.",
		[
			(assign, "$g_improvement_type", 253),
			(jump_to_menu, "mnu_center_improve")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "$g_next_menu")
		], ".")
	]
	),

	("center_improve", 0, "{s19} As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you {reg5} florins and will take {reg6} days.",
"none",
	[
		(call_script, "script_get_improvement_details", "$g_improvement_type"),
		(assign, ":var_1", reg0),
		(str_store_string, 4, 0),
		(str_store_string, 19, 1),
		(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		(assign, ":var_2", reg0),
		(assign, ":var_3", reg1),
		(assign, reg2, ":var_2"),
		(store_sub, ":value", 20, ":var_2"),
		(val_mul, ":var_1", ":value"),
		(val_div, ":var_1", 20),
		(store_div, ":value_2", ":var_1", 100),
		(val_add, ":value_2", 3),
		(val_div, ":value_2", 4),
		(try_begin),
			(this_or_next|eq, "$g_improvement_type", 252),
			(this_or_next|eq, "$g_improvement_type", 253),
			(eq, "$g_improvement_type", 248),
			(val_div, ":value_2", 5),
		(try_end),
		(assign, reg5, ":var_1"),
		(assign, reg6, ":value_2"),
		(try_begin),
			(eq, ":var_3", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 3, ":var_3"),
		(try_end)
	],
	[
		("dplmc_improve_cont",
		[
			(gt, "$g_player_chamberlain", 0),
			(store_troop_gold, ":troop_gold_household_possessions", "trp_household_possessions"),
			(ge, ":troop_gold_household_possessions", reg5)
		],
		"Go on. (Pay from treasury)",
		[
			(call_script, "script_dplmc_withdraw_from_treasury", reg5),
			(party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
			(store_current_hours, ":current_hours"),
			(store_mul, ":value", reg6, 24),
			(val_add, ":value", ":current_hours"),
			(party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":value"),
			(jump_to_menu, "mnu_center_manage")
		], "."),

		("improve_cont",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg5)
		],
		"Go on.",
		[
			(troop_remove_gold, "trp_player", reg5),
			(party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
			(store_current_hours, ":current_hours"),
			(store_mul, ":value", reg6, 24),
			(val_add, ":value", ":current_hours"),
			(party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":value"),
			(jump_to_menu, "mnu_center_manage")
		], "."),

		("forget_it",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(store_troop_gold, ":troop_gold_household_possessions", "trp_household_possessions"),
			(this_or_next|ge, ":troop_gold_household_possessions", reg5),
			(ge, ":troop_gold_player", reg5)
		],
		"Forget it.",
		[
			(jump_to_menu, "mnu_center_manage")
		], "."),

		("improve_not_enough_gold",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(store_troop_gold, ":troop_gold_household_possessions", "trp_household_possessions"),
			(this_or_next|lt, ":troop_gold_household_possessions", reg5),
			(lt, ":troop_gold_player", reg5)
		],
		"I don't have enough money for that.",
		[
			(jump_to_menu, "mnu_center_manage")
		], ".")
	]
	),

	("town_bandits_failed", 0, "{s4} {s5}",
"none",
	[
		(store_troop_gold, ":troop_gold_player", "trp_player"),
		(store_div, ":value", ":troop_gold_player", 30),
		(store_random_in_range, ":random_in_range_40_100", 40, 100),
		(val_add, ":value", ":random_in_range_40_100"),
		(val_min, ":value", ":troop_gold_player"),
		(troop_remove_gold, "trp_player", ":value"),
		(party_set_slot, "$current_town", slot_center_has_bandits, 0),
		(party_get_num_companions, ":num_companions_main_party", "p_main_party"),
		(str_store_string, 4, "@The assasins beat you down and leave you for dead. ."),
		(str_store_string, 4, "@You have fallen. The bandits quickly search your body for every coin they can find, then vanish into the night. They have left you alive, if only barely."),
		(try_begin),
			(gt, ":num_companions_main_party", 2),
			(str_store_string, 5, "@Luckily some of your companions come to search for you when you do not return, and find you lying by the side of the road. They hurry you to safety and dress your wounds."),
		(else_try),
			(str_store_string, 5, "@Luckily some passing townspeople find you lying by the side of the road, and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds."),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("town_bandits_succeeded", 0, "The bandits fall before you as wheat to a scythe! Soon you stand alone in the streets while most of your attackers lie unconscious, dead or dying. Searching the bodies, you find a purse which must have belonged to a previous victim of these brutes. Or perhaps, it was given to them by someone who wanted to arrange a suitable ending to your life.",
"none",
	[
		(party_set_slot, "$current_town", slot_center_has_bandits, 0),
		(assign, "$g_last_defeated_bandits_town", "$g_encountered_party"),
		(try_begin),
			(check_quest_active, "qst_deal_with_night_bandits"),
			(neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
			(quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, "$g_encountered_party"),
			(call_script, "script_succeed_quest", "qst_deal_with_night_bandits"),
		(try_end),
		(store_mul, ":value", "$num_center_bandits", 117),
		(add_xp_to_troop, ":value", "trp_player"),
		(store_mul, ":value_2", "$num_center_bandits", 50),
		(call_script, "script_troop_add_gold", "trp_player", ":value_2")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("village_steal_cattle_confirm", 0, "As the party member with the highest looting skill ({reg2}), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} heads of village's cattle.",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_looting"),
		(assign, reg2, reg0),
		(assign, ":var_1", reg1),
		(try_begin),
			(eq, ":var_1", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 1, ":var_1"),
		(try_end),
		(call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
		(assign, reg4, reg0)
	],
	[
		("village_steal_cattle_confirm",
		[],
		"Go on.",
		[
			(rest_for_hours_interactive, 3, 3, 1),
			(assign, "$auto_menu", "mnu_village_steal_cattle"),
			(change_screen_return)
		], "."),

		("forget_it",
		[],
		"Forget it.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("village_steal_cattle", 0, "{s1}",
"none",
	[
		(call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
		(assign, ":var_1", reg0),
		(val_add, ":var_1", 1),
		(store_random_in_range, ":random_in_range_0_var_1", 0, ":var_1"),
		(party_set_slot, "$current_town", slot_village_player_can_not_steal_cattle, 1),
		(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
		(try_begin),
			(le, ":random_in_range_0_var_1", 0),
			(call_script, "script_change_player_relation_with_center", "$current_town", -3),
			(str_store_string, 1, "@You fail to steal any cattle."),
		(else_try),
			(assign, reg17, ":random_in_range_0_var_1"),
			(store_sub, reg12, ":random_in_range_0_var_1", 1),
			(try_begin),
				(gt, ":current_town_town_lord", 0),
				(call_script, "script_change_player_relation_with_troop", ":current_town_town_lord", -3),
				(call_script, "script_add_log_entry", 66, "trp_player", "$current_town", ":current_town_town_lord", "$g_encountered_party_faction"),
			(try_end),
			(call_script, "script_change_player_relation_with_center", "$current_town", -5),
			(str_store_string, 1, "@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd."),
			(try_begin),
				(eq, ":random_in_range_0_var_1", 3),
				(unlock_achievement, 31),
			(try_end),
			(call_script, "script_create_cattle_herd", "$current_town", ":random_in_range_0_var_1"),
			(party_get_slot, ":current_town_village_number_of_cattle", "$current_town", slot_village_number_of_cattle),
			(val_sub, ":current_town_village_number_of_cattle", ":random_in_range_0_var_1"),
			(party_set_slot, "$current_town", slot_village_number_of_cattle, ":current_town_village_number_of_cattle"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("village_take_food_confirm", 0, "It will be difficult to force and threaten the peasants into giving their precious supplies. You think you will need at least one hour.",
"none",
	[],
	[
		("village_take_food_confirm",
		[],
		"Go ahead.",
		[
			(rest_for_hours_interactive, 1, 5, 0),
			(assign, "$auto_enter_town", "$current_town"),
			(assign, "$g_town_visit_after_rest", 1),
			(assign, "$auto_enter_menu_in_center", "mnu_village_take_food"),
			(change_screen_return)
		], "."),

		("forget_it",
		[],
		"Forget it.",
		[
			(jump_to_menu, "mnu_village_hostile_action")
		], ".")
	]
	),

	("village_take_food", 0, "The villagers grudgingly bring out what they have for you.",
"none",
	[
		(call_script, "script_party_count_members_with_full_health", "p_main_party"),
		(assign, ":var_1", reg0),
		(call_script, "script_party_count_members_with_full_health", "$current_town"),
		(assign, ":var_2", reg0),
		(try_begin),
			(lt, ":var_1", 6),
			(ge, ":var_2", 40),
			(neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(jump_to_menu, "mnu_village_start_attack"),
		(try_end)
	],
	[
		("take_supplies",
		[],
		"Take the supplies.",
		[
			(try_begin),
				(party_slot_ge, "$current_town", 26, -55),
				(try_begin),
					(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
					(call_script, "script_change_player_relation_with_center", "$current_town", -1),
				(else_try),
					(call_script, "script_change_player_relation_with_center", "$current_town", -3),
				(try_end),
			(try_end),
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(try_begin),
				(gt, ":current_town_town_lord", 1),
				(call_script, "script_change_player_relation_with_troop", ":current_town_town_lord", -1),
			(try_end),
			(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
			(party_get_skill_level, ":skill_level_main_party_looting", "p_main_party", "skl_looting"),
			(val_mul, ":skill_level_main_party_looting", 3),
			(store_sub, ":value", 70, ":skill_level_main_party_looting"),
			(try_for_range, ":number", 10, 106),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(lt, ":random_in_range_0_100", ":value"),
				(troop_set_inventory_slot, ":current_town_town_elder", ":number", -1),
			(try_end),
			(call_script, "script_objectionable_action", 3, "str_steal_from_villagers"),
			(call_script, "script_add_log_entry", 2, "trp_player", "$current_town", -1, -1),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", ":faction_of_party_current_town", 5),
			(jump_to_menu, "mnu_village"),
			(troop_sort_inventory, ":current_town_town_elder"),
			(change_screen_loot, ":current_town_town_elder")
		], "."),

		("let_them_keep_it",
		[],
		"Let them keep it.",
		[
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("village_start_attack", 0, "Some of the angry villagers grab their tools and prepare to resist you. It looks like you'll have a fight on your hands if you continue.",
"none",
	[
		(set_background_mesh, "mesh_pic_villageriot"),
		(call_script, "script_party_count_members_with_full_health", "p_main_party"),
		(assign, ":var_1", reg0),
		(call_script, "script_party_count_members_with_full_health", "$current_town"),
		(assign, ":var_2", reg0),
		(try_begin),
			(gt, ":var_1", 25),
			(jump_to_menu, "mnu_village_loot_no_resist"),
		(else_try),
			(this_or_next|eq, ":var_2", 0),
			(eq, "$g_battle_result", 1),
			(try_begin),
				(eq, "$g_battle_result", 1),
				(store_random_in_range, ":random_in_range_-30_-15", -30, -15),
				(call_script, "script_change_player_relation_with_center", "$current_town", ":random_in_range_-30_-15"),
				(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
				(gt, ":current_town_town_lord", 0),
				(call_script, "script_change_player_relation_with_troop", ":current_town_town_lord", -3),
			(try_end),
			(jump_to_menu, "mnu_village_loot_no_resist"),
		(else_try),
			(eq, "$g_battle_result", -1),
			(jump_to_menu, "mnu_village_loot_defeat"),
		(try_end)
	],
	[
		("village_raid_attack",
		[],
		"Charge them.",
		[
			(store_random_in_range, ":random_in_range_-10_-5", -10, -5),
			(call_script, "script_change_player_relation_with_center", "$current_town", ":random_in_range_-10_-5"),
			(try_begin),
				(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
				(gt, ":current_town_town_lord", 0),
				(call_script, "script_change_player_relation_with_troop", ":current_town_town_lord", -3),
			(try_end),
			(call_script, "script_calculate_battle_advantage"),
			(set_battle_advantage, reg0),
			(set_party_battle_mode),
			(assign, "$g_battle_result", 0),
			(assign, "$g_village_raid_evil", 1),
			(set_jump_mission, "mt_village_raid"),
			(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(jump_to_scene, ":current_town_town_center"),
			(assign, "$g_next_menu", "mnu_village_start_attack"),
			(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
			(call_script, "script_objectionable_action", 3, "str_loot_village"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("village_raid_leave",
		[],
		"Leave this village alone.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("village_loot_no_resist", 0, "The villagers here are few and frightened, and they quickly scatter and run before you. The village is at your mercy.",
"none",
	[],
	[
		("village_loot",
		[],
		"Plunder the village, then raze it.",
		[
			(call_script, "script_village_set_state", "$current_town", 1),
			(party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
			(assign, "$g_player_raiding_village", "$current_town"),
			(try_begin),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(store_relation, ":relation_players_kingdom_faction_of_party_current_town", "$players_kingdom", ":faction_of_party_current_town"),
				(ge, ":relation_players_kingdom_faction_of_party_current_town", 0),
				(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
			(try_end),
			(rest_for_hours, 3, 3, 1),
			(change_screen_return)
		], "."),

		("village_raid_leave",
		[],
		"Leave this village alone.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("village_loot_complete", 0, "On your orders your troops sack the village, pillaging everything of any value, and then put the buildings to the torch. From the coins and valuables that are found, you get your share of {reg1} florins.",
"none",
	[
		(get_achievement_stat, ":achievement_stat_30_0", 30, 0),
		(get_achievement_stat, ":achievement_stat_30_1", 30, 1),
		(val_add, ":achievement_stat_30_0", 1),
		(set_achievement_stat, 30, 0, ":achievement_stat_30_0"),
		(try_begin),
			(ge, ":achievement_stat_30_0", 3),
			(ge, ":achievement_stat_30_1", 3),
			(unlock_achievement, 30),
		(try_end),
		(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
		(try_begin),
			(gt, ":current_town_town_lord", 0),
			(call_script, "script_change_player_relation_with_troop", ":current_town_town_lord", -5),
		(try_end),
		(store_random_in_range, ":random_in_range_-35_-25", -35, -25),
		(call_script, "script_change_player_relation_with_center", "$current_town", ":random_in_range_-35_-25"),
		(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
		(store_relation, ":relation_faction_of_party_current_town_player_supporters_faction", ":faction_of_party_current_town", "fac_player_supporters_faction"),
		(try_begin),
			(lt, ":relation_faction_of_party_current_town_player_supporters_faction", 0),
			(call_script, "script_change_player_relation_with_faction", ":faction_of_party_current_town", -3),
		(try_end),
		(assign, ":var_7", 50),
		(party_get_slot, ":current_town_town_prosperity", "$current_town", slot_town_prosperity),
		(store_mul, ":value", ":current_town_town_prosperity", 5),
		(val_add, ":var_7", ":value"),
		(call_script, "script_troop_add_gold", "trp_player", ":var_7"),
		(assign, ":var_10", 3),
		(store_div, ":value_2", ":var_7", 100),
		(val_add, ":var_10", ":value_2"),
		(call_script, "script_change_player_party_morale", ":var_10"),
		(faction_get_slot, ":faction_of_party_current_town_morale_of_player_troops", ":faction_of_party_current_town", slot_faction_morale_of_player_troops),
		(store_mul, ":value_3", ":var_10", 200),
		(val_sub, ":faction_of_party_current_town_morale_of_player_troops", ":value_3"),
		(call_script, "script_objectionable_action", 3, "str_loot_village"),
		(assign, reg1, ":var_7")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_close"),
			(call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
			(assign, ":var_1", reg0),
			(val_mul, ":var_1", 3),
			(val_div, ":var_1", 2),
			(party_get_slot, ":current_town_village_number_of_cattle", "$current_town", slot_village_number_of_cattle),
			(val_min, ":var_1", ":current_town_village_number_of_cattle"),
			(val_add, ":var_1", 1),
			(store_random_in_range, ":random_in_range_0_var_1", 0, ":var_1"),
			(try_begin),
				(gt, ":random_in_range_0_var_1", 0),
				(call_script, "script_create_cattle_herd", "$current_town", ":random_in_range_0_var_1"),
				(val_sub, ":current_town_village_number_of_cattle", ":random_in_range_0_var_1"),
				(party_set_slot, "$current_town", slot_village_number_of_cattle, ":current_town_village_number_of_cattle"),
			(try_end),
			(troop_clear_inventory, "trp_temp_troop"),
			(reset_item_probabilities, 100),
			(troop_add_merchandise, "trp_temp_troop", 11, 45),
			(troop_sort_inventory, "trp_temp_troop"),
			(change_screen_loot, "trp_temp_troop")
		], ".")
	]
	),

	("village_loot_defeat", 0, "Fighting with courage and determination, the villagers manage to hold together and drive off your forces.",
"none",
	[
		(set_background_mesh, "mesh_pic_villageriot")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("village_loot_continue", 0, "Do you wish to continue looting this village?",
"none",
	[],
	[
		("disembark_yes",
		[],
		"Yes.",
		[
			(rest_for_hours, 3, 5, 1),
			(change_screen_return)
		], "."),

		("disembark_no",
		[],
		"No.",
		[
			(call_script, "script_village_set_state", "$current_town", 0),
			(party_set_slot, "$current_town", slot_village_raided_by, -1),
			(assign, "$g_player_raiding_village", 0),
			(change_screen_return)
		], ".")
	]
	),

	("close", 0, "Nothing.",
"none",
	[
		(change_screen_return)
	],
	[]
	),

	("town", 0, "{s10} {s14}^{s11}{s12}{s13}",
"none",
	[
		(try_begin),
			(eq, "$sneaked_into_town", 1),
			(call_script, "script_music_set_situation_with_culture", 16384),
		(else_try),
			(call_script, "script_music_set_situation_with_culture", 65536),
		(try_end),
		(store_encountered_party, "$current_town"),
		(try_begin),
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(ge, ":current_town_town_lord", 0),
			(set_fixed_point_multiplier, 100),
			(position_set_x, 0, 70),
			(position_set_y, 0, 5),
			(position_set_z, 0, 75),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":current_town_town_lord", 0),
		(try_end),
		(call_script, "script_update_center_recon_notes", "$current_town"),
		(assign, "$g_defending_against_siege", 0),
		(str_clear, 3),
		(party_get_battle_opponent, ":battle_opponent_l_current_town", "$current_town"),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
		(try_begin),
			(gt, ":battle_opponent_l_current_town", 0),
			(ge, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0),
			(store_faction_of_party, ":faction_of_party_battle_opponent_l_current_town", ":battle_opponent_l_current_town"),
			(store_relation, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", ":faction_of_party_battle_opponent_l_current_town", "fac_player_supporters_faction"),
			(this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(lt, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", 0),
			(assign, "$g_defending_against_siege", 1),
			(assign, "$g_siege_first_encounter", 1),
			(jump_to_menu, "mnu_siege_started_defender"),
		(try_end),
		(try_begin),
			(is_between, "$g_encountered_party", "p_town_1_1", "p_castle_1_1"),
			(store_sub, ":value", "$g_encountered_party", "p_town_1_1"),
			(set_achievement_stat, 26, ":value", 1),
			(assign, ":value_2", 0),
			(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
				(store_sub, ":value", ":party", "p_town_1_1"),
				(get_achievement_stat, ":achievement_stat_26_value", 26, ":value"),
				(eq, ":achievement_stat_26_value", 0),
				(assign, ":value_2", 1),
			(try_end),
			(try_begin),
				(eq, ":value_2", 0),
				(unlock_achievement, 26),
			(try_end),
		(try_end),
		(assign, "$qst_collect_taxes_currently_collecting", 0),
		(try_begin),
			(gt, "$quest_auto_menu", 0),
			(jump_to_menu, "$quest_auto_menu"),
			(assign, "$quest_auto_menu", 0),
		(try_end),
		(try_begin),
			(eq, "$g_town_assess_trade_goods_after_rest", 1),
			(assign, "$g_town_assess_trade_goods_after_rest", 0),
			(jump_to_menu, "mnu_town_trade_assessment"),
		(try_end),
		(assign, "$talk_context", 0),
		(assign, "$all_doors_locked", 0),
		(try_begin),
			(eq, "$g_town_visit_after_rest", 1),
			(assign, "$g_town_visit_after_rest", 0),
			(assign, "$town_entered", 1),
		(try_end),
		(try_begin),
			(eq, "$g_leave_town", 1),
			(assign, "$g_leave_town", 0),
			(assign, "$g_permitted_to_center", 0),
			(leave_encounter),
			(change_screen_return),
		(try_end),
		(str_store_party_name, 2, "$current_town"),
		(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
		(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
		(str_store_faction_name, 9, ":faction_of_party_current_town"),
		(try_begin),
			(ge, ":current_town_town_lord", 0),
			(str_store_troop_name, 8, ":current_town_town_lord"),
			(str_store_string, 7, "@{s8} of {s9}"),
		(try_end),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(str_store_string, 60, 2),
			(party_get_slot, ":current_town_town_prosperity", "$current_town", slot_town_prosperity),
			(try_begin),
				(ge, "$cheat_mode", 1),
				(assign, reg4, ":current_town_town_prosperity"),
				(display_message, "@{!}DEBUG -- Prosperity: {reg4}"),
			(try_end),
			(store_div, ":value_3", ":current_town_town_prosperity", 10),
			(val_min, ":value_3", 9),
			(val_add, ":value_3", "str_town_prosperity_0"),
			(str_store_string, 10, ":value_3"),
			(store_div, ":value_3", ":current_town_town_prosperity", 20),
			(val_min, ":value_3", 4),
			(val_add, ":value_3", "str_town_alt_prosperity_0"),
			(str_store_string, 14, ":value_3"),
		(else_try),
			(str_clear, 14),
			(str_store_string, 10, "@You are at {s2}."),
		(try_end),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, 2),
			(try_begin),
				(eq, ":current_town_town_lord", "trp_player"),
				(str_store_string, 11, "@ Your own banner flies over the castle gate."),
			(else_try),
				(gt, ":current_town_town_lord", -1),
				(troop_slot_eq, ":current_town_town_lord", slot_troop_spouse, "trp_player"),
				(str_store_string, 11, "str__you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate"),
			(else_try),
				(ge, ":current_town_town_lord", 0),
				(str_store_string, 11, "@ You see the banner of {s7} over the castle gate."),
			(else_try),
				(str_store_string, 11, "@ This castle has no garrison."),
			(try_end),
		(else_try),
			(try_begin),
				(eq, ":current_town_town_lord", "trp_player"),
				(str_store_string, 11, "@ Your own banner flies over the town gates."),
			(else_try),
				(gt, ":current_town_town_lord", -1),
				(troop_slot_eq, ":current_town_town_lord", slot_troop_spouse, "trp_player"),
				(str_store_string, 11, "str__the_banner_of_your_wifehusband_s7_flies_over_the_town_gates"),
			(else_try),
				(ge, ":current_town_town_lord", 0),
				(str_store_string, 11, "@ You see the banner of {s7} over the town gates."),
			(else_try),
				(str_store_string, 11, "@ This town has no garrison."),
			(try_end),
		(try_end),
		(str_clear, 12),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(party_get_slot, ":current_town_center_player_relation", "$current_town", slot_center_player_relation),
			(call_script, "script_describe_center_relation_to_s3", ":current_town_center_player_relation"),
			(assign, reg9, ":current_town_center_player_relation"),
			(str_store_string, 12, "@{!} {s3} ({reg9})."),
		(try_end),
		(str_clear, 13),
		(try_begin),
			(gt, "$entry_to_town_forbidden", 0),
			(str_store_string, 13, "@ You have successfully sneaked in."),
		(else_try),
			(faction_slot_eq, ":faction_of_party_current_town", slot_faction_ai_state, 6),
			(faction_slot_eq, ":faction_of_party_current_town", slot_faction_ai_object, "$current_town"),
			(str_store_string, 13, "str__the_lord_is_currently_holding_a_feast_in_his_hall"),
		(try_end),
		(try_begin),
			(store_time_of_day, reg12),
			(ge, reg12, 5),
			(lt, reg12, 21),
			(assign, "$town_nighttime", 0),
		(else_try),
			(assign, "$town_nighttime", 1),
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(str_store_string, 13, "str_town_nighttime"),
		(try_end),
		(try_begin),
			(party_slot_ge, "$current_town", 156, 1),
			(neg|is_currently_night),
			(party_set_slot, "$current_town", slot_town_has_tournament, 1),
			(str_store_string, 13, "@{s13} A tournament will be held here soon."),
		(try_end),
		(assign, "$castle_undefended", 0),
		(party_get_num_companions, ":num_companions_collective_enemy", "p_collective_enemy"),
		(try_begin),
			(eq, ":num_companions_collective_enemy", 0),
			(assign, "$castle_undefended", 1),
		(try_end),
		(call_script, "script_set_town_picture")
	],
	[
		("castle_castle",
		[
			(party_slot_eq, "$current_town", slot_party_type, 2),
			(eq, "$sneaked_into_town", 0),
			(str_clear, 1),
			(try_begin),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(faction_slot_eq, ":faction_of_party_current_town", slot_faction_ai_state, 6),
				(faction_slot_eq, ":faction_of_party_current_town", slot_faction_ai_object, "$current_town"),
				(str_store_string, 1, "str__join_the_feast"),
			(try_end)
		],
		"Go to the Lord's hall{s1}.",
		[
			(try_begin),
				(this_or_next|eq, "$all_doors_locked", 1),
				(eq, "$sneaked_into_town", 1),
				(display_message, "str_door_locked", 0xffffaaaa),
			(else_try),
				(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
				(neg|troop_slot_ge, "trp_player", 7, 50),
				(neg|troop_slot_ge, "trp_player", 7, 125),
				(neq, "$g_player_eligible_feast_center_no", "$current_town"),
				(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, 6),
				(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
				(neg|check_quest_active, "qst_wed_betrothed"),
				(neg|check_quest_active, "qst_wed_betrothed_female"),
				(neg|troop_slot_ge, "trp_player", 30, "trp_npc1"),
				(jump_to_menu, "mnu_cannot_enter_court"),
			(else_try),
				(assign, "$town_entered", 1),
				(call_script, "script_enter_court", "$current_town"),
			(try_end)
		], "Door_to_the_castle."),

		("join_tournament",
		[
			(neg|is_currently_night),
			(party_slot_ge, "$current_town", 156, 1),
			(eq, "$freelancer_state", 0)
		],
		"Join the tournament.",
		[
			(assign, "$g_tournament_cur_tier", 0),
			(assign, "$g_tournament_player_team_won", -1),
			(assign, "$g_tournament_bet_placed", 0),
			(assign, "$g_tournament_bet_win_amount", 0),
			(assign, "$g_tournament_last_bet_tier", -1),
			(assign, "$g_tournament_next_num_teams", 0),
			(assign, "$g_tournament_next_team_size", 0),
			(jump_to_menu, "mnu_town_tournament_start_new")
		], "."),

		("town_castle",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(eq, "$entry_to_town_forbidden", 0),
			(str_clear, 1),
			(try_begin),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(faction_slot_eq, ":faction_of_party_current_town", slot_faction_ai_state, 6),
				(faction_slot_eq, ":faction_of_party_current_town", slot_faction_ai_object, "$current_town"),
				(str_store_string, 1, "str__join_the_feast"),
			(try_end)
		],
		"Go to the castle{s1}.",
		[
			(try_begin),
				(this_or_next|eq, "$all_doors_locked", 1),
				(eq, "$sneaked_into_town", 1),
				(display_message, "str_door_locked", 0xffffaaaa),
			(else_try),
				(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
				(neg|troop_slot_ge, "trp_player", 7, 50),
				(neg|troop_slot_ge, "trp_player", 7, 125),
				(neq, "$g_player_eligible_feast_center_no", "$current_town"),
				(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, 6),
				(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
				(neg|check_quest_active, "qst_wed_betrothed"),
				(neg|check_quest_active, "qst_wed_betrothed_female"),
				(neg|troop_slot_ge, "trp_player", 30, "trp_npc1"),
				(jump_to_menu, "mnu_cannot_enter_court"),
			(else_try),
				(assign, "$town_entered", 1),
				(call_script, "script_enter_court", "$current_town"),
			(try_end)
		], "Door_to_the_castle."),

		("town_center",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(this_or_next|eq, "$entry_to_town_forbidden", 0),
			(eq, "$sneaked_into_town", 1)
		],
		"Take a walk around the streets.",
		[
			(try_begin),
				(eq, "$talk_context", 18),
				(assign, "$talk_context", 19),
				(assign, "$g_mt_mode", 3),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_1_archer", ":faction_of_party_current_town", slot_faction_quick_battle_tier_1_archer),
				(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", ":faction_of_party_current_town", slot_faction_quick_battle_tier_1_archer),
				(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_2_archer", ":faction_of_party_current_town", slot_faction_quick_battle_tier_2_archer),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
				(modify_visitors_at_site, ":current_town_town_center"),
				(reset_visitors),
				(try_begin),
					(party_get_slot, ":current_town_town_last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
					(store_current_hours, ":current_hours"),
					(store_add, ":value", ":current_town_town_last_nearby_fire_time", 4),
					(neg|is_between, ":current_hours", ":current_town_town_last_nearby_fire_time", ":value"),
					(store_time_of_day, ":time_of_day"),
					(try_begin),
						(ge, ":time_of_day", 6),
						(lt, ":time_of_day", 22),
						(set_visitors, 25, ":faction_of_party_current_town_quick_battle_tier_1_archer", 2),
						(set_visitors, 26, ":faction_of_party_current_town_quick_battle_tier_1_archer", 1),
						(set_visitors, 27, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", 2),
						(set_visitors, 28, ":faction_of_party_current_town_quick_battle_tier_2_archer", 1),
					(else_try),
						(set_visitors, 25, ":faction_of_party_current_town_quick_battle_tier_1_archer", 1),
						(set_visitors, 26, ":faction_of_party_current_town_quick_battle_tier_1_archer", 1),
						(set_visitors, 27, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", 1),
						(set_visitors, 28, ":faction_of_party_current_town_quick_battle_tier_2_archer", 1),
					(try_end),
				(else_try),
					(store_time_of_day, ":time_of_day"),
					(try_begin),
						(ge, ":time_of_day", 6),
						(lt, ":time_of_day", 22),
						(set_visitors, 25, ":faction_of_party_current_town_quick_battle_tier_1_archer", 1),
						(set_visitors, 26, ":faction_of_party_current_town_quick_battle_tier_1_archer", 0),
						(set_visitors, 27, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", 1),
						(set_visitors, 28, ":faction_of_party_current_town_quick_battle_tier_2_archer", 0),
					(else_try),
						(set_visitors, 25, ":faction_of_party_current_town_quick_battle_tier_1_archer", 1),
						(set_visitors, 26, ":faction_of_party_current_town_quick_battle_tier_1_archer", 0),
						(set_visitors, 27, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", 0),
						(set_visitors, 28, ":faction_of_party_current_town_quick_battle_tier_2_archer", 0),
					(try_end),
				(try_end),
				(set_jump_mission, "mt_town_center"),
				(jump_to_scene, ":current_town_town_center"),
				(change_screen_mission),
			(else_try),
				(assign, "$talk_context", 0),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
				(modify_visitors_at_site, ":current_town_town_center"),
				(reset_visitors),
				(assign, "$g_mt_mode", 0),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(try_begin),
					(neq, ":faction_of_party_current_town", "fac_player_supporters_faction"),
					(faction_get_slot, ":g_encountered_party_faction_prison_guard_troop", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
					(faction_get_slot, ":g_encountered_party_faction_castle_guard_troop", "$g_encountered_party_faction", slot_faction_castle_guard_troop),
					(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_1_archer", ":faction_of_party_current_town", slot_faction_quick_battle_tier_2_infantry),
					(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", ":faction_of_party_current_town", slot_faction_quick_battle_tier_1_archer),
				(else_try),
					(party_get_slot, ":current_town_center_original_faction", "$current_town", slot_center_original_faction),
					(faction_get_slot, ":g_encountered_party_faction_prison_guard_troop", ":current_town_center_original_faction", slot_faction_prison_guard_troop),
					(faction_get_slot, ":g_encountered_party_faction_castle_guard_troop", ":current_town_center_original_faction", slot_faction_castle_guard_troop),
					(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_1_archer", ":current_town_center_original_faction", slot_faction_quick_battle_tier_2_infantry),
					(faction_get_slot, ":faction_of_party_current_town_quick_battle_tier_1_archer_2", ":current_town_center_original_faction", slot_faction_quick_battle_tier_1_archer),
				(try_end),
				(try_begin),
					(party_get_slot, ":current_town_town_last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
					(store_current_hours, ":current_hours"),
					(store_add, ":value", ":current_town_town_last_nearby_fire_time", 4),
					(neg|is_between, ":current_hours", ":current_town_town_last_nearby_fire_time", ":value"),
					(set_visitor, 23, ":g_encountered_party_faction_castle_guard_troop"),
				(try_end),
				(set_visitor, 24, ":g_encountered_party_faction_prison_guard_troop"),
				(try_begin),
					(gt, ":faction_of_party_current_town_quick_battle_tier_1_archer", 0),
					(assign, reg0, ":faction_of_party_current_town_quick_battle_tier_1_archer_2"),
					(assign, reg1, ":faction_of_party_current_town_quick_battle_tier_1_archer_2"),
					(assign, reg2, ":faction_of_party_current_town_quick_battle_tier_1_archer"),
					(assign, reg3, ":faction_of_party_current_town_quick_battle_tier_1_archer"),
				(else_try),
					(assign, reg0, "trp_euro_spearman_3"),
					(assign, reg1, "trp_euro_spearman_3"),
					(assign, reg2, "trp_euro_archer_2"),
					(assign, reg3, "trp_euro_spearman_2"),
				(try_end),
				(shuffle_range, 0, 4),
				(try_begin),
					(party_get_slot, ":current_town_town_last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
					(store_current_hours, ":current_hours"),
					(store_add, ":value", ":current_town_town_last_nearby_fire_time", 4),
					(neg|is_between, ":current_hours", ":current_town_town_last_nearby_fire_time", ":value"),
					(set_visitor, 25, reg0),
					(set_visitor, 26, reg1),
					(set_visitor, 27, reg2),
					(set_visitor, 28, reg3),
				(try_end),
				(party_get_slot, ":current_town_town_armorer", "$current_town", slot_town_armorer),
				(set_visitor, 9, ":current_town_town_armorer"),
				(party_get_slot, ":current_town_town_armorer", "$current_town", slot_town_weaponsmith),
				(set_visitor, 10, ":current_town_town_armorer"),
				(party_get_slot, ":current_town_town_armorer", "$current_town", slot_town_elder),
				(set_visitor, 11, ":current_town_town_armorer"),
				(party_get_slot, ":current_town_town_armorer", "$current_town", slot_town_horse_merchant),
				(set_visitor, 12, ":current_town_town_armorer"),
				(call_script, "script_init_town_walkers"),
				(set_jump_mission, "mt_town_center"),
				(assign, ":value_2", 256),
				(try_begin),
					(eq, "$sneaked_into_town", 1),
					(assign, ":value_2", 447),
				(try_end),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":value_2"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":value_2"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":value_2"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":value_2"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":value_2"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":value_2"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":value_2"),
				(try_begin),
					(eq, "$town_entered", 0),
					(assign, "$town_entered", 1),
					(eq, "$town_nighttime", 0),
					(set_jump_entry, 1),
				(try_end),
				(jump_to_scene, ":current_town_town_center"),
				(change_screen_mission),
			(try_end)
		], "Door_to_the_town_center."),

		("town_tavern",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(this_or_next|eq, "$entry_to_town_forbidden", 0),
			(eq, "$sneaked_into_town", 1)
		],
		"Visit the tavern.",
		[
			(try_begin),
				(eq, "$all_doors_locked", 1),
				(display_message, "str_door_locked", 0xffffaaaa),
			(else_try),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(assign, "$town_entered", 1),
				(set_jump_mission, "mt_town_default"),
				(mission_tpl_entry_set_override_flags, "mt_town_default", 0, 256),
				(try_begin),
					(eq, "$sneaked_into_town", 1),
					(mission_tpl_entry_set_override_flags, "mt_town_default", 0, 447),
				(try_end),
				(party_get_slot, ":current_town_town_tavern", "$current_town", slot_town_tavern),
				(jump_to_scene, ":current_town_town_tavern"),
				(scene_set_slot, ":current_town_town_tavern", slot_scene_visited, 1),
				(assign, "$talk_context", 14),
				(call_script, "script_initialize_tavern_variables"),
				(store_random_in_range, ":random_in_range_0_4", 0, 4),
				(modify_visitors_at_site, ":current_town_town_tavern"),
				(reset_visitors),
				(party_get_slot, ":current_town_town_tavernkeeper", "$current_town", slot_town_tavernkeeper),
				(set_visitor, 9, ":current_town_town_tavernkeeper"),
				(assign, ":var_4", 17),
				(try_begin),
					(set_visitor, ":var_4", "trp_whore"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(troop_get_slot, ":belligerent_drunk_cur_center", "trp_belligerent_drunk", slot_troop_cur_center),
					(try_begin),
						(eq, "$cheat_mode", 0),
					(else_try),
						(is_between, ":belligerent_drunk_cur_center", "p_town_1_1", "p_salt_mine"),
						(str_store_party_name, 4, ":belligerent_drunk_cur_center"),
						(display_message, "str_belligerent_drunk_in_s4"),
					(else_try),
						(display_message, "str_belligerent_drunk_not_found"),
					(try_end),
					(troop_get_slot, ":fight_promoter_cur_center", "trp_fight_promoter", slot_troop_cur_center),
					(try_begin),
						(eq, "$cheat_mode", 0),
					(else_try),
						(is_between, ":fight_promoter_cur_center", "p_town_1_1", "p_salt_mine"),
						(str_store_party_name, 4, ":fight_promoter_cur_center"),
						(display_message, "str_roughlooking_character_in_s4"),
					(else_try),
						(display_message, "str_roughlooking_character_not_found"),
					(try_end),
				(try_end),
				(try_begin),
					(store_current_hours, ":current_hours"),
					(store_sub, ":value", ":current_hours", "$g_last_assassination_attempt_time"),
					(gt, ":value", 168),
					(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
						(troop_slot_eq, ":troop", slot_lord_reputation_type, 5),
						(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
						(party_is_active, ":troop_leaded_party"),
						(party_get_attached_to, ":attached_to_troop_leaded_party", ":troop_leaded_party"),
						(eq, ":attached_to_troop_leaded_party", "$g_encountered_party"),
						(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop"),
						(lt, reg0, -20),
						(assign, "$g_last_assassination_attempt_time", ":current_hours"),
						(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":random_in_range_0_4", 0),
					(call_script, "script_setup_tavern_attacker", ":var_4"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(eq, 1, 0),
					(troop_slot_eq, "trp_fight_promoter", slot_troop_cur_center, "$current_town"),
					(set_visitor, ":var_4", "trp_fight_promoter"),
					(val_add, ":var_4", 1),
				(try_end),
				(call_script, "script_get_available_mercenary_troop_and_amount_of_center", "$current_town"),
				(assign, ":var_12", reg0),
				(assign, ":var_13", reg1),
				(str_store_troop_name, 10, ":var_12"),
				(assign, reg25, ":var_13"),
				(try_begin),
					(gt, ":var_12", 0),
					(gt, ":var_13", 0),
					(set_visitor, ":var_4", ":var_12"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(eq, ":random_in_range_0_4", 1),
					(call_script, "script_setup_tavern_attacker", ":var_4"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_for_range, ":number", 3156, 3177),
					(troop_slot_eq, ":number", slot_troop_cur_center, "$current_town"),
					(set_visitor, ":var_4", ":number"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(eq, ":random_in_range_0_4", 2),
					(call_script, "script_setup_tavern_attacker", ":var_4"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(party_get_slot, ":current_town_center_ransom_broker", "$current_town", slot_center_ransom_broker),
					(gt, ":current_town_center_ransom_broker", 0),
					(assign, reg20, ":var_4"),
					(display_message, "@ransom broker present entry point: {reg20}."),
					(assign, reg0, ":current_town_center_ransom_broker"),
					(assign, reg1, "$current_town"),
					(set_visitor, ":var_4", ":current_town_center_ransom_broker"),
					(val_add, ":var_4", 1),
				(else_try),
					(is_between, "$g_talk_troop", "trp_ransom_broker_1", "trp_tavern_traveler_1"),
					(store_add, ":value_2", "$current_town", 9),
					(try_begin),
						(ge, ":value_2", "p_castle_1_1"),
						(val_sub, ":value_2", 22),
					(try_end),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_party_name, 3, "$current_town"),
						(str_store_party_name, 4, ":value_2"),
						(display_message, "@{!}DEBUG - Current town is {s3}, but also checking {s4}"),
					(try_end),
					(party_get_slot, ":current_town_center_ransom_broker", ":value_2", slot_center_ransom_broker),
					(gt, ":current_town_center_ransom_broker", 0),
					(set_visitor, ":var_4", ":current_town_center_ransom_broker"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(party_get_slot, ":current_town_center_tavern_traveler", "$current_town", slot_center_tavern_traveler),
					(gt, ":current_town_center_tavern_traveler", 0),
					(set_visitor, ":var_4", ":current_town_center_tavern_traveler"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(party_get_slot, ":current_town_center_tavern_minstrel", "$current_town", slot_center_tavern_minstrel),
					(gt, ":current_town_center_tavern_minstrel", 0),
					(set_visitor, ":var_4", ":current_town_center_tavern_minstrel"),
					(val_add, ":var_4", 1),
				(else_try),
					(store_add, ":value_2", "$current_town", 9),
					(try_begin),
						(ge, ":value_2", "p_castle_1_1"),
						(val_sub, ":value_2", 22),
					(try_end),
					(party_get_slot, ":current_town_center_tavern_minstrel", ":value_2", slot_center_tavern_minstrel),
					(gt, ":current_town_center_tavern_minstrel", 0),
					(set_visitor, ":var_4", ":current_town_center_tavern_minstrel"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(party_get_slot, ":current_town_center_tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
					(gt, ":current_town_center_tavern_bookseller", 0),
					(set_visitor, ":var_4", ":current_town_center_tavern_bookseller"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(eq, ":random_in_range_0_4", 3),
					(call_script, "script_setup_tavern_attacker", ":var_4"),
					(val_add, ":var_4", 1),
				(try_end),
				(try_begin),
					(neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
					(neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
					(assign, ":value_3", "p_salt_mine"),
					(try_for_range, ":party", "p_village_1_1", ":value_3"),
						(party_slot_eq, ":party", slot_village_bound_center, "$current_town"),
						(party_slot_ge, ":party", 39, 1),
						(neg|party_slot_eq, ":party", slot_town_lord, "trp_player"),
						(set_visitor, ":var_4", "trp_farmer_from_bandit_village"),
						(val_add, ":var_4", 1),
						(assign, ":value_3", 0),
					(try_end),
				(try_end),
				(try_begin),
					(eq, "$g_starting_town", "$current_town"),
					(this_or_next|neg|check_quest_finished, "qst_collect_men"),
					(this_or_next|neg|check_quest_finished, "qst_learn_where_merchant_brother_is"),
					(this_or_next|neg|check_quest_finished, "qst_save_relative_of_merchant"),
					(this_or_next|neg|check_quest_finished, "qst_save_town_from_bandits"),
					(eq, "$g_do_one_more_meeting_with_merchant", 1),
					(assign, ":value_4", 0),
					(try_begin),
						(eq, "$g_encountered_party_faction", "fac_kingdom_1"),
						(assign, ":value_4", "trp_merchant_kingdom_1"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_2"),
						(assign, ":value_4", "trp_merchant_kingdom_2"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_3"),
						(assign, ":value_4", "trp_merchant_kingdom_3"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_4"),
						(assign, ":value_4", "trp_merchant_kingdom_4"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_5"),
						(assign, ":value_4", "trp_merchant_kingdom_5"),
					(else_try),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_42"),
						(eq, "$g_encountered_party_faction", "fac_kingdom_6"),
						(assign, ":value_4", "trp_merchant_kingdom_6"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_7"),
						(assign, ":value_4", "trp_merchant_kingdom_7"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_8"),
						(assign, ":value_4", "trp_merchant_kingdom_8"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_9"),
						(assign, ":value_4", "trp_merchant_kingdom_9"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_10"),
						(assign, ":value_4", "trp_merchant_kingdom_10"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_11"),
						(assign, ":value_4", "trp_merchant_kingdom_11"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_12"),
						(assign, ":value_4", "trp_merchant_kingdom_12"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_13"),
						(assign, ":value_4", "trp_merchant_kingdom_13"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_14"),
						(assign, ":value_4", "trp_merchant_kingdom_14"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_15"),
						(assign, ":value_4", "trp_merchant_kingdom_15"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_16"),
						(assign, ":value_4", "trp_merchant_kingdom_16"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_17"),
						(assign, ":value_4", "trp_merchant_kingdom_17"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_18"),
						(assign, ":value_4", "trp_merchant_kingdom_18"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_19"),
						(assign, ":value_4", "trp_merchant_kingdom_19"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_20"),
						(assign, ":value_4", "trp_merchant_kingdom_20"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_papacy"),
						(assign, ":value_4", "trp_merchant_kingdom_21"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_22"),
						(assign, ":value_4", "trp_merchant_kingdom_22"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_23"),
						(assign, ":value_4", "trp_merchant_kingdom_23"),
					(else_try),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_24"),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_38"),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_39"),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_40"),
						(eq, "$g_encountered_party_faction", "fac_kingdom_41"),
						(assign, ":value_4", "trp_merchant_kingdom_24"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_25"),
						(assign, ":value_4", "trp_merchant_kingdom_25"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_25"),
						(assign, ":value_4", "trp_merchant_kingdom_25"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_26"),
						(assign, ":value_4", "trp_merchant_kingdom_26"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_27"),
						(assign, ":value_4", "trp_merchant_kingdom_27"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_28"),
						(assign, ":value_4", "trp_merchant_kingdom_28"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_29"),
						(assign, ":value_4", "trp_merchant_kingdom_29"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_30"),
						(assign, ":value_4", "trp_merchant_kingdom_30"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_31"),
						(assign, ":value_4", "trp_merchant_kingdom_31"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_32"),
						(assign, ":value_4", "trp_merchant_kingdom_32"),
					(else_try),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_34"),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_35"),
						(this_or_next|eq, "$g_encountered_party_faction", "fac_kingdom_36"),
						(eq, "$g_encountered_party_faction", "fac_kingdom_33"),
						(assign, ":value_4", "trp_merchant_kingdom_2"),
					(else_try),
						(eq, "$g_encountered_party_faction", "fac_kingdom_37"),
						(assign, ":value_4", "trp_merchant_kingdom_37"),
					(try_end),
					(gt, ":value_4", 0),
					(set_visitor, ":var_4", ":value_4"),
					(val_add, ":var_4", 1),
				(try_end),
				(change_screen_mission),
			(try_end)
		], "Door_to_the_tavern."),

		("town_merchant",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(eq, 1, 0),
			(eq, "$town_nighttime", 0),
			(this_or_next|eq, "$entry_to_town_forbidden", 0),
			(eq, "$sneaked_into_town", 1)
		],
		"Speak with the merchant.",
		[
			(try_begin),
				(this_or_next|eq, "$all_doors_locked", 1),
				(eq, "$town_nighttime", 1),
				(display_message, "str_door_locked", 0xffffaaaa),
			(else_try),
				(assign, "$town_entered", 1),
				(set_jump_mission, "mt_town_default"),
				(mission_tpl_entry_set_override_flags, "mt_town_default", 0, 256),
				(try_begin),
					(eq, "$sneaked_into_town", 1),
					(mission_tpl_entry_set_override_flags, "mt_town_default", 0, 447),
				(try_end),
				(party_get_slot, ":current_town_town_store", "$current_town", slot_town_store),
				(modify_visitors_at_site, ":current_town_town_store"),
				(reset_visitors),
				(party_get_slot, ":current_town_town_merchant", "$current_town", slot_town_merchant),
				(set_visitor, 9, ":current_town_town_merchant"),
				(jump_to_scene, ":current_town_town_store"),
				(scene_set_slot, ":current_town_town_store", slot_scene_visited, 1),
				(change_screen_mission),
			(try_end)
		], "Door_to_the_shop."),

		("town_arena",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(eq, "$sneaked_into_town", 0)
		],
		"Enter the arena.",
		[
			(try_begin),
				(this_or_next|eq, "$all_doors_locked", 1),
				(eq, "$town_nighttime", 1),
				(display_message, "str_door_locked", 0xffffaaaa),
			(else_try),
				(assign, "$g_mt_mode", 2),
				(assign, "$town_entered", 1),
				(set_jump_mission, "mt_arena_melee_fight"),
				(party_get_slot, ":current_town_town_arena", "$current_town", slot_town_arena),
				(modify_visitors_at_site, ":current_town_town_arena"),
				(reset_visitors),
				(party_get_slot, ":current_town_600", "$current_town", 600),
				(set_visitor, 52, ":current_town_600"),
				(set_visitor, 43, "trp_veteran_fighter"),
				(set_visitor, 44, "trp_regular_fighter"),
				(set_jump_entry, 50),
				(jump_to_scene, ":current_town_town_arena"),
				(scene_set_slot, ":current_town_town_arena", slot_scene_visited, 1),
				(change_screen_mission),
			(try_end)
		], "Door_to_the_arena."),

		("town_dungeon",
		[
			(eq, 1, 0)
		],
		"Never: Enter the prison.",
		[
			(try_begin),
				(eq, "$talk_context", 18),
				(gt, "$g_main_attacker_agent", 0),
				(neg|agent_is_alive, "$g_main_attacker_agent"),
				(agent_get_troop_id, ":troop_id_l_g_main_attacker_agent", "$g_main_attacker_agent"),
				(try_begin),
					(eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
					(party_get_slot, ":current_town_center_original_faction", "$current_town", slot_center_original_faction),
				(else_try),
					(assign, ":current_town_center_original_faction", "$g_encountered_party_faction"),
				(try_end),
				(faction_slot_eq, ":current_town_center_original_faction", slot_faction_prison_guard_troop, ":troop_id_l_g_main_attacker_agent"),
				(call_script, "script_deduct_casualties_from_garrison"),
				(call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
			(else_try),
				(eq, "$all_doors_locked", 1),
				(display_message, "str_door_locked", 0xffffaaaa),
			(else_try),
				(this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
				(eq, "$g_encountered_party_faction", "$players_kingdom"),
				(assign, "$town_entered", 1),
				(call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
			(else_try),
				(display_message, "str_door_locked", 0xffffaaaa),
			(try_end)
		], "Door_to_the_dungeon."),

		("castle_inspect",
		[
			(party_slot_eq, "$current_town", slot_party_type, 2)
		],
		"Take a walk around the courtyard.",
		[
			(try_begin),
				(eq, "$talk_context", 18),
				(assign, "$talk_context", 19),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
				(modify_visitors_at_site, ":current_town_town_center"),
				(reset_visitors),
				(assign, ":value", 40),
				(party_get_num_companion_stacks, ":num_companion_stacks_l_g_encountered_party", "$g_encountered_party"),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_l_g_encountered_party"),
					(party_get_slot, ":current_town_town_last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
					(store_current_hours, ":current_hours"),
					(store_add, ":value_2", ":current_town_town_last_nearby_fire_time", 4),
					(this_or_next|eq, ":value", 40),
					(neg|is_between, ":current_hours", ":current_town_town_last_nearby_fire_time", ":value_2"),
					(lt, ":value", 47),
					(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(neg|troop_is_hero, ":party_stack_troop_id_g_encountered_party_localvariable"),
					(party_stack_get_size, ":party_stack_size_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(party_stack_get_num_wounded, ":party_stack_num_wounded_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(val_sub, ":party_stack_size_g_encountered_party_localvariable", ":party_stack_num_wounded_g_encountered_party_localvariable"),
					(gt, ":party_stack_size_g_encountered_party_localvariable", 0),
					(party_stack_get_troop_dna, ":party_stack_troop_dna_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(set_visitor, ":value", ":party_stack_troop_id_g_encountered_party_localvariable", ":party_stack_troop_dna_g_encountered_party_localvariable"),
					(val_add, ":value", 1),
				(try_end),
				(set_visitor, 7, "$g_player_troop"),
				(set_jump_mission, "mt_castle_visit"),
				(jump_to_scene, ":current_town_town_center"),
				(change_screen_mission),
			(else_try),
				(assign, "$talk_context", 0),
				(assign, "$g_mt_mode", 0),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
				(modify_visitors_at_site, ":current_town_town_center"),
				(reset_visitors),
				(try_begin),
					(neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
					(faction_get_slot, ":g_encountered_party_faction_prison_guard_troop", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
				(else_try),
					(party_get_slot, ":current_town_center_original_faction", "$current_town", slot_center_original_faction),
					(faction_get_slot, ":g_encountered_party_faction_prison_guard_troop", ":current_town_center_original_faction", slot_faction_prison_guard_troop),
				(try_end),
				(set_visitor, 24, ":g_encountered_party_faction_prison_guard_troop"),
				(assign, ":value", 40),
				(party_get_num_companion_stacks, ":num_companion_stacks_l_g_encountered_party", "$g_encountered_party"),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_l_g_encountered_party"),
					(party_get_slot, ":current_town_town_last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
					(store_current_hours, ":current_hours"),
					(store_add, ":value_2", ":current_town_town_last_nearby_fire_time", 4),
					(neg|is_between, ":current_hours", ":value_2", ":current_town_town_last_nearby_fire_time"),
					(lt, ":value", 47),
					(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(neg|troop_is_hero, ":party_stack_troop_id_g_encountered_party_localvariable"),
					(party_stack_get_size, ":party_stack_size_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(party_stack_get_num_wounded, ":party_stack_num_wounded_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(val_sub, ":party_stack_size_g_encountered_party_localvariable", ":party_stack_num_wounded_g_encountered_party_localvariable"),
					(gt, ":party_stack_size_g_encountered_party_localvariable", 0),
					(party_stack_get_troop_dna, ":party_stack_troop_dna_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
					(set_visitor, ":value", ":party_stack_troop_id_g_encountered_party_localvariable", ":party_stack_troop_dna_g_encountered_party_localvariable"),
					(val_add, ":value", 1),
				(try_end),
				(try_begin),
					(eq, "$town_entered", 0),
					(assign, "$town_entered", 1),
				(try_end),
				(set_jump_entry, 1),
				(assign, ":value_3", 256),
				(try_begin),
					(eq, "$sneaked_into_town", 1),
					(assign, ":value_3", 447),
				(try_end),
				(set_jump_mission, "mt_castle_visit"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 0, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 1, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 2, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 3, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 4, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 5, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 6, ":value_3"),
				(mission_tpl_entry_set_override_flags, "mt_castle_visit", 7, ":value_3"),
				(jump_to_scene, ":current_town_town_center"),
				(change_screen_mission),
			(try_end)
		], "To_the_castle_courtyard."),

		("castle_player_sally_out",
		[
			(neg|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(neg|troop_is_wounded, "trp_player"),
			(party_get_slot, ":g_encountered_party_center_is_besieged_by", "$g_encountered_party", slot_center_is_besieged_by),
			(party_is_active, ":g_encountered_party_center_is_besieged_by"),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_g_encountered_party_center_is_besieged_by_g_encountered_party", ":g_encountered_party_center_is_besieged_by", "$g_encountered_party"),
			(le, ":distance_to_party_from_party_g_encountered_party_center_is_besieged_by_g_encountered_party", 7),
			(party_get_battle_opponent, ":battle_opponent_l_g_encountered_party", "$g_encountered_party"),
			(lt, ":battle_opponent_l_g_encountered_party", 0),
			(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_center_is_besieged_by_0", ":g_encountered_party_center_is_besieged_by", 0),
			(str_store_troop_name, 11, ":party_stack_troop_id_g_encountered_party_center_is_besieged_by_0"),
			(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_g_encountered_party_center_is_besieged_by_0", ":party_stack_troop_id_g_encountered_party_center_is_besieged_by_0"),
			(store_relation, ":relation_players_kingdom_faction_of_troop_party_stack_troop_id_g_encountered_party_center_is_besieged_by_0", "$players_kingdom", ":faction_of_troop_party_stack_troop_id_g_encountered_party_center_is_besieged_by_0"),
			(str_store_party_name, 12, "$current_town"),
			(lt, ":relation_players_kingdom_faction_of_troop_party_stack_troop_id_g_encountered_party_center_is_besieged_by_0", 0)
		],
		"{s12} is under siege.  Sally out to delay the attackers.",
		[
			(assign, "$auto_enter_town", 0),
			(party_get_slot, ":g_encountered_party_center_is_besieged_by", "$g_encountered_party", slot_center_is_besieged_by),
			(assign, "$g_player_sally_town", "$g_encountered_party"),
			(assign, "$g_player_sallies", ":g_encountered_party_center_is_besieged_by"),
			(display_message, "@sally"),
			(leave_encounter),
			(change_screen_return)
		], "."),

		("town_enterprise",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(party_get_slot, ":current_town_center_player_enterprise", "$current_town", slot_center_player_enterprise),
			(gt, ":current_town_center_player_enterprise", 1),
			(eq, "$entry_to_town_forbidden", 0),
			(call_script, "script_get_enterprise_name", ":current_town_center_player_enterprise"),
			(str_store_string, 3, reg0)
		],
		"Visit your {s3}.",
		[
			(store_sub, ":value", "$current_town", "p_town_1_1"),
			(store_add, ":value_2", "trp_town_1_master_craftsman", ":value"),
			(party_get_slot, ":current_town_center_player_enterprise", "$current_town", slot_center_player_enterprise),
			(assign, ":value_3", "scn_enterprise_mill"),
			(try_begin),
				(eq, ":current_town_center_player_enterprise", "itm_bread"),
				(assign, ":value_3", "scn_enterprise_mill"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_ale"),
				(assign, ":value_3", "scn_enterprise_brewery"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_oil"),
				(assign, ":value_3", "scn_enterprise_oil_press"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_wine"),
				(assign, ":value_3", "scn_enterprise_winery"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_leatherwork"),
				(assign, ":value_3", "scn_enterprise_tannery"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_wool_cloth"),
				(assign, ":value_3", "scn_enterprise_wool_weavery"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_linen"),
				(assign, ":value_3", "scn_enterprise_linen_weavery"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_velvet"),
				(assign, ":value_3", "scn_enterprise_dyeworks"),
			(else_try),
				(eq, ":current_town_center_player_enterprise", "itm_tools"),
				(assign, ":value_3", "scn_enterprise_smithy"),
			(try_end),
			(modify_visitors_at_site, ":value_3"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 17, ":value_2"),
			(set_jump_mission, "mt_town_default"),
			(jump_to_scene, ":value_3"),
			(change_screen_mission)
		], "Door_to_your_enterprise."),

		("visit_lady",
		[
			(neg|troop_slot_ge, "trp_player", 30, "trp_knight_1_1_wife"),
			(assign, "$love_interest_in_town", 0),
			(assign, "$love_interest_in_town_2", 0),
			(assign, "$love_interest_in_town_3", 0),
			(assign, "$love_interest_in_town_4", 0),
			(assign, "$love_interest_in_town_5", 0),
			(assign, "$love_interest_in_town_6", 0),
			(assign, "$love_interest_in_town_7", 0),
			(assign, "$love_interest_in_town_8", 0),
			(try_for_range, ":troop", "trp_knight_1_1_wife", "trp_heroes_end"),
				(troop_slot_eq, ":troop", slot_troop_cur_center, "$current_town"),
				(call_script, "script_get_kingdom_lady_social_determinants", ":troop"),
				(assign, ":var_2", reg0),
				(troop_slot_eq, ":troop", slot_troop_spouse, -1),
				(ge, ":var_2", 0),
				(this_or_next|troop_slot_ge, ":troop", 5, 2),
				(troop_slot_eq, ":var_2", slot_troop_love_interests_end, 1),
				(neg|troop_slot_eq, ":troop", slot_troop_met, 4),
				(try_begin),
					(eq, "$love_interest_in_town", 0),
					(assign, "$love_interest_in_town", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_2", 0),
					(assign, "$love_interest_in_town_2", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_3", 0),
					(assign, "$love_interest_in_town_3", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_4", 0),
					(assign, "$love_interest_in_town_4", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_5", 0),
					(assign, "$love_interest_in_town_5", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_6", 0),
					(assign, "$love_interest_in_town_6", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_7", 0),
					(assign, "$love_interest_in_town_7", ":troop"),
				(else_try),
					(eq, "$love_interest_in_town_8", 0),
					(assign, "$love_interest_in_town_8", ":troop"),
				(try_end),
			(try_end),
			(gt, "$love_interest_in_town", 0)
		],
		"Attempt to visit a lady",
		[
			(jump_to_menu, "mnu_lady_visit")
		], "Door_to_the_garden."),

		("meet_with_guild_master",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3)
		],
		"Meet with the guild master.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(call_script, "script_start_town_conversation", 25, 11),
			(try_end)
		], "."),

		("trade_with_merchants",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3)
		],
		"Go to the marketplace.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(jump_to_menu, "mnu_town_trade"),
			(try_end)
		], "."),

		("walled_center_manage",
		[
			(neg|party_slot_eq, "$current_town", slot_village_state, 5),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(assign, reg0, 1),
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(assign, reg0, 0),
			(try_end)
		],
		"Manage this {reg0?town:castle}.",
		[
			(assign, "$g_next_menu", "mnu_town"),
			(jump_to_menu, "mnu_center_manage")
		], "."),

		("walled_center_move_court",
		[
			(neg|party_slot_eq, "$current_town", slot_village_state, 5),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
			(neq, "$g_player_court", "$current_town")
		],
		"Move your court here.",
		[
			(jump_to_menu, "mnu_establish_court")
		], "."),

		("castle_station_troops",
		[
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(str_clear, 10),
			(assign, ":value", 0),
			(try_begin),
				(eq, ":current_town_town_lord", "trp_player"),
				(assign, ":value", 1),
			(else_try),
				(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
				(eq, ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
				(neg|party_slot_ge, "$g_encountered_party", 7, "trp_npc1"),
				(assign, ":value", 1),
			(else_try),
				(lt, ":current_town_town_lord", 0),
				(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party"),
				(eq, "$players_kingdom", ":faction_of_party_g_encountered_party_2"),
				(eq, "$g_encountered_party", "$g_castle_requested_by_player"),
				(str_store_string, 10, "str_retrieve_garrison_warning"),
				(assign, ":value", 1),
			(else_try),
				(lt, ":current_town_town_lord", 0),
				(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party"),
				(eq, "$players_kingdom", ":faction_of_party_g_encountered_party_2"),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_g_encountered_party", "$g_encountered_party"),
				(eq, ":party_size_wo_prisoners_g_encountered_party", 0),
				(str_store_string, 10, "str_retrieve_garrison_warning"),
				(assign, ":value", 1),
			(else_try),
				(party_slot_ge, "$g_encountered_party", 7, "trp_npc1"),
				(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party"),
				(eq, "$players_kingdom", ":faction_of_party_g_encountered_party_2"),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":current_town_town_lord"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 1)
		],
		"Manage the garrison {s10}",
		[
			(party_clear, "p_temp_party"),
			(jump_to_menu, "mnu_lance_prison")
		], "."),

		("town_spawn_manor",
		[
			(neg|party_slot_eq, "$current_town", slot_party_type, 2),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(party_get_slot, ":current_town_299", "$current_town", 299),
			(le, ":current_town_299", 0)
		],
		"Invest into regional manors.",
		[
			(assign, "$g_next_menu", "mnu_town"),
			(jump_to_menu, "mnu_center_spawn_manor")
		], "."),

		("castle_wait",
		[
			(this_or_next|ge, "$g_encountered_party_relation", 0),
			(eq, "$castle_undefended", 1),
			(assign, ":value", 1),
			(str_clear, 1),
			(try_begin),
				(neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
				(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
				(neg|party_slot_eq, "$current_town", slot_town_lord, ":player_spouse"),
				(party_slot_ge, "$current_town", 7, "trp_player"),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(neq, ":faction_of_party_current_town", "fac_player_supporters_faction"),
				(party_get_num_companions, ":num_companions_main_party", "p_main_party"),
				(store_div, reg1, ":num_companions_main_party", 4),
				(val_add, reg1, 1),
				(str_store_string, 1, "@ ({reg1} florins per night)"),
				(store_troop_gold, ":troop_gold_player", "trp_player"),
				(lt, ":troop_gold_player", reg1),
				(assign, ":value", 0),
			(try_end),
			(eq, ":value", 1)
		],
		"Wait here for some time{s1}.",
		[
			(assign, "$auto_enter_town", "$current_town"),
			(assign, "$g_town_visit_after_rest", 1),
			(assign, "$g_last_rest_center", "$current_town"),
			(assign, "$g_last_rest_payment_until", -1),
			(try_begin),
				(party_is_active, "p_main_party"),
				(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
				(try_begin),
					(eq, ":current_terrain_main_party", 5),
					(unlock_achievement, 28),
				(try_end),
			(try_end),
			(rest_for_hours_interactive, 168, 3, 0),
			(change_screen_return)
		], "."),

		("recruit_volunteers",
		[
			(call_script, "script_cf_town_recruit_volunteers_cond"),
			(assign, ":value", 0),
			(try_begin),
				(eq, "$use_feudal_lance", 1),
				(assign, ":value", 1),
				(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
				(assign, ":value", 0),
			(try_end),
			(eq, ":value", 0)
		],
		"Recruit Volunteers.",
		[
			(try_begin),
				(call_script, "script_cf_enter_center_location_bandit_check"),
			(else_try),
				(eq, "$use_feudal_lance", 0),
				(jump_to_menu, "mnu_recruit_volunteers"),
			(else_try),
				(eq, "$use_feudal_lance", 1),
				(jump_to_menu, "mnu_lance_recruitment"),
			(try_end)
		], "."),

		("recruit_specialists",
		[
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1")
		],
		"Recruit mercenary companions.",
		[
			(start_presentation, "prsnt_recruit_npc")
		], "."),

		("call_retinue",
		[
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(this_or_next|eq, ":current_town_town_lord", "trp_player"),
			(ge, "$cheat_mode", 1)
		],
		"Invite local nobles to your court.",
		[
			(set_jump_mission, "mt_visit_town_castle"),
			(mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
			(party_get_slot, ":current_town_town_castle", "$current_town", slot_town_castle),
			(modify_visitors_at_site, ":current_town_town_castle"),
			(reset_visitors),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(faction_get_slot, ":faction_of_party_current_town_guard_troop", ":faction_of_party_current_town", slot_faction_guard_troop),
			(try_begin),
				(le, ":faction_of_party_current_town_guard_troop", 0),
				(assign, ":faction_of_party_current_town_guard_troop", "trp_euro_spearman_3"),
			(try_end),
			(set_visitor, 6, ":faction_of_party_current_town_guard_troop"),
			(set_visitor, 7, ":faction_of_party_current_town_guard_troop"),
			(assign, ":var_4", 16),
			(assign, reg5, 0),
			(party_get_slot, ":current_town_center_culture", "$current_town", slot_center_culture),
			(party_get_slot, ":current_town_center_culture_2", "$current_town", slot_center_culture),
			(faction_get_slot, ":current_town_center_culture_2_101", ":current_town_center_culture_2", 101),
			(assign, ":value", -1),
			(assign, ":value_2", -1),
			(try_begin),
				(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_3"),
				(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_27"),
				(eq, ":current_town_center_culture", "fac_culture_mongol"),
				(faction_get_slot, ":current_town_center_culture_2_101", "fac_culture_mongol", 101),
				(assign, reg5, "$retinue_noble_mongol"),
				(val_add, "$retinue_noble_mongol", 1),
				(assign, ":value", "trp_npc13"),
				(assign, ":value_2", "trp_npc16"),
			(else_try),
				(eq, ":current_town_center_culture", "fac_culture_baltic"),
				(neq, ":faction_of_party_current_town", "fac_kingdom_1"),
				(assign, reg5, "$retinue_noble_balt"),
				(val_add, "$retinue_noble_balt", 1),
				(assign, ":value", "trp_npc1"),
				(assign, ":value_2", "trp_npc4"),
			(else_try),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_rus"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_serbian"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_balkan"),
				(eq, ":current_town_center_culture", "fac_culture_byzantium"),
				(assign, reg5, "$retinue_noble_orthodox"),
				(val_add, "$retinue_noble_orthodox", 1),
				(assign, ":value", "trp_npc7"),
				(assign, ":value_2", "trp_npc10"),
			(else_try),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_marinid"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_mamluke"),
				(this_or_next|eq, ":current_town_center_culture", "fac_culture_andalus"),
				(eq, ":current_town_center_culture", "fac_culture_anatolian"),
				(assign, reg5, "$retinue_noble_muslim"),
				(val_add, "$retinue_noble_muslim", 1),
				(assign, ":value", "trp_npc10"),
				(assign, ":value_2", "trp_npc13"),
			(else_try),
				(assign, reg5, "$retinue_noble_west"),
				(val_add, "$retinue_noble_west", 1),
				(assign, ":value", "trp_npc4"),
				(assign, ":value_2", "trp_npc7"),
				(eq, ":faction_of_party_current_town", "fac_kingdom_1"),
				(faction_get_slot, ":current_town_center_culture_2_101", "fac_culture_teutonic", 101),
			(try_end),
			(try_for_range, ":var_10", ":value", ":value_2"),
				(neg|troop_slot_eq, ":var_10", 400, 1),
				(troop_slot_eq, ":var_10", slot_troop_current_mission, 0),
				(troop_slot_eq, ":var_10", slot_troop_occupation, 0),
				(neg|troop_slot_ge, ":var_10", 8, 0),
				(neq, ":var_10", "$g_player_minister"),
				(neq, ":var_10", "$g_player_chamberlain"),
				(neq, ":var_10", "$g_player_constable"),
				(set_visitor, ":var_4", ":var_10"),
				(val_add, ":var_4", 1),
				(eq, reg5, 0),
				(call_script, "script_equip_companion", ":var_10", ":current_town_center_culture_2_101"),
			(try_end),
			(assign, "$talk_context", 1),
			(jump_to_scene, ":current_town_town_castle"),
			(change_screen_mission)
		], "."),

		("cheat_conquer_castle",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT: Instant conquer castle.",
		[
			(assign, "$g_next_menu", "mnu_castle_taken"),
			(jump_to_menu, "mnu_total_victory")
		], "."),

		("town_alley",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT: Go to the alley.",
		[
			(party_get_slot, reg11, "$current_town", slot_town_alley),
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, reg11),
			(change_screen_mission)
		], "."),

		("collect_taxes_qst",
		[
			(check_quest_active, "qst_collect_taxes"),
			(quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
			(neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
			(quest_get_slot, ":collect_taxes_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
			(str_store_troop_name, 1, ":collect_taxes_giver_troop"),
			(quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state)
		],
		"{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
		[
			(jump_to_menu, "mnu_collect_taxes")
		], "."),

		("town_leave",
		[],
		"Leave...",
		[
			(assign, "$g_permitted_to_center", 0),
			(change_screen_return, 0)
		], "Leave_Area."),

		("castle_cheat_interior",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Interior.",
		[
			(set_jump_mission, "mt_ai_training"),
			(party_get_slot, ":current_town_town_castle", "$current_town", slot_town_castle),
			(jump_to_scene, ":current_town_town_castle"),
			(change_screen_mission)
		], "."),

		("castle_cheat_town_exterior",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Exterior.",
		[
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(else_try),
				(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(try_end),
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, ":current_town_town_center"),
			(change_screen_mission)
		], "."),

		("castle_cheat_dungeon",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Prison.",
		[
			(set_jump_mission, "mt_ai_training"),
			(party_get_slot, ":current_town_town_prison", "$current_town", slot_town_prison),
			(jump_to_scene, ":current_town_town_prison"),
			(change_screen_mission)
		], "."),

		("castle_cheat_town_walls",
		[
			(eq, "$cheat_mode", 1),
			(party_slot_eq, "$current_town", slot_party_type, 3)
		],
		"{!}CHEAT! Town Walls.",
		[
			(party_get_slot, ":current_town_town_walls", "$current_town", slot_town_walls),
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, ":current_town_town_walls"),
			(change_screen_mission)
		], "."),

		("cheat_town_start_siege",
		[
			(eq, "$cheat_mode", 1),
			(party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
			(lt, "$g_encountered_party_2", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(gt, reg0, 1),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(assign, reg6, 1),
			(else_try),
				(assign, reg6, 0),
			(try_end)
		],
		"{!}CHEAT: Besiege the {reg6?town:castle}...",
		[
			(assign, "$g_player_besiege_town", "$g_encountered_party"),
			(jump_to_menu, "mnu_castle_besiege")
		], "."),

		("center_reports",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT! Show reports.",
		[
			(jump_to_menu, "mnu_center_reports")
		], "."),

		("sail_from_port",
		[
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(eq, "$cheat_mode", 1)
		],
		"{!}CHEAT: Sail from port.",
		[
			(assign, "$g_player_icon_state", 2),
			(party_set_flags, "p_main_party", 512, 1),
			(party_get_position, 1, "p_main_party"),
			(map_get_water_position_around_position, 2, 1, 6),
			(party_set_position, "p_main_party", 2),
			(assign, "$g_main_ship_party", -1),
			(change_screen_return)
		], ".")
	]
	),

	("cannot_enter_court", 0, "There is a feast in progress in the lord's hall, but you are not of sufficient status to be invited inside. Perhaps increasing your renown would win you admittance -- or you might also try distinguishing yourself at a tournament while the feast is in progress...",
"none",
	[],
	[
		("continue",
		[],
		"Continue",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("lady_visit", 0, "Whom do you wish to visit?",
"none",
	[],
	[
		("visit_lady_1",
		[
			(gt, "$love_interest_in_town", 0),
			(str_store_troop_name, 12, "$love_interest_in_town")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("visit_lady_2",
		[
			(gt, "$love_interest_in_town_2", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_2")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_2"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("visit_lady_3",
		[
			(gt, "$love_interest_in_town_3", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_3")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_3"),
			(jump_to_menu, "mnu_garden")
		], "Door_to_the_garden."),

		("visit_lady_4",
		[
			(gt, "$love_interest_in_town_4", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_4")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_4"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("visit_lady_5",
		[
			(gt, "$love_interest_in_town_5", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_5")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_5"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("visit_lady_6",
		[
			(gt, "$love_interest_in_town_6", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_6")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_6"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("visit_lady_7",
		[
			(gt, "$love_interest_in_town_7", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_7")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_7"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("visit_lady_8",
		[
			(gt, "$love_interest_in_town_8", 0),
			(str_store_troop_name, 12, "$love_interest_in_town_8")
		],
		"Visit {s12}",
		[
			(assign, "$love_interest_in_town", "$love_interest_in_town_8"),
			(jump_to_menu, "mnu_garden")
		], "."),

		("leave",
		[],
		"Leave",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("town_tournament_lost", 0, "You have been eliminated from the tournament.{s8}",
"none",
	[
		(str_clear, 8),
		(try_begin),
			(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
			(neg|troop_slot_ge, "trp_player", 7, 50),
			(neg|troop_slot_ge, "trp_player", 7, 125),
			(gt, "$g_player_tournament_placement", 4),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, 6),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
			(str_store_string, 8, "str__however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town_tournament_won_by_another")
		], ".")
	]
	),

	("town_tournament_won", 0, "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name. In addition to honour, fame and glory, you earn a prize of {reg9} florins. {s8}",
"none",
	[
		(str_store_party_name, 3, "$current_town"),
		(call_script, "script_change_troop_renown", "trp_player", 20),
		(call_script, "script_change_player_relation_with_center", "$current_town", 10),
		(assign, reg9, 5000),
		(add_xp_to_troop, 250, "trp_player"),
		(troop_add_gold, "trp_player", reg9),
		(str_clear, 8),
		(store_add, ":value", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
		(try_begin),
			(gt, "$g_tournament_bet_win_amount", 0),
			(assign, reg8, ":value"),
			(str_store_string, 8, "@Moreover, you earn {reg8} florins from the clever bets you placed on yourself..."),
		(try_end),
		(try_begin),
			(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
			(neg|troop_slot_ge, "trp_player", 7, 70),
			(neg|troop_slot_ge, "trp_player", 7, 145),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, 6),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
			(str_store_string, 8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
		(try_end),
		(troop_add_gold, "trp_player", ":value"),
		(assign, ":value_2", 0),
		(store_div, ":value_2", "$g_tournament_bet_win_amount", 5),
		(party_get_slot, ":current_town_town_player_odds", "$current_town", slot_town_player_odds),
		(val_sub, ":current_town_town_player_odds", ":value_2"),
		(val_max, ":current_town_town_player_odds", 250),
		(party_set_slot, "$current_town", slot_town_player_odds, ":current_town_town_player_odds"),
		(call_script, "script_play_victorious_sound"),
		(unlock_achievement, 33)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("town_tournament_won_by_another", 0, "As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament.",
"none",
	[
		(troop_get_slot, ":temp_array_c_1", "trp_temp_array_c", 1),
		(troop_get_slot, ":tournament_participants_1", "trp_tournament_participants", 1),
		(try_for_range, reg0, 2, 8),
			(troop_get_slot, ":temp_array_c_reg0", "trp_temp_array_c", reg0),
			(gt, ":temp_array_c_reg0", ":temp_array_c_1"),
			(troop_get_slot, ":temp_array_c_1", "trp_temp_array_c", reg0),
			(troop_get_slot, ":tournament_participants_1", "trp_tournament_participants", reg0),
		(try_end),
		(str_store_troop_name, 1, ":tournament_participants_1"),
		(troop_get_type, reg3, ":tournament_participants_1")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("town_tournament", 0, "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
"none",
	[
		(party_set_slot, "$current_town", slot_town_has_tournament, 0),
		(call_script, "script_sort_tournament_participant_troops"),
		(call_script, "script_get_num_tournament_participants"),
		(assign, ":var_1", reg0),
		(try_begin),
			(neg|troop_slot_eq, "trp_tournament_participants", slot_troop_relations_begin, 0),
			(assign, ":value", 0),
			(store_div, ":value", "$g_tournament_bet_placed", 5),
			(party_get_slot, ":current_town_town_player_odds", "$current_town", slot_town_player_odds),
			(val_add, ":current_town_town_player_odds", ":value"),
			(val_min, ":current_town_town_player_odds", 4000),
			(party_set_slot, "$current_town", slot_town_player_odds, ":current_town_town_player_odds"),
			(jump_to_menu, "mnu_town_tournament_lost"),
		(else_try),
			(eq, ":var_1", 1),
			(jump_to_menu, "mnu_town_tournament_won"),
		(else_try),
			(try_begin),
				(le, "$g_tournament_next_num_teams", 0),
				(call_script, "script_get_random_tournament_team_amount_and_size"),
				(assign, "$g_tournament_next_num_teams", reg0),
				(assign, "$g_tournament_next_team_size", reg1),
			(try_end),
			(assign, reg2, "$g_tournament_next_num_teams"),
			(assign, reg3, "$g_tournament_next_team_size"),
			(store_sub, reg4, reg3, 1),
			(str_clear, 1),
			(try_begin),
				(eq, "$g_tournament_player_team_won", 1),
				(str_store_string, 1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
			(else_try),
				(eq, "$g_tournament_player_team_won", 0),
				(str_store_string, 1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
			(try_end),
			(assign, reg1, ":var_1"),
			(store_add, reg0, "$g_tournament_cur_tier", 1),
		(try_end)
	],
	[
		("tournament_view_participants",
		[],
		"View participants.",
		[
			(jump_to_menu, "mnu_tournament_participants")
		], "."),

		("tournament_bet",
		[
			(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")
		],
		"Place a bet on yourself.",
		[
			(jump_to_menu, "mnu_tournament_bet")
		], "."),

		("tournament_join_next_fight",
		[],
		"Fight in the next round.",
		[
			(party_get_slot, ":current_town_town_arena", "$current_town", slot_town_arena),
			(modify_visitors_at_site, ":current_town_town_arena"),
			(reset_visitors),
			(assign, "$g_player_tournament_placement", "$g_tournament_cur_tier"),
			(try_begin),
				(gt, "$g_player_tournament_placement", 4),
				(assign, "$g_player_eligible_feast_center_no", "$current_town"),
			(try_end),
			(val_add, "$g_tournament_cur_tier", 1),
			(store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
			(troop_set_slot, "trp_tournament_participants", slot_troop_relations_begin, -1),
			(troop_set_slot, "trp_temp_array_a", slot_troop_relations_begin, "trp_player"),
			(try_for_range, ":globalvariable", 1, "$g_tournament_num_participants_for_fight"),
				(call_script, "script_get_random_tournament_participant"),
				(troop_set_slot, "trp_temp_array_a", ":globalvariable", reg0),
			(try_end),
			(call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),
			(try_for_range, ":globalvariable", 0, 4),
				(troop_set_slot, "trp_temp_array_b", ":globalvariable", ":globalvariable"),
			(try_end),
			(call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),
			(assign, ":var_3", 0),
			(try_for_range, ":globalvariable_2", 0, "$g_tournament_next_num_teams"),
				(troop_get_slot, ":temp_array_b_globalvariable_2", "trp_temp_array_b", ":globalvariable_2"),
				(try_for_range, ":globalvariable", 0, 8),
					(troop_set_slot, "trp_temp_array_c", ":globalvariable", ":globalvariable"),
				(try_end),
				(call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),
				(try_for_range, ":globalvariable_3", 0, "$g_tournament_next_team_size"),
					(store_mul, ":value", ":temp_array_b_globalvariable_2", 8),
					(troop_get_slot, ":temp_array_c_globalvariable_3", "trp_temp_array_c", ":globalvariable_3"),
					(val_add, ":value", ":temp_array_c_globalvariable_3"),
					(troop_get_slot, ":temp_array_a_var_3", "trp_temp_array_a", ":var_3"),
					(set_visitor, ":value", ":temp_array_a_var_3"),
					(val_add, ":var_3", 1),
				(try_end),
			(try_end),
			(assign, "$g_tournament_next_num_teams", 0),
			(assign, "$g_tournament_next_team_size", 0),
			(assign, "$g_mt_mode", 3),
			(party_get_slot, ":current_town_center_original_faction", "$current_town", slot_center_original_faction),
			(assign, ":var_11", 0),
			(assign, ":value_2", "p_castle_1_1"),
			(try_for_range, ":party", "p_town_1_1", ":value_2"),
				(try_begin),
					(eq, ":party", "$current_town"),
					(assign, ":value_2", 0),
				(else_try),
					(party_slot_eq, ":party", slot_center_original_faction, ":current_town_center_original_faction"),
					(val_add, ":var_11", 1),
				(try_end),
			(try_end),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(call_script, "script_raf_aor_faction_to_region", ":faction_of_party_current_town"),
			(try_begin),
				(this_or_next|eq, reg0, 3),
				(this_or_next|eq, reg0, 15),
				(eq, reg0, 1),
				(set_jump_mission, "mt_arena_tournament_fight_foot"),
			(else_try),
				(set_jump_mission, "mt_arena_tournament_fight"),
			(try_end),
			(jump_to_scene, ":current_town_town_arena"),
			(change_screen_mission)
		], "."),

		("leave_tournament",
		[],
		"Withdraw from the tournament.",
		[
			(jump_to_menu, "mnu_tournament_withdraw_verify")
		], ".")
	]
	),

	("tournament_withdraw_verify", 0, "Are you sure you want to withdraw from the tournament?",
"none",
	[],
	[
		("tournament_withdraw_yes",
		[],
		"Yes. This is a pointless affectation.",
		[
			(jump_to_menu, "mnu_town_tournament_won_by_another")
		], "."),

		("tournament_withdraw_no",
		[],
		"No, not as long as there is a chance of victory!",
		[
			(jump_to_menu, "mnu_town_tournament_new")
		], ".")
	]
	),

	("tournament_bet", 0, "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} florins on yourself, and if you win, you will earn {reg2} florins.:} How much do you want to bet?",
"none",
	[
		(assign, reg1, "$g_tournament_bet_placed"),
		(store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
		(call_script, "script_get_win_amount_for_tournament_bet"),
		(assign, ":var_1", reg0),
		(assign, ":value", 100000),
		(assign, ":value_2", 1),
		(assign, ":value_3", 1),
		(try_for_range, ":number", 1, 50),
			(try_for_range, ":number_2", 1, 50),
				(store_mul, ":value_4", 100, ":number"),
				(val_div, ":value_4", ":number_2"),
				(store_sub, ":value_5", ":var_1", ":value_4"),
				(val_abs, ":value_5"),
				(lt, ":value_5", ":value"),
				(assign, ":value", ":value_5"),
				(assign, ":value_2", ":number_2"),
				(assign, ":value_3", ":number"),
			(try_end),
		(try_end),
		(assign, reg5, ":value_3"),
		(assign, reg6, ":value_2")
	],
	[
		("bet_500_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 500)
		],
		"500 florins.",
		[
			(assign, "$temp", 500),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("bet_250_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 250)
		],
		"250 florins.",
		[
			(assign, "$temp", 250),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("bet_100_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 100)
		],
		"100 florins.",
		[
			(assign, "$temp", 100),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("bet_50_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 50)
		],
		"50 florins.",
		[
			(assign, "$temp", 50),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("bet_20_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 20)
		],
		"20 florins.",
		[
			(assign, "$temp", 20),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("bet_10_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 10)
		],
		"10 florins.",
		[
			(assign, "$temp", 10),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("bet_5_denars",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 5)
		],
		"5 florins.",
		[
			(assign, "$temp", 5),
			(jump_to_menu, "mnu_tournament_bet_confirm")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_town_tournament_new")
		], ".")
	]
	),

	("tournament_bet_confirm", 0, "If you bet {reg1} florins, you will earn {reg2} florins if you win the tournament. Is that all right?",
"none",
	[
		(call_script, "script_get_win_amount_for_tournament_bet"),
		(assign, ":var_1", reg0),
		(val_mul, ":var_1", "$temp"),
		(val_div, ":var_1", 100),
		(assign, reg1, "$temp"),
		(assign, reg2, ":var_1")
	],
	[
		("tournament_bet_accept",
		[],
		"Go ahead.",
		[
			(call_script, "script_tournament_place_bet", "$temp"),
			(jump_to_menu, "mnu_town_tournament_new")
		], "."),

		("tournament_bet_cancel",
		[],
		"Forget it.",
		[
			(jump_to_menu, "mnu_tournament_bet")
		], ".")
	]
	),

	("tournament_participants", 0, "You ask one of the criers for the names of the tournament participants. They are:^{s11}",
"none",
	[
		(str_clear, 11),
		(call_script, "script_sort_tournament_participant_troops"),
		(call_script, "script_get_num_tournament_participants"),
		(assign, ":var_1", reg0),
		(try_for_range, ":localvariable", 0, ":var_1"),
			(troop_get_slot, ":tournament_participants_localvariable", "trp_tournament_participants", ":localvariable"),
			(str_store_troop_name, 12, ":tournament_participants_localvariable"),
			(str_store_string, 11, "@{!}{s11}^{s12}"),
		(try_end)
	],
	[
		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_town_tournament")
		], ".")
	]
	),

	("town_tournament_start_new", 0, "Select which type of tournament do you wish to participate in. You can only participate in one of them.",
"none",
	[
		(assign, "$current_opponent", 0)
	],
	[
		("join_one_on_one",
		[],
		"Join one on one tournament.",
		[
			(party_set_slot, "$current_town", slot_town_has_tournament, 0),
			(assign, "$tournament_type", 0),
			(call_script, "script_init_tournament_participents", "$current_town"),
			(jump_to_menu, "mnu_town_tournament_new")
		], "."),

		("join_team_on_team",
		[
			(try_begin),
				(store_party_size, ":party_size_main_party", "p_main_party"),
				(lt, ":party_size_main_party", 5),
				(eq, "$freelancer_state", 0),
				(display_message, "@You do not have five men in your party to form a team!"),
			(try_end)
		],
		"Join team on team tournament.",
		[
			(party_set_slot, "$current_town", slot_town_has_tournament, 0),
			(assign, "$tournament_type", 1),
			(call_script, "script_init_tournament_participents", "$current_town"),
			(jump_to_menu, "mnu_town_tournament_new")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("town_tournament_new", 0, "{s2}^Current rankings:^ {s1}",
"none",
	[
		(set_background_mesh, "mesh_pic_tournament_euro"),
		(party_set_slot, "$current_town", slot_town_has_tournament, 0),
		(str_clear, 1),
		(try_for_range, reg0, 0, 8),
			(troop_get_slot, ":temp_array_c_reg0", "trp_temp_array_c", reg0),
			(assign, reg1, ":temp_array_c_reg0"),
			(store_sub, reg2, "$current_opponent", ":temp_array_c_reg0"),
			(troop_get_slot, ":tournament_participants_reg0", "trp_tournament_participants", reg0),
			(str_store_troop_name, 0, ":tournament_participants_reg0"),
			(try_begin),
				(eq, "$tournament_type", 0),
				(str_store_string, 1, "@{s1} {s0} wins:{reg1}, loses: {reg2}^"),
			(else_try),
				(str_store_string, 0, "@{s0}'s team"),
				(str_store_string, 1, "@{s1} {s0}, wins:{reg1}, loses: {reg2}^"),
			(try_end),
		(try_end),
		(str_store_string, 2, "@The tournament has ended!"),
		(try_begin),
			(lt, "$current_opponent", 7),
			(store_add, ":value", "$current_opponent", 1),
			(troop_get_slot, ":tournament_participants_reg0", "trp_tournament_participants", ":value"),
			(str_store_troop_name, 0, ":tournament_participants_reg0"),
			(str_store_string, 2, "@Your next opponent: {s0}"),
			(try_begin),
				(set_fixed_point_multiplier, 100),
				(position_set_x, 0, 70),
				(position_set_y, 0, 5),
				(position_set_z, 0, 75),
				(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":tournament_participants_reg0", 0),
			(try_end),
		(try_end),
		(troop_get_slot, ":temp_array_c_relations_begin", "trp_temp_array_c", slot_troop_relations_begin),
		(assign, "$g_player_tournament_placement", ":temp_array_c_relations_begin")
	],
	[
		("end_tournament",
		[
			(ge, "$current_opponent", 7)
		],
		"The tournament has ended, let's get drunk!",
		[
			(troop_get_slot, ":temp_array_c_relations_begin", "trp_temp_array_c", slot_troop_relations_begin),
			(try_for_range, reg0, 1, 8),
				(troop_get_slot, ":temp_array_c_reg0", "trp_temp_array_c", reg0),
				(gt, ":temp_array_c_reg0", ":temp_array_c_relations_begin"),
				(assign, ":temp_array_c_relations_begin", -1),
			(try_end),
			(try_begin),
				(eq, ":temp_array_c_relations_begin", -1),
				(jump_to_menu, "mnu_town_tournament_won_by_another"),
			(else_try),
				(assign, "$g_player_eligible_feast_center_no", "$current_town"),
				(jump_to_menu, "mnu_town_tournament_won"),
			(try_end)
		], "."),

		("bash_heads",
		[
			(lt, "$current_opponent", 7)
		],
		"Let's go bash some skulls!",
		[
			(party_get_slot, ":current_town_town_arena", "$current_town", slot_town_arena),
			(modify_visitors_at_site, ":current_town_town_arena"),
			(reset_visitors),
			(val_add, "$current_opponent", 1),
			(call_script, "script_simulate_next_battle", "$current_opponent"),
			(try_begin),
				(eq, "$tournament_type", 0),
				(troop_get_slot, ":tournament_participants_current_opponent", "trp_tournament_participants", "$current_opponent"),
				(set_visitor, 0, "trp_player"),
				(set_visitor, 8, ":tournament_participants_current_opponent"),
			(else_try),
				(eq, "$tournament_type", 1),
				(set_visitor, 0, "trp_player"),
				(try_for_range, reg0, 1, 5),
					(troop_get_slot, ":tournament_participants_current_opponent", "trp_temp_array_b", reg0),
					(ge, ":tournament_participants_current_opponent", 1),
					(set_visitor, reg0, ":tournament_participants_current_opponent"),
				(try_end),
				(store_mul, ":value", "$current_opponent", 5),
				(store_add, ":value_2", ":value", 5),
				(assign, ":var_5", 8),
				(try_for_range, reg0, ":value", ":value_2"),
					(troop_get_slot, ":tournament_participants_current_opponent", "trp_temp_array_b", reg0),
					(set_visitor, ":var_5", ":tournament_participants_current_opponent"),
					(val_add, ":var_5", 1),
				(try_end),
			(try_end),
			(assign, "$g_mt_mode", 3),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(faction_get_slot, ":faction_of_party_current_town_culture", ":faction_of_party_current_town", slot_faction_culture),
			(try_begin),
				(this_or_next|eq, ":faction_of_party_current_town_culture", "fac_culture_finnish"),
				(this_or_next|eq, ":faction_of_party_current_town_culture", "fac_culture_rus"),
				(this_or_next|eq, ":faction_of_party_current_town_culture", "fac_culture_baltic"),
				(eq, ":faction_of_party_current_town_culture", "fac_culture_gaelic"),
				(set_jump_mission, "mt_arena_tournament_fight_foot"),
			(else_try),
				(set_jump_mission, "mt_arena_tournament_fight"),
			(try_end),
			(jump_to_scene, ":current_town_town_arena"),
			(change_screen_mission)
		], "."),

		("participents",
		[
			(eq, "$tournament_type", 1)
		],
		"View the combatants.",
		[
			(jump_to_menu, "mnu_town_tournament_participents")
		], "."),

		("bet",
		[
			(lt, "$current_opponent", 7),
			(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")
		],
		"Place a bet on yourself.",
		[
			(jump_to_menu, "mnu_tournament_bet")
		], "."),

		("leave",
		[],
		"No more - I quit!",
		[
			(lt, "$current_opponent", 7),
			(jump_to_menu, "mnu_tournament_withdraw_verify")
		], ".")
	]
	),

	("town_tournament_participents", 0, "{s0}",
"none",
	[
		(str_clear, 0),
		(try_for_range, reg0, 0, 8),
			(troop_get_slot, ":tournament_participants_reg0", "trp_tournament_participants", reg0),
			(str_store_troop_name, 1, ":tournament_participants_reg0"),
			(store_mul, ":value", 5, reg0),
			(store_add, ":value_2", ":value", 5),
			(str_clear, 2),
			(try_for_range, reg1, ":value", ":value_2"),
				(troop_get_slot, ":temp_array_b_reg1", "trp_temp_array_b", reg1),
				(str_store_troop_name, 3, ":temp_array_b_reg1"),
				(str_store_string, 2, "@{s2} {s3};"),
			(try_end),
			(str_store_string, 0, "@{s0}{s1} team, consisting of: {s2}^"),
		(try_end)
	],
	[
		("go_back_dot",
		[],
		"I see.",
		[
			(jump_to_menu, "mnu_town_tournament_new")
		], ".")
	]
	),

	("collect_taxes", 0, "As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} that collecting taxes from here will take {reg4} days...",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
		(assign, ":var_1", reg0),
		(assign, reg2, reg0),
		(assign, ":var_2", reg1),
		(try_begin),
			(eq, ":var_2", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 1, ":var_2"),
		(try_end),
		(assign, ":value", 3000),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, 3),
			(assign, ":value", 6000),
		(try_end),
		(try_begin),
			(quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
			(store_add, ":value_2", ":var_1", 30),
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(store_div, "$qst_collect_taxes_total_hours", 5040, ":value_2"),
			(else_try),
				(store_div, "$qst_collect_taxes_total_hours", 2160, ":value_2"),
			(try_end),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(val_add, reg0, 20),
			(val_mul, "$qst_collect_taxes_total_hours", 20),
			(val_div, "$qst_collect_taxes_total_hours", reg0),
			(quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, "$qst_collect_taxes_total_hours"),
			(store_div, ":value_3", "$qst_collect_taxes_total_hours", 20),
			(store_div, ":value_4", "$qst_collect_taxes_total_hours", 4),
			(assign, ":var_7", ":value_4"),
			(store_mul, ":value_5", "$qst_collect_taxes_total_hours", 3),
			(val_div, ":value_5", 4),
			(val_mul, ":value", 2),
			(store_div, "$qst_collect_taxes_hourly_income", ":value", "$qst_collect_taxes_total_hours"),
			(store_random_in_range, "$qst_collect_taxes_menu_counter", ":value_3", ":value_4"),
			(store_random_in_range, "$qst_collect_taxes_unrest_counter", ":var_7", ":value_5"),
			(assign, "$qst_collect_taxes_halve_taxes", 0),
		(try_end),
		(quest_get_slot, ":collect_taxes_target_amount", "qst_collect_taxes", slot_quest_target_amount),
		(store_div, ":value_6", ":collect_taxes_target_amount", 24),
		(val_mul, ":value_6", 24),
		(try_begin),
			(lt, ":value_6", ":collect_taxes_target_amount"),
			(val_add, ":value_6", 24),
		(try_end),
		(val_div, ":value_6", 24),
		(assign, reg4, ":value_6")
	],
	[
		("start_collecting",
		[],
		"Start collecting.",
		[
			(assign, "$qst_collect_taxes_currently_collecting", 1),
			(try_begin),
				(quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
				(quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 1),
			(try_end),
			(rest_for_hours_interactive, 1000, 5, 0),
			(assign, "$auto_enter_town", "$current_town"),
			(assign, "$g_town_visit_after_rest", 1),
			(change_screen_return)
		], "."),

		("collect_later",
		[],
		"Put it off until later.",
		[
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], ".")
	]
	),

	("collect_taxes_complete", 0, "You've collected {reg3} florins in taxes from {s3}. {s19} will be expecting you to take the money to him.",
"none",
	[
		(str_store_party_name, 3, "$current_town"),
		(quest_get_slot, ":collect_taxes_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
		(str_store_troop_name, 19, ":collect_taxes_giver_troop"),
		(quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
		(try_begin),
			(eq, "$qst_collect_taxes_halve_taxes", 0),
			(call_script, "script_change_player_relation_with_center", "$current_town", -2),
		(try_end),
		(call_script, "script_succeed_quest", "qst_collect_taxes")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("collect_taxes_rebels_killed", 0, "Your quick action and strong arm have successfully put down the revolt. Surely, anyone with a mind to rebel against you will think better of it after this.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_map)
		], ".")
	]
	),

	("collect_taxes_failed", 0, "You could collect only {reg3} florins as tax from {s3} before the revolt broke out. {s1} won't be happy, but some silver will placate him better than nothing at all...",
"none",
	[
		(str_store_party_name, 3, "$current_town"),
		(quest_get_slot, ":collect_taxes_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
		(str_store_troop_name, 1, ":collect_taxes_giver_troop"),
		(quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
		(call_script, "script_fail_quest", "qst_collect_taxes"),
		(quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
		(rest_for_hours, 0, 0, 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_map)
		], ".")
	]
	),

	("collect_taxes_revolt_warning", 0, "The people of {s3} are outraged at your demands and decry it as nothing more than extortion. They're getting very restless, and they may react badly if you keep pressing them.",
"none",
	[
		(str_store_party_name, 3, "$current_town")
	],
	[
		("continue_collecting_taxes",
		[],
		"Ignore them and continue.",
		[
			(change_screen_return)
		], "."),

		("halve_taxes",
		[
			(quest_get_slot, ":collect_taxes_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
			(str_store_troop_name, 1, ":collect_taxes_giver_troop")
		],
		"Agree to reduce your collection by half. ({s1} may be upset)",
		[
			(assign, "$qst_collect_taxes_halve_taxes", 1),
			(change_screen_return)
		], ".")
	]
	),

	("collect_taxes_revolt", 0, "You are interrupted while collecting the taxes at {s3}. A large band of angry {reg9?peasants:townsmen} is marching nearer, shouting about the exorbitant taxes and waving torches and weapons. It looks like they aim to fight you!",
"none",
	[
		(str_store_party_name, 3, "$current_town"),
		(assign, reg9, 0),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, 4),
			(assign, reg9, 1),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(set_jump_mission, "mt_back_alley_revolt"),
			(quest_get_slot, ":collect_taxes_target_center", "qst_collect_taxes", slot_quest_target_center),
			(try_begin),
				(party_slot_eq, ":collect_taxes_target_center", slot_party_type, 3),
				(party_get_slot, ":collect_taxes_target_center_town_alley", ":collect_taxes_target_center", slot_town_alley),
			(else_try),
				(party_get_slot, ":collect_taxes_target_center_town_alley", ":collect_taxes_target_center", slot_town_center),
			(try_end),
			(modify_visitors_at_site, ":collect_taxes_target_center_town_alley"),
			(reset_visitors),
			(assign, ":var_3", 6),
			(store_character_level, ":character_level_player", "trp_player"),
			(val_div, ":character_level_player", 5),
			(val_add, ":var_3", ":character_level_player"),
			(set_visitors, 1, "trp_tax_rebel", ":var_3"),
			(jump_to_scene, ":collect_taxes_target_center_town_alley"),
			(change_screen_mission)
		], ".")
	]
	),

	("train_peasants_against_bandits", 0, "As the party member with the highest training skill ({reg2}), {reg3?you expect:{s1} expects} that getting some peasants ready for practice will take {reg4} hours.",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
		(assign, ":var_1", reg0),
		(assign, reg2, reg0),
		(assign, ":var_2", reg1),
		(try_begin),
			(eq, ":var_2", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 1, ":var_2"),
		(try_end),
		(store_sub, ":value", 20, ":var_1"),
		(val_mul, ":value", 3),
		(val_div, ":value", 5),
		(store_sub, reg4, ":value", "$qst_train_peasants_against_bandits_num_hours_trained")
	],
	[
		("make_preparation",
		[],
		"Train them.",
		[
			(assign, "$qst_train_peasants_against_bandits_currently_training", 1),
			(rest_for_hours_interactive, 1000, 5, 0),
			(assign, "$auto_enter_town", "$current_town"),
			(assign, "$g_town_visit_after_rest", 1),
			(change_screen_return)
		], "."),

		("train_later",
		[],
		"Put it off until later.",
		[
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("train_peasants_against_bandits_ready", 0, "You put the peasants through the basics of soldiering, discipline and obedience. You think {reg0} of them {reg1?have:has} fully grasped the training and {reg1?are:is} ready for some practice.",
"none",
	[
		(store_character_level, ":character_level_player", "trp_player"),
		(val_div, ":character_level_player", 10),
		(val_add, ":character_level_player", 1),
		(quest_get_slot, ":train_peasants_against_bandits_target_amount", "qst_train_peasants_against_bandits", slot_quest_target_amount),
		(quest_get_slot, ":train_peasants_against_bandits_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
		(val_sub, ":train_peasants_against_bandits_target_amount", ":train_peasants_against_bandits_current_state"),
		(assign, ":var_4", ":character_level_player"),
		(val_min, ":var_4", ":train_peasants_against_bandits_target_amount"),
		(val_add, ":var_4", 1),
		(store_random_in_range, ":random_in_range_1_var_4", 1, ":var_4"),
		(assign, "$g_train_peasants_against_bandits_num_peasants", ":random_in_range_1_var_4"),
		(assign, reg0, ":random_in_range_1_var_4"),
		(store_sub, reg1, ":random_in_range_1_var_4", 1),
		(str_store_troop_name_by_count, 0, "trp_trainee_peasant", ":random_in_range_1_var_4")
	],
	[
		("peasant_start_practice",
		[],
		"Start the practice fight.",
		[
			(set_jump_mission, "mt_village_training"),
			(quest_get_slot, ":train_peasants_against_bandits_target_center", "qst_train_peasants_against_bandits", slot_quest_target_center),
			(party_get_slot, ":train_peasants_against_bandits_target_center_town_center", ":train_peasants_against_bandits_target_center", slot_town_center),
			(modify_visitors_at_site, ":train_peasants_against_bandits_target_center_town_center"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitors, 1, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
			(set_jump_entry, 11),
			(jump_to_scene, ":train_peasants_against_bandits_target_center_town_center"),
			(jump_to_menu, "mnu_train_peasants_against_bandits_training_result"),
			(music_set_situation, 0),
			(change_screen_mission)
		], ".")
	]
	),

	("train_peasants_against_bandits_training_result", 0, "{s0}",
"none",
	[
		(assign, reg5, "$g_train_peasants_against_bandits_num_peasants"),
		(str_store_troop_name_by_count, 0, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
		(try_begin),
			(eq, "$g_train_peasants_against_bandits_training_succeeded", 0),
			(str_store_string, 0, "@You were beaten. The peasants are heartened by their success, but the lesson you wanted to teach them probably didn't get through..."),
		(else_try),
			(str_store_string, 0, "@After beating your last opponent, you explain to the peasants how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time."),
			(quest_get_slot, ":train_peasants_against_bandits_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
			(val_add, ":train_peasants_against_bandits_current_state", "$g_train_peasants_against_bandits_num_peasants"),
			(quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_current_state, ":train_peasants_against_bandits_current_state"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(quest_get_slot, ":train_peasants_against_bandits_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
				(quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_amount, ":train_peasants_against_bandits_current_state"),
				(jump_to_menu, "mnu_train_peasants_against_bandits_attack"),
			(else_try),
				(change_screen_map),
			(try_end)
		], ".")
	]
	),

	("train_peasants_against_bandits_attack", 0, "As you get ready to continue the training, a sentry from the village runs up to you, shouting alarums. The bandits have been spotted on the horizon, riding hard for {s3}. The elder begs that you organize your newly-trained militia and face them.",
"none",
	[
		(str_store_party_name, 3, "$current_town")
	],
	[
		("peasants_against_bandits_attack_resist",
		[],
		"Prepare for a fight!",
		[
			(store_random_in_range, ":random_in_range_0_3", 0, 3),
			(try_begin),
				(eq, ":random_in_range_0_3", 0),
				(assign, ":value", "trp_bandit"),
			(else_try),
				(eq, ":random_in_range_0_3", 1),
				(assign, ":value", "trp_mountain_bandit"),
			(else_try),
				(assign, ":value", "trp_forest_bandit"),
			(try_end),
			(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
			(modify_visitors_at_site, ":g_encountered_party_town_center"),
			(reset_visitors),
			(store_character_level, ":character_level_player", "trp_player"),
			(val_div, ":character_level_player", 2),
			(store_add, ":value_2", ":character_level_player", 16),
			(store_add, ":value_3", ":value_2", 6),
			(store_random_in_range, ":random_in_range_0_3", ":value_2", ":value_3"),
			(set_visitors, 0, ":value", ":random_in_range_0_3"),
			(assign, ":var_7", ":value_3"),
			(set_visitors, 2, "trp_trainee_peasant", ":var_7"),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			(assign, "$g_battle_result", 0),
			(set_jump_mission, "mt_village_attack_bandits"),
			(jump_to_scene, ":g_encountered_party_town_center"),
			(assign, "$g_next_menu", "mnu_train_peasants_against_bandits_attack_result"),
			(jump_to_menu, "mnu_battle_debrief"),
			(assign, "$g_mt_mode", 2),
			(change_screen_mission)
		], ".")
	]
	),

	("train_peasants_against_bandits_attack_result", 0, "{s9}",
"none",
	[
		(try_begin),
			(eq, "$g_battle_result", 1),
			(str_store_string, 9, "@The bandits are broken! Those few who remain alive and conscious run off with their tails between their legs, terrified of the peasants and their new champion."),
			(call_script, "script_succeed_quest", "qst_train_peasants_against_bandits"),
			(jump_to_menu, "mnu_train_peasants_against_bandits_success"),
		(else_try),
			(call_script, "script_fail_quest", "qst_train_peasants_against_bandits"),
			(str_store_string, 9, "@Try as you might, you could not defeat the bandits. Infuriated, they raze the village to the ground to punish the peasants, and then leave the burning wasteland behind to find greener pastures to plunder."),
			(set_background_mesh, "mesh_pic_looted_village"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(call_script, "script_village_set_state", "$current_town", 2),
				(party_set_slot, "$current_town", slot_village_raid_progress, 0),
				(party_set_slot, "$current_town", slot_village_recover_progress, 0),
				(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
				(call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
			(try_end),
			(change_screen_map)
		], ".")
	]
	),

	("train_peasants_against_bandits_success", 0, "The bandits are broken! Those few who remain run off with their tails between their legs, terrified of the peasants and their new champion. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find to show their gratitude.",
"none",
	[
		(party_clear, "p_temp_party"),
		(call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
		(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
		(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
		(try_for_range, ":number", 10, 106),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(lt, ":random_in_range_0_100", 50),
			(troop_set_inventory_slot, ":current_town_town_elder", ":number", -1),
		(try_end),
		(call_script, "script_add_log_entry", 4, "trp_player", "$current_town", -1, -1)
	],
	[
		("village_bandits_defeated_accept",
		[],
		"Take it as your just due.",
		[
			(jump_to_menu, "mnu_auto_return_to_map"),
			(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
			(troop_sort_inventory, ":current_town_town_elder"),
			(change_screen_loot, ":current_town_town_elder")
		], "."),

		("village_bandits_defeated_cont",
		[],
		"Refuse, stating that they need these items more than you do.",
		[
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
			(call_script, "script_change_player_honor", 1),
			(change_screen_map)
		], ".")
	]
	),

	("disembark", 0, "Do you wish to disembark?",
"none",
	[],
	[
		("disembark_yes",
		[],
		"Yes.",
		[
			(assign, "$g_player_icon_state", 0),
			(party_set_flags, "p_main_party", 512, 0),
			(party_get_position, 1, "p_main_party"),
			(party_set_position, "p_main_party", 0),
			(try_begin),
				(le, "$g_main_ship_party", 0),
				(set_spawn_radius, 0),
				(spawn_around_party, "p_main_party", "pt_none"),
				(assign, "$g_main_ship_party", reg0),
				(party_set_flags, "$g_main_ship_party", 2115072, 1),
				(str_store_troop_name, 1, "trp_player"),
				(party_set_name, "$g_main_ship_party", "@{s1}'s Ship"),
				(party_set_icon, "$g_main_ship_party", "icon_ship"),
				(party_set_slot, "$g_main_ship_party", slot_party_type, 16),
			(try_end),
			(enable_party, "$g_main_ship_party"),
			(party_set_position, "$g_main_ship_party", 0),
			(party_set_icon, "$g_main_ship_party", "icon_ship_on_land"),
			(assign, "$g_main_ship_party", -1),
			(change_screen_return)
		], "."),

		("disembark_no",
		[],
		"No.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("ship_reembark", 0, "Do you wish to embark?",
"none",
	[],
	[
		("reembark_yes",
		[],
		"Yes.",
		[
			(assign, "$g_player_icon_state", 2),
			(party_set_flags, "p_main_party", 512, 1),
			(party_get_position, 1, "p_main_party"),
			(map_get_water_position_around_position, 2, 1, 6),
			(party_set_position, "p_main_party", 2),
			(assign, "$g_main_ship_party", "$g_encountered_party"),
			(disable_party, "$g_encountered_party"),
			(change_screen_return)
		], "."),

		("reembark_no",
		[],
		"No.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("center_reports", 0, "Town Name: {s1}^Rent Income: {reg1} florins^Tariff Income: {reg2} florins^Food Stock: for {reg3} days",
"none",
	[
		(party_get_slot, ":g_encountered_party_food_store", "$g_encountered_party", slot_party_food_store),
		(call_script, "script_center_get_food_consumption", "$g_encountered_party"),
		(assign, ":var_2", reg0),
		(try_begin),
			(gt, ":var_2", 0),
			(store_div, reg3, ":g_encountered_party_food_store", ":var_2"),
		(else_try),
			(assign, reg3, 9999),
		(try_end),
		(str_store_party_name, 1, "$g_encountered_party"),
		(party_get_slot, reg1, "$g_encountered_party", slot_center_accumulated_rents),
		(party_get_slot, reg2, "$g_encountered_party", slot_center_accumulated_tariffs)
	],
	[
		("to_price_and_productions",
		[],
		"Show prices and productions.",
		[
			(jump_to_menu, "mnu_price_and_production")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
				(jump_to_menu, "mnu_village"),
			(else_try),
				(jump_to_menu, "mnu_town"),
			(try_end)
		], ".")
	]
	),

	("price_and_production", 0, "Productions are:^(Note: base/modified by raw materials/modified by materials plus prosperity)^{s1}^^Price factors are:^{s2}",
"none",
	[
		(assign, ":var_1", 0),
		(assign, ":var_2", 0),
		(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
			(call_script, "script_center_get_goods_availability", ":party"),
			(val_add, ":var_1", reg0),
		(try_end),
		(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
			(call_script, "script_center_get_goods_availability", ":party"),
			(val_add, ":var_2", reg0),
		(try_end),
		(val_div, ":var_2", 110),
		(val_div, ":var_1", 22),
		(call_script, "script_center_get_goods_availability", "$g_encountered_party"),
		(assign, reg1, ":var_1"),
		(assign, reg2, ":var_2"),
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_string, 1, "str___hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__"),
			(display_message, "@{!}DEBUG - {s1}"),
		(try_end),
		(try_for_range, ":item", "itm_spice", "itm_siege_supply"),
			(neq, ":item", "itm_pork"),
			(neq, ":item", "itm_chicken"),
			(neq, ":item", "itm_butter"),
			(neq, ":item", "itm_cattle_meat"),
			(neq, ":item", "itm_cabbages"),
			(call_script, "script_center_get_production", "$g_encountered_party", ":item"),
			(assign, ":var_5", reg0),
			(assign, ":var_6", reg2),
			(assign, ":var_7", reg1),
			(call_script, "script_center_get_consumption", "$g_encountered_party", ":item"),
			(assign, ":var_8", reg2),
			(assign, ":var_9", reg1),
			(assign, ":var_10", reg0),
			(store_sub, ":value", ":item", "itm_spice"),
			(val_add, ":value", 250),
			(party_get_slot, ":g_encountered_party_value", "$g_encountered_party", ":value"),
			(assign, ":var_13", 0),
			(assign, ":var_14", 0),
			(assign, ":var_15", 0),
			(assign, ":var_16", 0),
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(neg|is_between, ":party", "p_castle_1_1", "p_village_1_1"),
				(val_add, ":var_13", 1),
				(call_script, "script_center_get_production", ":party", ":item"),
				(assign, ":var_17", reg2),
				(call_script, "script_center_get_consumption", ":party", ":item"),
				(store_add, ":value_2", reg1, reg2),
				(party_get_slot, ":party_value", ":party", ":value"),
				(val_add, ":var_14", ":party_value"),
				(val_add, ":var_15", ":var_17"),
				(val_add, ":var_16", ":value_2"),
			(try_end),
			(assign, ":var_20", ":var_15"),
			(assign, ":var_21", ":var_16"),
			(val_div, ":var_14", ":var_13"),
			(val_div, ":var_15", ":var_13"),
			(val_div, ":var_16", ":var_13"),
			(str_store_item_name, 3, ":item"),
			(assign, reg1, ":var_6"),
			(assign, reg2, ":var_7"),
			(assign, reg3, ":var_5"),
			(assign, reg4, ":g_encountered_party_value"),
			(assign, reg5, ":var_15"),
			(assign, reg6, ":var_14"),
			(assign, reg7, ":var_8"),
			(assign, reg8, ":var_9"),
			(assign, reg9, ":var_10"),
			(assign, reg10, ":var_16"),
			(item_get_slot, ":item_production_slot", ":item", slot_item_production_slot),
			(party_get_slot, ":g_encountered_party_item_production_slot", "$g_encountered_party", ":item_production_slot"),
			(assign, reg11, ":g_encountered_party_item_production_slot"),
			(assign, reg12, ":var_20"),
			(assign, reg13, ":var_21"),
			(item_get_slot, ":item_production_string", ":item", slot_item_production_string),
			(str_store_string, 4, ":item_production_string"),
			(str_store_string, 1, "str___s3_price_=_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_"),
		(try_end)
	],
	[
		("go_back_dot",
		[],
		"Go back.",
		[
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
				(jump_to_menu, "mnu_village"),
			(else_try),
				(jump_to_menu, "mnu_town"),
			(try_end)
		], ".")
	]
	),

	("town_trade", 0, "You head towards the marketplace.",
"none",
	[],
	[
		("auto_sell",
		[],
		"Sell items automatically.",
		[
			(assign, "$g_next_menu", "mnu_town"),
			(jump_to_menu, "mnu_trade_auto_sell_begin")
		], "."),

		("assess_prices",
		[
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(store_relation, ":relation_faction_of_party_current_town_player_supporters_faction", ":faction_of_party_current_town", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_current_town_player_supporters_faction", 0)
		],
		"Assess the local prices.",
		[
			(jump_to_menu, "mnu_town_trade_assessment_begin")
		], "."),

		("trade_with_arms_merchant",
		[
			(party_slot_ge, "$current_town", 21, 1)
		],
		"Trade with the arms merchant.",
		[
			(party_get_slot, ":current_town_town_weaponsmith", "$current_town", slot_town_weaponsmith),
			(change_screen_trade, ":current_town_town_weaponsmith")
		], "."),

		("trade_with_armor_merchant",
		[
			(party_slot_ge, "$current_town", 22, 1)
		],
		"Trade with the armor merchant.",
		[
			(party_get_slot, ":current_town_town_armorer", "$current_town", slot_town_armorer),
			(change_screen_trade, ":current_town_town_armorer")
		], "."),

		("trade_with_horse_merchant",
		[
			(party_slot_ge, "$current_town", 24, 1)
		],
		"Trade with the horse merchant.",
		[
			(party_get_slot, ":current_town_town_horse_merchant", "$current_town", slot_town_horse_merchant),
			(change_screen_trade, ":current_town_town_horse_merchant")
		], "."),

		("trade_with_goods_merchant",
		[
			(party_slot_ge, "$current_town", 23, 1)
		],
		"Trade with the goods merchant.",
		[
			(party_get_slot, ":current_town_town_merchant", "$current_town", slot_town_merchant),
			(change_screen_trade, ":current_town_town_merchant")
		], "."),

		("auto_buy_food",
		[],
		"Buy food automatically.",
		[
			(assign, "$g_next_menu", "mnu_town"),
			(jump_to_menu, "mnu_trade_auto_buy_food_begin")
		], "."),

		("back_to_town_menu",
		[],
		"Head back.",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("trade_auto_sell_begin", 0, "Items in the inventory of companions which are selected as the type to sell and the prices of the items are below {reg1} florins will be sold to {reg2?all merchants:the elder} in current {reg2?town:village} automatically. Foods, trade goods and books will never be sold.^^You can change some settings here freely. ",
"none",
	[
		(assign, reg1, "$g_auto_sell_price_limit"),
		(try_begin),
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(assign, reg2, 1),
		(else_try),
			(assign, reg2, 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
				(party_get_slot, ":current_town_town_weaponsmith", "$current_town", slot_town_weaponsmith),
				(party_get_slot, ":current_town_town_armorer", "$current_town", slot_town_armorer),
				(party_get_slot, ":current_town_town_horse_merchant", "$current_town", slot_town_horse_merchant),
				(party_get_slot, ":current_town_town_merchant", "$current_town", slot_town_merchant),
			(else_try),
				(is_between, "$current_town", "p_village_1_1", "p_salt_mine"),
				(party_get_slot, ":current_town_town_elder", "$current_town", slot_town_elder),
			(try_end),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range_backwards, ":var_7", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_var_7", "p_main_party", ":var_7"),
				(is_between, ":party_stack_troop_id_main_party_var_7", "trp_npc1", "trp_kingdom_1_lord"),
				(store_free_inventory_capacity, ":free_inventory_capacity_party_stack_troop_id_main_party_var_7", ":party_stack_troop_id_main_party_var_7"),
				(store_troop_gold, ":troop_gold_party_stack_troop_id_main_party_var_7", ":party_stack_troop_id_main_party_var_7"),
				(try_begin),
					(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
					(call_script, "script_auto_sell", ":party_stack_troop_id_main_party_var_7", ":current_town_town_weaponsmith"),
					(call_script, "script_auto_sell", ":party_stack_troop_id_main_party_var_7", ":current_town_town_armorer"),
					(call_script, "script_auto_sell", ":party_stack_troop_id_main_party_var_7", ":current_town_town_horse_merchant"),
					(call_script, "script_auto_sell", ":party_stack_troop_id_main_party_var_7", ":current_town_town_merchant"),
				(else_try),
					(is_between, "$current_town", "p_village_1_1", "p_salt_mine"),
					(call_script, "script_auto_sell", ":party_stack_troop_id_main_party_var_7", ":current_town_town_elder"),
				(try_end),
				(store_free_inventory_capacity, ":free_inventory_capacity_party_stack_troop_id_main_party_var_7_2", ":party_stack_troop_id_main_party_var_7"),
				(store_troop_gold, ":troop_gold_party_stack_troop_id_main_party_var_7_2", ":party_stack_troop_id_main_party_var_7"),
				(neq, ":troop_gold_party_stack_troop_id_main_party_var_7_2", ":troop_gold_party_stack_troop_id_main_party_var_7"),
				(store_sub, ":value", ":troop_gold_party_stack_troop_id_main_party_var_7_2", ":troop_gold_party_stack_troop_id_main_party_var_7"),
				(set_show_messages, 0),
				(troop_remove_gold, ":party_stack_troop_id_main_party_var_7", ":value"),
				(troop_add_gold, "trp_player", ":value"),
				(set_show_messages, 1),
				(store_sub, reg1, ":free_inventory_capacity_party_stack_troop_id_main_party_var_7_2", ":free_inventory_capacity_party_stack_troop_id_main_party_var_7"),
				(assign, reg2, ":value"),
				(store_sub, reg3, reg1, 1),
				(store_sub, reg4, reg2, 1),
				(str_store_troop_name, 1, ":party_stack_troop_id_main_party_var_7"),
				(display_message, "@{s1} sold {reg1} {reg3?items:item} and recieved {reg2} {reg4?florins:florin}."),
			(try_end),
			(jump_to_menu, "$g_next_menu")
		], "."),

		("change_settings",
		[],
		"Change settings.",
		[
			(start_presentation, "prsnt_auto_sell_options")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "$g_next_menu")
		], ".")
	]
	),

	("trade_auto_buy_food_begin", 0, "You will buy any food which you don't have for one portion automatically. Do you want to continue?",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, ":value", 0),
			(try_begin),
				(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
				(party_get_slot, ":current_town_town_merchant", "$current_town", slot_town_merchant),
			(else_try),
				(is_between, "$current_town", "p_village_1_1", "p_salt_mine"),
				(party_get_slot, ":current_town_town_merchant", "$current_town", slot_town_elder),
			(try_end),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(store_free_inventory_capacity, ":free_inventory_capacity_player", "trp_player"),
			(set_show_messages, 0),
			(troop_get_inventory_capacity, ":inventory_capacity_current_town_town_merchant", ":current_town_town_merchant"),
			(try_for_range, ":localvariable", 10, ":inventory_capacity_current_town_town_merchant"),
				(troop_get_inventory_slot, ":inventory_slot_current_town_town_merchant_localvariable", ":current_town_town_merchant", ":localvariable"),
				(gt, ":inventory_slot_current_town_town_merchant_localvariable", -1),
				(is_between, ":inventory_slot_current_town_town_merchant_localvariable", "itm_smoked_fish", "itm_siege_supply"),
				(troop_inventory_slot_get_item_amount, ":troop_inventory_slot_item_amount_current_town_town_merchant_localvariable", ":current_town_town_merchant", ":localvariable"),
				(troop_inventory_slot_get_item_max_amount, ":value", ":current_town_town_merchant", ":localvariable"),
				(eq, ":troop_inventory_slot_item_amount_current_town_town_merchant_localvariable", ":value"),
				(neg|player_has_item, ":inventory_slot_current_town_town_merchant_localvariable"),
				(store_free_inventory_capacity, ":free_inventory_capacity_player_2", "trp_player"),
				(gt, ":free_inventory_capacity_player_2", 0),
				(call_script, "script_game_get_item_buy_price_factor", ":inventory_slot_current_town_town_merchant_localvariable"),
				(assign, ":var_10", reg0),
				(store_item_value, ":item_value_inventory_slot_current_town_town_merchant_localvariable", ":inventory_slot_current_town_town_merchant_localvariable"),
				(val_mul, ":item_value_inventory_slot_current_town_town_merchant_localvariable", ":var_10"),
				(val_div, ":item_value_inventory_slot_current_town_town_merchant_localvariable", 100),
				(val_max, ":item_value_inventory_slot_current_town_town_merchant_localvariable", 1),
				(store_troop_gold, ":troop_gold_player_2", "trp_player"),
				(ge, ":troop_gold_player_2", ":item_value_inventory_slot_current_town_town_merchant_localvariable"),
				(troop_add_item, "trp_player", ":inventory_slot_current_town_town_merchant_localvariable"),
				(troop_set_inventory_slot, ":current_town_town_merchant", ":localvariable", -1),
				(troop_remove_gold, "trp_player", ":item_value_inventory_slot_current_town_town_merchant_localvariable"),
				(troop_add_gold, ":current_town_town_merchant", ":item_value_inventory_slot_current_town_town_merchant_localvariable"),
			(try_end),
			(set_show_messages, 1),
			(store_troop_gold, ":troop_gold_player_3", "trp_player"),
			(store_free_inventory_capacity, ":free_inventory_capacity_player_3", "trp_player"),
			(try_begin),
				(neq, ":troop_gold_player_3", ":troop_gold_player"),
				(store_sub, reg1, ":troop_gold_player", ":troop_gold_player_3"),
				(store_sub, reg2, ":free_inventory_capacity_player", ":free_inventory_capacity_player_3"),
				(store_sub, reg3, reg1, 1),
				(store_sub, reg4, reg2, 1),
				(display_message, "@You have bought {reg2} {reg4?kinds:kind} of food and lost {reg1} {reg3?florins:florin}."),
			(try_end),
			(jump_to_menu, "$g_next_menu")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "$g_next_menu")
		], ".")
	]
	),

	("town_trade_assessment_begin", 0, "You overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
"none",
	[
		(str_clear, 42)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$auto_enter_town", "$current_town"),
			(assign, "$g_town_assess_trade_goods_after_rest", 1),
			(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
			(val_div, reg0, 2),
			(store_sub, ":value", 6, reg0),
			(assign, "$g_last_rest_center", "$current_town"),
			(assign, "$g_last_rest_payment_until", -1),
			(rest_for_hours, ":value", 5, 0),
			(change_screen_return)
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_town_trade")
		], ".")
	]
	),

	("town_trade_assessment", 0, "As the party member with the highest trade skill ({reg2}), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}",
"none",
	[
		(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
		(assign, ":var_1", reg0),
		(assign, ":var_2", reg1),
		(assign, ":var_3", 0),
		(assign, ":value", -1),
		(assign, ":value_2", -1),
		(assign, ":value_3", 0),
		(assign, ":value_4", -1),
		(assign, ":value_5", -1),
		(assign, ":value_6", 0),
		(assign, ":value_7", -1),
		(assign, ":value_8", -1),
		(assign, ":value_9", 0),
		(store_sub, ":value_10", "p_castle_1_1", "p_town_1_1"),
		(store_sub, ":value_11", "itm_siege_supply", "itm_spice"),
		(store_mul, ":value_12", ":value_10", ":value_11"),
		(val_mul, ":value_12", ":var_1"),
		(val_div, ":value_12", 20),
		(assign, ":var_16", "$g_encountered_party"),
		(try_for_range, ":unused", 0, ":value_12"),
			(store_random_in_range, ":random_in_range_spice_siege_supply", "itm_spice", "itm_siege_supply"),
			(store_random_in_range, ":random_in_range_town_1_1_castle_1_1", "p_town_1_1", "p_castle_1_1"),
			(assign, ":var_20", 0),
			(try_begin),
				(eq, ":random_in_range_spice_siege_supply", ":value"),
				(eq, ":random_in_range_town_1_1_castle_1_1", ":value_2"),
				(val_add, ":var_20", 1),
			(else_try),
				(eq, ":random_in_range_spice_siege_supply", ":value_4"),
				(eq, ":random_in_range_town_1_1_castle_1_1", ":value_5"),
				(val_add, ":var_20", 1),
			(else_try),
				(eq, ":random_in_range_spice_siege_supply", ":value_7"),
				(eq, ":random_in_range_town_1_1_castle_1_1", ":value_8"),
				(val_add, ":var_20", 1),
			(try_end),
			(eq, ":var_20", 0),
			(store_item_value, ":item_value_random_in_range_spice_siege_supply", ":random_in_range_spice_siege_supply"),
			(assign, "$g_encountered_party", ":var_16"),
			(call_script, "script_game_get_item_buy_price_factor", ":random_in_range_spice_siege_supply"),
			(store_mul, ":value_13", ":item_value_random_in_range_spice_siege_supply", reg0),
			(val_div, ":value_13", 100),
			(val_max, ":value_13", 1),
			(assign, "$g_encountered_party", ":random_in_range_town_1_1_castle_1_1"),
			(call_script, "script_game_get_item_sell_price_factor", ":random_in_range_spice_siege_supply"),
			(store_mul, ":value_14", ":item_value_random_in_range_spice_siege_supply", reg0),
			(val_div, ":value_14", 100),
			(val_max, ":value_14", 1),
			(store_sub, ":value_15", ":value_14", ":value_13"),
			(try_begin),
				(gt, ":value_15", ":value_3"),
				(val_add, ":var_3", 1),
				(val_min, ":var_3", 3),
				(assign, ":value_7", ":value_4"),
				(assign, ":value_8", ":value_5"),
				(assign, ":value_9", ":value_6"),
				(assign, ":value_4", ":value"),
				(assign, ":value_5", ":value_2"),
				(assign, ":value_6", ":value_3"),
				(assign, ":value", ":random_in_range_spice_siege_supply"),
				(assign, ":value_2", ":random_in_range_town_1_1_castle_1_1"),
				(assign, ":value_3", ":value_15"),
			(else_try),
				(gt, ":value_15", ":value_6"),
				(val_add, ":var_3", 1),
				(val_min, ":var_3", 3),
				(assign, ":value_7", ":value_4"),
				(assign, ":value_8", ":value_5"),
				(assign, ":value_9", ":value_6"),
				(assign, ":value_4", ":random_in_range_spice_siege_supply"),
				(assign, ":value_5", ":random_in_range_town_1_1_castle_1_1"),
				(assign, ":value_6", ":value_15"),
			(else_try),
				(gt, ":value_15", ":value_9"),
				(val_add, ":var_3", 1),
				(val_min, ":var_3", 3),
				(assign, ":value_7", ":random_in_range_spice_siege_supply"),
				(assign, ":value_8", ":random_in_range_town_1_1_castle_1_1"),
				(assign, ":value_9", ":value_15"),
			(try_end),
		(try_end),
		(assign, "$g_encountered_party", ":var_16"),
		(str_clear, 3),
		(assign, reg2, ":var_1"),
		(try_begin),
			(eq, ":var_2", "trp_player"),
			(assign, reg3, 1),
		(else_try),
			(assign, reg3, 0),
			(str_store_troop_name, 1, ":var_2"),
		(try_end),
		(try_begin),
			(le, ":var_3", 0),
			(str_store_string, 2, "@However, {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit."),
		(else_try),
			(try_begin),
				(ge, ":value_7", 0),
				(assign, reg6, ":value_9"),
				(str_store_item_name, 4, ":value_7"),
				(str_store_party_name, 5, ":value_8"),
				(str_store_string, 3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} florins per item.{s3}"),
			(try_end),
			(try_begin),
				(ge, ":value_4", 0),
				(assign, reg6, ":value_6"),
				(str_store_item_name, 4, ":value_4"),
				(str_store_party_name, 5, ":value_5"),
				(str_store_string, 3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} florins per item.{s3}"),
			(try_end),
			(try_begin),
				(ge, ":value", 0),
				(assign, reg6, ":value_3"),
				(str_store_item_name, 4, ":value"),
				(str_store_party_name, 5, ":value_2"),
				(str_store_string, 3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} florins per item.{s3}"),
			(try_end),
			(str_store_string, 2, "@{reg3?You find:{s1} finds} out the following:^{s3}"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town_trade")
		], ".")
	]
	),

	("sneak_into_town_suceeded", 0, "Disguised in the garments of a poor pilgrim, you fool the guards and make your way into the town.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$sneaked_into_town", 1),
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("sneak_into_town_caught", 0, "As you try to sneak in, one of the guards recognizes you and raises the alarm! You must flee back through the gates before all the guards in the town come down on you!",
"none",
	[
		(assign, "$auto_menu", "mnu_captivity_start_castle_surrender")
	],
	[
		("sneak_caught_fight",
		[],
		"Try to fight your way out!",
		[
			(assign, "$all_doors_locked", 1),
			(party_get_slot, ":current_town_town_center", "$current_town", slot_town_center),
			(modify_visitors_at_site, ":current_town_town_center"),
			(reset_visitors),
			(try_begin),
				(this_or_next|eq, "$talk_context", 19),
				(eq, "$talk_context", 18),
				(set_jump_entry, 7),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(set_jump_entry, 0),
			(else_try),
				(set_jump_entry, 1),
			(try_end),
			(set_jump_mission, "mt_sneak_caught_fight"),
			(set_passage_menu, "mnu_town"),
			(jump_to_scene, ":current_town_town_center"),
			(change_screen_mission)
		], "."),

		("sneak_caught_surrender",
		[],
		"Surrender.",
		[
			(jump_to_menu, "mnu_captivity_start_castle_surrender")
		], ".")
	]
	),

	("sneak_into_town_caught_dispersed_guards", 0, "You drive off the guards and cover your trail before running off, easily losing your pursuers in the maze of streets.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$sneaked_into_town", 1),
			(assign, "$town_entered", 1),
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("sneak_into_town_caught_ran_away", 0, "You make your way back through the gates and quickly retreat to the safety of the countryside.{s11}",
"none",
	[
		(str_clear, 11),
		(assign, ":value", 0),
		(assign, ":value_2", "trp_heroes_end"),
		(try_for_range, ":troop", "trp_npc1", ":value_2"),
			(try_begin),
				(troop_slot_eq, ":troop", slot_troop_mission_participation, 4),
				(assign, "$talk_context", 8),
				(assign, reg14, ":troop"),
				(call_script, "script_setup_troop_meeting", ":troop", -1),
				(troop_set_slot, ":troop", slot_troop_mission_participation, -1),
				(troop_get_slot, ":troop_prisoner_of_party", ":troop", slot_troop_prisoner_of_party),
				(party_remove_prisoners, ":troop_prisoner_of_party", ":troop", 1),
				(troop_set_slot, ":troop", slot_troop_prisoner_of_party, -1),
				(assign, ":value_2", -1),
			(else_try),
				(troop_slot_eq, ":troop", slot_troop_mission_participation, 5),
				(str_store_troop_name, 12, ":troop"),
				(try_begin),
					(eq, ":value", 0),
					(str_store_string, 11, "str_s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind"),
				(else_try),
					(str_store_string, 11, "str_s11_also_s12_was_wounded_and_had_to_be_left_behind"),
				(try_end),
				(assign, ":value", 1),
			(try_end),
			(troop_set_slot, ":troop", slot_troop_mission_participation, 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$auto_menu", -1),
			(store_encountered_party, "$last_sneak_attempt_town"),
			(store_current_hours, "$last_sneak_attempt_time"),
			(change_screen_return)
		], ".")
	]
	),

	("enemy_offer_ransom_for_prisoner", 0, "{s2} offers you a sum of {reg12} florins in silver if you are willing to sell him {s1}.",
"none",
	[
		(call_script, "script_calculate_ransom_amount_for_troop", "$g_ransom_offer_troop"),
		(assign, reg12, reg0),
		(str_store_troop_name, 1, "$g_ransom_offer_troop"),
		(store_faction_of_troop, ":faction_of_troop_g_ransom_offer_troop", "$g_ransom_offer_troop"),
		(str_store_faction_name, 2, ":faction_of_troop_g_ransom_offer_troop")
	],
	[
		("ransom_accept",
		[],
		"Accept the offer.",
		[
			(troop_add_gold, "trp_player", reg12),
			(party_remove_prisoners, "$g_ransom_offer_party", "$g_ransom_offer_troop", 1),
			(call_script, "script_remove_troop_from_prison", "$g_ransom_offer_troop"),
			(change_screen_return)
		], "."),

		("ransom_reject",
		[],
		"Reject the offer.",
		[
			(call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
			(call_script, "script_change_player_honor", -1),
			(assign, "$g_ransom_offer_rejected", 1),
			(change_screen_return)
		], ".")
	]
	),

	("training_ground", 0, "You approach a training field where you can practice your martial skills. What kind of training do you want to do?",
"none",
	[
		(store_add, "$g_training_ground_melee_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
		(val_sub, "$g_training_ground_melee_training_scene", "p_training_ground"),
		(try_begin),
			(ge, "$g_training_ground_training_count", 3),
			(assign, "$g_training_ground_training_count", 0),
			(rest_for_hours, 1, 5, 1),
			(assign, "$auto_enter_town", "$g_encountered_party"),
			(change_screen_return),
		(try_end)
	],
	[
		("camp_trainer",
		[],
		"Speak with the trainer.",
		[
			(set_jump_mission, "mt_training_ground_trainer_talk"),
			(modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
			(reset_visitors),
			(set_jump_entry, 5),
			(jump_to_scene, "$g_training_ground_melee_training_scene"),
			(change_screen_mission),
			(music_set_situation, 0)
		], "."),

		("camp_train_melee",
		[
			(neg|troop_is_wounded, "trp_player"),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(gt, reg0, 1)
		],
		"Sparring practice.",
		[
			(assign, "$g_mt_mode", 1),
			(jump_to_menu, "mnu_training_ground_selection_details_melee_1"),
			(music_set_situation, 0)
		], "."),

		("camp_train_archery",
		[],
		"Ranged weapon practice.",
		[
			(jump_to_menu, "mnu_training_ground_selection_details_ranged_1"),
			(music_set_situation, 0)
		], "."),

		("camp_train_mounted",
		[],
		"Horseback practice.",
		[
			(assign, "$g_mt_mode", 3),
			(jump_to_menu, "mnu_training_ground_selection_details_mounted"),
			(music_set_situation, 0)
		], "."),

		("go_to_track",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}Cheat: Go to track.",
		[
			(set_jump_mission, "mt_ai_training"),
			(store_add, ":value", "scn_training_ground_horse_track_1", "$g_encountered_party"),
			(val_sub, ":value", "p_training_ground"),
			(jump_to_scene, ":value"),
			(change_screen_mission)
		], "."),

		("go_to_range",
		[
			(eq, "$cheat_mode", 1)
		],
		"{!}Cheat: Go to range.",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "$g_training_ground_melee_training_scene"),
			(change_screen_mission)
		], "."),

		("leave",
		[],
		"Leave.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("training_ground_selection_details_melee_1", 0, "How many opponents will you go against?",
"none",
	[
		(call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
		(troop_get_slot, "$temp", "trp_stack_selection_amounts", 1),
		(assign, "$temp_2", 1)
	],
	[
		("camp_train_melee_num_men_1",
		[
			(ge, "$temp", 1)
		],
		"One.",
		[
			(assign, "$temp", 1),
			(jump_to_menu, "mnu_training_ground_selection_details_melee_2")
		], "."),

		("camp_train_melee_num_men_2",
		[
			(ge, "$temp", 2)
		],
		"Two.",
		[
			(assign, "$temp", 2),
			(jump_to_menu, "mnu_training_ground_selection_details_melee_2")
		], "."),

		("camp_train_melee_num_men_3",
		[
			(ge, "$temp", 3)
		],
		"Three.",
		[
			(assign, "$temp", 3),
			(jump_to_menu, "mnu_training_ground_selection_details_melee_2")
		], "."),

		("camp_train_melee_num_men_4",
		[
			(ge, "$temp", 4)
		],
		"Four.",
		[
			(assign, "$temp", 4),
			(jump_to_menu, "mnu_training_ground_selection_details_melee_2")
		], "."),

		("go_back_dot",
		[],
		"Cancel.",
		[
			(jump_to_menu, "mnu_training_ground")
		], ".")
	]
	),

	("training_ground_selection_details_melee_2", 0, "Choose your opponent #{reg1}:",
"none",
	[
		(assign, reg1, "$temp_2"),
		(troop_get_slot, "$temp_3", "trp_stack_selection_amounts", slot_troop_relations_begin)
	],
	[
		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 1)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 1)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 2)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 2)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 3)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 3)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 4)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 4)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 5)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 5)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 6)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 6)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 7)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 7)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 8)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 8)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 9)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 9)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 10)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 10)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 11)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 11)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 12)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 12)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 13)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 13)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 14)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 14)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 15)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 15)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 16)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 16)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 17)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 17)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 18)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 18)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 19)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 19)
		], "."),

		("s0",
		[
			(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 20)
		],
		"{s0}",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", 20)
		], "."),

		("training_ground_selection_details_melee_random",
		[],
		"Choose randomly.",
		[
			(call_script, "script_training_ground_sub_routine_2_for_melee_details", -1)
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_training_ground")
		], ".")
	]
	),

	("training_ground_selection_details_mounted", 0, "What kind of weapon do you want to train with?",
"none",
	[],
	[
		("camp_train_mounted_details_1",
		[],
		"One handed weapon.",
		[
			(call_script, "script_start_training_at_training_ground", 2, 0)
		], "."),

		("camp_train_mounted_details_2",
		[],
		"Polearm.",
		[
			(call_script, "script_start_training_at_training_ground", 4, 0)
		], "."),

		("camp_train_mounted_details_3",
		[],
		"Bow.",
		[
			(call_script, "script_start_training_at_training_ground", 8, 0)
		], "."),

		("camp_train_mounted_details_4",
		[],
		"Thrown weapon.",
		[
			(call_script, "script_start_training_at_training_ground", 10, 0)
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_training_ground")
		], ".")
	]
	),

	("training_ground_selection_details_ranged_1", 0, "What kind of ranged weapon do you want to train with?",
"none",
	[],
	[
		("camp_train_ranged_weapon_bow",
		[],
		"Bow and arrows.",
		[
			(assign, "$g_mt_mode", 2),
			(assign, "$temp", 8),
			(jump_to_menu, "mnu_training_ground_selection_details_ranged_2")
		], "."),

		("camp_train_ranged_weapon_crossbow",
		[],
		"Crossbow.",
		[
			(assign, "$g_mt_mode", 2),
			(assign, "$temp", 9),
			(jump_to_menu, "mnu_training_ground_selection_details_ranged_2")
		], "."),

		("camp_train_ranged_weapon_thrown",
		[],
		"Throwing Knives.",
		[
			(assign, "$g_mt_mode", 2),
			(assign, "$temp", 10),
			(jump_to_menu, "mnu_training_ground_selection_details_ranged_2")
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_training_ground")
		], ".")
	]
	),

	("training_ground_selection_details_ranged_2", 0, "What range do you want to practice at?",
"none",
	[],
	[
		("camp_train_ranged_details_1",
		[],
		"10 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 10)
		], "."),

		("camp_train_ranged_details_2",
		[],
		"20 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 20)
		], "."),

		("camp_train_ranged_details_3",
		[],
		"30 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 30)
		], "."),

		("camp_train_ranged_details_4",
		[],
		"40 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 40)
		], "."),

		("camp_train_ranged_details_5",
		[
			(eq, "$g_mt_mode", 2)
		],
		"50 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 50)
		], "."),

		("camp_train_ranged_details_6",
		[
			(eq, "$g_mt_mode", 2)
		],
		"60 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 60)
		], "."),

		("camp_train_ranged_details_7",
		[
			(eq, "$g_mt_mode", 2)
		],
		"70 yards.",
		[
			(call_script, "script_start_training_at_training_ground", "$temp", 70)
		], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_training_ground")
		], ".")
	]
	),

	("training_ground_description", 0, "{s0}",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_scene, "$g_training_ground_training_scene"),
			(change_screen_mission)
		], ".")
	]
	),

	("training_ground_training_result", 0, "{s7}{s2}",
"none",
	[
		(store_skill_level, ":skill_level_trainer_player", "skl_trainer", "trp_player"),
		(store_add, ":value", 5, ":skill_level_trainer_player"),
		(call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
		(str_clear, 2),
		(troop_get_slot, ":stack_selection_amounts_1", "trp_stack_selection_amounts", 1),
		(troop_get_slot, ":stack_selection_amounts_relations_begin", "trp_stack_selection_amounts", slot_troop_relations_begin),
		(try_begin),
			(gt, "$g_training_ground_training_success_ratio", 0),
			(store_mul, ":value_2", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
			(try_begin),
				(eq, "$g_training_ground_training_success_ratio", 100),
				(val_mul, ":value_2", 2),
			(try_end),
			(try_begin),
				(eq, "$g_mt_mode", 1),
				(val_div, ":value_2", 2),
			(try_end),
			(val_div, ":value_2", 10),
			(try_begin),
				(gt, ":stack_selection_amounts_1", 8),
				(val_mul, ":value_2", 3),
				(assign, ":value_3", ":stack_selection_amounts_1"),
				(convert_to_fixed_point, ":value_3"),
				(store_sqrt, ":value_3", ":value_3"),
				(convert_to_fixed_point, ":value_2"),
				(val_div, ":value_2", ":value_3"),
			(try_end),
			(store_mul, ":value_4", ":value_2", ":value"),
			(val_div, ":value_4", 10),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(store_add, ":value_5", ":stack_selection_amounts_relations_begin", 2),
			(try_for_range, ":localvariable", 2, ":value_5"),
				(troop_get_slot, ":stack_selection_amounts_localvariable", "trp_stack_selection_amounts", ":localvariable"),
				(troop_get_slot, ":stack_selection_ids_localvariable", "trp_stack_selection_ids", ":localvariable"),
				(assign, ":value_6", ":num_companion_stacks_main_party"),
				(try_for_range, ":localvariable_2", 0, ":value_6"),
					(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable_2", "p_main_party", ":localvariable_2"),
					(eq, ":party_stack_troop_id_main_party_localvariable_2", ":stack_selection_ids_localvariable"),
					(assign, ":value_6", 0),
					(call_script, "script_cf_training_ground_sub_routine_for_training_result", ":stack_selection_ids_localvariable", ":localvariable_2", ":stack_selection_amounts_localvariable", ":value_4"),
					(str_store_troop_name_by_count, 1, ":stack_selection_ids_localvariable", ":stack_selection_amounts_localvariable"),
					(assign, reg1, ":stack_selection_amounts_localvariable"),
					(str_store_string, 2, "@{s2}^{reg1} {s1} earned {reg0} experience."),
				(try_end),
			(try_end),
			(try_begin),
				(eq, "$g_mt_mode", 1),
				(store_mul, ":value_7", ":value_2", 3),
				(val_div, ":value_7", 2),
				(try_for_range, ":globalvariable", 0, "$g_training_ground_training_num_enemies"),
					(troop_get_slot, ":stack_selection_ids_localvariable", "trp_temp_array_a", ":globalvariable"),
					(assign, ":value_6", ":num_companion_stacks_main_party"),
					(try_for_range, ":localvariable_2", 0, ":value_6"),
						(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable_2", "p_main_party", ":localvariable_2"),
						(eq, ":party_stack_troop_id_main_party_localvariable_2", ":stack_selection_ids_localvariable"),
						(assign, ":value_6", 0),
						(call_script, "script_cf_training_ground_sub_routine_for_training_result", ":stack_selection_ids_localvariable", ":localvariable_2", 1, ":value_7"),
						(str_store_troop_name, 1, ":stack_selection_ids_localvariable"),
						(str_store_string, 2, "@{s2}^{s1} earned an additional {reg0} experience."),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":value_2"),
				(str_store_string, 2, "@^You earned {reg0} experience.{s2}"),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$g_training_ground_training_success_ratio", 0),
			(str_store_string, 7, "@The training didn't go well at all."),
		(else_try),
			(lt, "$g_training_ground_training_success_ratio", 25),
			(str_store_string, 7, "@The training didn't go well at all."),
		(else_try),
			(lt, "$g_training_ground_training_success_ratio", 50),
			(str_store_string, 7, "@The training didn't go very well."),
		(else_try),
			(lt, "$g_training_ground_training_success_ratio", 75),
			(str_store_string, 7, "@The training went quite well."),
		(else_try),
			(lt, "$g_training_ground_training_success_ratio", 99),
			(str_store_string, 7, "@The training went very well."),
		(else_try),
			(str_store_string, 7, "@The training went perfectly."),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_training_ground")
		], ".")
	]
	),

	("marshall_selection_candidate_ask", 0, "{s15} will soon select a new marshall for {s23}. Some of the lords have suggested your name as a likely candidate.",
"none",
	[
		(try_begin),
			(eq, "$g_presentation_marshall_selection_ended", 1),
			(change_screen_return),
		(try_end),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 15, ":players_kingdom_leader"),
		(str_store_faction_name, 23, "$players_kingdom")
	],
	[
		("marshall_candidate_accept",
		[],
		"Let {s15} learn that you are willing to serve as marshall.",
		[
			(start_presentation, "prsnt_marshall_selection")
		], "."),

		("marshall_candidate_reject",
		[],
		"Tell everyone that you are too busy these days.",
		[
			(try_begin),
				(eq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
				(assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
				(assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
			(else_try),
				(assign, "$g_presentation_marshall_selection_max_renown_1", "$g_presentation_marshall_selection_max_renown_2"),
				(assign, "$g_presentation_marshall_selection_max_renown_1_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
				(assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
				(assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
			(try_end),
			(start_presentation, "prsnt_marshall_selection")
		], ".")
	]
	),

	("captivity_avoid_wilderness", 0, "Suddenly all the world goes black around you. Many hours later you regain your conciousness and find yourself at the spot you fell. Your enemies must have taken you up for dead and left you there. However, it seems that none of your wound were lethal, and altough you feel awful, you find out that can still walk. You get up and try to look for any other survivors from your party.",
"none",
	[],
	[]
	),

	("captivity_start_wilderness", 0, "Stub",
"none",
	[
		(assign, "$g_player_is_captive", 1),
		(try_begin),
			(eq, "$g_player_surrenders", 1),
			(jump_to_menu, "mnu_captivity_start_wilderness_surrender"),
		(else_try),
			(jump_to_menu, "mnu_captivity_start_wilderness_defeat"),
		(try_end)
	],
	[]
	),

	("captivity_start_wilderness_surrender", 0, "Stub",
"none",
	[
		(assign, "$g_player_is_captive", 1),
		(assign, "$auto_menu", -1),
		(assign, "$capturer_party", "$g_encountered_party"),
		(jump_to_menu, "mnu_captivity_wilderness_taken_prisoner")
	],
	[]
	),

	("captivity_start_wilderness_defeat", 0, "Your enemies take you prisoner.",
"none",
	[
		(assign, "$g_player_is_captive", 1),
		(assign, "$auto_menu", -1),
		(assign, "$capturer_party", "$g_encountered_party"),
		(try_begin),
			(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_0", "$g_encountered_party", 0),
			(is_between, ":party_stack_troop_id_g_encountered_party_0", "trp_npc1", "trp_knight_1_1_wife"),
			(troop_slot_eq, ":party_stack_troop_id_g_encountered_party_0", slot_troop_occupation, 2),
			(store_sub, ":value", ":party_stack_troop_id_g_encountered_party_0", "trp_npc1"),
			(set_achievement_stat, 7, ":value", 1),
		(try_end),
		(jump_to_menu, "mnu_captivity_wilderness_taken_prisoner")
	],
	[]
	),

	("captivity_start_castle_surrender", 0, "Stub",
"none",
	[
		(assign, "$g_player_is_captive", 1),
		(assign, "$auto_menu", -1),
		(assign, "$capturer_party", "$g_encountered_party"),
		(jump_to_menu, "mnu_captivity_castle_taken_prisoner")
	],
	[]
	),

	("captivity_start_castle_defeat", 0, "Stub",
"none",
	[
		(assign, "$g_player_is_captive", 1),
		(assign, "$auto_menu", -1),
		(assign, "$capturer_party", "$g_encountered_party"),
		(jump_to_menu, "mnu_captivity_castle_taken_prisoner")
	],
	[]
	),

	("captivity_start_under_siege_defeat", 0, "Your enemies take you prisoner.",
"none",
	[
		(assign, "$g_player_is_captive", 1),
		(assign, "$auto_menu", -1),
		(assign, "$capturer_party", "$g_encountered_party"),
		(jump_to_menu, "mnu_captivity_castle_taken_prisoner")
	],
	[]
	),

	("captivity_wilderness_taken_prisoner", 0, "Your enemies take you prisoner.",
"none",
	[
		(set_background_mesh, "mesh_pic_prisoner_wilderness")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(set_camera_follow_party, "$capturer_party"),
			(assign, "$g_player_is_captive", 1),
			(store_random_in_range, ":random_in_range_18_30", 18, 30),
			(call_script, "script_event_player_captured_as_prisoner"),
			(call_script, "script_stay_captive_for_hours", ":random_in_range_18_30"),
			(assign, "$auto_menu", "mnu_captivity_wilderness_check"),
			(change_screen_return)
		], ".")
	]
	),

	("captivity_wilderness_check", 0, "stub",
"none",
	[
		(jump_to_menu, "mnu_captivity_end_wilderness_escape")
	],
	[]
	),

	("captivity_end_wilderness_escape", 0, "After painful days of being dragged about as a prisoner, you find a chance and escape from your captors!",
"none",
	[
		(play_cue_track, "track_escape"),
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_escape_1_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_escape_1"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_player_is_captive", 0),
			(try_begin),
				(party_is_active, "$capturer_party"),
				(party_relocate_near_party, "p_main_party", "$capturer_party", 2),
			(try_end),
			(call_script, "script_set_parties_around_player_ignore_player", 8, 12),
			(assign, "$g_player_icon_state", 0),
			(set_camera_follow_party, "p_main_party"),
			(rest_for_hours, 0, 0, 0),
			(change_screen_return)
		], ".")
	]
	),

	("captivity_castle_taken_prisoner", 0, "You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the dungeon where you must while away the miserable days of your captivity.",
"none",
	[
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_prisoner_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_prisoner_man"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_player_is_captive", 1),
			(store_random_in_range, ":random_in_range_16_22", 16, 22),
			(call_script, "script_event_player_captured_as_prisoner"),
			(call_script, "script_stay_captive_for_hours", ":random_in_range_16_22"),
			(assign, "$auto_menu", "mnu_captivity_castle_check"),
			(change_screen_return)
		], ".")
	]
	),

	("captivity_rescue_lord_taken_prisoner", 0, "You remain in disguise for as long as possible before revealing yourself. The guards are outraged and beat you savagely before throwing you back into the cell for God knows how long...",
"none",
	[
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_prisoner_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_prisoner_man"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_player_is_captive", 1),
			(store_random_in_range, ":random_in_range_16_22", 16, 22),
			(call_script, "script_event_player_captured_as_prisoner"),
			(call_script, "script_stay_captive_for_hours", ":random_in_range_16_22"),
			(assign, "$auto_menu", "mnu_captivity_castle_check"),
			(change_screen_return)
		], ".")
	]
	),

	("captivity_castle_check", 0, "stub",
"none",
	[
		(store_random_in_range, reg7, 0, 10),
		(try_begin),
			(party_is_active, "$capturer_party"),
			(store_faction_of_party, ":faction_of_party_capturer_party", "$capturer_party"),
			(is_between, ":faction_of_party_capturer_party", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(store_relation, ":relation_faction_of_party_capturer_party_player_faction", ":faction_of_party_capturer_party", "fac_player_faction"),
			(ge, ":relation_faction_of_party_capturer_party_player_faction", 0),
			(jump_to_menu, "mnu_captivity_end_exchanged_with_prisoner"),
		(else_try),
			(lt, reg7, 4),
			(store_character_level, ":character_level_player", "trp_player"),
			(store_mul, "$player_ransom_amount", ":character_level_player", 50),
			(val_add, "$player_ransom_amount", 100),
			(store_troop_gold, reg3, "trp_player"),
			(store_div, ":value", reg3, 20),
			(val_add, "$player_ransom_amount", ":value"),
			(gt, reg3, "$player_ransom_amount"),
			(jump_to_menu, "mnu_captivity_end_propose_ransom"),
		(else_try),
			(lt, reg7, 7),
			(jump_to_menu, "mnu_captivity_end_exchanged_with_prisoner"),
		(else_try),
			(jump_to_menu, "mnu_captivity_castle_remain"),
		(try_end)
	],
	[]
	),

	("captivity_end_exchanged_with_prisoner", 0, "After days of imprisonment, you are finally set free when your captors exchange you with another prisoner.",
"none",
	[
		(play_cue_track, "track_escape")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_player_is_captive", 0),
			(try_begin),
				(party_is_active, "$capturer_party"),
				(party_relocate_near_party, "p_main_party", "$capturer_party", 2),
			(try_end),
			(call_script, "script_set_parties_around_player_ignore_player", 8, 12),
			(assign, "$g_player_icon_state", 0),
			(set_camera_follow_party, "p_main_party"),
			(rest_for_hours, 0, 0, 0),
			(change_screen_return)
		], ".")
	]
	),

	("captivity_end_propose_ransom", 0, "You spend long hours in the sunless dank of the dungeon, more than you can count. Suddenly one of your captors enters your cell with an offer; he proposes to free you in return for {reg5} florins of your hidden wealth. You decide to...",
"none",
	[
		(assign, reg5, "$player_ransom_amount")
	],
	[
		("captivity_end_ransom_accept",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", "$player_ransom_amount")
		],
		"Accept the offer.",
		[
			(play_cue_track, "track_escape"),
			(assign, "$g_player_is_captive", 0),
			(troop_remove_gold, "trp_player", "$player_ransom_amount"),
			(try_begin),
				(party_is_active, "$capturer_party"),
				(party_relocate_near_party, "p_main_party", "$capturer_party", 1),
			(try_end),
			(call_script, "script_set_parties_around_player_ignore_player", 8, 12),
			(assign, "$g_player_icon_state", 0),
			(set_camera_follow_party, "p_main_party"),
			(rest_for_hours, 0, 0, 0),
			(change_screen_return)
		], "."),

		("captivity_end_ransom_deny",
		[],
		"Refuse him, wait for something better.",
		[
			(assign, "$g_player_is_captive", 1),
			(store_random_in_range, reg8, 16, 22),
			(call_script, "script_stay_captive_for_hours", reg8),
			(assign, "$auto_menu", "mnu_captivity_castle_check"),
			(change_screen_return)
		], ".")
	]
	),

	("captivity_castle_remain", 0, "More days pass in the darkness of your cell. You get through them as best you can, enduring the kicks and curses of the guards, watching your underfed body waste away more and more...",
"none",
	[
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_prisoner_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_prisoner_man"),
		(try_end),
		(store_random_in_range, ":random_in_range_16_22", 16, 22),
		(call_script, "script_stay_captive_for_hours", ":random_in_range_16_22"),
		(assign, "$auto_menu", "mnu_captivity_castle_check")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_player_is_captive", 1),
			(change_screen_return)
		], ".")
	]
	),

	("kingdom_army_quest_report_to_army", 0, "{s8} sends word that he wishes you to join {reg4?her:his} new military campaign. You need to bring at least {reg13} troops to the army, and are instructed to raise more men with all due haste if you do not have enough.",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(quest_get_slot, ":report_to_army_target_troop", "qst_report_to_army", slot_quest_target_troop),
		(quest_get_slot, ":report_to_army_target_amount", "qst_report_to_army", slot_quest_target_amount),
		(call_script, "script_get_information_about_troops_position", ":report_to_army_target_troop", 0),
		(str_clear, 9),
		(try_begin),
			(eq, reg0, 1),
			(str_store_string, 9, 1),
		(try_end),
		(str_store_troop_name, 8, ":report_to_army_target_troop"),
		(assign, reg13, ":report_to_army_target_amount"),
		(troop_get_type, reg4, ":report_to_army_target_troop")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(quest_get_slot, ":report_to_army_target_troop", "qst_report_to_army", slot_quest_target_troop),
			(quest_get_slot, ":report_to_army_target_amount", "qst_report_to_army", slot_quest_target_amount),
			(str_store_troop_name_link, 13, ":report_to_army_target_troop"),
			(assign, reg13, ":report_to_army_target_amount"),
			(setup_quest_text, "qst_report_to_army"),
			(str_store_string, 2, "@{s13} asked you to report to him with at least {reg13} troops."),
			(call_script, "script_start_quest", "qst_report_to_army", ":report_to_army_target_troop"),
			(call_script, "script_report_quest_troop_positions", "qst_report_to_army", ":report_to_army_target_troop", 3),
			(change_screen_return)
		], ".")
	]
	),

	("kingdom_army_quest_messenger", 0, "{s8} sends word that he wishes to speak with you about a task he needs performed. He requests you to come and see him as soon as possible.",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
		(str_store_troop_name, 8, ":players_kingdom_marshall")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("kingdom_army_quest_join_siege_order", 0, "{s8} sends word that you are to join the siege of {s9} in preparation for a full assault. Your troops are to take {s9} at all costs.",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
		(quest_get_slot, ":join_siege_with_army_target_center", "qst_join_siege_with_army", slot_quest_target_center),
		(str_store_troop_name, 8, ":players_kingdom_marshall"),
		(str_store_party_name, 9, ":join_siege_with_army_target_center")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(call_script, "script_end_quest", "qst_follow_army"),
			(quest_get_slot, ":join_siege_with_army_target_center", "qst_join_siege_with_army", slot_quest_target_center),
			(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
			(str_store_troop_name_link, 13, ":players_kingdom_marshall"),
			(str_store_party_name_link, 14, ":join_siege_with_army_target_center"),
			(setup_quest_text, "qst_join_siege_with_army"),
			(str_store_string, 2, "@{s13} ordered you to join the assault against {s14}."),
			(call_script, "script_start_quest", "qst_join_siege_with_army", ":players_kingdom_marshall"),
			(change_screen_return)
		], ".")
	]
	),

	("kingdom_army_follow_failed", 0, "You have failed to follow {s8}. The marshal assumes that you were otherwise engaged, but would have appreciated your support.",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
		(str_store_troop_name, 8, ":players_kingdom_marshall"),
		(call_script, "script_abort_quest", "qst_follow_army", 1)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("invite_player_to_faction_without_center", 0, "You receive an offer of vassalage!^^ {s8} of {s9} has sent a royal herald to bring you an invititation in his own hand. You would be granted the honour of becoming a vassal {lord/lady} of {s9}, and in return {s8} asks you to swear an oath of homage to him and fight in his military campaigns, although he offers you no lands or titles. He will surely be offended if you do not take the offer...",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
		(str_store_troop_name, 8, "$g_invite_faction_lord"),
		(str_store_faction_name, 9, "$g_invite_faction")
	],
	[
		("faction_accept",
		[],
		"Accept!",
		[
			(str_store_troop_name, 1, "$g_invite_faction_lord"),
			(setup_quest_text, "qst_join_faction"),
			(str_store_troop_name_link, 3, "$g_invite_faction_lord"),
			(str_store_faction_name_link, 4, "$g_invite_faction"),
			(quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
			(quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
			(quest_set_slot, "qst_join_faction", slot_quest_failure_consequence, 0),
			(str_store_string, 2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
			(call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
			(call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
			(jump_to_menu, "mnu_invite_player_to_faction_accepted")
		], "."),

		("faction_reject",
		[],
		"Decline the invitation.",
		[
			(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
			(call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
			(assign, "$g_invite_faction", 0),
			(assign, "$g_invite_faction_lord", 0),
			(assign, "$g_invite_offered_center", 0),
			(change_screen_return)
		], ".")
	]
	),

	("invite_player_to_faction", 0, "You receive an offer of vassalage!^^ {s8} of {s9} has sent a royal herald to bring you an invititation in his own hand. You would be granted the honour of becoming a vassal {lord/lady} of {s9}, and in return {s8} asks you to swear an oath of homage to him and fight in his military campaigns, offering you the fief of {s2} for your loyal service. He will surely be offended if you do not take the offer...",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
		(str_store_troop_name, 8, "$g_invite_faction_lord"),
		(str_store_faction_name, 9, "$g_invite_faction"),
		(str_store_party_name, 2, "$g_invite_offered_center")
	],
	[
		("faction_accept",
		[],
		"Accept!",
		[
			(str_store_troop_name, 1, "$g_invite_faction_lord"),
			(setup_quest_text, "qst_join_faction"),
			(str_store_troop_name_link, 3, "$g_invite_faction_lord"),
			(str_store_faction_name_link, 4, "$g_invite_faction"),
			(quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
			(quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
			(str_store_string, 2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
			(call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
			(call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
			(jump_to_menu, "mnu_invite_player_to_faction_accepted")
		], "."),

		("faction_reject",
		[],
		"Decline the invitation.",
		[
			(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
			(assign, "$g_invite_faction", 0),
			(assign, "$g_invite_faction_lord", 0),
			(assign, "$g_invite_offered_center", 0),
			(change_screen_return)
		], ".")
	]
	),

	("invite_player_to_faction_accepted", 0, "In order to become a vassal, you must swear an oath of homage to {s3}. You shall have to find him and give him your oath in person. {s5}",
"none",
	[
		(call_script, "script_get_information_about_troops_position", "$g_invite_faction_lord", 0),
		(str_store_troop_name, 3, "$g_invite_faction_lord"),
		(str_store_string, 5, "@{!}{s1}")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("question_peace_offer", 0, "You Receive a Peace Offer^^The {s1} offers you a peace agreement. What is your answer?",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("peace_offer_accept",
		[],
		"Accept",
		[
			(call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
			(change_screen_return)
		], "."),

		("dplmc_peace_offer_terms",
		[],
		"Dictate the peace terms",
		[
			(jump_to_menu, "mnu_dplmc_dictate_terms")
		], "."),

		("peace_offer_reject",
		[],
		"Reject",
		[
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
			(change_screen_return)
		], ".")
	]
	),

	("notification_truce_expired", 0, "Truce Has Expired^^The truce between {s1} and {s2} has expired.",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_feast_quest_expired", 0, "{s10}",
"none",
	[
		(str_store_string, 10, "str_feast_quest_expired")
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_sortie_possible", 0, "Enemy Sighted: Enemies have been sighted outside the walls of {s4}, and {s5} and others are preparing for a sortie. You may join them if you wish.",
"none",
	[
		(str_store_party_name, 4, "$g_notification_menu_var1"),
		(party_stack_get_troop_id, ":party_stack_troop_id_g_notification_menu_var2_0", "$g_notification_menu_var2", 0),
		(str_store_troop_name, 5, ":party_stack_troop_id_g_notification_menu_var2_0")
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_casus_belli_expired", 0, "Kingdom Fails to Respond^^The {s1} has not responded to the {s2}'s provocations, and {s3} suffers a loss of face among {reg4?her:his} more bellicose subjects...^",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(faction_get_slot, ":g_notification_menu_var1_leader", "$g_notification_menu_var1", slot_faction_leader),
		(str_store_troop_name, 3, ":g_notification_menu_var1_leader"),
		(troop_get_type, reg4, ":g_notification_menu_var1_leader"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue",
		[
			(call_script, "script_faction_follows_controversial_policy", "$g_notification_menu_var1", 81),
			(change_screen_return)
		], ".")
	]
	),

	("notification_lord_defects", 0, "Defection: {s4} has abandoned the {s5} and joined the {s7}, taking {reg4?her:his} his fiefs with him",
"none",
	[
		(assign, ":var_1", "$g_notification_menu_var1"),
		(assign, ":var_2", "$g_notification_menu_var2"),
		(str_store_troop_name, 4, ":var_1"),
		(str_store_faction_name, 5, ":var_2"),
		(store_faction_of_troop, ":faction_of_troop_var_1", ":var_1"),
		(str_store_faction_name, 7, ":faction_of_troop_var_1"),
		(troop_get_type, reg4, ":var_1")
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_treason_indictment", 0, "Treason Indictment^^{s9}",
"none",
	[
		(assign, ":var_1", "$g_notification_menu_var1"),
		(assign, ":var_2", "$g_notification_menu_var2"),
		(faction_get_slot, ":var_2_leader", ":var_2", slot_faction_leader),
		(try_begin),
			(eq, ":var_1", "trp_player"),
			(str_store_troop_name, 7, ":var_2_leader"),
			(str_store_string, 9, "str_you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life"),
		(else_try),
			(str_store_troop_name, 4, ":var_1"),
			(str_store_faction_name, 5, ":var_2"),
			(str_store_troop_name, 6, ":var_2_leader"),
			(troop_get_type, reg4, ":var_1"),
			(store_faction_of_troop, ":faction_of_troop_var_1", ":var_1"),
			(try_begin),
				(is_between, ":faction_of_troop_var_1", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(str_store_faction_name, 10, ":faction_of_troop_var_1"),
				(str_store_string, 11, "str_with_the_s10"),
			(else_try),
				(str_store_string, 11, "str_outside_calradia"),
			(try_end),
			(str_store_string, 9, "str_by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_border_incident", 0, "Border incident^^Word reaches you that {s9}. Though you don't know whether or not the rumors are true, you do know one thing -- this seemingly minor incident has raised passions among the {s4}, making it easier for them to go to war against the {s3}, if they want it...",
"none",
	[
		(assign, ":var_1", "$g_notification_menu_var1"),
		(assign, ":var_2", "$g_notification_menu_var2"),
		(store_faction_of_party, ":faction_of_party_var_1", ":var_1"),
		(try_begin),
			(eq, ":var_2", -1),
			(party_get_slot, ":var_1_center_original_faction", ":var_1", slot_center_original_faction),
			(try_begin),
				(this_or_next|eq, ":var_1_center_original_faction", ":faction_of_party_var_1"),
				(neg|faction_slot_eq, ":var_1_center_original_faction", slot_faction_state, 0),
				(party_get_slot, ":var_1_center_original_faction", ":var_1", slot_center_ex_faction),
			(try_end),
			(str_store_party_name, 1, ":var_1"),
			(str_store_faction_name, 3, ":faction_of_party_var_1"),
			(str_store_faction_name, 4, ":var_1_center_original_faction"),
			(faction_get_slot, ":var_1_center_original_faction_leader", ":var_1_center_original_faction", slot_faction_leader),
			(str_store_troop_name, 5, ":var_1_center_original_faction_leader"),
			(str_store_string, 9, "str_local_notables_from_s1_a_village_claimed_by_the_s4_have_been_mistreated_by_their_overlords_from_the_s3_and_petition_s5_for_protection"),
			(display_log_message, "@There has been an alleged border incident: {s9}"),
			(call_script, "script_add_log_entry", 75, ":var_1", -1, -1, ":faction_of_party_var_1"),
		(else_try),
			(store_faction_of_party, ":var_1_center_original_faction", ":var_2"),
			(str_store_party_name, 1, ":var_1"),
			(str_store_party_name, 2, ":var_2"),
			(store_random_in_range, ":random_in_range_0_3", 0, 3),
			(try_begin),
				(eq, ":random_in_range_0_3", 0),
				(str_store_string, 9, "str_villagers_from_s1_stole_some_cattle_from_s2"),
				(display_log_message, "@There has been an alleged border incident: {s9}"),
				(call_script, "script_add_log_entry", 72, ":var_1", ":var_2", -1, ":faction_of_party_var_1"),
			(else_try),
				(eq, ":random_in_range_0_3", 1),
				(str_store_string, 9, "str_villagers_from_s1_abducted_a_woman_from_a_prominent_family_in_s2_to_marry_one_of_their_boys"),
				(display_log_message, "@There has been an alleged border incident: {s9}"),
				(call_script, "script_add_log_entry", 73, ":var_1", ":var_2", -1, ":faction_of_party_var_1"),
			(else_try),
				(eq, ":random_in_range_0_3", 2),
				(str_store_string, 9, "str_villagers_from_s1_killed_some_farmers_from_s2_in_a_fight_over_the_diversion_of_a_stream"),
				(display_log_message, "@There has been an alleged border incident: {s9}"),
				(call_script, "script_add_log_entry", 74, ":var_1", ":var_2", -1, ":faction_of_party_var_1"),
			(try_end),
		(try_end),
		(str_store_faction_name, 3, ":faction_of_party_var_1"),
		(str_store_faction_name, 4, ":var_1_center_original_faction"),
		(store_add, ":value", ":faction_of_party_var_1", 170),
		(val_sub, ":value", "fac_player_supporters_faction"),
		(faction_set_slot, ":var_1_center_original_faction", ":value", 30)
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_faction_active", 0, "You now possess land in your name, without being tied to any kingdom. This makes you a monarch in your own right, with your court temporarily located at {s12}. However, the other kings in Europe will at first consider you a threat, for if any upstart warlord can grab a throne, then their own legitimacy is called into question.^^You may find it desirable at this time to pledge yourself to an existing kingdom. If you want to continue as a sovereign monarch, then your first priority should be to establish an independent right to rule. You can establish your right to rule through several means -- marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions.^^At any rate, your first step should be to appoint a chief minister from among your companions, to handle affairs of state. Different companions have different capabilities.^You may appoint new ministers from time to time. You may also change the location of your court, by speaking to the minister.  Don't forget to change your kingdom's religion through your minister.",
"none",
	[
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", 0),
		(unlock_achievement, 52),
		(play_track, "track_coronation"),
		(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
			(lt, "$g_player_court", "p_town_1_1"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(eq, ":faction_of_party_party", "fac_player_supporters_faction"),
			(assign, "$g_player_court", ":party"),
			(party_get_slot, ":g_player_court_center_original_faction", "$g_player_court", slot_center_original_faction),
			(assign, "$g_player_culture", ":g_player_court_center_original_faction"),
			(try_begin),
				(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
				(is_between, ":player_spouse", "trp_knight_1_1_wife", "trp_heroes_end"),
				(troop_set_slot, ":player_spouse", slot_troop_cur_center, "$g_player_court"),
			(try_end),
			(str_store_party_name, 12, "$g_player_court"),
		(try_end)
	],
	[
		("appoint_spouse",
		[
			(troop_slot_ge, "trp_player", 30, 1),
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(neg|troop_slot_eq, ":player_spouse", slot_troop_occupation, 2),
			(str_store_troop_name, 10, ":player_spouse")
		],
		"Appoint your wife, {s10}...",
		[
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(assign, "$g_player_minister", ":player_spouse"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc1",
		[
			(main_party_has_troop, "trp_npc1"),
			(str_store_troop_name, 10, "trp_npc1")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc1"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc2",
		[
			(main_party_has_troop, "trp_npc2"),
			(str_store_troop_name, 10, "trp_npc2")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc2"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc3",
		[
			(main_party_has_troop, "trp_npc3"),
			(str_store_troop_name, 10, "trp_npc3")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc3"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc4",
		[
			(main_party_has_troop, "trp_npc4"),
			(str_store_troop_name, 10, "trp_npc4")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc4"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc5",
		[
			(main_party_has_troop, "trp_npc5"),
			(str_store_troop_name, 10, "trp_npc5")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc5"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc6",
		[
			(main_party_has_troop, "trp_npc6"),
			(str_store_troop_name, 10, "trp_npc6")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc6"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc7",
		[
			(main_party_has_troop, "trp_npc7"),
			(str_store_troop_name, 10, "trp_npc7")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc7"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc8",
		[
			(main_party_has_troop, "trp_npc8"),
			(str_store_troop_name, 10, "trp_npc8")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc8"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc9",
		[
			(main_party_has_troop, "trp_npc9"),
			(str_store_troop_name, 10, "trp_npc9")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc9"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc10",
		[
			(main_party_has_troop, "trp_npc10"),
			(str_store_troop_name, 10, "trp_npc10")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc10"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc11",
		[
			(main_party_has_troop, "trp_npc11"),
			(str_store_troop_name, 10, "trp_npc11")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc11"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc12",
		[
			(main_party_has_troop, "trp_npc12"),
			(str_store_troop_name, 10, "trp_npc12")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc12"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc13",
		[
			(main_party_has_troop, "trp_npc13"),
			(str_store_troop_name, 10, "trp_npc13")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc13"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc14",
		[
			(main_party_has_troop, "trp_npc14"),
			(str_store_troop_name, 10, "trp_npc14")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc14"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc15",
		[
			(main_party_has_troop, "trp_npc15"),
			(str_store_troop_name, 10, "trp_npc15")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc15"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc16",
		[
			(main_party_has_troop, "trp_npc16"),
			(str_store_troop_name, 10, "trp_npc16")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc16"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc17",
		[
			(main_party_has_troop, "trp_npc17"),
			(str_store_troop_name, 10, "trp_npc17")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc17"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc18",
		[
			(main_party_has_troop, "trp_npc18"),
			(str_store_troop_name, 10, "trp_npc18")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc18"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc20",
		[
			(main_party_has_troop, "trp_npc20"),
			(str_store_troop_name, 10, "trp_npc20")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc20"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc21",
		[
			(main_party_has_troop, "trp_npc21"),
			(str_store_troop_name, 10, "trp_npc21")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc21"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc22",
		[
			(main_party_has_troop, "trp_npc22"),
			(str_store_troop_name, 10, "trp_npc22")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc22"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc23",
		[
			(main_party_has_troop, "trp_npc23"),
			(str_store_troop_name, 10, "trp_npc23")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc23"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc24",
		[
			(main_party_has_troop, "trp_npc24"),
			(str_store_troop_name, 10, "trp_npc24")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc24"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc25",
		[
			(main_party_has_troop, "trp_npc25"),
			(str_store_troop_name, 10, "trp_npc25")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc25"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_npc26",
		[
			(main_party_has_troop, "trp_npc26"),
			(str_store_troop_name, 10, "trp_npc26")
		],
		"Appoint {s10}",
		[
			(assign, "$g_player_minister", "trp_npc26"),
			(jump_to_menu, "mnu_minister_confirm")
		], "."),

		("appoint_default",
		[],
		"Appoint a prominent citizen from the area...",
		[
			(assign, "$g_player_minister", "trp_temporary_minister"),
			(troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
			(jump_to_menu, "mnu_minister_confirm")
		], ".")
	]
	),

	("minister_confirm", 0, "{s9}can be found at your court in {s12}. You should consult periodically, to avoid the accumulation of unresolved issues that may sap your authority...",
"none",
	[
		(try_begin),
			(eq, "$players_kingdom_name_set", 1),
			(change_screen_return),
		(try_end),
		(try_begin),
			(eq, "$g_player_minister", "trp_temporary_minister"),
			(str_store_string, 9, "str_your_new_minister_"),
		(else_try),
			(str_store_troop_name, 10, "$g_player_minister"),
			(str_store_string, 9, "str_s10_is_your_new_minister_and_"),
		(try_end),
		(try_begin),
			(main_party_has_troop, "$g_player_minister"),
			(remove_member_from_party, "$g_player_minister", "p_main_party"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(start_presentation, "prsnt_name_kingdom")
		], ".")
	]
	),

	("notification_court_lost", 0, "{s12}",
"none",
	[
		(try_begin),
			(is_between, "$g_player_court", "p_town_1_1", "p_salt_mine"),
			(str_store_party_name, 10, "$g_player_court"),
			(str_store_party_name, 11, "$g_player_court"),
		(else_try),
			(str_store_string, 10, "str_your_previous_court_some_time_ago"),
			(str_store_string, 11, "str_your_previous_court_some_time_ago"),
		(try_end),
		(assign, "$g_player_court", -1),
		(str_store_string, 14, "str_after_to_the_fall_of_s11_your_court_has_nowhere_to_go"),
		(try_begin),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, 2),
			(str_store_string, 14, "str_as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court"),
		(try_end),
		(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
			(eq, "$g_player_court", -1),
			(neg|party_slot_eq, ":party", slot_village_infested_by_bandits, "trp_peasant_woman"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(eq, ":faction_of_party_party", "fac_player_supporters_faction"),
			(neg|party_slot_ge, ":party", 7, "trp_npc1"),
			(assign, "$g_player_court", ":party"),
			(try_begin),
				(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
				(is_between, ":player_spouse", "trp_knight_1_1_wife", "trp_heroes_end"),
				(troop_set_slot, ":player_spouse", slot_troop_cur_center, "$g_player_court"),
				(str_store_party_name, 11, "$g_player_court"),
			(try_end),
			(str_store_string, 14, "str_due_to_the_fall_of_s10_your_court_has_been_relocated_to_s12"),
		(try_end),
		(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
			(eq, "$g_player_court", -1),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(eq, ":faction_of_party_party", "fac_player_supporters_faction"),
			(assign, "$g_player_court", ":party"),
			(try_begin),
				(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
				(is_between, ":player_spouse", "trp_knight_1_1_wife", "trp_heroes_end"),
				(troop_set_slot, ":player_spouse", slot_troop_cur_center, "$g_player_court"),
			(try_end),
			(party_get_slot, ":party_town_lord", ":party", slot_town_lord),
			(str_store_party_name, 11, "$g_player_court"),
			(str_store_troop_name, 9, ":party_town_lord"),
			(str_store_string, 14, "str_after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_"),
		(try_end),
		(try_begin),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, 2),
			(str_store_string, 14, "str_as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court"),
		(try_end),
		(str_store_string, 12, 14)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_faction_deactive", 0, "Your kingdom no longer holds any land.",
"none",
	[
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
			(try_end),
			(assign, "$g_player_minister", -1),
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_wedding_day", 0, "{s8} wishes to inform you that preparations for your wedding at {s10} have been complete, and that your presence is expected imminently .",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(str_store_troop_name, 8, "$g_notification_menu_var1"),
		(str_store_party_name, 10, "$g_notification_menu_var2")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_kingdom_holds_feast", 0, "{s11}",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(str_store_troop_name, 8, "$g_notification_menu_var1"),
		(store_faction_of_troop, ":faction_of_troop_g_notification_menu_var1", "$g_notification_menu_var1"),
		(str_store_faction_name, 9, ":faction_of_troop_g_notification_menu_var1"),
		(str_store_party_name, 10, "$g_notification_menu_var2"),
		(str_clear, 12),
		(try_begin),
			(check_quest_active, "qst_wed_betrothed"),
			(quest_get_slot, ":wed_betrothed_giver_troop", "qst_wed_betrothed", slot_quest_giver_troop),
			(store_faction_of_troop, ":faction_of_troop_wed_betrothed_giver_troop", ":wed_betrothed_giver_troop"),
			(eq, ":faction_of_troop_wed_betrothed_giver_troop", "$players_kingdom"),
			(str_store_string, 12, "str_feast_wedding_opportunity"),
		(try_end),
		(str_store_string, 11, "str_s8_wishes_to_inform_you_that_the_lords_of_s9_will_be_gathering_for_a_feast_at_his_great_hall_in_s10_and_invites_you_to_be_part_of_this_august_assembly"),
		(try_begin),
			(eq, "$g_notification_menu_var1", 0),
			(str_store_string, 11, "str_the_great_lords_of_your_kingdom_plan_to_gather_at_your_hall_in_s10_for_a_feast"),
		(try_end),
		(str_store_string, 11, "@{!}{s11}{s12}"),
		(try_begin),
			(ge, "$cheat_mode", 1),
			(store_current_hours, ":current_hours"),
			(faction_get_slot, ":players_kingdom_last_feast_concluded", "$players_kingdom", slot_faction_last_feast_concluded),
			(val_sub, ":current_hours", ":players_kingdom_last_feast_concluded"),
			(assign, reg4, ":current_hours"),
			(display_message, "@{!}DEBUG -- Hours since last feast started: {reg4}"),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_center_under_siege", 0, "{s1} has been besieged by {s2} of {s3}!",
"none",
	[
		(str_store_party_name, 1, "$g_notification_menu_var1"),
		(str_store_troop_name, 2, "$g_notification_menu_var2"),
		(store_faction_of_troop, ":faction_of_troop_g_notification_menu_var2", "$g_notification_menu_var2"),
		(str_store_faction_name, 3, ":faction_of_troop_g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 62),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_village_raided", 0, "Enemies have Laid Waste to a Fief^^{s1} has been raided by {s2} of {s3}!",
"none",
	[
		(str_store_party_name, 1, "$g_notification_menu_var1"),
		(str_store_troop_name, 2, "$g_notification_menu_var2"),
		(store_faction_of_troop, ":faction_of_troop_g_notification_menu_var2", "$g_notification_menu_var2"),
		(str_store_faction_name, 3, ":faction_of_troop_g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 62),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_village_raid_started", 0, "Your Village is under Attack!^^{s2} of {s3} is laying waste to {s1}.",
"none",
	[
		(str_store_party_name, 1, "$g_notification_menu_var1"),
		(str_store_troop_name, 2, "$g_notification_menu_var2"),
		(store_faction_of_troop, ":faction_of_troop_g_notification_menu_var2", "$g_notification_menu_var2"),
		(str_store_faction_name, 3, ":faction_of_troop_g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 62),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_one_faction_left", 0, "Europe Conquered by One Kingdom^^{s1} has defeated all rivals and stands as the sole kingdom.",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(try_begin),
			(is_between, "$g_notification_menu_var1", "fac_kingdom_1", "fac_kingdoms_end"),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", 0),
		(else_try),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0),
		(try_end),
		(try_begin),
			(faction_slot_eq, "$g_notification_menu_var1", slot_faction_leader, "trp_player"),
			(unlock_achievement, 44),
		(else_try),
			(unlock_achievement, 53),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_oath_renounced_faction_defeated", 0, "Your Old Faction was Defeated^^You won the battle against {s1}! This ends your struggle which started after you renounced your oath to them.",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(try_begin),
			(is_between, "$g_notification_menu_var1", "fac_kingdom_1", "fac_kingdoms_end"),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", 0),
		(else_try),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_center_lost", 0, "An Estate was Lost^^You have lost {s1} to {s2}.",
"none",
	[
		(str_store_party_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 62),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_troop_left_players_faction", 0, "Betrayal!^^{s1} has left {s2} and joined {s3}.",
"none",
	[
		(str_store_troop_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$players_kingdom"),
		(str_store_faction_name, 3, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 55),
		(position_set_y, 0, 20),
		(position_set_z, 0, 100),
		(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_troop_joined_players_faction", 0, "Good news!^^ {s1} has left {s2} and joined {s3}.",
"none",
	[
		(str_store_troop_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(str_store_faction_name, 3, "$players_kingdom"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 55),
		(position_set_y, 0, 20),
		(position_set_z, 0, 100),
		(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_war_declared", 0, "Declaration of War^^{s1} has declared war against {s2}!",
"none",
	[
		(try_begin),
			(str_store_faction_name, 1, "$g_notification_menu_var1"),
			(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(try_end),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(store_sub, ":value", "$g_notification_menu_var1", "fac_player_supporters_faction"),
		(store_sub, ":value_2", "$g_notification_menu_var2", "fac_player_supporters_faction"),
		(val_mul, ":value", 128),
		(val_add, ":value", ":value_2"),
		(set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":value", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_peace_declared", 0, "Peace Agreement^^{s1} and {s2} have made peace!^{s57}",
"none",
	[
		(try_begin),
			(eq, 1, 0),
			(eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
			(assign, "$g_include_diplo_explanation", 0),
		(else_try),
			(str_clear, 57),
		(try_end),
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(store_sub, ":value", "$g_notification_menu_var1", "fac_player_supporters_faction"),
		(store_sub, ":value_2", "$g_notification_menu_var2", "fac_player_supporters_faction"),
		(val_mul, ":value", 128),
		(val_add, ":value", ":value_2"),
		(set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":value", 0)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_faction_defeated", 0, "Faction Eliminated^^{s1} is no more!",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(try_begin),
			(is_between, "$g_notification_menu_var1", "fac_kingdom_1", "fac_kingdoms_end"),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", 0),
		(else_try),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(is_between, "$supported_pretender", "trp_kingdom_4_pretender", "trp_knight_1_1_wife"),
				(troop_slot_eq, "$supported_pretender", slot_troop_original_faction, "$g_notification_menu_var1"),
				(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
					(troop_slot_eq, ":troop", slot_troop_occupation, 2),
					(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
					(eq, ":faction_of_troop_troop", "fac_player_supporters_faction"),
					(troop_set_faction, ":troop", "$g_notification_menu_var1"),
					(call_script, "script_troop_set_title_according_to_faction", ":troop", "$g_notification_menu_var1"),
					(try_begin),
						(this_or_next|eq, "$g_notification_menu_var1", "$players_kingdom"),
						(eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
						(call_script, "script_check_concilio_calradi_achievement"),
					(try_end),
				(else_try),
					(troop_slot_eq, ":troop", slot_troop_occupation, 2),
					(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
					(eq, ":faction_of_troop_troop", "$g_notification_menu_var1"),
					(call_script, "script_troop_change_relation_with_troop", ":troop", "trp_player", 5),
				(try_end),
				(try_for_parties, ":var_3"),
					(store_faction_of_party, ":faction_of_troop_troop", ":var_3"),
					(eq, ":faction_of_troop_troop", "fac_player_supporters_faction"),
					(party_set_faction, ":var_3", "$g_notification_menu_var1"),
				(try_end),
				(assign, "$players_kingdom", "$g_notification_menu_var1"),
				(try_begin),
					(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
					(is_between, ":player_spouse", "trp_knight_1_1_wife", "trp_heroes_end"),
					(troop_set_faction, ":player_spouse", "$g_notification_menu_var1"),
				(try_end),
				(call_script, "script_add_notification_menu", "mnu_notification_rebels_switched_to_faction", "$g_notification_menu_var1", "$supported_pretender"),
				(faction_set_slot, "$g_notification_menu_var1", slot_faction_state, 0),
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, 2),
				(faction_get_slot, ":g_notification_menu_var1_leader", "$g_notification_menu_var1", slot_faction_leader),
				(troop_set_slot, ":g_notification_menu_var1_leader", slot_troop_change_to_faction, "fac_commoners"),
				(faction_set_slot, "$g_notification_menu_var1", slot_faction_leader, "$supported_pretender"),
				(troop_set_faction, "$supported_pretender", "$g_notification_menu_var1"),
				(faction_get_slot, ":g_notification_menu_var1_marshall", "$g_notification_menu_var1", slot_faction_marshall),
				(try_begin),
					(ge, ":g_notification_menu_var1_marshall", 0),
					(troop_get_slot, ":g_notification_menu_var1_marshall_leaded_party", ":g_notification_menu_var1_marshall", slot_troop_leaded_party),
					(party_is_active, ":g_notification_menu_var1_marshall_leaded_party"),
					(party_set_marshall, ":g_notification_menu_var1_marshall_leaded_party", 0),
				(try_end),
				(faction_set_slot, "$g_notification_menu_var1", slot_faction_marshall, "trp_player"),
				(faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_state, 0),
				(faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_object, -1),
				(troop_set_slot, "$supported_pretender", slot_troop_occupation, 2),
				(troop_set_slot, "$supported_pretender", slot_troop_renown, 1000),
				(party_remove_members, "p_main_party", "$supported_pretender", 1),
				(call_script, "script_set_player_relation_with_faction", "$g_notification_menu_var1", 0),
				(try_for_range, ":faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(faction_slot_eq, ":faction", slot_faction_state, 0),
					(neq, ":faction", "$g_notification_menu_var1"),
					(store_relation, ":relation_faction_player_supporters_faction", ":faction", "fac_player_supporters_faction"),
					(set_relation, ":faction", "$g_notification_menu_var1", ":relation_faction_player_supporters_faction"),
				(try_end),
				(assign, "$supported_pretender", 0),
				(assign, "$supported_pretender_old_faction", 0),
				(assign, "$g_recalculate_ais", 1),
				(call_script, "script_update_all_notes"),
			(try_end),
			(change_screen_return)
		], ".")
	]
	),

	("notification_rebels_switched_to_faction", 0, "Rebellion Success^^ Your rebellion is victorious! Your faction now has the sole claim to the title of {s11}, with {s12} as the single ruler.",
"none",
	[
		(str_store_faction_name, 11, "$g_notification_menu_var1"),
		(str_store_troop_name, 12, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(try_begin),
			(is_between, "$g_notification_menu_var1", "fac_kingdom_1", "fac_kingdoms_end"),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", 0),
		(else_try),
			(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$talk_context", 15),
			(start_map_conversation, "$g_notification_menu_var2", -1),
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_should_consult", 0, "Your minister send words that there are problems brewing in the realm which, if left untreated, could sap your authority. You should consult with him at your earliest convenience",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(setup_quest_text, "qst_consult_with_minister"),
			(str_store_troop_name, 11, "$g_player_minister"),
			(str_store_party_name, 12, "$g_player_court"),
			(str_store_string, 2, "str_consult_with_s11_at_your_court_in_s12"),
			(call_script, "script_start_quest", "qst_consult_with_minister", -1),
			(quest_set_slot, "qst_consult_with_minister", slot_quest_expiration_days, 30),
			(quest_set_slot, "qst_consult_with_minister", slot_quest_giver_troop, "$g_player_minister"),
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_feast_in_progress", 0, "Feast in Preparation^^Your wife has started preparations for a feast in your hall in {s11}",
"none",
	[
		(str_store_party_name, 11, "$g_notification_menu_var1")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_lady_requests_visit", 0, "An elderly woman approaches your party and passes one of your men a letter, sealed in plain wax. It is addressed to you. When you break the seal, you see it is from {s15}. It reads, 'I so enjoyed your last visit. {s14} I am currently in {s10}.{s12}'",
"none",
	[
		(assign, ":var_1", "$g_notification_menu_var1"),
		(assign, ":var_2", "$g_notification_menu_var2"),
		(str_store_troop_name, 15, ":var_1"),
		(str_store_party_name, 10, ":var_2"),
		(store_current_hours, ":current_hours"),
		(troop_get_slot, ":var_1_last_talk_time", ":var_1", slot_troop_last_talk_time),
		(val_sub, ":current_hours", ":var_1_last_talk_time"),
		(call_script, "script_get_kingdom_lady_social_determinants", ":var_1"),
		(assign, ":var_5", reg0),
		(str_store_troop_name, 16, ":var_5"),
		(call_script, "script_troop_get_family_relation_to_troop", ":var_5", ":var_1"),
		(str_clear, 14),
		(try_begin),
			(lt, ":current_hours", 336),
			(try_begin),
				(troop_slot_eq, ":var_1", slot_lord_reputation_type, 23),
				(str_store_string, 14, "str_as_brief_as_our_separation_has_been_the_longing_in_my_heart_to_see_you_has_made_it_seem_as_many_years"),
			(else_try),
				(str_store_string, 14, "str_although_it_has_only_been_a_short_time_since_your_departure_but_i_would_be_most_pleased_to_see_you_again"),
			(try_end),
		(else_try),
			(ge, ":current_hours", 336),
			(try_begin),
				(troop_slot_eq, ":var_1", slot_lord_reputation_type, 24),
				(str_store_string, 14, "str_although_i_have_received_no_word_from_you_for_quite_some_time_i_am_sure_that_you_must_have_been_very_busy_and_that_your_failure_to_come_see_me_in_no_way_indicates_that_your_attentions_to_me_were_insincere_"),
			(else_try),
				(troop_slot_eq, ":var_1", slot_lord_reputation_type, 25),
				(str_store_string, 14, "str_i_trust_that_you_have_comported_yourself_in_a_manner_becoming_a_gentleman_during_our_long_separation_"),
			(else_try),
				(str_store_string, 14, "str_it_has_been_many_days_since_you_came_and_i_would_very_much_like_to_see_you_again"),
			(try_end),
		(try_end),
		(str_clear, 12),
		(str_clear, 18),
		(try_begin),
			(troop_slot_eq, ":var_5", slot_troop_love_interests_end, 0),
			(str_store_string, 12, "str__you_should_ask_my_s11_s16s_permission_but_i_have_no_reason_to_believe_that_he_will_prevent_you_from_coming_to_see_me"),
			(str_store_string, 18, "str__you_should_first_ask_her_s11_s16s_permission"),
		(else_try),
			(troop_slot_eq, ":var_5", slot_troop_love_interests_end, -1),
			(str_store_string, 12, "str__alas_as_we_know_my_s11_s16_will_not_permit_me_to_see_you_however_i_believe_that_i_can_arrange_away_for_you_to_enter_undetected"),
		(else_try),
			(troop_slot_eq, ":var_5", slot_troop_love_interests_end, 1),
			(str_store_string, 12, "str__as_my_s11_s16_has_already_granted_permission_for_you_to_see_me_i_shall_expect_your_imminent_arrival"),
		(try_end)
	],
	[
		("continue",
		[],
		"Tell the woman to inform her mistress that you will come shortly",
		[
			(assign, ":var_1", "$g_notification_menu_var1"),
			(str_store_troop_name_link, 3, ":var_1"),
			(str_store_party_name_link, 4, "$g_notification_menu_var2"),
			(str_store_string, 2, "str_visit_s3_who_was_last_at_s4s18"),
			(call_script, "script_start_quest", "qst_visit_lady", ":var_1"),
			(quest_set_slot, "qst_visit_lady", slot_quest_giver_troop, ":var_1"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(quest_get_slot, ":visit_lady_giver_troop", "qst_visit_lady", slot_quest_giver_troop),
				(str_store_troop_name, 2, ":visit_lady_giver_troop"),
				(display_message, "str_giver_troop_=_s2"),
			(try_end),
			(quest_set_slot, "qst_visit_lady", slot_quest_expiration_days, 30),
			(change_screen_return)
		], "."),

		("continue",
		[],
		"Tell the woman to inform her mistress that you are indisposed",
		[
			(troop_set_slot, "$g_notification_menu_var1", slot_troop_love_interest_3, 1),
			(change_screen_return)
		], ".")
	]
	),

	("garden", 0, "{s12}",
"none",
	[
		(call_script, "script_get_kingdom_lady_social_determinants", "$love_interest_in_town"),
		(assign, ":var_1", reg0),
		(str_store_troop_name, 11, "$love_interest_in_town"),
		(try_begin),
			(call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", ":var_1", "trp_player"),
			(lt, reg0, 0),
			(troop_set_slot, ":var_1", slot_troop_love_interests_end, -1),
		(try_end),
		(assign, "$nurse_assists_entry", 0),
		(try_begin),
			(troop_slot_eq, ":var_1", slot_troop_love_interests_end, 1),
			(str_store_string, 12, "str_the_guards_at_the_gate_have_been_ordered_to_allow_you_through_you_might_be_imagining_things_but_you_think_one_of_them_may_have_given_you_a_wink"),
		(else_try),
			(call_script, "script_troop_get_relation_with_troop", "trp_player", "$love_interest_in_town"),
			(gt, reg0, 0),
			(assign, ":value", 0),
			(try_begin),
				(check_quest_active, "qst_visit_lady"),
				(quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, "$love_interest_in_town"),
				(assign, ":value", 1),
			(else_try),
				(check_quest_active, "qst_formal_marriage_proposal"),
				(quest_slot_eq, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$love_interest_in_town"),
				(this_or_next|check_quest_succeeded, "qst_formal_marriage_proposal"),
				(check_quest_failed, "qst_formal_marriage_proposal"),
				(assign, ":value", 1),
			(else_try),
				(check_quest_active, "qst_duel_courtship_rival"),
				(quest_slot_eq, "qst_duel_courtship_rival", slot_quest_giver_troop, "$love_interest_in_town"),
				(this_or_next|check_quest_succeeded, "qst_duel_courtship_rival"),
				(check_quest_failed, "qst_duel_courtship_rival"),
				(assign, ":value", 1),
			(try_end),
			(try_begin),
				(store_current_hours, ":current_hours"),
				(troop_get_slot, ":love_interest_in_town_last_talk_time", "$love_interest_in_town", slot_troop_last_talk_time),
				(val_sub, ":current_hours", ":love_interest_in_town_last_talk_time"),
				(this_or_next|ge, ":current_hours", 96),
				(eq, ":value", 1),
				(try_begin),
					(is_between, "$g_encountered_party", "p_town_1_1", "p_castle_1_1"),
					(str_store_string, 12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_don_this_dress_and_throw_the_hood_over_your_face_i_will_smuggle_you_inside_the_castle_to_meet_her_in_the_guise_of_a_skullery_maid__the_guards_will_not_look_too_carefully_but_i_beg_you_for_all_of_our_sakes_be_discrete"),
					(assign, "$nurse_assists_entry", 1),
				(else_try),
					(str_store_string, 12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_wait_for_a_while_by_the_spring_outside_the_walls_i_will_smuggle_her_ladyship_out_to_meet_you_dressed_in_the_guise_of_a_shepherdess_but_i_beg_you_for_all_of_our_sakes_be_discrete"),
					(assign, "$nurse_assists_entry", 2),
				(try_end),
			(else_try),
				(str_store_string, 12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_her_ladyship_asks_me_to_say_that_yearns_to_see_you_but_that_you_should_bide_your_time_a_bit_her_ladyship_says_that_to_arrange_a_clandestine_meeting_so_soon_after_your_last_encounter_would_be_too_dangerous"),
			(try_end),
		(else_try),
			(str_store_string, 12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter"),
		(try_end)
	],
	[
		("enter",
		[
			(call_script, "script_get_kingdom_lady_social_determinants", "$love_interest_in_town"),
			(troop_slot_eq, reg0, slot_troop_love_interests_end, 1)
		],
		"Enter",
		[
			(jump_to_menu, "mnu_town"),
			(call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party")
		], "."),

		("nurse",
		[
			(eq, "$nurse_assists_entry", 1)
		],
		"Go with the nurse",
		[
			(jump_to_menu, "mnu_town"),
			(call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party")
		], "."),

		("nurse",
		[
			(eq, "$nurse_assists_entry", 2)
		],
		"Wait by the spring",
		[
			(jump_to_menu, "mnu_town"),
			(call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party")
		], "."),

		("leave",
		[],
		"Leave",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("kill_local_merchant_begin", 0, "You spot your victim and follow him, observing as he turns a corner into a dark alley. This will surely be your best opportunity to attack him.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(set_jump_mission, "mt_back_alley_kill_local_merchant"),
			(party_get_slot, ":qst_kill_local_merchant_center_town_alley", "$qst_kill_local_merchant_center", slot_town_alley),
			(modify_visitors_at_site, ":qst_kill_local_merchant_center_town_alley"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_local_merchant"),
			(jump_to_menu, "mnu_town"),
			(jump_to_scene, ":qst_kill_local_merchant_center_town_alley"),
			(change_screen_mission)
		], ".")
	]
	),

	("debug_alert_from_s65", 0, "DEBUG ALERT: {s65}",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$debug_message_in_queue", 0),
			(change_screen_return)
		], ".")
	]
	),

	("auto_return_to_map", 0, "stub",
"none",
	[
		(change_screen_map)
	],
	[]
	),

	("bandit_lair", 0, "{s3}",
"none",
	[
		(try_begin),
			(eq, "$loot_screen_shown", 1),
			(try_for_range, ":partytemplate", "pt_steppe_bandits", "pt_deserters"),
				(party_template_slot_eq, ":partytemplate", slot_party_template_lair_party, "$g_encountered_party"),
				(party_template_set_slot, ":partytemplate", slot_party_template_lair_party, 0),
			(try_end),
			(try_begin),
				(ge, "$g_encountered_party", 0),
				(party_is_active, "$g_encountered_party"),
				(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
				(neq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(remove_party, "$g_encountered_party"),
			(try_end),
			(assign, "$g_leave_encounter", 0),
			(change_screen_return),
		(else_try),
			(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_0", "$g_encountered_party", 0),
			(str_store_troop_name_plural, 4, ":party_stack_troop_id_g_encountered_party_0"),
			(str_store_string, 5, "str_bandit_approach_defile"),
			(try_begin),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_desert_bandit"),
				(str_store_string, 5, "str_bandit_approach_defile"),
			(else_try),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_mountain_bandit"),
				(str_store_string, 5, "str_bandit_approach_cliffs"),
			(else_try),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_forest_bandit"),
				(str_store_string, 5, "str_bandit_approach_swamp"),
			(else_try),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_taiga_bandit"),
				(str_store_string, 5, "str_bandit_approach_swamp"),
			(else_try),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_steppe_bandit"),
				(str_store_string, 5, "str_bandit_approach_thickets"),
			(else_try),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_sea_raider"),
				(str_store_string, 5, "str_bandit_approach_cove"),
			(else_try),
				(eq, ":party_stack_troop_id_g_encountered_party_0", "trp_raider"),
				(str_store_string, 5, "str_bandit_approach_cove"),
			(try_end),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0),
				(str_store_string, 3, "str_bandit_hideout_preattack"),
			(else_try),
				(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
				(eq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1),
				(str_store_string, 3, "str_lost_startup_hideout_attack"),
			(else_try),
				(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1),
				(str_store_string, 3, "str_bandit_hideout_failure"),
			(else_try),
				(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2),
				(str_store_string, 3, "str_bandit_hideout_success"),
			(try_end),
		(try_end)
	],
	[
		("continue_1",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0)
		],
		"Attack the hideout...",
		[
			(party_set_slot, "$g_encountered_party", slot_party_ai_substate, 1),
			(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
			(assign, "$g_enemy_party", "$g_encountered_party"),
			(try_begin),
				(eq, ":template_id_l_g_encountered_party", "pt_sea_raider_lair"),
				(assign, ":value", "trp_sea_raider"),
				(assign, ":value_2", "scn_lair_sea_raiders"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_forest_bandit_lair"),
				(assign, ":value", "trp_forest_bandit"),
				(assign, ":value_2", "scn_lair_forest_bandits"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_desert_bandit_lair"),
				(assign, ":value", "trp_desert_bandit"),
				(assign, ":value_2", "scn_lair_desert_bandits"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_mountain_bandit_lair"),
				(assign, ":value", "trp_mountain_bandit"),
				(assign, ":value_2", "scn_lair_mountain_bandits"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_taiga_bandit_lair"),
				(assign, ":value", "trp_taiga_bandit"),
				(assign, ":value_2", "scn_lair_taiga_bandits"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_steppe_bandit_lair"),
				(assign, ":value", "trp_steppe_bandit"),
				(assign, ":value_2", "scn_lair_steppe_bandits"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_robber_knight_lair"),
				(assign, ":value", "trp_raider"),
				(assign, ":value_2", "scn_lair_sea_raiders"),
			(else_try),
				(eq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(assign, ":value", "trp_looter"),
				(store_faction_of_party, ":faction_of_party_g_starting_town", "$g_starting_town"),
				(try_begin),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_5"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_6"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_7"),
					(eq, ":faction_of_party_g_starting_town", "fac_kingdom_1"),
					(assign, ":value_2", "scn_lair_forest_bandits"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_8"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_15"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_29"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_30"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_33"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_34"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_35"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_36"),
					(eq, ":faction_of_party_g_starting_town", "fac_kingdom_2"),
					(assign, ":value_2", "scn_lair_taiga_bandits"),
				(else_try),
					(eq, ":faction_of_party_g_starting_town", "fac_kingdom_3"),
					(assign, ":value_2", "scn_lair_steppe_bandits"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_11"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_14"),
					(eq, ":faction_of_party_g_starting_town", "fac_kingdom_4"),
					(assign, ":value_2", "scn_lair_sea_raiders"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_9"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_37"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_10"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_12"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_13"),
					(eq, ":faction_of_party_g_starting_town", "fac_kingdom_5"),
					(assign, ":value_2", "scn_lair_mountain_bandits"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_16"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_17"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_18"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_19"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_papacy"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_22"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_23"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_24"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_25"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_26"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_27"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_28"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_31"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_32"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_38"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_39"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_40"),
					(this_or_next|eq, ":faction_of_party_g_starting_town", "fac_kingdom_41"),
					(eq, ":faction_of_party_g_starting_town", "fac_kingdom_20"),
					(assign, ":value_2", "scn_lair_desert_bandits"),
				(try_end),
			(try_end),
			(modify_visitors_at_site, ":value_2"),
			(reset_visitors),
			(store_character_level, ":character_level_player", "trp_player"),
			(store_add, ":value_3", 5, ":character_level_player"),
			(val_div, ":value_3", 3),
			(try_for_range, ":unused", 0, ":value_3"),
				(store_random_in_range, ":random_in_range_2_11", 2, 11),
				(set_visitor, ":random_in_range_2_11", ":value", 1),
			(try_end),
			(party_clear, "p_temp_casualties"),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			(assign, "$g_battle_result", 0),
			(set_jump_mission, "mt_bandit_lair"),
			(jump_to_scene, ":value_2"),
			(change_screen_mission)
		], "."),

		("leave_no_attack",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0)
		],
		"Leave...",
		[
			(change_screen_return)
		], "."),

		("leave_victory",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2)
		],
		"Continue...",
		[
			(try_for_range, ":partytemplate", "pt_steppe_bandits", "pt_deserters"),
				(party_template_slot_eq, ":partytemplate", slot_party_template_lair_party, "$g_encountered_party"),
				(party_template_set_slot, ":partytemplate", slot_party_template_lair_party, 0),
			(try_end),
			(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
			(try_begin),
				(neq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(check_quest_active, "qst_destroy_bandit_lair"),
				(quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
				(call_script, "script_succeed_quest", "qst_destroy_bandit_lair"),
			(try_end),
			(assign, "$g_leave_encounter", 0),
			(change_screen_return),
			(try_begin),
				(eq, "$loot_screen_shown", 0),
				(assign, "$loot_screen_shown", 1),
				(troop_clear_inventory, "trp_temp_troop"),
				(party_get_num_companion_stacks, ":num_companion_stacks_temp_casualties", "p_temp_casualties"),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_temp_casualties"),
					(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
					(try_begin),
						(party_stack_get_size, ":party_stack_size_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
						(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
						(gt, ":party_stack_size_temp_casualties_localvariable", 0),
						(party_add_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_casualties_localvariable", ":party_stack_size_temp_casualties_localvariable"),
						(party_stack_get_num_wounded, ":party_stack_num_wounded_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
						(gt, ":party_stack_num_wounded_temp_casualties_localvariable", 0),
						(party_wound_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_casualties_localvariable", ":party_stack_num_wounded_temp_casualties_localvariable"),
					(try_end),
				(try_end),
				(call_script, "script_party_calculate_loot", "p_total_enemy_casualties"),
				(gt, reg0, 0),
				(troop_sort_inventory, "trp_temp_troop"),
				(assign, ":var_8", 0),
				(party_get_num_companion_stacks, ":num_companion_stacks_temp_casualties", "p_main_party"),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_temp_casualties"),
					(party_stack_get_troop_id, ":party_stack_troop_id_temp_casualties_localvariable", "p_main_party", ":localvariable"),
					(is_between, ":party_stack_troop_id_temp_casualties_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
					(val_add, ":var_8", 1),
				(try_end),
				(try_begin),
					(gt, ":var_8", 0),
					(assign, "$return_menu", "mnu_bandit_lair"),
					(jump_to_menu, "mnu_manage_loot_pool"),
				(else_try),
					(change_screen_loot, "trp_temp_troop"),
				(try_end),
			(try_end),
			(try_begin),
				(ge, "$g_encountered_party", 0),
				(party_is_active, "$g_encountered_party"),
				(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
				(eq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(remove_party, "$g_encountered_party"),
			(try_end)
		], "."),

		("leave_defeat",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1)
		],
		"Continue...",
		[
			(try_for_range, ":partytemplate", "pt_steppe_bandits", "pt_deserters"),
				(party_template_slot_eq, ":partytemplate", slot_party_template_lair_party, "$g_encountered_party"),
				(party_template_set_slot, ":partytemplate", slot_party_template_lair_party, 0),
			(try_end),
			(try_begin),
				(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
				(neq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(check_quest_active, "qst_destroy_bandit_lair"),
				(quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
				(call_script, "script_fail_quest", "qst_destroy_bandit_lair"),
			(try_end),
			(try_begin),
				(ge, "$g_encountered_party", 0),
				(party_is_active, "$g_encountered_party"),
				(party_get_template_id, ":template_id_l_g_encountered_party", "$g_encountered_party"),
				(neq, ":template_id_l_g_encountered_party", "pt_looter_lair"),
				(remove_party, "$g_encountered_party"),
			(try_end),
			(assign, "$g_leave_encounter", 0),
			(try_begin),
				(party_is_active, "$g_encountered_party"),
				(party_set_slot, "$g_encountered_party", slot_party_ai_substate, 0),
			(try_end),
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_faction_political_issue_resolved", 0, "After consulting with the peers of the realm, {s10} has decided to confer {s11} on {s12}.",
"none",
	[
		(assign, ":var_1", "$g_notification_menu_var1"),
		(assign, ":var_2", "$g_notification_menu_var2"),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 10, ":players_kingdom_leader"),
		(try_begin),
			(eq, ":var_1", 1),
			(str_store_string, 11, "str_the_marshalship"),
		(else_try),
			(str_store_party_name, 11, ":var_1"),
		(try_end),
		(str_store_troop_name, 12, ":var_2")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("notification_player_faction_political_issue_resolved_for_player", 0, "After consulting with the peers of the realm, {s10} has decided to confer {s11} on you. You may decline the honor, but it will probably mean that you will not receive other awards for a little while.{s12}",
"none",
	[
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 10, ":players_kingdom_leader"),
		(faction_get_slot, ":players_kingdom_political_issue", "$players_kingdom", slot_faction_political_issue),
		(try_begin),
			(eq, ":players_kingdom_political_issue", 1),
			(str_store_string, 11, "str_the_marshalship"),
			(str_store_string, 12, "@^^Note that so long as you remain marshal, the lords of the realm will be expecting you to lead them on campaign. So, if you are awaiting a feast, either for a wedding or for other purposes, you may wish to resign the marshalship by speaking to your liege."),
		(else_try),
			(str_clear, 12),
			(str_store_party_name, 11, ":players_kingdom_political_issue"),
		(try_end)
	],
	[
		("accept",
		[],
		"Accept the honor",
		[
			(faction_get_slot, ":players_kingdom_political_issue", "$players_kingdom", slot_faction_political_issue),
			(try_begin),
				(eq, ":players_kingdom_political_issue", 1),
				(call_script, "script_check_and_finish_active_army_quests_for_faction", "$players_kingdom"),
				(call_script, "script_appoint_faction_marshall", "$players_kingdom", "trp_player"),
				(unlock_achievement, 41),
			(else_try),
				(call_script, "script_give_center_to_lord", ":players_kingdom_political_issue", "trp_player", 0),
			(try_end),
			(faction_set_slot, "$players_kingdom", slot_faction_political_issue, 0),
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$players_kingdom"),
				(troop_set_slot, ":troop", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(change_screen_return)
		], "."),

		("decline",
		[],
		"Decline the honor",
		[
			(faction_get_slot, ":players_kingdom_political_issue", "$players_kingdom", slot_faction_political_issue),
			(try_begin),
				(is_between, ":players_kingdom_political_issue", "p_town_1_1", "p_salt_mine"),
				(assign, "$g_dont_give_fief_to_player_days", 30),
			(else_try),
				(assign, "$g_dont_give_marshalship_to_player_days", 30),
			(try_end),
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$players_kingdom"),
				(troop_set_slot, ":troop", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(change_screen_return)
		], ".")
	]
	),

	("start_phase_2_5", 0, "{!}{s16}",
"none",
	[
		(str_store_party_name, 1, "$g_starting_town"),
		(str_store_string, 16, "@You came by caravan through the heartland of Europe. Green shoots of wheat, barley and oats are beginning to push through the dark soil of the rolling hills, and on the lower slopes of the snowcapped mountains, herds of cattle and sheep are grazing on the spring grass. Occasionally, too, you catch sight of one of the great warhorses that are the pride of the European nobility. The land here is rich -- but also troubled, as the occasional burnt-out farm bears witness. You keep a wide berth of the forests, where desperate men have taken refuge, and it is some relief when you crest a ridge and catch sight of the great city of {s1}, its rooftops made golden by the last rays of the setting sun.")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_start_phase_3")
		], ".")
	]
	),

	("start_phase_3", 0, "{s16}^^You are exhausted by the time you find the inn in {s1}, you get drunk and fall asleep under the table. However, you awake before dawn and are eager to explore your surroundings. You venture out onto the streets, which are still deserted. You continue out of the town to begin your adventure.",
"none",
	[
		(assign, ":value", 1),
		(try_begin),
			(eq, "$current_startup_quest_phase", 1),
			(try_begin),
				(eq, "$g_killed_first_bandit", 1),
				(str_store_string, 11, "str_killed_bandit_at_alley_fight"),
			(else_try),
				(str_store_string, 11, "str_wounded_by_bandit_at_alley_fight"),
			(try_end),
			(jump_to_menu, "mnu_start_phase_4"),
			(assign, ":value", 0),
		(else_try),
			(eq, "$current_startup_quest_phase", 3),
			(try_begin),
				(eq, "$g_killed_first_bandit", 1),
				(str_store_string, 11, "str_killed_bandit_at_alley_fight"),
			(else_try),
				(str_store_string, 11, "str_wounded_by_bandit_at_alley_fight"),
			(try_end),
			(jump_to_menu, "mnu_start_phase_4"),
			(assign, ":value", 0),
		(try_end),
		(str_store_party_name, 1, "$g_starting_town"),
		(str_clear, 16),
		(eq, ":value", 1)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$g_starting_town", -1),
			(call_script, "script_player_arrived"),
			(party_set_morale, "p_main_party", 100),
			(set_encountered_party, "$current_town"),
			(party_get_position, 2, "$current_town"),
			(map_get_land_position_around_position, 1, 2, 1),
			(party_set_position, "p_main_party", 1),
			(change_screen_map)
		], ".")
	]
	),

	("start_phase_4", 0, "{s11}",
"none",
	[
		(assign, ":value", 1),
		(try_begin),
			(eq, "$current_startup_quest_phase", 2),
			(change_screen_return),
			(assign, ":value", 0),
		(else_try),
			(eq, "$current_startup_quest_phase", 3),
			(str_store_string, 11, "str_merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern"),
		(else_try),
			(eq, "$current_startup_quest_phase", 4),
			(try_begin),
				(eq, "$g_killed_first_bandit", 1),
				(str_store_string, 11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits"),
			(else_try),
				(str_store_string, 11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded"),
			(try_end),
		(try_end),
		(eq, ":value", 1)
	],
	[
		("continue",
		[
			(this_or_next|eq, "$current_startup_quest_phase", 1),
			(eq, "$current_startup_quest_phase", 4)
		],
		"Continue...",
		[
			(assign, "$town_entered", 1),
			(try_begin),
				(eq, "$current_town", "p_town_5_1"),
				(assign, ":value", "trp_merchant_kingdom_5"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_14_1"),
				(assign, ":value", "trp_merchant_kingdom_14"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_11_2"),
				(assign, ":value", "trp_merchant_kingdom_11"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_12_1"),
				(assign, ":value", "trp_merchant_kingdom_12"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_4_1"),
				(assign, ":value", "trp_merchant_kingdom_4"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_10_1"),
				(assign, ":value", "trp_merchant_kingdom_10"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_13_2"),
				(assign, ":value", "trp_merchant_kingdom_13"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_9_1"),
				(assign, ":value", "trp_merchant_kingdom_9"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_2_1"),
				(assign, ":value", "trp_merchant_kingdom_2"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_1_1"),
				(assign, ":value", "trp_merchant_kingdom_1"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_6_1"),
				(assign, ":value", "trp_merchant_kingdom_6"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_8_1"),
				(assign, ":value", "trp_merchant_kingdom_8"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_7_1"),
				(assign, ":value", "trp_merchant_kingdom_7"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(eq, "$current_town", "p_town_3_1"),
				(assign, ":value", "trp_merchant_kingdom_3"),
				(assign, ":value_2", "scn_town_1_room"),
			(else_try),
				(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
				(try_begin),
					(eq, ":faction_of_party_current_town", "fac_kingdom_1"),
					(assign, ":value", "trp_merchant_kingdom_1"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_33"),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_34"),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_35"),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_36"),
					(eq, ":faction_of_party_current_town", "fac_kingdom_2"),
					(assign, ":value", "trp_merchant_kingdom_2"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_3"),
					(assign, ":value", "trp_merchant_kingdom_3"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_4"),
					(assign, ":value", "trp_merchant_kingdom_4"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_5"),
					(assign, ":value", "trp_merchant_kingdom_5"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_42"),
					(eq, ":faction_of_party_current_town", "fac_kingdom_6"),
					(assign, ":value", "trp_merchant_kingdom_6"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_7"),
					(assign, ":value", "trp_merchant_kingdom_7"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_15"),
					(eq, ":faction_of_party_current_town", "fac_kingdom_8"),
					(assign, ":value", "trp_merchant_kingdom_8"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_9"),
					(assign, ":value", "trp_merchant_kingdom_9"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_10"),
					(assign, ":value", "trp_merchant_kingdom_10"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_11"),
					(assign, ":value", "trp_merchant_kingdom_11"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_12"),
					(assign, ":value", "trp_merchant_kingdom_12"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_13"),
					(assign, ":value", "trp_merchant_kingdom_13"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_14"),
					(assign, ":value", "trp_merchant_kingdom_14"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_15"),
					(assign, ":value", "trp_merchant_kingdom_15"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_16"),
					(assign, ":value", "trp_merchant_kingdom_16"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_17"),
					(assign, ":value", "trp_merchant_kingdom_17"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_18"),
					(assign, ":value", "trp_merchant_kingdom_18"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_19"),
					(assign, ":value", "trp_merchant_kingdom_19"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_20"),
					(assign, ":value", "trp_merchant_kingdom_20"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_papacy"),
					(assign, ":value", "trp_merchant_kingdom_21"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_22"),
					(assign, ":value", "trp_merchant_kingdom_22"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_23"),
					(assign, ":value", "trp_merchant_kingdom_23"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_24"),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_38"),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_39"),
					(this_or_next|eq, ":faction_of_party_current_town", "fac_kingdom_40"),
					(eq, ":faction_of_party_current_town", "fac_kingdom_41"),
					(assign, ":value", "trp_merchant_kingdom_24"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_25"),
					(assign, ":value", "trp_merchant_kingdom_25"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_26"),
					(assign, ":value", "trp_merchant_kingdom_26"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_27"),
					(assign, ":value", "trp_merchant_kingdom_27"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_28"),
					(assign, ":value", "trp_merchant_kingdom_28"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_29"),
					(assign, ":value", "trp_merchant_kingdom_29"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_30"),
					(assign, ":value", "trp_merchant_kingdom_30"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_31"),
					(assign, ":value", "trp_merchant_kingdom_31"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_32"),
					(assign, ":value", "trp_merchant_kingdom_32"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(eq, ":faction_of_party_current_town", "fac_kingdom_37"),
					(assign, ":value", "trp_merchant_kingdom_37"),
					(assign, ":value_2", "scn_town_1_room"),
				(else_try),
					(display_message, "@unknown faction in module game menus start phase 4!"),
				(try_end),
			(try_end),
			(modify_visitors_at_site, ":value_2"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 9, ":value"),
			(assign, "$talk_context", 21),
			(assign, "$dialog_with_merchant_ended", 0),
			(set_jump_mission, "mt_meeting_merchant"),
			(jump_to_scene, ":value_2"),
			(change_screen_mission)
		], "."),

		("continue",
		[
			(eq, "$current_startup_quest_phase", 3)
		],
		"Continue...",
		[
			(call_script, "script_prepare_town_to_fight")
		], ".")
	]
	),

	("lost_tavern_duel", 0, "{s11}",
"none",
	[
		(try_begin),
			(agent_get_troop_id, ":troop_id_l_g_main_attacker_agent", "$g_main_attacker_agent"),
			(eq, ":troop_id_l_g_main_attacker_agent", "trp_belligerent_drunk"),
			(str_store_string, 11, "str_lost_tavern_duel_ordinary"),
		(else_try),
			(agent_get_troop_id, ":troop_id_l_g_main_attacker_agent", "$g_main_attacker_agent"),
			(eq, ":troop_id_l_g_main_attacker_agent", "trp_hired_assassin"),
			(str_store_string, 11, "str_lost_tavern_duel_assassin"),
		(try_end),
		(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("establish_court", 0, "To establish {s4} as your court will require a small refurbishment. In particular, you will need a set of tools and a bolt of velvet. it may also take a short while for some of your followers to relocate here. Do you wish to proceed?",
"none",
	[
		(str_store_party_name, 4, "$g_encountered_party")
	],
	[
		("establish",
		[
			(player_has_item, "itm_tools"),
			(player_has_item, "itm_velvet")
		],
		"Establish {s4} as your court",
		[
			(assign, "$g_player_court", "$current_town"),
			(troop_remove_item, "trp_player", "itm_tools"),
			(troop_remove_item, "trp_player", "itm_velvet"),
			(party_get_slot, ":g_player_court_center_original_faction", "$g_player_court", slot_center_original_faction),
			(assign, "$g_player_culture", ":g_player_court_center_original_faction"),
			(jump_to_menu, "mnu_town")
		], "."),

		("continue",
		[],
		"Hold off...",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("notification_relieved_as_marshal", 0, "{s4} wishes to inform you that your services as marshal are no longer required. In honor of valiant efforts on behalf of the realm over the last {reg4} days, however, {reg8?she:he} offers you a purse of {reg5} florins.",
"none",
	[
		(assign, reg4, "$g_player_days_as_marshal"),
		(store_div, ":value", "$g_player_days_as_marshal", 4),
		(val_min, ":value", 20),
		(store_mul, ":value_2", "$g_player_days_as_marshal", 50),
		(val_max, ":value_2", 200),
		(val_min, ":value_2", 4000),
		(troop_add_gold, "trp_player", ":value_2"),
		(call_script, "script_change_troop_renown", "trp_player", ":value"),
		(assign, "$g_player_days_as_marshal", 0),
		(assign, "$g_dont_give_marshalship_to_player_days", 15),
		(assign, reg5, ":value_2"),
		(faction_get_slot, ":players_kingdom_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, 4, ":players_kingdom_leader"),
		(troop_get_type, reg8, ":players_kingdom_leader")
	],
	[
		("continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("export_import_npcs", 0, "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
"none",
	[
		(assign, reg0, "$g_player_troop"),
		(str_store_troop_name, 0, "$g_player_troop")
	],
	[
		("export_import_back",
		[],
		"Go back",
		[
			(assign, "$g_player_troop", "trp_player"),
			(set_player_troop, "$g_player_troop"),
			(jump_to_menu, "mnu_camp")
		], "."),

		("export_import_npc1",
		[
			(store_add, ":value", "trp_npc1", 0),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 0),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc2",
		[
			(store_add, ":value", "trp_npc1", 1),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 1),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc3",
		[
			(store_add, ":value", "trp_npc1", 2),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 2),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc4",
		[
			(store_add, ":value", "trp_npc1", 3),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 3),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc5",
		[
			(store_add, ":value", "trp_npc1", 4),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 4),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc6",
		[
			(store_add, ":value", "trp_npc1", 5),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 5),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc7",
		[
			(store_add, ":value", "trp_npc1", 6),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 6),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc8",
		[
			(store_add, ":value", "trp_npc1", 7),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 7),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_next",
		[],
		"Next page",
		[
			(jump_to_menu, "mnu_export_import_npcs_2")
		], ".")
	]
	),

	("export_import_npcs_2", 0, "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
"none",
	[
		(assign, reg0, "$g_player_troop"),
		(str_store_troop_name, 0, "$g_player_troop")
	],
	[
		("export_import_prev",
		[],
		"Previous page",
		[
			(jump_to_menu, "mnu_export_import_npcs")
		], "."),

		("export_import_npc9",
		[
			(store_add, ":value", "trp_npc1", 8),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 8),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc10",
		[
			(store_add, ":value", "trp_npc1", 9),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 9),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc11",
		[
			(store_add, ":value", "trp_npc1", 10),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 10),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc12",
		[
			(store_add, ":value", "trp_npc1", 11),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 11),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc13",
		[
			(store_add, ":value", "trp_npc1", 12),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 12),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc14",
		[
			(store_add, ":value", "trp_npc1", 13),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 13),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc15",
		[
			(store_add, ":value", "trp_npc1", 14),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 14),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc16",
		[
			(store_add, ":value", "trp_npc1", 15),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 15),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_next",
		[],
		"Next page",
		[
			(jump_to_menu, "mnu_export_import_npcs_3")
		], ".")
	]
	),

	("export_import_npcs_3", 0, "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
"none",
	[
		(assign, reg0, "$g_player_troop"),
		(str_store_troop_name, 0, "$g_player_troop")
	],
	[
		("export_import_prev",
		[],
		"Previous page",
		[
			(jump_to_menu, "mnu_export_import_npcs_2")
		], "."),

		("export_import_npc17",
		[
			(store_add, ":value", "trp_npc1", 16),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 16),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc18",
		[
			(store_add, ":value", "trp_npc1", 17),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 17),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc19",
		[
			(store_add, ":value", "trp_npc1", 18),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 18),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc20",
		[
			(store_add, ":value", "trp_npc1", 19),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 19),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc21",
		[
			(store_add, ":value", "trp_npc1", 20),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 20),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc22",
		[
			(store_add, ":value", "trp_npc1", 21),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 21),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc23",
		[
			(store_add, ":value", "trp_npc1", 22),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 22),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc24",
		[
			(store_add, ":value", "trp_npc1", 23),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 23),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_next",
		[],
		"Next page",
		[
			(jump_to_menu, "mnu_export_import_npcs_4")
		], ".")
	]
	),

	("export_import_npcs_4", 0, "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
"none",
	[
		(assign, reg0, "$g_player_troop"),
		(str_store_troop_name, 0, "$g_player_troop")
	],
	[
		("export_import_prev",
		[],
		"Previous page",
		[
			(jump_to_menu, "mnu_export_import_npcs_3")
		], "."),

		("export_import_npc25",
		[
			(store_add, ":value", "trp_npc1", 24),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 24),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc26",
		[
			(store_add, ":value", "trp_npc1", 25),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 25),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc27",
		[
			(store_add, ":value", "trp_npc1", 26),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 26),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc28",
		[
			(store_add, ":value", "trp_npc1", 27),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 27),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], "."),

		("export_import_npc29",
		[
			(store_add, ":value", "trp_npc1", 28),
			(str_store_troop_name, 0, ":value")
		],
		"{s0}",
		[
			(store_add, ":value", "trp_npc1", 28),
			(assign, "$g_player_troop", ":value"),
			(set_player_troop, "$g_player_troop")
		], ".")
	]
	),

	("pick_nation", 0, "Whom will you serve?",
"none",
	[],
	[
		("serve_noone",
		[],
		"No-one",
		[
			(assign, "$g_start_faction", -1),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("serve_pick",
		[],
		"or select",
		[
			(assign, "$g_start_faction", -1),
			(start_presentation, "prsnt_faction_selection")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "mnu_start_character_4")
		], ".")
	]
	),

	("dplmc_notification_alliance_declared", 0, "Alliance Agreement^^{s1} and {s2} have formed an alliance!^{s57}",
"none",
	[
		(str_clear, 57),
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(store_sub, ":value", "$g_notification_menu_var1", "fac_player_supporters_faction"),
		(store_sub, ":value_2", "$g_notification_menu_var2", "fac_player_supporters_faction"),
		(val_mul, ":value", 128),
		(val_add, ":value", ":value_2"),
		(set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":value", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_defensive_declared", 0, "Defensive Pact^^{s1} and {s2} have agreed to a defensive pact!^{s57}",
"none",
	[
		(str_clear, 57),
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(store_sub, ":value", "$g_notification_menu_var1", "fac_player_supporters_faction"),
		(store_sub, ":value_2", "$g_notification_menu_var2", "fac_player_supporters_faction"),
		(val_mul, ":value", 128),
		(val_add, ":value", ":value_2"),
		(set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":value", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_trade_declared", 0, "Trade Agreement^^{s1} and {s2} have signed a trade agreement!^{s57}",
"none",
	[
		(str_clear, 57),
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(store_sub, ":value", "$g_notification_menu_var1", "fac_player_supporters_faction"),
		(store_sub, ":value_2", "$g_notification_menu_var2", "fac_player_supporters_faction"),
		(val_mul, ":value", 128),
		(val_add, ":value", ":value_2"),
		(set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":value", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_nonaggression_declared", 0, "Non-aggression Treaty^^{s1} and {s2} have concluded a non-aggression treaty!^{s57}",
"none",
	[
		(str_clear, 57),
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(store_sub, ":value", "$g_notification_menu_var1", "fac_player_supporters_faction"),
		(store_sub, ":value_2", "$g_notification_menu_var2", "fac_player_supporters_faction"),
		(val_mul, ":value", 128),
		(val_add, ":value", ":value_2"),
		(set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":value", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_question_alliance_offer", 0, "You Receive an Alliance Offer^^The {s1} wants to form an alliance with you. What is your answer?",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_alliance_offer_accept",
		[],
		"Accept",
		[
			(call_script, "script_dplmc_start_alliance_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
			(change_screen_return)
		], "."),

		("dplmc_alliance_offer_reject",
		[],
		"Reject",
		[
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_question_defensive_offer", 0, "You Receive a Pact Offer^^The {s1} offers you a defensive pact. What is your answer?",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_defensive_offer_accept",
		[],
		"Accept",
		[
			(call_script, "script_dplmc_start_defensive_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
			(change_screen_return)
		], "."),

		("dplmc_defensive_offer_reject",
		[],
		"Reject",
		[
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_question_trade_offer", 0, "You Receive a Pact Offer^^The {s1} offers you a trade pact. What is your answer?",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_trade_offer_accept",
		[],
		"Accept",
		[
			(call_script, "script_dplmc_start_trade_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
			(change_screen_return)
		], "."),

		("dplmc_trade_offer_reject",
		[],
		"Reject",
		[
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_question_nonaggression_offer", 0, "You Receive a Pact Offer^^The {s1} offers you a non-aggression treaty. What is your answer?",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_nonaggression_offer_accept",
		[],
		"Accept",
		[
			(call_script, "script_dplmc_start_nonaggression_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
			(change_screen_return)
		], "."),

		("dplmc_nonaggression_offer_reject",
		[],
		"Reject",
		[
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_alliance_expired", 0, "Alliance Has Expired^^The alliance between {s1} and {s2} has expired and was degraded to a defensive pact.",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_defensive_expired", 0, "Defensive Pact Has Expired^^The defensive pact between {s1} and {s2} has expired and was degraded to a trade agreement.",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_trade_expired", 0, "Trade Agreement Has Expired^^The trade agreement between {s1} and {s2} has expired and was degraded to a non-aggression treaty.",
"none",
	[
		(str_store_faction_name, 1, "$g_notification_menu_var1"),
		(str_store_faction_name, 2, "$g_notification_menu_var2"),
		(set_fixed_point_multiplier, 100),
		(position_set_x, 0, 65),
		(position_set_y, 0, 30),
		(position_set_z, 0, 170),
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_dictate_terms", menu_text_color(0xff000000), "Dictate your peace terms.",
"none",
	[
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_demand_4000",
		[
			(gt, "$g_player_chamberlain", 0)
		],
		"Demand 4000 florins",
		[
			(call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
			(assign, ":var_1", reg0),
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -3),
			(try_begin),
				(le, ":random_in_range_0_4", ":var_1"),
				(call_script, "script_dplmc_pay_into_treasury", 4000),
				(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
				(change_screen_return),
			(else_try),
				(jump_to_menu, "mnu_dplmc_deny_terms"),
			(try_end)
		], "."),

		("dplmc_demand_8000",
		[
			(gt, "$g_player_chamberlain", 0)
		],
		"Demand 8000 florins",
		[
			(call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
			(assign, ":var_1", reg0),
			(val_mul, ":var_1", 2),
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
			(try_begin),
				(le, ":random_in_range_0_10", ":var_1"),
				(call_script, "script_dplmc_pay_into_treasury", 8000),
				(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
				(change_screen_return),
			(else_try),
				(jump_to_menu, "mnu_dplmc_deny_terms"),
			(try_end)
		], "."),

		("dplmc_demand_castle",
		[
			(assign, ":value", 100),
			(assign, "$demanded_castle", -1),
			(try_for_range, ":party", "p_castle_1_1", "p_village_1_1"),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$g_notification_menu_var1"),
				(try_for_range, ":party_2", "p_town_1_1", "p_salt_mine"),
					(store_faction_of_party, ":faction_of_party_party_2", ":party_2"),
					(eq, ":faction_of_party_party_2", "fac_player_supporters_faction"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_party_2_party", ":party_2", ":party"),
					(lt, ":distance_to_party_from_party_party_2_party", ":value"),
					(assign, ":value", ":distance_to_party_from_party_party_2_party"),
					(assign, "$demanded_castle", ":party"),
					(str_store_party_name, 2, ":party"),
				(try_end),
			(try_end),
			(is_between, "$demanded_castle", "p_castle_1_1", "p_village_1_1")
		],
		"Demand {s2}.",
		[
			(call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
			(assign, ":var_1", reg0),
			(val_mul, ":var_1", 2),
			(store_random_in_range, ":random_in_range_0_12", 0, 12),
			(call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -6),
			(try_begin),
				(le, ":random_in_range_0_12", ":var_1"),
				(call_script, "script_give_center_to_faction", "$demanded_castle", "fac_player_supporters_faction"),
				(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
				(change_screen_return),
			(else_try),
				(jump_to_menu, "mnu_dplmc_deny_terms"),
			(try_end)
		], "."),

		("dplmc_go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "mnu_question_peace_offer")
		], ".")
	]
	),

	("dplmc_deny_terms", menu_text_color(0xff000000), "The {s1} refuses your terms and is breaking off of negotiations.",
"none",
	[
		(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", 0)
	],
	[
		("dplmc_continue",
		[],
		"Continue",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_village_riot_result", 0, "{s9}",
"none",
	[
		(try_begin),
			(eq, "$g_battle_result", 1),
			(jump_to_menu, "mnu_dplmc_village_riot_removed"),
		(else_try),
			(set_background_mesh, "mesh_pic_villageriot"),
			(str_store_string, 9, "@Try as you might, you could not defeat the rebelling village."),
		(try_end)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("dplmc_village_riot_removed", 0, "In bloody battle you and your men slaughter the rebels and regain control over the village. But there is not much left you can control.",
"none",
	[
		(set_background_mesh, "mesh_pic_looted_village"),
		(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
		(call_script, "script_village_set_state", "$current_town", 2)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(jump_to_menu, "mnu_village")
		], ".")
	]
	),

	("dplmc_town_riot_removed", 0, "In bloody battle you and your men slaughter the rebels and regain control over the town.",
"none",
	[],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(assign, "$new_encounter", 1),
			(try_begin),
				(party_get_slot, ":g_encountered_party_town_lord", "$g_encountered_party", slot_town_lord),
				(troop_get_slot, ":g_encountered_party_town_lord_banner_scene_prop", ":g_encountered_party_town_lord", slot_troop_banner_scene_prop),
				(gt, ":g_encountered_party_town_lord_banner_scene_prop", 0),
				(val_sub, ":g_encountered_party_town_lord_banner_scene_prop", "spr_banner_a"),
				(val_add, ":g_encountered_party_town_lord_banner_scene_prop", "icon_banner_01"),
				(party_set_banner_icon, "$g_encountered_party", ":g_encountered_party_town_lord_banner_scene_prop"),
			(try_end),
			(jump_to_menu, "mnu_castle_outside")
		], ".")
	]
	),

	("dplmc_riot_negotiate", 0, "You approach the angry crowd and begin negotiations. The leader of the riot demands {reg0} florins. He agrees to lay down arms if you are willing to pay.",
"none",
	[
		(party_get_slot, ":g_encountered_party_center_player_relation", "$g_encountered_party", slot_center_player_relation),
		(val_min, ":g_encountered_party_center_player_relation", 0),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
			(val_sub, ":g_encountered_party_center_player_relation", 75),
			(set_background_mesh, "mesh_pic_townriot"),
		(else_try),
			(val_sub, ":g_encountered_party_center_player_relation", 50),
			(set_background_mesh, "mesh_pic_villageriot"),
		(try_end),
		(store_skill_level, ":skill_level_persuasion_player", "skl_persuasion", "trp_player"),
		(val_add, ":g_encountered_party_center_player_relation", ":skill_level_persuasion_player"),
		(val_mul, ":g_encountered_party_center_player_relation", ":g_encountered_party_center_player_relation"),
		(assign, reg0, ":g_encountered_party_center_player_relation")
	],
	[
		("dplmc_pay_riot_treasury",
		[
			(gt, "$g_player_chamberlain", 0),
			(store_troop_gold, ":troop_gold_household_possessions", "trp_household_possessions"),
			(ge, ":troop_gold_household_possessions", reg0)
		],
		"Induce your chamberlain to pay the money from the treasury.",
		[
			(call_script, "script_dplmc_withdraw_from_treasury", reg0),
			(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(jump_to_menu, "mnu_castle_outside"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("dplmc_pay_riot_cash",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg0)
		],
		"Pay cash.",
		[
			(troop_remove_gold, "trp_player", reg0),
			(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(jump_to_menu, "mnu_castle_outside"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("dplmc_back",
		[],
		"Back...",
		[
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 3),
				(jump_to_menu, "mnu_castle_outside"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], ".")
	]
	),

	("dplmc_notification_riot", 0, "The peasants of {s1} launched a riot against you! In a surprise attack, men loyal to you have been slain. The remainder joined the angry crowd.",
"none",
	[
		(str_store_party_name, 1, "$g_notification_menu_var1"),
		(try_begin),
			(party_slot_eq, "$g_notification_menu_var1", slot_party_type, 3),
			(set_background_mesh, "mesh_pic_townriot"),
		(else_try),
			(set_background_mesh, "mesh_pic_villageriot"),
		(try_end)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_appoint_chamberlain", 0, "As a lord of a fief you can now appoint a chamberlain who resides at you court for a weekly salary of 15 florins. He will handle all financial affairs like collecting and determining taxes, paying wages and managing your estate. In addition he supervises money transfers between kingdoms giving you more diplomatic options.",
"none",
	[],
	[
		("dplmc_appoint_default",
		[],
		"Appoint a prominent nobleman from the area.",
		[
			(assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
			(troop_equip_items, "$g_player_chamberlain"),
			(jump_to_menu, "mnu_dplmc_chamberlain_confirm")
		], "."),

		("dplmc_continue",
		[],
		"Proceed without chamberlain.",
		[
			(assign, "$g_player_chamberlain", -1),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_chamberlain_confirm", 0, "Your chamberlain can be found at your court. You should consult him if you want to give him any financial advice or you need greater amounts of money. You should always make sure that there is enough money in the treasury to pay for political affairs.",
"none",
	[],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_appoint_constable", 0, "As a lord of a fief you can now appoint a constable who resides at you court for a weekly salary of 15 florins. He will recruit new troops and provide information about your army.",
"none",
	[],
	[
		("dplmc_appoint_default",
		[],
		"Appoint a prominent nobleman from the area.",
		[
			(assign, "$g_player_constable", "trp_dplmc_constable"),
			(assign, "$g_constable_training_center", -1),
			(troop_equip_items, "$g_player_constable"),
			(jump_to_menu, "mnu_dplmc_constable_confirm")
		], "."),

		("dplmc_continue",
		[],
		"Proceed without constable.",
		[
			(assign, "$g_player_constable", -1),
			(assign, "$g_constable_training_center", -1),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_constable_confirm", 0, "Your constable can be found at your court. You should consult him if you want to recruit new troops or get detailed informatiom about your standing  army.",
"none",
	[],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_notification_appoint_chancellor", 0, "As a lord of a fief you can now appoint a chancellor who resides at you court for a weekly salary of 20 florins. He will be the keeper of your seal and conduct the correspondence between you and other important persons.",
"none",
	[],
	[
		("dplmc_appoint_default",
		[],
		"Appoint a prominent nobleman from the area.",
		[
			(assign, "$g_player_chancellor", "trp_dplmc_chancellor"),
			(troop_equip_items, "$g_player_chancellor"),
			(jump_to_menu, "mnu_dplmc_chancellor_confirm")
		], "."),

		("dplmc_continue",
		[],
		"Proceed without chancellor.",
		[
			(assign, "$g_player_chancellor", -1),
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_chancellor_confirm", 0, "Your chancellor can be found at your court. You should consult him if you want to send messages or gifts.",
"none",
	[],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_deserters", 0, "Some of your men don't believe that you will pay their wages and desert. Overall you lose: {s11} men.",
"none",
	[
		(set_background_mesh, "mesh_pic_deserters"),
		(store_random_in_range, ":random_in_range_1_g_notification_menu_var1", 1, "$g_notification_menu_var1"),
		(call_script, "script_dplmc_player_troops_leave", ":random_in_range_1_g_notification_menu_var1"),
		(str_store_string, 11, "@{reg0}")
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("dplmc_negotiate_besieger", 0, "You appear with a white flag at the top of the wall. After a while a negotiator of {s11} approaches you. He demands {s6} and all associated villages as well as {reg0} florins for safe conduct.",
"none",
	[
		(party_get_slot, ":current_town_center_is_besieged_by", "$current_town", slot_center_is_besieged_by),
		(party_stack_get_troop_id, ":party_stack_troop_id_current_town_center_is_besieged_by_0", ":current_town_center_is_besieged_by", 0),
		(str_store_troop_name, 11, ":party_stack_troop_id_current_town_center_is_besieged_by_0"),
		(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_current_town_center_is_besieged_by_0", ":party_stack_troop_id_current_town_center_is_besieged_by_0"),
		(assign, ":var_4", 0),
		(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
			(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
			(eq, ":faction_of_troop_troop", ":faction_of_troop_party_stack_troop_id_current_town_center_is_besieged_by_0"),
			(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
			(party_is_active, ":troop_leaded_party"),
			(party_slot_eq, ":troop_leaded_party", slot_party_ai_state, 11),
			(party_slot_eq, ":troop_leaded_party", slot_party_ai_object, ":current_town_center_is_besieged_by"),
			(party_is_active, ":current_town_center_is_besieged_by"),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_leaded_party_current_town_center_is_besieged_by", ":troop_leaded_party", ":current_town_center_is_besieged_by"),
			(lt, ":distance_to_party_from_party_troop_leaded_party_current_town_center_is_besieged_by", 25),
			(party_get_num_companions, ":num_companions_troop_leaded_party", ":troop_leaded_party"),
			(val_add, ":var_4", ":num_companions_troop_leaded_party"),
		(try_end),
		(assign, ":var_10", 0),
		(party_get_num_companion_stacks, ":num_companion_stacks_l_current_town", "$current_town"),
		(try_for_range, ":localvariable", 0, ":num_companion_stacks_l_current_town"),
			(party_stack_get_size, ":party_stack_size_current_town_localvariable", "$current_town", ":localvariable"),
			(val_add, ":var_10", ":party_stack_size_current_town_localvariable"),
		(try_end),
		(val_sub, ":var_4", ":var_10"),
		(store_skill_level, ":skill_level_persuasion_player", "skl_persuasion", "trp_player"),
		(val_mul, ":skill_level_persuasion_player", 10),
		(store_sub, "$diplomacy_var", ":var_4", ":skill_level_persuasion_player"),
		(val_mul, "$diplomacy_var", 4),
		(val_max, "$diplomacy_var", 500),
		(val_div, "$diplomacy_var", 100),
		(val_mul, "$diplomacy_var", 100),
		(assign, reg0, "$diplomacy_var"),
		(str_store_party_name, 6, "$current_town")
	],
	[
		("dplmc_comply_treasury",
		[
			(store_troop_gold, ":troop_gold_household_possessions", "trp_household_possessions"),
			(ge, ":troop_gold_household_possessions", "$diplomacy_var")
		],
		"Comply and induce your chamberlain to pay the money form the treasury.",
		[
			(call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
			(call_script, "script_dplmc_player_center_surrender", "$current_town"),
			(change_screen_return)
		], "."),

		("dplmc_comply",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", "$diplomacy_var")
		],
		"Comply and pay the money cash.",
		[
			(troop_remove_gold, "trp_player", "$diplomacy_var"),
			(call_script, "script_dplmc_player_center_surrender", "$current_town"),
			(change_screen_return)
		], "."),

		("dplmc_break_off",
		[],
		"Break off negotiations.",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("dplmc_messenger", 0, "Sire, I found {s10} and delivered your message. His answer was {s11}.",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(str_store_troop_name, 10, "$g_notification_menu_var1"),
		(try_begin),
			(eq, "$g_notification_menu_var2", 1),
			(str_store_string, 11, "@positive"),
		(else_try),
			(str_store_string, 11, "@negative"),
		(try_end)
	],
	[
		("dplmc_continue",
		[],
		"Continue...",
		[
			(change_screen_return)
		], ".")
	]
	),

	("manage_loot_pool", 0, "{s10}",
"none",
	[
		(assign, "$pool_troop", "trp_temp_troop"),
		(assign, reg20, 0),
		(troop_get_inventory_capacity, ":inventory_capacity_l_pool_troop", "$pool_troop"),
		(try_for_range, ":localvariable", 0, ":inventory_capacity_l_pool_troop"),
			(troop_get_inventory_slot, ":inventory_slot_pool_troop_localvariable", "$pool_troop", ":localvariable"),
			(ge, ":inventory_slot_pool_troop_localvariable", 0),
			(val_add, reg20, 1),
		(try_end),
		(try_begin),
			(eq, reg20, 0),
			(str_store_string, 10, "str_item_pool_no_items"),
			(str_store_string, 20, "str_item_pool_leave"),
		(else_try),
			(eq, reg20, 1),
			(str_store_string, 10, "str_item_pool_one_item"),
			(str_store_string, 20, "str_item_pool_abandon"),
		(else_try),
			(str_store_string, 10, "str_item_pool_many_items"),
			(str_store_string, 20, "str_item_pool_abandon"),
		(try_end)
	],
	[
		("auto_loot",
		[
			(eq, "$inventory_menu_offset", 0),
			(store_free_inventory_capacity, ":free_inventory_capacity_pool_troop", "$pool_troop"),
			(ge, ":free_inventory_capacity_pool_troop", 10)
		],
		"Let your heroes select gear from the item pool.",
		[
			(jump_to_menu, "mnu_auto_loot")
		], "."),

		("auto_loot_no",
		[
			(eq, "$inventory_menu_offset", 0),
			(store_free_inventory_capacity, ":free_inventory_capacity_pool_troop", "$pool_troop"),
			(lt, ":free_inventory_capacity_pool_troop", 10),
			(disable_menu_option)
		],
		"Insufficient item pool space for auto-upgrade.",
		[], "."),

		("loot",
		[],
		"Access the item pool.",
		[
			(change_screen_loot, "$pool_troop")
		], "."),

		("auto_loot_upgrade_management",
		[],
		"Upgrade management of the NPC's equipments.",
		[
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(is_between, ":party_stack_troop_id_main_party_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(assign, "$temp", ":party_stack_troop_id_main_party_localvariable"),
				(assign, ":num_companion_stacks_main_party", 0),
			(try_end),
			(start_presentation, "prsnt_autoloot_upgrade_management")
		], "."),

		("auto_loot_leave_with_nothing",
		[
			(gt, reg20, 0),
			(assign, reg1, "$g_price_threshold_for_picking"),
			(gt, reg1, 0)
		],
		"Pick the items which price higher than {reg1} florins and continue.",
		[
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(is_between, ":party_stack_troop_id_main_party_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(call_script, "script_transfer_special_inventory", "$pool_troop", ":party_stack_troop_id_main_party_localvariable"),
			(try_end),
			(call_script, "script_sort_food", "trp_player"),
			(jump_to_menu, "$return_menu")
		], "."),

		("auto_loot_leave",
		[],
		"{s20}",
		[
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(is_between, ":party_stack_troop_id_main_party_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(call_script, "script_transfer_inventory", "$pool_troop", ":party_stack_troop_id_main_party_localvariable", 1),
			(try_end),
			(call_script, "script_sort_food", "trp_player"),
			(jump_to_menu, "$return_menu")
		], ".")
	]
	),

	("auto_loot", 0, "Your heroes will automatically grab items from the item pool based on their pre-selected upgrade options. Heroes listed first in the party order will have first pick. Any equipment no longer needed will be placed back into the item pool. Are you sure you wish to do this?",
"none",
	[],
	[
		("No",
		[],
		"No, I've changed my mind.",
		[
			(jump_to_menu, "mnu_manage_loot_pool")
		], "."),

		("Yes",
		[],
		"Yes, perform the upgrading.",
		[
			(call_script, "script_auto_loot_all"),
			(jump_to_menu, "mnu_manage_loot_pool")
		], ".")
	]
	),

	("pagan_stronghold", 0, "You enter a deep forest and spot a fortified settlement, it belongs to the {s21}.",
"none",
	[
		(str_store_faction_name, 21, "$g_encountered_party_faction"),
		(troop_get_type, ":type_player", "trp_player"),
		(try_begin),
			(eq, ":type_player", 1),
			(set_background_mesh, "mesh_pic_siege_sighted_fem"),
		(else_try),
			(set_background_mesh, "mesh_pic_siege_sighted"),
		(try_end)
	],
	[
		("pagan_stronghold_attack",
		[
			(store_relation, ":relation_g_encountered_party_faction_player_supporters_faction", "$g_encountered_party_faction", "fac_player_supporters_faction"),
			(assign, reg0, ":relation_g_encountered_party_faction_player_supporters_faction"),
			(display_message, "@relation: {reg0}"),
			(lt, ":relation_g_encountered_party_faction_player_supporters_faction", 0),
			(set_background_mesh, "mesh_pic_siege_attack")
		],
		"Attack...",
		[
			(call_script, "script_calculate_renown_value"),
			(call_script, "script_calculate_battle_advantage"),
			(assign, ":var_1", reg0),
			(val_mul, ":var_1", 2),
			(val_div, ":var_1", 3),
			(set_battle_advantage, ":var_1"),
			(set_jump_mission, "mt_pagan_stronghold_attack"),
			(assign, "$g_next_menu", "mnu_castle_taken"),
			(set_party_battle_mode),
			(assign, ":var_2", "scn_pagan_stronghold_1"),
			(assign, "$g_next_menu", "mnu_simple_encounter"),
			(jump_to_scene, ":var_2"),
			(jump_to_menu, "mnu_battle_debrief"),
			(change_screen_mission)
		], "."),

		("pagan_stronghold_leave",
		[],
		"Leave.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("manor_center", 0, "{s9} {s21}. {s22} {s23}",
"none",
	[
		(try_begin),
			(store_time_of_day, ":time_of_day"),
			(ge, ":time_of_day", 5),
			(lt, ":time_of_day", 21),
			(assign, "$town_nighttime", 0),
		(else_try),
			(assign, "$town_nighttime", 1),
		(try_end),
		(str_store_faction_name, 21, "$g_encountered_party_faction"),
		(troop_get_type, ":type_player", "trp_player"),
		(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
		(str_store_string, 9, "@You come across a small settlement. It belongs to the"),
		(try_begin),
			(this_or_next|party_slot_eq, ":g_encountered_party_village_bound_center", slot_village_state, 2),
			(party_slot_eq, "$g_encountered_party", slot_village_state, 2),
			(party_slot_eq, "$g_encountered_party", 327, 0),
			(set_background_mesh, "mesh_pic_looted_village"),
			(str_store_string, 9, "@You come across a small abandoned settlement. It belonged to the"),
		(else_try),
			(set_background_mesh, "mesh_pic_manor"),
		(try_end),
		(str_clear, 22),
		(assign, ":value", 0),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", 327, 0),
			(this_or_next|party_slot_eq, ":g_encountered_party_village_bound_center", slot_village_state, 2),
			(party_slot_eq, "$g_encountered_party", slot_village_state, 2),
			(assign, ":value", 1),
		(try_end),
		(eq, ":value", 0),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 1),
			(str_store_string, 22, "@Troublesome bandits are abusing the peasants."),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 2),
			(str_store_string, 22, "@A company of mercenaries are abusing the peasants. Locals say that they are well armed!"),
		(else_try),
			(str_store_string, 22, "@Troublesome bandits are abusing the peasants."),
			(str_clear, 22),
		(try_end),
		(str_clear, 23),
		(try_begin),
			(party_get_slot, ":g_encountered_party_342", "$g_encountered_party", 342),
			(party_get_slot, ":g_encountered_party_town_prosperity", "$g_encountered_party", slot_town_prosperity),
			(assign, reg0, ":g_encountered_party_342"),
			(assign, reg1, ":g_encountered_party_town_prosperity"),
			(str_store_string, 23, "@Current population: {reg0}, current prosperity: {reg1}"),
		(try_end)
	],
	[
		("manor_debug",
		[
			(eq, 0, 1)
		],
		"DEBUG this manor.",
		[
			(jump_to_menu, "mnu_manor_build")
		], "."),

		("manor_center_bandits",
		[
			(party_slot_ge, "$g_encountered_party", 39, 1),
			(neg|party_slot_eq, "$g_encountered_party", slot_village_state, 2),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(neg|party_slot_eq, ":g_encountered_party_village_bound_center", slot_village_state, 2)
		],
		"Smash the bastards.",
		[
			(party_clear_particle_systems, "$g_encountered_party"),
			(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(party_clear, ":g_encountered_party_town_center"),
			(modify_visitors_at_site, ":g_encountered_party_town_center"),
			(reset_visitors),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 2),
				(store_random_in_range, ":random_in_range_3_7", 3, 7),
				(call_script, "script_get_mercenary_troop_for_manor", ":faction_of_party_g_encountered_party"),
				(assign, ":value", reg0),
				(set_visitors, 0, ":value", ":random_in_range_3_7"),
				(party_add_members, "$g_encountered_party", ":value", ":random_in_range_3_7"),
				(store_random_in_range, ":random_in_range_3_7", 3, 7),
				(call_script, "script_get_mercenary_troop_for_manor", ":faction_of_party_g_encountered_party"),
				(assign, ":value", reg0),
				(set_visitors, 0, ":value", ":random_in_range_3_7"),
				(party_add_members, "$g_encountered_party", ":value", ":random_in_range_3_7"),
				(store_random_in_range, ":random_in_range_3_7", 3, 7),
				(call_script, "script_get_mercenary_troop_for_manor", ":faction_of_party_g_encountered_party"),
				(assign, ":value", reg0),
				(set_visitors, 0, ":value", ":random_in_range_3_7"),
				(party_add_members, "$g_encountered_party", ":value", ":random_in_range_3_7"),
				(store_random_in_range, ":random_in_range_3_7", 3, 7),
				(call_script, "script_get_mercenary_troop_for_manor", ":faction_of_party_g_encountered_party"),
				(assign, ":value", reg0),
				(set_visitors, 0, ":value", ":random_in_range_3_7"),
				(party_add_members, "$g_encountered_party", ":value", ":random_in_range_3_7"),
			(else_try),
				(store_random_in_range, ":value", "trp_mountain_bandit", "trp_taiga_bandit"),
				(store_random_in_range, ":random_in_range_3_7", 10, 31),
				(set_visitors, 0, ":value", ":random_in_range_3_7"),
				(party_add_members, "$g_encountered_party", ":value", ":random_in_range_3_7"),
			(try_end),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			(assign, "$g_battle_result", 0),
			(set_jump_mission, "mt_manor_attack_bandits"),
			(jump_to_scene, ":g_encountered_party_town_center"),
			(assign, "$g_next_menu", "mnu_manor_infest_bandits_result"),
			(jump_to_menu, "mnu_battle_debrief"),
			(assign, "$g_mt_mode", 1),
			(change_screen_mission)
		], "."),

		("manor_walk",
		[
			(neg|party_slot_eq, "$g_encountered_party", slot_village_state, 2),
			(party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(this_or_next|party_slot_eq, "$g_encountered_party", 327, 1),
			(neg|party_slot_eq, ":g_encountered_party_village_bound_center", slot_village_state, 2)
		],
		"Walk around the center.",
		[
			(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(assign, "$current_town", ":g_encountered_party_village_bound_center"),
			(call_script, "script_manor_refresh_inventories", "$g_encountered_party"),
			(modify_visitors_at_site, ":g_encountered_party_town_center"),
			(reset_visitors),
			(try_begin),
				(call_script, "script_init_manor_agents", "$g_encountered_party"),
				(set_jump_mission, "mt_manor_center"),
			(try_end),
			(jump_to_scene, ":g_encountered_party_town_center"),
			(change_screen_mission)
		], "."),

		("manor_improve",
		[
			(neg|party_slot_eq, "$g_encountered_party", 301, 1),
			(neg|party_slot_eq, "$g_encountered_party", 301, 2),
			(this_or_next|eq, "$g_encountered_party_template", "pt_salt"),
			(eq, "$g_encountered_party_template", "pt_iron"),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(party_get_slot, ":g_encountered_party_village_bound_center_town_lord", ":g_encountered_party_village_bound_center", slot_town_lord),
			(eq, ":g_encountered_party_village_bound_center_town_lord", "trp_player"),
			(neg|party_slot_eq, ":g_encountered_party_village_bound_center", slot_village_state, 2)
		],
		"Improve this settlment.",
		[
			(jump_to_menu, "mnu_manor_improve_menu")
		], "."),

		("manor_leave",
		[],
		"Leave.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("manor_build", 0, "MANOR DEBUG",
"none",
	[],
	[
		("manor_improve_next",
		[],
		"Next Page",
		[
			(try_begin),
				(eq, "$tom_page", 0),
				(assign, "$tom_page", 1),
			(else_try),
				(assign, "$tom_page", 0),
			(try_end)
		], "."),

		("manor_improve_leave",
		[],
		"Reset Buildings.",
		[
			(party_set_slot, "$g_encountered_party", 302, 0),
			(party_set_slot, "$g_encountered_party", 308, 0),
			(party_set_slot, "$g_encountered_party", 309, 0),
			(party_set_slot, "$g_encountered_party", 310, 0),
			(party_set_slot, "$g_encountered_party", 311, 0),
			(party_set_slot, "$g_encountered_party", 303, 0),
			(party_set_slot, "$g_encountered_party", 304, 0),
			(party_set_slot, "$g_encountered_party", 305, 0),
			(party_set_slot, "$g_encountered_party", 306, 0),
			(party_set_slot, "$g_encountered_party", 307, 0),
			(party_set_slot, "$g_encountered_party", 312, 0),
			(party_set_slot, "$g_encountered_party", 313, 0),
			(party_set_slot, "$g_encountered_party", 314, 0),
			(party_set_slot, "$g_encountered_party", 315, 0),
			(party_set_slot, "$g_encountered_party", 316, 0),
			(party_set_slot, "$g_encountered_party", 317, 0),
			(party_set_slot, "$g_encountered_party", 318, 0),
			(party_set_slot, "$g_encountered_party", 319, 0),
			(party_set_slot, "$g_encountered_party", 320, 0),
			(party_set_slot, "$g_encountered_party", 321, 0),
			(party_set_slot, "$g_encountered_party", 322, 0),
			(party_set_slot, "$g_encountered_party", 323, 0),
			(party_set_slot, "$g_encountered_party", 324, 0),
			(party_set_slot, "$g_encountered_party", 325, 0),
			(party_set_slot, "$g_encountered_party", 327, 0),
			(party_set_slot, "$g_encountered_party", 326, 0)
		], "."),

		("manor_improve_leave",
		[],
		"Go Back.",
		[
			(jump_to_menu, "mnu_manor_center"),
			(change_screen_return)
		], "."),

		("manor_improve_house",
		[
			(eq, "$tom_page", 0),
			(this_or_next|party_slot_eq, "$g_encountered_party", 302, 0),
			(party_slot_eq, "$g_encountered_party", 302, 1)
		],
		"Improve houses",
		[
			(party_get_slot, ":g_encountered_party_302", "$g_encountered_party", 302),
			(val_add, ":g_encountered_party_302", 1),
			(party_set_slot, "$g_encountered_party", 302, ":g_encountered_party_302")
		], "."),

		("manor_improve_farm",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 308, 0)
		],
		"Build grain farm",
		[
			(party_get_slot, ":g_encountered_party_308", "$g_encountered_party", 308),
			(val_add, ":g_encountered_party_308", 1),
			(party_set_slot, "$g_encountered_party", 308, ":g_encountered_party_308")
		], "."),

		("manor_improve_livestock",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 309, 0)
		],
		"Build animal farm",
		[
			(party_get_slot, ":g_encountered_party_309", "$g_encountered_party", 309),
			(val_add, ":g_encountered_party_309", 1),
			(party_set_slot, "$g_encountered_party", 309, ":g_encountered_party_309")
		], "."),

		("manor_improve_fruitfarm",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 310, 0)
		],
		"Build fruit farm",
		[
			(party_get_slot, ":g_encountered_party_310", "$g_encountered_party", 310),
			(val_add, ":g_encountered_party_310", 1),
			(party_set_slot, "$g_encountered_party", 310, ":g_encountered_party_310")
		], "."),

		("manor_improve_fisher",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 311, 0)
		],
		"Build fishers",
		[
			(party_get_slot, ":g_encountered_party_311", "$g_encountered_party", 311),
			(val_add, ":g_encountered_party_311", 1),
			(party_set_slot, "$g_encountered_party", 311, ":g_encountered_party_311")
		], "."),

		("manor_improve_marketplace",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 303, 0)
		],
		"Build Marketplace",
		[
			(party_get_slot, ":g_encountered_party_303", "$g_encountered_party", 303),
			(val_add, ":g_encountered_party_303", 1),
			(party_set_slot, "$g_encountered_party", 303, ":g_encountered_party_303")
		], "."),

		("manor_improve_tavern",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 304, 0)
		],
		"Build tavern",
		[
			(party_get_slot, ":g_encountered_party_304", "$g_encountered_party", 304),
			(val_add, ":g_encountered_party_304", 1),
			(party_set_slot, "$g_encountered_party", 304, ":g_encountered_party_304")
		], "."),

		("manor_improve_whorehouse",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 305, 0)
		],
		"Build Harlot houses",
		[
			(party_get_slot, ":g_encountered_party_305", "$g_encountered_party", 305),
			(val_add, ":g_encountered_party_305", 1),
			(party_set_slot, "$g_encountered_party", 305, ":g_encountered_party_305")
		], "."),

		("manor_improve_temple",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 306, 0)
		],
		"Build Monastery",
		[
			(party_get_slot, ":g_encountered_party_306", "$g_encountered_party", 306),
			(val_add, ":g_encountered_party_306", 1),
			(party_set_slot, "$g_encountered_party", 306, ":g_encountered_party_306")
		], "."),

		("manor_improve_well",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 307, 0)
		],
		"Dig wells",
		[
			(party_get_slot, ":g_encountered_party_307", "$g_encountered_party", 307),
			(val_add, ":g_encountered_party_307", 1),
			(party_set_slot, "$g_encountered_party", 307, ":g_encountered_party_307")
		], "."),

		("manor_improve_bakery",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 312, 0)
		],
		"Build bakery",
		[
			(party_get_slot, ":g_encountered_party_312", "$g_encountered_party", 312),
			(val_add, ":g_encountered_party_312", 1),
			(party_set_slot, "$g_encountered_party", 312, ":g_encountered_party_312")
		], "."),

		("manor_improve_winery",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 313, 0)
		],
		"Build Winery",
		[
			(party_get_slot, ":g_encountered_party_313", "$g_encountered_party", 313),
			(val_add, ":g_encountered_party_313", 1),
			(party_set_slot, "$g_encountered_party", 313, ":g_encountered_party_313")
		], "."),

		("manor_improve_brewery",
		[
			(eq, "$tom_page", 0),
			(party_slot_eq, "$g_encountered_party", 314, 0)
		],
		"Build Brewery",
		[
			(party_get_slot, ":g_encountered_party_314", "$g_encountered_party", 314),
			(val_add, ":g_encountered_party_314", 1),
			(party_set_slot, "$g_encountered_party", 314, ":g_encountered_party_314")
		], "."),

		("manor_improve_potter",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 315, 0)
		],
		"Build Pottery",
		[
			(party_get_slot, ":g_encountered_party_315", "$g_encountered_party", 315),
			(val_add, ":g_encountered_party_315", 1),
			(party_set_slot, "$g_encountered_party", 315, ":g_encountered_party_315")
		], "."),

		("manor_improve_blacksmith",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 316, 0)
		],
		"Build Blacksmith",
		[
			(party_get_slot, ":g_encountered_party_316", "$g_encountered_party", 316),
			(val_add, ":g_encountered_party_316", 1),
			(party_set_slot, "$g_encountered_party", 316, ":g_encountered_party_316")
		], "."),

		("manor_improve_butcher",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 317, 0)
		],
		"Build Butchery",
		[
			(party_get_slot, ":g_encountered_party_317", "$g_encountered_party", 317),
			(val_add, ":g_encountered_party_317", 1),
			(party_set_slot, "$g_encountered_party", 317, ":g_encountered_party_317")
		], "."),

		("manor_improve_oilmaker",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 318, 0)
		],
		"Build Oil Maker",
		[
			(party_get_slot, ":g_encountered_party_318", "$g_encountered_party", 318),
			(val_add, ":g_encountered_party_318", 1),
			(party_set_slot, "$g_encountered_party", 318, ":g_encountered_party_318")
		], "."),

		("manor_improve_linenworkshop",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 319, 0)
		],
		"Build Linen Workshop",
		[
			(party_get_slot, ":g_encountered_party_319", "$g_encountered_party", 319),
			(val_add, ":g_encountered_party_319", 1),
			(party_set_slot, "$g_encountered_party", 319, ":g_encountered_party_319")
		], "."),

		("manor_improve_woolworkshop",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 320, 0)
		],
		"Build Wool Workshop",
		[
			(party_get_slot, ":g_encountered_party_320", "$g_encountered_party", 320),
			(val_add, ":g_encountered_party_320", 1),
			(party_set_slot, "$g_encountered_party", 320, ":g_encountered_party_320")
		], "."),

		("manor_improve_tannery",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 321, 0)
		],
		"Build Tannery",
		[
			(party_get_slot, ":g_encountered_party_321", "$g_encountered_party", 321),
			(val_add, ":g_encountered_party_321", 1),
			(party_set_slot, "$g_encountered_party", 321, ":g_encountered_party_321")
		], "."),

		("manor_improve_prison",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 322, 0)
		],
		"Build Prison",
		[
			(party_get_slot, ":g_encountered_party_322", "$g_encountered_party", 322),
			(val_add, ":g_encountered_party_322", 1),
			(party_set_slot, "$g_encountered_party", 322, ":g_encountered_party_322")
		], "."),

		("manor_improve_armorsmith",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 323, 0)
		],
		"Build Armorsmithy",
		[
			(party_get_slot, ":g_encountered_party_323", "$g_encountered_party", 323),
			(val_add, ":g_encountered_party_323", 1),
			(party_set_slot, "$g_encountered_party", 323, ":g_encountered_party_323")
		], "."),

		("manor_improve_weaponsmith",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 324, 0)
		],
		"Build Weaponsmithy",
		[
			(eq, "$tom_page", 1),
			(party_get_slot, ":g_encountered_party_324", "$g_encountered_party", 324),
			(val_add, ":g_encountered_party_324", 1),
			(party_set_slot, "$g_encountered_party", 324, ":g_encountered_party_324")
		], "."),

		("manor_improve_fletcher",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 325, 0)
		],
		"Build Fletchery",
		[
			(party_get_slot, ":g_encountered_party_325", "$g_encountered_party", 325),
			(val_add, ":g_encountered_party_325", 1),
			(party_set_slot, "$g_encountered_party", 325, ":g_encountered_party_325")
		], "."),

		("manor_improve_breeder",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 326, 0)
		],
		"Build Stables",
		[
			(party_get_slot, ":g_encountered_party_326", "$g_encountered_party", 326),
			(val_add, ":g_encountered_party_326", 1),
			(party_set_slot, "$g_encountered_party", 326, ":g_encountered_party_326")
		], "."),

		("manor_improve_walls",
		[
			(eq, "$tom_page", 1),
			(party_slot_eq, "$g_encountered_party", 327, 0)
		],
		"Build Walls",
		[
			(party_get_slot, ":g_encountered_party_327", "$g_encountered_party", 327),
			(val_add, ":g_encountered_party_327", 1),
			(party_set_slot, "$g_encountered_party", 327, ":g_encountered_party_327")
		], ".")
	]
	),

	("manor_improve_menu", 0, "Do you wish to upgrade your {s0} to a {s1}. This would increase their production. It would cost you {reg0}",
"none",
	[
		(try_begin),
			(eq, "$g_encountered_party_template", "pt_salt"),
			(str_store_string, 0, "@Salt Trader"),
			(str_store_string, 1, "@Salt Mine"),
			(store_add, reg0, 12000, 12000),
		(else_try),
			(eq, "$g_encountered_party_template", "pt_iron"),
			(str_store_string, 0, "@Iron Trader"),
			(str_store_string, 1, "@Iron Mine"),
			(store_add, reg0, 10000, 10000),
		(else_try),
			(jump_to_menu, "mnu_manor_center"),
		(try_end)
	],
	[
		("manor_improve_menu_accept",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg0)
		],
		"Yes.",
		[
			(troop_remove_gold, "trp_player", reg0),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(assign, ":value", 0),
			(try_begin),
				(eq, "$g_encountered_party_template", "pt_salt"),
				(call_script, "script_spawn_manor_party", "pt_salt_mine", ":g_encountered_party_village_bound_center"),
				(assign, ":value", reg0),
			(else_try),
				(call_script, "script_spawn_manor_party", "pt_iron_mine", ":g_encountered_party_village_bound_center"),
				(assign, ":value", reg0),
			(try_end),
			(party_get_position, 0, "$g_encountered_party"),
			(party_set_position, ":value", 0),
			(remove_party, "$g_encountered_party"),
			(assign, "$g_encountered_party", ":value"),
			(call_script, "script_update_manor_array"),
			(change_screen_return)
		], "."),

		("manor_improve_menu_refuse",
		[],
		"No.",
		[
			(jump_to_menu, "mnu_manor_center")
		], ".")
	]
	),

	("center_spawn_manor", 0, "Do you wish to purchase a manor house nearby? It costs {reg10}",
"none",
	[
		(assign, reg10, 10000)
	],
	[
		("center_spawn_manor_farm",
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", 10000),
			(assign, reg0, 10000)
		],
		"Yes!",
		[
			(call_script, "script_spawn_manor_party", "pt_manor", "$current_town"),
			(call_script, "script_update_manor_array"),
			(troop_remove_gold, "trp_player", 10000),
			(display_message, "@You purchased a manor nearby!"),
			(jump_to_menu, "$g_next_menu")
		], "."),

		("center_spawn_manor_leave",
		[],
		"No.",
		[
			(jump_to_menu, "$g_next_menu")
		], ".")
	]
	),

	("manor_infest_bandits_result", 0, "{s9}",
"none",
	[
		(try_begin),
			(eq, "$g_battle_result", 1),
			(str_store_string, 9, "@You slaughter the bastards like pigs! The peasants cheer your name and are planning on holding a feast in the near future to honor you!    "),
		(else_try),
			(str_store_string, 9, "@Try as you might, you could not defeat the bastards. They had their fun with the local peasants and left."),
			(set_background_mesh, "mesh_pic_looted_village"),
		(try_end)
	],
	[
		("manor_infest_victory",
		[
			(eq, "$g_battle_result", 1)
		],
		"Huzzah! Now to the looting...",
		[
			(display_message, "@Relationship with the regional center improves!"),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(call_script, "script_change_player_relation_with_center", ":g_encountered_party_village_bound_center", 1),
			(troop_clear_inventory, "trp_temp_troop"),
			(party_get_num_companion_stacks, ":num_companion_stacks_l_g_encountered_party", "$g_encountered_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_l_g_encountered_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
				(party_stack_get_size, ":party_stack_size_g_encountered_party_localvariable", "$g_encountered_party", ":localvariable"),
				(try_for_range, ":unused", 0, ":party_stack_size_g_encountered_party_localvariable"),
					(troop_loot_troop, "trp_temp_troop", ":party_stack_troop_id_g_encountered_party_localvariable", 70),
				(try_end),
			(try_end),
			(party_clear, "$g_encountered_party"),
			(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(assign, ":var_7", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_l_g_encountered_party", "p_main_party"),
			(try_for_range, ":localvariable_2", 0, ":num_companion_stacks_l_g_encountered_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_g_encountered_party_localvariable", "p_main_party", ":localvariable_2"),
				(is_between, ":party_stack_troop_id_g_encountered_party_localvariable", "trp_npc1", "trp_kingdom_1_lord"),
				(val_add, ":var_7", 1),
			(try_end),
			(try_begin),
				(gt, ":var_7", 0),
				(assign, "$return_menu", "mnu_manor_center"),
				(jump_to_menu, "mnu_manage_loot_pool"),
			(else_try),
				(jump_to_menu, "mnu_manor_center"),
				(change_screen_loot, "trp_temp_troop"),
			(try_end)
		], "."),

		("manor_infest_defeat",
		[
			(neq, "$g_battle_result", 1)
		],
		"Well, atleast I'm still alive...",
		[
			(display_message, "@Relationship with the regional center deteriorates..."),
			(party_get_slot, ":g_encountered_party_village_bound_center", "$g_encountered_party", slot_village_bound_center),
			(call_script, "script_change_player_relation_with_center", ":g_encountered_party_village_bound_center", -1),
			(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
			(party_set_slot, "$g_encountered_party", slot_village_state, 2),
			(party_clear, "$g_encountered_party"),
			(change_screen_return)
		], ".")
	]
	),

	("harlot_services", 0, "{s9}",
"none",
	[
		(str_store_string, 9, "@You walk with the harlot to a private room to have some fun. Time passes...")
	],
	[
		("harlot_services_continue",
		[
			(str_store_string, 0, "@And my tackle became really itchy too...")
		],
		"{s0}",
		[], ".")
	]
	),

	("lance_recruitment", 0, "{s30}^{s31}^ {s32}^ {s33} ",
"none",
	[
		(str_clear, 30),
		(str_clear, 31),
		(str_clear, 32),
		(str_clear, 33),
		(str_store_string, 30, "@There are no lances available for recruitment."),
		(str_store_string, 31, "@There is no local mercenary company available for hire."),
		(party_get_slot, reg20, "$current_town", slot_center_volunteer_troop_amount),
		(party_get_slot, reg21, "$current_town", 703),
		(party_get_slot, reg22, "$current_town", 706),
		(party_get_slot, reg23, "$current_town", 709),
		(try_begin),
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(this_or_next|eq, "$cheat_mode", 1),
			(eq, ":current_town_town_lord", "trp_player"),
			(str_store_string, 30, "@You currently have {reg20} lances available for recruitment."),
			(party_get_slot, reg24, "$current_town", 715),
			(party_get_slot, reg25, "$current_town", 714),
			(this_or_next|gt, reg24, 0),
			(gt, reg25, 0),
			(str_store_string, 30, "@You currently have {reg20} lances available for recruitment. Among them are {reg24} nobles and {reg25} commoners that have experience in the field of battle."),
		(try_end),
		(try_begin),
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(gt, reg21, 0),
			(str_store_string, 31, "@A local mercenary company is available for hire."),
		(try_end),
		(try_begin),
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(try_begin),
				(party_slot_eq, "$current_town", 705, 28),
				(str_store_string, 32, "@Geonese crossbowmen have their headquarters here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 23),
				(str_store_string, 32, "@Turkopole mecenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 21),
				(str_store_string, 32, "@Georgian mecenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 24),
				(str_store_string, 32, "@Cuman mecenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 20),
				(str_store_string, 32, "@Brabantine mecenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 22),
				(str_store_string, 32, "@Sicilian mecenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 4),
				(str_store_string, 32, "@Maghrebi mercenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 31),
				(str_store_string, 32, "@Khwarezmian mercenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 32),
				(str_store_string, 32, "@Mordovian mercenaries often pass-by here."),
			(else_try),
				(party_slot_eq, "$current_town", 705, 33),
				(str_store_string, 32, "@Kipchak mercenaries often pass-by here."),
			(try_end),
		(try_end),
		(try_begin),
			(party_slot_eq, "$current_town", 708, 50),
			(str_store_string, 33, "@The Varangians have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 51),
			(str_store_string, 33, "@The Teutonic Order have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 52),
			(str_store_string, 33, "@The Hospitalier Order have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 53),
			(str_store_string, 33, "@The Templar Order have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 54),
			(str_store_string, 33, "@The Order of Saint Lazarus have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 55),
			(str_store_string, 33, "@The Order of Santiago have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 56),
			(str_store_string, 33, "@The Order of Calatrava have their headquarters here."),
		(else_try),
			(party_slot_eq, "$current_town", 708, 57),
			(str_store_string, 33, "@The Order of Saint Thomas have their headquarters here."),
		(try_end),
		(set_background_mesh, "mesh_pic_recruits")
	],
	[
		("recruit_lance",
		[
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(this_or_next|eq, ":current_town_town_lord", "trp_player"),
			(eq, "$cheat_mode", 1),
			(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
			(ge, ":free_companions_capacity_main_party", 10),
			(party_get_slot, ":current_town_center_volunteer_troop_amount", "$current_town", slot_center_volunteer_troop_amount),
			(gt, ":current_town_center_volunteer_troop_amount", 0),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(call_script, "script_check_if_faction_is_at_war", ":faction_of_party_current_town"),
			(assign, reg5, 0),
			(str_clear, 1),
			(try_begin),
				(eq, reg0, 0),
				(assign, reg5, 500),
				(str_store_string, 1, "@Cost: {reg5}"),
			(try_end),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg5)
		],
		"Recruit one lance {s1}",
		[
			(party_get_slot, ":current_town_center_volunteer_troop_amount", "$current_town", slot_center_volunteer_troop_amount),
			(val_sub, ":current_town_center_volunteer_troop_amount", 1),
			(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, ":current_town_center_volunteer_troop_amount"),
			(call_script, "script_fill_lance", "$current_town", "p_main_party"),
			(call_script, "script_balance_lance_storage"),
			(try_begin),
				(gt, reg5, 0),
				(troop_remove_gold, "trp_player", reg5),
			(try_end),
			(try_begin),
				(gt, ":current_town_center_volunteer_troop_amount", 0),
				(jump_to_menu, "mnu_lance_recruitment"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("recruit_all_lances",
		[
			(party_get_slot, ":current_town_town_lord", "$current_town", slot_town_lord),
			(eq, ":current_town_town_lord", "trp_player"),
			(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
			(ge, ":free_companions_capacity_main_party", 20),
			(party_get_slot, ":current_town_center_volunteer_troop_amount", "$current_town", slot_center_volunteer_troop_amount),
			(gt, ":current_town_center_volunteer_troop_amount", 1),
			(set_background_mesh, "mesh_pic_recruits"),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(call_script, "script_check_if_faction_is_at_war", ":faction_of_party_current_town"),
			(assign, reg6, 0),
			(str_clear, 2),
			(try_begin),
				(eq, reg0, 0),
				(assign, reg6, 500),
				(val_mul, reg6, ":current_town_center_volunteer_troop_amount"),
				(str_store_string, 2, "@Cost: {reg6}"),
			(try_end),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg6)
		],
		"Recruit all of the lances. {s2}",
		[
			(party_get_slot, ":current_town_center_volunteer_troop_amount", "$current_town", slot_center_volunteer_troop_amount),
			(assign, ":var_2", ":current_town_center_volunteer_troop_amount"),
			(try_for_range, ":unused", 0, ":var_2"),
				(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
				(ge, ":free_companions_capacity_main_party", 10),
				(call_script, "script_fill_lance", "$current_town", "p_main_party"),
				(call_script, "script_balance_lance_storage"),
				(val_sub, ":current_town_center_volunteer_troop_amount", 1),
			(try_end),
			(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, ":current_town_center_volunteer_troop_amount"),
			(try_begin),
				(gt, reg6, 0),
				(troop_remove_gold, "trp_player", reg6),
			(try_end),
			(try_begin),
				(gt, ":current_town_center_volunteer_troop_amount", 0),
				(jump_to_menu, "mnu_lance_recruitment"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("recruit_company",
		[
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(party_slot_ge, "$current_town", 703, 1),
			(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
			(ge, ":free_companions_capacity_main_party", 30),
			(call_script, "script_get_number_of_hero_centers", "trp_player"),
			(assign, reg7, 1000),
			(str_clear, 1),
			(try_begin),
				(gt, reg0, 0),
				(assign, reg7, 3000),
			(try_end),
			(store_party_size, ":party_size_main_party", "p_main_party"),
			(store_div, ":value", ":party_size_main_party", 20),
			(val_add, ":value", 1),
			(assign, reg0, ":value"),
			(try_begin),
				(eq, 0, 1),
				(gt, ":value", 1),
				(val_mul, reg7, ":value"),
			(try_end),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg7),
			(str_store_string, 3, "@Cost: {reg7}")
		],
		"Hire a local mercenary company. {s3}",
		[
			(party_get_slot, ":current_town_703", "$current_town", 703),
			(val_sub, ":current_town_703", 1),
			(party_set_slot, "$current_town", 703, ":current_town_703"),
			(try_begin),
				(gt, reg7, 0),
				(troop_remove_gold, "trp_player", reg7),
			(try_end),
			(call_script, "script_fill_company", "$current_town", "p_main_party", 702),
			(try_begin),
				(gt, ":current_town_703", 0),
				(jump_to_menu, "mnu_lance_recruitment"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("recruit_company_special",
		[
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(party_slot_ge, "$current_town", 705, 1),
			(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
			(ge, ":free_companions_capacity_main_party", 30),
			(party_get_slot, ":current_town_706", "$current_town", 706),
			(gt, ":current_town_706", 0),
			(call_script, "script_get_number_of_hero_centers", "trp_player"),
			(assign, reg8, 1000),
			(str_clear, 1),
			(try_begin),
				(gt, reg0, 0),
				(assign, reg8, 3000),
			(try_end),
			(store_party_size, ":party_size_main_party", "p_main_party"),
			(store_div, ":value", ":party_size_main_party", 20),
			(val_add, ":value", 1),
			(assign, reg0, ":value"),
			(try_begin),
				(eq, 0, 1),
				(gt, ":value", 1),
				(val_mul, reg8, ":value"),
			(try_end),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg8),
			(str_store_string, 4, "@Cost: {reg8}"),
			(try_begin),
				(party_slot_eq, "$current_town", 705, 28),
				(str_store_string, 20, "@Geonese crossbowmen"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 23),
				(str_store_string, 20, "@Turcopoles"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 21),
				(str_store_string, 20, "@Georgians"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 24),
				(str_store_string, 20, "@Cumans"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 20),
				(str_store_string, 20, "@Brabantine"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 22),
				(str_store_string, 20, "@Sicilian Muslims"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 29),
				(str_store_string, 20, "@Welshmen"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 33),
				(str_store_string, 20, "@Kipchaks"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 32),
				(str_store_string, 20, "@Mordovians"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 31),
				(str_store_string, 20, "@Khwarezmians"),
			(try_end)
		],
		"Hire a company of {s20}. {s4}",
		[
			(party_get_slot, ":current_town_706", "$current_town", 706),
			(val_sub, ":current_town_706", 1),
			(party_set_slot, "$current_town", 706, ":current_town_706"),
			(try_begin),
				(gt, reg8, 0),
				(troop_remove_gold, "trp_player", reg8),
			(try_end),
			(call_script, "script_fill_company", "$current_town", "p_main_party", 705),
			(try_begin),
				(gt, ":current_town_706", 0),
				(jump_to_menu, "mnu_lance_recruitment"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("recruit_crusaders",
		[
			(is_between, "$current_town", "p_town_1_1", "p_castle_1_1"),
			(party_slot_ge, "$current_town", 708, 1),
			(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
			(ge, ":free_companions_capacity_main_party", 30),
			(party_get_slot, ":current_town_709", "$current_town", 709),
			(gt, ":current_town_709", 0),
			(store_faction_of_party, ":faction_of_party_current_town", "$current_town"),
			(eq, ":faction_of_party_current_town", "$players_kingdom"),
			(str_clear, 1),
			(assign, reg9, 4000),
			(store_party_size, ":party_size_main_party", "p_main_party"),
			(store_div, ":value", ":party_size_main_party", 20),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg9),
			(str_store_string, 5, "@Cost: {reg9}"),
			(try_begin),
				(party_slot_eq, "$current_town", 708, 53),
				(str_store_string, 21, "@The Knights Templar"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 52),
				(str_store_string, 21, "@The Knights Hospitalier"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 54),
				(str_store_string, 21, "@The Knights of Saint Lazarus"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 55),
				(str_store_string, 21, "@The Knights of Santiago"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 56),
				(str_store_string, 21, "@The Knights of Calatrava"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 57),
				(str_store_string, 21, "@The Knights of Saint Thomas of Acre"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 51),
				(str_store_string, 21, "@The Teutonic Knights"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 50),
				(str_store_string, 21, "@The Varangians"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 30),
				(str_store_string, 21, "@The Mamluks"),
			(try_end)
		],
		"Call upon {s21}. {s5}",
		[
			(party_get_slot, ":current_town_709", "$current_town", 709),
			(val_sub, ":current_town_709", 1),
			(party_set_slot, "$current_town", 709, ":current_town_709"),
			(call_script, "script_fill_company", "$current_town", "p_main_party", 708),
			(try_begin),
				(gt, reg9, 0),
				(troop_remove_gold, "trp_player", reg9),
			(try_end),
			(try_begin),
				(gt, ":current_town_709", 0),
				(jump_to_menu, "mnu_lance_recruitment"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], "."),

		("camp_disband_lances",
		[
			(eq, "$use_feudal_lance", 1)
		],
		"Disband lance forces.",
		[
			(assign, "$g_next_menu", "mnu_lance_recruitment"),
			(jump_to_menu, "mnu_disband_lances")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(try_begin),
				(party_slot_eq, "$current_town", slot_party_type, 3),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(party_slot_eq, "$current_town", slot_party_type, 2),
				(jump_to_menu, "mnu_town"),
			(else_try),
				(jump_to_menu, "mnu_village"),
			(try_end)
		], ".")
	]
	),

	("lance_prison", 0, "Garrison management for {s0}^ Currently the garrison is controlled and maintained by {s1}.",
"none",
	[
		(str_store_party_name, 0, "$current_town"),
		(try_begin),
			(party_slot_eq, "$current_town", 700, 0),
			(str_store_string, 1, "@the militia"),
		(else_try),
			(str_store_string, 1, "@the lord"),
		(try_end),
		(assign, "$g_move_heroes", 1),
		(try_begin),
			(party_slot_eq, "$current_town", 700, 0),
			(call_script, "script_party_prisoners_add_party_prisoners", "$current_town", "p_temp_party"),
			(call_script, "script_party_remove_all_prisoners", "p_temp_party"),
			(call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
			(party_clear, "p_temp_party"),
		(try_end),
		(set_background_mesh, "mesh_pic_siege_sighted_fem")
	],
	[
		("trade_prisoners",
		[
			(party_slot_eq, "$current_town", 700, 0)
		],
		"Trade prisoners.",
		[
			(call_script, "script_party_prisoners_add_party_prisoners", "p_temp_party", "$current_town"),
			(call_script, "script_party_remove_all_prisoners", "$current_town"),
			(assign, "$g_next_menu", "mnu_lance_prison"),
			(change_screen_exchange_members, 1, "p_temp_party")
		], "."),

		("adjust_garrison",
		[
			(party_slot_eq, "$current_town", 700, 1)
		],
		"Inspect the garrison.",
		[
			(change_screen_exchange_members, 1)
		], "."),

		("garrison_control_player",
		[
			(party_slot_eq, "$current_town", 700, 0)
		],
		"Take control of the garrison (Warning: this will disband current garrison).",
		[
			(party_set_slot, "$current_town", 700, 1),
			(call_script, "script_party_remove_all_companions", "$current_town"),
			(try_begin),
				(neg|is_between, "$current_town", "p_castle_1_1", "p_village_1_1"),
				(call_script, "script_change_player_relation_with_center", "$current_town", -10),
				(display_message, "@The commoners are angry that you took away their rights!"),
				(play_sound, "snd_quest_failed"),
			(try_end)
		], "."),

		("garrison_control_ai",
		[
			(party_slot_eq, "$current_town", 700, 1)
		],
		"Give the control of the garrison to the town.(Warning: this will disband current garrison).",
		[
			(party_set_slot, "$current_town", 700, 0),
			(call_script, "script_party_remove_all_companions", "$current_town"),
			(call_script, "script_cf_reinforce_party", "$current_town"),
			(call_script, "script_cf_reinforce_party", "$current_town"),
			(call_script, "script_cf_reinforce_party", "$current_town"),
			(play_sound, "snd_quest_succeeded")
		], "."),

		("garrison_control_hire_local_merc",
		[
			(party_slot_eq, "$current_town", 700, 0),
			(party_slot_ge, "$current_town", 702, 1),
			(party_slot_ge, "$current_town", 703, 1),
			(assign, reg5, 3000)
		],
		"Hire local mercenaries to reinforce the garrison, cost: {reg5}",
		[
			(try_begin),
				(store_troop_gold, ":troop_gold_player", "trp_player"),
				(lt, ":troop_gold_player", reg5),
				(display_message, "@You do not have enough florins!", 0x00ff0000),
			(else_try),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_current_town", "$current_town"),
				(ge, ":party_size_wo_prisoners_current_town", 400),
				(display_message, "@Town garrison is full and can not hire additional men!", 0x00ff0000),
			(else_try),
				(troop_remove_gold, "trp_player", reg5),
				(party_get_slot, ":current_town_703", "$current_town", 703),
				(party_get_slot, ":current_town_704", "$current_town", 704),
				(val_sub, ":current_town_703", 1),
				(party_set_slot, "$current_town", 703, ":current_town_703"),
				(call_script, "script_fill_company", "$current_town", "$current_town", 702),
			(try_end)
		], "."),

		("garrison_control_hire_merc_1",
		[
			(party_slot_eq, "$current_town", 700, 0),
			(party_slot_ge, "$current_town", 705, 1),
			(party_slot_ge, "$current_town", 706, 1),
			(assign, reg6, 3000),
			(try_begin),
				(party_slot_eq, "$current_town", 705, 28),
				(str_store_string, 20, "@Geonese crossbowmen"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 23),
				(str_store_string, 20, "@Turcopoles"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 21),
				(str_store_string, 20, "@Georgians"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 24),
				(str_store_string, 20, "@Cumans"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 20),
				(str_store_string, 20, "@Brabantine"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 22),
				(str_store_string, 20, "@Sicilian Muslims"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 29),
				(str_store_string, 20, "@Welshmen"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 33),
				(str_store_string, 20, "@Kipchaks"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 32),
				(str_store_string, 20, "@Mordovians"),
			(else_try),
				(party_slot_eq, "$current_town", 705, 31),
				(str_store_string, 20, "@Khwarezmians"),
			(try_end)
		],
		"Hire {s20} mercenaries to reinforce the garrison, cost: {reg6}",
		[
			(try_begin),
				(store_troop_gold, ":troop_gold_player", "trp_player"),
				(lt, ":troop_gold_player", reg6),
				(display_message, "@You do not have enough florins!", 0x00ff0000),
			(else_try),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_current_town", "$current_town"),
				(ge, ":party_size_wo_prisoners_current_town", 400),
				(display_message, "@Town garrison is full and can not hire additional men!", 0x00ff0000),
			(else_try),
				(troop_remove_gold, "trp_player", reg6),
				(party_get_slot, ":current_town_706", "$current_town", 706),
				(party_get_slot, ":current_town_704", "$current_town", 704),
				(val_sub, ":current_town_706", 1),
				(party_set_slot, "$current_town", 706, ":current_town_706"),
				(call_script, "script_fill_company", "$current_town", "$current_town", 705),
			(try_end)
		], "."),

		("garrison_control_hire_merc_2",
		[
			(party_slot_eq, "$current_town", 700, 0),
			(party_slot_ge, "$current_town", 708, 1),
			(party_slot_ge, "$current_town", 709, 1),
			(assign, reg7, 3000),
			(try_begin),
				(party_slot_eq, "$current_town", 708, 53),
				(str_store_string, 21, "@The Knights Templar"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 52),
				(str_store_string, 21, "@The Knights Hospitalier"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 54),
				(str_store_string, 21, "@The Knights of Saint Lazarus"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 55),
				(str_store_string, 21, "@The Knights of Santiago"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 56),
				(str_store_string, 21, "@The Knights of Calatrava"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 57),
				(str_store_string, 21, "@The Knights of Saint Thomas of Acre"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 51),
				(str_store_string, 21, "@The Teutonic Knights"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 50),
				(str_store_string, 21, "@The Varangians"),
			(else_try),
				(party_slot_eq, "$current_town", 708, 30),
				(str_store_string, 21, "@The Mamluks"),
			(try_end)
		],
		"Hire {s21} to the town garrison, cost: {reg7}",
		[
			(try_begin),
				(store_troop_gold, ":troop_gold_player", "trp_player"),
				(lt, ":troop_gold_player", reg7),
				(display_message, "@You do not have enough florins!", 0x00ff0000),
			(else_try),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_current_town", "$current_town"),
				(ge, ":party_size_wo_prisoners_current_town", 400),
				(display_message, "@Town garrison is full and can not hire additional men!", 0x00ff0000),
			(else_try),
				(troop_remove_gold, "trp_player", reg7),
				(party_get_slot, ":current_town_709", "$current_town", 709),
				(party_get_slot, ":current_town_704", "$current_town", 704),
				(val_sub, ":current_town_709", 1),
				(party_set_slot, "$current_town", 709, ":current_town_709"),
				(call_script, "script_fill_company", "$current_town", "$current_town", 708),
			(try_end)
		], "."),

		("go_back",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_town")
		], ".")
	]
	),

	("mongol_camp", 0, "You come across a Mongolian Camp. {s10}",
"none",
	[
		(str_clear, 10),
		(party_get_slot, ":g_encountered_party_299", "$g_encountered_party", 299),
		(party_get_slot, ":g_encountered_party_299_town_lord", ":g_encountered_party_299", slot_town_lord),
		(call_script, "script_troop_get_player_relation", ":g_encountered_party_299_town_lord"),
		(store_faction_of_party, ":faction_of_party_g_encountered_party_299", ":g_encountered_party_299"),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(try_begin),
			(eq, ":faction_of_party_g_encountered_party_299", ":faction_of_party_g_encountered_party"),
			(str_store_troop_name, 0, ":g_encountered_party_299_town_lord"),
			(call_script, "script_troop_get_player_relation", ":g_encountered_party_299_town_lord"),
			(try_begin),
				(eq, "trp_player", ":g_encountered_party_299_town_lord"),
				(str_store_string, 10, "@You are the protector of this camp."),
			(else_try),
				(gt, reg0, 0),
				(str_store_string, 10, "@The camp is protected by {s0}. Because you have a positive relationship with him, he would not mind if you recruited some of the Mongols for your army."),
			(else_try),
				(str_store_string, 10, "@The camp is protected by {s0}. Because you have a bad relationship with him, he does not allow you to recruit the Mongols for your army."),
			(try_end),
		(try_end)
	],
	[
		("camp_walk",
		[
			(party_slot_eq, "$g_encountered_party", 301, 1),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0)
		],
		"Walk around the campsite.",
		[
			(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
			(party_get_current_terrain, ":current_terrain_l_g_encountered_party", "$g_encountered_party"),
			(try_begin),
				(this_or_next|eq, ":current_terrain_l_g_encountered_party", 4),
				(eq, ":current_terrain_l_g_encountered_party", 12),
				(assign, ":g_encountered_party_town_center", "scn_village_mongol_snow"),
			(else_try),
				(this_or_next|eq, ":current_terrain_l_g_encountered_party", 5),
				(eq, ":current_terrain_l_g_encountered_party", 13),
				(assign, ":g_encountered_party_town_center", "scn_village_mongol_desert"),
			(else_try),
				(this_or_next|eq, ":current_terrain_l_g_encountered_party", 3),
				(eq, ":current_terrain_l_g_encountered_party", 11),
				(assign, ":g_encountered_party_town_center", "scn_village_mongol_plains"),
			(try_end),
			(modify_visitors_at_site, ":g_encountered_party_town_center"),
			(reset_visitors),
			(set_visitor, 11, "trp_tatar_heavy_lancer"),
			(assign, "$current_town", "$g_encountered_party"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_0_troop, "trp_khergit_walker_1"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_1_troop, "trp_khergit_walker_2"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_2_troop, "trp_khergit_walker_1"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_3_troop, "trp_khergit_walker_2"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_4_troop, "trp_khergit_walker_1"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_5_troop, "trp_khergit_walker_2"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_6_troop, "trp_khergit_walker_1"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_7_troop, "trp_khergit_walker_2"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_8_troop, "trp_khergit_walker_1"),
			(party_set_slot, "$g_encountered_party", slot_center_walker_9_troop, "trp_khergit_walker_2"),
			(call_script, "script_init_town_walkers"),
			(set_jump_mission, "mt_village_center"),
			(assign, "$talk_context", 22),
			(jump_to_scene, ":g_encountered_party_town_center"),
			(change_screen_mission)
		], "."),

		("camp_recruit",
		[
			(party_get_slot, ":g_encountered_party_299", "$g_encountered_party", 299),
			(party_get_slot, ":g_encountered_party_299_town_lord", ":g_encountered_party_299", slot_town_lord),
			(call_script, "script_troop_get_player_relation", ":g_encountered_party_299_town_lord"),
			(this_or_next|gt, reg0, 0),
			(this_or_next|eq, ":g_encountered_party_299_town_lord", "trp_player"),
			(eq, "$cheat_mode", 1),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(ge, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0),
			(party_get_free_companions_capacity, ":free_companions_capacity_main_party", "p_main_party"),
			(ge, ":free_companions_capacity_main_party", 10),
			(party_get_slot, ":g_encountered_party_center_volunteer_troop_amount", "$g_encountered_party", slot_center_volunteer_troop_amount),
			(gt, ":g_encountered_party_center_volunteer_troop_amount", 0),
			(assign, reg1, ":g_encountered_party_center_volunteer_troop_amount"),
			(assign, reg5, 2000),
			(try_begin),
				(eq, ":g_encountered_party_299_town_lord", "trp_player"),
				(assign, reg5, 500),
			(try_end),
			(str_store_string, 1, "@Cost: {reg5}"),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(ge, ":troop_gold_player", reg5)
		],
		"Recruit some Tribesman {s1}. (Available: {reg1})",
		[
			(party_get_slot, ":g_encountered_party_center_volunteer_troop_amount", "$g_encountered_party", slot_center_volunteer_troop_amount),
			(val_sub, ":g_encountered_party_center_volunteer_troop_amount", 1),
			(party_set_slot, "$g_encountered_party", slot_center_volunteer_troop_amount, ":g_encountered_party_center_volunteer_troop_amount"),
			(call_script, "script_fill_lance", "$g_encountered_party", "p_main_party"),
			(try_begin),
				(gt, reg5, 0),
				(troop_remove_gold, "trp_player", reg5),
			(try_end),
			(jump_to_menu, "mnu_mongol_camp")
		], "."),

		("camp_attack",
		[],
		"Burn it! Burn them all! Attack the camp!",
		[
			(party_get_slot, ":g_encountered_party_299", "$g_encountered_party", 299),
			(party_get_slot, ":g_encountered_party_299_town_lord", ":g_encountered_party_299", slot_town_lord),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(jump_to_menu, "mnu_simple_encounter")
		], "."),

		("manor_leave",
		[],
		"Leave.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("inspect_property", 0, "'House!",
"none",
	[],
	[
		("build",
		[],
		"Build",
		[
			(start_presentation, "prsnt_economy_build")
		], "."),

		("visit_house",
		[
			(eq, 0, 1)
		],
		"Go to your house",
		[
			(modify_visitors_at_site, "scn_town_house_euro"),
			(reset_visitors),
			(mission_tpl_entry_set_override_flags, "mt_home_visit", 0, 256),
			(set_visitor, 0, "trp_player"),
			(assign, ":var_1", 3),
			(set_visitor, ":var_1", "trp_maid_1"),
			(set_jump_mission, "mt_home_visit"),
			(jump_to_scene, "scn_town_house_euro"),
			(change_screen_mission)
		], "."),

		("buy_house",
		[
			(eq, 0, 1)
		],
		"Buy a house in this town, cost: {reg1}",
		[], "."),

		("recruit_maid",
		[
			(eq, 0, 1)
		],
		"Recruit a housemaid for the ",
		[
			(change_screen_view_character)
		], "."),

		("leave",
		[],
		"Nevermind.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("disband_lances", 0, "Do you really want to disband your feudal forces? (This will only affect forces that were recruited in fief lances.)",
"none",
	[],
	[
		("disband",
		[],
		"Yes! The peasants emit a strong, foul odour... Reward the nobles though!",
		[
			(call_script, "script_balance_lance_storage"),
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(try_for_range, ":globalvariable", 0, "$lance_troop_serving"),
					(troop_get_slot, ":lances_places_globalvariable", "trp_lances_places", ":globalvariable"),
					(troop_get_slot, ":lances_troops_globalvariable", "trp_lances_troops", ":globalvariable"),
					(eq, ":party", ":lances_places_globalvariable"),
					(main_party_has_troop, ":lances_troops_globalvariable"),
					(troop_set_slot, "trp_lances_troops_reserve", "$lance_troop_reserve", ":lances_troops_globalvariable"),
					(troop_set_slot, "trp_lances_places_reserve", "$lance_troop_reserve", ":lances_places_globalvariable"),
					(troop_set_slot, "trp_lances_troops", ":globalvariable", 0),
					(troop_set_slot, "trp_lances_places", ":globalvariable", 0),
					(val_add, "$lance_troop_reserve", 1),
					(party_remove_members, "p_main_party", ":lances_troops_globalvariable", 1),
					(party_get_slot, ":lances_places_globalvariable_716", ":lances_places_globalvariable", 716),
					(val_add, ":lances_places_globalvariable_716", 1),
					(party_set_slot, ":lances_places_globalvariable", 716, ":lances_places_globalvariable_716"),
				(try_end),
			(try_end),
			(call_script, "script_balance_lance_storage"),
			(try_for_range, ":globalvariable", 0, "$lance_troop_serving"),
				(troop_get_slot, ":lances_places_globalvariable", "trp_lances_places", ":globalvariable"),
				(troop_get_slot, ":lances_troops_globalvariable", "trp_lances_troops", ":globalvariable"),
				(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
					(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
					(is_between, ":party_stack_troop_id_main_party_localvariable", 110, 439),
					(assign, reg10, -1),
					(call_script, "script_troop_tree_search", ":party_stack_troop_id_main_party_localvariable", ":lances_troops_globalvariable"),
					(ge, reg10, ":party_stack_troop_id_main_party_localvariable"),
					(assign, ":num_companion_stacks_main_party", -1),
				(try_end),
				(ge, reg10, 0),
				(troop_set_slot, "trp_lances_troops", ":globalvariable", 0),
				(troop_set_slot, "trp_lances_places", ":globalvariable", 0),
				(troop_set_slot, "trp_lances_troops_reserve", "$lance_troop_reserve", reg10),
				(troop_set_slot, "trp_lances_places_reserve", "$lance_troop_reserve", ":lances_places_globalvariable"),
				(party_remove_members, "p_main_party", reg10, 1),
				(party_get_slot, ":lances_places_globalvariable_716", ":lances_places_globalvariable", 716),
				(val_add, ":lances_places_globalvariable_716", 1),
				(party_set_slot, ":lances_places_globalvariable", 716, ":lances_places_globalvariable_716"),
				(val_add, "$lance_troop_reserve", 1),
			(try_end),
			(call_script, "script_balance_lance_storage"),
			(call_script, "script_party_copy", "p_temp_casualties", "p_main_party"),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_temp_casualties"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_temp_casualties", ":localvariable"),
				(is_between, ":party_stack_troop_id_main_party_localvariable", 110, 439),
				(party_stack_get_size, ":party_stack_size_temp_casualties_localvariable", "p_temp_casualties", ":localvariable"),
				(try_for_range, reg2, 0, ":party_stack_size_temp_casualties_localvariable"),
					(try_for_range, ":lances_places_globalvariable", "p_town_1_1", "p_salt_mine"),
						(party_slot_eq, ":lances_places_globalvariable", slot_town_lord, "trp_player"),
						(troop_set_slot, "trp_lances_troops_reserve", "$lance_troop_reserve", ":party_stack_troop_id_main_party_localvariable"),
						(troop_set_slot, "trp_lances_places_reserve", "$lance_troop_reserve", ":lances_places_globalvariable"),
						(val_add, "$lance_troop_reserve", 1),
						(party_remove_members, "p_main_party", ":party_stack_troop_id_main_party_localvariable", 1),
						(party_get_slot, ":lances_places_globalvariable_716", ":lances_places_globalvariable", 716),
						(val_add, ":lances_places_globalvariable_716", 1),
						(party_set_slot, ":lances_places_globalvariable", 716, ":lances_places_globalvariable_716"),
					(try_end),
				(try_end),
			(try_end),
			(call_script, "script_balance_lance_storage"),
			(call_script, "script_count_nobles_commoners_for_center"),
			(assign, "$lance_troop_serving", 0),
			(jump_to_menu, "$g_next_menu")
		], "."),

		("leave",
		[],
		"No. I'd rather burn a village or two instead!",
		[
			(jump_to_menu, "$g_next_menu")
		], ".")
	]
	),

	("recruit_companions", 0, "what? Companion maker mk1.0",
"none",
	[
		(set_player_troop, "trp_player")
	],
	[
		("recruit_noble",
		[],
		"Recruit a local noble to your party",
		[], "."),

		("recruit_priest",
		[],
		"Recruit a holy man to your party",
		[
			(change_screen_view_character)
		], "."),

		("recruit_trainer",
		[],
		"Recruit an experienced troop trainer",
		[], "."),

		("recruit_trader",
		[],
		"Recruit a fat local merchant",
		[], "."),

		("recruit_pathfinder",
		[],
		"Recruit an experienced pathfinder",
		[], "."),

		("manor_leave",
		[],
		"Nevermind.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("world_map_soldier", 0, "What do you need to do soldier?",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_world_map"),
		(troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party),
		(try_begin),
			(eq, "$culture_pool_initialized", 1),
			(eq, "$culture_pool", 1),
			(call_script, "script_rebalance_troops_by_culture"),
		(try_end)
	],
	[
		("join_commander_battle",
		[
			(party_get_battle_opponent, ":battle_opponent_l_enlisted_party", "$enlisted_party"),
			(gt, ":battle_opponent_l_enlisted_party", 0)
		],
		"Follow the commander into battle.",
		[
			(party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 1),
			(try_begin),
				(neg|troop_is_guarantee_horse, "$player_cur_troop"),
				(troop_get_inventory_slot, ":inventory_slot_player_8", "trp_player", 8),
				(gt, ":inventory_slot_player_8", 0),
				(troop_get_inventory_slot_modifier, ":inventory_slot_modifier_player_8", "trp_player", 8),
				(set_show_messages, 0),
				(troop_add_item, "trp_player", ":inventory_slot_player_8", ":inventory_slot_modifier_player_8"),
				(troop_set_inventory_slot, "trp_player", 8, -1),
				(set_show_messages, 1),
			(try_end),
			(start_encounter, "$enlisted_party"),
			(change_screen_map)
		], "."),

		("enter_town",
		[
			(party_is_in_any_town, "$enlisted_party")
		],
		"Enter stationed town.",
		[
			(party_get_cur_town, ":cur_town_l_enlisted_party", "$enlisted_party"),
			(start_encounter, ":cur_town_l_enlisted_party"),
			(change_screen_map)
		], "."),

		("commander",
		[
			(party_get_battle_opponent, ":battle_opponent_l_enlisted_party", "$enlisted_party"),
			(lt, ":battle_opponent_l_enlisted_party", 0)
		],
		"Request audience with your commander.",
		[
			(jump_to_menu, "mnu_commander_aud")
		], "."),

		("revolt",
		[],
		"Revolt against the commander!",
		[
			(jump_to_menu, "mnu_ask_revolt")
		], "."),

		("desert",
		[],
		"Desert the army.(keep equipment but lose relations)",
		[
			(jump_to_menu, "mnu_ask_desert")
		], "."),

		("report",
		[],
		"Commander's Report",
		[
			(start_presentation, "prsnt_taragoth_lords_report")
		], "."),

		("return_to_duty",
		[
			(party_get_battle_opponent, ":battle_opponent_l_enlisted_party", "$enlisted_party"),
			(this_or_next|lt, ":battle_opponent_l_enlisted_party", 0),
			(troop_is_wounded, "trp_player")
		],
		"Return to duty.",
		[
			(change_screen_map),
			(assign, "$g_infinite_camping", 1),
			(rest_for_hours_interactive, 8760, 5, 1)
		], ".")
	]
	),

	("commander_aud", 0, "Your request for a meeting is relayed to your commander's camp, and finally {s6} appears from his tent to speak with you.",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_world_map"),
		(str_store_troop_name, 6, "$enlisted_lord")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(try_begin),
				(neg|party_is_in_any_town, "$enlisted_party"),
				(start_encounter, "$enlisted_party"),
				(change_screen_map),
			(else_try),
				(assign, "$g_encountered_party", "$enlisted_party"),
				(store_faction_of_party, "$g_encountered_party_faction", "$g_encountered_party"),
				(store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
				(party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
				(party_get_template_id, "$g_encountered_party_template", "$g_encountered_party"),
				(assign, "$talk_context", 2),
				(call_script, "script_setup_party_meeting", "$g_encountered_party"),
			(try_end)
		], "."),

		("reject_talk_lord",
		[],
		"No, nevermind.",
		[
			(change_screen_map)
		], ".")
	]
	),

	("ask_revolt", 0, "Are you sure you want to revolt?",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_rebel"),
		(str_store_troop_name, 6, "$enlisted_lord")
	],
	[
		("confirm_revolt",
		[],
		"Yes, {s6} will be the death of us all, it is time to act!",
		[
			(jump_to_menu, "mnu_revolt")
		], "."),

		("reject_revolt",
		[],
		"No, I am loyal to {s6}.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("revolt", 0, "Do you want to release the prisoners to help your men?",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_rebel"),
		(assign, "$cant_leave_encounter", 1),
		(call_script, "script_freelancer_detach_party"),
		(call_script, "script_event_player_deserts"),
		(call_script, "script_get_desert_troops"),
		(call_script, "script_change_player_relation_with_troop", "$enlisted_lord", -10),
		(store_faction_of_troop, ":faction_of_troop_enlisted_lord", "$enlisted_lord"),
		(try_begin),
			(party_get_battle_opponent, ":battle_opponent_l_enlisted_party", "$enlisted_party"),
			(gt, ":battle_opponent_l_enlisted_party", 0),
			(store_faction_of_party, ":faction_of_party_battle_opponent_l_enlisted_party", ":battle_opponent_l_enlisted_party"),
			(store_relation, ":relation_faction_of_party_battle_opponent_l_enlisted_party_faction_of_troop_enlisted_lord", ":faction_of_party_battle_opponent_l_enlisted_party", ":faction_of_troop_enlisted_lord"),
			(store_sub, ":value", 100, ":relation_faction_of_party_battle_opponent_l_enlisted_party_faction_of_troop_enlisted_lord"),
			(val_add, ":value", 5),
			(call_script, "script_change_player_relation_with_faction_ex", ":faction_of_troop_enlisted_lord", ":value"),
		(try_end)
	],
	[
		("revolt_prisoners",
		[],
		"Yes, I will take the risk for a greater advantage.",
		[
			(party_clear, "p_temp_party_2"),
			(party_get_num_prisoner_stacks, ":num_prisoner_stacks_l_enlisted_party", "$enlisted_party"),
			(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_l_enlisted_party"),
				(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_enlisted_party_localvariable", "$enlisted_party", ":localvariable"),
				(ge, ":party_prisoner_stack_troop_id_enlisted_party_localvariable", 1),
				(party_prisoner_stack_get_size, ":party_prisoner_stack_size_enlisted_party_localvariable", "$enlisted_party", ":localvariable"),
				(party_remove_prisoners, "$enlisted_party", ":party_prisoner_stack_troop_id_enlisted_party_localvariable", ":party_prisoner_stack_size_enlisted_party_localvariable"),
				(party_add_members, "p_temp_party_2", ":party_prisoner_stack_troop_id_enlisted_party_localvariable", ":party_prisoner_stack_size_enlisted_party_localvariable"),
			(try_end),
			(party_attach_to_party, "p_temp_party_2", "p_main_party"),
			(start_encounter, "$enlisted_party"),
			(change_screen_map)
		], "."),

		("revolt_no_prisoners",
		[],
		"No, I don't trust prisoners.",
		[
			(start_encounter, "$enlisted_party"),
			(change_screen_map)
		], ".")
	]
	),

	("ask_desert", 0, "Do you want to desert?",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_desert")
	],
	[
		("confirm_desert",
		[],
		"Yes, this is pointless.",
		[
			(jump_to_menu, "mnu_desert")
		], "."),

		("reject_desert",
		[],
		"No, I am loyal to my commander.",
		[
			(change_screen_return)
		], ".")
	]
	),

	("desert", 0, "While in the army you've made some good friends. Some could possibly follow you.",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_desert"),
		(call_script, "script_freelancer_detach_party"),
		(call_script, "script_event_player_deserts")
	],
	[
		("desert_party",
		[],
		"Try to convince them to follow you.",
		[
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(try_begin),
				(eq, ":random_in_range_0_4", 0),
				(assign, "$g_encountered_party", "$enlisted_party"),
				(jump_to_menu, "mnu_captivity_start_wilderness"),
			(else_try),
				(call_script, "script_get_desert_troops"),
				(call_script, "script_party_restore"),
				(call_script, "script_set_parties_around_player_ignore_player", 2, 4),
			(try_end),
			(change_screen_map),
			(display_message, "@You have deserted and are now wanted!"),
			(call_script, "script_desert_order")
		], "."),

		("desert_alone",
		[],
		"No, I have a better chance alone.",
		[
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(try_begin),
				(eq, ":random_in_range_0_10", 0),
				(assign, "$g_encountered_party", "$enlisted_party"),
				(jump_to_menu, "mnu_captivity_start_wilderness"),
			(else_try),
				(call_script, "script_party_restore"),
				(call_script, "script_set_parties_around_player_ignore_player", 2, 4),
			(try_end),
			(change_screen_map),
			(display_message, "@You have deserted and are now wanted!"),
			(call_script, "script_desert_order")
		], ".")
	]
	),

	("upgrade_path", 0, "In recognition of your excellent service, you have been promoted.",
"none",
	[
		(set_background_mesh, "mesh_pic_soldier_world_map"),
		(call_script, "script_freelancer_unequip_troop", "$player_cur_troop")
	],
	[
		("upgrade_path_1",
		[
			(troop_get_upgrade_troop, ":upgrade_troop_player_cur_troop_0", "$player_cur_troop", 0),
			(ge, ":upgrade_troop_player_cur_troop_0", 0),
			(str_store_troop_name, 66, ":upgrade_troop_player_cur_troop_0")
		],
		"{s66}",
		[
			(troop_get_upgrade_troop, "$player_cur_troop", "$player_cur_troop", 0),
			(store_faction_of_troop, ":faction_of_troop_enlisted_lord", "$enlisted_lord"),
			(faction_set_slot, ":faction_of_troop_enlisted_lord", 301, "$player_cur_troop"),
			(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
			(str_store_troop_name, 5, "$player_cur_troop"),
			(str_store_string, 5, "@Current rank: {s5}"),
			(add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, 5, 1),
			(change_screen_map)
		], "."),

		("upgrade_path_2",
		[
			(troop_get_upgrade_troop, ":upgrade_troop_player_cur_troop_1", "$player_cur_troop", 1),
			(ge, ":upgrade_troop_player_cur_troop_1", 1),
			(str_store_troop_name, 67, ":upgrade_troop_player_cur_troop_1")
		],
		"{s67}",
		[
			(troop_get_upgrade_troop, "$player_cur_troop", "$player_cur_troop", 1),
			(store_faction_of_troop, ":faction_of_troop_enlisted_lord", "$enlisted_lord"),
			(faction_set_slot, ":faction_of_troop_enlisted_lord", 301, "$player_cur_troop"),
			(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
			(str_store_troop_name, 5, "$player_cur_troop"),
			(str_store_string, 5, "@Current rank: {s5}"),
			(add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, 5, 1),
			(change_screen_map)
		], ".")
	]
	),

	("choose_scenes_0", 0, "Choose a scene: (Page 1 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_13")
		], "."),

		("choose_scene_0",
		[],
		"1257 combat euro 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_1",
		[],
		"1257 combat euro 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_2",
		[],
		"1257 combat euro 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_3",
		[],
		"1257 combat euro 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_4",
		[],
		"1257 combat euro hillside 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_hillside_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_5",
		[],
		"1257 combat euro hillside 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_hillside_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_6",
		[],
		"1257 combat euro hillside 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_hillside_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_7",
		[],
		"1257 combat euro hillside 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_hillside_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_8",
		[],
		"1257 combat euro hillside 4: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_euro_hillside_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_9",
		[],
		"1257 combat forest 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_forest_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_10",
		[],
		"1257 combat iberian 0: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_1257_combat_iberian_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_11",
		[],
		"1257 combat iberian hillside 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_12",
		[],
		"1257 combat iberian hillside 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_1"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_13", 0, "Choose a scene: (Page 2 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_26")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_0")
		], "."),

		("choose_scene_13",
		[],
		"1257 combat iberian hillside 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_14",
		[],
		"1257 combat iberian hillside 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_15",
		[],
		"1257 combat iberian hillside 4: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_16",
		[],
		"1257 combat iberian hillside 5: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_17",
		[],
		"1257 combat iberian hillside 6: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_18",
		[],
		"1257 combat iberian hillside 7: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_19",
		[],
		"1257 combat iberian hillside 8: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_iberian_hillside_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_20",
		[],
		"1257 combat mountain 0: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_21",
		[],
		"1257 combat mountain 1: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_22",
		[],
		"1257 combat mountain 2: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_23",
		[],
		"1257 combat mountain 3: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_24",
		[],
		"1257 combat mountain 4: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_25",
		[],
		"1257 combat mountain 5: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_5"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_26", 0, "Choose a scene: (Page 3 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_39")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_13")
		], "."),

		("choose_scene_26",
		[],
		"1257 combat mountain 6: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_27",
		[],
		"1257 combat mountain 7: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_28",
		[],
		"1257 combat mountain 8: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_29",
		[],
		"1257 combat mountain 9: generate",
		[
			(jump_to_scene, "scn_1257_combat_mountain_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_30",
		[],
		"1257 combat mountain desert 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_mountain_desert_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_31",
		[],
		"1257 combat mountain desert 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_mountain_desert_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_32",
		[],
		"1257 combat river 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_river_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_33",
		[],
		"1257 combat rocky desert 0: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_1257_combat_rocky_desert_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_34",
		[],
		"1257 combat snow 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_35",
		[],
		"1257 combat snow 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_36",
		[],
		"1257 combat snow 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_37",
		[],
		"1257 combat snow 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_38",
		[],
		"1257 combat snow 4: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_4"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_39", 0, "Choose a scene: (Page 4 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_52")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_26")
		], "."),

		("choose_scene_39",
		[],
		"1257 combat snow 5: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_40",
		[],
		"1257 combat snow 6: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_41",
		[],
		"1257 combat snow 7: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_snow_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_42",
		[],
		"1257 combat steppe 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_steppe_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_43",
		[],
		"1257 combat steppe 1: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_1257_combat_steppe_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_44",
		[],
		"1257 combat steppe 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_steppe_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_45",
		[],
		"1257 combat steppe 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_steppe_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_46",
		[],
		"1257 combat swamp 0: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_0"),
			(change_screen_mission)
		], "."),

		("choose_scene_47",
		[],
		"1257 combat swamp 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_48",
		[],
		"1257 combat swamp 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_49",
		[],
		"1257 combat swamp 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_50",
		[],
		"1257 combat swamp 4: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_51",
		[],
		"1257 combat swamp 5: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_5"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_52", 0, "Choose a scene: (Page 5 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_65")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_39")
		], "."),

		("choose_scene_52",
		[],
		"1257 combat swamp 6: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_53",
		[],
		"1257 combat swamp 7: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_54",
		[],
		"1257 combat swamp 8: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_55",
		[],
		"1257 combat swamp 9: generate|auto entry points",
		[
			(jump_to_scene, "scn_1257_combat_swamp_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_56",
		[],
		"aachen center: generate",
		[
			(jump_to_scene, "scn_aachen_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_57",
		[],
		"aachen walls: generate",
		[
			(jump_to_scene, "scn_aachen_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_58",
		[],
		"acre center: generate",
		[
			(jump_to_scene, "scn_acre_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_59",
		[],
		"acre walls: generate",
		[
			(jump_to_scene, "scn_acre_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_60",
		[],
		"aleppo center: generate",
		[
			(jump_to_scene, "scn_aleppo_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_61",
		[],
		"aleppo walls: generate",
		[
			(jump_to_scene, "scn_aleppo_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_62",
		[],
		"bristol center: generate",
		[
			(jump_to_scene, "scn_bristol_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_63",
		[],
		"bristol walls: generate",
		[
			(jump_to_scene, "scn_bristol_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_64",
		[],
		"byzantine castle: generate",
		[
			(jump_to_scene, "scn_byzantine_castle"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_65", 0, "Choose a scene: (Page 6 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_78")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_52")
		], "."),

		("choose_scene_65",
		[],
		"byzantine center: generate",
		[
			(jump_to_scene, "scn_byzantine_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_66",
		[],
		"byzantine walls belfry: generate",
		[
			(jump_to_scene, "scn_byzantine_walls_belfry"),
			(change_screen_mission)
		], "."),

		("choose_scene_67",
		[],
		"byzantine walls one ladder: generate",
		[
			(jump_to_scene, "scn_byzantine_walls_one_ladder"),
			(change_screen_mission)
		], "."),

		("choose_scene_68",
		[],
		"camp scene: generate|auto entry points",
		[
			(jump_to_scene, "scn_camp_scene"),
			(change_screen_mission)
		], "."),

		("choose_scene_69",
		[],
		"camp scene horse track: generate|auto entry points",
		[
			(jump_to_scene, "scn_camp_scene_horse_track"),
			(change_screen_mission)
		], "."),

		("choose_scene_70",
		[],
		"campside desert: generate",
		[
			(jump_to_scene, "scn_campside_desert"),
			(change_screen_mission)
		], "."),

		("choose_scene_71",
		[],
		"campside mongol: generate",
		[
			(jump_to_scene, "scn_campside_mongol"),
			(change_screen_mission)
		], "."),

		("choose_scene_72",
		[],
		"campside plain: generate",
		[
			(jump_to_scene, "scn_campside_plain"),
			(change_screen_mission)
		], "."),

		("choose_scene_73",
		[],
		"campside snow: generate",
		[
			(jump_to_scene, "scn_campside_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_74",
		[],
		"campside steppe: generate",
		[
			(jump_to_scene, "scn_campside_steppe"),
			(change_screen_mission)
		], "."),

		("choose_scene_75",
		[],
		"castle 11 exterior: generate",
		[
			(jump_to_scene, "scn_castle_11_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_76",
		[],
		"castle 11 interior: indoors",
		[
			(jump_to_scene, "scn_castle_11_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_77",
		[],
		"castle 11 prison: indoors",
		[
			(jump_to_scene, "scn_castle_11_prison"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_78", 0, "Choose a scene: (Page 7 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_91")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_65")
		], "."),

		("choose_scene_78",
		[],
		"castle 12 exterior: generate",
		[
			(jump_to_scene, "scn_castle_12_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_79",
		[],
		"castle 12 interior: indoors",
		[
			(jump_to_scene, "scn_castle_12_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_80",
		[],
		"castle 12 prison: indoors",
		[
			(jump_to_scene, "scn_castle_12_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_81",
		[],
		"castle 13 exterior: generate",
		[
			(jump_to_scene, "scn_castle_13_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_82",
		[],
		"castle 13 interior: indoors",
		[
			(jump_to_scene, "scn_castle_13_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_83",
		[],
		"castle 13 prison: indoors",
		[
			(jump_to_scene, "scn_castle_13_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_84",
		[],
		"castle 15 exterior: generate",
		[
			(jump_to_scene, "scn_castle_15_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_85",
		[],
		"castle 15 interior: indoors",
		[
			(jump_to_scene, "scn_castle_15_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_86",
		[],
		"castle 15 prison: indoors",
		[
			(jump_to_scene, "scn_castle_15_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_87",
		[],
		"castle 17 exterior: generate",
		[
			(jump_to_scene, "scn_castle_17_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_88",
		[],
		"castle 17 interior: indoors",
		[
			(jump_to_scene, "scn_castle_17_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_89",
		[],
		"castle 17 prison: indoors",
		[
			(jump_to_scene, "scn_castle_17_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_90",
		[],
		"castle 18 exterior: generate",
		[
			(jump_to_scene, "scn_castle_18_exterior"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_91", 0, "Choose a scene: (Page 8 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_104")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_78")
		], "."),

		("choose_scene_91",
		[],
		"castle 18 interior: indoors",
		[
			(jump_to_scene, "scn_castle_18_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_92",
		[],
		"castle 18 prison: indoors",
		[
			(jump_to_scene, "scn_castle_18_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_93",
		[],
		"castle 19 exterior: generate",
		[
			(jump_to_scene, "scn_castle_19_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_94",
		[],
		"castle 19 interior: indoors",
		[
			(jump_to_scene, "scn_castle_19_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_95",
		[],
		"castle 19 prison: indoors",
		[
			(jump_to_scene, "scn_castle_19_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_96",
		[],
		"castle 1 exterior: generate",
		[
			(jump_to_scene, "scn_castle_1_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_97",
		[],
		"castle 1 interior: indoors",
		[
			(jump_to_scene, "scn_castle_1_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_98",
		[],
		"castle 1 prison: indoors",
		[
			(jump_to_scene, "scn_castle_1_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_99",
		[],
		"castle 20 exterior: generate",
		[
			(jump_to_scene, "scn_castle_20_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_100",
		[],
		"castle 20 interior: indoors",
		[
			(jump_to_scene, "scn_castle_20_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_101",
		[],
		"castle 20 prison: indoors",
		[
			(jump_to_scene, "scn_castle_20_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_102",
		[],
		"castle 21 exterior: generate",
		[
			(jump_to_scene, "scn_castle_21_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_103",
		[],
		"castle 21 interior: indoors",
		[
			(jump_to_scene, "scn_castle_21_interior"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_104", 0, "Choose a scene: (Page 9 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_117")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_91")
		], "."),

		("choose_scene_104",
		[],
		"castle 21 prison: indoors",
		[
			(jump_to_scene, "scn_castle_21_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_105",
		[],
		"castle 22 exterior: generate",
		[
			(jump_to_scene, "scn_castle_22_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_106",
		[],
		"castle 22 interior: indoors",
		[
			(jump_to_scene, "scn_castle_22_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_107",
		[],
		"castle 22 prison: indoors",
		[
			(jump_to_scene, "scn_castle_22_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_108",
		[],
		"castle 23 exterior: generate",
		[
			(jump_to_scene, "scn_castle_23_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_109",
		[],
		"castle 23 interior: indoors",
		[
			(jump_to_scene, "scn_castle_23_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_110",
		[],
		"castle 23 prison: indoors",
		[
			(jump_to_scene, "scn_castle_23_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_111",
		[],
		"castle 29 exterior: generate",
		[
			(jump_to_scene, "scn_castle_29_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_112",
		[],
		"castle 29 interior: indoors",
		[
			(jump_to_scene, "scn_castle_29_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_113",
		[],
		"castle 29 prison: indoors",
		[
			(jump_to_scene, "scn_castle_29_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_114",
		[],
		"castle 2 exterior: generate",
		[
			(jump_to_scene, "scn_castle_2_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_115",
		[],
		"castle 2 interior: indoors",
		[
			(jump_to_scene, "scn_castle_2_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_116",
		[],
		"castle 2 prison: indoors",
		[
			(jump_to_scene, "scn_castle_2_prison"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_117", 0, "Choose a scene: (Page 10 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_130")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_104")
		], "."),

		("choose_scene_117",
		[],
		"castle 37 exterior: generate",
		[
			(jump_to_scene, "scn_castle_37_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_118",
		[],
		"castle 37 interior: indoors",
		[
			(jump_to_scene, "scn_castle_37_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_119",
		[],
		"castle 37 prison: indoors",
		[
			(jump_to_scene, "scn_castle_37_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_120",
		[],
		"castle 39 exterior: generate",
		[
			(jump_to_scene, "scn_castle_39_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_121",
		[],
		"castle 39 interior: indoors",
		[
			(jump_to_scene, "scn_castle_39_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_122",
		[],
		"castle 39 prison: indoors",
		[
			(jump_to_scene, "scn_castle_39_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_123",
		[],
		"castle 3 exterior: generate",
		[
			(jump_to_scene, "scn_castle_3_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_124",
		[],
		"castle 3 interior: indoors",
		[
			(jump_to_scene, "scn_castle_3_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_125",
		[],
		"castle 3 prison: indoors",
		[
			(jump_to_scene, "scn_castle_3_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_126",
		[],
		"castle 42 exterior: generate",
		[
			(jump_to_scene, "scn_castle_42_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_127",
		[],
		"castle 42 interior: indoors",
		[
			(jump_to_scene, "scn_castle_42_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_128",
		[],
		"castle 42 prison: indoors",
		[
			(jump_to_scene, "scn_castle_42_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_129",
		[],
		"castle 43 exterior: generate",
		[
			(jump_to_scene, "scn_castle_43_exterior"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_130", 0, "Choose a scene: (Page 11 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_143")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_117")
		], "."),

		("choose_scene_130",
		[],
		"castle 43 interior: indoors",
		[
			(jump_to_scene, "scn_castle_43_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_131",
		[],
		"castle 43 prison: indoors",
		[
			(jump_to_scene, "scn_castle_43_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_132",
		[],
		"castle 45 exterior: generate",
		[
			(jump_to_scene, "scn_castle_45_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_133",
		[],
		"castle 45 interior: indoors",
		[
			(jump_to_scene, "scn_castle_45_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_134",
		[],
		"castle 45 prison: indoors",
		[
			(jump_to_scene, "scn_castle_45_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_135",
		[],
		"castle 46 exterior: generate",
		[
			(jump_to_scene, "scn_castle_46_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_136",
		[],
		"castle 46 interior: indoors",
		[
			(jump_to_scene, "scn_castle_46_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_137",
		[],
		"castle 46 prison: indoors",
		[
			(jump_to_scene, "scn_castle_46_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_138",
		[],
		"castle 47 exterior: generate",
		[
			(jump_to_scene, "scn_castle_47_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_139",
		[],
		"castle 47 interior: indoors",
		[
			(jump_to_scene, "scn_castle_47_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_140",
		[],
		"castle 47 prison: indoors",
		[
			(jump_to_scene, "scn_castle_47_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_141",
		[],
		"castle 9 exterior: generate",
		[
			(jump_to_scene, "scn_castle_9_exterior"),
			(change_screen_mission)
		], "."),

		("choose_scene_142",
		[],
		"castle 9 interior: indoors",
		[
			(jump_to_scene, "scn_castle_9_interior"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_143", 0, "Choose a scene: (Page 12 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_156")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_130")
		], "."),

		("choose_scene_143",
		[],
		"castle 9 prison: indoors",
		[
			(jump_to_scene, "scn_castle_9_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_144",
		[],
		"castle cold: generate",
		[
			(jump_to_scene, "scn_castle_cold"),
			(change_screen_mission)
		], "."),

		("choose_scene_145",
		[],
		"castle interior arab: indoors",
		[
			(jump_to_scene, "scn_castle_interior_arab"),
			(change_screen_mission)
		], "."),

		("choose_scene_146",
		[],
		"castle interior byz: indoors",
		[
			(jump_to_scene, "scn_castle_interior_byz"),
			(change_screen_mission)
		], "."),

		("choose_scene_147",
		[],
		"castle interior eastern: indoors",
		[
			(jump_to_scene, "scn_castle_interior_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_148",
		[],
		"castle interior euro: indoors",
		[
			(jump_to_scene, "scn_castle_interior_euro"),
			(change_screen_mission)
		], "."),

		("choose_scene_149",
		[],
		"castle interior iberia: indoors",
		[
			(jump_to_scene, "scn_castle_interior_iberia"),
			(change_screen_mission)
		], "."),

		("choose_scene_150",
		[],
		"castle interior italy: indoors",
		[
			(jump_to_scene, "scn_castle_interior_italy"),
			(change_screen_mission)
		], "."),

		("choose_scene_151",
		[],
		"castle interior mongol: indoors",
		[
			(jump_to_scene, "scn_castle_interior_mongol"),
			(change_screen_mission)
		], "."),

		("choose_scene_152",
		[],
		"castle interior nordic: indoors",
		[
			(jump_to_scene, "scn_castle_interior_nordic"),
			(change_screen_mission)
		], "."),

		("choose_scene_153",
		[],
		"castle mike random: generate",
		[
			(jump_to_scene, "scn_castle_mike_random"),
			(change_screen_mission)
		], "."),

		("choose_scene_154",
		[],
		"castle player nordic 1: generate",
		[
			(jump_to_scene, "scn_castle_player_nordic_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_155",
		[],
		"castle player nordic 2: generate",
		[
			(jump_to_scene, "scn_castle_player_nordic_2"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_156", 0, "Choose a scene: (Page 13 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_169")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_143")
		], "."),

		("choose_scene_156",
		[],
		"castle player nordic 3: generate",
		[
			(jump_to_scene, "scn_castle_player_nordic_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_157",
		[],
		"castle prison arab: indoors",
		[
			(jump_to_scene, "scn_castle_prison_arab"),
			(change_screen_mission)
		], "."),

		("choose_scene_158",
		[],
		"castle prison eastern: indoors",
		[
			(jump_to_scene, "scn_castle_prison_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_159",
		[],
		"castle prison euro: indoors",
		[
			(jump_to_scene, "scn_castle_prison_euro"),
			(change_screen_mission)
		], "."),

		("choose_scene_160",
		[],
		"castle prison iberia: indoors",
		[
			(jump_to_scene, "scn_castle_prison_iberia"),
			(change_screen_mission)
		], "."),

		("choose_scene_161",
		[],
		"castle prison italy: indoors",
		[
			(jump_to_scene, "scn_castle_prison_italy"),
			(change_screen_mission)
		], "."),

		("choose_scene_162",
		[],
		"castle prison mongol: indoors",
		[
			(jump_to_scene, "scn_castle_prison_mongol"),
			(change_screen_mission)
		], "."),

		("choose_scene_163",
		[],
		"castle prison nordic: indoors",
		[
			(jump_to_scene, "scn_castle_prison_nordic"),
			(change_screen_mission)
		], "."),

		("choose_scene_164",
		[],
		"castle walls arab: generate",
		[
			(jump_to_scene, "scn_castle_walls_arab"),
			(change_screen_mission)
		], "."),

		("choose_scene_165",
		[],
		"castle walls eastern: generate",
		[
			(jump_to_scene, "scn_castle_walls_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_166",
		[],
		"castle walls euro: generate",
		[
			(jump_to_scene, "scn_castle_walls_euro"),
			(change_screen_mission)
		], "."),

		("choose_scene_167",
		[],
		"castle walls iberia: generate",
		[
			(jump_to_scene, "scn_castle_walls_iberia"),
			(change_screen_mission)
		], "."),

		("choose_scene_168",
		[],
		"castle walls italy: generate",
		[
			(jump_to_scene, "scn_castle_walls_italy"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_169", 0, "Choose a scene: (Page 14 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_182")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_156")
		], "."),

		("choose_scene_169",
		[],
		"castle walls mongol: generate",
		[
			(jump_to_scene, "scn_castle_walls_mongol"),
			(change_screen_mission)
		], "."),

		("choose_scene_170",
		[],
		"castle walls nordic: generate",
		[
			(jump_to_scene, "scn_castle_walls_nordic"),
			(change_screen_mission)
		], "."),

		("choose_scene_171",
		[],
		"center antioch: generate",
		[
			(jump_to_scene, "scn_center_antioch"),
			(change_screen_mission)
		], "."),

		("choose_scene_172",
		[],
		"center jerusalem: generate",
		[
			(jump_to_scene, "scn_center_jerusalem"),
			(change_screen_mission)
		], "."),

		("choose_scene_173",
		[],
		"center saphet: generate",
		[
			(jump_to_scene, "scn_center_saphet"),
			(change_screen_mission)
		], "."),

		("choose_scene_174",
		[],
		"constantinople center: generate",
		[
			(jump_to_scene, "scn_constantinople_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_175",
		[],
		"conversation scene: generate",
		[
			(jump_to_scene, "scn_conversation_scene"),
			(change_screen_mission)
		], "."),

		("choose_scene_176",
		[],
		"den bosch: generate",
		[
			(jump_to_scene, "scn_den_bosch"),
			(change_screen_mission)
		], "."),

		("choose_scene_177",
		[],
		"dhorak keep: generate",
		[
			(jump_to_scene, "scn_dhorak_keep"),
			(change_screen_mission)
		], "."),

		("choose_scene_178",
		[],
		"enterprise brewery: indoors",
		[
			(jump_to_scene, "scn_enterprise_brewery"),
			(change_screen_mission)
		], "."),

		("choose_scene_179",
		[],
		"enterprise dyeworks: indoors",
		[
			(jump_to_scene, "scn_enterprise_dyeworks"),
			(change_screen_mission)
		], "."),

		("choose_scene_180",
		[],
		"enterprise linen weavery: indoors",
		[
			(jump_to_scene, "scn_enterprise_linen_weavery"),
			(change_screen_mission)
		], "."),

		("choose_scene_181",
		[],
		"enterprise mill: indoors",
		[
			(jump_to_scene, "scn_enterprise_mill"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_182", 0, "Choose a scene: (Page 15 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_195")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_169")
		], "."),

		("choose_scene_182",
		[],
		"enterprise oil press: indoors",
		[
			(jump_to_scene, "scn_enterprise_oil_press"),
			(change_screen_mission)
		], "."),

		("choose_scene_183",
		[],
		"enterprise smithy: indoors",
		[
			(jump_to_scene, "scn_enterprise_smithy"),
			(change_screen_mission)
		], "."),

		("choose_scene_184",
		[],
		"enterprise tannery: generate",
		[
			(jump_to_scene, "scn_enterprise_tannery"),
			(change_screen_mission)
		], "."),

		("choose_scene_185",
		[],
		"enterprise winery: indoors",
		[
			(jump_to_scene, "scn_enterprise_winery"),
			(change_screen_mission)
		], "."),

		("choose_scene_186",
		[],
		"enterprise wool weavery: indoors",
		[
			(jump_to_scene, "scn_enterprise_wool_weavery"),
			(change_screen_mission)
		], "."),

		("choose_scene_187",
		[],
		"field 1: generate",
		[
			(jump_to_scene, "scn_field_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_188",
		[],
		"field 2: generate",
		[
			(jump_to_scene, "scn_field_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_189",
		[],
		"field 3: generate",
		[
			(jump_to_scene, "scn_field_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_190",
		[],
		"field 4: generate",
		[
			(jump_to_scene, "scn_field_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_191",
		[],
		"field 5: generate",
		[
			(jump_to_scene, "scn_field_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_192",
		[],
		"four ways inn: generate",
		[
			(jump_to_scene, "scn_four_ways_inn"),
			(change_screen_mission)
		], "."),

		("choose_scene_193",
		[],
		"interior moscow: indoors",
		[
			(jump_to_scene, "scn_interior_moscow"),
			(change_screen_mission)
		], "."),

		("choose_scene_194",
		[],
		"interior motte bailey 1: indoors",
		[
			(jump_to_scene, "scn_interior_motte_bailey_1"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_195", 0, "Choose a scene: (Page 16 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_208")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_182")
		], "."),

		("choose_scene_195",
		[],
		"interior motte bailey 2: indoors",
		[
			(jump_to_scene, "scn_interior_motte_bailey_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_196",
		[],
		"lair desert bandits: generate",
		[
			(jump_to_scene, "scn_lair_desert_bandits"),
			(change_screen_mission)
		], "."),

		("choose_scene_197",
		[],
		"lair forest bandits: generate",
		[
			(jump_to_scene, "scn_lair_forest_bandits"),
			(change_screen_mission)
		], "."),

		("choose_scene_198",
		[],
		"lair mountain bandits: generate",
		[
			(jump_to_scene, "scn_lair_mountain_bandits"),
			(change_screen_mission)
		], "."),

		("choose_scene_199",
		[],
		"lair sea raiders: generate",
		[
			(jump_to_scene, "scn_lair_sea_raiders"),
			(change_screen_mission)
		], "."),

		("choose_scene_200",
		[],
		"lair steppe bandits: generate",
		[
			(jump_to_scene, "scn_lair_steppe_bandits"),
			(change_screen_mission)
		], "."),

		("choose_scene_201",
		[],
		"lair taiga bandits: generate",
		[
			(jump_to_scene, "scn_lair_taiga_bandits"),
			(change_screen_mission)
		], "."),

		("choose_scene_202",
		[],
		"london center: generate",
		[
			(jump_to_scene, "scn_london_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_203",
		[],
		"london walls: generate",
		[
			(jump_to_scene, "scn_london_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_204",
		[],
		"manor: generate",
		[
			(jump_to_scene, "scn_manor"),
			(change_screen_mission)
		], "."),

		("choose_scene_205",
		[],
		"manor Monastery: generate",
		[
			(jump_to_scene, "scn_manor_monastery"),
			(change_screen_mission)
		], "."),

		("choose_scene_206",
		[],
		"manor central european armour smith: generate",
		[
			(jump_to_scene, "scn_manor_central_european_armour_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_207",
		[],
		"manor central european farm: generate",
		[
			(jump_to_scene, "scn_manor_central_european_farm"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_208", 0, "Choose a scene: (Page 17 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_221")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_195")
		], "."),

		("choose_scene_208",
		[],
		"manor central european fletchery: generate",
		[
			(jump_to_scene, "scn_manor_central_european_fletchery"),
			(change_screen_mission)
		], "."),

		("choose_scene_209",
		[],
		"manor central european horse breeder: generate",
		[
			(jump_to_scene, "scn_manor_central_european_horse_breeder"),
			(change_screen_mission)
		], "."),

		("choose_scene_210",
		[],
		"manor central european linen workshop: generate",
		[
			(jump_to_scene, "scn_manor_central_european_linen_workshop"),
			(change_screen_mission)
		], "."),

		("choose_scene_211",
		[],
		"manor central european mines: generate",
		[
			(jump_to_scene, "scn_manor_central_european_mines"),
			(change_screen_mission)
		], "."),

		("choose_scene_212",
		[],
		"manor central european trader: generate",
		[
			(jump_to_scene, "scn_manor_central_european_trader"),
			(change_screen_mission)
		], "."),

		("choose_scene_213",
		[],
		"manor central european weapon smith: generate",
		[
			(jump_to_scene, "scn_manor_central_european_weapon_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_214",
		[],
		"manor desert armour smith: generate",
		[
			(jump_to_scene, "scn_manor_desert_armour_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_215",
		[],
		"manor desert farm: generate",
		[
			(jump_to_scene, "scn_manor_desert_farm"),
			(change_screen_mission)
		], "."),

		("choose_scene_216",
		[],
		"manor desert fletchery: generate",
		[
			(jump_to_scene, "scn_manor_desert_fletchery"),
			(change_screen_mission)
		], "."),

		("choose_scene_217",
		[],
		"manor desert horse breeder: generate",
		[
			(jump_to_scene, "scn_manor_desert_horse_breeder"),
			(change_screen_mission)
		], "."),

		("choose_scene_218",
		[],
		"manor desert linen workshop: generate",
		[
			(jump_to_scene, "scn_manor_desert_linen_workshop"),
			(change_screen_mission)
		], "."),

		("choose_scene_219",
		[],
		"manor desert mines: generate",
		[
			(jump_to_scene, "scn_manor_desert_mines"),
			(change_screen_mission)
		], "."),

		("choose_scene_220",
		[],
		"manor desert trader: generate",
		[
			(jump_to_scene, "scn_manor_desert_trader"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_221", 0, "Choose a scene: (Page 18 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_234")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_208")
		], "."),

		("choose_scene_221",
		[],
		"manor desert weapon smith: generate",
		[
			(jump_to_scene, "scn_manor_desert_weapon_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_222",
		[],
		"manor feudal: generate",
		[
			(jump_to_scene, "scn_manor_feudal"),
			(change_screen_mission)
		], "."),

		("choose_scene_223",
		[],
		"manor fortified arabian: generate",
		[
			(jump_to_scene, "scn_manor_fortified_arabian"),
			(change_screen_mission)
		], "."),

		("choose_scene_224",
		[],
		"manor fortified baltic: generate",
		[
			(jump_to_scene, "scn_manor_fortified_baltic"),
			(change_screen_mission)
		], "."),

		("choose_scene_225",
		[],
		"manor fortified byzantium: generate",
		[
			(jump_to_scene, "scn_manor_fortified_byzantium"),
			(change_screen_mission)
		], "."),

		("choose_scene_226",
		[],
		"manor fortified crusader: generate",
		[
			(jump_to_scene, "scn_manor_fortified_crusader"),
			(change_screen_mission)
		], "."),

		("choose_scene_227",
		[],
		"manor fortified euro desert: generate",
		[
			(jump_to_scene, "scn_manor_fortified_euro_desert"),
			(change_screen_mission)
		], "."),

		("choose_scene_228",
		[],
		"manor fortified euro plains: generate",
		[
			(jump_to_scene, "scn_manor_fortified_euro_plains"),
			(change_screen_mission)
		], "."),

		("choose_scene_229",
		[],
		"manor fortified euro snow: generate",
		[
			(jump_to_scene, "scn_manor_fortified_euro_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_230",
		[],
		"manor fortified euro steppe: generate",
		[
			(jump_to_scene, "scn_manor_fortified_euro_steppe"),
			(change_screen_mission)
		], "."),

		("choose_scene_231",
		[],
		"manor fortified iberian: generate",
		[
			(jump_to_scene, "scn_manor_fortified_iberian"),
			(change_screen_mission)
		], "."),

		("choose_scene_232",
		[],
		"manor fortified latin: generate",
		[
			(jump_to_scene, "scn_manor_fortified_latin"),
			(change_screen_mission)
		], "."),

		("choose_scene_233",
		[],
		"manor fortified rus: generate",
		[
			(jump_to_scene, "scn_manor_fortified_rus"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_234", 0, "Choose a scene: (Page 19 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_247")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_221")
		], "."),

		("choose_scene_234",
		[],
		"manor fortified scand: generate",
		[
			(jump_to_scene, "scn_manor_fortified_scand"),
			(change_screen_mission)
		], "."),

		("choose_scene_235",
		[],
		"manor fortified teutonic: generate",
		[
			(jump_to_scene, "scn_manor_fortified_teutonic"),
			(change_screen_mission)
		], "."),

		("choose_scene_236",
		[],
		"manor nordic armour smith: generate",
		[
			(jump_to_scene, "scn_manor_nordic_armour_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_237",
		[],
		"manor nordic farm: generate",
		[
			(jump_to_scene, "scn_manor_nordic_farm"),
			(change_screen_mission)
		], "."),

		("choose_scene_238",
		[],
		"manor nordic fletchery: generate",
		[
			(jump_to_scene, "scn_manor_nordic_fletchery"),
			(change_screen_mission)
		], "."),

		("choose_scene_239",
		[],
		"manor nordic horse breeder: generate",
		[
			(jump_to_scene, "scn_manor_nordic_horse_breeder"),
			(change_screen_mission)
		], "."),

		("choose_scene_240",
		[],
		"manor nordic linen workshop: generate",
		[
			(jump_to_scene, "scn_manor_nordic_linen_workshop"),
			(change_screen_mission)
		], "."),

		("choose_scene_241",
		[],
		"manor nordic mines: generate",
		[
			(jump_to_scene, "scn_manor_nordic_mines"),
			(change_screen_mission)
		], "."),

		("choose_scene_242",
		[],
		"manor nordic trader: generate",
		[
			(jump_to_scene, "scn_manor_nordic_trader"),
			(change_screen_mission)
		], "."),

		("choose_scene_243",
		[],
		"manor nordic weapon smith: generate",
		[
			(jump_to_scene, "scn_manor_nordic_weapon_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_244",
		[],
		"manor steppe armour smith: generate",
		[
			(jump_to_scene, "scn_manor_steppe_armour_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_245",
		[],
		"manor steppe farm: generate",
		[
			(jump_to_scene, "scn_manor_steppe_farm"),
			(change_screen_mission)
		], "."),

		("choose_scene_246",
		[],
		"manor steppe fletchery: generate",
		[
			(jump_to_scene, "scn_manor_steppe_fletchery"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_247", 0, "Choose a scene: (Page 20 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_260")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_234")
		], "."),

		("choose_scene_247",
		[],
		"manor steppe horse breeder: generate",
		[
			(jump_to_scene, "scn_manor_steppe_horse_breeder"),
			(change_screen_mission)
		], "."),

		("choose_scene_248",
		[],
		"manor steppe linen workshop: generate",
		[
			(jump_to_scene, "scn_manor_steppe_linen_workshop"),
			(change_screen_mission)
		], "."),

		("choose_scene_249",
		[],
		"manor steppe mines: generate",
		[
			(jump_to_scene, "scn_manor_steppe_mines"),
			(change_screen_mission)
		], "."),

		("choose_scene_250",
		[],
		"manor steppe trader: generate",
		[
			(jump_to_scene, "scn_manor_steppe_trader"),
			(change_screen_mission)
		], "."),

		("choose_scene_251",
		[],
		"manor steppe weapon smith: generate",
		[
			(jump_to_scene, "scn_manor_steppe_weapon_smith"),
			(change_screen_mission)
		], "."),

		("choose_scene_252",
		[],
		"manor test: generate",
		[
			(jump_to_scene, "scn_manor_test"),
			(change_screen_mission)
		], "."),

		("choose_scene_253",
		[],
		"manors end: generate|randomize",
		[
			(jump_to_scene, "scn_manors_end"),
			(change_screen_mission)
		], "."),

		("choose_scene_254",
		[],
		"meeting scene desert: generate",
		[
			(jump_to_scene, "scn_meeting_scene_desert"),
			(change_screen_mission)
		], "."),

		("choose_scene_255",
		[],
		"meeting scene desert forest: generate",
		[
			(jump_to_scene, "scn_meeting_scene_desert_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_256",
		[],
		"meeting scene plain: generate",
		[
			(jump_to_scene, "scn_meeting_scene_plain"),
			(change_screen_mission)
		], "."),

		("choose_scene_257",
		[],
		"meeting scene plain forest: generate",
		[
			(jump_to_scene, "scn_meeting_scene_plain_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_258",
		[],
		"meeting scene sea: generate",
		[
			(jump_to_scene, "scn_meeting_scene_sea"),
			(change_screen_mission)
		], "."),

		("choose_scene_259",
		[],
		"meeting scene snow: generate",
		[
			(jump_to_scene, "scn_meeting_scene_snow"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_260", 0, "Choose a scene: (Page 21 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_273")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_247")
		], "."),

		("choose_scene_260",
		[],
		"meeting scene snow forest: generate",
		[
			(jump_to_scene, "scn_meeting_scene_snow_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_261",
		[],
		"meeting scene steppe: generate",
		[
			(jump_to_scene, "scn_meeting_scene_steppe"),
			(change_screen_mission)
		], "."),

		("choose_scene_262",
		[],
		"meeting scene steppe forest: generate",
		[
			(jump_to_scene, "scn_meeting_scene_steppe_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_263",
		[],
		"multi scene 1: generate",
		[
			(jump_to_scene, "scn_multi_scene_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_264",
		[],
		"multi scene 10: generate",
		[
			(jump_to_scene, "scn_multi_scene_10"),
			(change_screen_mission)
		], "."),

		("choose_scene_265",
		[],
		"multi scene 11: generate",
		[
			(jump_to_scene, "scn_multi_scene_11"),
			(change_screen_mission)
		], "."),

		("choose_scene_266",
		[],
		"multi scene 12: generate",
		[
			(jump_to_scene, "scn_multi_scene_12"),
			(change_screen_mission)
		], "."),

		("choose_scene_267",
		[],
		"multi scene 13: generate",
		[
			(jump_to_scene, "scn_multi_scene_13"),
			(change_screen_mission)
		], "."),

		("choose_scene_268",
		[],
		"multi scene 14: generate",
		[
			(jump_to_scene, "scn_multi_scene_14"),
			(change_screen_mission)
		], "."),

		("choose_scene_269",
		[],
		"multi scene 15: generate",
		[
			(jump_to_scene, "scn_multi_scene_15"),
			(change_screen_mission)
		], "."),

		("choose_scene_270",
		[],
		"multi scene 16: generate",
		[
			(jump_to_scene, "scn_multi_scene_16"),
			(change_screen_mission)
		], "."),

		("choose_scene_271",
		[],
		"multi scene 17: generate",
		[
			(jump_to_scene, "scn_multi_scene_17"),
			(change_screen_mission)
		], "."),

		("choose_scene_272",
		[],
		"multi scene 18: generate|muddy water",
		[
			(jump_to_scene, "scn_multi_scene_18"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_273", 0, "Choose a scene: (Page 22 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_286")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_260")
		], "."),

		("choose_scene_273",
		[],
		"multi scene 2: generate",
		[
			(jump_to_scene, "scn_multi_scene_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_274",
		[],
		"multi scene 3: generate",
		[
			(jump_to_scene, "scn_multi_scene_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_275",
		[],
		"multi scene 4: generate",
		[
			(jump_to_scene, "scn_multi_scene_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_276",
		[],
		"multi scene 5: generate",
		[
			(jump_to_scene, "scn_multi_scene_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_277",
		[],
		"multi scene 6: generate",
		[
			(jump_to_scene, "scn_multi_scene_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_278",
		[],
		"multi scene 7: generate",
		[
			(jump_to_scene, "scn_multi_scene_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_279",
		[],
		"multi scene 8: generate",
		[
			(jump_to_scene, "scn_multi_scene_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_280",
		[],
		"multi scene 9: generate",
		[
			(jump_to_scene, "scn_multi_scene_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_281",
		[],
		"multiplayer maps end: generate",
		[
			(jump_to_scene, "scn_multiplayer_maps_end"),
			(change_screen_mission)
		], "."),

		("choose_scene_282",
		[],
		"novice ground: indoors",
		[
			(jump_to_scene, "scn_novice_ground"),
			(change_screen_mission)
		], "."),

		("choose_scene_283",
		[],
		"nuernberg arena: generate",
		[
			(jump_to_scene, "scn_nuernberg_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_284",
		[],
		"nuernberg castle: indoors",
		[
			(jump_to_scene, "scn_nuernberg_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_285",
		[],
		"nuernberg center: generate",
		[
			(jump_to_scene, "scn_nuernberg_center"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_286", 0, "Choose a scene: (Page 23 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_299")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_273")
		], "."),

		("choose_scene_286",
		[],
		"nuernberg prison: indoors",
		[
			(jump_to_scene, "scn_nuernberg_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_287",
		[],
		"nuernberg store: indoors",
		[
			(jump_to_scene, "scn_nuernberg_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_288",
		[],
		"nuernberg tavern: indoors",
		[
			(jump_to_scene, "scn_nuernberg_tavern"),
			(change_screen_mission)
		], "."),

		("choose_scene_289",
		[],
		"nuernberg walls: generate",
		[
			(jump_to_scene, "scn_nuernberg_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_290",
		[],
		"oslo center: generate",
		[
			(jump_to_scene, "scn_oslo_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_291",
		[],
		"pagan stronghold 1: generate",
		[
			(jump_to_scene, "scn_pagan_stronghold_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_292",
		[],
		"player castle central Europe tier1: generate",
		[
			(jump_to_scene, "scn_player_castle_central_europe_tier1"),
			(change_screen_mission)
		], "."),

		("choose_scene_293",
		[],
		"player castle central Europe tier2: generate",
		[
			(jump_to_scene, "scn_player_castle_central_europe_tier2"),
			(change_screen_mission)
		], "."),

		("choose_scene_294",
		[],
		"player castle central Europe tier3: generate",
		[
			(jump_to_scene, "scn_player_castle_central_europe_tier3"),
			(change_screen_mission)
		], "."),

		("choose_scene_295",
		[],
		"player castle desert tier1: generate",
		[
			(jump_to_scene, "scn_player_castle_desert_tier1"),
			(change_screen_mission)
		], "."),

		("choose_scene_296",
		[],
		"player castle desert tier2: generate",
		[
			(jump_to_scene, "scn_player_castle_desert_tier2"),
			(change_screen_mission)
		], "."),

		("choose_scene_297",
		[],
		"player castle desert tier3: generate",
		[
			(jump_to_scene, "scn_player_castle_desert_tier3"),
			(change_screen_mission)
		], "."),

		("choose_scene_298",
		[],
		"player castle french tier1: generate",
		[
			(jump_to_scene, "scn_player_castle_french_tier1"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_299", 0, "Choose a scene: (Page 24 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_312")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_286")
		], "."),

		("choose_scene_299",
		[],
		"player castle french tier2: generate",
		[
			(jump_to_scene, "scn_player_castle_french_tier2"),
			(change_screen_mission)
		], "."),

		("choose_scene_300",
		[],
		"player castle french tier3: generate",
		[
			(jump_to_scene, "scn_player_castle_french_tier3"),
			(change_screen_mission)
		], "."),

		("choose_scene_301",
		[],
		"prison motte bailey 1: indoors",
		[
			(jump_to_scene, "scn_prison_motte_bailey_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_302",
		[],
		"prison motte bailey 2: indoors",
		[
			(jump_to_scene, "scn_prison_motte_bailey_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_303",
		[],
		"quick battle 1: generate",
		[
			(jump_to_scene, "scn_quick_battle_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_304",
		[],
		"quick battle 2: generate",
		[
			(jump_to_scene, "scn_quick_battle_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_305",
		[],
		"quick battle 3: generate",
		[
			(jump_to_scene, "scn_quick_battle_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_306",
		[],
		"quick battle 4: generate",
		[
			(jump_to_scene, "scn_quick_battle_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_307",
		[],
		"quick battle 5: generate",
		[
			(jump_to_scene, "scn_quick_battle_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_308",
		[],
		"quick battle 6: generate",
		[
			(jump_to_scene, "scn_quick_battle_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_309",
		[],
		"quick battle 7: generate",
		[
			(jump_to_scene, "scn_quick_battle_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_310",
		[],
		"quick battle maps end: generate",
		[
			(jump_to_scene, "scn_quick_battle_maps_end"),
			(change_screen_mission)
		], "."),

		("choose_scene_311",
		[],
		"quick battle scene 1: generate",
		[
			(jump_to_scene, "scn_quick_battle_scene_1"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_312", 0, "Choose a scene: (Page 25 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_325")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_299")
		], "."),

		("choose_scene_312",
		[],
		"quick battle scene 2: generate",
		[
			(jump_to_scene, "scn_quick_battle_scene_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_313",
		[],
		"quick battle scene 3: generate",
		[
			(jump_to_scene, "scn_quick_battle_scene_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_314",
		[],
		"quick battle scene 4: generate",
		[
			(jump_to_scene, "scn_quick_battle_scene_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_315",
		[],
		"quick battle scene 5: generate",
		[
			(jump_to_scene, "scn_quick_battle_scene_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_316",
		[],
		"random multi plain large: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_multi_plain_large"),
			(change_screen_mission)
		], "."),

		("choose_scene_317",
		[],
		"random multi plain medium: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_multi_plain_medium"),
			(change_screen_mission)
		], "."),

		("choose_scene_318",
		[],
		"random multi steppe large: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_multi_steppe_large"),
			(change_screen_mission)
		], "."),

		("choose_scene_319",
		[],
		"random multi steppe medium: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_multi_steppe_medium"),
			(change_screen_mission)
		], "."),

		("choose_scene_320",
		[],
		"random scene: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene"),
			(change_screen_mission)
		], "."),

		("choose_scene_321",
		[],
		"random scene desert: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_desert"),
			(change_screen_mission)
		], "."),

		("choose_scene_322",
		[],
		"random scene desert forest: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_desert_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_323",
		[],
		"random scene plain: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_plain"),
			(change_screen_mission)
		], "."),

		("choose_scene_324",
		[],
		"random scene plain forest: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_plain_forest"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_325", 0, "Choose a scene: (Page 26 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_338")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_312")
		], "."),

		("choose_scene_325",
		[],
		"random scene snow: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_326",
		[],
		"random scene snow forest: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_snow_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_327",
		[],
		"random scene steppe: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_steppe"),
			(change_screen_mission)
		], "."),

		("choose_scene_328",
		[],
		"random scene steppe forest: generate|auto entry points|randomize",
		[
			(jump_to_scene, "scn_random_scene_steppe_forest"),
			(change_screen_mission)
		], "."),

		("choose_scene_329",
		[],
		"reserved10",
		[
			(jump_to_scene, "scn_reserved10"),
			(change_screen_mission)
		], "."),

		("choose_scene_330",
		[],
		"reserved11",
		[
			(jump_to_scene, "scn_reserved11"),
			(change_screen_mission)
		], "."),

		("choose_scene_331",
		[],
		"reserved12: indoors",
		[
			(jump_to_scene, "scn_reserved12"),
			(change_screen_mission)
		], "."),

		("choose_scene_332",
		[],
		"reserved4: generate",
		[
			(jump_to_scene, "scn_reserved4"),
			(change_screen_mission)
		], "."),

		("choose_scene_333",
		[],
		"reserved5: generate",
		[
			(jump_to_scene, "scn_reserved5"),
			(change_screen_mission)
		], "."),

		("choose_scene_334",
		[],
		"reserved6: generate",
		[
			(jump_to_scene, "scn_reserved6"),
			(change_screen_mission)
		], "."),

		("choose_scene_335",
		[],
		"reserved7: generate",
		[
			(jump_to_scene, "scn_reserved7"),
			(change_screen_mission)
		], "."),

		("choose_scene_336",
		[],
		"reserved8: generate",
		[
			(jump_to_scene, "scn_reserved8"),
			(change_screen_mission)
		], "."),

		("choose_scene_337",
		[],
		"reserved9: indoors",
		[
			(jump_to_scene, "scn_reserved9"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_338", 0, "Choose a scene: (Page 27 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_351")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_325")
		], "."),

		("choose_scene_338",
		[],
		"rus center: generate",
		[
			(jump_to_scene, "scn_rus_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_339",
		[],
		"rus snow center: generate",
		[
			(jump_to_scene, "scn_rus_snow_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_340",
		[],
		"rus snow walls: generate",
		[
			(jump_to_scene, "scn_rus_snow_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_341",
		[],
		"rus walls: generate",
		[
			(jump_to_scene, "scn_rus_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_342",
		[],
		"salt mine: generate",
		[
			(jump_to_scene, "scn_salt_mine"),
			(change_screen_mission)
		], "."),

		("choose_scene_343",
		[],
		"scene sea: generate",
		[
			(jump_to_scene, "scn_scene_sea"),
			(change_screen_mission)
		], "."),

		("choose_scene_344",
		[],
		"scene sea player eastern vs generic: generate",
		[
			(jump_to_scene, "scn_scene_sea_player_eastern_vs_generic"),
			(change_screen_mission)
		], "."),

		("choose_scene_345",
		[],
		"scene sea player eastern vs nordic: generate",
		[
			(jump_to_scene, "scn_scene_sea_player_eastern_vs_nordic"),
			(change_screen_mission)
		], "."),

		("choose_scene_346",
		[],
		"scene sea player generic vs eastern: generate",
		[
			(jump_to_scene, "scn_scene_sea_player_generic_vs_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_347",
		[],
		"scene sea player generic vs nordic: generate",
		[
			(jump_to_scene, "scn_scene_sea_player_generic_vs_nordic"),
			(change_screen_mission)
		], "."),

		("choose_scene_348",
		[],
		"scene sea player nord vs eastern: generate",
		[
			(jump_to_scene, "scn_scene_sea_player_nord_vs_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_349",
		[],
		"scene sea player nord vs generic: generate",
		[
			(jump_to_scene, "scn_scene_sea_player_nord_vs_generic"),
			(change_screen_mission)
		], "."),

		("choose_scene_350",
		[],
		"sitd battle nile 1: generate|auto entry points",
		[
			(jump_to_scene, "scn_sitd_battle_nile_1"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_351", 0, "Choose a scene: (Page 28 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_364")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_338")
		], "."),

		("choose_scene_351",
		[],
		"sitd battle nile 2: generate|auto entry points",
		[
			(jump_to_scene, "scn_sitd_battle_nile_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_352",
		[],
		"sitd battle nile 3: generate|auto entry points",
		[
			(jump_to_scene, "scn_sitd_battle_nile_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_353",
		[],
		"sitd battle nile 4: generate|auto entry points",
		[
			(jump_to_scene, "scn_sitd_battle_nile_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_354",
		[],
		"smyrna center: generate",
		[
			(jump_to_scene, "scn_smyrna_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_355",
		[],
		"smyrna walls: generate",
		[
			(jump_to_scene, "scn_smyrna_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_356",
		[],
		"test2: generate",
		[
			(jump_to_scene, "scn_test2"),
			(change_screen_mission)
		], "."),

		("choose_scene_357",
		[],
		"test3: generate",
		[
			(jump_to_scene, "scn_test3"),
			(change_screen_mission)
		], "."),

		("choose_scene_358",
		[],
		"test scene: generate",
		[
			(jump_to_scene, "scn_test_scene"),
			(change_screen_mission)
		], "."),

		("choose_scene_359",
		[],
		"the happy boar: indoors",
		[
			(jump_to_scene, "scn_the_happy_boar"),
			(change_screen_mission)
		], "."),

		("choose_scene_360",
		[],
		"to center: generate",
		[
			(jump_to_scene, "scn_to_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_361",
		[],
		"to interior: indoors",
		[
			(jump_to_scene, "scn_to_interior"),
			(change_screen_mission)
		], "."),

		("choose_scene_362",
		[],
		"to walls: generate",
		[
			(jump_to_scene, "scn_to_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_363",
		[],
		"town 10 1 room: indoors",
		[
			(jump_to_scene, "scn_town_10_1_room"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_364", 0, "Choose a scene: (Page 29 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_377")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_351")
		], "."),

		("choose_scene_364",
		[],
		"town 11 2 room: indoors",
		[
			(jump_to_scene, "scn_town_11_2_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_365",
		[],
		"town 13 room: indoors",
		[
			(jump_to_scene, "scn_town_13_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_366",
		[],
		"town 14 1 room: indoors",
		[
			(jump_to_scene, "scn_town_14_1_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_367",
		[],
		"town 1 room: indoors",
		[
			(jump_to_scene, "scn_town_1_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_368",
		[],
		"town 21 room: indoors",
		[
			(jump_to_scene, "scn_town_21_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_369",
		[],
		"town 29 room: indoors",
		[
			(jump_to_scene, "scn_town_29_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_370",
		[],
		"town 30 room: indoors",
		[
			(jump_to_scene, "scn_town_30_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_371",
		[],
		"town 40 room: indoors",
		[
			(jump_to_scene, "scn_town_40_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_372",
		[],
		"town 42 room: indoors",
		[
			(jump_to_scene, "scn_town_42_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_373",
		[],
		"town 4 1 room: indoors",
		[
			(jump_to_scene, "scn_town_4_1_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_374",
		[],
		"town 5 room: indoors",
		[
			(jump_to_scene, "scn_town_5_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_375",
		[],
		"town 6 1 room: indoors",
		[
			(jump_to_scene, "scn_town_6_1_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_376",
		[],
		"town 9 room: indoors",
		[
			(jump_to_scene, "scn_town_9_room"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_377", 0, "Choose a scene: (Page 30 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_390")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_364")
		], "."),

		("choose_scene_377",
		[],
		"town arab alley: generate",
		[
			(jump_to_scene, "scn_town_arab_alley"),
			(change_screen_mission)
		], "."),

		("choose_scene_378",
		[],
		"town arab arena: generate",
		[
			(jump_to_scene, "scn_town_arab_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_379",
		[],
		"town arab castle: indoors",
		[
			(jump_to_scene, "scn_town_arab_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_380",
		[],
		"town arab castle west: indoors",
		[
			(jump_to_scene, "scn_town_arab_castle_west"),
			(change_screen_mission)
		], "."),

		("choose_scene_381",
		[],
		"town arab center: generate",
		[
			(jump_to_scene, "scn_town_arab_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_382",
		[],
		"town arab prison: indoors",
		[
			(jump_to_scene, "scn_town_arab_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_383",
		[],
		"town arab store: indoors",
		[
			(jump_to_scene, "scn_town_arab_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_384",
		[],
		"town arab tavern: indoors",
		[
			(jump_to_scene, "scn_town_arab_tavern"),
			(change_screen_mission)
		], "."),

		("choose_scene_385",
		[],
		"town arab walls: generate",
		[
			(jump_to_scene, "scn_town_arab_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_386",
		[],
		"town baltic alley: generate",
		[
			(jump_to_scene, "scn_town_baltic_alley"),
			(change_screen_mission)
		], "."),

		("choose_scene_387",
		[],
		"town baltic arena: generate",
		[
			(jump_to_scene, "scn_town_baltic_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_388",
		[],
		"town baltic castle: indoors",
		[
			(jump_to_scene, "scn_town_baltic_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_389",
		[],
		"town baltic center: generate",
		[
			(jump_to_scene, "scn_town_baltic_center"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_390", 0, "Choose a scene: (Page 31 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_403")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_377")
		], "."),

		("choose_scene_390",
		[],
		"town baltic prison: indoors",
		[
			(jump_to_scene, "scn_town_baltic_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_391",
		[],
		"town baltic store: indoors",
		[
			(jump_to_scene, "scn_town_baltic_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_392",
		[],
		"town baltic tavern: indoors",
		[
			(jump_to_scene, "scn_town_baltic_tavern"),
			(change_screen_mission)
		], "."),

		("choose_scene_393",
		[],
		"town baltic walls: generate",
		[
			(jump_to_scene, "scn_town_baltic_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_394",
		[],
		"town castle crusade 1: indoors",
		[
			(jump_to_scene, "scn_town_castle_crusade_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_395",
		[],
		"town castle crusade 2: indoors",
		[
			(jump_to_scene, "scn_town_castle_crusade_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_396",
		[],
		"town eastern alley: generate",
		[
			(jump_to_scene, "scn_town_eastern_alley"),
			(change_screen_mission)
		], "."),

		("choose_scene_397",
		[],
		"town eastern arena: generate",
		[
			(jump_to_scene, "scn_town_eastern_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_398",
		[],
		"town eastern castle: indoors",
		[
			(jump_to_scene, "scn_town_eastern_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_399",
		[],
		"town eastern center: generate",
		[
			(jump_to_scene, "scn_town_eastern_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_400",
		[],
		"town eastern prison: indoors",
		[
			(jump_to_scene, "scn_town_eastern_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_401",
		[],
		"town eastern store: indoors",
		[
			(jump_to_scene, "scn_town_eastern_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_402",
		[],
		"town eastern tavern: indoors",
		[
			(jump_to_scene, "scn_town_eastern_tavern"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_403", 0, "Choose a scene: (Page 32 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_416")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_390")
		], "."),

		("choose_scene_403",
		[],
		"town eastern walls: generate",
		[
			(jump_to_scene, "scn_town_eastern_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_404",
		[],
		"town euro alley: generate",
		[
			(jump_to_scene, "scn_town_euro_alley"),
			(change_screen_mission)
		], "."),

		("choose_scene_405",
		[],
		"town euro arena: generate",
		[
			(jump_to_scene, "scn_town_euro_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_406",
		[],
		"town euro castle: indoors",
		[
			(jump_to_scene, "scn_town_euro_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_407",
		[],
		"town euro center: generate",
		[
			(jump_to_scene, "scn_town_euro_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_408",
		[],
		"town euro center 10: generate",
		[
			(jump_to_scene, "scn_town_euro_center_10"),
			(change_screen_mission)
		], "."),

		("choose_scene_409",
		[],
		"town euro center 11: generate",
		[
			(jump_to_scene, "scn_town_euro_center_11"),
			(change_screen_mission)
		], "."),

		("choose_scene_410",
		[],
		"town euro center 2: generate",
		[
			(jump_to_scene, "scn_town_euro_center_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_411",
		[],
		"town euro center 3: generate",
		[
			(jump_to_scene, "scn_town_euro_center_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_412",
		[],
		"town euro center 4: generate",
		[
			(jump_to_scene, "scn_town_euro_center_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_413",
		[],
		"town euro center 4: generate",
		[
			(jump_to_scene, "scn_town_euro_center_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_414",
		[],
		"town euro center 5: generate",
		[
			(jump_to_scene, "scn_town_euro_center_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_415",
		[],
		"town euro center 6: generate",
		[
			(jump_to_scene, "scn_town_euro_center_6"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_416", 0, "Choose a scene: (Page 33 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_429")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_403")
		], "."),

		("choose_scene_416",
		[],
		"town euro center 7: generate",
		[
			(jump_to_scene, "scn_town_euro_center_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_417",
		[],
		"town euro center 8: generate",
		[
			(jump_to_scene, "scn_town_euro_center_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_418",
		[],
		"town euro center 9: generate",
		[
			(jump_to_scene, "scn_town_euro_center_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_419",
		[],
		"town euro prison: indoors",
		[
			(jump_to_scene, "scn_town_euro_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_420",
		[],
		"town euro store: indoors",
		[
			(jump_to_scene, "scn_town_euro_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_421",
		[],
		"town euro tavern: indoors",
		[
			(jump_to_scene, "scn_town_euro_tavern"),
			(change_screen_mission)
		], "."),

		("choose_scene_422",
		[],
		"town euro walls: generate",
		[
			(jump_to_scene, "scn_town_euro_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_423",
		[],
		"town house arabian: indoors",
		[
			(jump_to_scene, "scn_town_house_arabian"),
			(change_screen_mission)
		], "."),

		("choose_scene_424",
		[],
		"town house eastern: indoors",
		[
			(jump_to_scene, "scn_town_house_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_425",
		[],
		"town house euro: indoors",
		[
			(jump_to_scene, "scn_town_house_euro"),
			(change_screen_mission)
		], "."),

		("choose_scene_426",
		[],
		"town interior byz: indoors",
		[
			(jump_to_scene, "scn_town_interior_byz"),
			(change_screen_mission)
		], "."),

		("choose_scene_427",
		[],
		"town italy castle: indoors",
		[
			(jump_to_scene, "scn_town_italy_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_428",
		[],
		"town italy center: generate",
		[
			(jump_to_scene, "scn_town_italy_center"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_429", 0, "Choose a scene: (Page 34 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_442")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_416")
		], "."),

		("choose_scene_429",
		[],
		"town italy walls: generate",
		[
			(jump_to_scene, "scn_town_italy_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_430",
		[],
		"town italy walls new: generate",
		[
			(jump_to_scene, "scn_town_italy_walls_new"),
			(change_screen_mission)
		], "."),

		("choose_scene_431",
		[],
		"town mongol alley: generate",
		[
			(jump_to_scene, "scn_town_mongol_alley"),
			(change_screen_mission)
		], "."),

		("choose_scene_432",
		[],
		"town mongol arena: generate",
		[
			(jump_to_scene, "scn_town_mongol_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_433",
		[],
		"town mongol castle: generate",
		[
			(jump_to_scene, "scn_town_mongol_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_434",
		[],
		"town mongol center: generate",
		[
			(jump_to_scene, "scn_town_mongol_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_435",
		[],
		"town mongol prison: indoors",
		[
			(jump_to_scene, "scn_town_mongol_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_436",
		[],
		"town mongol room: indoors",
		[
			(jump_to_scene, "scn_town_mongol_room"),
			(change_screen_mission)
		], "."),

		("choose_scene_437",
		[],
		"town mongol store: indoors",
		[
			(jump_to_scene, "scn_town_mongol_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_438",
		[],
		"town mongol tavern: indoors",
		[
			(jump_to_scene, "scn_town_mongol_tavern"),
			(change_screen_mission)
		], "."),

		("choose_scene_439",
		[],
		"town mongol walls: generate",
		[
			(jump_to_scene, "scn_town_mongol_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_440",
		[],
		"town nordic alley: generate",
		[
			(jump_to_scene, "scn_town_nordic_alley"),
			(change_screen_mission)
		], "."),

		("choose_scene_441",
		[],
		"town nordic arena: generate",
		[
			(jump_to_scene, "scn_town_nordic_arena"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_442", 0, "Choose a scene: (Page 35 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_455")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_429")
		], "."),

		("choose_scene_442",
		[],
		"town nordic castle: indoors",
		[
			(jump_to_scene, "scn_town_nordic_castle"),
			(change_screen_mission)
		], "."),

		("choose_scene_443",
		[],
		"town nordic center: generate",
		[
			(jump_to_scene, "scn_town_nordic_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_444",
		[],
		"town nordic center new: generate",
		[
			(jump_to_scene, "scn_town_nordic_center_new"),
			(change_screen_mission)
		], "."),

		("choose_scene_445",
		[],
		"town nordic prison: indoors",
		[
			(jump_to_scene, "scn_town_nordic_prison"),
			(change_screen_mission)
		], "."),

		("choose_scene_446",
		[],
		"town nordic store: indoors",
		[
			(jump_to_scene, "scn_town_nordic_store"),
			(change_screen_mission)
		], "."),

		("choose_scene_447",
		[],
		"town nordic tavern: indoors",
		[
			(jump_to_scene, "scn_town_nordic_tavern"),
			(change_screen_mission)
		], "."),

		("choose_scene_448",
		[],
		"town nordic walls: generate",
		[
			(jump_to_scene, "scn_town_nordic_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_449",
		[],
		"town nordic walls new: generate",
		[
			(jump_to_scene, "scn_town_nordic_walls_new"),
			(change_screen_mission)
		], "."),

		("choose_scene_450",
		[],
		"training ground: generate",
		[
			(jump_to_scene, "scn_training_ground"),
			(change_screen_mission)
		], "."),

		("choose_scene_451",
		[],
		"training ground horse track 1: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_452",
		[],
		"training ground horse track 10: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_10"),
			(change_screen_mission)
		], "."),

		("choose_scene_453",
		[],
		"training ground horse track 11: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_11"),
			(change_screen_mission)
		], "."),

		("choose_scene_454",
		[],
		"training ground horse track 12: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_12"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_455", 0, "Choose a scene: (Page 36 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_468")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_442")
		], "."),

		("choose_scene_455",
		[],
		"training ground horse track 13: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_13"),
			(change_screen_mission)
		], "."),

		("choose_scene_456",
		[],
		"training ground horse track 14: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_14"),
			(change_screen_mission)
		], "."),

		("choose_scene_457",
		[],
		"training ground horse track 15: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_15"),
			(change_screen_mission)
		], "."),

		("choose_scene_458",
		[],
		"training ground horse track 16: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_16"),
			(change_screen_mission)
		], "."),

		("choose_scene_459",
		[],
		"training ground horse track 17: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_17"),
			(change_screen_mission)
		], "."),

		("choose_scene_460",
		[],
		"training ground horse track 18: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_18"),
			(change_screen_mission)
		], "."),

		("choose_scene_461",
		[],
		"training ground horse track 2: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_462",
		[],
		"training ground horse track 3: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_463",
		[],
		"training ground horse track 4: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_464",
		[],
		"training ground horse track 5: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_465",
		[],
		"training ground horse track 5: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_466",
		[],
		"training ground horse track 6: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_467",
		[],
		"training ground horse track 7: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_7"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_468", 0, "Choose a scene: (Page 37 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_481")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_455")
		], "."),

		("choose_scene_468",
		[],
		"training ground horse track 8: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_469",
		[],
		"training ground horse track 9: generate",
		[
			(jump_to_scene, "scn_training_ground_horse_track_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_470",
		[],
		"training ground ranged melee 1: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_471",
		[],
		"training ground ranged melee 10: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_10"),
			(change_screen_mission)
		], "."),

		("choose_scene_472",
		[],
		"training ground ranged melee 11: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_11"),
			(change_screen_mission)
		], "."),

		("choose_scene_473",
		[],
		"training ground ranged melee 12: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_12"),
			(change_screen_mission)
		], "."),

		("choose_scene_474",
		[],
		"training ground ranged melee 13: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_13"),
			(change_screen_mission)
		], "."),

		("choose_scene_475",
		[],
		"training ground ranged melee 14: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_14"),
			(change_screen_mission)
		], "."),

		("choose_scene_476",
		[],
		"training ground ranged melee 15: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_15"),
			(change_screen_mission)
		], "."),

		("choose_scene_477",
		[],
		"training ground ranged melee 16: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_16"),
			(change_screen_mission)
		], "."),

		("choose_scene_478",
		[],
		"training ground ranged melee 17: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_17"),
			(change_screen_mission)
		], "."),

		("choose_scene_479",
		[],
		"training ground ranged melee 18: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_18"),
			(change_screen_mission)
		], "."),

		("choose_scene_480",
		[],
		"training ground ranged melee 2: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_2"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_481", 0, "Choose a scene: (Page 38 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_494")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_468")
		], "."),

		("choose_scene_481",
		[],
		"training ground ranged melee 3: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_482",
		[],
		"training ground ranged melee 4: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_483",
		[],
		"training ground ranged melee 5: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_484",
		[],
		"training ground ranged melee 6: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_6"),
			(change_screen_mission)
		], "."),

		("choose_scene_485",
		[],
		"training ground ranged melee 7: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_486",
		[],
		"training ground ranged melee 8: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_487",
		[],
		"training ground ranged melee 9: generate",
		[
			(jump_to_scene, "scn_training_ground_ranged_melee_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_488",
		[],
		"tutorial 1: indoors",
		[
			(jump_to_scene, "scn_tutorial_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_489",
		[],
		"tutorial 2: indoors",
		[
			(jump_to_scene, "scn_tutorial_2"),
			(change_screen_mission)
		], "."),

		("choose_scene_490",
		[],
		"tutorial 3: indoors",
		[
			(jump_to_scene, "scn_tutorial_3"),
			(change_screen_mission)
		], "."),

		("choose_scene_491",
		[],
		"tutorial 4: generate",
		[
			(jump_to_scene, "scn_tutorial_4"),
			(change_screen_mission)
		], "."),

		("choose_scene_492",
		[],
		"tutorial 5: generate",
		[
			(jump_to_scene, "scn_tutorial_5"),
			(change_screen_mission)
		], "."),

		("choose_scene_493",
		[],
		"tutorial 6: generate",
		[
			(jump_to_scene, "scn_tutorial_6"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_494", 0, "Choose a scene: (Page 39 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_507")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_481")
		], "."),

		("choose_scene_494",
		[],
		"tutorial 7: generate",
		[
			(jump_to_scene, "scn_tutorial_7"),
			(change_screen_mission)
		], "."),

		("choose_scene_495",
		[],
		"tutorial 8: generate",
		[
			(jump_to_scene, "scn_tutorial_8"),
			(change_screen_mission)
		], "."),

		("choose_scene_496",
		[],
		"tutorial 9: generate",
		[
			(jump_to_scene, "scn_tutorial_9"),
			(change_screen_mission)
		], "."),

		("choose_scene_497",
		[],
		"tutorial training ground: generate",
		[
			(jump_to_scene, "scn_tutorial_training_ground"),
			(change_screen_mission)
		], "."),

		("choose_scene_498",
		[],
		"venice center: generate",
		[
			(jump_to_scene, "scn_venice_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_499",
		[],
		"village arab: generate",
		[
			(jump_to_scene, "scn_village_arab"),
			(change_screen_mission)
		], "."),

		("choose_scene_500",
		[],
		"village byz: generate",
		[
			(jump_to_scene, "scn_village_byz"),
			(change_screen_mission)
		], "."),

		("choose_scene_501",
		[],
		"village byzantine: generate",
		[
			(jump_to_scene, "scn_village_byzantine"),
			(change_screen_mission)
		], "."),

		("choose_scene_502",
		[],
		"village eastern: generate",
		[
			(jump_to_scene, "scn_village_eastern"),
			(change_screen_mission)
		], "."),

		("choose_scene_503",
		[],
		"village eastern2: generate",
		[
			(jump_to_scene, "scn_village_eastern2"),
			(change_screen_mission)
		], "."),

		("choose_scene_504",
		[],
		"village england: generate",
		[
			(jump_to_scene, "scn_village_england"),
			(change_screen_mission)
		], "."),

		("choose_scene_505",
		[],
		"village euro: generate",
		[
			(jump_to_scene, "scn_village_euro"),
			(change_screen_mission)
		], "."),

		("choose_scene_506",
		[],
		"village euro2: generate",
		[
			(jump_to_scene, "scn_village_euro2"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_507", 0, "Choose a scene: (Page 40 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_520")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_494")
		], "."),

		("choose_scene_507",
		[],
		"village iberia: generate",
		[
			(jump_to_scene, "scn_village_iberia"),
			(change_screen_mission)
		], "."),

		("choose_scene_508",
		[],
		"village italy: generate",
		[
			(jump_to_scene, "scn_village_italy"),
			(change_screen_mission)
		], "."),

		("choose_scene_509",
		[],
		"village mongol: generate",
		[
			(jump_to_scene, "scn_village_mongol"),
			(change_screen_mission)
		], "."),

		("choose_scene_510",
		[],
		"village mongol desert: generate",
		[
			(jump_to_scene, "scn_village_mongol_desert"),
			(change_screen_mission)
		], "."),

		("choose_scene_511",
		[],
		"village mongol plains: generate",
		[
			(jump_to_scene, "scn_village_mongol_plains"),
			(change_screen_mission)
		], "."),

		("choose_scene_512",
		[],
		"village mongol snow: generate",
		[
			(jump_to_scene, "scn_village_mongol_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_513",
		[],
		"village nordic: generate",
		[
			(jump_to_scene, "scn_village_nordic"),
			(change_screen_mission)
		], "."),

		("choose_scene_514",
		[],
		"village nordic2: generate",
		[
			(jump_to_scene, "scn_village_nordic2"),
			(change_screen_mission)
		], "."),

		("choose_scene_515",
		[],
		"village nordic3: generate",
		[
			(jump_to_scene, "scn_village_nordic3"),
			(change_screen_mission)
		], "."),

		("choose_scene_516",
		[],
		"vilnius center: generate",
		[
			(jump_to_scene, "scn_vilnius_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_517",
		[],
		"vilnius walls: generate",
		[
			(jump_to_scene, "scn_vilnius_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_518",
		[],
		"walls antioch: generate",
		[
			(jump_to_scene, "scn_walls_antioch"),
			(change_screen_mission)
		], "."),

		("choose_scene_519",
		[],
		"walls arensburg: generate",
		[
			(jump_to_scene, "scn_walls_arensburg"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_520", 0, "Choose a scene: (Page 41 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_533")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_507")
		], "."),

		("choose_scene_520",
		[],
		"walls arwa: generate",
		[
			(jump_to_scene, "scn_walls_arwa"),
			(change_screen_mission)
		], "."),

		("choose_scene_521",
		[],
		"walls balt: generate",
		[
			(jump_to_scene, "scn_walls_balt"),
			(change_screen_mission)
		], "."),

		("choose_scene_522",
		[],
		"walls beaumaris: generate",
		[
			(jump_to_scene, "scn_walls_beaumaris"),
			(change_screen_mission)
		], "."),

		("choose_scene_523",
		[],
		"walls brandenburg: generate",
		[
			(jump_to_scene, "scn_walls_brandenburg"),
			(change_screen_mission)
		], "."),

		("choose_scene_524",
		[],
		"walls carlisle: generate",
		[
			(jump_to_scene, "scn_walls_carlisle"),
			(change_screen_mission)
		], "."),

		("choose_scene_525",
		[],
		"walls conwy: generate",
		[
			(jump_to_scene, "scn_walls_conwy"),
			(change_screen_mission)
		], "."),

		("choose_scene_526",
		[],
		"walls dorpat: generate",
		[
			(jump_to_scene, "scn_walls_dorpat"),
			(change_screen_mission)
		], "."),

		("choose_scene_527",
		[],
		"walls generic french: generate",
		[
			(jump_to_scene, "scn_walls_generic_french"),
			(change_screen_mission)
		], "."),

		("choose_scene_528",
		[],
		"walls hedingham: generate",
		[
			(jump_to_scene, "scn_walls_hedingham"),
			(change_screen_mission)
		], "."),

		("choose_scene_529",
		[],
		"walls hohenburg: generate",
		[
			(jump_to_scene, "scn_walls_hohenburg"),
			(change_screen_mission)
		], "."),

		("choose_scene_530",
		[],
		"walls jerusalem: generate",
		[
			(jump_to_scene, "scn_walls_jerusalem"),
			(change_screen_mission)
		], "."),

		("choose_scene_531",
		[],
		"walls karak: generate",
		[
			(jump_to_scene, "scn_walls_karak"),
			(change_screen_mission)
		], "."),

		("choose_scene_532",
		[],
		"walls kernave: generate",
		[
			(jump_to_scene, "scn_walls_kernave"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_533", 0, "Choose a scene: (Page 42 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_546")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_520")
		], "."),

		("choose_scene_533",
		[],
		"walls krak: generate",
		[
			(jump_to_scene, "scn_walls_krak"),
			(change_screen_mission)
		], "."),

		("choose_scene_534",
		[],
		"walls ladoga: generate",
		[
			(jump_to_scene, "scn_walls_ladoga"),
			(change_screen_mission)
		], "."),

		("choose_scene_535",
		[],
		"walls lake: generate",
		[
			(jump_to_scene, "scn_walls_lake"),
			(change_screen_mission)
		], "."),

		("choose_scene_536",
		[],
		"walls lemsahl: generate",
		[
			(jump_to_scene, "scn_walls_lemsahl"),
			(change_screen_mission)
		], "."),

		("choose_scene_537",
		[],
		"walls llansteffan: generate",
		[
			(jump_to_scene, "scn_walls_llansteffan"),
			(change_screen_mission)
		], "."),

		("choose_scene_538",
		[],
		"walls lublin: generate",
		[
			(jump_to_scene, "scn_walls_lublin"),
			(change_screen_mission)
		], "."),

		("choose_scene_539",
		[],
		"walls mann: generate",
		[
			(jump_to_scene, "scn_walls_mann"),
			(change_screen_mission)
		], "."),

		("choose_scene_540",
		[],
		"walls mansoura: generate",
		[
			(jump_to_scene, "scn_walls_mansoura"),
			(change_screen_mission)
		], "."),

		("choose_scene_541",
		[],
		"walls marienwerder: generate",
		[
			(jump_to_scene, "scn_walls_marienwerder"),
			(change_screen_mission)
		], "."),

		("choose_scene_542",
		[],
		"walls montefort: generate",
		[
			(jump_to_scene, "scn_walls_montefort"),
			(change_screen_mission)
		], "."),

		("choose_scene_543",
		[],
		"walls moscow: generate",
		[
			(jump_to_scene, "scn_walls_moscow"),
			(change_screen_mission)
		], "."),

		("choose_scene_544",
		[],
		"walls motte bailey 1: generate",
		[
			(jump_to_scene, "scn_walls_motte_bailey_1"),
			(change_screen_mission)
		], "."),

		("choose_scene_545",
		[],
		"walls motte bailey 2: generate",
		[
			(jump_to_scene, "scn_walls_motte_bailey_2"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_546", 0, "Choose a scene: (Page 43 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("next",
		[],
		"Next...",
		[
			(jump_to_menu, "mnu_choose_scenes_559")
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_533")
		], "."),

		("choose_scene_546",
		[],
		"walls munchen: generate",
		[
			(jump_to_scene, "scn_walls_munchen"),
			(change_screen_mission)
		], "."),

		("choose_scene_547",
		[],
		"walls opole: generate",
		[
			(jump_to_scene, "scn_walls_opole"),
			(change_screen_mission)
		], "."),

		("choose_scene_548",
		[],
		"walls pevensey: generate",
		[
			(jump_to_scene, "scn_walls_pevensey"),
			(change_screen_mission)
		], "."),

		("choose_scene_549",
		[],
		"walls pskov: generate",
		[
			(jump_to_scene, "scn_walls_pskov"),
			(change_screen_mission)
		], "."),

		("choose_scene_550",
		[],
		"walls ragnhildsholmen: generate",
		[
			(jump_to_scene, "scn_walls_ragnhildsholmen"),
			(change_screen_mission)
		], "."),

		("choose_scene_551",
		[],
		"walls saphet: generate",
		[
			(jump_to_scene, "scn_walls_saphet"),
			(change_screen_mission)
		], "."),

		("choose_scene_552",
		[],
		"walls scot: generate",
		[
			(jump_to_scene, "scn_walls_scot"),
			(change_screen_mission)
		], "."),

		("choose_scene_553",
		[],
		"walls seiminiskeliai: generate",
		[
			(jump_to_scene, "scn_walls_seiminiskeliai"),
			(change_screen_mission)
		], "."),

		("choose_scene_554",
		[],
		"walls seiminiskeliai snow: generate",
		[
			(jump_to_scene, "scn_walls_seiminiskeliai_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_555",
		[],
		"walls taurapilis: generate",
		[
			(jump_to_scene, "scn_walls_taurapilis"),
			(change_screen_mission)
		], "."),

		("choose_scene_556",
		[],
		"walls taurapilis snow: generate",
		[
			(jump_to_scene, "scn_walls_taurapilis_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_557",
		[],
		"walls tonbridge: generate",
		[
			(jump_to_scene, "scn_walls_tonbridge"),
			(change_screen_mission)
		], "."),

		("choose_scene_558",
		[],
		"walls treyden: generate",
		[
			(jump_to_scene, "scn_walls_treyden"),
			(change_screen_mission)
		], ".")
	]
	),

	("choose_scenes_559", 0, "Choose a scene: (Page 44 of 44)",
"none",
	[],
	[
		("back",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], "."),

		("previous",
		[],
		"Previous...",
		[
			(jump_to_menu, "mnu_choose_scenes_546")
		], "."),

		("choose_scene_559",
		[],
		"walls tunsberg: generate",
		[
			(jump_to_scene, "scn_walls_tunsberg"),
			(change_screen_mission)
		], "."),

		("choose_scene_560",
		[],
		"walls vladimir: generate",
		[
			(jump_to_scene, "scn_walls_vladimir"),
			(change_screen_mission)
		], "."),

		("choose_scene_561",
		[],
		"walls vladimir snow: generate",
		[
			(jump_to_scene, "scn_walls_vladimir_snow"),
			(change_screen_mission)
		], "."),

		("choose_scene_562",
		[],
		"walls wenden: generate",
		[
			(jump_to_scene, "scn_walls_wenden"),
			(change_screen_mission)
		], "."),

		("choose_scene_563",
		[],
		"walls york: generate",
		[
			(jump_to_scene, "scn_walls_york"),
			(change_screen_mission)
		], "."),

		("choose_scene_564",
		[],
		"water",
		[
			(jump_to_scene, "scn_water"),
			(change_screen_mission)
		], "."),

		("choose_scene_565",
		[],
		"wedding: indoors",
		[
			(jump_to_scene, "scn_wedding"),
			(change_screen_mission)
		], "."),

		("choose_scene_566",
		[],
		"york center: generate",
		[
			(jump_to_scene, "scn_york_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_567",
		[],
		"york walls: generate",
		[
			(jump_to_scene, "scn_york_walls"),
			(change_screen_mission)
		], "."),

		("choose_scene_568",
		[],
		"zendar arena: generate",
		[
			(jump_to_scene, "scn_zendar_arena"),
			(change_screen_mission)
		], "."),

		("choose_scene_569",
		[],
		"zendar center: generate",
		[
			(jump_to_scene, "scn_zendar_center"),
			(change_screen_mission)
		], "."),

		("choose_scene_570",
		[],
		"zendar merchant: indoors",
		[
			(jump_to_scene, "scn_zendar_merchant"),
			(change_screen_mission)
		], ".")
	]
	),

]