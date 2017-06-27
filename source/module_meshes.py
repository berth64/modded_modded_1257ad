from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
	("pic_bandits", 0, "pic_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mb_warrior_1", 0, "pic_mb_warrior_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_messenger", 0, "pic_messenger_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_man", 0, "pic_prisoner_man", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_fem", 0, "pic_prisoner_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_wilderness", 0, "pic_prisoner_wilderness", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_sighted", 0, "pic_siege_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_sighted_fem", 0, "pic_siege_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_camp", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_payment", 0, "pic_payment", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_escape_1", 0, "pic_escape_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_escape_1_fem", 0, "pic_escape_1_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_victory", 0, "pic_victory_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_defeat", 0, "pic_defeat", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wounded", 0, "pic_wounded", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wounded_fem", 0, "pic_wounded_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_steppe_bandits", 0, "pic_taiga_bandits_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_tundra_bandits", 0, "pic_tundra_bandits_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_desert_bandits", 0, "pic_desert_bandits_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mountain_bandits", 0, "pic_mountain_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sea_raiders", 0, "pic_pirates_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_deserters", 0, "pic_deserters_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_forest_bandits", 0, "pic_forest_bandits_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_roving_knights", 0, "pic_roving_knights_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cattle", 0, "pic_cattle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_looted_village", 0, "pic_looted_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_p", 0, "pic_village_p", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_s", 0, "pic_village_s", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_w", 0, "pic_village_w", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_recruits", 0, "pic_recruits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castle1", 0, "pic_castle1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castledes", 0, "pic_castledes", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castlesnow", 0, "pic_castlesnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_charge", 0, "pic_charge", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sally_out", 0, "pic_sally_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_attack", 0, "pic_siege_attack", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_town1", 0, "pic_town1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_towndes", 0, "pic_towndes", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_townriot", 0, "pic_townriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_townsnow", 0, "pic_townsnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_villageriot", 0, "pic_villageriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_teutonic", 0, "pic_arms_teutonic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_lithuania", 0, "pic_arms_lithuania", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_mongol", 0, "pic_arms_mongol", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_denmark", 0, "pic_arms_denmark", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_poland", 0, "pic_arms_poland", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_hre", 0, "pic_arms_hre", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_hungary", 0, "pic_arms_hungary", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_novgorod", 0, "pic_arms_novgorod", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_england", 0, "pic_arms_england", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_france", 0, "pic_arms_france", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_norway", 0, "pic_arms_norway", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_scotland", 0, "pic_arms_scotland", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_ireland", 0, "pic_arms_ireland", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_sweden", 0, "pic_arms_sweden", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_galicia", 0, "pic_arms_galicia", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_portugal", 0, "pic_arms_portugal", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_aragon", 0, "pic_arms_aragon", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_castile", 0, "pic_arms_castile", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_navarre", 0, "pic_arms_navarre", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_granada", 0, "pic_arms_granada", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_papacy", 0, "pic_arms_papacy", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_byzantine", 0, "pic_arms_byzantine", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_acre", 0, "pic_arms_acre", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_sicily", 0, "pic_arms_sicily", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_mameluke", 0, "pic_arms_mameluke", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_latin", 0, "pic_arms_latin", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_ilkhanate", 0, "pic_arms_ilkhanate", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_hafsid", 0, "pic_arms_hafsid", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_serbia", 0, "pic_arms_serbia", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_bulgaria", 0, "pic_arms_bulgaria", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_marinid", 0, "pic_arms_marinid", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_venice", 0, "pic_arms_venice", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_jotvingians", 0, "pic_arms_pagan", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_prussia", 0, "pic_arms_prussia", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_curonnians", 0, "pic_arms_pagan", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_samogitian", 0, "pic_arms_samogitian", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_wales", 0, "pic_arms_wales", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_genoa", 0, "pic_arms_genoa", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_pisa", 0, "pic_arms_pisa", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_guelph", 0, "pic_arms_guelph", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_gibelini", 0, "pic_arms_gibelini", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_bohemia", 0, "pic_arms_bohemia", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_weuro", 0, "pic_encounter_weuro", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_leuro", 0, "pic_encounter_leuro", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_rus", 0, "pic_encounter_rus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_teutonic", 0, "pic_encounter_teutonic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_mongol", 0, "pic_encounter_mongol", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_balt", 0, "pic_encounter_balt", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_scand", 0, "pic_encounter_scand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_welsh", 0, "pic_encounter_welsh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_irish", 0, "pic_encounter_irish", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_scot", 0, "pic_encounter_scot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_mamluk", 0, "pic_encounter_mamluk", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_andalus", 0, "pic_encounter_andalus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_byz", 0, "pic_encounter_byz", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_serbs", 0, "pic_encounter_serbs", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_bulgars", 0, "pic_encounter_bulgars", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_iberians", 0, "pic_encounter_iberians", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_marrinid", 0, "pic_encounter_marrinid", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_baltic_village", 0, "pic_baltic_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_baltic_castle", 0, "pic_baltic_castle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_baltic_town", 0, "pic_baltic_town", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cataholic_village", 0, "pic_cataholic_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cataholic_castle", 0, "pic_cataholic_castle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cataholic_town", 0, "pic_cataholic_town", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_orthodox_village", 0, "pic_orthodox_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_orthodox_castle", 0, "pic_orthodox_castle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_orthodox_town", 0, "pic_orthodox_town", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_muslim_town", 0, "pic_muslim_town", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_muslim_castle", 0, "pic_muslim_castle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_muslim_village", 0, "pic_muslim_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_knock_out_retreat", 0, "pic_knock_out_retreat", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_camp", 0, "pic_siege_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mongolian_camp", 0, "pic_mongolian_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_looters_new", 0, "pic_encounter_looters_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter_mountain_bandits_new", 0, "pic_encounter_mountain_bandits_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_tournament_euro", 0, "pic_tournament_euro", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_infantry", 0, "flag_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_archers", 0, "flag_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_cavalry", 0, "flag_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("inv_slot", 0, "inv_slot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_1", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_2", 0, "mp_ui_host_maps_a2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_3", 0, "mp_ui_host_maps_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_4", 0, "mp_ui_host_maps_ruinedf", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_5", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_6", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_7", 0, "mp_ui_host_maps_fieldby", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_8", 0, "mp_ui_host_maps_castle2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_9", 0, "mp_ui_host_maps_snovyv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_10", 0, "mp_ui_host_maps_castle3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_11", 0, "mp_ui_host_maps_c1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_12", 0, "mp_ui_host_maps_c2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_13", 0, "mp_ui_host_maps_c3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_randoms", 0, "mp_ui_host_maps_randoms", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sw", 0, "flag_project_sw", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_vg", 0, "flag_project_vg", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_kh", 0, "flag_project_kh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_nd", 0, "flag_project_nd", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rh", 0, "flag_project_rh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sr", 0, "flag_project_sr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_projects_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sw_miss", 0, "flag_project_sw_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_vg_miss", 0, "flag_project_vg_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_kh_miss", 0, "flag_project_kh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_nd_miss", 0, "flag_project_nd_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rh_miss", 0, "flag_project_rh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sr_miss", 0, "flag_project_sr_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_misses_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("color_picker", 0, "color_picker", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("custom_map_banner_01", 0, "custom_map_banner_01", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_map_banner_02", 0, "custom_map_banner_02", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_map_banner_03", 0, "custom_map_banner_03", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_banner_01", 0, "custom_banner_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("custom_banner_02", 0, "custom_banner_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("custom_banner_bg", 0, "custom_banner_bg", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg01", 0, "custom_banner_fg01", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg02", 0, "custom_banner_fg02", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg03", 0, "custom_banner_fg03", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg04", 0, "custom_banner_fg04", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg05", 0, "custom_banner_fg05", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg06", 0, "custom_banner_fg06", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg07", 0, "custom_banner_fg07", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg08", 0, "custom_banner_fg08", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg09", 0, "custom_banner_fg09", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg10", 0, "custom_banner_fg10", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg11", 0, "custom_banner_fg11", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg12", 0, "custom_banner_fg12", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg13", 0, "custom_banner_fg13", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg14", 0, "custom_banner_fg14", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg15", 0, "custom_banner_fg15", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg16", 0, "custom_banner_fg16", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg17", 0, "custom_banner_fg17", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg18", 0, "custom_banner_fg18", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg19", 0, "custom_banner_fg19", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg20", 0, "custom_banner_fg20", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg21", 0, "custom_banner_fg21", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg22", 0, "custom_banner_fg22", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg23", 0, "custom_banner_fg23", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_01", 0, "custom_banner_charge_01", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_02", 0, "custom_banner_charge_02", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_03", 0, "custom_banner_charge_03", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_04", 0, "custom_banner_charge_04", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_05", 0, "custom_banner_charge_05", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_06", 0, "custom_banner_charge_06", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_07", 0, "custom_banner_charge_07", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_08", 0, "custom_banner_charge_08", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_09", 0, "custom_banner_charge_09", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_10", 0, "custom_banner_charge_10", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_11", 0, "custom_banner_charge_11", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_12", 0, "custom_banner_charge_12", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_13", 0, "custom_banner_charge_13", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_14", 0, "custom_banner_charge_14", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_15", 0, "custom_banner_charge_15", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_16", 0, "custom_banner_charge_16", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_17", 0, "custom_banner_charge_17", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_18", 0, "custom_banner_charge_18", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_19", 0, "custom_banner_charge_19", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_20", 0, "custom_banner_charge_20", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_21", 0, "custom_banner_charge_21", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_22", 0, "custom_banner_charge_22", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_23", 0, "custom_banner_charge_23", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_24", 0, "custom_banner_charge_24", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_25", 0, "custom_banner_charge_25", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_26", 0, "custom_banner_charge_26", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_27", 0, "custom_banner_charge_27", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_28", 0, "custom_banner_charge_28", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_29", 0, "custom_banner_charge_29", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_30", 0, "custom_banner_charge_30", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_31", 0, "custom_banner_charge_31", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_32", 0, "custom_banner_charge_32", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_33", 0, "custom_banner_charge_33", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_34", 0, "custom_banner_charge_34", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_35", 0, "custom_banner_charge_35", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_36", 0, "custom_banner_charge_36", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_37", 0, "custom_banner_charge_37", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_38", 0, "custom_banner_charge_38", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_39", 0, "custom_banner_charge_39", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_40", 0, "custom_banner_charge_40", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_41", 0, "custom_banner_charge_41", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_42", 0, "custom_banner_charge_42", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_43", 0, "custom_banner_charge_43", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_44", 0, "custom_banner_charge_44", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_45", 0, "custom_banner_charge_45", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_46", 0, "custom_banner_charge_46", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner", 0, "tableau_mesh_custom_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_square", 0, "tableau_mesh_custom_banner_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_tall", 0, "tableau_mesh_custom_banner_tall", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_short", 0, "tableau_mesh_custom_banner_short", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_1", 0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_2", 0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_3", 0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_4", 0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_5", 0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_1", 0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_2", 0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_3", 0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_1", 0, "tableau_mesh_shield_kite_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_2", 0, "tableau_mesh_shield_kite_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_3", 0, "tableau_mesh_shield_kite_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_4", 0, "tableau_mesh_shield_kite_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("heraldic_armor_bg", 0, "heraldic_armor_bg", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_d", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("outer_terrain_plain_1", 0, "ter_border_a", -90, 0, 0, 0, 0, 0, 1, 1, 1),

	("banner_a01", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a02", 0, "banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a03", 0, "banner_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a04", 0, "banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a06", 0, "banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a08", 0, "banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a12", 0, "banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a13", 0, "banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a16", 0, "banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a17", 0, "banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a18", 0, "banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a19", 0, "banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a20", 0, "banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a21", 0, "banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b01", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b02", 0, "banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b05", 0, "banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b06", 0, "banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b07", 0, "banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b08", 0, "banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b09", 0, "banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b10", 0, "banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b14", 0, "banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b15", 0, "banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b16", 0, "banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b18", 0, "banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b20", 0, "banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c01", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c04", 0, "banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c06", 0, "banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c07", 0, "banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c10", 0, "banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c12", 0, "banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c13", 0, "banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c14", 0, "banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c16", 0, "banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c19", 0, "banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d02", 0, "banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d03", 0, "banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d04", 0, "banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d06", 0, "banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d07", 0, "banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d08", 0, "banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d09", 0, "banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d11", 0, "banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d12", 0, "banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d13", 0, "banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d14", 0, "banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d15", 0, "banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d16", 0, "banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d17", 0, "banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d18", 0, "banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d19", 0, "banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d20", 0, "banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d21", 0, "banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f21", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g01", 0, "banner_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g02", 0, "banner_g02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g03", 0, "banner_g03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g04", 0, "banner_g04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g05", 0, "banner_g05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g06", 0, "banner_g06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g07", 0, "banner_g07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g08", 0, "banner_g08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g09", 0, "banner_g09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g10", 0, "banner_g10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g11", 0, "banner_g11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g12", 0, "banner_g12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g13", 0, "banner_g13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g14", 0, "banner_g14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g15", 0, "banner_g15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g16", 0, "banner_g16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g17", 0, "banner_g17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g18", 0, "banner_g18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g19", 0, "banner_g19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g20", 0, "banner_g20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g21", 0, "banner_g21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h01", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h02", 0, "banner_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h03", 0, "banner_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h04", 0, "banner_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h05", 0, "banner_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h06", 0, "banner_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h07", 0, "banner_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h08", 0, "banner_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h09", 0, "banner_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h10", 0, "banner_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h11", 0, "banner_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h12", 0, "banner_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h13", 0, "banner_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h14", 0, "banner_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h15", 0, "banner_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h16", 0, "banner_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h17", 0, "banner_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h18", 0, "banner_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h19", 0, "banner_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h20", 0, "banner_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h21", 0, "banner_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i01", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i02", 0, "banner_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i03", 0, "banner_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i04", 0, "banner_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i05", 0, "banner_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i06", 0, "banner_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i07", 0, "banner_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i08", 0, "banner_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i09", 0, "banner_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i10", 0, "banner_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i11", 0, "banner_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i12", 0, "banner_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i13", 0, "banner_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i14", 0, "banner_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i15", 0, "banner_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i16", 0, "banner_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i17", 0, "banner_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i18", 0, "banner_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i19", 0, "banner_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i20", 0, "banner_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i21", 0, "banner_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j01", 0, "banner_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j02", 0, "banner_j02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j03", 0, "banner_j03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j04", 0, "banner_j04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j05", 0, "banner_j05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j06", 0, "banner_j06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j07", 0, "banner_j07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j08", 0, "banner_j08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j09", 0, "banner_j09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j10", 0, "banner_j10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j11", 0, "banner_j11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j12", 0, "banner_j12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j13", 0, "banner_j13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j14", 0, "banner_j14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j15", 0, "banner_j15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j16", 0, "banner_j16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j17", 0, "banner_j17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j18", 0, "banner_j18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j19", 0, "banner_j19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j20", 0, "banner_j20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j21", 0, "banner_j21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k01", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k02", 0, "banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k03", 0, "banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k04", 0, "banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k05", 0, "banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k06", 0, "banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k07", 0, "banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k08", 0, "banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k09", 0, "banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k10", 0, "banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k11", 0, "banner_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k12", 0, "banner_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k13", 0, "banner_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k14", 0, "banner_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k15", 0, "banner_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k16", 0, "banner_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k17", 0, "banner_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k18", 0, "banner_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k19", 0, "banner_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k20", 0, "banner_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k21", 0, "banner_k21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l01", 0, "banner_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l02", 0, "banner_l02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l03", 0, "banner_l03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l04", 0, "banner_l04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l05", 0, "banner_l05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l06", 0, "banner_l06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l07", 0, "banner_l07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l08", 0, "banner_l08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l09", 0, "banner_l09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l10", 0, "banner_l10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l11", 0, "banner_l11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l12", 0, "banner_l12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l13", 0, "banner_l13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l14", 0, "banner_l14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l15", 0, "banner_l15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l16", 0, "banner_l16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l17", 0, "banner_l17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l18", 0, "banner_l18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l19", 0, "banner_l19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l20", 0, "banner_l20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l21", 0, "banner_l21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m01", 0, "banner_m01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m02", 0, "banner_m02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m03", 0, "banner_m03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m04", 0, "banner_m04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m05", 0, "banner_m05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m06", 0, "banner_m06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m07", 0, "banner_m07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m08", 0, "banner_m08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m09", 0, "banner_m09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m10", 0, "banner_m10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m11", 0, "banner_m11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m12", 0, "banner_m12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m13", 0, "banner_m13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m14", 0, "banner_m14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m15", 0, "banner_m15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m16", 0, "banner_m16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m17", 0, "banner_m17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m18", 0, "banner_m18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m19", 0, "banner_m19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m20", 0, "banner_m20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_m21", 0, "banner_m21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n01", 0, "banner_n01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n02", 0, "banner_n02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n03", 0, "banner_n03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n04", 0, "banner_n04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n05", 0, "banner_n05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n06", 0, "banner_n06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n07", 0, "banner_n07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n08", 0, "banner_n08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n09", 0, "banner_n09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n10", 0, "banner_n10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n11", 0, "banner_n11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n12", 0, "banner_n12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n13", 0, "banner_n13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n14", 0, "banner_n14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n15", 0, "banner_n15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n16", 0, "banner_n16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n17", 0, "banner_n17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n18", 0, "banner_n18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n19", 0, "banner_n19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n20", 0, "banner_n20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_n21", 0, "banner_n21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o01", 0, "banner_o01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o02", 0, "banner_o02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o03", 0, "banner_o03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o04", 0, "banner_o04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o05", 0, "banner_o05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o06", 0, "banner_o06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o07", 0, "banner_o07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o08", 0, "banner_o08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o09", 0, "banner_o09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o10", 0, "banner_o10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o11", 0, "banner_o11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o12", 0, "banner_o12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o13", 0, "banner_o13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o14", 0, "banner_o14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o15", 0, "banner_o15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o16", 0, "banner_o16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o17", 0, "banner_o17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o18", 0, "banner_o18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o19", 0, "banner_o19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o20", 0, "banner_o20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_o21", 0, "banner_o21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p01", 0, "banner_p01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p02", 0, "banner_p02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p03", 0, "banner_p03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p04", 0, "banner_p04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p05", 0, "banner_p05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p06", 0, "banner_p06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p07", 0, "banner_p07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p08", 0, "banner_p08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p09", 0, "banner_p09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p10", 0, "banner_p10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p11", 0, "banner_p11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p12", 0, "banner_p12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p13", 0, "banner_p13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p14", 0, "banner_p14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p15", 0, "banner_p15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p16", 0, "banner_p16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p17", 0, "banner_p17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p18", 0, "banner_p18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p19", 0, "banner_p19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p20", 0, "banner_p20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_p21", 0, "banner_p21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q01", 0, "banner_q01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q02", 0, "banner_q02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q03", 0, "banner_q03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q04", 0, "banner_q04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q05", 0, "banner_q05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q06", 0, "banner_q06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q07", 0, "banner_q07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q08", 0, "banner_q08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q09", 0, "banner_q09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q10", 0, "banner_q10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q11", 0, "banner_q11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q12", 0, "banner_q12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q13", 0, "banner_q13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q14", 0, "banner_q14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q15", 0, "banner_q15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q16", 0, "banner_q16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q17", 0, "banner_q17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q18", 0, "banner_q18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q19", 0, "banner_q19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q20", 0, "banner_q20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_q21", 0, "banner_q21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r01", 0, "banner_r01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r02", 0, "banner_r02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r03", 0, "banner_r03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r04", 0, "banner_r04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r05", 0, "banner_r05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r06", 0, "banner_r06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r07", 0, "banner_r07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r08", 0, "banner_r08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r09", 0, "banner_r09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r10", 0, "banner_r10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r11", 0, "banner_r11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r12", 0, "banner_r12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r13", 0, "banner_r13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r14", 0, "banner_r14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r15", 0, "banner_r15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r16", 0, "banner_r16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r17", 0, "banner_r17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r18", 0, "banner_r18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r19", 0, "banner_r19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r20", 0, "banner_r20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_r21", 0, "banner_r21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s01", 0, "banner_s01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s02", 0, "banner_s02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s03", 0, "banner_s03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s04", 0, "banner_s04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s05", 0, "banner_s05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s06", 0, "banner_s06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s07", 0, "banner_s07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s08", 0, "banner_s08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s09", 0, "banner_s09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s10", 0, "banner_s10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s11", 0, "banner_s11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s12", 0, "banner_s12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s13", 0, "banner_s13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s14", 0, "banner_s14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s15", 0, "banner_s15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s16", 0, "banner_s16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s17", 0, "banner_s17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s18", 0, "banner_s18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s19", 0, "banner_s19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s20", 0, "banner_s20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_s21", 0, "banner_s21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t01", 0, "banner_t01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t02", 0, "banner_t02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t03", 0, "banner_t03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t04", 0, "banner_t04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t05", 0, "banner_t05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t06", 0, "banner_t06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t07", 0, "banner_t07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t08", 0, "banner_t08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t09", 0, "banner_t09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t10", 0, "banner_t10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t11", 0, "banner_t11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t12", 0, "banner_t12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t13", 0, "banner_t13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t14", 0, "banner_t14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t15", 0, "banner_t15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t16", 0, "banner_t16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t17", 0, "banner_t17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t18", 0, "banner_t18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t19", 0, "banner_t19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t20", 0, "banner_t20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_t21", 0, "banner_t21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u01", 0, "banner_u01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u02", 0, "banner_u02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u03", 0, "banner_u03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u04", 0, "banner_u04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u05", 0, "banner_u05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u06", 0, "banner_u06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u07", 0, "banner_u07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u08", 0, "banner_u08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u09", 0, "banner_u09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u10", 0, "banner_u10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u11", 0, "banner_u11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u12", 0, "banner_u12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u13", 0, "banner_u13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u14", 0, "banner_u14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u15", 0, "banner_u15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u16", 0, "banner_u16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u17", 0, "banner_u17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u18", 0, "banner_u18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u19", 0, "banner_u19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u20", 0, "banner_u20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_u21", 0, "banner_u21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v01", 0, "banner_v01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v02", 0, "banner_v02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v03", 0, "banner_v03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v04", 0, "banner_v04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v05", 0, "banner_v05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v06", 0, "banner_v06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v07", 0, "banner_v07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v08", 0, "banner_v08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v09", 0, "banner_v09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v10", 0, "banner_v10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v11", 0, "banner_v11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v12", 0, "banner_v12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v13", 0, "banner_v13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v14", 0, "banner_v14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v15", 0, "banner_v15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v16", 0, "banner_v16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v17", 0, "banner_v17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v18", 0, "banner_v18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v19", 0, "banner_v19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v20", 0, "banner_v20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_v21", 0, "banner_v21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x01", 0, "banner_x01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x02", 0, "banner_x02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x03", 0, "banner_x03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x04", 0, "banner_x04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x05", 0, "banner_x05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x06", 0, "banner_x06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x07", 0, "banner_x07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x08", 0, "banner_x08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x09", 0, "banner_x09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x10", 0, "banner_x10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x11", 0, "banner_x11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x12", 0, "banner_x12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x13", 0, "banner_x13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x14", 0, "banner_x14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x15", 0, "banner_x15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x16", 0, "banner_x16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x17", 0, "banner_x17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x18", 0, "banner_x18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x19", 0, "banner_x19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x20", 0, "banner_x20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_x21", 0, "banner_x21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_1", 0, "banner_q01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_2", 0, "banner_p01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_3", 0, "banner_n01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_4", 0, "banner_m01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_5", 0, "banner_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_6", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_7", 0, "banner_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_8", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_9", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_10", 0, "banner_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_11", 0, "banner_r01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_12", 0, "banner_s01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_13", 0, "banner_t01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_14", 0, "banner_u01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_15", 0, "banner_v01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_16", 0, "banner_x01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_17", 0, "banner_x02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_18", 0, "banner_x03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_19", 0, "banner_x04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_20", 0, "banner_x05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_22", 0, "banner_x07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_23", 0, "banner_x08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_24", 0, "banner_x09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_25", 0, "banner_x10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_26", 0, "banner_x11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_27", 0, "banner_x12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_28", 0, "banner_x13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_29", 0, "banner_x15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_30", 0, "banner_x16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_31", 0, "banner_x17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_32", 0, "banner_x06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_21", 0, "banner_x06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a01", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a02", 0, "banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a03", 0, "banner_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a04", 0, "banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a06", 0, "banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a08", 0, "banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a12", 0, "banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a13", 0, "banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a16", 0, "banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a17", 0, "banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a18", 0, "banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a19", 0, "banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a20", 0, "banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a21", 0, "banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b01", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b02", 0, "banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b05", 0, "banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b06", 0, "banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b07", 0, "banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b08", 0, "banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b09", 0, "banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b10", 0, "banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b14", 0, "banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b15", 0, "banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b16", 0, "banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b18", 0, "banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b20", 0, "banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c01", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c04", 0, "banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c06", 0, "banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c07", 0, "banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c10", 0, "banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c12", 0, "banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c13", 0, "banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c14", 0, "banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c16", 0, "banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c19", 0, "banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d02", 0, "banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d03", 0, "banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d04", 0, "banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d06", 0, "banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d07", 0, "banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d08", 0, "banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d09", 0, "banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d11", 0, "banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d12", 0, "banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d13", 0, "banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d14", 0, "banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d15", 0, "banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d16", 0, "banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d17", 0, "banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d18", 0, "banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d19", 0, "banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d20", 0, "banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d21", 0, "banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f21", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g01", 0, "banner_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g02", 0, "banner_g02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g03", 0, "banner_g03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g04", 0, "banner_g04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g05", 0, "banner_g05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g06", 0, "banner_g06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g07", 0, "banner_g07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g08", 0, "banner_g08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g09", 0, "banner_g09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g10", 0, "banner_g10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g11", 0, "banner_g11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g12", 0, "banner_g12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g13", 0, "banner_g13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g14", 0, "banner_g14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g15", 0, "banner_g15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g16", 0, "banner_g16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g17", 0, "banner_g17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g18", 0, "banner_g18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g19", 0, "banner_g19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g20", 0, "banner_g20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g21", 0, "banner_g21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h01", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h02", 0, "banner_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h03", 0, "banner_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h04", 0, "banner_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h05", 0, "banner_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h06", 0, "banner_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h07", 0, "banner_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h08", 0, "banner_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h09", 0, "banner_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h10", 0, "banner_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h11", 0, "banner_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h12", 0, "banner_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h13", 0, "banner_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h14", 0, "banner_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h15", 0, "banner_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h16", 0, "banner_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h17", 0, "banner_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h18", 0, "banner_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h19", 0, "banner_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h20", 0, "banner_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h21", 0, "banner_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i01", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i02", 0, "banner_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i03", 0, "banner_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i04", 0, "banner_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i05", 0, "banner_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i06", 0, "banner_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i07", 0, "banner_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i08", 0, "banner_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i09", 0, "banner_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i10", 0, "banner_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i11", 0, "banner_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i12", 0, "banner_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i13", 0, "banner_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i14", 0, "banner_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i15", 0, "banner_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i16", 0, "banner_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i17", 0, "banner_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i18", 0, "banner_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i19", 0, "banner_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i20", 0, "banner_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i21", 0, "banner_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j01", 0, "banner_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j02", 0, "banner_j02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j03", 0, "banner_j03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j04", 0, "banner_j04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j05", 0, "banner_j05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j06", 0, "banner_j06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j07", 0, "banner_j07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j08", 0, "banner_j08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j09", 0, "banner_j09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j10", 0, "banner_j10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j11", 0, "banner_j11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j12", 0, "banner_j12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j13", 0, "banner_j13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j14", 0, "banner_j14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j15", 0, "banner_j15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j16", 0, "banner_j16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j17", 0, "banner_j17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j18", 0, "banner_j18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j19", 0, "banner_j19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j20", 0, "banner_j20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j21", 0, "banner_j21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k01", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k02", 0, "banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k03", 0, "banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k04", 0, "banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k05", 0, "banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k06", 0, "banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k07", 0, "banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k08", 0, "banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k09", 0, "banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k10", 0, "banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k11", 0, "banner_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k12", 0, "banner_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k13", 0, "banner_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k14", 0, "banner_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k15", 0, "banner_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k16", 0, "banner_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k17", 0, "banner_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k18", 0, "banner_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k19", 0, "banner_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k20", 0, "banner_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k21", 0, "banner_k21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l01", 0, "banner_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l02", 0, "banner_l02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l03", 0, "banner_l03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l04", 0, "banner_l04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l05", 0, "banner_l05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l06", 0, "banner_l06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l07", 0, "banner_l07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l08", 0, "banner_l08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l09", 0, "banner_l09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l10", 0, "banner_l10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l11", 0, "banner_l11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l12", 0, "banner_l12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l13", 0, "banner_l13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l14", 0, "banner_l14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l15", 0, "banner_l15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l16", 0, "banner_l16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l17", 0, "banner_l17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l18", 0, "banner_l18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l19", 0, "banner_l19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l20", 0, "banner_l20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l21", 0, "banner_l21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m01", 0, "banner_m01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m02", 0, "banner_m02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m03", 0, "banner_m03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m04", 0, "banner_m04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m05", 0, "banner_m05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m06", 0, "banner_m06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m07", 0, "banner_m07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m08", 0, "banner_m08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m09", 0, "banner_m09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m10", 0, "banner_m10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m11", 0, "banner_m11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m12", 0, "banner_m12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m13", 0, "banner_m13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m14", 0, "banner_m14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m15", 0, "banner_m15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m16", 0, "banner_m16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m17", 0, "banner_m17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m18", 0, "banner_m18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m19", 0, "banner_m19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m20", 0, "banner_m20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_m21", 0, "banner_m21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n01", 0, "banner_n01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n02", 0, "banner_n02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n03", 0, "banner_n03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n04", 0, "banner_n04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n05", 0, "banner_n05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n06", 0, "banner_n06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n07", 0, "banner_n07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n08", 0, "banner_n08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n09", 0, "banner_n09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n10", 0, "banner_n10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n11", 0, "banner_n11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n12", 0, "banner_n12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n13", 0, "banner_n13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n14", 0, "banner_n14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n15", 0, "banner_n15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n16", 0, "banner_n16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n17", 0, "banner_n17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n18", 0, "banner_n18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n19", 0, "banner_n19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n20", 0, "banner_n20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_n21", 0, "banner_n21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o01", 0, "banner_o01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o02", 0, "banner_o02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o03", 0, "banner_o03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o04", 0, "banner_o04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o05", 0, "banner_o05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o06", 0, "banner_o06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o07", 0, "banner_o07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o08", 0, "banner_o08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o09", 0, "banner_o09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o10", 0, "banner_o10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o11", 0, "banner_o11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o12", 0, "banner_o12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o13", 0, "banner_o13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o14", 0, "banner_o14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o15", 0, "banner_o15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o16", 0, "banner_o16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o17", 0, "banner_o17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o18", 0, "banner_o18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o19", 0, "banner_o19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o20", 0, "banner_o20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_o21", 0, "banner_o21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p01", 0, "banner_p01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p02", 0, "banner_p02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p03", 0, "banner_p03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p04", 0, "banner_p04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p05", 0, "banner_p05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p06", 0, "banner_p06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p07", 0, "banner_p07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p08", 0, "banner_p08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p09", 0, "banner_p09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p10", 0, "banner_p10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p11", 0, "banner_p11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p12", 0, "banner_p12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p13", 0, "banner_p13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p14", 0, "banner_p14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p15", 0, "banner_p15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p16", 0, "banner_p16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p17", 0, "banner_p17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p18", 0, "banner_p18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p19", 0, "banner_p19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p20", 0, "banner_p20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_p21", 0, "banner_p21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q01", 0, "banner_q01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q02", 0, "banner_q02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q03", 0, "banner_q03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q04", 0, "banner_q04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q05", 0, "banner_q05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q06", 0, "banner_q06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q07", 0, "banner_q07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q08", 0, "banner_q08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q09", 0, "banner_q09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q10", 0, "banner_q10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q11", 0, "banner_q11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q12", 0, "banner_q12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q13", 0, "banner_q13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q14", 0, "banner_q14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q15", 0, "banner_q15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q16", 0, "banner_q16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q17", 0, "banner_q17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q18", 0, "banner_q18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q19", 0, "banner_q19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q20", 0, "banner_q20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_q21", 0, "banner_q21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r01", 0, "banner_r01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r02", 0, "banner_r02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r03", 0, "banner_r03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r04", 0, "banner_r04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r05", 0, "banner_r05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r06", 0, "banner_r06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r07", 0, "banner_r07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r08", 0, "banner_r08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r09", 0, "banner_r09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r10", 0, "banner_r10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r11", 0, "banner_r11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r12", 0, "banner_r12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r13", 0, "banner_r13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r14", 0, "banner_r14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r15", 0, "banner_r15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r16", 0, "banner_r16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r17", 0, "banner_r17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r18", 0, "banner_r18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r19", 0, "banner_r19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r20", 0, "banner_r20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_r21", 0, "banner_r21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s01", 0, "banner_s01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s02", 0, "banner_s02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s03", 0, "banner_s03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s04", 0, "banner_s04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s05", 0, "banner_s05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s06", 0, "banner_s06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s07", 0, "banner_s07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s08", 0, "banner_s08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s09", 0, "banner_s09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s10", 0, "banner_s10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s11", 0, "banner_s11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s12", 0, "banner_s12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s13", 0, "banner_s13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s14", 0, "banner_s14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s15", 0, "banner_s15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s16", 0, "banner_s16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s17", 0, "banner_s17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s18", 0, "banner_s18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s19", 0, "banner_s19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s20", 0, "banner_s20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_s21", 0, "banner_s21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t01", 0, "banner_t01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t02", 0, "banner_t02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t03", 0, "banner_t03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t04", 0, "banner_t04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t05", 0, "banner_t05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t06", 0, "banner_t06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t07", 0, "banner_t07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t08", 0, "banner_t08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t09", 0, "banner_t09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t10", 0, "banner_t10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t11", 0, "banner_t11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t12", 0, "banner_t12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t13", 0, "banner_t13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t14", 0, "banner_t14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t15", 0, "banner_t15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t16", 0, "banner_t16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t17", 0, "banner_t17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t18", 0, "banner_t18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t19", 0, "banner_t19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t20", 0, "banner_t20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_t21", 0, "banner_t21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u01", 0, "banner_u01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u02", 0, "banner_u02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u03", 0, "banner_u03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u04", 0, "banner_u04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u05", 0, "banner_u05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u06", 0, "banner_u06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u07", 0, "banner_u07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u08", 0, "banner_u08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u09", 0, "banner_u09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u10", 0, "banner_u10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u11", 0, "banner_u11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u12", 0, "banner_u12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u13", 0, "banner_u13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u14", 0, "banner_u14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u15", 0, "banner_u15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u16", 0, "banner_u16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u17", 0, "banner_u17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u18", 0, "banner_u18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u19", 0, "banner_u19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u20", 0, "banner_u20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_u21", 0, "banner_u21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v01", 0, "banner_v01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v02", 0, "banner_v02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v03", 0, "banner_v03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v04", 0, "banner_v04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v05", 0, "banner_v05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v06", 0, "banner_v06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v07", 0, "banner_v07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v08", 0, "banner_v08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v09", 0, "banner_v09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v10", 0, "banner_v10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v11", 0, "banner_v11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v12", 0, "banner_v12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v13", 0, "banner_v13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v14", 0, "banner_v14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v15", 0, "banner_v15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v16", 0, "banner_v16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v17", 0, "banner_v17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v18", 0, "banner_v18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v19", 0, "banner_v19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v20", 0, "banner_v20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_v21", 0, "banner_v21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x01", 0, "banner_x01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x02", 0, "banner_x02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x03", 0, "banner_x03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x04", 0, "banner_x04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x05", 0, "banner_x05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x06", 0, "banner_x06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x07", 0, "banner_x07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x08", 0, "banner_x08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x09", 0, "banner_x09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x10", 0, "banner_x10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x11", 0, "banner_x11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x12", 0, "banner_x12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x13", 0, "banner_x13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x14", 0, "banner_x14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x15", 0, "banner_x15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x16", 0, "banner_x16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x17", 0, "banner_x17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x18", 0, "banner_x18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x19", 0, "banner_x19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x20", 0, "banner_x20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_x21", 0, "banner_x21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_1", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_2", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_3", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_4", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_5", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_6", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_7", 0, "banner_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_8", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_9", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_10", 0, "banner_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_11", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_12", 0, "banner_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_13", 0, "banner_m01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_14", 0, "banner_n01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_15", 0, "banner_v01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_16", 0, "banner_x01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_17", 0, "banner_x02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_18", 0, "banner_x03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_19", 0, "banner_x04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_20", 0, "banner_x05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_21", 0, "banner_x06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_22", 0, "banner_x07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_23", 0, "banner_x08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_24", 0, "banner_x09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_25", 0, "banner_x10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_26", 0, "banner_x11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_27", 0, "banner_x12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_28", 0, "banner_x13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_29", 0, "banner_x15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_30", 0, "banner_x16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("troop_label_banner", 0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("ui_kingdom_shield_1", 0, "ui_kingdom_shield_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_2", 0, "ui_kingdom_shield_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_3", 0, "ui_kingdom_shield_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_4", 0, "ui_kingdom_shield_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_5", 0, "ui_kingdom_shield_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_6", 0, "ui_kingdom_shield_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_down", 0, "mouse_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_right", 0, "mouse_arrow_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_left", 0, "mouse_arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_up", 0, "mouse_arrow_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_plus", 0, "mouse_arrow_plus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_left_click", 0, "mouse_left_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_right_click", 0, "mouse_right_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("status_ammo_ready", 0, "status_ammo_ready", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_quick_battle_a", 0, "ui_quick_battle_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_bg_plane_a", 0, "white_bg_plane_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_infantry", 0, "cb_ui_icon_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_archer", 0, "cb_ui_icon_archer", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_horseman", 0, "cb_ui_icon_horseman", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_01", 0, "cb_ui_maps_scene_01", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_02", 0, "cb_ui_maps_scene_02", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_03", 0, "cb_ui_maps_scene_03", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_04", 0, "cb_ui_maps_scene_04", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_05", 0, "cb_ui_maps_scene_05", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_06", 0, "cb_ui_maps_scene_06", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_07", 0, "cb_ui_maps_scene_07", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_08", 0, "cb_ui_maps_scene_08", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_09", 0, "cb_ui_maps_scene_09", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_14", 0, "mp_ui_host_maps_c4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_15", 0, "mp_ui_host_maps_c5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("quit_adv", 0, "quit_adv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("quit_adv_b", 0, "quit_adv_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_7", 0, "ui_kingdom_shield_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rb", 0, "flag_project_rb", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rb_miss", 0, "flag_project_rb_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_16", 0, "mp_ui_host_maps_d1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_17", 0, "mp_ui_host_maps_d2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_18", 0, "mp_ui_host_maps_d3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_19", 0, "mp_ui_host_maps_e2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_20", 0, "mp_ui_host_maps_e1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("longer_button", 0, "longer_button", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("longer_button_down", 0, "longer_button_down", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("options_window", 0, "options_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("note_window", 0, "note_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("drop_button", 0, "button_drop", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_down", 0, "button_drop_clicked", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_hl", 0, "button_drop_hl", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child", 0, "button_drop_child", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child_down", 0, "button_drop_child_clicked", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child_hl", 0, "button_drop_child_hl", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("pic_troops_arab", 0, "pic_troops_arab", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_balt", 0, "pic_troops_balt", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_byzantine", 0, "pic_troops_byzantine", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_cuman", 0, "pic_troops_cuman", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_eastern", 0, "pic_troops_eastern", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_european", 0, "pic_troops_european", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_hospitaller", 0, "pic_troops_hospitaller", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_mercenary", 0, "pic_troops_mercenary", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_mongol", 0, "pic_troops_mongol", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_nordic", 0, "pic_troops_nordic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_troops_templar", 0, "pic_troops_templar", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_lance", 0, "tableau_mesh_heraldic_lance", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_iberia", 0, "tableau_mesh_shield_iberia", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_flag_pole", 0, "tableau_mesh_flag_pole", 0, 0, 0, 0, 0, 0, 5, 5, 5),

	("tableau_mesh_shield_kite_byz", 0, "tableau_mesh_shield_kite_byz", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("pic_soldier_world_map", 0, "pic_siege_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_soldier_rebel", 0, "pic_siege_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_soldier_desert", 0, "pic_siege_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_manor", 0, "pic_manor", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("order_frame", 0, "order_frame", 0, 0, 0, 0, 0, 0, 1, 1, 1),

]