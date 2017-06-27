# -*- coding: utf-8 -*-
from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0

parties = [
	("main_party", "Main Party", icon_player|pf_limit_members, no_menu, pt_none, fac_player_faction, aggressiveness_0, ai_bhvr_hold, 0, (17.0, 52.5), [(trp_player, 1, 0)]),

	("temp_party", "{!}temp party", icon_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("camp_bandits", "{!}camp bandits", icon_player|pf_disabled, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), [(trp_temp_troop, 3, 0)]),

	("temp_party_2", "{!}temp party 2", icon_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_casualties", "{!}casualties", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_casualties_2", "{!}casualties", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_casualties_3", "{!}casualties", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_wounded", "{!}enemies wounded", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_killed", "{!}enemies killed", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("main_party_backup", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("encountered_party_backup", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_friends_backup", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("player_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("enemy_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("ally_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_enemy", "{!}collective enemy", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_ally", "{!}collective ally", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_friends", "{!}collective ally", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("total_enemy_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("routed_enemies", "{!}routed enemies", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("zendar", "Zendar", icon_town|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("town_1_1", "Elbing", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (60.36, 75.75), [], 263.0),

	("town_1_2", "KÃ¶nigsberg", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.5, 89.5), [], 120.0),

	("town_1_3", "Thorn", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.43, 65.115), [], 150.0),

	("town_1_4", "Riga", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (100.2, 114.0), [], 25.0),

	("town_2_1", "Vilnius", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (117.48, 72.9), [], 100.0),

	("town_2_2", "Raseiniai", icon_wooden|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.145, 88.11), [], 170.0),

	("town_2_3", "Novogorodok", icon_wooden|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (126.195, 61.83), [], 35.0),

	("town_2_4", "Polotesk", icon_rus|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (152.04, 94.77), [], 170.0),

	("town_3_1", "Sarai", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (269.58, 1.32), []),

	("town_3_2", "Smolensk", icon_rus|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.2, 87.01), [], 170.0),

	("town_3_3", "Kiev", icon_wooden|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (168.03, 21.36), [], 170.0),

	("town_3_4", "Chernigov", icon_rus|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (172.47, 50.41), [], 170.0),

	("town_4_1", "Lund", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.485, 98.13), [], 15.0),

	("town_4_2", "Roarskeldae", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-24.375, 98.835), [], 15.0),

	("town_4_3", "Reval", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (103.11, 144.24), [], 15.0),

	("town_4_4", "WybÃ¦rgh", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-51.375, 104.55), [], 15.0),

	("town_5_1", "KrakÃ³w", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (49.815, 25.725), [], 25.0),

	("town_5_2", "WrocÅ‚aw", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (19.665, 36.63), [], 60.0),

	("town_5_3", "GdaÅ„sk", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (43.62, 81.57), [], 135.0),

	("town_5_4", "PoznaÅ„", icon_teutonic_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (29.955, 51.885), [], 260.0),

	("town_6_1", "NÃ¼rnberg", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-22.92, 27.435), [], 100.0),

	("town_6_2", "KÃ¶ln", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-75.25, 40.615), [], 100.0),

	("town_6_3", "Frankfurt", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-49.98, 34.86), [], 100.0),

	("town_6_4", "Basel", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-68.36, -5.98), [], 100.0),

	("town_6_5", "Magdeburg", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-22.395, 55.41), [], 100.0),

	("town_6_6", "LÃ¼beck", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-38.0, 75.0), [], 100.0),

	("town_7_1", "Varad", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.64, -12.495), []),

	("town_7_2", "Gradec", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.69, -32.325), [], 128.0),

	("town_7_3", "Poson", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.68, -2.21), []),

	("town_7_4", "Zeged", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (63.555, -18.405), []),

	("town_8_1", "Velikiy Novgorod", icon_rus|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (188.58, 132.51), [], 100.0),

	("town_8_2", "Russa", icon_rus|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (186.37, 118.93), []),

	("town_9_1", "London", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-138.57, 47.955), []),

	("town_9_2", "Bristol", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-176.22, 41.31), []),

	("town_9_3", "Chester", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-173.115, 65.4), []),

	("town_9_4", "York", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.965, 81.015), []),

	("town_9_5", "Bordeaux", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-150.615, -39.63), []),

	("town_9_6", "Dublin", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-209.505, 69.3), []),

	("town_10_1", "Paris", icon_french_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-122.49, 12.72), []),

	("town_10_2", "Nantes", icon_french_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-158.01, -9.81), []),

	("town_10_3", "Dijon", icon_french_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-99.015, -12.135), []),

	("town_10_4", "Toulouse", icon_french_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-130.38, -54.33), []),

	("town_10_5", "Rouen", icon_french_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-130.11, 22.62), []),

	("town_10_6", "Aix-en-Provence", icon_french_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-91.455, -51.855), []),

	("town_11_1", "NiÃ°arÃ³s", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-27.81, 206.535), []),

	("town_11_2", "BiÇ«rgyn", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-88.215, 152.955), []),

	("town_11_3", "Ã�slÃ³", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-34.185, 149.775), []),

	("town_12_1", "Stirling", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-182.18, 102.98), []),

	("town_12_2", "Glasgow", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-188.69, 99.89), []),

	("town_13_1", "Donegal", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-231.735, 78.72), []),

	("town_13_2", "Dungannon", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-215.85, 87.75), []),

	("town_14_1", "Westraarus", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (28.545, 149.28), [], 15.0),

	("town_14_2", "Ã�bÃº", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.79, 159.285), [], 15.0),

	("town_14_3", "WysbÃº", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.04, 124.11), [], 15.0),

	("town_15_1", "Volodymyr", icon_wooden|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (115.7, 44.1), []),

	("town_15_2", "Halych", icon_wooden|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (117.48, 16.61), []),

	("town_15_3", "Zvenigorod", icon_wooden|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (104.96, 16.82), []),

	("town_16_1", "Lisboa", icon_italy|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-232.275, -113.175), []),

	("town_16_2", "Coimbra", icon_italy|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-228.87, -94.935), []),

	("town_17_1", "Barcelona", icon_italy|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-123.18, -80.415), []),

	("town_17_2", "Valencia", icon_italy|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-145.95, -104.805), []),

	("town_18_1", "Toledo", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-183.825, -103.02), []),

	("town_18_2", "Sevilla ", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-206.2, -129.5), []),

	("town_19_1", "Pamplona", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-160.23, -62.535), []),

	("town_20_1", "Granada", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.785, -132.105), []),

	("town_20_2", "MÃ¡laga", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-189.45, -137.355), []),

	("town_21_1", "Roma", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.55, -75.36), []),

	("town_21_2", "Ancona", icon_italy_new_b|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.58, -52.65), []),

	("town_22_1", "Nicaea", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (157.59, -95.985), []),

	("town_22_2", "Smyrna", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (128.04, -117.465), []),

	("town_22_3", "Chonai", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (147.765, -126.48), []),

	("town_22_4", "Thessalonica", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.56, -89.325), []),

	("town_23_1", "Acre", icon_acre|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (208.665, -191.925), []),

	("town_23_2", "Tarsus", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (208.38, -139.575), []),

	("town_23_4", "Antioch", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (219.495, -147.525), []),

	("town_23_5", "Nicosia", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (194.88, -158.16), []),

	("town_23_6", "Saphet", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (221.69, -172.02), []),

	("town_24_1", "Palermo", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.83, -122.77), []),

	("town_24_2", "Napoli", icon_italy_new_b|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-0.675, -85.755), []),

	("town_25_1", "Cairo", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (168.51, -233.52), []),

	("town_25_2", "Alexandria", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.375, -209.61), []),

	("town_25_3", "Damietta", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (178.905, -211.305), []),

	("town_25_4", "Damascus", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (237.76, -174.48), []),

	("town_25_5", "Jerusalem", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (210.75, -204.24), []),

	("town_26_1", "Constantinople", icon_constantinople|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (146.025, -84.66), []),

	("town_26_2", "Patras", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.79, -120.54), []),

	("town_27_1", "Trebizond", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (240.075, -86.805), []),

	("town_27_2", "Ankara", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (183.255, -104.325), []),

	("town_27_3", "Iconium", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (180.153, -128.235), []),

	("town_27_4", "Aleppo", icon_eastern2|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (226.74, -146.11), []),

	("town_28_1", "Tunis", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.44, -136.965), []),

	("town_28_2", "Tripoli", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-23.745, -187.215), []),

	("town_29_1", "Kotor", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (41.19, -67.0), []),

	("town_29_2", "Brskovo", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (53.8, -56.65), []),

	("town_30_1", "Tarnovo", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (116.38, -60.64), []),

	("town_30_2", "Plovdiv ", icon_eastern|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.74, -73.65), []),

	("town_31_1", "Fes", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-195.825, -168.0), []),

	("town_31_2", "Marakesh", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-212.52, -194.31), []),

	("town_31_3", "Oran", icon_andalusian|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-146.265, -156.39), []),

	("town_32_1", "Venezia", icon_italy_new_b|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-18.93, -36.885), []),

	("town_32_2", "Candia", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (110.84, -156.98), []),

	("town_32_3", "Ragusa", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (35.51, -64.53), []),

	("town_37_1", "Aberffraw", icon_town|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-188.16, 68.51), []),

	("town_38_1", "Genova", icon_italy_new_b|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.105, -41.97), []),

	("town_39_1", "Pisa", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-36.05, -56.35), []),

	("town_40_1", "Milano", icon_italy_new_b|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-53.59, -30.99), []),

	("town_40_2", "Firenze", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-25.83, -56.81), []),

	("town_41_1", "Verona", icon_italy_new_a|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-30.495, -31.035), [], 90.0),

	("town_41_2", "Siena", icon_italy_new_b|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-25.55, -66.19), []),

	("town_42_1", "Praha", icon_prague|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (3.045, 26.625), [], 100.0),

	("town_42_2", "OlmÃ¼tz", icon_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (13.84, 26.26), [], 53.0),

	("castle_1_1", "Arensburg", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.91, 127.96), [], 135.0),

	("castle_1_2", "Balga", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (57.5, 85.0), [], 310.0),

	("castle_1_3", "Fellin", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.16, 130.24), [], 60.0),

	("castle_1_4", "Georgenburg", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (91.395, 100.71), [], 170.0),

	("castle_1_5", "Dorpat", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (127.05, 131.25), [], 55.0),

	("castle_1_6", "Lemsahl", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (104.025, 124.185), [], 180.0),

	("castle_1_7", "Treyden", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (106.245, 110.745), [], 170.0),

	("castle_1_8", "Marienwerder", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (75.78, 77.93), [], 170.0),

	("castle_1_9", "Wenden", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (120.555, 116.265), [], 170.0),

	("castle_2_1", "VerÅ¡viai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (96.795, 84.09), []),

	("castle_2_2", "Å eiminiÅ¡kÄ—liai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (110.46, 92.055), []),

	("castle_2_3", "Dubingiai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (132.42, 76.89), []),

	("castle_2_4", "KernavÄ—", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.405, 80.565), []),

	("castle_2_5", "Taurapilis", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (135.51, 85.395), []),

	("castle_2_6", "Horodna", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.855, 71.58), []),

	("castle_2_7", "Mensk", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (145.56, 73.125), []),

	("castle_2_8", "Vitebsk", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.93, 86.925), []),

	("castle_3_1", "Ryazan", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (263.04, 71.3), [], 75.0),

	("castle_3_2", "Vladimir", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (251.11, 94.71), [], 90.0),

	("castle_3_3", "Sugdeya", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (203.38, -39.1), [], 90.0),

	("castle_3_4", "Novgorod Seversky", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (202.89, 64.29), [], 90.0),

	("castle_3_5", "Elec", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (250.64, 55.53), [], 90.0),

	("castle_3_6", "Moscow", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (218.97, 89.72), [], 90.0),

	("castle_3_7", "Pereyaslavl", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (195.3, 10.93), [], 90.0),

	("castle_3_8", "TÃ®rgoviste", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.11, -37.61), [], 90.0),

	("castle_4_1", "Ã†ggersburgh", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-56.385, 114.81), [], 90.0),

	("castle_4_2", "Ã�rÃ³s", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.65, 103.47), [], 90.0),

	("castle_4_3", "RipÃ¦rhÃºs", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.03, 86.295), [], 90.0),

	("castle_4_4", "SlÃ¦swich", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-43.425, 79.665), [], 90.0),

	("castle_4_5", "Swinaburgh", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-37.275, 91.53), [], 90.0),

	("castle_4_6", "KalundÃ¦burgh", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-31.905, 98.295), [], 90.0),

	("castle_4_7", "HelsingiÃ¦burgh", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-13.98, 103.365), [], 90.0),

	("castle_4_8", "Varbiargh", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-21.465, 120.18), [], 90.0),

	("castle_5_1", "Gniezno", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (46.29, 48.255), [], 135.0),

	("castle_5_2", "Sandomierz", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.33, 38.355), []),

	("castle_5_3", "GÅ‚ogÃ³w", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (17.025, 45.465), [], 110.0),

	("castle_5_4", "Opole", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (32.37, 30.495), [], 260.0),

	("castle_5_5", "CheÅ‚mno", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (57.405, 64.8), [], 260.0),

	("castle_5_6", "CzÅ‚uchÃ³w", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (35.55, 70.305), [], 260.0),

	("castle_5_7", "Lubusz", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.765, 57.75), [], 170.0),

	("castle_5_8", "Lublin", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (89.175, 49.5), [], 10.0),

	("castle_6_1", "Aachen", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-86.61, 39.945), [], 90.0),

	("castle_6_2", "Trier", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-79.44, 25.61), [], 90.0),

	("castle_6_3", "Wien", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (11.92, 1.7), [], 90.0),

	("castle_6_4", "Mainz", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-62.505, 24.27), [], 90.0),

	("castle_6_5", "MÃ¼nchen", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-24.69, 5.55), [], 90.0),

	("castle_6_6", "Brandenburg", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-9.81, 62.49), [], 90.0),

	("castle_6_7", "Leuwen", icon_dutch_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-96.765, 43.83), [], 90.0),

	("castle_6_8", "Nancy", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-82.0, 12.9), [], 90.0),

	("castle_6_9", "Braunschweig", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-48.44, 53.14), [], 90.0),

	("castle_6_10", "StraÃŸburg", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.43, -20.325), [], 90.0),

	("castle_6_11", "Baden", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-52.815, 14.58), [], 90.0),

	("castle_6_12", "MeiÃŸen", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-5.13, 37.635), [], 90.0),

	("castle_6_13", "Sponheim", icon_castle_icon_a|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-68.63, 19.99), [], 90.0),

	("castle_7_1", "Breber", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.4, -33.48), [], 97.0),

	("castle_7_2", "Albens", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (100.785, -20.265), [], 90.0),

	("castle_7_3", "Kwszug", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.69, -11.28), [], 90.0),

	("castle_7_4", "Soklos", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (31.88, -28.56), [], 90.0),

	("castle_7_5", "Zoulum", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.42, 5.77), []),

	("castle_7_6", "Patak", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.925, 3.285), [], 90.0),

	("castle_7_7", "Colocsa", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.58, -18.825), []),

	("castle_7_8", "Eztergom", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (40.38, -5.685), []),

	("castle_7_9", "Vrhbosna", icon_european_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.3, -49.54), []),

	("castle_8_1", "Pskov", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (142.69, 120.48), [], 90.0),

	("castle_8_2", "Velikiye Luki", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (170.46, 100.91), [], 90.0),

	("castle_8_3", "Torzhok", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (213.37, 99.73), [], 90.0),

	("castle_8_4", "Ladoga", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (190.98, 158.74), [], 90.0),

	("castle_9_1", "Beeston Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-165.075, 70.32), [], 135.0),

	("castle_9_2", "Lewes Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-146.13, 38.985), [], 135.0),

	("castle_9_3", "Corfe Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-164.175, 38.385), [], 135.0),

	("castle_9_4", "Dover Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-132.945, 41.385), [], 135.0),

	("castle_9_5", "Bamburgh Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-162.87, 96.72), [], 135.0),

	("castle_9_6", "Lancaster Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-171.69, 79.935), [], 135.0),

	("castle_9_7", "Clare Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-136.23, 54.555), [], 135.0),

	("castle_9_8", "Pembroke Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.12, 48.91), [], 135.0),

	("castle_9_9", "Wexford Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-212.16, 61.11), [], 135.0),

	("castle_10_1", "Carcassonne", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-121.125, -59.685), [], 135.0),

	("castle_10_2", "Mortain", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-153.69, 10.02), [], 135.0),

	("castle_10_3", "Boulogne", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-126.75, 34.53), [], 135.0),

	("castle_10_4", "ChÃ¢lons", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-93.105, 20.205), [], 135.0),

	("castle_10_5", "AngoulÃªme", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-148.05, -25.38), [], 135.0),

	("castle_10_6", "Cahors", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-129.42, -40.95), [], 135.0),

	("castle_10_7", "Clermont", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-115.395, -26.22), [], 135.0),

	("castle_10_8", "OrlÃ©ans", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-126.93, 1.45), [], 135.0),

	("castle_10_9", "Sens", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-120.255, -2.775), [], 135.0),

	("castle_10_10", "Chinon", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-142.89, -11.265), [], 135.0),

	("castle_10_11", "Arras", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-114.72, 28.935), [], 135.0),

	("castle_10_12", "Angers", icon_french_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-143.04, -4.815), [], 135.0),

	("castle_11_1", "BorglÃ³", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-74.565, 187.185), [], 90.0),

	("castle_11_2", "Borgyndr", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-71.445, 165.72), [], 90.0),

	("castle_11_3", "Stafangr", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-85.26, 142.665), [], 90.0),

	("castle_11_4", "TÃºnsberg", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-42.825, 140.295), [], 90.0),

	("castle_11_5", "RagnhildarhÃ³lmr", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-26.235, 131.16), [], 90.0),

	("castle_11_6", "Mann", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-188.565, 79.59), [], 90.0),

	("castle_12_1", "Urquhart", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-188.92, 118.77), [], 135.0),

	("castle_12_2", "Dingwall", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-187.74, 124.38), [], 135.0),

	("castle_12_3", "Killdrummy", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-172.95, 118.73), [], 135.0),

	("castle_12_4", "Edinburgh", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-175.76, 99.78), [], 135.0),

	("castle_13_1", "Sligo", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-240.33, 70.5), [], 135.0),

	("castle_13_2", "Tullyhogue Fort", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-211.5, 80.415), [], 135.0),

	("castle_13_3", "Blarney Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-226.83, 63.84), [], 135.0),

	("castle_13_4", "Carrickabraghey Castle", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-226.62, 88.38), [], 135.0),

	("castle_14_1", "Kalmarnir", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.195, 107.34), [], 90.0),

	("castle_14_2", "Stokholm", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.075, 144.795), [], 90.0),

	("castle_14_3", "Scara", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-5.73, 130.35), [], 90.0),

	("castle_14_4", "Visingsey ", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (7.08, 120.21), [], 90.0),

	("castle_14_5", "StÃ¦geburgh", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.975, 128.82), [], 90.0),

	("castle_14_6", "LinkÃ¸pang", icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (14.58, 127.23), [], 90.0),

	("castle_15_1", "Przemysl", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (89.99, 28.81), [], 135.0),

	("castle_15_2", "Lutsk", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (133.6, 34.09), [], 135.0),

	("castle_15_3", "Dorogichin", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (89.51, 63.74), [], 135.0),

	("castle_15_4", "Bakota", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (149.12, -4.5), [], 135.0),

	("castle_15_5", "Kholm", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (97.2, 47.84), [], 135.0),

	("castle_15_6", "Terebovl", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (144.65, 20.94), [], 135.0),

	("castle_16_1", "GuimarÃ£es", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-224.59, -80.38), [], 135.0),

	("castle_16_2", "MÃ©rtola", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-216.3, -127.72), [], 135.0),

	("castle_16_3", "Silves", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-228.9285, -131.93295), [], 135.0),

	("castle_16_4", "BraganÃ§a", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-212.058, -76.33635), [], 135.0),

	("castle_17_1", "Zaragoza", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.4445, -78.6393), [], 135.0),

	("castle_17_2", "Castellciutat", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-133.30275, -73.2633), [], 135.0),

	("castle_17_3", "PerpinyÃ ", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-114.81, -65.55), [], 135.0),

	("castle_17_4", "Alcoi", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.7145, -111.5379), [], 135.0),

	("castle_17_5", "Tortosa", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-132.1962, -84.83655), [], 135.0),

	("castle_17_6", "Jaca", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-150.576, -68.55), [], 135.0),

	("castle_17_7", "AlbarracÃ­n", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-160.485, -90.5568), [], 135.0),

	("castle_18_1", "Lemos", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-223.158, -67.14525), [], 135.0),

	("castle_18_2", "Vizcaya", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-177.444, -56.04525), [], 135.0),

	("castle_18_3", "LeÃ³n", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-202.5645, -66.0393), [], 135.0),

	("castle_18_4", "Burgos", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-177.5385, -64.1763), [], 135.0),

	("castle_18_5", "Badajoz", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-209.3235, -105.7749), [], 135.0),

	("castle_18_6", "Murcia", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.425, -118.93905), [], 135.0),

	("castle_19_1", "San Sebastian", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-164.385, -57.42), [], 135.0),

	("castle_20_1", "Qasbat Tarifa", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-200.79, -144.435), []),

	("castle_20_2", "Qasbat Antakira", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-192.28, -132.28), []),

	("castle_20_3", "Qasbat Wadi-Aci", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-169.82, -128.3), []),

	("castle_20_4", "Qasbat Al-Mariyya", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-173.65, -139.79), []),

	("castle_20_5", "Al-Qal'a", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-184.365, -125.97), []),

	("castle_20_6", "ShalubÄ�nya", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.92, -139.4), []),

	("castle_20_7", "Baza", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-174.54, -122.535), []),

	("castle_22_1", "Myra", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (152.94, -144.93), [], 135.0),

	("castle_22_2", "Attalia", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (166.83, -138.93), [], 135.0),

	("castle_22_3", "Sozopolis", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (168.435, -121.665), [], 135.0),

	("castle_22_4", "Ephesus", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (131.415, -123.84), [], 135.0),

	("castle_22_5", "Thyatira", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (145.59, -110.925), [], 135.0),

	("castle_22_6", "Adramyttium", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (128.37, -102.09), [], 135.0),

	("castle_23_1", "Krak des Chevaliers", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (230.7825, -160.602), []),

	("castle_23_2", "Montfort Castle", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (213.26, -190.16), []),

	("castle_23_3", "Tripoli", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (219.795, -167.31), []),

	("castle_24_1", "Scilla", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (15.31, -120.91), []),

	("castle_24_2", "Bari", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (26.36, -84.74), []),

	("castle_24_3", "Melfi", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (15.34, -85.61), []),

	("castle_24_4", "Otranto", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.12, -96.62), []),

	("castle_25_1", "Mansoura", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (171.21, -221.355), []),

	("castle_25_2", "Al`Arish", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.19, -210.135), []),

	("castle_25_3", "Ismailiya", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.085, -226.47), []),

	("castle_25_4", "Akaba", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (205.53, -240.03), []),

	("castle_25_5", "Barca", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.595, -191.01), []),

	("castle_25_6", "Karak", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (220.425, -214.515), []),

	("castle_25_7", "Beni Suef", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (162.0, -243.25), []),

	("castle_26_1", "Larissa", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.04, -109.05), [], 135.0),

	("castle_26_2", "Janina", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (68.25, -109.38), [], 135.0),

	("castle_26_3", "Adrianople", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (124.335, -76.815), [], 135.0),

	("castle_26_4", "Chrystoupolis", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (105.43, -84.11), [], 135.0),

	("castle_27_1", "Ermenak", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (186.075, -143.085), [], 135.0),

	("castle_27_2", "Amasya", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (212.37, -90.915), [], 135.0),

	("castle_27_3", "Erzincan", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (231.765, -104.61), [], 135.0),

	("castle_27_4", "Edessa", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (252.87, -147.81), [], 135.0),

	("castle_27_5", "Ragga", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (254.94, -163.8), [], 135.0),

	("castle_27_6", "Kars", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (268.02, -93.75), [], 135.0),

	("castle_28_1", "Kairwan", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-37.68, -157.815), []),

	("castle_28_2", "El Krib", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-45.87, -150.135), []),

	("castle_28_3", "Dar Sidi al Azhar", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.045, -153.72), []),

	("castle_28_4", "Bougie", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-91.545, -140.955), []),

	("castle_28_5", "Gabes", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-42.735, -175.2), []),

	("castle_28_6", "Sirt", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (33.465, -213.045), []),

	("castle_29_1", "MagliÄ�", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.28, -51.92), [], 135.0),

	("castle_29_2", "Bar", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.33, -77.84), [], 135.0),

	("castle_30_1", "Drastar", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (131.6, -48.01), [], 135.0),

	("castle_30_2", "Sredets", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (92.31, -67.88), [], 135.0),

	("castle_30_3", "Bdin", icon_castle_byzantium|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.14, -44.68), [], 135.0),

	("castle_31_1", "Tangier", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-201.9, -152.79), []),

	("castle_31_2", "Algiers", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-124.71, -141.915), []),

	("castle_32_1", "Pula", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-3.02, -36.57), []),

	("castle_32_2", "Spalato", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.12, -59.11), []),

	("castle_33_1", "Å iurpilis", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.02, 66.49), []),

	("castle_33_2", "KatkuÅ¡kÄ—s", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (92.43, 69.72), []),

	("castle_33_3", "DuoliebaiÄ�iai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (84.34, 75.35), []),

	("castle_34_1", "Katniava", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (81.9, 77.95), []),

	("castle_34_2", "PagÄ—giai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (73.65, 88.91), []),

	("castle_34_3", "VÄ—luva", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.65, 81.29), []),

	("castle_35_1", "Dzintare", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (75.74, 109.49), []),

	("castle_35_2", "Ä®piltis", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.62, 102.9), []),

	("castle_35_3", "DiÅ¾deme", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.95, 106.28), []),

	("castle_36_1", "Å iauliai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.41, 97.72), []),

	("castle_36_2", "KraÅ¾iai", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.72, 94.74), []),

	("castle_36_3", "MedvÄ—galis", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (80.63, 90.63), []),

	("castle_37_1", "Caernarfon", icon_norman_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-186.67, 65.28), [], 135.0),

	("castle_38_1", "Bonifacio", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-52.95, -79.45), []),

	("castle_38_2", "Cagliari", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-52.93, -108.56), []),

	("castle_39_1", "Olbia", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-47.14, -85.55), []),

	("castle_39_2", "Oristano", icon_italy_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.67, -102.37), []),

	("castle_player", "Player Castle", icon_castle_c|pf_disabled|pf_castle, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (-124.71, -141.915), []),

	("village_1_1", "Rehden", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (72.6, 69.87), [], 100.0),

	("village_1_2", "Strasburg", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (81.585, 66.255), [], 80.0),

	("village_1_3", "Kokenhausen", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (123.945, 108.615), [], 260.0),

	("village_1_4", "Kreva", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.06, 122.55), [], 280.0),

	("village_1_5", "Ragnit", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (73.32, 86.43), [], 260.0),

	("village_1_6", "Ascheraden", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (118.98, 111.21), [], 100.0),

	("village_1_7", "Tervete", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (90.31605, 111.35205), [], 100.0),

	("village_1_8", "Bartenstein", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (60.255, 78.87), [], 100.0),

	("village_1_9", "Braunsberg", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.55, 83.75), [], 100.0),

	("village_1_10", "Rositten", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (131.07, 115.545), [], 100.0),

	("village_1_11", "Wolmar", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (112.16, 114.36), [], 20.0),

	("village_1_12", "Memelburg", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.61, 97.14), [], 60.0),

	("village_1_13", "Mona", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (89.94495, 134.50455), [], 55.0),

	("village_1_14", "Osterode", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.86, 74.175), [], 260.0),

	("village_1_15", "Pedole", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (80.55, 116.445), [], 100.0),

	("village_1_16", "Leal", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (89.505, 104.25), [], 260.0),

	("village_1_17", "Heilsberg", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.33, 73.06), [], 10.0),

	("village_2_1", "BraÅ¾uolÄ—", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.915, 72.84), []),

	("village_2_2", "Berzgainiai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (125.835, 85.845), []),

	("village_2_3", "UÅ¾paliai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (116.955, 100.575), []),

	("village_2_4", "Vosgeliai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (136.17, 97.515), []),

	("village_2_5", "Veliuona", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (90.9, 81.225), []),

	("village_2_6", "VilkmergÄ—", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.715, 87.675), []),

	("village_2_7", "Ariogala", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (99.945, 91.68), []),

	("village_2_8", "Betygala", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (91.485, 93.495), []),

	("village_2_9", "Braslavl", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (141.75, 100.38), []),

	("village_2_10", "Lida", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (119.85, 66.96), []),

	("village_2_11", "Slonim", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (116.28, 62.325), []),

	("village_2_12", "Slutsk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (141.9, 55.35), []),

	("village_2_13", "Turov", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (144.72, 52.14), []),

	("village_2_14", "Kletsk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (132.33, 59.085), []),

	("village_2_15", "Orsha", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (155.61, 72.255), []),

	("village_2_16", "Svisloch", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (148.2, 66.78), []),

	("village_3_1", "Korsun", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (188.54, 0.6), [], 100.0),

	("village_3_2", "Kolomna", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (228.73, 80.34), [], 130.0),

	("village_3_3", "Vyazma", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.72, 91.4), [], 100.0),

	("village_3_4", "Kursk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (224.69, 43.47), [], 80.0),

	("village_3_5", "Vyshgorod", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.95, 30.92), [], 10.0),

	("village_3_6", "Murom", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (259.48, 86.5), [], 10.0),

	("village_3_7", "Pronsk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (256.03, 73.36), [], 10.0),

	("village_3_8", "Snovsk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (184.89, 51.37), [], 10.0),

	("village_3_9", "Mstislavl", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (179.66, 73.99), [], 10.0),

	("village_3_10", "Karf", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (213.24, -34.45), [], 10.0),

	("village_3_11", "Sevsk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (222.67, 62.33), [], 10.0),

	("village_3_12", "Azak", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (257.08, -5.0), [], 10.0),

	("village_3_13", "Beldzamen", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (263.76, 9.6), [], 10.0),

	("village_3_14", "Zvenigrad", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (165.91, 14.09), [], 10.0),

	("village_3_15", "Lybich", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.86, 55.95), [], 10.0),

	("village_3_16", "Slatina", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (109.49, -45.66), [], 10.0),

	("village_4_1", "SlangÃ¦Ã¾orp", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-20.055, 100.89), [], 10.0),

	("village_4_2", "KÃ¸pmannÃ¦hafn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-18.99, 97.11), [], 10.0),

	("village_4_3", "ÃžrÃ¦leburgh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.22, 93.36), [], 10.0),

	("village_4_4", "Hammershus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (6.705, 91.755), [], 10.0),

	("village_4_5", "Narvia", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (144.24, 146.23), [], 10.0),

	("village_4_6", "WesenbÃ¦rgh", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.145, 140.61), [], 10.0),

	("village_4_7", "RandrÃ¸sÃ¦", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-42.18, 107.16), [], 10.0),

	("village_4_8", "Ã�lÃ¦burgh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-45.45, 112.545), [], 10.0),

	("village_4_9", "HjÃ³ring", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-44.325, 120.555), [], 10.0),

	("village_4_10", "RipÃ¦", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.195, 93.045), [], 10.0),

	("village_4_11", "HorsnÃ¦s", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-45.66, 99.54), [], 10.0),

	("village_4_12", "OÃ¾Ã¦nswÃ©", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-38.565, 95.385), [], 10.0),

	("village_4_13", "FlÃ¦nsburgh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-47.31, 84.075), [], 10.0),

	("village_4_14", "HalmstaÃ¾r", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-15.345, 111.12), [], 10.0),

	("village_4_15", "FalkenbÃ¦rgh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-19.185, 116.64), [], 10.0),

	("village_4_16", "RingstaÃ¾r", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-23.895, 92.37), [], 10.0),

	("village_5_1", "WieleÅ„", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.6, 55.395), [], 260.0),

	("village_5_2", "Miedzyrzecz", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (6.465, 55.755), [], 260.0),

	("village_5_3", "Tyniec", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (45.795, 21.9), [], 110.0),

	("village_5_4", "Åšwidnica", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (19.32, 32.325), [], 120.0),

	("village_5_5", "BolesÅ‚awiec", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (11.97, 45.945), [], 130.0),

	("village_5_6", "OstrÃ³w", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (35.85, 63.72), [], 170.0),

	("village_5_7", "Giecz", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (34.71, 46.08), [], 170.0),

	("village_5_8", "Czersk", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.01, 52.02), [], 100.0),

	("village_5_9", "WÅ‚ocÅ‚awek", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (61.665, 61.005), [], 110.0),

	("village_5_10", "RacibÃ³rz", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.275, 30.615), [], 120.0),

	("village_5_11", "WiÅ›lica", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (72.9, 35.175), [], 130.0),

	("village_5_12", "Legnica", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (13.2, 36.315), [], 170.0),

	("village_5_13", "Szczecin", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.895, 70.155), [], 170.0),

	("village_5_14", "KoÅ‚obrzeg", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (21.315, 79.065), [], 170.0),

	("village_5_15", "Biecz", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.275, 25.905), [], 100.0),

	("village_5_16", "Ostrowiec", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (51.765, 47.52), [], 10.0),

	("village_6_1", "Bremen", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-53.25, 60.42), [], 10.0),

	("village_6_2", "Koblenz", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-70.34, 32.04), [], 10.0),

	("village_6_3", "Heidelberg", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-51.48, 25.47), [], 10.0),

	("village_6_4", "Landshut", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-19.455, 8.085), [], 10.0),

	("village_6_5", "Salzwedel", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-27.915, 61.935), [], 10.0),

	("village_6_6", "Gelnhausen", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.95, 38.79), [], 10.0),

	("village_6_7", "Leipzig", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-16.425, 44.46), [], 10.0),

	("village_6_8", "Stuttgart", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-44.115, 18.435), [], 10.0),

	("village_6_9", "Bingen", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-67.38, 27.09), [], 10.0),

	("village_6_10", "Bonn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-74.0, 37.0), [], 10.0),

	("village_6_11", "NeuÃŸ", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-83.46, 53.22), [], 10.0),

	("village_6_13", "Eger", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.395, 27.84), [], 10.0),

	("village_6_14", "NÃ¶rdlingen", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-27.15, 19.23), [], 10.0),

	("village_6_15", "WÃ¼rzburg", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-33.135, 30.195), [], 10.0),

	("village_6_16", "Regensburg", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.925, 19.11), [], 10.0),

	("village_6_17", "Wittenberg", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-13.905, 55.17), [], 10.0),

	("village_6_18", "Hamburg", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-39.99, 67.02), [], 10.0),

	("village_6_19", "Den Bosch", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-90.345, 46.875), [], 10.0),

	("village_6_20", "Spandau", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.07, 63.06), [], 10.0),

	("village_6_21", "Brussel", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-98.88, 39.45), [], 10.0),

	("village_6_22", "Limburg", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-55.77, 39.45), [], 10.0),

	("village_6_23", "Graz", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (14.79, -13.125), [], 10.0),

	("village_6_24", "Friesach", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-74.115, 63.99), [], 10.0),

	("village_6_25", "ZÃ¼rich", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-62.28, -6.8), [], 10.0),

	("village_6_26", "Bern", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-75.81, -9.46), [], 10.0),

	("village_7_1", "Cremnychbana", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.38, 10.27), []),

	("village_7_2", "Peech", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (33.27, -25.515), []),

	("village_7_3", "Pest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.45, -10.02), []),

	("village_7_4", "Kulusuar", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (101.13, -14.25), []),

	("village_7_5", "Ikurwar", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.77, -12.96), []),

	("village_7_6", "Tholchwa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.455, 1.68), []),

	("village_7_7", "Jaztraburzca", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (14.79, -31.98), []),

	("village_7_8", "Jablanaz", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (9.862425, -38.4657), []),

	("village_7_9", "Vesprim", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (34.29, -13.77), []),

	("village_7_10", "Zyn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (19.395, -36.405), []),

	("village_7_11", "Keurus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (50.595, -16.65), []),

	("village_7_12", "Arad", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.825, -26.265), []),

	("village_7_13", "Ziloc", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (92.805, -9.36), []),

	("village_7_14", "Buda", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.18, -9.885), []),

	("village_7_15", "Chonad", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (68.145, -19.755), []),

	("village_7_16", "Tymes", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.225, -30.915), []),

	("village_7_17", "Travnik", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (36.69, -42.06), []),

	("village_8_1", "Opochka", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.91, 103.77), [], 110.0),

	("village_8_2", "Tyosovo", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (174.33, 137.76), [], 260.0),

	("village_8_3", "Izborsk", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (136.07, 118.97), [], 10.0),

	("village_8_4", "Kholm", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.44, 111.13), [], 10.0),

	("village_8_5", "Vyshny Volochyok", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (202.67, 111.71), [], 10.0),

	("village_8_6", "Nebolchi", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (201.36, 139.45), [], 10.0),

	("village_8_7", "Bezek", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (229.11, 108.9), [], 10.0),

	("village_8_8", "Koporye", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (153.08, 150.22), [], 260.0),

	("village_9_1", "Lincoln", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-150.95, 68.11), [], 10.0),

	("village_9_2", "Powys", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.07, 57.78), [], 10.0),

	("village_9_3", "Guildford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-145.95, 46.8), [], 10.0),

	("village_9_4", "Patcham", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-153.48, 41.085), [], 10.0),

	("village_9_5", "Aberystwyth", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-185.51, 57.51), [], 10.0),

	("village_9_6", "St. Ives", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-191.775, 32.235), [], 10.0),

	("village_9_7", "Oxford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-144.48, 53.01), [], 10.0),

	("village_9_8", "Norwich", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-133.455, 57.285), [], 10.0),

	("village_9_9", "Hereford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-176.055, 47.94), [], 10.0),

	("village_9_10", "Wigan", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-171.165, 76.545), [], 10.0),

	("village_9_11", "Bridlington", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-156.825, 85.005), [], 10.0),

	("village_9_12", "Gloucester", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-156.435, 51.675), [], 10.0),

	("village_9_13", "Corfe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-170.115, 37.905), [], 10.0),

	("village_9_14", "Hornsea", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-150.57, 78.48), [], 10.0),

	("village_9_15", "Bude", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-181.725, 38.28), [], 10.0),

	("village_9_16", "Rothbury", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-161.445, 93.405), [], 10.0),

	("village_9_17", "Merignac", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-153.48, -43.65), [], 10.0),

	("village_9_18", "Bergerac", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-138.855, -37.695), [], 10.0),

	("village_9_19", "Limerick", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-232.095, 55.635), [], 10.0),

	("village_9_20", "Cork", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-237.0, 47.97), [], 10.0),

	("village_9_21", "Waterford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-215.895, 56.865), [], 10.0),

	("village_10_1", "Poitiers", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-149.58, -16.11), [], 10.0),

	("village_10_2", "Rennes", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-161.25, 3.48), [], 10.0),

	("village_10_3", "Evreux", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-133.2, 13.725), [], 10.0),

	("village_10_4", "Caen", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-147.345, 16.98), [], 10.0),

	("village_10_5", "Chartres", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-131.355, 6.48), [], 10.0),

	("village_10_6", "Amiens", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-121.545, 24.645), [], 10.0),

	("village_10_7", "Calais", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-122.43, 39.735), [], 10.0),

	("village_10_8", "Limoges", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-138.75, -21.585), [], 10.0),

	("village_10_10", "Albi", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-123.24, -52.305), [], 10.0),

	("village_10_12", "Narbonne", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-115.53, -58.425), [], 10.0),

	("village_10_13", "Troyes", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.94, 4.515), [], 10.0),

	("village_10_14", "Coutance", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-159.93, 16.92), [], 10.0),

	("village_10_15", "Avignon", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-97.05, -46.605), [], 10.0),

	("village_10_16", "Quimper", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-181.905, 1.575), [], 10.0),

	("village_10_17", "Toulon", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-84.48, -57.42), [], 10.0),

	("village_10_18", "Mende", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-109.68, -43.815), [], 10.0),

	("village_10_19", "Marseille", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-91.83, -56.34), [], 10.0),

	("village_10_20", "BesanÃ§on", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-83.655, -5.91), [], 10.0),

	("village_10_21", "Laon", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.97, 22.905), [], 10.0),

	("village_10_22", "Nevers", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-122.925, -12.78), [], 10.0),

	("village_10_23", "Lyon", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-99.72, -25.2), [], 10.0),

	("village_10_24", "Langres", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-96.18, -3.63), [], 10.0),

	("village_10_28", "Reims", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-105.57, 19.965), [], 10.0),

	("village_10_30", "Le Mans", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-140.7, 3.75), [], 10.0),

	("village_11_1", "Hjaltlandseyjar", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-155.685, 153.48), [], 10.0),

	("village_11_2", "Freysey", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-3.195, 197.31), [], 10.0),

	("village_11_3", "Ãžorshofn", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-214.335, 177.96), [], 10.0),

	("village_11_4", "Hamarr", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-32.52, 157.665), [], 10.0),

	("village_11_5", "Borg", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-32.385, 140.34), [], 10.0),

	("village_11_6", "VÃ©ey", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-60.405, 191.19), [], 10.0),

	("village_11_7", "Kaupangr", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-78.585, 166.08), [], 10.0),

	("village_11_8", "SkiÃ°a", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-48.375, 138.855), [], 10.0),

	("village_11_9", "Konungahella", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-23.235, 131.16), [], 10.0),

	("village_11_10", "SuÃ°reyjar", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-211.995, 127.62), [], 10.0),

	("village_11_11", "Orkneyjar", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-173.55, 139.59), [], 10.0),

	("village_11_12", "Steinker", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-38.31, 196.035), [], 10.0),

	("village_12_1", "Inverness", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-183.72, 119.72), [], 10.0),

	("village_12_2", "Oban", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-198.09, 107.45), [], 10.0),

	("village_12_3", "Wick", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.56, 131.21), [], 10.0),

	("village_12_4", "Scone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.42, 109.46), [], 10.0),

	("village_12_5", "Carluke", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-179.97, 94.46), [], 10.0),

	("village_12_6", "Elgin", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-175.79, 123.62), [], 10.0),

	("village_12_7", "Linlithgow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.63, 101.06), [], 10.0),

	("village_12_8", "Perth", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-179.69, 108.53), [], 10.0),

	("village_13_1", "Cashel", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-234.6, 75.675), [], 10.0),

	("village_13_2", "Ennis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-230.385, 60.12), [], 10.0),

	("village_13_3", "Castlerea", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-205.455, 86.835), [], 10.0),

	("village_13_4", "Raphoe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-227.895, 76.365), [], 10.0),

	("village_13_5", "Corcomroe Abbey", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-237.345, 67.92), [], 10.0),

	("village_13_6", "Omagh Abbey", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-215.475, 77.655), [], 10.0),

	("village_13_7", "Carrick", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-208.02, 89.49), [], 10.0),

	("village_13_8", "Strabane", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-225.375, 85.14), [], 10.0),

	("village_14_1", "Upsalir", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (35.055, 151.215), [], 10.0),

	("village_14_2", "ArbugÃ¦", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (21.6, 145.83), [], 10.0),

	("village_14_3", "Ã�land", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (58.2, 155.385), [], 10.0),

	("village_14_4", "Wybiargh", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (134.64, 159.225), [], 10.0),

	("village_14_5", "RÃºm", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (41.13, 118.965), [], 10.0),

	("village_14_6", "VestrvÃ­k", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (21.63, 121.485), [], 10.0),

	("village_14_7", "Vecsioren", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (3.12, 113.13), [], 10.0),

	("village_14_8", "Ã˜rÃ¦brÃº", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (13.275, 137.355), [], 10.0),

	("village_14_9", "BjÃ¦lbÃº", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (10.725, 123.81), [], 10.0),

	("village_14_10", "FalukÃ¸pang", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-4.38, 125.04), [], 10.0),

	("village_14_11", "SuÃ¾rkÃ¸pang", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (22.02, 129.765), [], 10.0),

	("village_14_12", "SigtÃºnÃ¦", icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.27, 148.95), [], 10.0),

	("village_15_1", "Lvov", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.18, 22.7), [], 10.0),

	("village_15_2", "Buzen", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.18, 20.16), [], 10.0),

	("village_15_3", "Towmacz", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (130.47, 14.78), [], 10.0),

	("village_15_4", "Byikyina", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (124.68, 19.46), [], 10.0),

	("village_15_5", "Vasilev", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (144.45, 10.77), [], 10.0),

	("village_15_6", "Belz", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.82, 35.17), [], 10.0),

	("village_15_7", "Yaroslav", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.53, 32.89), [], 10.0),

	("village_15_8", "Duben", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (138.45, 30.45), [], 10.0),

	("village_15_9", "Mielnik", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.24, 61.52), [], 10.0),

	("village_15_10", "Onut", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (145.0, -4.51), [], 10.0),

	("village_15_11", "Berestye", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (101.71, 55.91), [], 10.0),

	("village_15_12", "Cherven", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (107.84, 36.39), [], 10.0),

	("village_16_1", "Faro", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-224.73, -136.08), []),

	("village_16_2", "Leiria", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-230.16, -100.425), []),

	("village_16_3", "SantarÃ©m", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-222.9, -105.87), []),

	("village_16_4", "AlcÃ¡cer do Sal", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-224.76, -118.215), []),

	("village_16_5", "Beja", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-219.45, -122.21), []),

	("village_16_6", "Portalegre", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-215.85, -99.03), []),

	("village_16_7", "Braga", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-227.68, -78.05), []),

	("village_16_8", "Porto", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-230.25, -85.17), []),

	("village_17_1", "Tarragona", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-143.385, -94.725), []),

	("village_17_2", "Girona", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-124.71, -77.505), []),

	("village_17_3", "Gandia", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-145.335, -117.45), []),

	("village_17_4", "Borriana", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-146.235, -101.985), []),

	("village_17_5", "Calatayud", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-161.25, -85.725), []),

	("village_17_6", "Lleida", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-140.745, -75.675), []),

	("village_17_7", "EmpÃºries", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-114.645, -71.76), []),

	("village_17_8", "DÃ©nia", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-141.885, -113.655), []),

	("village_17_9", "CastellÃ³", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-150.57, -99.78), []),

	("village_17_10", "Luna", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.74, -69.57), []),

	("village_17_11", "Teruel", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.56, -93.345), []),

	("village_18_1", "Cuenca", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-170.655, -93.585), []),

	("village_18_2", "Madrid", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.285, -92.325), []),

	("village_18_3", "CÃ¡diz", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-209.94, -137.46), []),

	("village_18_4", "CÃ³rdoba", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.445, -121.485), []),

	("village_18_5", "Compostela", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-229.845, -58.905), []),

	("village_18_6", "Oviedo", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-193.86, -56.46), []),

	("village_18_7", "Zamora", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-202.53, -77.0505), []),

	("village_18_8", "Soria", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-170.4, -76.59), []),

	("village_18_9", "JaÃ©n", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.555, -117.225), []),

	("village_18_10", "CÃ¡ceres", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-207.285, -97.905), []),

	("village_19_1", "Tudela", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-160.8615, -69.77805), []),

	("village_19_2", "SangÃ¼esa", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-157.82, -64.71), []),

	("village_19_3", "Estella", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-164.91, -63.41), []),

	("village_20_1", "Al-Jazira", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-197.56, -143.97), []),

	("village_20_2", "Marbilla", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-191.22, -141.92), []),

	("village_20_3", "Ronda", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-196.88, -136.71), []),

	("village_20_4", "Lawsa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-185.66, -133.74), []),

	("village_20_5", "Berchat", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-171.435, -132.93), []),

	("village_20_6", "Hisn Al-Lawza", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.585, -126.645), []),

	("village_20_7", "Al-Boks", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-162.42, -126.26), []),

	("village_20_8", "Al-Mediniya", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-187.32, -126.39), []),

	("village_20_9", "Al-Lancharon", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.74, -136.09), []),

	("village_20_10", "Qanalis", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-168.56, -123.25), []),

	("village_20_11", "Qullar", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-164.98, -124.32), []),

	("village_21_1", "Nettuno", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.48, -80.72), []),

	("village_21_2", "Tivoli", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-18.56, -61.0), []),

	("village_21_3", "Spoleto", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.79, -65.56), []),

	("village_21_4", "Ravenna", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-20.87, -44.51), []),

	("village_22_1", "Nikomedia", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (151.83, -90.135), []),

	("village_22_2", "Chalcedon", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (151.755, -85.665), []),

	("village_22_3", "Sardis", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (140.985, -127.97175), []),

	("village_22_4", "Pergamum", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (137.055, -115.65), []),

	("village_22_5", "Laodicea", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (152.4, -132.99), []),

	("village_22_6", "Amorion", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.78, -123.09), []),

	("village_22_7", "Arycanda", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.795, -144.33), []),

	("village_22_8", "Seliniys", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (166.965, -133.68), []),

	("village_22_9", "Philometium", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (171.69, -121.785), []),

	("village_22_10", "Heraclea", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (176.52, -84.405), []),

	("village_22_11", "Kotyaion", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.735, -110.37), []),

	("village_22_12", "Kyzikos", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (137.73, -100.995), []),

	("village_22_13", "Prilep", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (77.265, -86.22), []),

	("village_22_14", "DrÃ¡ma", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (96.82, -83.88), []),

	("village_23_1", "Baalbec", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (225.81, -180.225), []),

	("village_23_3", "Beirut", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (215.94, -175.98), []),

	("village_23_4", "Tyre", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (210.96, -186.51), []),

	("village_23_5", "Selimus", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (184.77, -147.09), []),

	("village_23_6", "Tarlasa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (218.835, -160.86), []),

	("village_23_7", "Jabala", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (218.55, -154.32), []),

	("village_23_8", "Seleucia", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (199.38, -143.415), []),

	("village_23_9", "Limassol", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (190.92, -165.42), []),

	("village_23_10", "Famagusta", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (199.605, -157.92), []),

	("village_23_11", "Homs", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (234.285, -160.215), []),

	("village_23_12", "Tiberias", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (221.12, -175.66), []),

	("village_23_13", "Haifa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (212.87, -178.1), []),

	("village_23_14", "Jaffa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (208.02, -198.375), []),

	("village_24_1", "Messina", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (9.78, -122.77), []),

	("village_24_2", "Caccamo", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-4.57, -124.62), []),

	("village_24_3", "Tropea", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (17.31, -114.81), []),

	("village_24_4", "Pescara", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-0.82, -66.64), []),

	("village_24_5", "Capua", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-2.22, -83.77), []),

	("village_24_6", "Brindisi", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (33.79, -89.69), []),

	("village_24_7", "Salerno", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (3.53, -89.22), []),

	("village_24_8", "Trani", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (22.17, -82.17), []),

	("village_25_1", "Minuf", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.015, -226.095), []),

	("village_25_2", "Ashmun", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (161.055, -229.41), []),

	("village_25_3", "Wadi Miftah", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (174.015, -235.41), []),

	("village_25_4", "Damanhur", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (169.05, -213.165), []),

	("village_25_5", "Zagazig", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (182.88, -216.81), []),

	("village_25_6", "Tanta", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (175.26, -214.62), []),

	("village_25_7", "Abu Hammad", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (179.31, -230.745), []),

	("village_25_8", "Ballah", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.54, -221.415), []),

	("village_25_9", "Wadi Sidr", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.285, -231.18), []),

	("village_25_10", "Marba Dabthan", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (199.92, -237.375), []),

	("village_25_11", "Suluq", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (76.92, -197.37), []),

	("village_25_12", "Ma'an", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (215.385, -232.2), []),

	("village_25_13", "Al Fayyun", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.5, -240.75), []),

	("village_25_14", "Burqush", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (233.16, -174.68), []),

	("village_25_15", "Kiswa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (237.87, -179.06), []),

	("village_25_16", "Ascalon", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (204.165, -206.34), []),

	("village_25_17", "Ramleh", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (205.155, -202.53), []),

	("village_26_1", "Delcus", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (138.105, -77.46), []),

	("village_26_2", "Rodosto", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (135.495, -84.495), []),

	("village_26_3", "Corinthos", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (90.525, -128.19), []),

	("village_26_4", "Athenai", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (93.6, -119.89), []),

	("village_26_5", "Beroea", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.265, -107.595), []),

	("village_26_6", "Kastoria", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.165, -94.26), []),

	("village_26_7", "Dydimoteichon", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (130.605, -73.185), []),

	("village_26_8", "Gallipoli", icon_village_middle_europe|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (120.66, -87.165), []),

	("village_27_1", "Koloneia", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (232.02, -91.785), []),

	("village_27_2", "Theodosiopolis", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (243.645, -100.47), []),

	("village_27_3", "Aksera", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (182.925, -116.145), []),

	("village_27_4", "Cesarea", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (203.91, -114.465), []),

	("village_27_5", "Satala", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (177.675, -129.075), []),

	("village_27_6", "Podandus", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (201.255, -126.45), []),

	("village_27_7", "Karaman", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (189.315, -135.765), []),

	("village_27_8", "Sivas", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (213.36, -101.895), []),

	("village_27_9", "Erzerum", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (237.27, -111.42), []),

	("village_27_10", "Lori", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (261.945, -118.65), []),

	("village_27_11", "Amid", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (261.075, -144.735), []),

	("village_27_12", "Tikrit", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (261.21, -175.98), []),

	("village_27_13", "Manbij", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (229.05, -143.42), []),

	("village_27_14", "Qal'at Ja'bar", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (232.85, -146.86), []),

	("village_28_1", "Qasr Bani Walid", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-9.5355, -202.29), []),

	("village_28_2", "Ksar Hadada", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-43.2, -189.18), []),

	("village_28_3", "Constantine", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-77.13, -145.065), []),

	("village_28_4", "Bona", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.735, -136.395), []),

	("village_28_5", "Setif", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-88.305, -149.025), []),

	("village_28_6", "El Jemaa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.975, -153.03), []),

	("village_28_7", "Dekrnia", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-47.205, -152.985), []),

	("village_28_8", "Mahedia", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-34.17, -163.065), []),

	("village_28_9", "Medenine", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-35.295, -180.195), []),

	("village_28_10", "Al Bu'aryat", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.845, -209.85), []),

	("village_29_1", "ZveÄ�an", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (72.06, -66.84), []),

	("village_29_2", "Liplian", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (72.64, -75.79), []),

	("village_29_3", "PeÄ‡", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (60.66, -76.38), []),

	("village_29_4", "Skadar", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (56.87, -81.24), []),

	("village_29_5", "Blagaj", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.88, -60.6), []),

	("village_29_6", "Rudnic", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.34, -48.34), []),

	("village_30_1", "Nish", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.76, -59.41), []),

	("village_30_2", "Varna", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (138.43, -56.24), []),

	("village_30_3", "Cherven", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (118.83, -54.72), []),

	("village_30_4", "Konstantsa", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (143.38, -46.11), []),

	("village_30_5", "Lovech", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (105.02, -58.5), []),

	("village_30_6", "Skopie", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.48, -79.03), []),

	("village_30_7", "Boruy", icon_village_byzantium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.02, -74.75), []),

	("village_31_1", "Melilla", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-171.15, -161.88), []),

	("village_31_2", "Rabat", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-204.75, -169.8), []),

	("village_31_3", "Tenes", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-140.4, -150.015), []),

	("village_31_4", "Tlemsen", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-153.6, -156.465), []),

	("village_31_5", "Safi", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-219.675, -179.31), []),

	("village_31_6", "Ourzazate", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-202.62, -188.385), []),

	("village_31_7", "Tetuan", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-196.965, -154.74), []),

	("village_31_8", "Corso", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-104.1, -146.115), []),

	("village_32_1", "Caorle", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-16.09, -27.61), []),

	("village_32_2", "Chioggia", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-19.88, -32.43), []),

	("village_32_3", "Sita", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (119.52, -160.34), []),

	("village_32_4", "Canea", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (95.09, -155.91), []),

	("village_32_5", "PoreÄ�", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.94, -33.31), []),

	("village_32_6", "Sibinicum ", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (20.56, -56.61), []),

	("village_32_7", "Zara", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (14.23, -51.59), []),

	("village_32_8", "Rethymno", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (103.49, -157.67), []),

	("village_33_1", "Varnupiai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (94.0, 72.89), []),

	("village_33_2", "Pajevonis", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.83, 71.76), []),

	("village_33_2", "Pajevonis", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.83, 71.76), []),

	("village_34_1", "MikutÄ—liai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (80.73, 80.3), []),

	("village_34_1", "MikutÄ—liai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (80.73, 80.3), []),

	("village_34_1", "MikutÄ—liai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (80.73, 80.3), []),

	("village_35_1", "CiecerÄ—", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (80.0, 104.71), []),

	("village_35_2", "Palanga", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.9, 101.79), []),

	("village_35_3", "Gandinga", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.92, 100.22), []),

	("village_36_1", "Gurkiai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (87.57, 98.13), []),

	("village_36_1", "Gurkiai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (87.57, 98.13), []),

	("village_36_1", "Gurkiai", icon_village_eastern|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (87.57, 98.13), []),

	("village_37_1", "Dolbadarn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-184.7, 66.9), []),

	("village_37_2", "Dolwyddelan", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-181.08, 62.38), []),

	("village_37_3", "Nefyn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-189.18, 64.48), []),

	("village_38_1", "Rapallo", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-53.2, -42.68), []),

	("village_38_2", "Chiavari", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-49.26, -44.21), []),

	("village_38_4", "Porto Vecchio", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-50.38, -79.85), []),

	("village_38_5", "Quartu S. Elena", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-49.96, -108.3), []),

	("village_39_1", "S. Giuliano", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-33.87, -53.04), []),

	("village_39_2", "Calci", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-39.16, -53.35), []),

	("village_39_3", "Ardara", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-53.61, -88.25), []),

	("village_39_4", "Tharres", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.64, -98.81), []),

	("village_40_1", "Bologna", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-27.21, -43.24), []),

	("village_40_2", "Brescia", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-39.33, -29.81), []),

	("village_40_3", "Alessandria", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.76, -35.6), []),

	("village_40_4", "Este", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-24.47, -31.75), []),

	("village_41_1", "Belluno", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-20.31, -25.76), []),

	("village_41_2", "Cremona", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-45.37, -37.36), []),

	("village_41_3", "Soncino", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-42.24, -32.45), []),

	("village_41_4", "Asti", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-62.01, -39.93), []),

	("village_42_1", "HradiÅ¡tÄ›", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (6.75, 33.11), [], 10.0),

	("village_42_2", "Brno", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (11.4, 20.71), [], 35.0),

	("village_42_3", "MÄ›lnÃ­k", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.37, 32.43), [], 87.0),

	("village_42_4", "StarÃ¡ Boleslav", icon_village_italy|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (3.25, 30.14), [], 45.0),

	("village_player", "Crap", icon_village_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-104.1, -146.115), []),

	("salt_mine", "Salt Mine", icon_town|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-160.425, -139.71), []),

	("four_ways_inn", "Four Ways Inn", icon_town|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-43.89, -113.355), []),

	("test_scene", "test scene", icon_town|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-43.875, -105.96), []),

	("battlefields", "battlefields", icon_town|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-43.605, -109.035), []),

	("dhorak_keep", "Dhorak Keep", icon_town|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-76.605, -132.315), []),

	("training_ground", "Training Ground", icon_training_ground|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-101.325, 9.0), []),

	("training_ground_1", "Training Field I", icon_training_ground|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (48.705, 63.015), [], 100.0),

	("training_ground_2", "Training Field II", icon_training_ground|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.12, -18.63), [], 100.0),

	("bridge_1", "{!}1", icon_bridge_a|pf_disabled|pf_is_static|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (46.935, 76.83), [], -72.0),

	("bridge_2", "{!}2", icon_bridge_a|pf_disabled|pf_is_static|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (138.6, -29.985), [], -20.0),

	("bridge_3", "{!}3", icon_bridge_a|pf_disabled|pf_is_static|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-15.98, 9.14), [], -60.72),

	("ship_1", "1", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-156.33, -30.66), [], -145.0),

	("ship_2", "2", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-127.395, 34.68), [], -188.0),

	("ship_3", "3", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-132.435, 46.86), [], -147.0),

	("ship_4", "4", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-176.835, 104.055), [], 27.0),

	("ship_5", "5", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-171.54, 139.335), [], -64.0),

	("ship_6", "6", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-155.16, 151.395), [], -64.0),

	("ship_7", "7", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-211.59, 171.24), [], -64.0),

	("ship_8", "8", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-217.34, 114.4), [], -64.0),

	("ship_9", "9", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.565, 100.815), [], -64.0),

	("ship_10", "9", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-205.725, 77.235), [], -64.0),

	("ship_11", "11", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-208.215, 54.78), [], -64.0),

	("ship_12", "12", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-182.175, 45.81), [], -64.0),

	("ship_13", "13", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-188.13, 79.35), [], -64.0),

	("ship_14", "14", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-42.57, 90.735), [], -145.0),

	("ship_15", "15", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-34.98, 94.545), [], -188.0),

	("ship_16", "16", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-30.225, 95.07), [], -147.0),

	("ship_17", "17", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.545, 119.1), [], 27.0),

	("ship_18", "18", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.35, 119.565), [], -64.0),

	("ship_19", "19", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.255, 137.775), [], -64.0),

	("ship_20", "20", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (46.11, 154.17), [], -64.0),

	("ship_21", "21", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (54.765, 153.555), [], -64.0),

	("ship_22", "22", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (68.805, 158.58), [], -64.0),

	("ship_23", "23", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.855, 146.16), [], -64.0),

	("ship_24", "24", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (100.245, 118.83), [], -64.0),

	("ship_25", "25", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (77.52, 129.3), [], -64.0),

	("ship_26", "26", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.8, 100.5), [], -64.0),

	("ship_27", "27", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (47.94, 85.21), [], -64.0),

	("ship_28", "28", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-24.96, 79.05), [], -64.0),

	("ship_29", "29", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-59.625, 75.225), [], -64.0),

	("ship_30", "30", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-61.14, 113.37), [], -64.0),

	("ship_31", "31", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-35.91, 137.87), [], -64.0),

	("ship_32", "32", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-33.93, 209.55), [], -64.0),

	("ship_33", "33", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-87.24, 142.485), [], -64.0),

	("ship_34", "34", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-166.59, -7.8), [], -64.0),

	("ship_35", "35", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-233.94, -86.565), [], -64.0),

	("ship_36", "36", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-235.035, -117.42), [], -64.0),

	("ship_37", "37", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-201.15, -148.41), [], -64.0),

	("ship_38", "38", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-135.03, -89.55), [], -64.0),

	("ship_39", "39", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-99.6, -55.89), [], -64.0),

	("ship_40", "40", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-55.635, -44.145), [], -64.0),

	("ship_41", "41", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.065, -82.47), [], -64.0),

	("ship_42", "42", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-7.965, -121.74), [], -64.0),

	("ship_43", "43", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (13.86, -120.33), [], -64.0),

	("ship_44", "44", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-18.735, -37.77), [], -64.0),

	("ship_45", "45", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.425, -64.725), [], -64.0),

	("ship_46", "46", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (99.345, -126.825), [], -64.0),

	("ship_47", "47", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.85, -94.02), [], -64.0),

	("ship_48", "48", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (149.235, -85.71), [], -64.0),

	("ship_49", "49", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (155.07, -33.42), [], -64.0),

	("ship_50", "50", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (193.8, -44.16), [], -64.0),

	("ship_51", "51", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (244.44, -83.44), [], -64.0),

	("ship_52", "52", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (129.375, -127.32), [], -64.0),

	("ship_53", "53", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (196.605, -153.135), [], -64.0),

	("ship_54", "54", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (214.08, -146.28), [], -64.0),

	("ship_55", "55", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (207.435, -188.145), [], -64.0),

	("ship_56", "56", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (176.57, -205.46), [], -64.0),

	("ship_57", "57", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.255, -206.265), [], -64.0),

	("ship_58", "58", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (58.155, -196.575), [], -64.0),

	("ship_59", "59", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.74, -191.37), [], -64.0),

	("ship_60", "60", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.53, -131.08), [], -64.0),

	("ship_61", "61", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-108.45, -137.775), [], -64.0),

	("ship_62", "62", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-140.16, -144.855), [], -64.0),

	("ship_63", "63", icon_ship_on_land|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.19, -96.13), [], -64.0),

	("looter_spawn_point", "{!}looter sp", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-16.155, 20.565), [(trp_looter, 15, 0)]),

	("taiga_bandit_spawn_point_1", "the tundra 1", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (156.39, 107.58), []),

	("taiga_bandit_spawn_point_2", "the tundra 2", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (85.215, 165.66), []),

	("steppe_bandit_spawn_point_1", "the steppes 1", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (132.6, 16.65), []),

	("steppe_bandit_spawn_point_2", "the steppes 2", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (169.38, 19.32), []),

	("forest_bandit_spawn_point_1", "the forests 1", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-116.94, -53.055), []),

	("forest_bandit_spawn_point_2", "the forests 2", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (56.19, -9.735), []),

	("forest_bandit_spawn_point_3", "the forests 3", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (48.0, -54.285), []),

	("forest_bandit_spawn_point_4", "the forests 4", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (78.6, -114.42), []),

	("forest_bandit_spawn_point_5", "the forests 5", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (189.6, -117.075), []),

	("forest_bandit_spawn_point_6", "the forests 6", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (221.445, -98.025), []),

	("forest_bandit_spawn_point_7", "the forests 7", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-56.085, 44.325), []),

	("mountain_bandit_spawn_point_1", "the highways 1", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (134.355, 99.675), []),

	("mountain_bandit_spawn_point_2", "the highways 2", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-222.555, 71.265), []),

	("mountain_bandit_spawn_point_3", "the highways 3", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-160.395, 72.96), []),

	("mountain_bandit_spawn_point_4", "the highways 4", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (36.6, 4.485), []),

	("mountain_bandit_spawn_point_5", "the highways 5", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-131.115, 10.425), []),

	("mountain_bandit_spawn_point_6", "the highways 6", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (17.955, 46.41), [], 100.0),

	("mountain_bandit_spawn_point_7", "the highways 7", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (160.47, 67.44), [], 100.0),

	("mountain_bandit_spawn_point_8", "the highways 8", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-101.115, 30.375), [], 100.0),

	("mountain_bandit_spawn_point_9", "the highways 9", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-63.81, 32.88), [], 100.0),

	("mountain_bandit_spawn_point_10", "the highways 10", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (46.38, 54.915), [], 100.0),

	("mountain_bandit_spawn_point_11", "the highways 11", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-10.305, 169.56), [], 100.0),

	("mountain_bandit_spawn_point_12", "the highways 12", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-35.97, 51.51), [], 100.0),

	("mountain_bandit_spawn_point_13", "the highways 13", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (94.875, 52.71), [], 100.0),

	("mountain_bandit_spawn_point_14", "the highways 14", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-136.02, -19.005), [], 100.0),

	("mountain_bandit_spawn_point_15", "the highways 15", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-183.345, -96.255), [], 100.0),

	("mountain_bandit_spawn_point_16", "the highways 16", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-27.465, 168.435), [], 100.0),

	("mountain_bandit_spawn_point_17", "the highways 17", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (59.865, -47.82), [], 100.0),

	("mountain_bandit_spawn_point_18", "the highways 18", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (140.13, -82.41), [], 100.0),

	("mountain_bandit_spawn_point_19", "the highways 19", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (157.095, -127.83), [], 100.0),

	("mountain_bandit_spawn_point_20", "the highways 20", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (233.25, -152.91), [], 100.0),

	("mountain_bandit_spawn_point_21", "the highways 21", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (9.78, -86.265), [], 100.0),

	("sea_raider_spawn_point_1", "the coast 1", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (39.705, 148.26), []),

	("sea_raider_spawn_point_2", "the coast 2", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (81.39, 118.71), []),

	("sea_raider_spawn_point_3", "the coast 3", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-89.715, 58.35), []),

	("sea_raider_spawn_point_4", "the coast 4", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-27.045, 76.485), []),

	("sea_raider_spawn_point_5", "the coast 5", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-115.71, 36.495), []),

	("sea_raider_spawn_point_6", "the coast 6", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-88.125, 155.01), []),

	("sea_raider_spawn_point_7", "the coast 7", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-175.44, 9.48), []),

	("sea_raider_spawn_point_8", "the coast 8", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (51.99, 80.745), []),

	("sea_raider_spawn_point_9", "the coast 9", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-155.565, 36.615), []),

	("sea_raider_spawn_point_10", "the coast 10", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-28.83, 132.885), []),

	("sea_raider_spawn_point_11", "the coast 11", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-165.165, 119.46), []),

	("sea_raider_spawn_point_12", "the coast 12", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (31.155, 97.185), []),

	("sea_raider_spawn_point_13", "the coast 13", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (132.81, 142.845), []),

	("sea_raider_spawn_point_14", "the coast 14", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (185.745, -77.205), []),

	("sea_raider_spawn_point_15", "the coast 15", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-180.495, -147.915), []),

	("sea_raider_spawn_point_16", "the coast 16", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-20.4, -138.615), []),

	("sea_raider_spawn_point_17", "the coast 17", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (108.63, -110.64), []),

	("desert_bandit_spawn_point_1", "the desert 1", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (163.32, -222.0), []),

	("desert_bandit_spawn_point_2", "the desert 2", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (222.945, -196.965), []),

	("desert_bandit_spawn_point_3", "the desert 3", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-27.015, -193.155), []),

	("desert_bandit_spawn_point_4", "the desert 4", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-196.755, -170.19), []),

	("desert_bandit_spawn_point_5", "the desert 5", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-81.105, -150.87), []),

	("spawn_points_end", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_looter, 15, 0)]),

	("reserved_1", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_looter, 15, 0)]),

	("reserved_2", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_looter, 15, 0)]),

	("reserved_3", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_looter, 15, 0)]),

	("reserved_4", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_looter, 15, 0)]),

	("reserved_5", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_looter, 15, 0)]),

	("freelancer_party_backup", "{!}", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

]