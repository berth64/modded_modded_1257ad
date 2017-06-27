# -*- coding: utf-8 -*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

factions = [
	("no_faction", "No Faction", 0, 0.9, []),

	("commoners", "Commoners", 0, 0.1, [("undeads",-0.70),("forest_bandits",-0.20),("mountain_bandits",-0.20),("outlaws",-0.60),("player_faction",0.10)]),

	("outlaws", "Outlaws", 0, 0.5, [("kingdom_22",-0.05),("kingdom_34",-0.05),("crusade",-0.05),("kingdom_15",-0.05),("kingdom_26",-0.05),("kingdom_10",-0.05),("kingdom_35",-0.05),("kingdom_16",-0.05),("kingdom_9",-0.05),("kingdom_6",-0.05),("kingdom_41",-0.05),("kingdom_12",-0.05),("kingdom_33",-0.05),("kingdom_30",-0.05),("kingdom_37",-0.05),("commoners",-0.60),("kingdom_42",-0.05),("kingdom_5",-0.05),("kingdom_2",-0.05),("kingdom_13",-0.05),("kingdom_19",-0.05),("innocents",-0.05),("kingdom_1",-0.05),("player_supporters_faction",-0.05),("kingdom_3",-0.05),("kingdom_23",-0.05),("kingdom_31",-0.05),("kingdom_11",-0.05),("kingdom_29",-0.05),("kingdom_20",-0.05),("kingdom_38",-0.05),("kingdom_4",-0.05),("merchants",-0.50),("kingdom_39",-0.05),("kingdom_18",-0.05),("kingdom_27",-0.05),("kingdom_28",-0.05),("manhunters",-0.60),("kingdom_24",-0.05),("kingdom_36",-0.05),("kingdom_25",-0.05),("kingdom_32",-0.05),("kingdom_40",-0.05),("kingdom_7",-0.05),("kingdom_17",-0.05),("papacy",-0.05),("kingdom_8",-0.05),("player_faction",-0.15),("kingdom_14",-0.05)], [], 0x00888888),

	("neutral", "Neutral", 0, 0.1, [], [], 0x00ffffff),

	("innocents", "Innocents", ff_always_hide_label, 0.5, [("dark_knights",-0.90),("outlaws",-0.05)]),

	("merchants", "Merchants", ff_always_hide_label, 0.5, [("forest_bandits",-0.50),("deserters",-0.50),("mountain_bandits",-0.50),("outlaws",-0.50)]),

	("dark_knights", "{!}Dark Knights", 0, 0.5, [("innocents",-0.90),("player_faction",-0.40)]),

	("culture_finnish", "{!}culture finnish", 0, 0.9, []),

	("culture_mazovian", "{!}culture mazovian", 0, 0.9, []),

	("culture_serbian", "{!}culture serbian", 0, 0.9, []),

	("culture_welsh", "{!}culture welsh", 0, 0.9, []),

	("culture_teutonic", "{!}culture teutonic", 0, 0.9, []),

	("culture_balkan", "{!}culture balkan", 0, 0.9, []),

	("culture_rus", "{!}culture rus", 0, 0.9, []),

	("culture_nordic", "{!}culture nordic", 0, 0.9, []),

	("culture_baltic", "{!}culture baltic", 0, 0.9, []),

	("culture_marinid", "{!}culture marinid", 0, 0.9, []),

	("culture_mamluke", "{!}culture mamluke", 0, 0.9, []),

	("culture_byzantium", "{!}culture byzantium", 0, 0.9, []),

	("culture_iberian", "{!}culture iberian", 0, 0.9, []),

	("culture_italian", "{!}culture italian", 0, 0.9, []),

	("culture_andalus", "{!}culture andalus", 0, 0.9, []),

	("culture_gaelic", "{!}culture gaelic", 0, 0.9, []),

	("culture_anatolian_christian", "{!}culture anatolian", 0, 0.9, []),

	("culture_anatolian", "{!}culture anatolian", 0, 0.9, []),

	("culture_scotish", "{!}culture scotish", 0, 0.9, []),

	("culture_western", "{!}culture western", 0, 0.9, []),

	("culture_mongol", "{!}culture mongol", 0, 0.9, []),

	("player_faction", "Player Faction", 0, 0.9, [("peasant_rebels",-0.40),("commoners",0.10),("dark_knights",-0.40),("black_khergits",-0.30),("undeads",-0.50),("forest_bandits",-0.15),("player_supporters_faction",1.00),("deserters",-0.10),("manhunters",0.10),("mountain_bandits",-0.15),("outlaws",-0.15)], [], 0x00cccccc),

	("player_supporters_faction", "Player's Supporters", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("player_faction",1.00)], [], 0x00468493),

	("kingdom_1", "Ordo Teutonicus", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_6",0.50),("black_khergits",-0.02),("forest_bandits",-0.05),("kingdom_4",0.10),("deserters",-0.02),("mountain_bandits",-0.05),("kingdom_8",-0.20),("outlaws",-0.05),("kingdom_14",0.10)], [], 0x00e9e9e9),

	("kingdom_2", "Regnum Litus", 0, 0.9, [("kingdom_34",0.50),("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_35",0.50),("kingdom_33",0.50),("black_khergits",-0.02),("forest_bandits",-0.05),("kingdom_3",0.10),("deserters",-0.02),("kingdom_36",0.50),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00badeb2),

	("kingdom_3", "Altan Ordyn Uls", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_5",-1.00),("kingdom_2",0.10),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_7",-1.00),("mountain_bandits",-0.05),("kingdom_8",0.10),("outlaws",-0.05)], [], 0x00a33e32),

	("kingdom_4", "Regnum Daniae", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_1",0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x009b1a1a),

	("kingdom_5", "Regnum Poloniae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_3",-1.00),("deserters",-0.02),("kingdom_7",0.10),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00ff0000),

	("kingdom_6", "Sacrum Imperium Romanum", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_41",1.00),("kingdom_42",1.00),("kingdom_1",0.50),("forest_bandits",-0.05),("kingdom_38",0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00ffcc00),

	("kingdom_7", "Regnum Hungariae", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_5",0.10),("forest_bandits",-0.05),("kingdom_3",-1.00),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00289327),

	("kingdom_8", "Novgorod Weliki", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_1",-0.20),("forest_bandits",-0.05),("kingdom_3",0.10),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_14",-0.20)], [], 0x009e0b6f),

	("kingdom_9", "Regnum Angliae", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_37",-1.00),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00931124),

	("kingdom_10", "Regnum Franciae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00002395),

	("kingdom_11", "Kongeriket Norge", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_12",-0.20),("kingdom_13",-0.20),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x006669d6),

	("kingdom_12", "Regnum Scotiae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_11",-0.20),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0022d8a7),

	("kingdom_13", "Scotia Maior", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_11",-0.20),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0077b322),

	("kingdom_14", "Konungariket Sverige", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_1",0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("kingdom_8",-0.20),("outlaws",-0.05)], [], 0x003254b5),

	("kingdom_15", "Regnum Galiciae et Lodomeriae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00ece874),

	("kingdom_16", "Regnum Portugaliae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_20",-40.00),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00003399),

	("kingdom_17", "Corona Aragonae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0007b233),

	("kingdom_18", "Regnum Castiliae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_20",-40.00),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00d85ac4),

	("kingdom_19", "Regnum Navarrae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00f7f497),

	("kingdom_20", "Imarat al Nasri", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_16",-40.00),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_18",-40.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00abc904),

	("papacy", "Patrimonium Sancti Petri", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00fff17a),

	("kingdom_22", "Basileia ton Rhomaion", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_26",-1.00),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00760d0d),

	("kingdom_23", "Regnum Hierosolymitanum", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_27",0.10),("kingdom_25",-1.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00f3efb8),

	("kingdom_24", "Regnum Siciliae", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00799cb5),

	("kingdom_25", "Sultanat al Mamalik", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("forest_bandits",-0.05),("kingdom_23",-1.00),("deserters",-0.02),("kingdom_27",-1.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00ebe800),

	("kingdom_26", "Imperium Romaniae", 0, 0.9, [("kingdom_22",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00b26248),

	("kingdom_27", "Ilkhanate", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("forest_bandits",-0.05),("kingdom_23",0.10),("deserters",-0.02),("kingdom_25",-1.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00e19004),

	("kingdom_28", "Sultanat al Hafsi", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00a48460),

	("kingdom_29", "Kraljevstvo Srbsko", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00b38263),

	("kingdom_30", "Balgarsko Tsarstvo", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0076a296),

	("kingdom_31", "Sultanat al Marini", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00c1272d),

	("kingdom_32", "Repubblica di Venezia", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00c1172d),

	("kingdom_33", "Jotvingiai", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_2",0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x003e7583),

	("kingdom_34", "Pruteni", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_2",0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0065c0d7),

	("kingdom_35", "Kursi", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_2",0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x003e7583),

	("kingdom_36", "Zemaiciai", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_2",0.50),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00529cae),

	("kingdom_37", "Cymry", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_9",-1.00),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0000dc00),

	("kingdom_38", "Respublica Ianuensis", 0, 0.9, [("peasant_rebels",-0.10),("crusade",-0.50),("kingdom_6",0.50),("forest_bandits",-0.05),("kingdom_39",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00e1900a),

	("kingdom_39", "Respublica Pisarum", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_38",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0007e233),

	("kingdom_40", "Comuni Guelfi", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_41",-0.80),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x003254e5),

	("kingdom_41", "Comuni Ghibellini", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_6",1.00),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_40",-0.80),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x009e026a),

	("kingdom_42", "ÄŒeskÃ© KrÃ¡lovstvÃ­", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_6",1.00),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00e8e8e8),

	("kingdoms_end", "{!}kingdoms end", 0, 0.0, []),

	("robber_knights", "{!}robber knights", 0, 0.1, []),

	("khergits", "{!}Khergits", 0, 0.5, []),

	("black_khergits", "{!}Black Khergits", 0, 0.5, [("kingdom_2",-0.02),("kingdom_1",-0.02),("player_faction",-0.30)]),

	("manhunters", "Captivos Proscriptorum", 0, 0.5, [("forest_bandits",-0.60),("deserters",-0.60),("mountain_bandits",-0.60),("outlaws",-0.60),("player_faction",0.10)]),

	("deserters", "Deserti", 0, 0.5, [("kingdom_22",-0.02),("kingdom_34",-0.02),("crusade",-0.02),("kingdom_15",-0.02),("kingdom_26",-0.02),("kingdom_10",-0.02),("kingdom_35",-0.02),("kingdom_16",-0.02),("kingdom_9",-0.02),("kingdom_6",-0.02),("kingdom_41",-0.02),("kingdom_12",-0.02),("kingdom_33",-0.02),("kingdom_30",-0.02),("kingdom_37",-0.02),("kingdom_42",-0.02),("kingdom_5",-0.02),("kingdom_2",-0.02),("kingdom_13",-0.02),("kingdom_19",-0.02),("kingdom_1",-0.02),("player_supporters_faction",-0.02),("kingdom_3",-0.02),("kingdom_23",-0.02),("kingdom_31",-0.02),("kingdom_11",-0.02),("kingdom_29",-0.02),("kingdom_20",-0.02),("kingdom_38",-0.02),("kingdom_4",-0.02),("merchants",-0.50),("kingdom_39",-0.02),("kingdom_18",-0.02),("kingdom_27",-0.02),("kingdom_28",-0.02),("manhunters",-0.60),("kingdom_24",-0.02),("kingdom_36",-0.02),("kingdom_25",-0.02),("kingdom_32",-0.02),("kingdom_40",-0.02),("kingdom_7",-0.02),("kingdom_17",-0.02),("papacy",-0.02),("kingdom_8",-0.02),("player_faction",-0.10),("kingdom_14",-0.02)], [], 0x00888888),

	("mountain_bandits", "Montes Sicarii", 0, 0.5, [("kingdom_22",-0.05),("kingdom_34",-0.05),("crusade",-0.05),("kingdom_15",-0.05),("kingdom_26",-0.05),("kingdom_10",-0.05),("kingdom_35",-0.05),("kingdom_16",-0.05),("kingdom_9",-0.05),("kingdom_6",-0.05),("kingdom_41",-0.05),("kingdom_12",-0.05),("kingdom_33",-0.05),("kingdom_30",-0.05),("kingdom_37",-0.05),("commoners",-0.20),("kingdom_42",-0.05),("kingdom_5",-0.05),("kingdom_2",-0.05),("kingdom_13",-0.05),("kingdom_19",-0.05),("kingdom_1",-0.05),("player_supporters_faction",-0.05),("kingdom_3",-0.05),("kingdom_23",-0.05),("kingdom_31",-0.05),("kingdom_11",-0.05),("kingdom_29",-0.05),("kingdom_20",-0.05),("kingdom_38",-0.05),("kingdom_4",-0.05),("merchants",-0.50),("kingdom_39",-0.05),("kingdom_18",-0.05),("kingdom_27",-0.05),("kingdom_28",-0.05),("manhunters",-0.60),("kingdom_24",-0.05),("kingdom_36",-0.05),("kingdom_25",-0.05),("kingdom_32",-0.05),("kingdom_40",-0.05),("kingdom_7",-0.05),("kingdom_17",-0.05),("papacy",-0.05),("kingdom_8",-0.05),("player_faction",-0.15),("kingdom_14",-0.05)], [], 0x00888888),

	("forest_bandits", "Silvae Sicarii", 0, 0.5, [("kingdom_22",-0.05),("kingdom_34",-0.05),("crusade",-0.05),("kingdom_15",-0.05),("kingdom_26",-0.05),("kingdom_10",-0.05),("kingdom_35",-0.05),("kingdom_16",-0.05),("kingdom_9",-0.05),("kingdom_6",-0.05),("kingdom_41",-0.05),("kingdom_12",-0.05),("kingdom_33",-0.05),("kingdom_30",-0.05),("kingdom_37",-0.05),("commoners",-0.20),("kingdom_42",-0.05),("kingdom_5",-0.05),("kingdom_2",-0.05),("kingdom_13",-0.05),("kingdom_19",-0.05),("kingdom_1",-0.05),("player_supporters_faction",-0.05),("kingdom_3",-0.05),("kingdom_23",-0.05),("kingdom_31",-0.05),("kingdom_11",-0.05),("kingdom_29",-0.05),("kingdom_20",-0.05),("kingdom_38",-0.05),("kingdom_4",-0.05),("merchants",-0.50),("kingdom_39",-0.05),("kingdom_18",-0.05),("kingdom_27",-0.05),("kingdom_28",-0.05),("manhunters",-0.60),("kingdom_24",-0.05),("kingdom_36",-0.05),("kingdom_25",-0.05),("kingdom_32",-0.05),("kingdom_40",-0.05),("kingdom_7",-0.05),("kingdom_17",-0.05),("papacy",-0.05),("kingdom_8",-0.05),("player_faction",-0.15),("kingdom_14",-0.05)], [], 0x00888888),

	("undeads", "{!}Undeads", 0, 0.5, [("commoners",-0.70),("player_faction",-0.50)]),

	("slavers", "{!}Slavers", 0, 0.1, []),

	("peasant_rebels", "{!}Peasant Rebels", 0, 1.0, [("kingdom_22",-0.10),("kingdom_34",-0.10),("crusade",-0.10),("kingdom_15",-0.10),("kingdom_26",-0.10),("kingdom_10",-0.10),("kingdom_35",-0.10),("kingdom_16",-0.10),("kingdom_9",-0.10),("noble_refugees",-1.00),("kingdom_6",-0.10),("kingdom_41",-0.10),("kingdom_12",-0.10),("kingdom_33",-0.10),("kingdom_30",-0.10),("kingdom_37",-0.10),("kingdom_42",-0.10),("kingdom_5",-0.10),("kingdom_2",-0.10),("kingdom_13",-0.10),("kingdom_19",-0.10),("kingdom_1",-0.10),("player_supporters_faction",-0.10),("kingdom_3",-0.10),("kingdom_23",-0.10),("kingdom_31",-0.10),("kingdom_11",-0.10),("kingdom_29",-0.10),("kingdom_20",-0.10),("kingdom_38",-0.10),("kingdom_4",-0.10),("kingdom_39",-0.10),("kingdom_18",-0.10),("kingdom_27",-0.10),("kingdom_28",-0.10),("kingdom_24",-0.10),("kingdom_36",-0.10),("kingdom_25",-0.10),("kingdom_32",-0.10),("kingdom_40",-0.10),("kingdom_7",-0.10),("kingdom_17",-0.10),("papacy",-0.10),("kingdom_8",-0.10),("player_faction",-0.40),("kingdom_14",-0.10)]),

	("noble_refugees", "{!}Noble Refugees", 0, 0.5, [("peasant_rebels",-1.00)]),

	("crusade", "Crusaders", 0, 0.9, [("kingdom_34",-0.50),("peasant_rebels",-0.10),("kingdom_35",-0.50),("kingdom_33",-0.50),("kingdom_2",-0.50),("forest_bandits",-0.05),("kingdom_3",-0.50),("kingdom_31",-0.50),("kingdom_20",-0.50),("kingdom_38",-0.50),("deserters",-0.02),("kingdom_27",-0.50),("kingdom_28",-0.50),("kingdom_36",-0.50),("kingdom_25",-0.50),("mountain_bandits",-0.05),("papacy",-0.50),("outlaws",-0.05)], [], 0x00fff17a),

	("end_minor_faction", "Village Idiots", 0, 0.9, [], [], 0x00fff17a),

]