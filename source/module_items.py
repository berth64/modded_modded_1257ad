# -*- coding: utf-8 -*-
from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
	["no_item", "Items begin", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["tutorial_spear1", "Kettle Helm with Mail Coif", [("kettlehat1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_club1", "Kettle Helm with Padding", [("kettlehat_c_green", imodbits_none), ("inv_kettlehat_c_green", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["tutorial_battle_axe1", "Kettle Helm with Padding", [("chapel-de-fer_cloth3", imodbits_none), ("inv_chapel-de-fer_cloth3", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["tutorial_arrows1", "Kettle Helm with Padding", [("chapel-de-fer_cloth2", imodbits_none), ("inv_chapel-de-fer_cloth2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["tutorial_bolts1", "Kettle Helm with Padding", [("chapel-de-fer_cloth1", imodbits_none), ("inv_chapel-de-fer_cloth1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["tutorial_short_bow1", "Surcoat over Mail Haubergeon", [("rnd_surcoat2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_crossbow1", "Surcoat over Mail Haubergeon", [("rnd_surcoat3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_throwing_daggers1", "Surcoat over Mail Haubergeon", [("rnd_surcoat4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_saddle_horse1", "Surcoat over Mail Haubergeon", [("rnd_surcoat5", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_shield1", "Surcoat over Mail Haubergeon", [("rnd_surcoat6", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_staff_no_attack1", "Surcoat over Mail Haubergeon", [("rnd_surcoat7", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_staff1", "Surcoat over Mail Haubergeon", [("rnd_surcoat8", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_sword1", "Surcoat over Mail Haubergeon", [("rnd_surcoat9", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_axe1", "Surcoat over Mail Haubergeon", [("rnd_surcoat10", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_dagger1", "Surcoat over Mail Haubergeon", [("rnd_surcoat11", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_12_1", "Surcoat over Mail Haubergeon", [("rnd_surcoat12", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_sword", "Wooden Club", [("gaelic_stick", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(59), imodbits_none],

	["heavy_practice_sword", "Shillelagh", [("long_stick", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 300, thrust_damage(24, blunt)|hit_points(27648)|spd_rtng(78)|abundance(100)|weight(3.0)|swing_damage(24, blunt)|difficulty(6)|weapon_length(101), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_gaelic, fac_kingdom_13]],

	["practice_dagger", "Wooden Club", [("maglorg", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(58), imodbits_none],

	["lyre1", "Templar Surcoat over Mail Haubergeon", [("Chinese_Hochmeister", imodbits_none), ("Chinese_Templar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_western]],

	["lyre1", "Templar Surcoat over Mail Haubergeon", [("Chinese_Hochmeister", imodbits_none), ("Chinese_Templar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_western]],

	["lute1", "Billhook-fork", [("1429_bill_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["arena_axe", "Cleaving Voulge", [("1429_voulge_6", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_poleaxe, 400, thrust_damage(45, cut)|hit_points(14029)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(152), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["arena_lance", "Fauchard", [("1429_fauchard_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_no_blur, itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(28672)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(186), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["practice_staff", "Broken Spear", [("vik_broken_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 15, thrust_damage(20, cut)|hit_points(33792)|spd_rtng(100)|abundance(100)|weight(1.0)|swing_damage(15, blunt)|weapon_length(108), imodbit_cracked|imodbit_bent],

	["practice_lance", "Fauchard-glaive", [("1429_fauchard_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 440, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(171), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["practice_shield", "Wooden Shield", [("lithuanian_shield_old", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 114, hit_points(47)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield],

	["cudgel", "Club", [("caribbean_club_2h", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 300, thrust_damage(24, blunt)|hit_points(27648)|spd_rtng(82)|abundance(100)|weight(3.0)|swing_damage(24, blunt)|difficulty(6)|weapon_length(87), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_gaelic, fac_kingdom_13]],

	["practice_crossbow", "Fauchard-fork", [("1429_fauchard_fork_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(197), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["practice_javelin", "Fauchard-fork", [("1429_fauchard_fork_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(200), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["practice_javelin_melee1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_02_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_throwing_daggers1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_03_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_throwing_daggers_100_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_06_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_horse", "Glaive-fork", [("1429_glaive_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(29696)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["club", "Truncheon", [("caribbean_club", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(50), imodbits_none],

	["practice_bolts1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_13_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_arrows_10_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_14_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_arrows_100_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_17_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_bolts_9_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_19_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["practice_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["book_tactics", "De Re Militari", [("book_a", imodbits_none)], itp_type_book, 0, 4000, abundance(100)|weight(2.0), imodbits_none],

	["book_persuasion", "Rhetorica ad Herennium", [("book_b", imodbits_none)], itp_type_book, 0, 5000, abundance(100)|weight(2.0), imodbits_none],

	["book_leadership", "The Life of Alixenus the Great", [("book_d", imodbits_none)], itp_type_book, 0, 4200, abundance(100)|weight(2.0), imodbits_none],

	["book_intelligence", "Essays on Logic", [("book_e", imodbits_none)], itp_type_book, 0, 2900, abundance(100)|weight(2.0), imodbits_none],

	["book_trade", "A Treatise on the Value of Things", [("book_f", imodbits_none)], itp_type_book, 0, 3100, abundance(100)|weight(2.0), imodbits_none],

	["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d", imodbits_none)], itp_type_book, 0, 4200, abundance(100)|weight(2.0), imodbits_none],

	["book_engineering", "Method of Mechanical Theorems", [("book_open", imodbits_none)], itp_type_book, 0, 4000, abundance(100)|weight(2.0), imodbits_none],

	["book_wound_treatment_reference", "The Book of Healing", [("book_c", imodbits_none)], itp_type_book, 0, 3500, abundance(100)|weight(2.0), imodbits_none],

	["book_training_reference", "Manual of Arms", [("book_open", imodbits_none)], itp_type_book, 0, 3500, abundance(100)|weight(2.0), imodbits_none],

	["book_surgery_reference", "The Great Book of Surgery", [("book_c", imodbits_none)], itp_type_book, 0, 3500, abundance(100)|weight(2.0), imodbits_none],

	["spice", "Spice", [("spice_sack", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["salt", "Salt", [("salt_sack", imodbits_none)], itp_type_goods|itp_merchandise, 0, 255, abundance(120)|weight(50.0), imodbits_none],

	["oil", "Oil", [("oil", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 450, max_ammo(50)|abundance(60)|weight(50.0), imodbits_none],

	["pottery", "Pottery", [("jug", imodbits_none)], itp_type_goods|itp_merchandise, 0, 100, abundance(90)|weight(50.0), imodbits_none],

	["raw_flax", "Flax Bundle", [("raw_flax", imodbits_none)], itp_type_goods|itp_merchandise, 0, 150, abundance(90)|weight(40.0), imodbits_none],

	["linen", "Linen", [("linen", imodbits_none)], itp_type_goods|itp_merchandise, 0, 250, abundance(90)|weight(40.0), imodbits_none],

	["wool", "Wool", [("wool_sack", imodbits_none)], itp_type_goods|itp_merchandise, 0, 130, abundance(90)|weight(40.0), imodbits_none],

	["wool_cloth", "Wool Cloth", [("wool_cloth", imodbits_none)], itp_type_goods|itp_merchandise, 0, 250, abundance(90)|weight(40.0), imodbits_none],

	["raw_silk", "Raw Silk", [("raw_silk_bundle", imodbits_none)], itp_type_goods|itp_merchandise, 0, 600, abundance(90)|weight(30.0), imodbits_none],

	["raw_dyes", "Dyes", [("dyes", imodbits_none)], itp_type_goods|itp_merchandise, 0, 200, abundance(90)|weight(10.0), imodbits_none],

	["velvet", "Velvet", [("velvet", imodbits_none)], itp_type_goods|itp_merchandise, 0, 1025, abundance(30)|weight(40.0), imodbits_none],

	["iron", "Iron", [("iron", imodbits_none)], itp_type_goods|itp_merchandise, 0, 264, abundance(60)|weight(60.0), imodbits_none],

	["tools", "Tools", [("smith_hammer", imodbits_none)], itp_type_goods|itp_merchandise, 0, 410, abundance(90)|weight(50.0), imodbits_none],

	["raw_leather", "Hides", [("leatherwork_inventory", imodbits_none)], itp_type_goods|itp_merchandise, 0, 120, abundance(90)|weight(40.0), imodbits_none],

	["leatherwork", "Leatherwork", [("leatherwork_frame", imodbits_none)], itp_type_goods|itp_merchandise, 0, 220, abundance(90)|weight(40.0), imodbits_none],

	["raw_date_fruit", "Date Fruit", [("date_inventory", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 120, max_ammo(10)|abundance(100)|weight(40.0)|food_quality(10), imodbits_none],

	["furs", "Furs", [("fur_pack", imodbits_none)], itp_type_goods|itp_merchandise, 0, 391, abundance(90)|weight(40.0), imodbits_none],

	["wine", "Wine", [("amphora_slim", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 220, max_ammo(50)|abundance(60)|weight(30.0), imodbits_none],

	["ale", "Ale", [("ale_barrel", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 120, max_ammo(50)|abundance(70)|weight(30.0), imodbits_none],

	["smoked_fish", "Smoked Fish", [("smoked_fish", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 65, max_ammo(150)|abundance(110)|weight(15.0)|food_quality(50), imodbits_none],

	["cheese", "Cheese", [("cheese_b", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, max_ammo(90)|abundance(110)|weight(6.0)|food_quality(40), imodbits_none],

	["honey", "Honey", [("honey_pot", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 220, max_ammo(90)|abundance(110)|weight(5.0)|food_quality(40), imodbits_none],

	["sausages", "Sausages", [("sausages", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, max_ammo(120)|abundance(110)|weight(10.0)|food_quality(40), imodbits_none],

	["cabbages", "Cabbages", [("cabbage", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 30, max_ammo(150)|abundance(110)|weight(15.0)|food_quality(40), imodbits_none],

	["dried_meat", "Dried Meat", [("smoked_meat", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, max_ammo(150)|abundance(100)|weight(15.0)|food_quality(70), imodbits_none],

	["apples", "Fruit", [("apple_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 44, max_ammo(150)|abundance(110)|weight(20.0)|food_quality(40), imodbits_none],

	["raw_grapes", "Grapes", [("grapes_inventory", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 75, max_ammo(30)|abundance(90)|weight(40.0)|head_armor(10), imodbits_none],

	["raw_olives", "Olives", [("olive_inventory", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 100, max_ammo(30)|abundance(90)|weight(40.0)|head_armor(10), imodbits_none],

	["grain", "Grain", [("wheat_sack", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 30, max_ammo(150)|abundance(110)|weight(30.0)|head_armor(40), imodbits_none],

	["cattle_meat", "Beef", [("raw_meat", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 80, max_ammo(50)|abundance(100)|weight(20.0)|food_quality(80), imodbits_none],

	["bread", "Bread", [("bread_a", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 50, max_ammo(50)|abundance(110)|weight(30.0)|food_quality(40), imodbits_none],

	["chicken", "Chicken", [("chicken", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, max_ammo(50)|abundance(110)|weight(10.0)|food_quality(40), imodbits_none],

	["pork", "Pork", [("pork", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, max_ammo(50)|abundance(100)|weight(15.0)|food_quality(70), imodbits_none],

	["butter", "Butter", [("butter_pot", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 150, max_ammo(30)|abundance(110)|weight(6.0)|food_quality(40), imodbits_none],

	["siege_supply", "Supplies", [("ale_barrel", imodbits_none)], itp_type_goods, 0, 96, abundance(70)|weight(40.0), imodbits_none],

	["quest_wine", "Wine", [("amphora_slim", imodbits_none)], itp_type_goods, 0, 46, max_ammo(50)|abundance(60)|weight(40.0), imodbits_none],

	["quest_ale", "Ale", [("ale_barrel", imodbits_none)], itp_type_goods, 0, 31, max_ammo(50)|abundance(70)|weight(40.0), imodbits_none],

	["sumpter_horse", "Packhorse", [("sumpter_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 134, hit_points(120)|horse_maneuver(43)|abundance(90)|horse_charge(12)|horse_speed(40)|body_armor(24)|horse_scale(100), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited],

	["saddle_horse", "Rouncey", [("saddle_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 240, hit_points(120)|horse_maneuver(46)|abundance(90)|difficulty(1)|horse_charge(10)|horse_speed(42)|body_armor(24)|horse_scale(104), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited],

	["steppe_horse", "Steppe Horse", [("steppe_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 192, hit_points(120)|horse_maneuver(51)|abundance(80)|difficulty(2)|horse_charge(8)|horse_speed(44)|body_armor(24)|horse_scale(90), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited, [], [fac_culture_mongol]],

	["arabian_horse_a", "Arabian Horse", [("arabian_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 550, hit_points(120)|horse_maneuver(45)|abundance(80)|difficulty(2)|horse_charge(12)|horse_speed(48)|body_armor(24)|horse_scale(100), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["courser", "Palfrey", [("courser", imodbits_none)], itp_type_horse|itp_merchandise, 0, 600, hit_points(120)|horse_maneuver(47)|abundance(70)|difficulty(2)|horse_charge(22)|horse_speed(48)|body_armor(24)|horse_scale(106), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion],

	["arabian_horse_b", "Arabian Horse", [("arabian_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 700, hit_points(120)|horse_maneuver(54)|abundance(80)|difficulty(3)|horse_charge(16)|horse_speed(44)|body_armor(24)|horse_scale(100), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["hunter", "Courser", [("hunting_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 810, hit_points(120)|horse_maneuver(46)|abundance(60)|difficulty(3)|horse_charge(28)|horse_speed(45)|body_armor(24)|horse_scale(108), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion],

	["warhorse", "War Horse", [("warhorse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_white", "Barded Destrier", [("covered_horse_white", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_red", "Barded Destrier", [("covered_horse_red", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_blue", "Barded Destrier", [("covered_horse_blue", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_yellow", "Barded Destrier", [("covered_horse_yellow", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_player", "Custom Barded Destrier", [("covered_horse_player", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_lionel", "Barded Destrier", [("covered_horse_lionel", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_lethwin", "Barded Destrier", [("covered_horse_lethwin", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_01", "Caparisoned Destrier", [("rnd_horse_01", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_02", "Caparisoned Destrier", [("rnd_horse_02", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_03", "Caparisoned Destrier", [("rnd_horse_03", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_04", "Caparisoned Destrier", [("rnd_horse_04", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_05", "Caparisoned Destrier", [("rnd_horse_05", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_06", "Caparisoned Destrier", [("rnd_horse_06", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_07", "Caparisoned Destrier", [("rnd_horse_07", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_08", "Caparisoned Destrier", [("rnd_horse_08", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_09", "Caparisoned Destrier", [("rnd_horse_09", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_10", "Caparisoned Destrier", [("rnd_horse_10", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_11", "Caparisoned Destrier", [("rnd_horse_11", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_12", "Caparisoned Destrier", [("rnd_horse_12", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_13", "Caparisoned Destrier", [("rnd_horse_13", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_14", "Caparisoned Destrier", [("rnd_horse_14", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_15", "Caparisoned Destrier", [("rnd_horse_15", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_16", "Caparisoned Destrier", [("rnd_horse_16", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_17", "Caparisoned Destrier", [("rnd_horse_17", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_18", "Caparisoned Destrier", [("rnd_horse_18", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_19", "Caparisoned Destrier", [("rnd_horse_19", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_20", "Caparisoned Destrier", [("rnd_horse_20", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_21", "Caparisoned Destrier", [("rnd_horse_21", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_22", "Caparisoned Destrier", [("rnd_horse_22", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_23", "Caparisoned Destrier", [("rnd_horse_23", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_denmark_a", "Danish Destrier", [("warhorse_denmark_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_4]],

	["warhorse_england_a", "English Destrier", [("warhorse_england_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_devalence", "English Destrier", [("warhorse_devalence", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_demontfort", "English Destrier", [("warhorse_demontfort", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_mortimer", "English Destrier", [("warhorse_mortimer", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_bigod", "English Destrier", [("warhorse_bigod", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_dewarenne", "English Destrier", [("warhorse_dewarenne", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_france_a", "French Destrier", [("warhorse_france_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

	["warhorse_hre_a", "HRE Destrier", [("warhorse_hre_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_6]],

	["warhorse_bohemia", "Bohemian Destrier", [("warhorse_bohemia", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_6]],

	["warhorse_hungary_a", "Hungarian Destrier", [("warhorse_hungary_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_7]],

	["warhorse_ireland_a", "Irish Destrier", [("warhorse_gaelic", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_13]],

	["warhorse_lithuania_a", "Lithuanian Destrier", [("warhorse_lithuania_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_2]],

	["warhorse_norway_a", "Norwegian Destrier", [("warhorse_norway_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_11]],

	["warhorse_novgorod_a", "Novgorod Destrier", [("warhorse_novgorod_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_8]],

	["warhorse_scotland_a", "Scottish Destrier", [("warhorse_scotland_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_12]],

	["warhorse_sweden_a", "Swedish Destrier", [("warhorse_sweden_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_14]],

	["warhorse_przemysl2", "Polish Destrier", [("warhorse_przemysl2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_czersk", "Polish Destrier", [("warhorse_czersk", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_slask_a", "Caparisoned Destrier", [("warhorse_slask_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_siemowit_a", "Caparisoned Destrier", [("warhorse_siemowit_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_poland_a", "Polish Destrier", [("warhorse_poland_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_poland_b", "Polish Destrier", [("warhorse_poland_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_kaliskie_a", "Welsh Destrier", [("warhorse_kaliskie_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_welsh]],

	["warhorse_gslask", "Polish Destrier", [("warhorse_gslask", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_swietopelk", "Polish Destrier", [("warhorse_swietopelk", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_pol_a", "Polish Destrier", [("warhorse_pol_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_pol_b", "Polish Destrier", [("warhorse_pol_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_pol_c", "Polish Destrier", [("warhorse_pol_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_pol_d", "Polish Destrier", [("warhorse_pol_d", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_pol_e", "Polish Destrier", [("warhorse_pol_e", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_pol_g", "Polish Destrier", [("warhorse_pol_g", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["warhorse_swidnica", "Polish Destrier", [("warhorse_swidnica", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

	["teu_warhorse_c", "Teutonic Destrier", [("teu_war_horse_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_1]],

	["teu_warhorse_b", "Teutonic Destrier", [("teu_war_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_1]],

	["teu_warhorse_a", "Teutonic Destrier", [("teu_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_1]],

	["mon_lamellar_horse_a", "Lamellar Destrier", [("warhorse_lamellar_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["mon_lamellar_horse_b", "Lamellar Destrier", [("warhorse_lamellar_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["mon_lamellar_horse_c", "Lamellar Destrier", [("warhorse_lamellar_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["kau_montcada_horse", "Montcada Destrier", [("kau_montcada_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_alego_horse", "Alego Destrier", [("kau_alego_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_cervello_horse", "Cervello Destrier", [("kau_cervello_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_cruilles_horse", "Cruilles Destrier", [("kau_cruilles_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_epyres_horse", "Epyres Destrier", [("kau_epyres_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_luna_horse", "Luna Destrier", [("kau_luna_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_reino_horse", "Reino Destrier", [("kau_reino_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["kau_urgell_horse", "Urgell Destrier", [("kau_urgell_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

	["templar_warhorse_a", "Caparisoned Destrier", [("templar_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

	["hospitaller_warhorse_a", "Caparisoned Destrier", [("hospitaller_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

	["hospitaller_warhorse_b", "Caparisoned Destrier", [("hospitaller_war_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

	["warhorse_sarranid", "Lamellar War Horse", [("warhorse_sarranid", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["warhorse_steppe", "Lamellar War Horse", [("warhorse_steppe", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mongol]],

	["byz_warhorse", "Lamellar War Horse", [("byz_warhorse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["jerusalem_horse", "Caparisoned Destrier", [("jerusalem_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

	["tripoli_horse", "Caparisoned Destrier", [("tripoli_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

	["portugal_horse", "Caparisoned Destrier", [("portugal_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_16]],

	["castile_horse", "Caparisoned Destrier", [("castile_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_18]],

	["arrows", "Arrows", [("vik_arrow", imodbits_none), ("vik_arrow", ixmesh_flying_ammo), ("vik_quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 200, thrust_damage(24, cut)|max_ammo(60)|abundance(100)|weight(3.0)|weapon_length(96), imodbit_large_bag, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["khergit_arrows", "War Arrows", [("vik_arrow_b", imodbits_none), ("vik_arrow_b", ixmesh_flying_ammo), ("vik_quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 600, thrust_damage(28, cut)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(96), imodbit_large_bag, [], [fac_culture_mongol]],

	["barbed_arrows", "Barbed Arrows", [("vik_barbed_arrow", imodbits_none), ("vik_barbed_arrow", ixmesh_flying_ammo), ("vik_quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 400, thrust_damage(26, cut)|max_ammo(60)|abundance(75)|weight(3.0)|weapon_length(92), imodbit_large_bag, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["bodkin_arrows", "Bodkin Arrows", [("vik_piercing_arrow", imodbits_none), ("vik_piercing_arrow", ixmesh_flying_ammo), ("vik_quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 600, thrust_damage(28, pierce)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(92), imodbit_large_bag],

	["bolts", "Bolts", [("vik_bolt", imodbits_none), ("vik_bolt", ixmesh_flying_ammo), ("vik_bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 300, thrust_damage(25, pierce)|max_ammo(29)|abundance(100)|weight(1.5)|weapon_length(63), imodbit_large_bag, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["strely", "Munitions Arrows", [("vik_munitions_arrow", imodbits_none), ("vik_munitions_arrow", ixmesh_flying_ammo), ("vik_arena_quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 100, thrust_damage(22, cut)|max_ammo(60)|abundance(100)|weight(3.0)|weapon_length(96), imodbit_large_bag],

	["cartridges", "Billhook-fork", [("1429_glaive_fork", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["pilgrim_disguise", "Glaive", [("1429_glaive_guisarme_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_spear, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(199), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["pilgrim_hood", "Glaive-guisarme", [("1429_glaive_guisarme_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(206), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["leather_gloves", "Hand Wraps", [("gf_tekko_1_L", imodbits_none)], itp_type_hand_armor, 0, 40, abundance(100)|weight(0.12)|body_armor(1), imodbits_cloth],

	["mail_mittens", "Mail Mittens", [("mail_mittens_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 360, abundance(60)|weight(0.5)|difficulty(6)|body_armor(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["scale_gauntlets", "Leather Gloves", [("leather_gloves_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 90, abundance(100)|weight(0.25)|body_armor(2), imodbits_cloth],

	["lamellar_gauntlets", "Padded Linen Gloves", [("wantus1_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 180, abundance(60)|weight(0.37)|body_armor(3), imodbits_cloth],

	["wrapping_boots", "Ankle Boots", [("wrapping_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["woolen_hose", "Grey Hose", [("peasant_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["hunter_boots", "Blue Hose", [("blue_hose_mod_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["hide_boots", "Green Hose", [("green_hose_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["ankle_boots", "Grey Hose", [("leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 92, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["nomad_boots", "Mongol Boots", [("tied_up_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth],

	["leather_boots", "Black Hose", [("green_hose_b_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["splinted_leather_greaves", "Green Hose with Kneecaps", [("hose_kneecops_green", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["mail_chausses", "Mail Chausses", [("mail_chausses_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["splinted_greaves", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["splinted_greaves_long", "Splinted Greaves", [("kua_splinted_greaves_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2520, abundance(100)|weight(4.0)|leg_armor(30)|difficulty(12), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_anatolian_christian, fac_culture_western]],

	["mail_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["mail_boots_long", "Mail Boots", [("mail_spurs_cp1257_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["kau_mail_boots_dark", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["kau_mail_boots_dark_long", "Mail Chausses with Padding", [("raf_chausses", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sarranid_boots_a", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["sarranid_boots_a_long", "Black Hose", [("hose_black_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sarranid_boots_b", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["sarranid_boots_b_long", "Black and White Hose", [("hose_grey_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sarranid_boots_c", "Black and White Hose", [("hose_grey_3", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sarranid_boots_d", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["sarranid_boots_d_long", "Mail with Shoes", [("leather_greaves_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["raf_mail_chausses", "Tan Hose", [("hose_tan_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["kau_mail_boots", "Red Hose", [("kau_mail_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["mamluke_boots", "Mamluk Boots", [("mamluke_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["cuman_boots", "Cuman Boots", [("cuman_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_kingdom_7]],

	["byz_lord_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["byz_lord_boots_long", "Red Hose with Kneecaps", [("hose_kneecops_red", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["lapcie", "Eastern Wrapping Shoes", [("lapcie", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

	["byz_boots_c", "Byzantine Leather Boots", [("byz_leather_boots_c", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_cavalry_boots", "Mail with Boots", [("byz_cavalry_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_anatolian_christian, fac_culture_western]],

	["byz_boots_a", "Byzantine Leather Boots", [("byz_leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_boots_b", "Byzantine Leather Boots", [("byz_leather_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_greaves", "Byzantine Greaves", [("byzantine_greaves", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["leather_fur_boots", "Black Hose", [("hose_black_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["red_hose", "Dark Red Hose", [("red_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["green_hose", "Green Hose", [("green_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["grey_hose", "Blue Hose with Wrapping Boots", [("grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["dark_grey_hose", "Grey Hose", [("dark_grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["yellow_hose", "Yellow Hose", [("yellow_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["green_hose_b", "Black Hose", [("green_hose_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["tied_up_shoes", "Green and Purple Hose", [("hose_green_and_purple", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["blue_hose_mod", "Blue Hose", [("blue_hose_mod", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["berber_shoes", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["legs_with_shoes", "Shoes", [("legs_with_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 48, abundance(100)|weight(0.5)|leg_armor(2), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["bare_legs", "Sandals", [("calrad_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 48, abundance(100)|weight(0.5)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_iberian, fac_culture_italian, fac_culture_andalus]],

	["shoes", "Boots", [("shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["priest_2_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["blue_hose", "Blue Hose", [("wrapping_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rus_cav_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

	["rus_boots_a", "Rus' Boots", [("rus_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["rus_boots_b", "Hide Boots", [("hide_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth],

	["red_dress", "Red Dress", [("red_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["brown_dress", "Brown Dress", [("brown_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["green_dress", "Green Dress", [("green_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["khergit_lady_dress", "Mongol Lady Dress", [("khergit_lady_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_lady_dress_b", "Mongol Leather Lady Dress", [("khergit_lady_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

	["sarranid_lady_dress", "Saracen Lady Dress", [("sarranid_lady_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_lady_dress_b", "Saracen Lady Dress", [("sarranid_lady_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_common_dress", "Saracen Dress", [("sarranid_common_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_common_dress_b", "Saracen Dress", [("sarranid_common_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["nomad_armor", "Yellow Rus Tunic", [("rus_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_armor", "Black Rus Tunic", [("rus_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

	["leather_jacket", "Militia Tunic", [("militia_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["rawhide_coat", "Gambeson", [("aketon_acok", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth],

	["fur_coat", "Brown Tunic", [("kuauik_dornish_leather_tunic_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["merchant_outfit", "Merchant Outfit", [("nobleman_outfit_b_new", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["blue_dress", "Red Dress", [("blue_dress_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["peasant_dress", "Peasant Dress", [("barkeeper_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["linen_tunic", "Linen Tunic", [("shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["short_tunic", "Tunic With Felt Vest", [("rich_tunic_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["red_shirt", "Linen Tunic", [("kuauik_dornish_leather_tunic_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["robe", "Robe", [("sar_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["coarse_tunic", "Tunic", [("coarse_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["leather_vest", "Linen Vest", [("leather_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["steppe_armor", "Steppe Armor", [("lamellar_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["gambeson_a", "Gambeson", [("gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["gambeson_b", "Gambeson", [("gambeson_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gambeson_c", "Gambeson", [("gambeson_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gambeson_d", "Gambeson", [("gambeson_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["padded_cloth", "Aketon", [("padded_cloth_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["leather_jerkin", "Shirt", [("pentoshi_style_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["nomad_vest", "Linen Tunic", [("pentoshi_style_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["ragged_outfit", "Militia Tunic", [("militia_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["tribal_warrior_outfit", "Shirt", [("kuauik_norvoshi_style_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["haubergeon", "Mail Hauberk", [("kau_mail_shirt_cloak", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["lamellar_vest", "Mongolian Gambeson", [("tribal_warrior_outfit_a_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["lamellar_vest_khergit", "Mongolian Gambeson", [("peltastos_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["mail_with_surcoat", "Surcoat over Mail Haubergeon", [("rnd_surcoat_12_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["surcoat_over_mail", "Surcoat over Mail Haubergeon", [("rnd_surcoat_15_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["coat_of_plates", "Mail Hauberk", [("norman_short_hauberk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["coat_of_plates_red", "Brown Coat of Plates over Mail", [("coat_of_plates_red_mod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17841, abundance(10)|weight(36.0)|leg_armor(36)|difficulty(15)|body_armor(72), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["pelt_coat", "Blue Rus Tunic", [("rus_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["bishop_cop", "Red Coat of Plates over Mail", [("bishop_CoP", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17841, abundance(10)|weight(36.0)|leg_armor(36)|difficulty(15)|body_armor(72), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["sarranid_cloth_robe", "Worn Robe", [("sar_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["archers_vest", "Archer's Padded Vest", [("archers_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_leather_armor", "Saracen Padded Kaftan", [("kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_cavalry_robe", "Arabic Mail Hauberk", [("cavalle_moro_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arabian_armor_b", "Arabic Mail Hauberk", [("cavalle_moro_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_mail_shirt", "Arabic Mail Hauberk", [("cavalle_moro_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["mamluke_mail", "Mamluk Plated Mail", [("sipahi_jawshan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["veteran_surcoat_a", "Surcoat over Mail Haubergeon", [("surcoat_cop_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["veteran_surcoat_b", "Surcoat over Mail Haubergeon", [("surcoat_cop_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["veteran_surcoat_c", "Surcoat over Mail Haubergeon", [("surcoat_cop_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["veteran_surcoat_d", "Surcoat over Mail Haubergeon", [("surcoat_cop_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["veteran_surcoat_e", "Surcoat over Mail Haubergeon", [("surcoat_cop_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["arena_outfit_a", "Surcoat over Mail Haubergeon", [("arena_outfit_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["arena_outfit_b", "Surcoat over Mail Haubergeon", [("arena_outfit_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["arena_outfit_c", "Surcoat over Mail Haubergeon", [("arena_outfit_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["arena_outfit_d", "Surcoat over Mail Haubergeon", [("arena_outfit_yellow", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["kau_aragon_knight", "Aragonian Surcoat over Mail", [("kau_aragon_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

	["kau_aragon_a", "Aragonian Surcoat over Mail Haubergeon", [("kau_aragon_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

	["kau_aragon_b", "Aragonian Surcoat over Mail", [("kau_aragon_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

	["kau_aragon_c", "Aragonian Surcoat over Mail", [("kau_aragon_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

	["kau_montcada_surcoat", "Montcada Surcoat over Mail", [("kau_montcada_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_alego_surcoat", "Alego Surcoat over Mail", [("kau_alego_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_cervello_surcoat", "Cervello Surcoat over Mail", [("kau_cervello_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_cruilles_surcoat", "Cruilles Surcoat over Mail", [("kau_cruilles_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_entenca_surcoat", "Entensa Surcoat over Mail", [("kau_entenca_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_epyres_surcoat", "Epyres Surcoat over Mail", [("kau_epyres_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_luna_surcoat", "Luna Surcoat over Mail", [("kau_luna_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_pons_surcoat", "Pons Surcoat over Mail", [("kau_pons_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_castile_knight", "Crown of Castile Surcoat over Mail", [("kau_castile_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

	["kau_castile_a", "Crown of Castile Surcoat over Mail Haubergeon", [("kau_castile_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

	["kau_castile_b", "Crown of Castile Surcoat over Mail Haubergeon", [("kau_castile_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

	["kau_castile_c", "Crown of Castile Surcoat over Mail Haubergeon", [("kau_castile_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

	["kau_santiago", "Santiago Surcoat over Mail Haubergeon", [("kau_santiago", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

	["kau_portugal_a", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

	["kau_portugal_b", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

	["kau_portugal_c", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

	["kau_portugal_d", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

	["kau_papal", "Papal Surcoat over Mail Haubergeon", [("kau_papal", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_papacy]],

	["kau_sicily_a", "Sicilian Surcoat over Mail Haubergeon", [("kau_sicily_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_24]],

	["kau_sicily_b", "Sicilian Surcoat over Mail Haubergeon", [("kau_sicily_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_24]],

	["kau_antioch", "Antioch Surcoat over Mail Haubergeon", [("kau_antioch", imodbits_none), ("kau_antioch", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23, fac_kingdom_23]],

	["kau_cyprus", "Cyprus Surcoat over Mail Haubergeon", [("kau_cyprus", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["kau_antioch", "Antioch Surcoat over Mail Haubergeon", [("kau_antioch", imodbits_none), ("kau_antioch", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23, fac_kingdom_23]],

	["kau_jerusalem", "Jerusalem Surcoat over Mail Haubergeon", [("kau_jerusalem", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["kau_latin_a", "Latin Empire Surcoat over Mail Haubergeon", [("kau_latin_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

	["kau_latin_b", "Latin Empire Surcoat over Mail Haubergeon", [("kau_latin_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

	["kau_athens", "Latin Empire Surcoat over Mail Haubergeon", [("kau_athens", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

	["kau_courtenay", "Latin Empire Surcoat over Mail Haubergeon", [("kau_courtenay", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

	["rnd_surcoat_01", "Surcoat over Mail Haubergeon", [("rnd_surcoat_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_01"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_02", "Surcoat over Mail Haubergeon", [("rnd_surcoat_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_03", "Surcoat over Mail Haubergeon", [("rnd_surcoat_03", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_03"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_04", "Surcoat over Mail Haubergeon", [("rnd_surcoat_04", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_05", "Surcoat over Mail Haubergeon", [("rnd_surcoat_05", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_05"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_06", "Surcoat over Mail Haubergeon", [("rnd_surcoat_06", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_07", "Surcoat over Mail Haubergeon", [("rnd_surcoat_07", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_07"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_08", "Surcoat over Mail Haubergeon", [("rnd_surcoat_08", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_09", "Surcoat over Mail Haubergeon", [("rnd_surcoat_09", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_09"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_10", "Surcoat over Mail Haubergeon", [("rnd_surcoat_10", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_11", "Surcoat over Mail Haubergeon", [("rnd_surcoat_11", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_11"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_12", "Surcoat over Mail Haubergeon", [("rnd_surcoat_12", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_13", "Surcoat over Mail Haubergeon", [("rnd_surcoat_13", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_13"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_14", "Surcoat over Mail Haubergeon", [("rnd_surcoat_14", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_15", "Surcoat over Mail Haubergeon", [("rnd_surcoat_15", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_15"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_16", "Surcoat over Mail Haubergeon", [("rnd_surcoat_16", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_17", "Surcoat over Mail Haubergeon", [("rnd_surcoat_17", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_17"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_18", "Surcoat over Mail Haubergeon", [("rnd_surcoat_18", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_19", "Surcoat over Mail Haubergeon", [("rnd_surcoat_19", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_19"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_20", "Surcoat over Mail Haubergeon", [("rnd_surcoat_20", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_21", "Surcoat over Mail Haubergeon", [("rnd_surcoat_21", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_21"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_22", "Surcoat over Mail Haubergeon", [("rnd_surcoat_22", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["rnd_surcoat_23", "Surcoat over Mail Haubergeon", [("rnd_surcoat_23", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_23"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["surcoat_denmark_a", "Danish Surcoat over Mail Haubergeon", [("surcoat_denmark_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_4]],

	["surcoat_england_a", "English Surcoat over Mail Haubergeon", [("surcoat_england_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

	["surcoat_devalence", "English Surcoat over Mail Haubergeon", [("surcoat_devalence", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

	["surcoat_demontfort", "English Surcoat over Mail Haubergeon", [("surcoat_demontfort", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

	["surcoat_mortimer", "English Surcoat over Mail Haubergeon", [("surcoat_mortimer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

	["surcoat_bigod", "English Surcoat over Mail Haubergeon", [("surcoat_bigod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

	["surcoat_dewarenne", "English Surcoat over Mail Haubergeon", [("surcoat_dewarenne", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

	["surcoat_france_a", "French Surcoat over Mail Haubergeon", [("surcoat_france_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_10]],

	["surcoat_hre_a", "HRE Surcoat over Mail Haubergeon", [("surcoat_hre_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

	["richard_of_cornwall_surcoat_over_mail", "HRE Surcoat over Mail Haubergeon", [("surcoat_richard_of_cornwall_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

	["surcoat_bohemia", "Bohemian Surcoat over Golden Mail Haubergeon", [("surcoat_bohemia_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_42]],

	["surcoat_hungary_a", "Hungarian Surcoat over Mail Haubergeon", [("surcoat_hungary_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

	["surcoat_ireland_a", "Irish Cuir Bouilli over Mail", [("surcoat_gaelic_kingdoms", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_13]],

	["surcoat_lithuania_a", "Lithuanian Scale Armour", [("surcoat_lithuania_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_2]],

	["surcoat_lithuania_b", "Lithuanian Mail Hauberk", [("surcoat_lithuania_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_2]],

	["surcoat_norway_a", "Norwegian Surcoat over Mail Haubergeon", [("surcoat_norway", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_11]],

	["surcoat_novgorod", "Novgorod Scale Armour", [("surcoat_novgorod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(60)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["surcoat_scotland_a", "Scottish Surcoat over Mail Haubergeon", [("surcoat_scotland", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_12]],

	["surcoat_sweden_a", "Swedish Surcoat over Mail Haubergeon", [("surcoat_sweden_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_14]],

	["surcoat_kaliskie", "Polish Surcoat over Mail Haubergeon", [("surcoat_kaliskie_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_poland_a", "Polish Surcoat over Mail Haubergeon", [("surcoat_poland_wb_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["siemowit_surcoat_over_mail", "Polish Surcoat over Mail Haubergeon", [("surcoat_siemowit_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_gslask", "Polish Mail Hauberk with Lamellar Vest", [("surcoat_gslask_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_dslask", "Polish Surcoat over Mail Haubergeon", [("surcoat_dslask_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_mazowsze", "Polish Surcoat over Mail Haubergeon", [("surcoat_mazowsze_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_swidnica", "Polish Surcoat over Mail Haubergeon", [("surcoat_swidnica_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_swietopelk", "Polish Surcoat over Mail Haubergeon", [("surcoat_swietopelk_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_henry3", "Surcoat over Mail Haubergeon", [("surcoat_henry3_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_a", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_b", "Polish Mail Hauberk with Lamellar Vest", [("surcoat_pol_wb_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_c", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_d", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_e", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_f", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_pol_g", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_czersk", "Polish Mail Hauberk with Lamellar Vest", [("surcoat_czersk_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["surcoat_przemysl2", "Polish Surcoat over Mail Haubergeon", [("surcoat_przemysl2_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["teu_hochmeister_surcoat", "Hochmeister Haubergeon", [("teu_hochmeister_surcoat", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic]],

	["teu_brother_surcoat_a", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_b", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_c", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_d", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_e", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_sariant_mail", "Teutonic Surcoat over Hauberk", [("teu_sariant_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_postulant_a", "HalbbrÃ¼der Surcoat over Mail Haubergeon", [("teu_postulant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_hbrother_mail", "Teutonic Gambeson", [("teu_hbrother_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_sergeant", "Teutonic Gambeson", [("teutonic_sergeant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["liv_sergeant", "Teutonic Gambeson", [("livonian_sergeant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_monk_surcoat_a", "Livonian Gambeson", [("teu_monk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["liv_tunic_a", "Livonian Tunic", [("liv_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_gambeson", "Teutonic Gambeson", [("teu_gambeson", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_coat_of_plates", "White Coat of Plates over Mail", [("teu_coat_of_plates_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17841, abundance(10)|weight(36.0)|leg_armor(36)|difficulty(15)|body_armor(72), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["scale_shirt_a", "Baltic Scale Shirt", [("raf_scale_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

	["kau_padded_mail_a", "White Aketon", [("kau_padded_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_a", "Mail Hauberk", [("kau_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_b", "Mail Hauberk", [("kau_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_haubergeon_a", "Red Aketon", [("kau_haubergeon_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_a", "Aketon", [("kau_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_b", "Mail Hauberk", [("kau_mail_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_c", "Blue Aketon", [("kau_mail_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_d", "Blue Aketon", [("kau_mail_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_rus_a", "Rus Mail Hauberk", [("kau_rus_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_b", "Eastern Scale Shirt", [("kau_rus_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_d", "Eastern Gambeson", [("kau_rus_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_scale_a", "Eastern Mail Hauberk with Lamellar Vest", [("kau_rus_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_noble_b", "Eastern Scale Shirt", [("kau_rus_nobleman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(60)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_lamellar_vest", "Leather Lamellar Vest over Mail Hauberk", [("kau_rus_nobleman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_noble_a", "Eastern Mail Hauberk", [("kau_rus_nobleman_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_c", "Eastern Mail Hauberk with Lamellar Vest", [("kau_rus_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kau_rus_mail_shirt_a", "Leather Scale Shirt", [("kau_rusmilitia", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(80)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_mail_shirt_b", "Rus Aketon", [("kau_rus_aketon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["rus_mail_shirt_c", "Rus Mail Hauberk", [("rus_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

	["kau_rus_e", "Eastern Shirt", [("kau_rus_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["kau_lit_mail", "Baltic Leather Scale Vest", [("balt_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

	["kau_rus_tunic_a", "Rus' Tunic", [("kau_rus_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_tunic_b", "Rus' Tunic", [("kau_rus_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_tunic_c", "Rus' Tunic", [("kau_rus_tunic_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["kau_arab_aketon_blue", "Arabic Scale Vest", [("kau_arab_aketon_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_aketon", "Arabic Gambeson", [("kau_arab_aketon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_aketon_red", "Arabic Gambeson", [("kau_arab_aketon_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_aketon_green", "Arabic Gambeson", [("kau_arab_aketon_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_lamellar_vest_a", "Arabic Gambeson", [("kau_ayubbid", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_lamellar_vest_b", "Arabic Gambeson", [("kau_ayubbid_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_lamellar_vest_c", "Arabic Gambeson", [("kau_ayubbid_copy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_mail_a", "Arabic Lamellar Vest", [("arab_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_mail_b", "Arabic Lamellar Vest over Mail Hauberk", [("arab_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_mail_c", "Arabic Lamellar Vest", [("arab_mail_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_mail_d", "Arabic Lamellar Vest over Mail Hauberk", [("arab_mail_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_mail_shirt_a", "Arabic Robe", [("kau_mail_sara", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(80)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_mail_shirt_b", "Arabic Mail Hauberk", [("kau_mail_saracen", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_mail_shirt_c", "Arabic Mail Hauberk", [("kau_mail_saracen_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_mail_shirt_d", "Arabic Gambeson", [("kau_mail_saracen_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_tunic_a", "Bedouin Gambeson", [("kau_muslim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kau_arab_tunic_b", "Bedouin Gambeson", [("kau_muslim_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_banded_a", "Saracen Mail Hauberk", [("kau_banded_armor_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_banded_b", "Saracen Mail Hauberk", [("kau_banded_armor_muslim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_banded_c", "Saracen Mail Hauberk", [("kau_banded_armor_muslima", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["templar_sarjeant_surcoat", "Templar Surcoat over Mail Haubergeon", [("templar_serjeant_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["templar_sarjeant_mail", "Teutonic Mail Hauberk", [("teu_postulant_acok", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["templar_mail_a", "Templar Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_23]],

	["templar_tunic_a", "Templar Surcoat over Mail Haubergeon", [("rnd_surcoat_temple", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["templar_knight_a", "Templar Surcoat over Mail Haubergeon", [("templar_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["templar_knight_b", "Templar Surcoat over Mail Haubergeon", [("templar_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["templar_knight_c", "Templar Surcoat over Mail Haubergeon", [("templar_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["templar_gambeson_a", "Templar Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_23]],

	["hospitaller_knight_a", "Hospitaller Surcoat over Mail Haubergeon", [("fi_chain_mail_hauberk_heraldic_3", imodbits_none), ("hospitaller_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23, fac_kingdom_23]],

	["hospitaller_knight_b", "Hospitaller Surcoat over Mail", [("hospitaller_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_knight_c", "Hospitaller Surcoat over Mail", [("hospitaller_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_knight_d", "Hospitaller Surcoat over Mail", [("hospitaller_knight_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_knight_e", "Hospitaller Surcoat over Mail", [("hospitaller_knight_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_knight_f", "Hospitaller Surcoat over Mail Haubergeon", [("hospitaller_knight_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_sarjeant_surcoat", "Hospitaller Surcoat over Mail Haubergeon", [("Chinese_Hospitaller", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_sarjeant_mail", "Order Mantle of the Knights Hospitaller", [("templar_serjeant_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_tunic_a", "Order Mantle of the Knights Templar", [("templar_postulant_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_gambeson_a", "Templar Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_23]],

	["hospitaller_knight_a", "Hospitaller Surcoat over Mail Haubergeon", [("fi_chain_mail_hauberk_heraldic_3", imodbits_none), ("hospitaller_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23, fac_kingdom_23]],

	["hirdman_a", "Scandinavian Mail Haubergeon", [("kau_hirdman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_nordic]],

	["cuman_shirt_a", "Cuman Mail Hauberk", [("cuman_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

	["cuman_shirt_b", "Cuman Gambeson", [("cuman_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7]],

	["cuman_shirt_c", "Cuman Gambeson", [("cuman_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7]],

	["cuman_shirt_d", "Cuman Gambeson", [("cuman_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7]],

	["kipchak_shirt_a", "Kipchak Mail Hauberk", [("kipchak_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

	["kipchak_shirt_b", "Kipchak Tunic", [("kipchak_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_kingdom_7]],

	["kipchak_mail_a", "Surcoat over Mail Haubergeon", [("rnd_surcoat_09_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["mongol_warrior_a", "Mongol Tunic with Lamellar", [("mongol_light_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(100)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["mongol_warrior_b", "Mongol Kaftan with Lamellar", [("mongol_light_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(100)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["mongol_warrior_c", "Mongol Leather Lamellar", [("mongol_leather_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_warrior_d", "Chinese Gambeson", [("mongol_warrior_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a", imodbits_none), ("mongol_warrior_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol, fac_culture_mongol]],

	["mongol_tunic_b", "Mongol Gambeson", [("mongol_warrior_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_warrior_ilkhanate", "Mongol Gambeson", [("ilkhanate_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["mamluk_shirt_a", "Mamluk Shirt", [("mamluk_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_b", "Mamluk Mail Hauberk", [("mamluk_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_c", "Mamluk Mail Hauberk", [("mamluk_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_d", "Mamluk Lamellar Vest", [("mamluk_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_e", "Seljuk Mail Hauberk", [("mamluk_shirt_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_f", "Arabic Scale Armour", [("mamluk_shirt_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(60)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["peasant_tunic_a", "Linen Tunic", [("peasant_outfit_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["peasant_b", "Linen Tunic", [("peasant_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["peasant_c", "Linen Tunic", [("peasant_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["peasant_d", "Linen Tunic", [("peasant_man_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["ragged_cloth_b", "Linen Tunic", [("ragged_cloth_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["peasant_f", "Linen Tunic", [("ragged_cloth_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["peasant_g", "Linen Tunic with Cape", [("peasant_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["byz_lord", "Byzantine Lamellar Armour over Mail Hauberk", [("byz_lord", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_emperor", "Byzantine Lamellar Armour over Mail Hauberk", [("byz_emperor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["bishop_a", "Bishop Surcoat over Mail Haubergeon", [("bishop_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["varangian_a", "Varangian Mail Haubergeon", [("varangian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

	["varangian_b", "Byzantine Lamellar Vest", [("varangian_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

	["varangian_c", "Varangian Mail Hauberk", [("rus_coat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

	["kau_rus_noble_d", "Rus Mail Hauberk with Lamellar Vest", [("kau_rus_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["balt_lamellar_vest_a", "Baltic Gambeson", [("balt_lamellar_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_lamellar_vest_b", "Baltic Gambeson", [("balt_lamellar_vest_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_lamellar_vest_c", "Baltic Lamellar Vest", [("balt_lamellar_vest_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["byz_mail_a", "Byzantine Lamellar over Mail Hauberk", [("byzantine_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_lamellar_a", "Byzantine Lamellar Leather Armour", [("byz_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_lamellar_b", "Byzantine Lamellar Leather Armour", [("byz_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_leather_a", "Byzantine Gambeson", [("byz_leather_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_leather_b", "Byzantine Gambeson", [("byz_leather_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_padded_leather", "Byzantine Mail Hauberk", [("byz_padded_cloth", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(50)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_scale_armor", "Byzantine Scale Shirt", [("byz_cavalry", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

	["byz_cavalry_a", "Byzantine Cavalry Mail Hauberk", [("byz_cavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_cavalry_b", "Byzantine Cavalry Mail Hauberk", [("byz_cavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_mail_b", "Byzantine Mail Hauberk", [("byz_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_hcavalry_a", "Byzantine Scale over Mail Hauberk", [("byz_hcavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_hcavalry_b", "Byzantine Scale over Mail Hauberk", [("byz_hcavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_hcavalry_c", "Byzantine Gambeson", [("byz_hcavalry_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(80)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_psiloi_a", "Byzantine Tunic", [("byz_psiloi_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["byz_psiloi_b", "Byzantine Tunic", [("byz_psiloi_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["byz_kataphrakt", "Byzantine Mail Hauberk", [("byz_kataphrakt", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kipchak_lamellar_a", "Kipchak Mail Hauberk", [("kipchak_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["kipchak_lamellar_b", "Kipchak Scale Shirt", [("kipchak_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["balt_shirt_a", "Baltic Tunic", [("balt_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_shirt_b", "Baltic Tunic", [("balt_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_shirt_e", "Baltic Tunic", [("balt_shirt_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_shirt_d", "Baltic Tunic", [("balt_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_fur_coat_a", "Baltic Tunic", [("balt_fur_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_fur_coat_b", "Baltic Tunic", [("balt_fur_coat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["mon_lamellar_a", "Mongol Lamellar Armor", [("mon_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["mon_lamellar_b", "Mongol Leather Lamellar Armor", [("mon_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(40)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["byz_footman_a", "Byzantine Mail Hauberk", [("byz_footman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_footman_b", "Byzantine Gambeson", [("byz_footman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_footman_c", "Byzantine Mail Hauberk", [("byz_footman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_1", "Welsh Mail Hauberk", [("galloglass_padded2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["byz_swordsman_2", "Byzantine Lamellar Armour over Mail Hauberk", [("rathos_lamellar_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_3", "Eastern Lamellar over Mail Hauberk", [("leatherovermail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_4", "Eastern Lamellar over Mail Hauberk", [("leatherovermail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_guard_a", "Byzantine Mail Hauberk", [("byz_guard_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_guard_b", "Byzantine Mail Hauberk", [("byz_guard_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kau_arab_nobleman", "Saracen Mirror Armour over Mail Hauberk", [("kau_arab_nobleman", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["almogavar_a", "Iberian Tunic", [("almogavar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

	["almogavar_b", "Iberian Tunic", [("almogavar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

	["almogavar_c", "Iberian Tunic", [("almogavar_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

	["burlap_tunic", "Linen Tunic", [("shirt_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["heraldic_mail_with_surcoat", "Mail Hauberk", [("norman_short_hauberk_yellow", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["sarranid_head_cloth", "Lady Head Cloth", [("tulbent", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["head_wrappings", "Bastard Battle Axe", [("vik_tveirhendr_vendelox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(88), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["turret_hat_green", "Barbette", [("barbette_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["wimple_a", "Wimple", [("wimple_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["wimple_with_veil", "Wimple with Veil", [("wimple_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["straw_hat", "Green Cap", [("rus_hat_03", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

	["headcloth", "Headcloth", [("headcloth_a_new", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["arming_cap", "Arming Cap", [("1257_arming_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["fur_hat", "Brown Cap", [("rus_hat_01", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

	["nomad_cap", "Hood", [("fi_hood_4", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["nomad_cap_b", "Red Cap", [("cuman_cap_clothing_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

	["steppe_cap", "Hood", [("fi_hood_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["padded_coif", "Black Cap", [("rus_hat_04", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

	["woolen_cap", "Blue Cap", [("cuman_cap_clothing_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["felt_hat", "Felt Hat", [("birka_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["felt_hat_b", "Blue Cap", [("rus_hat_05", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

	["leather_cap", "Woolen Cap", [("rus_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["female_hood", "Lady's Hood", [("ladys_hood_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["leather_steppe_cap_a", "Steppe Cap", [("rus_fur_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

	["leather_steppe_cap_b", "Gold Topped Cap", [("helmetpad", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

	["leather_steppe_cap_c", "Woolen Cap", [("saxon_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

	["mail_coif", "Mail Coif", [("coif_1257", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["footman_helmet", "Footman's Helmet", [("skull_cap_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["khergit_lady_hat", "Blue Robe", [("armenian_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["khergit_lady_hat_b", "Mongol Lady Leather Hat", [("khergit_lady_hat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_mongol]],

	["armenian_knight_b", "Red Robe", [("armenian_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["turban", "Turban", [("dornish_open_turban", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["desert_turban", "Desert Turban", [("dornish_turban", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["turban_a", "Turban", [("arab_turban_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["turban_b", "Turban Helm", [("arab_turban_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(80)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["turban_c", "Turban Helm", [("arab_turban_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(80)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_mail_coif", "Saracen Mail Coif", [("arabic_coif", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["seljuk_helmet", "Seljuk Full Mail Coif Helmet", [("seljuk_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_warrior_cap", "Turban Helm", [("dornish_turban_helmet_2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(80)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_horseman_helmet", "Turban Helm", [("dornish_turban_helmet_1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(80)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_helmet1", "Saracen Mail Coif with Helm", [("casco_moro1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_mail_coif", "Saracen Mail Coif with Helm", [("dornish_turban_helmet_mail", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_veiled_helmet", "Saracen Mamluk Veiled Helm", [("dornish_cataphract_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["vaegir_mask", "Rus War Mask with Padding", [("otk_shlem", imodbits_none), ("otk_shlem_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 8260, abundance(30)|weight(3.0)|difficulty(12)|body_armor(2)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["winged_great_helmet", "Kettle Helmet with Mail Coif", [("flat_kettle2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["osp_great_helm_a", "Red Great Helm", [("englishgreathelmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["osp_great_helm_b", "Heaume", [("osp_greathelm_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["osp_byzantion_a", "Byzantine Helmet with Mail Coif", [("osp_byzantion_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["vik_norman_helmet_a", "Norman Helmet with Aventail", [("vik_coifedpointyhelm", imodbits_none), ("inv_vik_coifedpointyhelm", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["vik_norman_helmet_b", "Norman Helmet with Padding", [("vik_normanhelmet", imodbits_none), ("inv_vik_normanhelmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["vik_norman_helmet_c", "Norman Helmet with Mail Coif", [("vik_pointedhelmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["vik_norman_helmet_e", "Nasal Helm", [("viki_plainhelm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["vik_spangen_a", "Spangen Helm", [("vik_norskspangen1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["vik_spangen_b", "Spangen Helm with Padding", [("vik_norskspangendecorated", imodbits_none), ("inv_vik_norskspangendecorated", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["balt_spiked_helmet", "Balt Spiked Cap with Mail Coif", [("pointy_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_footman_helmet", "Kettlehelm with Mail Coif", [("smallbrim_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 4800, abundance(50)|weight(2.25)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["balt_helmet_a", "Balt Helmet", [("lit_segmented_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_helmet_b", "Full Mail Coif", [("fullfacecoif", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["balt_helmet_c", "Balt Helmet with Mail Coif", [("rusiu_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["teu_kettle_hat_a", "Kettle Helm", [("teu_kettle_hat_cloth_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_western, fac_kingdom_1, fac_kingdom_23]],

	["teu_kettle_hat_b", "Kettle Helm", [("teu_kettle_hat_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["slonim", "Slonim with Aventail", [("slonim", imodbits_none), ("inv_slonim", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6320, abundance(40)|weight(2.75)|difficulty(12)|body_armor(6)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["osp_faceplate", "Kettle Helm with Padding", [("osp_faceplate", imodbits_none), ("inv_osp_faceplate", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_01", "Decorated Great Helm", [("rnd_helm_01", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_02", "Winged Great Helm", [("rnd_helm_02", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_03", "Great Helm", [("rnd_helm_03", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_04", "Great Helm", [("civan_helm_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_05", "Great Helm", [("civan_helm_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_06", "Kettle Helm with Padding", [("kettlehat_b_red", imodbits_none), ("inv_kettlehat_b_red", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["kau_alego_helmet", "Aragonese Cervelliere", [("kau_alego_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.25)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian]],

	["kau_epyres_helmet", "Aragonese Cervelliere", [("kau_epyres_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.25)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian]],

	["kau_pons_helmet", "Aragonese Cervelliere", [("kau_pons_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.25)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian]],

	["kau_urgell_helmet", "Aragonese Cervelliere", [("kau_urgell_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.25)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian]],

	["byz_yoman_a", "Byzantine Helmet with Full Mail Coif", [("facecovermail_plume", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_yoman_b", "Byzantine Helmet with Aventail", [("facecovermail_kettlehat", imodbits_none), ("facecovermail_kettlehat", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6320, abundance(40)|weight(2.75)|difficulty(12)|body_armor(6)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_yoman_c", "Byzantine Helmet", [("facecovermail_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_yoman_d", "Byzantine Helmet with Padding", [("facecovermail", imodbits_none), ("inv_facecovermail", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["templar_kettlehat_a", "Kettle Helm", [("templar_kettle_cloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["hospitaller_kettlehat_a", "Nasal Helm with Full Mail Coif", [("normanhelmfullcoif", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["elm1", "Chapel de Fer with Aventail", [("chapel-de-fer_mail2", imodbits_none), ("inv_chapel-de-fer_mail2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(40)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["elm2", "Skullcap with Arming Cap", [("elm_type2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["elm3", "Chapel de Fer with Aventail", [("chapel-de-fer_mail1", imodbits_none), ("inv_chapel-de-fer_mail1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(40)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["elm5", "Aragonese Helmet", [("elm_type5", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian]],

	["elm6", "Fluted Spangen Helmet with Mail Coif", [("elm_type6", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["elm7", "Chapel de Fer with Aventail", [("chapel-de-fer_mail3", imodbits_none), ("inv_chapel-de-fer_mail3", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(40)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["elm8", "Spangen Helmet with Mail Coif", [("elm_type8", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["elm9", "Yesenovo Helm with Mail Coif", [("elm_type9", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["elm10", "Byzantine Brimmed Helmet with Aventail", [("byz_kettle", imodbits_none), ("inv_byz_kettle", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_helmet_a", "Byzantine Footman's Helmet with Aventail", [("byz_helmet_a", imodbits_none), ("inv_byz_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["leather_warrior_cap", "Kettle Helm with Padding", [("kettlehat_a_blue", imodbits_none), ("inv_kettlehat_a_blue", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["skullcap", "Kettle Helm with Padding", [("norman_helmtet", imodbits_none), ("inv_norman_helmtet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["raf_spangen", "Spangen Helm", [("spangen", imodbits_none)], itp_type_head_armor, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["arab_helmet_a", "Andalusian Tiara", [("arab_helmet_a", imodbits_none)], itp_type_head_armor, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_helmet_b", "Saracen Helm with Mail Coif", [("arab_helmet_b", imodbits_none)], itp_type_head_armor, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_helmet_c", "Saracen Helm with Mail Coif", [("arab_helmet_c", imodbits_none)], itp_type_head_armor, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["berber_helmet_a", "Berber Turban", [("berber_helmet", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus]],

	["maciejowski_helm", "Great Helm", [("maciejowskihelm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["talak_litchina", "Litchina War Mask Helmet", [("talak_litchina", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["crown_coif", "Crowned Cervilliere", [("coif_crown_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["aragon_crown", "Crowned Spangen Helm with Mail Coif", [("crowned_helmtet_02", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["talak_crown_ornate", "Crowned Mail Coif", [("talak_crown_ornate", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["cuman_cap_a", "Cuman Hat with Padding", [("cuman_cap_a", imodbits_none), ("inv_cuman_cap_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_kingdom_7]],

	["cuman_cap_b", "Cuman Helm", [("cuman_cap_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

	["cuman_cap_c", "Cuman Hat", [("cuman_cap_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_kingdom_7]],

	["maciejowski_kettle_hat_a", "Kettle Helm with Aventail", [("maciejowski_kettle_a", imodbits_none), ("inv_maciejowski_kettle_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3720, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["maciejowski_kettle_hat_b", "Kettle Helm with Padding", [("maciejowski_kettle_b", imodbits_none), ("inv_maciejowski_kettle_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["norman_coif_a", "Kettle Helm", [("red_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["maciejowski_crown", "Crowned Gold Great Helm", [("crown_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["crowned_norman", "Crowned Norman Helm", [("crown_helmtet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["norman_coif_b", "Flattop Helm with Mail Coif", [("flattop_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rus_helm_a", "Gnezdovo Helm with Mail Coif", [("gnezdovo_helm_a", imodbits_none), ("inv_gnezdovo_helm_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_helmet_b", "Slavic Helm with Aventail", [("rus_helmet_b", imodbits_none), ("inv_rus_helmet_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["norman_coif_c", "Kettle Helmet with Aventail", [("blue_helmet", imodbits_none), ("inv_blue_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["norman_coif_d", "Kettle Helm", [("green_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["norman_coif_e", "Norman Helmet", [("white_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["teu_kettle_hat_a_mail", "Teutonic Kettle Helm with Mail Coif", [("teu_kettle_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["templar_kettlehat_a_mail", "Templar Kettle Helm with Mail Coif", [("templar_kettle_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["hospitaller_kettlehat_a_mail", "Templar Kettle Helm with Mail Coif", [("col1_kettlehat1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["kolpak_mail", "Cervilliere", [("kolpak_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["mail_coif_b", "Mail Coif", [("bandage_coif_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["mail_coif_c", "Mail Coif", [("bandage_coif_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["norman_faceplate", "Nasal Helm with Mail Coif", [("norman_faceplate_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["varangian_helm", "Varangian Veiled Helmet", [("varangian_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mamluke_helm", "Mamluk Helmet with Aventail", [("mamluk_helmet", imodbits_none), ("inv_mamluk_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["long_axe_alt", "Long Danish Axe", [("vik_long_danox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_civilian|itp_next_item_as_melee|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 235, thrust_damage(39, cut)|hit_points(44032)|spd_rtng(75)|abundance(100)|weight(3.375)|swing_damage(39, cut)|difficulty(12)|weapon_length(115), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["long_axe_b_alt", "Long Danish Axe", [("vik_long_danox_alt", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_thrust_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 0, thrust_damage(31, pierce)|hit_points(44032)|spd_rtng(85)|weight(3.375)|swing_damage(20, blunt)|difficulty(12)|weapon_length(115), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["hammer", "One Handed Long Danish Axe", [("axe_d", imodbits_none), ("axe_d_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(43008)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(71), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["wooden_stick", "European Arming Sword", [("bb_arming_sword", imodbits_none), ("bb_arming_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["winged_mace", "One Handed Angle Axe", [("axe_c", imodbits_none), ("axe_c_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(41984)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["spiked_mace", "One Handed Hooked Axe", [("axe_b", imodbits_none), ("axe_b_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(39936)|spd_rtng(87)|abundance(100)|weight(1.875)|swing_damage(27, cut)|difficulty(6)|weapon_length(58), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["military_hammer", "One Handed Broad Axe", [("axe_a", imodbits_none), ("axe_a_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(39936)|spd_rtng(87)|abundance(100)|weight(1.875)|swing_damage(27, cut)|difficulty(6)|weapon_length(56), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["maul", "Winged Glaive", [("glaive3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 400, thrust_damage(35, pierce)|hit_points(40960)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(155), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sledgehammer", "Long Glaive", [("1429_bill_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 520, thrust_damage(41, pierce)|hit_points(35840)|spd_rtng(69)|abundance(100)|weight(6.2)|swing_damage(51, cut)|difficulty(12)|weapon_length(219), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["warhammer", "One Handed Boarding Axe", [("mackie_tomahawk", imodbits_none), ("mackie_tomahawk_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(36864)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(45), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["pickaxe", "One Handed Cutting Axe", [("heavy_cutting_axe", imodbits_none), ("heavy_cutting_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(36864)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(47), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["spiked_club", "One Handed Old Axe", [("gael_beard_axe", imodbits_none), ("gael_beard_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(43008)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(47), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["fighting_pick", "One Handed Small Bearded Axe", [("vik_axe_f", imodbits_none), ("vik_axe_f_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 170, hit_points(36864)|spd_rtng(88)|abundance(100)|weight(1.75)|swing_damage(26, cut)|difficulty(6)|weapon_length(54), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["military_pick", "One Handed Small Danish Axe", [("vik_axe_e", imodbits_none), ("vik_axe_e_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 170, hit_points(36864)|spd_rtng(88)|abundance(100)|weight(1.75)|swing_damage(26, cut)|difficulty(6)|weapon_length(50), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["morningstar", "Winged Mace", [("newmace_bronze3", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_sword_left_hip|itc_cleaver|itc_parry_polearm, 1250, hit_points(31744)|spd_rtng(80)|abundance(25)|weight(5.0)|swing_damage(36, blunt)|difficulty(12)|weapon_length(85), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sickle", "Hoe", [("war_hoe", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_unbalanced|itp_no_blur, itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itc_parry_polearm, 50, hit_points(33792)|spd_rtng(80)|abundance(100)|weight(1.5)|swing_damage(30, cut)|weapon_length(100), imodbit_cracked|imodbit_bent],

	["cleaver", "One Handed Chopping Axe", [("vik_throwing_axe", imodbits_none), ("vik_throwing_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 155, hit_points(36864)|spd_rtng(91)|abundance(100)|weight(1.375)|swing_damage(23, cut)|difficulty(6)|weapon_length(37), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["knife", "Seax", [("seax_1_1", imodbits_none), ("seax_1_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_wakizashi|itcf_show_holster_when_drawn|itc_longsword, 58, thrust_damage(17, pierce)|hit_points(14336)|spd_rtng(115)|abundance(100)|weight(0.5)|swing_damage(22, cut)|weapon_length(40), imodbit_fine|imodbits_sword_high, [], [fac_culture_welsh, fac_culture_italian, fac_culture_gaelic]],

	["butchering_knife", "Broad Dagger", [("norman_dagger", imodbits_none), ("norman_dagger_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_longsword, 75, thrust_damage(20, pierce)|hit_points(14336)|spd_rtng(115)|abundance(100)|weight(0.75)|swing_damage(20, cut)|weapon_length(44), imodbit_fine|imodbits_sword_high],

	["dagger", "Scian", [("scian", imodbits_none), ("scian_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_overswing_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itcf_overswing_spear|itcf_overswing_musket|itcf_thrust_musket|itc_parry_onehanded, 250, thrust_damage(30, pierce)|hit_points(14336)|spd_rtng(115)|abundance(100)|weight(0.5)|swing_damage(15, cut)|weapon_length(54), imodbit_fine|imodbits_sword_high, [], [fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_gaelic, fac_culture_scotish, fac_culture_western]],

	["falchion", "Straight Falchion", [("falchion_1", imodbits_none), ("falchion_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(25600)|spd_rtng(90)|abundance(40)|weight(2.75)|swing_damage(34, cut)|difficulty(9)|weapon_length(72), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["scimitar", "Falchion", [("falchion_2", imodbits_none), ("falchion_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(26, cut)|hit_points(34816)|spd_rtng(87)|abundance(40)|weight(3.25)|swing_damage(36, cut)|difficulty(9)|weapon_length(74), imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["scimitar_b", "Arabic Sabre", [("sword_arabic_1", imodbits_none), ("sword_arabic_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(22, cut)|hit_points(38912)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(91), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arabian_sword_a", "Arabic Sword", [("sword_arabic_2", imodbits_none), ("sword_arabic_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(26, cut)|difficulty(9)|weapon_length(91), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arabian_sword_b", "Arabic Sabre", [("sword_arabic_3", imodbits_none), ("sword_arabic_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(22, cut)|hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(89), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["sarranid_cavalry_sword", "Mamluk Sabre", [("sword_arabic_4", imodbits_none), ("sword_arabic_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(24, cut)|hit_points(38912)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(91), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arabian_sword_d", "Mamluk Sword", [("sword_arabic_5", imodbits_none), ("sword_arabic_5_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(38912)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(91), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["andalusian_sword", "Mamluk Sabre", [("sword_arabic_6", imodbits_none), ("sword_arabic_6_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(24, cut)|hit_points(35840)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(89), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["hatchet", "One Handed Thin Axe", [("vik_einhendi_hoggox", imodbits_none), ("vik_einhendi_hoggox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(32768)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(47), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tutorial_sword", "Long Spiked Mace", [("spikemace3", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_sword_left_hip|itc_cleaver|itc_poleaxe, 750, thrust_damage(35, pierce)|hit_points(81744)|spd_rtng(82)|abundance(25)|weight(4.0)|swing_damage(34, blunt)|difficulty(9)|weapon_length(98), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["talak_bastard_sword", "Godenak", [("falchion_godenak", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_sword_left_hip|itc_longsword, 1750, thrust_damage(22, blunt)|spd_rtng(84)|abundance(25)|weight(3.0)|swing_damage(38, cut)|difficulty(12)|weapon_length(72), imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_rus]],

	["raf_one_handed_axe_a", "One Handed Danish Axe", [("vik_einhendi_danox", imodbits_none), ("vik_einhendi_danox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(39936)|spd_rtng(87)|abundance(100)|weight(1.875)|swing_damage(27, cut)|difficulty(6)|weapon_length(57), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_b", "One Handed Quarter Axe", [("vik_einhendi_breithofudox", imodbits_none), ("vik_einhendi_breithofudox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(44032)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(72), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_c", "One Handed Bearded Axe", [("vik_einhendi_haloygox", imodbits_none), ("vik_einhendi_haloygox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(39936)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_d", "One Handed Small Axe", [("vik_einhendi_hedmarkrox", imodbits_none), ("vik_einhendi_hedmarkrox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(36864)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(67), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_e", "One Handed Decorated Axe", [("vik_einhendi_trondrox", imodbits_none), ("vik_einhendi_trondrox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(41984)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(67), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_f", "One Handed Battle Axe", [("vik_einhendi_vendelox", imodbits_none), ("vik_einhendi_vendelox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 180, hit_points(41984)|spd_rtng(86)|abundance(100)|weight(2.0)|swing_damage(28, cut)|difficulty(6)|weapon_length(61), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_g", "One Handed Spiked Axe", [("slim_axe", imodbits_none), ("slim_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 180, hit_points(43008)|spd_rtng(86)|abundance(100)|weight(2.0)|swing_damage(28, cut)|difficulty(6)|weapon_length(62), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_one_handed_axe_h", "One Handed Long Bearded Axe", [("rus_axe_a", imodbits_none), ("rus_axe_a_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(44032)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(72), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_two_handed_axe_a", "Two Handed War Axe", [("vik_tveirhendr_hedmarkrox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(64032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(109), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_two_handed_axe_b", "Two Handed Danish Axe", [("vik_tveirhendr_danox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(44032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(109), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["raf_two_handed_axe_c", "Two Handed GallÃ³glach Axe", [("talak_nordic_axe", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 230, thrust_damage(38, cut)|hit_points(64032)|spd_rtng(76)|abundance(100)|weight(3.25)|swing_damage(38, cut)|difficulty(9)|weapon_length(111), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["sarranid_mace_1", "Billhook", [("1429_guisarme", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 500, thrust_damage(25, blunt)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(207), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace],

	["sarranid_axe_a", "Glaive-fork", [("1429_lochaber_axe_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(29696)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(188), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sarranid_axe_b", "Hooked Voulge", [("1429_lochaber_axe_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(40960)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_type_xii", "European Arming Sword", [("senlac", imodbits_none), ("senlac_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_type_xiia", "Ornate European Sword", [("alsacian_sword", imodbits_none), ("alsacian_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(45056)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(90), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_type_xiii", "European Arming Sword", [("norman_sword", imodbits_none), ("norman_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_type_xiiia", "European Longsword", [("gaddhjalt", imodbits_none), ("gaddhjalt_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3250, thrust_damage(35, pierce)|hit_points(43008)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(33, cut)|difficulty(9)|weapon_length(104), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_type_xiiib", "European Sword", [("norman_sverd", imodbits_none), ("norman_sverd_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_type_xiv", "Scandinavian Sword", [("the_stamford2", imodbits_none), ("the_stamford2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(36864)|spd_rtng(95)|abundance(10)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["cp391_sword", "Templar Arming Sword", [("bb_templar_sword_a", imodbits_none), ("bb_templar_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(10)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_anatolian_christian]],

	["spatha", "Spatha", [("sword_balkan_1", imodbits_none), ("sword_balkan_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, cut)|hit_points(39936)|spd_rtng(95)|abundance(40)|weight(2.5)|swing_damage(32, cut)|difficulty(9)|weapon_length(85), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["bb_serbian_sword_1", "European Sidesword", [("sword_euro_5", imodbits_none), ("sword_euro_5_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1700, thrust_damage(30, pierce)|hit_points(37888)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(34, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["bb_serbian_sword_5", "European Arming Sword", [("sword_euro_6", imodbits_none), ("sword_euro_6_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["bb_rus_sword_6", "Rus Shortsword", [("short_rus_sword", imodbits_none), ("scab_short_rus_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 750, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(82), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["bb_rus_sword_1", "Rus Sword", [("sword_rus_6", imodbits_none), ("sword_rus_6_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.5)|swing_damage(32, cut)|difficulty(9)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["bb_rus_sword_3", "Rus Scimitar", [("rus_scimitar", imodbits_none), ("rus_scimitar_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(34816)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(97), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["two_handed_cleaver", "Rus Sword", [("sword_rus_5", imodbits_none), ("sword_rus_5_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.5)|swing_damage(32, cut)|difficulty(9)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["military_cleaver_b", "Baltic Sword", [("sword_rus_4", imodbits_none), ("sword_rus_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(26, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(93), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["military_cleaver_c", "Baltic Sword", [("sword_rus_3", imodbits_none), ("sword_rus_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(26, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(93), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["military_sickle_a", "One Handed Cavalry Axe", [("rus_cav_axe", imodbits_none), ("rus_cav_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(43008)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(73), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["voulge", "Voulge", [("mackie_voulge", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(40960)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["long_axe", "Two Handed Hooked Axe", [("axe_b_2h", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(44032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(106), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["tutorial_battle_axe", "European Shortsword", [("sword_euro_1", imodbits_none), ("sword_euro_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(77), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["long_axe_b", "Two Handed Angle Axe", [("axe_c_2h", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 230, thrust_damage(38, cut)|hit_points(44032)|spd_rtng(76)|abundance(100)|weight(3.25)|swing_damage(38, cut)|difficulty(9)|weapon_length(113), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["tutorial_axe", "European Arming Sword", [("sword_euro_2", imodbits_none), ("sword_euro_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["bardiche", "Bardiche", [("euro_axe_02", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 1000, thrust_damage(45, cut)|hit_points(28697)|spd_rtng(74)|abundance(50)|weight(5.87)|swing_damage(45, cut)|difficulty(12)|weapon_length(95), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_teutonic, fac_culture_rus, fac_culture_baltic]],

	["hafted_blade_b", "European Shortsword", [("sword_euro_7", imodbits_none), ("sword_euro_7_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(76), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["hafted_blade_a", "European Arming Sword", [("sword_euro_8", imodbits_none), ("sword_euro_8_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["shortened_military_scythe", "European Longsword", [("the_gaddhjalt", imodbits_none), ("the_gaddhjalt_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3250, thrust_damage(35, pierce)|hit_points(43008)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(33, cut)|difficulty(9)|weapon_length(104), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_viking_1", "Baltic Old Sword", [("sword_rus_1", imodbits_none), ("sword_rus_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 875, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(6)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["sword_viking_2", "Baltic Old Sword", [("sword_rus_2", imodbits_none), ("sword_rus_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 875, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(6)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["sword_viking_2_small", "Baltic Old Shortsword", [("viking_short_sword", imodbits_none), ("viking_short_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 750, thrust_damage(22, pierce)|hit_points(36864)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(75), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

	["sword_viking_3", "Scandinavian Arming Sword", [("sword_euro_3", imodbits_none), ("sword_euro_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_viking_3_small", "Scandinavian Arming Sword", [("sword_euro_4", imodbits_none), ("sword_euro_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["sword_khergit_1", "Eastern Sword", [("sword_mongol_1", imodbits_none), ("sword_mongol_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.25)|swing_damage(26, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_khergit_2", "Eastern Sabre", [("sword_mongol_2", imodbits_none), ("sword_mongol_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(22, cut)|hit_points(40960)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_khergit_3", "Mongol Sabre", [("sword_mongol_3", imodbits_none), ("sword_mongol_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(24, cut)|hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_khergit_4", "Mongol Sword", [("sword_mongol_4", imodbits_none), ("sword_mongol_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(41984)|spd_rtng(100)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mace_1", "HÃ¦ftmace", [("haeftmace", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_blur, itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 380, thrust_damage(34, pierce)|hit_points(64032)|spd_rtng(91)|abundance(50)|weight(3.4)|swing_damage(34, cut)|difficulty(9)|weapon_length(143), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_welsh, fac_culture_nordic, fac_culture_gaelic, fac_culture_scotish]],

	["mace_2", "Knobbed Mace", [("mace_knobbed", imodbits_none), ("mace_knobbed_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 370, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(2.5)|swing_damage(30, blunt)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["mace_3", "Spiral Mace", [("mace_spiral", imodbits_none), ("mace_spiral_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 370, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(2.5)|swing_damage(30, blunt)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["mace_4", "Iberian Mace", [("Faradon_IberianMace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_mace_left_hip|itc_cleaver|itc_parry_two_handed, 560, hit_points(31744)|spd_rtng(85)|abundance(100)|weight(3.5)|swing_damage(32, blunt)|difficulty(9)|weapon_length(81), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_iberian]],

	["club_with_spike_head", "Billhook", [("Rathos_bill_hook", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 440, thrust_damage(23, blunt)|hit_points(14029)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(172), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["long_spiked_club", "Guisarme", [("guisarme_a", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(53248)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(232), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["long_hafted_knobbed_mace", "Bill", [("english_bill", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(35840)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(231), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["long_hafted_spiked_mace", "War Spear", [("ped_spjotkesja", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 260, thrust_damage(41, pierce)|hit_points(32768)|spd_rtng(89)|abundance(100)|weight(3.1)|swing_damage(15, blunt)|difficulty(9)|weapon_length(211), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["studded_club", "Studded Club", [("Faradon_StuddedClub", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 1000, thrust_damage(38, blunt)|hit_points(86864)|spd_rtng(76)|abundance(10)|weight(8.0)|swing_damage(38, blunt)|difficulty(9)|weapon_length(102), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_teutonic, fac_culture_western]],

	["scythe", "Glaive with Rondel", [("glaive1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 380, thrust_damage(34, pierce)|hit_points(40960)|spd_rtng(76)|abundance(100)|weight(4.8)|swing_damage(44, cut)|difficulty(12)|weapon_length(149), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["pitch_fork", "Hooked Voulge", [("1429_lochaber_axe_3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 460, thrust_damage(24, blunt)|hit_points(40960)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(186), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["military_fork", "Couteau de BrÃ¨che", [("war_glaive_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 440, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(73)|abundance(100)|weight(4.8)|swing_damage(47, cut)|difficulty(12)|weapon_length(177), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["battle_fork", "Couteau de BrÃ¨che", [("war_glaive_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(196), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["glaive", "Glaive", [("hewing_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 420, thrust_damage(36, pierce)|hit_points(40960)|spd_rtng(74)|abundance(100)|weight(5.2)|swing_damage(46, cut)|difficulty(12)|weapon_length(169), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["staff", "Hooked Voulge", [("1429_lochaber_axe_4", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 440, thrust_damage(23, blunt)|hit_points(40960)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["quarter_staff", "Spiked Voulge", [("1429_voulge_3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(44032)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(182), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_balkan]],

	["iron_staff", "Voulge", [("1429_voulge_5", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(44032)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(200), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_balkan]],

	["military_scythe", "Bill", [("fi_bill", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 520, thrust_damage(41, pierce)|hit_points(45056)|spd_rtng(69)|abundance(100)|weight(6.2)|swing_damage(51, cut)|difficulty(12)|weapon_length(215), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["light_lance", "Coloured Lance", [("colored_lance_a", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["lance", "Coloured Lance", [("colored_lance_b", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["heavy_lance", "Coloured Lance", [("colored_lance_c", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["muslim_lance", "Coloured Lance", [("colored_lance_d", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["heraldic_lance", "Heraldic Lance", [("heraldic_lance", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 240, thrust_damage(29, pierce)|hit_points(10240)|spd_rtng(81)|abundance(100)|weight(2.9)|difficulty(6)|weapon_length(190), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_heraldic_lance_1", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["bamboo_spear", "Coloured Lance", [("colored_lance_f", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["berber_spear", "Coloured Lance", [("colored_lance_g", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_a", "Spear", [("norman_cavalry_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 210, thrust_damage(36, pierce)|hit_points(29696)|spd_rtng(94)|abundance(100)|weight(2.6)|swing_damage(15, blunt)|difficulty(6)|weapon_length(169), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_b", "Spear", [("norman_cavalry_lance", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 250, thrust_damage(40, pierce)|hit_points(23552)|spd_rtng(90)|abundance(100)|weight(3.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(204), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_c", "Spear", [("vik_bryntvari2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 160, thrust_damage(31, pierce)|hit_points(28672)|spd_rtng(99)|abundance(100)|weight(2.1)|swing_damage(15, blunt)|difficulty(6)|weapon_length(118), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_d", "Spear", [("vik_fjadraspjot", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(23552)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(134), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_e", "Spear", [("vik_hoggkesja", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(29696)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(134), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_f", "Spear", [("vik_kastad_krokaspjott", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 220, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(93)|abundance(100)|weight(2.7)|swing_damage(15, blunt)|difficulty(6)|weapon_length(173), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_g", "Spear", [("vik_kastspjottmidtaggir", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(28672)|spd_rtng(100)|abundance(100)|weight(2.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(109), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_h", "Spear", [("vik_krokaspjott1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 220, thrust_damage(37, pierce)|hit_points(22528)|spd_rtng(93)|abundance(100)|weight(2.7)|swing_damage(15, blunt)|difficulty(6)|weapon_length(173), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_i", "Spear", [("vik_krokaspjott2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(139), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_j", "Spear", [("vik_langr_bryntvari", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 250, thrust_damage(40, pierce)|hit_points(17408)|spd_rtng(90)|abundance(100)|weight(3.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(205), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_k", "Spear", [("vik_langr_hoggspjott", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 240, thrust_damage(39, pierce)|hit_points(18432)|spd_rtng(91)|abundance(100)|weight(2.9)|swing_damage(15, blunt)|difficulty(6)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_l", "Spear", [("vik_langr_svia", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 250, thrust_damage(40, pierce)|hit_points(16384)|spd_rtng(90)|abundance(100)|weight(3.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(208), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_m", "Spear", [("vik_spjot", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(24576)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(132), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_n", "Spear", [("vik_spjotkesja", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 270, thrust_damage(42, pierce)|hit_points(16384)|spd_rtng(88)|abundance(100)|weight(3.2)|swing_damage(15, blunt)|difficulty(6)|weapon_length(229), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_o", "Spear", [("vik_svia2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(23552)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(132), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["spear_p", "Spear", [("vik_sviar", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 170, thrust_damage(32, pierce)|hit_points(27648)|spd_rtng(98)|abundance(100)|weight(2.2)|swing_damage(15, blunt)|difficulty(6)|weapon_length(122), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["wooden_shield", "Lithuanian Shield", [("lithuanian_shield10", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["nordic_shield", "Lithuanian Shield", [("lithuanian_shield11", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["leather_covered_round_shield", "Assegai", [("assegai", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 140, thrust_damage(43, cut)|hit_points(16384)|spd_rtng(87)|abundance(100)|weight(3.3)|swing_damage(15, blunt)|difficulty(9)|weapon_length(231), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_mamluke]],

	["hide_covered_round_shield", "Lithuanian Shield", [("lithuanian_shield12", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["tab_shield_small_round_n", "Hungarian Surcoat over Mail Haubergeon", [("surcoat_hungary_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

	["tab_shield_round_a", "Plank Shield", [("tableau_shield_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 56, hit_points(35)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(50)|resistance(48), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["tab_shield_round_b", "Round Shield", [("tableau_shield_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 84, hit_points(41)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(50)|resistance(55), imodbits_shield],

	["tab_shield_round_c", "Round Shield with Boss", [("tableau_shield_round_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(47)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["tab_shield_round_d", "Oval Shield with Boss", [("tableau_shield_round_byz", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 76, hit_points(64)|spd_rtng(90)|abundance(100)|weight(5.0)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield],

	["tab_shield_round_e", "Iron Rimmed Round Shield", [("tableau_shield_round_1", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 152, hit_points(51)|spd_rtng(84)|abundance(100)|weight(4.0)|shield_width(50)|resistance(67), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["tab_shield_kite_c", "Flat Topped Kite Shield", [("tableau_shield_kite_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield],

	["tab_shield_kite_cav_a", "Bastard Thin Axe", [("vik_tveirhendr_hoggox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(86), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["tab_shield_kite_cav_b", "Small Iron Rimmed Kite Shield", [("tableau_shield_kite_4", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(31)|spd_rtng(103)|abundance(100)|weight(2.0)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["tab_shield_heater_c", "Heater Shield", [("tableau_shield_heater_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield],

	["tab_shield_heater_cav_a", "Two Handed Gaelic Axe", [("mackie_celtic_axe", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 220, thrust_damage(36, cut)|hit_points(44032)|spd_rtng(78)|abundance(100)|weight(3.0)|swing_damage(36, cut)|difficulty(9)|weapon_length(100), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_gaelic, fac_culture_scotish]],

	["tab_shield_heater_cav_b", "Norman Iron Rimmed Kite Shield", [("tableau_shield_kite_byz", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(64)|spd_rtng(85)|abundance(100)|weight(5.5)|shield_width(40)|resistance(67)|shield_height(65), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_byz", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["huscarl_armour", "Norwegian Surcoat over Mail Haubergeon", [("surcoat_norway_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_11]],

	["tab_shield_small_round_a", "Small Round Shield", [("tableau_shield_small_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 30, hit_points(31)|spd_rtng(105)|abundance(100)|weight(2.0)|shield_width(40)|resistance(61), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["tab_shield_small_round_b", "Small Iron Rimmed Round Shield", [("tableau_shield_small_round_1", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 40, hit_points(37)|spd_rtng(103)|abundance(100)|weight(2.5)|shield_width(40)|resistance(67), imodbits_shield],

	["tab_shield_small_round_c", "Small Elite Iron Rimmed Round Shield", [("tableau_shield_small_round_2", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 45, hit_points(42)|spd_rtng(100)|abundance(100)|weight(3.0)|shield_width(40)|resistance(70), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["lit_pavise_a_3", "Lithuanian Shield", [("lithuanian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_b_3", "Lithuanian Shield", [("lithuanian_shield2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_c_3", "Lithuanian Shield", [("lithuanian_shield3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_d_3", "Lithuanian Shield", [("lithuanian_shield4", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_e_3", "Lithuanian Shield", [("lithuanian_shield5", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_f_3", "Lithuanian Shield", [("lithuanian_shield6", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_g_3", "Lithuanian Shield", [("lithuanian_shield7", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lit_pavise_h_3", "Lithuanian Shield", [("lithuanian_shield8", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["lithuanian_shield9", "Tough Lithuanian Shield", [("lithuanian_shield9", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 276, hit_points(70)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(67)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

	["arab_shield_a_3", "Saracen Round Shield", [("arab_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_b_3", "Saracen Round Shield", [("arab_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_c_3", "Saracen Round Shield", [("arab_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_d_3", "Saracen Round Shield", [("arab_shield_d", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_e_3", "Saracen Round Shield", [("arab_shield_e", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_f_3", "Saracen Round Shield", [("arab_shield_f", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_g_3", "Saracen Round Shield", [("arab_shield_g", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_h_3", "Saracen Round Shield", [("arab_shield_h", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_i_3", "Saracen Round Shield", [("arab_shield_i", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["cuman_shield_a_3", "Cuman Round Shield", [("cuman_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_kingdom_7]],

	["cuman_shield_b_3", "Cuman Round Shield", [("cuman_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_kingdom_7]],

	["cuman_shield_c_3", "Cuman Round Shield", [("cuman_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, [], [fac_kingdom_7]],

	["talak_buckler", "Buckler", [("talak_buckler", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_dagger_front_left, 100, hit_points(25)|spd_rtng(140)|abundance(100)|weight(1.0)|shield_width(32)|resistance(35), imodbits_shield, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["tab_shield_iberia_c", "Iberian Shield", [("tableau_shield_iberia", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_iberia_shield", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_iberian]],

	["berber_shield_3", "Berber Shield", [("berber_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_marinid]],

	["byz_shield", "Tough Byzantine Kite Shield", [("byz_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, hit_points(51)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(36)|resistance(67)|shield_height(70), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_kite", "Two Handed Quarter Axe", [("vik_tveirhendr_breithofudox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 210, thrust_damage(34, cut)|hit_points(64032)|spd_rtng(80)|abundance(100)|weight(2.75)|swing_damage(34, cut)|difficulty(9)|weapon_length(93), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["byz_shield_round", "Two Handed Small Danish Axe", [("vik_tveirhendr_danox_small", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 210, thrust_damage(34, cut)|hit_points(64032)|spd_rtng(80)|abundance(100)|weight(2.75)|swing_damage(34, cut)|difficulty(9)|weapon_length(91), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["adarga_a", "Moorish Shield", [("adarga_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, [], [fac_culture_andalus]],

	["adarga_b", "Moorish Shield", [("adarga_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, [], [fac_culture_andalus]],

	["byz_shield_1", "Byzantine Shield", [("byz_shield_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_2", "Byzantine Shield", [("byz_shield_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_3", "Byzantine Cavalry Shield", [("byz_shield_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_4", "Byzantine Infantry Shield", [("byz_shield_4", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_5", "Byzantine Infantry Shield", [("byz_shield_5", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_shield_1", "Almond Shield", [("rus_shield_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["rus_shield_2", "Almond Shield", [("rus_shield_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["reiforced_shield_horse", "Almond Shield", [("reiforced_shield_horse", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["reiforced_shield_infantry", "Almond Shield", [("reiforced_shield_infantry", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["ball", "Capped Mace", [("Faradon_Mace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_mace_left_hip|itc_cleaver|itc_parry_two_handed, 190, hit_points(31744)|spd_rtng(88)|abundance(100)|weight(1.75)|swing_damage(28, blunt)|difficulty(6)|weapon_length(68), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_teutonic, fac_culture_anatolian_christian, fac_culture_western]],

	["jarid", "Darts", [("vik_dart", imodbits_none), ("vik_dart_carry", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 200, thrust_damage(30, cut)|max_ammo(10)|spd_rtng(95)|abundance(50)|weight(3.2)|difficulty(1)|weapon_length(43)|shoot_speed(36), imodbit_cracked|imodbit_tempered|imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["darts", "Sling Stones", [("vc_throwing_stone", imodbits_none), ("vc_throwing_stone", ixmesh_flying_ammo)], itp_type_bullets|itp_merchandise|itp_can_knock_down, 0, 10, thrust_damage(12, blunt)|max_ammo(60)|abundance(100)|weight(5.0)|weapon_length(4), imodbit_large_bag],

	["war_darts", "Javelins", [("vik_heavy_dart", imodbits_none), ("vik_heavy_dart_carry", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 300, thrust_damage(30, pierce)|max_ammo(8)|spd_rtng(93)|abundance(50)|weight(3.6)|difficulty(2)|weapon_length(35)|shoot_speed(32), imodbit_cracked|imodbit_tempered|imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["javelin", "Sling", [("vc_Sling2", imodbits_none)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_use_on_horseback, itcf_shoot_pistol|itcf_reload_pistol, 25, thrust_damage(24, blunt)|max_ammo(1)|spd_rtng(85)|abundance(100)|weight(0.25)|leg_armor(75)|shoot_speed(55), imodbits_none],

	["balt_javelin", "Throwing Spears", [("vik_atgeirr_thrown", imodbits_none), ("atgeirr_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 480, thrust_damage(33, pierce)|max_ammo(6)|spd_rtng(91)|abundance(20)|weight(3.2)|difficulty(3)|weapon_length(45)|shoot_speed(28), imodbit_cracked|imodbit_tempered|imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["throwing_spears", "Falarica", [("vik_bryntvari2_thrown", imodbits_none), ("vik_bryntvari_a_quiver", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 600, thrust_damage(36, pierce)|max_ammo(4)|spd_rtng(89)|abundance(20)|weight(4.0)|difficulty(4)|weapon_length(50)|shoot_speed(26), imodbit_cracked|imodbit_tempered|imodbits_missile],

	["fustibalus", "Fustibalus", [("vc_Staf_Sling_fustibalus_2", imodbits_none)], itp_type_musket|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_knock_down, itcf_shoot_musket|itcf_reload_pistol, 100, thrust_damage(30, blunt)|max_ammo(1)|spd_rtng(85)|abundance(100)|weight(1.25)|leg_armor(85)|shoot_speed(65), imodbits_none],

	["throwing_knives", "Rocks with Sling (Thrown)", [("vc_Sling", imodbits_none), ("caribbean_stone", ixmesh_flying_ammo)], itp_type_thrown|itp_primary|itp_cant_use_on_horseback|itp_can_knock_down, itcf_throw_stone, 25, thrust_damage(18, blunt)|max_ammo(30)|spd_rtng(85)|abundance(100)|weight(3.0)|weapon_length(8)|shoot_speed(45), imodbit_large_bag, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["stones", "Stones", [("vik_rocks", imodbits_none)], itp_type_thrown|itp_primary|itp_secondary|itp_can_knock_down, itcf_throw_knife, 1, thrust_damage(12, blunt)|max_ammo(12)|spd_rtng(97)|abundance(100)|weight(4.0)|weapon_length(6)|shoot_speed(35), imodbit_heavy|imodbit_large_bag],

	["light_throwing_axes", "Francisca", [("vik_francisca", imodbits_none), ("vik_francisca_carry", ixmesh_carry)], itp_type_thrown|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_civilian|itp_next_item_as_melee|itp_unbalanced|itp_extra_penetration, itcf_throw_axe|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 160, thrust_damage(24, cut)|max_ammo(1)|spd_rtng(90)|abundance(10)|weight(1.6)|weapon_length(31)|shoot_speed(12), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	, [fac_culture_finnish, fac_culture_mazovian, fac_culture_balkan, fac_culture_rus, fac_culture_nordic, fac_culture_baltic, fac_culture_gaelic]],

	["light_throwing_axes_melee", "Francisca", [("vik_francisca", imodbits_none), ("vik_francisca_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 0, spd_rtng(90)|weight(1.6)|swing_damage(24, cut)|difficulty(6)|weapon_length(42), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace],

	["hunting_bow", "Hunting Bow", [("bow_f_hunting_bow", imodbits_none), ("bow_f_hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 8, thrust_damage(5, cut)|spd_rtng(95)|abundance(100)|weight(1.5)|accuracy(75)|shoot_speed(55), imodbit_heavy|imodbits_crossbow],

	["short_bow", "Hunting Self Bow", [("bow_f_simple", imodbits_none), ("bow_f_simple_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 117, thrust_damage(7, cut)|spd_rtng(70)|abundance(100)|weight(2.0)|accuracy(80)|difficulty(1)|shoot_speed(65), imodbit_heavy|imodbits_crossbow],

	["nomad_bow", "Composite Bow", [("bow_f_dothraki", imodbits_none), ("bow_f_dothraki_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 269, thrust_damage(8, cut)|spd_rtng(60)|abundance(100)|weight(2.75)|accuracy(90)|difficulty(3)|shoot_speed(95), imodbit_heavy|imodbits_crossbow, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium, fac_culture_anatolian, fac_culture_mongol]],

	["long_bow", "Yew Self Long Bow", [("bow_f_longbow_2", imodbits_none), ("bow_f_longbow_2_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 445, thrust_damage(10, pierce)|spd_rtng(45)|abundance(100)|weight(3.0)|accuracy(90)|difficulty(4)|shoot_speed(85), imodbit_heavy|imodbits_crossbow, [], [fac_kingdom_4, fac_kingdom_6, fac_kingdom_9, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14]],

	["khergit_bow", "Reflex Bow", [("bow_f_dornish", imodbits_none), ("bow_f_dornish_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 137, thrust_damage(6, cut)|spd_rtng(65)|abundance(100)|weight(2.25)|accuracy(85)|difficulty(2)|shoot_speed(90), imodbit_heavy|imodbits_crossbow, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["strong_bow", "Self Bow", [("bow_f_longbow_1", imodbits_none), ("bow_f_longbow_1_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 258, thrust_damage(9, cut)|spd_rtng(60)|abundance(100)|weight(2.5)|accuracy(85)|difficulty(2)|shoot_speed(75), imodbit_heavy|imodbits_crossbow],

	["hunting_crossbow", "Hunting Crossbow", [("crossbow_new", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 122, thrust_damage(30, pierce)|max_ammo(1)|spd_rtng(45)|abundance(100)|weight(1.75)|accuracy(75)|shoot_speed(55), imodbit_heavy|imodbits_crossbow],

	["light_crossbow", "Cavalry Crossbow", [("crossbow_b", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 267, thrust_damage(35, pierce)|max_ammo(1)|spd_rtng(35)|abundance(100)|weight(2.5)|accuracy(80)|shoot_speed(65), imodbit_heavy|imodbits_crossbow],

	["crossbow", "Crossbow", [("crossbow_c", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 382, thrust_damage(40, pierce)|max_ammo(1)|spd_rtng(30)|abundance(100)|weight(3.25)|accuracy(85)|shoot_speed(75), imodbit_heavy|imodbits_crossbow],

	["heavy_crossbow", "Composite Crossbow", [("crossbow_a", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 949, thrust_damage(45, pierce)|max_ammo(1)|spd_rtng(25)|abundance(80)|weight(4.25)|accuracy(90)|difficulty(6)|shoot_speed(100), imodbit_heavy|imodbits_crossbow],

	["sniper_crossbow", "Arbalest", [("xenoargh_arbalest", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_cant_reload_while_moving, itcf_shoot_crossbow|itcf_carry_crossbow_back|itcf_reload_musket, 1083, thrust_damage(50, pierce)|max_ammo(1)|spd_rtng(20)|abundance(40)|weight(6.0)|accuracy(95)|difficulty(9)|shoot_speed(110), imodbit_heavy|imodbits_crossbow],

	["torch", "Tizona", [("fi_tri_blade_b", imodbits_none)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_no_blur, itcf_carry_sword_left_hip|itc_longsword, 100000, thrust_damage(35, pierce)|hit_points(43008)|spd_rtng(100)|weight(3.0)|swing_damage(40, cut)|difficulty(9)|weapon_length(119), imodbits_none],

	["arena_sword", "European Sidesword", [("sword_euro_9", imodbits_none), ("sword_euro_9_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1700, thrust_damage(34, pierce)|hit_points(37888)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["arena_sword_two_handed", "Ornate European Longsword", [("sword_euro_10", imodbits_none), ("sword_euro_10_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3500, thrust_damage(36, pierce)|hit_points(37888)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(34, cut)|difficulty(9)|weapon_length(102), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["khergit_war_helmet", "Mongol Helmet", [("mongolian_helmet", imodbits_none), ("mongolian_helmet_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["khergit_guard_helmet", "Mongol Lamellar Helmet", [("lamellar_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["khergit_cavalry_helmet", "Mongol Helmet", [("lamellar_helmet_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["khergit_guard_boots", "Scandinavian Shortsword", [("norman_short_sword_2", imodbits_none), ("norman_short_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(38912)|spd_rtng(100)|abundance(100)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(82), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["tunic_with_green_cape", "Tunic with Green Cape", [("archer_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["keys", "Bastard Bearded Axe", [("vik_tveirhendr_haloygox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(88), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["bride_dress", "Bride Dress", [("bride_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["bride_crown", "Crown of Flowers", [("bride_crown", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1, abundance(100)|weight(0.5)|head_armor(4), imodbits_cloth],

	["bride_shoes", "Bride Shoes", [("bride_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 30, abundance(100)|weight(1.0)|leg_armor(8), imodbits_cloth],

	["practice_bow_2", "One Handed GallÃ³glaigh Axe", [("talak_jomsviking_axe", imodbits_none), ("talak_jomsviking_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(43008)|spd_rtng(87)|abundance(100)|weight(1.87)|swing_damage(27, cut)|difficulty(6)|weapon_length(58), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["practice_arrows_2", "Bastard Gaelic Axe", [("gaelic_long_axe", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(85), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["heraldic_mail_with_surcoat_for_tableau", "Scandinavian Sword", [("the_stamford", imodbits_none), ("the_stamford_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["almogavar_sword", "Iberian Sword", [("varangiansword", imodbits_none), ("varangiansword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(22, cut)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.75)|swing_damage(32, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_iberian, fac_culture_andalus]],

	["welsh_archer", "Welsh Bowman Tunic", [("welsh_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_9]],

	["long_axe_3_alt", "Long War Axe", [("vik_long_hedmarkox", imodbits_none)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_civilian|itp_next_item_as_melee|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itc_parry_polearm, 245, thrust_damage(41, cut)|hit_points(44032)|spd_rtng(73)|abundance(100)|weight(3.625)|swing_damage(41, cut)|difficulty(12)|weapon_length(127), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["long_axe_4_alt", "Long War Axe", [("vik_long_hedmarkox_alt", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_thrust_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 0, thrust_damage(32, pierce)|hit_points(44032)|spd_rtng(83)|weight(3.625)|swing_damage(20, blunt)|difficulty(12)|weapon_length(127), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["armenian_knight_c", "Bastard Small Axe", [("vik_tveirhendr_hedmarkrox_small", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(89), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

	["archer_a", "Nobleman Outfit", [("noble_cloak", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["archer_b", "Tunic", [("archer_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["archer_c", "Shirt", [("archer_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surcoat_a", "Gambeson", [("surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surcoat_b", "Gambeson", [("surcoat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surcoat_c", "Gambeson", [("surcoat_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surcoat_d", "Gambeson", [("surcoat_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surcoat_e", "Gambeson", [("surcoat_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surcoat_f", "Gambeson", [("surcoat_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["surcoat_g", "Mail Hauberk", [("surcoat_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["teu_hbrother_a", "HalbbrÃ¼der Surcoat over Mail Haubergeon", [("teu_hbrother_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_hbrother_b", "HalbbrÃ¼der Surcoat over Mail Haubergeon", [("teu_hbrother_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

	["flat_kettle_hat", "Flattop Kettle Helm", [("flat_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["seljuk_horse", "Seljuk Horse", [("seljuk_horse", imodbits_none)], itp_type_horse, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_22]],

	["seljuk_armour", "Seljuk Gambeson", [("seljuk_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_22]],

	["seljuk_lamellar_a", "Seljuk Lamellar Vest", [("seljuk_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

	["seljuk_lamellar_b", "Seljuk Lamellar Vest", [("seljuk_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

	["andalus_helmet_a", "Andalusian Helm with Full Mail Coif", [("andalus_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["andalus_infantry_helmet", "Andalusian Helm with Full Mail Coif", [("andalus_infantry_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["andalusian_knight", "Andalusian Surcoat over Mail Hauberk", [("andalusian_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["gaelic_mail_shirt_a", "Gaelic Gambeson", [("gaelic_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_1", "Targe", [("s_h1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["highlander_boots_1", "Highlander Boots", [("highlander_boots_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_byrnie_a", "Gaelic Gambeson", [("gaelic_byrnie_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_byrnie_b", "Gaelic Gambeson", [("gaelic_byrnie_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["genoa_padded_a", "Italian Gambeson", [("genoa_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_padded_b", "Italian Gambeson", [("genoa_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_padded_c", "Italian Gambeson", [("genoa_padded_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_mail_b", "Italian Gambeson", [("genoa_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_mail_c", "Italian Gambeson", [("genoa_mail_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["shortened_voulge", "Shortened Voulge", [("mackie_short_voulge", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_sword_left_hip|itcf_horseback_slash_polearm|itc_longsword, 205, thrust_damage(29, pierce)|hit_points(36864)|spd_rtng(81)|abundance(100)|weight(2.875)|swing_damage(39, cut)|difficulty(9)|weapon_length(86), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

	["andalusian_shield_2", "Finnish Billhook", [("mackie_vesuri", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_axe_left_hip|itc_cleaver|itc_parry_two_handed, 200, hit_points(36864)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(34, cut)|difficulty(6)|weapon_length(70), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_kingdom_14]],

	["andalusian_shield_3", "Moorish Shield", [("andalusian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, [], [fac_culture_andalus]],

	["andalusian_shield_4", "Tough Moorish Shield", [("heavy_adarga", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, hit_points(51)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(36)|resistance(67)|shield_height(70), imodbits_shield, [], [fac_culture_andalus]],

	["andalusian_helmet_a", "Andalusian Helmet with Mail Coif", [("andalusian_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["andalusian_helmet_b", "Iberian Helmet with Mail Coif", [("andalusian_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["talak_warhammer", "War Pick", [("rrr_hammer2", imodbits_none), ("rrr_hammer2_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 500, hit_points(31744)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(34, pierce)|difficulty(9)|weapon_length(60), imodbit_bent|imodbit_chipped|imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_kingdom_9]],

	["meghrebi_leather_a", "Meghrebi Gambeson", [("meghrebi_leather_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["meghrebi_leather_b", "Meghrebi Gambeson", [("meghrebi_leather_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["meghrebi_leather_c", "Meghrebi Gambeson", [("meghrebi_leather_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["meghrebi_vest", "Meghrebi Gambeson", [("meghrebi_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["buff_leather", "Iberian Gambeson", [("buff_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["black_guard", "Arabic Gambeson", [("black_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["black_guard_helmet", "Saracen Fluted Helmet with Full Mail Coif", [("black_guard_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["gaelic_mail_shirt_b", "Gaelic Gambeson", [("gaelic_mail_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["surcoat_gaelic", "Gaelic Scale Shirt", [("gaelic_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_13]],

	["almohad_robe_a", "Almohad Gambeson", [("almohad_robe_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_robe_b", "Almohad Gambeson", [("almohad_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_robe_c", "Almohad Gambeson", [("almohad_robe_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_robe_d", "Almohad Gambeson", [("almohad_robe_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_padded_a", "Almohad Gambeson", [("almohad_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_padded_b", "Almohad Gambeson", [("almohad_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_padded_c", "Almohad Gambeson", [("almohad_padded_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_cavalry_a", "Almohad Gambeson", [("almohad_cavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_cavalry_b", "Almohad Gambeson", [("almohad_cavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["andalusian_archers_vest", "Andalusian Gambeson", [("andalusianarchers_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["andalusian_skirmisher_armor", "Andalusian Mail Hauberk", [("andalusianskirmisher_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["arabian_lamellar", "Arabic Gambeson", [("arabian_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["horse_d", "Courser", [("horse_d", imodbits_none), ("horse_d", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(120)|horse_maneuver(46)|abundance(60)|difficulty(3)|horse_charge(28)|horse_speed(45)|body_armor(24)|horse_scale(108), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion],

	["arab_nobleman_a", "Arabian Mail Hauberk", [("arab_nobleman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(50)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_nobleman_b", "Arabic Gambeson", [("arab_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_nobleman_c", "Arabic Gambeson", [("arab_nobleman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["andalusian_heavy_a", "Andalusian Scale over Mail Hauberk", [("andalusian_heavy_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["andalusian_heavy_b", "Andalusian Scale over Mail Hauberk", [("andalusian_heavy_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["berber_tunic_a", "Berber Gambeson", [("berber_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["berber_tunic_b", "Berber Leather Scale Vest", [("berber_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["berber_tunic_c", "Berber Gambeson", [("berber_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["berber_turban", "Moorish Turban", [("berber_turban", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_andalus]],

	["iberian_leather_armour_a", "Iberian Gambeson", [("iberian_leather_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["iberian_leather_armour_b", "Iberian Gambeson", [("iberian_leather_armour_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["iberian_leather_armour_c", "Iberian Gambeson", [("iberian_leather_armour_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["andalusi_horseman_robe", "Moorish Gambeson", [("andalusi_horseman_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

	["galloglass_mail", "GallÃ³glaigh Mail Hauberk", [("galloglass_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["galloglass_padded", "GallÃ³glach Mail Hauberk", [("galloglass_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["baltic_sword", "Baltic Short Falchion", [("dublin3_sword", imodbits_none), ("dublin3_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, cut)|hit_points(34816)|spd_rtng(90)|abundance(40)|weight(2.75)|swing_damage(32, cut)|difficulty(6)|weapon_length(69), imodbit_fine|imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["man_at_arms_a", "Gambeson", [("man_at_arms_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(80)|weight(12.0)|leg_armor(12)|body_armor(24), imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_thick|imodbit_hardened, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["man_at_arms_b", "Blue Gambeson over Mail Hauberk", [("man_at_arms_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["man_at_arms_c", "Red Gambeson over Mail Hauberk", [("man_at_arms_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["arab_padded_vest", "Saracen Gambeson", [("arab_padded_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_archer", "Saracen Gambeson", [("arab_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["mamluk_infantry_lamellar_a", "Mamluk Lamellar over Mail Hauberk", [("mamluk_infantry_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["mamluk_infantry_lamellar_b", "Mamluk Lamellar over Mail Hauberk", [("mamluk_infantry_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["targe_2", "Targe", [("s_h1_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_3", "Targe", [("s_h1_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_4", "Targe", [("s_h2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_5", "Targe", [("s_h2_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_6", "Targe", [("s_h2_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["balt_lamellar_coat_a", "Baltic Leather Lamellar Vest", [("baltic_lamellar_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_lamellar_coat_b", "Baltic Leather Lamellar Vest", [("baltic_lamellar_coat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["rus_padded", "Eastern Leather Scale", [("rus_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["baltic_sword_b", "Baltic Falchion", [("berserkr_sword", imodbits_none), ("berserkr_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(28, cut)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["mongol_helmet_a", "Mongol Lamellar Helmet", [("mongol_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["mongol_helmet_b", "Mongol Helmet", [("mongol_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["mongol_helmet_c", "Mongol Helmet", [("mongol_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["steppe_helmet", "Eastern Cap with Aventail", [("steppe_helmet", imodbits_none), ("inv_steppe_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1920, abundance(100)|weight(1.5)|difficulty(6)|body_armor(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["priest_cap_1", "Red Cap", [("rus_hat_02", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

	["priest_cap_2", "Cap", [("vik_tveirhendr_trondrox", imodbits_none), ("priest_cap_2", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur|itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 43, abundance(60)|weight(0.5)|head_armor(8), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace|imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western, fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["priest_robe_1", "Priest Robe", [("priest_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["priest_robe_2", "Priest Robe", [("priest_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["priest_robe_3", "Priest Robe", [("priest_2_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["surgeon", "Gambeson", [("studden_leather_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth],

	["bishop_great_helm", "Bishop Great Helm", [("osp_greathelm_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["bishop_armour", "Archbishop Surcoat over Mail Haubergeon", [("bishop", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["bishop_mitre", "Bishop Mittre with Mail Coif", [("bishop_mitre", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

	["bishop_staff", "Lance of Longinus", [("fi_cross_spear", imodbits_none)], itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_covers_head|itp_couchable|itp_crush_through|itp_no_blur, itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 100000, thrust_damage(36, pierce)|spd_rtng(94)|weight(3.6)|swing_damage(26, blunt)|difficulty(12)|weapon_length(162), imodbits_none],

	["varangian_shield_a", "Varangian Shield", [("varangian_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["varangian_shield_b", "Varangian Shield", [("varangian_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["varangian_shield_c", "Varangian Shield", [("varangian_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sabre", "Byzantine Sabre", [("paramerion", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itc_scimitar, 2000, hit_points(36864)|spd_rtng(110)|abundance(40)|weight(2.5)|swing_damage(30, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_byzantium]],

	["byzantine_sword", "Pike", [("fi_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_pike|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_thrust_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(50, pierce)|hit_points(10240)|spd_rtng(70)|abundance(30)|weight(5.0)|swing_damage(15, blunt)|difficulty(12)|weapon_length(300), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["byzantine_sword_1", "Scandinavian Damascus Steel Sword", [("gaelic_fine_sword", imodbits_none), ("gaelic_fine_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 10000, thrust_damage(28, pierce)|hit_points(39936)|spd_rtng(95)|abundance(5)|weight(2.5)|swing_damage(36, cut)|difficulty(9)|weapon_length(90), imodbit_fine|imodbit_balanced|imodbit_tempered|imodbit_masterwork, [], [fac_culture_nordic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium]],

	["byzantine_sword_3", "Balkan Scimitar", [("sabre_rus_2_1", imodbits_none), ("sabre_rus_2_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(99), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_4", "Balkan Scimitar", [("sabre_rus_3_1", imodbits_none), ("sabre_rus_3_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(40960)|spd_rtng(105)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_5", "Balkan Scimitar", [("sabre_rus_4_1", imodbits_none), ("sabre_rus_4_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(99), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_7", "Balkan Scimitar", [("sabre_rus_5_1", imodbits_none), ("sabre_rus_5_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(41984)|spd_rtng(105)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_extra", "Balkan Scimitar", [("sabre_rus_1_1", imodbits_none), ("sabre_rus_1_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_shield_a_3", "Almond Shield", [("rus_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["rus_shield_b_3", "Almond Shield", [("rus_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["rus_shield_c_3", "Almond Shield", [("rus_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["rus_shield_d_3", "Almond Shield", [("rus_shield_d", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

	["cuman_noble_helmet", "Cuman Enclosed Helmet", [("cuman_noble", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["ghulam_helmet", "Ghulam Helmet with Mail Coif", [("ghulam_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["ilkhanate_mongol_helmet", "Mongol Helmet", [("ilkhanate_mongol_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["polski_helm", "Polish Helmet with Mail Coif", [("polska_helma", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

	["mamluke_helm_b", "Mighfar with Aventail", [("mamluke_helm_b", imodbits_none), ("inv_mamluke_helm_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mongol_helmet_d", "Mongol Helmet", [("mongol_leather_helm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["nikloskoe_helmet_warrior", "Nikloskoe Enclosed Helmet", [("nikloskoe_helmet_warrior", imodbits_none), ("inv_nikloskoe_helmet_warrior", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kiev_helmet_2_facemail", "Rus Enclosed Helmet", [("kiev_helmet_2_facemail", imodbits_none), ("inv_kiev_helmet_2_facemail", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["kiev_helmet_1_facemail_1", "Rus Enclosed Helmet", [("kiev_helmet_1_facemail_1", imodbits_none), ("inv_kiev_helmet_1_facemail_1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_byzantinenoble_kettle", "Byzantine Kettle Helm with Aventail", [("rus_byzantinenoble_kettle", imodbits_none), ("inv_byzantinenoble_kettle", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["rus_helmet_a", "Eastern Helmet with Aventail", [("rus_helmet_a", imodbits_none), ("inv_rus_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_infantry_helmet", "Eastern Helmet with Padding", [("rus_infantry_helmet", imodbits_none), ("inv_rus_infantry_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_militia_helmet", "Eastern Helmet with Mail Coif", [("rus_militia_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(1.75)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_noble_helmet", "Yesenovo Enclosed Helmet", [("rus_noble_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["seljuk_archer_cap", "Seljuk Cap", [("seljuk_archer_cap", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["ilkhanate_cap", "Ilkanate Hat with Padding", [("ilkhanate_cap", imodbits_none), ("inv_ilkhanate_cap", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["cuman_cap_d", "Cuman Hat with Aventail", [("cuman_cap_d", imodbits_none), ("inv_cuman_cap_d", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1920, abundance(100)|weight(1.5)|difficulty(6)|body_armor(6)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

	["anatolian_horseman_lamellar", "Anatolian Lamellar over Mail Hauberk", [("anatolian_horseman_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["anatolian_leather_lamellar", "Anatolian Lamellar Armour", [("anatolian_leather_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["anatolian_mail", "Anatolian Mail Hauberk", [("anatolian_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["arab_headcloth", "Headcloth", [("arab_headcloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["seljuk_tunic", "Seljuk Mail Hauberk", [("seljuk_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["seljuk_tunic_b", "Seljuk Mail Hauberk", [("seljuk_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["seljuk_tunic_c", "Seljuk Mail Hauberk", [("seljuk_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_noble_mail", "Rus Mail Hauberk", [("rus_noble_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_mask_helmet", "Rus Enclosed Helmet", [("mask_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["mamluk_lamellar", "Mamluk Lamellar Armour", [("mamluk_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["rus_leather_scale", "Rus Lamellar over Mail Hauberk", [("rus_scale_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_leather_scale_b", "Rus Leather Scale over Mail Hauberk", [("rus_scale_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rohatyna", "War Spear", [("ped_fjadraspjot", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 200, thrust_damage(35, pierce)|hit_points(32768)|spd_rtng(95)|abundance(100)|weight(2.5)|swing_damage(15, blunt)|difficulty(9)|weapon_length(150), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

	["flat_topped_helmet_a", "Spangen Helmet with Mail Coif", [("flattop_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["flat_topped_helmet_b", "Spangen Helmet with Mail Coif", [("flattop_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["great_helmet_a", "Great Helm", [("greathelmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_b", "Great Helm", [("greathelmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_c", "Great Helm", [("greathelmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_d", "Cervelliere", [("greathelmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_decorative", "Phrigian Helm with Mail Coif", [("greathelmet_decorative", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["bill", "Billhook", [("billhook", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 400, thrust_damage(22, blunt)|hit_points(14029)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(152), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["almogavar_helmet", "Almoghavar Helmet", [("almogavar_helmet", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["curonian_helmet", "Curonian Helmet with Mail Coif", [("curonian_helmet", imodbits_none)], itp_type_head_armor, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_padded_a", "Baltic Gambeson", [("balt_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_2]],

	["balt_padded_b", "Baltic Gambeson", [("balt_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_2]],

	["thomas_padded_armour", "Baltic Gambeson", [("thomas_padded_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_2]],

	["militia_tunic_a", "Gambeson", [("padded_long_orange", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["militia_tunic_b", "Gambeson", [("padded_long_bge", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rus_militia_padded_a", "Rus Gambeson", [("rus_militia_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["little_samogitian", "Å½emaitukas", [("warmblood", imodbits_none), ("warmblood", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 512, hit_points(120)|horse_maneuver(49)|abundance(60)|difficulty(3)|horse_charge(10)|horse_speed(45)|body_armor(24)|horse_scale(95), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_baltic]],

	["kettlehat_a", "Kettle Helm with Mail Coif", [("kettlehat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["kettlehat_b", "Kettle Helm with Mail Coif", [("kettlehat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["kettlehat_c", "Kettle Helm with Mail Coif and Rondels", [("kettlehat_cheek", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["andalus_marinid_hasfid_elite_a", "Moorish Mail Hauberk", [("andalus_marinid_hasfid_elite_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

	["andalus_marinid_hasfid_elite_b", "Moorish Mail Hauberk", [("andalus_marinid_hasfid_elite_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

	["berber_kaftan", "Moorish Gambeson", [("berber_kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["berber_mail_a", "Moorish Mail Hauberk", [("berber_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

	["berber_mail_b", "Moorish Mail Hauberk", [("berber_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

	["seljuk_hauberk_jawshan", "Seljuk Lamellar Vest", [("seljuk_hauberk_jawshan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["mamluk_jawshan_leather", "Mamluk Gambeson", [("mamluk_jawshan_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["horse_e", "Courser", [("horse_e", imodbits_none), ("horse_e", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(120)|horse_maneuver(46)|abundance(60)|difficulty(3)|horse_charge(28)|horse_speed(45)|body_armor(24)|horse_scale(108), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion],

	["gaelic_shirt_blue", "Gaelic Shirt", [("gaelic_shirt_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["gaelic_shirt_green", "Gaelic Shirt", [("gaelic_shirt_green_muted", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["gaelic_shirt_red", "Gaelic Shirt", [("gaelic_shirt_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

	["andalusian_helmet_c", "Andalusian Helmet", [("andalusian_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["andalusian_helmet_d", "Andalusian Helmet with Mail Coif", [("andalusian_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["arab_helmet_d", "Saracen Full Mail Helmet", [("arab_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["mamluk_helm_b", "Tawashi Helmet", [("mamluk_helmet_4", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["iberian_cleaver", "European Shortsword", [("norman_short_sword_p7", imodbits_none), ("norman_short_sword_p7_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(78), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["moorish_hat", "Moorish Hat", [("moorish_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["alsacian_sword", "Arabic Damascus Steel Scimitar", [("fi_scimitar_return", imodbits_none), ("fi_scab_scimitar_return", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 10000, hit_points(39936)|spd_rtng(100)|abundance(5)|weight(2.5)|swing_damage(38, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbit_balanced|imodbit_tempered|imodbit_masterwork, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium]],

	["moorish_axe", "Arabic Mace", [("saracen_mace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_mace_left_hip|itc_cleaver|itc_parry_two_handed, 560, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(3.5)|swing_damage(31, blunt)|difficulty(9)|weapon_length(74), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_iberian]],

	["kettle_cloth", "Kettle Helm", [("kettle_cloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["armenian_knight_a", "Green Robe", [("armenian_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rus_helmet", "Rus Helmet with Mail Coif", [("rus_helmet", imodbits_none), ("inv_rus_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_helmet_1", "Rus Helmet with Mail Coif", [("rus_helmet1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_helmet_2", "Rus Helmet with Full Mail Coif", [("rus_helmet2", imodbits_none), ("inv_rus_helmet2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_helmet_3", "Rus Enclosed Helmet", [("rus_helmet3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["balt_rus_cap", "Balt Cap with Padding", [("balt_rus_hat", imodbits_none), ("inv_balt_rus_hat", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_culture_rus]],

	["moors_quilted_kaftan_blue", "Moorish Gambeson", [("moors_quilted_kaftan_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["moors_quilted_kaftan_brown", "Moorish Gambeson", [("moors_quilted_kaftan_brown", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_marinid]],

	["czekan", "Maciejowski Axe", [("euro_axe_01", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 215, thrust_damage(35, cut)|hit_points(28697)|spd_rtng(79)|abundance(100)|weight(2.875)|swing_damage(35, cut)|difficulty(9)|weapon_length(95), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_western]],

	["ilkhanate_kaftan", "Mongol Gambeson", [("mongol_ilkhanate_kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

	["turk_kaftan_beige", "Turkic Gambeson", [("turk_kaftan_beige", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_15, fac_kingdom_22, fac_kingdom_29, fac_kingdom_30]],

	["turk_kaftan_furtrim", "Turkic Gambeson", [("turk_kaftan_furtrim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_15, fac_kingdom_22, fac_kingdom_29, fac_kingdom_30]],

	["turk_kaftan_green", "Turkic Lamellar over Mail Hauberk", [("turk_kaftan_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7, fac_kingdom_15, fac_kingdom_22, fac_kingdom_29, fac_kingdom_30]],

	["saracen_mail", "Saracen Mail Hauberk", [("kau_arabian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["jineta_sword", "Scandinavian Shortsword", [("norman_short_sword", imodbits_none), ("norman_short_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(38912)|spd_rtng(100)|abundance(100)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(82), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["gaelic_helmet_a", "Gaelic Helmet", [("gaelic_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_13]],

	["priest_cap_2", "Cap", [("vik_tveirhendr_trondrox", imodbits_none), ("priest_cap_2", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur|itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 43, abundance(60)|weight(0.5)|head_armor(8), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace|imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western, fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["byz_helmet_b", "Byzantine Helmet", [("byz_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["pilgrim_hat", "Hat", [("pilgrim_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gaelic_long_tunic_a", "Tunic", [("gaelic_long_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_long_tunic_b", "Tunic", [("gaelic_long_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_long_tunic_c", "Tunic", [("gaelic_long_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_shield_a", "Gaelic Infantry Shield", [("gaelic_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_shield_b", "Gaelic Shield", [("gaelic_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_shield_c", "Gaelic Shield", [("gaelic_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["rhodok_great_helmet", "Heaume", [("rhodok_great_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rhodok_four_plated_helmet", "Kettlehelm with Mail Coif", [("kettlehat2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rhodok_kettle_hat_c", "Kettle Helm with Padding", [("rhodok_kettle_hat_c", imodbits_none), ("inv_rhodok_kettle_hat_c", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["rhodok_nasal_helmet_a", "Norman Helm with Aventail", [("rhodok_nasal_helmet_a", imodbits_none), ("inv_rhodok_nasal_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["saint_thomas_knight", "Order Surcoat of the Knights of Saint Thomas", [("rnd_surcoat_santiago", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["lazarus_serjeant_tunic", "Order Mantle of the Knights of Saint Lazarus", [("lazarus_serjeant_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["calatrava_knight", "Order Surcoat of the Knights of Calatrava", [("rnd_surcoat_calatrava", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["santiago_knight", "Order Mantle of the Knights of Santiago", [("santiago_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

	["studden_leather_armour_a", "Mail Hauberk", [("norman_short_hauberk_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["faris_helmet", "Saracen Helm", [("faris_helmet", imodbits_none)], itp_type_head_armor, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["arab_mail_e", "Saracen Lamellar Armour", [("arab_mail_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["georgian_mail", "Armenian Mail Hauberk", [("georgian_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["seljuk_scale_a", "Saracen Lamellar over Mail Hauberk", [("seljuk_scale_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["balt_shirt_c", "Baltic Gambeson", [("balt_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["armenian_mail_b", "Armenian Mail Hauberk", [("armenian_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kau_turcopole_a", "Turcopole Gambeson", [("kau_turcopole_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["kau_turcopole_b", "Turcopole Gambeson", [("kau_turcopole_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["mamluk_cap", "Seljuk Cap", [("mamluk_cap", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["1257_hood", "Hood", [("1257_hood", imodbits_none), ("inv_1257_hood", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 195, abundance(100)|weight(1.0)|body_armor(2)|head_armor(8), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

	["berber_turban_cape", "Berber Turban", [("berber_turban_cape", imodbits_none), ("inv_berber_turban_cape", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus]],

	["bulgar_warrior_a", "Bulgarian Lamellar Vest", [("bulgar_warrior_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

	["bulgar_warrior_b", "Bulgarian Gambeson", [("bulgar_warrior_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

	["bulgar_helm", "Bulgar Helm with Aventail", [("bulgar_helm", imodbits_none), ("inv_bulgar_helm", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["bulgar_helm_b", "Bulgar Helm with Padding", [("bulgar_helm_b", imodbits_none), ("inv_bulgar_helm_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["berber_robe_a", "Berber Gambeson", [("berber_robe_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["berber_robe_b", "Berber Gambeson", [("berber_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["berber_robe_c", "Berber Gambeson", [("berber_robe_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

	["saracen_kaftan_a", "Saracen Gambeson", [("saracen_kaftan_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["saracen_kaftan_b", "Saracen Gambeson", [("saracen_kaftan_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["saracen_kaftan_c", "Saracen Gambeson", [("saracen_kaftan_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["saracen_kaftan_d", "Saracen Gambeson", [("saracen_kaftan_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["rus_hat_with_padding", "Rus Hat with Padding", [("rus_hat_with_padding", imodbits_none), ("inv_rus_hat_with_padding", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_culture_rus]],

	["mongol_fur_hat", "Mongol Tribal Hat", [("mongol_fur_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a", imodbits_none), ("mongol_warrior_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol, fac_culture_mongol]],

	["gaelic_tunic_cape_a", "Gaelic Gambeson", [("gaelic_tunic_cape_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["kettle_cloth_cape_b", "Kettle Helm with Padding", [("kettle_cloth_cape_b", imodbits_none), ("inv_kettle_cloth_cape_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kettle_cloth_cape", "Kettle Helm with Padding", [("kettle_cloth_cape", imodbits_none), ("inv_kettle_cloth_cape", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["wenceslav_helmet", "Saint Wenceslav Helmet with Aventail", [("wenceslav_helmet", imodbits_none), ("inv_wenceslav_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["baltic_ponted_helmet", "Balt Helmet with Aventail", [("baltic_ponted_helmet", imodbits_none), ("inv_baltic_ponted_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

	["berber_white_turban", "Turban Helm with Aventail", [("berber_white_turban", imodbits_none), ("inv_berber_white_turban", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["surcoat_france_b", "French Plated Surcoat over Golden Mail", [("surcoat_france_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_10]],

	["byzantine_crown", "Crown", [("byzantine_crown", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 300, abundance(30)|weight(0.5)|head_armor(4), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["rus_coat", "Rus Coat", [("varangian_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["moor_helmet_a", "Andalusian Helmet with Mail Coif", [("moor_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["moor_helmet_b", "Andalusian Helmet with Mail Coif", [("moor_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["moor_helmet_c", "Andalusian Helmet with Mail Coif", [("moor_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["moor_helmet_d", "Andalusian Helmet with Mail Coif", [("moor_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["berber_helmet_g", "Berber Turban", [("berber_helmet_g", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 267, abundance(100)|weight(1.25)|head_armor(20), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["andalusian_helmet_e", "Andalusian Helmet with Mail Coif", [("andalusian_helmet_e", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["megreb_spangen", "Plain Helm", [("megreb_spangen", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["mamluke_helm_ventail", "Mamluk Helmet with Mail Coif", [("mamluke_helm_ventail", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mongol_kettle", "Mongol Kettle Helm", [("mongol_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["kipchak_steppe_helmet", "Kiphak Helmet with Full Mail Coif", [("kipchak_steppe_helmet", imodbits_none), ("inv_kipchak_steppe_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["mongol_warrior_de", "Mongol Lamellar Armour", [("mongol_warrior_de", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

	["yaroslav_helmet", "Rus Noble Helmet with Aventail", [("yaroslav_helmet", imodbits_none), ("inv_yaroslav_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["polovtsian_helmet", "Volga Bulgar Veiled Helmet with Aventail", [("polovtsian_helmet", imodbits_none), ("inv_polovtsian_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6320, abundance(40)|weight(2.75)|difficulty(12)|body_armor(6)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

	["byz_helmet_golden", "Byzantine Helmet with Aventail", [("byz_helmet_golden", imodbits_none), ("inv_byz_helmet_golden", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["nordic_fur_cap", "Nordic Hat", [("nordic_fur_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_rus]],

	["gaelic_crown", "Crown", [("gaelic_crown", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 300, abundance(30)|weight(0.5)|head_armor(4), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["helmet_with_feathers", "Enclosed Helm", [("normanpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["frenchpepperpot2", "Enclosed Helm", [("frenchpepperpot2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["frenchpepperpot3", "Enclosed Helm", [("frenchpepperpot3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["munitionshelm2", "Enclosed Helm", [("munitionshelm2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["pepperpothelm1", "Enclosed Helm", [("pepperpothelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["munitionshelm1", "Enclosed Helm", [("munitionshelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["frenchpepperpot", "Rounded Enclosed Helmet", [("frenchpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish, fac_culture_western]],

	["steel_bolts", "Munitions Bolts", [("vik_munitions_bolt", imodbits_none), ("vik_munitions_bolt", ixmesh_flying_ammo), ("vik_bolt_bag_b", ixmesh_carry)], itp_type_bolts|itp_merchandise, itcf_carry_quiver_right_vertical, 150, thrust_damage(23, cut)|max_ammo(29)|abundance(100)|weight(1.5)|weapon_length(64), imodbit_large_bag, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["new_turban_a", "Turban", [("new_turban_a", imodbits_none), ("inv_new_turban_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["new_turban_b", "Turban", [("new_turban_b", imodbits_none), ("inv_new_turban_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

	["kufia_berber_black", "Berber Helm", [("kufia_berber_black", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 1600, weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

	["african_spangen", "Spangen Helm", [("african_spangen", imodbits_none)], itp_type_head_armor|itp_covers_head|itp_couchable, 0, 1600, weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

	["african_turban", "African Turban", [("african_turban", imodbits_none)], itp_type_head_armor|itp_covers_head|itp_couchable, 0, 0, weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_marinid]],

	["head_african", "African Head", [("head_african", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_covers_head|itp_couchable, 0, 0, weight(0.5), imodbits_cloth, [], [fac_culture_marinid]],

	["african_hat", "African Hat", [("african_hat", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_covers_head|itp_couchable, 0, 0, weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_marinid]],

	["legs_african", "African Boots", [("legs_african", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid]],

	["hands_african", "Hands African", [("hands_african_L", imodbits_none)], itp_type_hand_armor, 0, 0, weight(0.25), imodbits_cloth, [], [fac_culture_marinid]],

	["african_trousers", "African Trousers", [("african_trousers", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid]],

	["irish_surcoat", "Irish Surcoat over Mail Haubergeon", [("irish_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["crown_european", "Crown", [("crown_european", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(100)|weight(1.0)|head_armor(10), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["crown", "Crown", [("crown", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(100)|weight(1.0)|head_armor(10), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["seljuk_hair", "Seljuk Hairstyle", [("seljuk_hair", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 3, abundance(100)|weight(1.0)|head_armor(2), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["flag_pole_1", "Flag", [("flag_pole_1", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_parry_polearm, 40000, spd_rtng(60)|abundance(100)|weight(16.5)|weapon_length(155), imodbits_none, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_flag_pole", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["flag_pole_2", "Flag", [("flag_pole_2", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_parry_polearm, 40000, spd_rtng(60)|abundance(100)|weight(16.5)|weapon_length(155), imodbits_none],

	["flag_pole_3", "Flag", [("flag_pole_3", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_parry_polearm, 40000, spd_rtng(60)|abundance(100)|weight(16.5)|weapon_length(155), imodbits_none, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_flag_pole", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["cross", "Cross", [("true_cross", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_parry_polearm, 40000, spd_rtng(60)|abundance(100)|weight(16.5)|weapon_length(155), imodbits_none],

	["items_end_", "Surcoat over Mail Haubergeon", [("rnd_surcoat_20_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

]