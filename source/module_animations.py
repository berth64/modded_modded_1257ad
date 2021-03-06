from header_common import *
from header_animations import *

####################################################################################################################
#  There are two animation arrays (one for human and one for horse). Each animation in these arrays contains the following fields:
#  1) Animation id (string): used for referencing animations in other files. The prefix anim_ is automatically added before each animation-id .
#  2) Animation flags: could be anything beginning with acf_ defined in header_animations.py
#  3) Animation master flags: could be anything beginning with amf_ defined in header_animations.py
#  4) Animation sequences (list).
#  4.1) Duration of the sequence.
#  4.2) Name of the animation resource.
#  4.3) Beginning frame of the sequence within the animation resource.
#  4.4) Ending frame of the sequence within the animation resource.
#  4.5) Sequence flags: could be anything beginning with arf_ defined in header_animations.py
# 
####################################################################################################################

#plan : 
# basic movement : walk ride etc. 0 -20000
#  on_foot  : 0     - 10000
#  horse    : 10000 - 20000
# combat         :                20000 - 40000
# fall           :                4000 - 70000
# act            : misc.          70000 - ...

amf_priority_jump           = 2
amf_priority_ride           = 2
amf_priority_continue       = 1
amf_priority_attack         = 10
amf_priority_cancel         = 12
amf_priority_defend         = 14
amf_priority_defend_parry   = amf_priority_defend + 1
amf_priority_throw          = amf_priority_defend + 1
amf_priority_blocked        = amf_priority_defend_parry
amf_priority_parried        = amf_priority_defend_parry
amf_priority_kick           = 33
amf_priority_jump_end       = 33
amf_priority_reload         = 60
amf_priority_mount          = 64
amf_priority_equip          = 70
amf_priority_rear           = 74
amf_priority_striked        = 80
amf_priority_fall_from_horse= 81
amf_priority_die            = 95



horse_move = 10000
combat     = 20000
defend     = 35000
blow       = 40000

attack_parried_duration = 0.6
attack_blocked_duration = 0.3
attack_blocked_duration_thrust = attack_blocked_duration + 0.3
attack_parried_duration_thrust = attack_parried_duration + 0.1
defend_parry_duration_1 = 0.6
defend_parry_duration_2 = 0.6
defend_parry_duration_3 = 0.8
ready_durn     = 0.35
defend_duration = 0.75
defend_keep_duration = 2.0
cancel_duration = 0.25

blend_in_defense = arf_blend_in_3
blend_in_ready = arf_blend_in_6
blend_in_release = arf_blend_in_5
blend_in_parry = arf_blend_in_5
blend_in_parried = arf_blend_in_3


blend_in_walk = arf_blend_in_3
blend_in_continue = arf_blend_in_1

#### Animations begin here

# All of the animations are hardcoded. You can edit the individual sequences, resources or times. But each
# animation must stay at the same position, otherwise the game won't run properly. If you want to add a new animation,
# you can change both the ids and values of the animations which are named as unused_human_anim_???
# and unused_horse_anim_??? (??? = any number). You must not change used animations' ids.

animations = [
	["stand", 0, amf_client_prediction,
		[3.0, "anim_human", 50, 52, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25],
		[3.0, "anim_human", 60, 62, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.75],
		[3.0, "anim_human", 70, 72, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25],
		[3.0, "anim_human", 80, 82, arf_two_handed_blade|arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.5]
	],

	["stand_man", 0, amf_client_prediction,
		[11.0, "stand_man", 0, 315, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["stand_player_first_person", 0, amf_client_prediction,
		[3.5, "anim_human", 90, 100, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25],
		[3.5, "anim_human", 110, 120, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["jump", acf_enforce_lowerbody, amf_priority_jump|amf_priority_ride|amf_client_prediction|amf_play|amf_continue_to_next,
		[1.0, "jump", 22, 46, arf_blend_in_1]
	],

	["jump_loop", acf_enforce_lowerbody, amf_priority_jump|amf_priority_ride|amf_client_prediction|amf_play,
		[0.5, "jump_loop", 0, 14, arf_blend_in_3|arf_cyclic]
	],

	["jump_end", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[0.3, "jump", 48, 55, arf_blend_in_2]
	],

	["jump_end_hard", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[0.6, "jump_end_hard", 36, 54, arf_blend_in_1]
	],

	["stand_unarmed", 0, amf_client_prediction,
		[8.0, "noweapon_cstance", 0, 100, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["stand_single", 0, amf_client_prediction,
		[9.0, "sword_loop01", 0, 200, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["stand_greatsword", 0, amf_client_prediction,
		[6.0, "greatsword_cstance", 0, 91, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["stand_staff", 0, amf_client_prediction,
		[2.0, "staff_cstance", 0, 60, arf_cyclic|arf_use_stand_progress]
	],

	["stand_crossbow", 0, amf_client_prediction,
		[2.0, "staff_cstance", 0, 60, arf_cyclic|arf_use_stand_progress]
	],

	["turn_right", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "stand_man", 0, 30, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["turn_left", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "stand_man", 0, 30, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["turn_right_single", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "turn_man_onehanded", 0, 23, arf_blend_in_3|arf_make_walk_sound|arf_cyclic, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["turn_left_single", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "turn_man_onehanded", 30, 53, arf_blend_in_3|arf_make_walk_sound|arf_cyclic, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["turn_right_staff", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "turn_man_staff", 0, 20, arf_blend_in_3|arf_make_walk_sound|arf_cyclic, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["turn_left_staff", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "turn_man_staff", 30, 50, arf_blend_in_3|arf_make_walk_sound|arf_cyclic, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["turn_right_greatsword", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "turn_man_greatsword", 0, 20, arf_blend_in_3|arf_make_walk_sound|arf_cyclic, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["turn_left_greatsword", acf_enforce_lowerbody, amf_client_prediction|amf_play,
		[0.95, "turn_man_greatsword", 30, 50, arf_blend_in_3|arf_make_walk_sound|arf_cyclic, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["prepare_kick_0", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play|amf_continue_to_next,
		[0.05, "kick_rightleg", 10, 12, arf_blend_in_3]
	],

	["prepare_kick_1", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play|amf_continue_to_next,
		[0.05, "kick_rightleg", 12, 12, arf_blend_in_3]
	],

	["prepare_kick_2", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play|amf_continue_to_next,
		[0.05, "kick_rightleg", 12, 12, arf_blend_in_3]
	],

	["prepare_kick_3", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_play|amf_continue_to_next,
		[0.05, "kick_rightleg", 12, 12, arf_blend_in_3]
	],

	["kick_right_leg", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_play,
		[0.7, "kick_rightleg", 12, 33, arf_blend_in_1]
	],

	["kick_left_leg", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[0.7, "kick_rightleg", 12, 33, arf_blend_in_1]
	],

	["run_forward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_onehanded", 0, 24, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_staff", 0, 24, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_greatsword", 0, 24, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_hips_right", 0, 22, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_hips_left", 0, 22, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_right", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_right_onehanded", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_right_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_right_stuff", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_right_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_right_greatsword", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_right_hips_right", 0, 22, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_right_hips_left", 0, 19, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_left", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_left_onehanded", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_left_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_left_stuff", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_left_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_forward_left_greatsword", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.6, "run_forward_left_hips_right", 0, 19, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_forward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_forward_left_hips_left", 0, 22, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_staff", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_twohanded", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_hips_right", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_hips_left", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_right", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_right", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_right_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_staff_right", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_right_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_twohanded_right", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_right_hips_right", 0, 19, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_right_hips_left", 0, 22, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_left", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_left", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_left_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_staff_left", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_left_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_twohanded_left", 0, 21, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_left_hips_right", 0, 22, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_backward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.7, "run_backward_left_hips_left", 0, 19, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.4]
	],

	["run_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_right", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_right_onehanded", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_right_greatsword", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_right_stuff", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_right_stuff", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_right_hips_left", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_left", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_left_onehanded", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_left_greatsword", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_left_stuff", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_left_hips_right", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["run_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "run_man_left_stuff", 0, 24, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk_staff", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk_greatsword", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_forward_hips_right", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_forward_hips_left", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward", 0, 30, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk_staff", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "man_walk_greatsword", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward_hips_right", 0, 30, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward_hips_left", 0, 30, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_right_normal", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_right_onehanded_r", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_right_greatsword_r", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_right_staff_r", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_right_staff_r", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_right_hips_left", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_left_normal", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_left_onehanded_r", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_left_greatsword", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_left_staff", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_left_hips_right", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_left_staff", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_normal", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_onehanded", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_greatsword", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_staff", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_forward_right_hips_right", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_forward_right_hips_left", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_normal", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_onehanded", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_greatsword", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_staff", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_forward_left_hips_right", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_forward_left_hips_left", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_normal", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_onehanded", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_greatsword", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossright_staff", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward_left_hips_right", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward_left_hips_left", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_normal", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_onehanded", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_greatsword", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_crossleft_staff", 32, 0, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward_right_hips_right", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_backward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "walk_backward_right_hips_left", 0, 32, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["walk_forward_crouch", acf_enforce_lowerbody, 0,
		[1.7, "low_walk", 0, 48, arf_blend_in_3|arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 58726, (0.0, 0.0, 0.0), 0.0]
	],

	["stand_to_crouch", acf_enforce_lowerbody, 0,
		[1.3, "crouch_down", 0, 50, arf_blend_in_1]
	],

	["crouch_to_stand", acf_enforce_lowerbody, 0,
		[1.0, "crouch_down", 56, 91, arf_blend_in_1]
	],

	["ride_0", acf_enforce_lowerbody, amf_client_prediction,
		[15.0, "stand_onhorse", 0, 456, arf_cyclic]
	],

	["ride_1", acf_synch_with_horse|acf_enforce_lowerbody, amf_client_prediction,
		[1.0, "anim_human_02", 0, 31, arf_cyclic]
	],

	["lancer_ride_1", acf_synch_with_horse|acf_enforce_lowerbody, amf_priority_jump|amf_priority_ride|amf_client_prediction|amf_play,
		[1.0, "lancer_ride1", 0, 31, arf_cyclic]
	],

	["lancer_charge_parried", acf_enforce_lowerbody, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[1.0, "anim_human", 10210, 10220, arf_blend_in_32]
	],

	["ride_2", acf_synch_with_horse|acf_enforce_lowerbody, amf_client_prediction,
		[0.8, "anim_human_02", 50, 69, arf_cyclic]
	],

	["ride_3", acf_synch_with_horse|acf_enforce_lowerbody, amf_client_prediction,
		[0.6, "anim_human_02", 100, 116, arf_cyclic]
	],

	["ride_4", acf_synch_with_horse|acf_enforce_lowerbody, amf_client_prediction,
		[0.5, "anim_human_02", 150, 165, arf_blend_in_32|arf_cyclic]
	],

	["lancer_ride_4", acf_synch_with_horse|acf_enforce_lowerbody|acf_rot_vertical_sword|acf_anim_length(30), amf_priority_jump|amf_priority_ride|amf_rider_rot_couched_lance|amf_client_prediction|amf_play,
		[0.5, "lancer_ride4", 0, 15, arf_blend_in_128|arf_cyclic]
	],

	["lancer_ride_4_no_shield", acf_synch_with_horse|acf_enforce_lowerbody|acf_rot_vertical_sword|acf_anim_length(30), amf_priority_jump|amf_priority_ride|amf_rider_rot_couched_lance|amf_client_prediction|amf_play,
		[0.5, "lancer_ride4_no_shield", 0, 15, arf_blend_in_128|arf_cyclic]
	],

	["ride_rear", acf_enforce_lowerbody|acf_ignore_slope, amf_priority_mount|amf_client_prediction|amf_play,
		[1.7, "anim_human_02", 265, 297, arf_blend_in_8]
	],

	["ride_spur", acf_enforce_lowerbody, amf_priority_jump|amf_priority_ride|amf_play,
		[0.3, "anim_human", 10860, 10865, arf_blend_in_8]
	],

	["ride_jump", acf_enforce_lowerbody, amf_client_prediction,
		[1.6, "anim_human_02", 205, 222, arf_blend_in_4]
	],

	["ride_jump_end", acf_enforce_all, amf_client_prediction,
		[0.1, "anim_human_02", 222, 224, arf_blend_in_16]
	],

	["ride_turn_right", acf_synch_with_horse|acf_enforce_lowerbody, amf_client_prediction,
		[1.0, "anim_human_02", 500, 533, arf_cyclic]
	],

	["ride_turn_left", acf_synch_with_horse|acf_enforce_lowerbody, amf_client_prediction,
		[1.0, "anim_human_02", 450, 483, arf_cyclic]
	],

	["mount_horse", acf_enforce_all, amf_priority_mount|amf_client_prediction|amf_play,
		[1.3, "anim_human", 11003, 11045, arf_blend_in_1]
	],

	["dismount_horse", acf_enforce_lowerbody|acf_displace_position, amf_priority_mount|amf_accurate_body|amf_client_prediction|amf_play,
		[1.1, "anim_human", 11103, 11145, arf_blend_in_1, 0, (-0.5, 0.0, 0.0), 0.0]
	],

	["lancer_ride_0", acf_enforce_lowerbody, amf_priority_jump|amf_priority_ride|amf_client_prediction|amf_play,
		[43.0, "stand_onhorse_staff", 0, 1300, arf_lancer|arf_cyclic]
	],

	["equip_default", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.6, "equip_arms", 206, 221, arf_blend_in_0]
	],

	["unequip_default", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_arms", 207, 200, arf_blend_in_0]
	],

	["equip_sword", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_sword", 0, 27, arf_blend_in_0]
	],

	["unequip_sword", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_sword", 6, 0, arf_blend_in_0]
	],

	["equip_greatsword", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[1.2, "draw_greatsword", 0, 35, arf_blend_in_0]
	],

	["unequip_greatsword", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "draw_greatsword", 10, 0, arf_blend_in_0]
	],

	["equip_axe_left_hip", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "draw_axe", 0, 16, arf_blend_in_0]
	],

	["unequip_axe_left_hip", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "draw_axe", 6, 0, arf_blend_in_0]
	],

	["equip_crossbow", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[1.2, "equip_greataxe", 0, 20, arf_blend_in_0]
	],

	["unequip_crossbow", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_greataxe", 10, 0, arf_blend_in_0]
	],

	["equip_spear", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_arms", 17, 34, arf_blend_in_0]
	],

	["unequip_spear", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_arms", 15, 10, arf_blend_in_0]
	],

	["equip_dagger_front_left", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_arms", 253, 276, arf_blend_in_0]
	],

	["unequip_dagger_front_left", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.2, "equip_arms", 254, 250, arf_blend_in_0]
	],

	["equip_dagger_front_right", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_arms", 305, 333, arf_blend_in_0]
	],

	["unequip_dagger_front_right", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.4, "equip_arms", 306, 300, arf_blend_in_0]
	],

	["equip_axe_back", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[1.0, "equip_greataxe", 0, 17, arf_blend_in_0]
	],

	["unequip_axe_back", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_greataxe", 7, 0, arf_blend_in_0]
	],

	["equip_revolver_right", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_granate", 0, 8, arf_blend_in_0]
	],

	["unequip_revolver_right", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_granate", 8, 0, arf_blend_in_0]
	],

	["equip_pistol_front_left", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_arms", 253, 276, arf_blend_in_0]
	],

	["unequip_pistol_front_left", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.2, "equip_arms", 254, 250, arf_blend_in_0]
	],

	["equip_katana", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_sword", 0, 27, arf_blend_in_0]
	],

	["unequip_katana", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_sword", 6, 0, arf_blend_in_0]
	],

	["equip_wakizashi", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_arms", 253, 276, arf_blend_in_0]
	],

	["unequip_wakizashi", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.2, "equip_arms", 254, 250, arf_blend_in_0]
	],

	["equip_shield", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.8, "equip_arms", 68, 84, arf_blend_in_0]
	],

	["unequip_shield", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.4, "equip_arms", 62, 50, arf_blend_in_0]
	],

	["equip_bow_back", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.7, "equip_arms", 161, 179, arf_blend_in_0]
	],

	["unequip_bow_back", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_arms", 163, 150, arf_blend_in_0]
	],

	["equip_bow_left_hip", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.7, "equip_arms", 110, 148, arf_blend_in_0]
	],

	["unequip_bow_left_hip", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_arms", 115, 108, arf_blend_in_0]
	],

	["cancel_attack_onehanded", 0, amf_priority_cancel|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_use_inertia,
		[0.25, "sword_loop01", 10, 11, arf_blend_in_8]
	],

	["cancel_attack_twohanded", 0, amf_priority_cancel|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_use_inertia,
		[0.25, "greatsword_cstance", 10, 11, arf_blend_in_8]
	],

	["cancel_attack_polearm", 0, amf_priority_cancel|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_use_inertia,
		[0.25, "staff_cstance", 10, 11, arf_blend_in_8]
	],

	["ready_bow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_bow|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[1.5, "anim_archery", 16, 133, arf_blend_in_6|arf_make_custom_sound, 28707, (0.0, 0.0, 0.0), 0.0]
	],

	["release_bow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_bow|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "anim_archery", 133, 174, arf_blend_in_2]
	],

	["ready_bow_mounted", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_bow|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[1.5, "anim_human", 20800, 20830, arf_blend_in_6|arf_make_custom_sound, 26137, (0.0, 0.0, 0.0), 0.0]
	],

	["release_bow_mounted", acf_rot_vertical_bow|acf_anim_length(100), amf_rider_rot_bow,
		[0.3, "anim_human", 20830, 20832, arf_blend_in_2]
	],

	["ready_crossbow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_crossbow|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[1.5, "anim_human", 21300, 21320, arf_blend_in_6]
	],

	["release_crossbow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_crossbow|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.2, "anim_human", 21330, 21331, arf_blend_in_1]
	],

	["reload_crossbow", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[1.5, "crossbow_reload_pavise", 0, 158, arf_blend_in_8|arf_make_custom_sound, 26351, (0.0, 0.0, 0.0), 0.0]
	],

	["reload_crossbow_horseback", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[1.6, "anim_human", 21800, 21877, arf_blend_in_8|arf_make_custom_sound, 61252, (0.0, 0.0, 0.0), 0.0]
	],

	["ready_javelin", acf_rot_vertical_bow, amf_priority_attack|amf_rider_rot_throw|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.6, "throw_javelin2", 0, 30, arf_blend_in_6]
	],

	["release_javelin", acf_rot_vertical_bow, amf_priority_defend_parry|amf_rider_rot_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.9, "throw_javelin2", 55, 100, arf_blend_in_0]
	],

	["ready_throwing_knife", acf_rot_vertical_bow, amf_priority_attack|amf_rider_rot_throw|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.6, "throwing_stone", 0, 20, arf_blend_in_6]
	],

	["release_throwing_knife", acf_rot_vertical_bow, amf_priority_defend_parry|amf_rider_rot_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.9, "throwing_stone", 20, 65, arf_blend_in_0]
	],

	["ready_throwing_axe", acf_rot_vertical_bow, amf_priority_attack|amf_rider_rot_throw|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.6, "throwing_axe", 7, 23, arf_blend_in_6]
	],

	["release_throwing_axe", acf_rot_vertical_bow, amf_priority_defend_parry|amf_rider_rot_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.9, "throwing_axe", 23, 60, arf_blend_in_0]
	],

	["ready_stone", acf_rot_vertical_bow, amf_priority_attack|amf_rider_rot_throw|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.5, "throwing_slinge_20_35", 0, 15, arf_blend_in_6|arf_make_custom_sound|arf_cyclic, 28707, (0.0, 0.0, 0.0), 0.0]
	],

	["release_stone", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_pistol|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[2.0, "throwing_slinge", 30, 59, arf_blend_in_0]
	],

	["ready_pistol", acf_rot_vertical_bow, amf_priority_attack|amf_rider_rot_throw|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.5, "throwing_slinge_20_35", 0, 15, arf_blend_in_6|arf_make_custom_sound|arf_cyclic, 28707, (0.0, 0.0, 0.0), 0.0]
	],

	["release_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_pistol|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[2.0, "throwing_slinge", 30, 59, arf_blend_in_0]
	],

	["reload_pistol", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[2.0, "throwing_slinge", 80, 119, arf_blend_in_0]
	],

	["ready_musket", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_crossbow|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.35, "musket_upper_swing_butt", 12, 19, arf_blend_in_6]
	],

	["release_musket", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_crossbow|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.25, "musket_upper_swing_butt", 31, 40, arf_blend_in_5]
	],

	["reload_musket", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[2.0, "rack_and_pinion_reload", 1, 239, arf_blend_in_8|arf_make_custom_sound, 61286, (0.0, 0.0, 0.0), 0.0]
	],

	["ready_swingright_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.35, "right_swing", 0, 15, arf_blend_in_6]
	],

	["release_swingright_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.5, "right_swing", 15, 41, arf_blend_in_5]
	],

	["release_swingright_fist_continue", 0, amf_priority_attack|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.5, "right_swing", 15, 41, arf_blend_in_5]
	],

	["blocked_swingright_fist", 0, amf_priority_defend_parry|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 24013, 24008, arf_blend_in_5]
	],

	["parried_swingright_fist", 0, amf_priority_defend_parry|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 24013, 24008, arf_blend_in_5]
	],

	["ready_swingleft_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.35, "anim_human", 24300, 24300, arf_blend_in_6]
	],

	["release_swingleft_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.5, "anim_human", 24300, 24335, arf_blend_in_5]
	],

	["release_swingleft_fist_continue", 0, amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.5, "anim_human", 24300, 24335, arf_blend_in_5]
	],

	["blocked_swingleft_fist", 0, amf_priority_defend_parry|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 24313, 24308, arf_blend_in_5]
	],

	["parried_swingleft_fist", 0, amf_priority_defend_parry|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 24313, 24308, arf_blend_in_5]
	],

	["ready_direct_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.35, "direct_fist", 0, 16, arf_blend_in_6]
	],

	["release_direct_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.5, "direct_fist", 17, 36, arf_blend_in_5]
	],

	["release_direct_fist_continue", 0, amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.5, "direct_fist", 17, 36, arf_blend_in_5]
	],

	["blocked_direct_fist", 0, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 24613, 24608, arf_blend_in_5]
	],

	["parried_direct_fist", 0, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 24613, 24608, arf_blend_in_5]
	],

	["ready_uppercut_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.35, "uppercut", 0, 17, arf_blend_in_6]
	],

	["release_uppercut_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.5, "uppercut", 17, 34, arf_blend_in_5]
	],

	["release_uppercut_fist_continue", 0, amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.5, "uppercut", 17, 34, arf_blend_in_5]
	],

	["blocked_uppercut_fist", 0, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 24913, 24908, arf_blend_in_5]
	],

	["parried_uppercut_fist", 0, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 24913, 24908, arf_blend_in_5]
	],

	["ready_slashright_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "musket_butt_side", 0, 0, arf_blend_in_6]
	],

	["release_slashright_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.5, "musket_butt_side", 0, 20, arf_blend_in_5]
	],

	["release_slashright_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "musket_butt_side", 20, 30, arf_blend_in_1]
	],

	["blocked_slashright_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "musket_butt_side_stagger", 10, 0, arf_blend_in_2]
	],

	["parried_slashright_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "musket_butt_side_stagger", 10, 0, arf_blend_in_2]
	],

	["ready_slashleft_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "musket_butt_up", 0, 0, arf_blend_in_6]
	],

	["release_slashleft_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.4, "musket_butt_up", 0, 20, arf_blend_in_5]
	],

	["release_slashleft_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "musket_butt_up", 20, 34, arf_blend_in_1]
	],

	["blocked_slashleft_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "musket_butt_up_stagger", 10, 0, arf_blend_in_2]
	],

	["parried_slashleft_twohanded", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "musket_butt_up_stagger", 10, 0, arf_blend_in_2]
	],

	["ready_thrust_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "slashright_twohanded_y4", 0, 15, arf_blend_in_6]
	],

	["release_thrust_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.61, "slashright_twohanded_y4", 16, 34, arf_blend_in_5]
	],

	["release_thrust_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.61, "slashright_twohanded_y4", 35, 60, arf_blend_in_2]
	],

	["blocked_thrust_twohanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "slashright_twohanded_y4", 21, 14, arf_blend_in_2]
	],

	["parried_thrust_twohanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "slashright_twohanded_y4", 21, 14, arf_blend_in_2]
	],

	["ready_overswing_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_ready", 16, 24, arf_blend_in_6]
	],

	["release_overswing_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.3, "attacks_new", 68, 69, arf_blend_in_5]
	],

	["release_overswing_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_new", 69, 70, arf_blend_in_1]
	],

	["blocked_overswing_twohanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "attacks_new", 69, 70, arf_blend_in_1]
	],

	["parried_overswing_twohanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "attacks_new", 69, 70, arf_blend_in_1]
	],

	["ready_thrust_onehanded", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_thrust_onehanded", 5, 13, arf_blend_in_6]
	],

	["release_thrust_onehanded", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.47, "attacks_thrust_onehanded", 12, 32, arf_blend_in_5]
	],

	["release_thrust_onehanded_continue", 0, amf_priority_continue|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_thrust_onehanded", 32, 54, arf_blend_in_1]
	],

	["blocked_thrust_onehanded", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 28515, 28513, arf_blend_in_5]
	],

	["parried_thrust_onehanded", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.7, "anim_human", 28515, 28513, arf_blend_in_5]
	],

	["ready_thrust_onehanded_horseback", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_thrust_onehanded", 5, 13, arf_blend_in_6]
	],

	["release_thrust_onehanded_horseback", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.47, "attacks_thrust_onehanded", 12, 32, arf_blend_in_5]
	],

	["release_thrust_onehanded_horseback_continue", 0, amf_priority_continue|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_thrust_onehanded", 32, 54, arf_blend_in_1]
	],

	["blocked_thrust_onehanded_horseback", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 28515, 28513, arf_blend_in_5]
	],

	["parried_thrust_onehanded_horseback", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.7, "anim_human", 28515, 28513, arf_blend_in_5]
	],

	["ready_thrust_onehanded_lance", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "thrust_onehanded_lance_hb", 5, 8, arf_blend_in_6]
	],

	["release_thrust_onehanded_lance", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.47, "thrust_onehanded_lance_hb", 8, 33, arf_blend_in_5]
	],

	["release_thrust_onehanded_lance_continue", 0, amf_priority_continue|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.1, "thrust_onehanded_lance_hb", 33, 45, arf_blend_in_1]
	],

	["blocked_thrust_onehanded_lance", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 29515, 29513, arf_blend_in_5]
	],

	["parried_thrust_onehanded_lance", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.7, "anim_human", 29515, 29513, arf_blend_in_5]
	],

	["ready_slashright_onehanded", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_single_righttoleft", 2, 5, arf_blend_in_6]
	],

	["release_slashright_onehanded", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.6, "attacks_single_righttoleft", 5, 28, arf_blend_in_5]
	],

	["release_slashright_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.4, "attacks_single_righttoleft", 28, 44, arf_blend_in_1]
	],

	["blocked_slashright_onehanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_righttoleft", 0, 14, arf_blend_in_5]
	],

	["parried_slashright_onehanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "parry_single_righttoleft", 0, 14, arf_blend_in_5]
	],

	["ready_slashleft_onehanded", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_single_lefttoright", 4, 11, arf_blend_in_6]
	],

	["release_slashleft_onehanded", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.61, "attacks_single_lefttoright", 11, 29, arf_blend_in_5]
	],

	["release_slashleft_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.4, "attacks_single_lefttoright", 29, 43, arf_blend_in_1]
	],

	["blocked_slashleft_onehanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_lefttoright", 0, 75, arf_blend_in_5]
	],

	["parried_slashleft_onehanded", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "parry_single_lefttoright", 0, 75, arf_blend_in_5]
	],

	["ready_overswing_onehanded", acf_enforce_rightside|acf_overswing, amf_priority_attack|amf_rider_rot_overswing|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_single_overswing", 5, 16, arf_blend_in_6]
	],

	["release_overswing_onehanded", acf_enforce_rightside|acf_overswing, amf_priority_attack|amf_rider_rot_overswing|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.6, "attacks_single_overswing", 16, 37, arf_blend_in_5]
	],

	["release_overswing_onehanded_continue", 0, amf_priority_continue|amf_rider_rot_overswing|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.2, "attacks_single_overswing", 37, 40, arf_blend_in_1]
	],

	["blocked_overswing_onehanded", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_overswing|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 29315, 29310, arf_blend_in_5]
	],

	["parried_overswing_onehanded", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_overswing|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 29315, 29310, arf_blend_in_5]
	],

	["ready_slash_horseback_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_single_righttoleft_horseback", 8, 17, arf_blend_in_6]
	],

	["release_slash_horseback_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.7, "attacks_single_righttoleft_horseback", 17, 39, arf_blend_in_5]
	],

	["release_slash_horseback_right_continue", 0, amf_priority_continue|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.4, "attacks_single_righttoleft_horseback", 39, 54, arf_blend_in_1]
	],

	["blocked_slash_horseback_right", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_righttoleft", 0, 14, arf_blend_in_5]
	],

	["parried_slash_horseback_right", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.6, "parry_single_righttoleft", 0, 14, arf_blend_in_5]
	],

	["ready_slash_horseback_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_single_lefttoright_horseback", 7, 21, arf_blend_in_6]
	],

	["release_slash_horseback_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.7, "attacks_single_lefttoright_horseback", 21, 43, arf_blend_in_5]
	],

	["release_slash_horseback_left_continue", 0, amf_priority_continue|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_single_lefttoright_horseback", 43, 51, arf_blend_in_1]
	],

	["blocked_slash_horseback_left", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_lefttoright", 0, 75, arf_blend_in_5]
	],

	["parried_slash_horseback_left", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.6, "parry_single_lefttoright", 0, 75, arf_blend_in_5]
	],

	["ready_slash_horseback_polearm_right", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_rider_rot_crossbow|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[1.0, "VC_sling_long", 0, 32, arf_blend_in_6|arf_cyclic]
	],

	["release_slash_horseback_polearm_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.6, "1h_slashright_13.9.10", 5, 30, arf_blend_in_5]
	],

	["release_slash_horseback_polearm_right_continue", 0, amf_priority_continue|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.2, "1h_slashright_13.9.10", 30, 35, arf_blend_in_1]
	],

	["blocked_slash_horseback_polearm_right", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_righttoleft", 0, 14, arf_blend_in_5]
	],

	["parried_slash_horseback_polearm_right", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_right|amf_use_weapon_speed|amf_play,
		[0.6, "parry_single_righttoleft", 0, 14, arf_blend_in_5]
	],

	["ready_slash_horseback_polearm_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[1.1, "VC_sling", 0, 32, arf_blend_in_6|arf_cyclic]
	],

	["release_slash_horseback_polearm_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.61, "1h_slashleft_13.9.10", 5, 29, arf_blend_in_5]
	],

	["release_slash_horseback_polearm_left_continue", 0, amf_priority_continue|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.2, "1h_slashleft_13.9.10", 29, 34, arf_blend_in_1]
	],

	["blocked_slash_horseback_polearm_left", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_lefttoright", 0, 75, arf_blend_in_5]
	],

	["parried_slash_horseback_polearm_left", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_swing_left|amf_use_weapon_speed|amf_play,
		[0.3, "parry_single_lefttoright", 0, 75, arf_blend_in_5]
	],

	["ready_overswing_staff", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_staff_uptodown", 9, 26, arf_blend_in_6]
	],

	["release_overswing_staff", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.6, "attacks_staff_uptodown", 26, 61, arf_blend_in_5]
	],

	["release_overswing_staff_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_staff_uptodown", 61, 68, arf_blend_in_1]
	],

	["blocked_overswing_staff", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 27017, 27014, arf_blend_in_2]
	],

	["parried_overswing_staff", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 27017, 27014, arf_blend_in_2]
	],

	["ready_thrust_staff", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_staff_thrust", 14, 21, arf_blend_in_6]
	],

	["release_thrust_staff", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play,
		[0.45, "attacks_staff_thrust", 21, 40, arf_blend_in_5]
	],

	["release_thrust_staff_continue", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.6, "attacks_staff_thrust", 40, 58, arf_blend_in_5]
	],

	["blocked_thrust_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 27316, 27313, arf_blend_in_2]
	],

	["parried_thrust_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.7, "anim_human", 27316, 27313, arf_blend_in_2]
	],

	["ready_slashleft_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_staff_lefttoright", 10, 16, arf_blend_in_6]
	],

	["release_slashleft_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.6, "attacks_staff_lefttoright", 16, 44, arf_blend_in_5]
	],

	["release_slashleft_staff_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_staff_lefttoright", 44, 55, arf_blend_in_1]
	],

	["blocked_slashleft_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 27615, 27613, arf_blend_in_2]
	],

	["parried_slashleft_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 27615, 27613, arf_blend_in_2]
	],

	["ready_slashright_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_staff_righttoleft", 6, 16, arf_blend_in_6]
	],

	["release_slashright_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.6, "attacks_staff_righttoleft", 16, 40, arf_blend_in_5]
	],

	["release_slashright_staff_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.4, "attacks_staff_righttoleft", 40, 48, arf_blend_in_1]
	],

	["blocked_slashright_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "anim_human", 27915, 27913, arf_blend_in_2]
	],

	["parried_slashright_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.6, "anim_human", 27915, 27913, arf_blend_in_2]
	],

	["defend_fist", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction,
		[0.75, "anim_human", 24950, 24960, arf_blend_in_3]
	],

	["defend_fist_keep", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend|amf_rider_rot_defend|amf_keep|amf_client_owner_prediction,
		[2.0, "anim_human", 24950, 24960, arf_blend_in_2|arf_cyclic]
	],

	["defend_fist_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 24962, 24970, arf_blend_in_0]
	],

	["defend_fist_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 24962, 24970, arf_blend_in_0]
	],

	["defend_fist_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 24962, 24970, arf_blend_in_0]
	],

	["defend_shield_forward", 0, amf_priority_defend|amf_rider_rot_shield|amf_use_defend_speed|amf_play|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_shield_forward", 6, 25, arf_blend_in_3]
	],

	["defend_shield_up", 0, amf_priority_defend|amf_rider_rot_shield|amf_use_defend_speed|amf_play|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_shield_up", 1, 27, arf_blend_in_3]
	],

	["defend_shield_right", 0, amf_priority_defend|amf_rider_rot_shield|amf_use_defend_speed|amf_play|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_shield_right", 5, 26, arf_blend_in_3]
	],

	["defend_shield_left", 0, amf_priority_defend|amf_rider_rot_shield|amf_use_defend_speed|amf_play|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_shield_left", 5, 26, arf_blend_in_3]
	],

	["defend_shield", 0, amf_priority_defend|amf_rider_rot_shield|amf_use_defend_speed|amf_play|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_shield_up", 1, 17, arf_blend_in_3]
	],

	["defend_shield_keep", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend|amf_rider_rot_defend|amf_keep|amf_client_owner_prediction,
		[2.0, "shield3", 6, 6, arf_blend_in_4|arf_cyclic]
	],

	["defend_shield_parry_1", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_shield|amf_play|amf_restart,
		[0.6, "anim_human", 35121, 35130, arf_blend_in_1]
	],

	["defend_shield_parry_2", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_shield|amf_play|amf_restart,
		[0.6, "anim_human", 35121, 35130, arf_blend_in_1]
	],

	["defend_shield_parry_3", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend_parry|amf_rider_rot_shield|amf_play|amf_restart,
		[0.8, "anim_human", 35121, 35130, arf_blend_in_1]
	],

	["defend_forward_greatsword", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "musket_block_down", 0, 0, arf_blend_in_3]
	],

	["defend_forward_greatsword_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "musket_block_down", 0, 0, arf_blend_in_3|arf_cyclic]
	],

	["defend_forward_greatsword_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_down", 1, 3, arf_blend_in_1]
	],

	["defend_forward_greatsword_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_down", 1, 3, arf_blend_in_1]
	],

	["defend_forward_greatsword_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "musket_block_down", 1, 3, arf_blend_in_1]
	],

	["defend_up_twohanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "musket_block_up", 0, 0, arf_blend_in_3]
	],

	["defend_up_twohanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "musket_block_up", 0, 0, arf_blend_in_3|arf_cyclic]
	],

	["defend_up_twohanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_up", 1, 3, arf_blend_in_1]
	],

	["defend_up_twohanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_up", 1, 3, arf_blend_in_1]
	],

	["defend_up_twohanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "musket_block_up", 1, 3, arf_blend_in_1]
	],

	["defend_right_twohanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "musket_block_right", 0, 0, arf_blend_in_3]
	],

	["defend_right_twohanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "musket_block_right", 0, 0, arf_blend_in_3|arf_cyclic]
	],

	["defend_right_twohanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_right", 1, 3, arf_blend_in_1]
	],

	["defend_right_twohanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_right", 1, 3, arf_blend_in_1]
	],

	["defend_right_twohanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "musket_block_right", 1, 3, arf_blend_in_1]
	],

	["defend_left_twohanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "musket_block_left", 0, 0, arf_blend_in_3]
	],

	["defend_left_twohanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "musket_block_left", 0, 0, arf_blend_in_3|arf_cyclic]
	],

	["defend_left_twohanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_left", 1, 3, arf_blend_in_1]
	],

	["defend_left_twohanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "musket_block_left", 1, 3, arf_blend_in_1]
	],

	["defend_left_twohanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "musket_block_left", 1, 3, arf_blend_in_1]
	],

	["defend_forward_onehanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_forward_onehanded", 20, 41, arf_blend_in_3]
	],

	["defend_forward_onehanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[5.0, "defend_onehanded", 15, 70, arf_blend_in_3|arf_cyclic]
	],

	["defend_forward_onehanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "defend_onehanded", 75, 85, arf_blend_in_1]
	],

	["defend_forward_onehanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "defend_onehanded", 75, 85, arf_blend_in_1]
	],

	["defend_forward_onehanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "defend_onehanded", 75, 85, arf_blend_in_1]
	],

	["defend_up_onehanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_up_onehanded", 9, 25, arf_blend_in_3]
	],

	["defend_up_onehanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.8, "defend_up_onehanded_keep", 1, 87, arf_blend_in_3|arf_cyclic]
	],

	["defend_up_onehanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 36121, 36130, arf_blend_in_1]
	],

	["defend_up_onehanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 36121, 36130, arf_blend_in_1]
	],

	["defend_up_onehanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 36121, 36130, arf_blend_in_1]
	],

	["defend_right_onehanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_right_onehanded", 14, 31, arf_blend_in_3]
	],

	["defend_right_onehanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.5, "defend_right_onehanded_keep", 0, 79, arf_blend_in_5|arf_cyclic]
	],

	["defend_right_onehanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 36221, 36230, arf_blend_in_1]
	],

	["defend_right_onehanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 36221, 36230, arf_blend_in_1]
	],

	["defend_right_onehanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 36221, 36230, arf_blend_in_1]
	],

	["defend_left_onehanded", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_left_onehanded", 12, 28, arf_blend_in_3]
	],

	["defend_left_onehanded_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.2, "defend_left_onehanded_keep", 1, 71, arf_blend_in_3|arf_cyclic]
	],

	["defend_left_onehanded_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 36321, 36330, arf_blend_in_1]
	],

	["defend_left_onehanded_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 36321, 36330, arf_blend_in_1]
	],

	["defend_left_onehanded_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 36321, 36330, arf_blend_in_1]
	],

	["defend_forward_staff", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "defend_staff", 0, 5, arf_blend_in_3]
	],

	["defend_forward_staff_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "defend_staff", 5, 5, arf_blend_in_3|arf_cyclic]
	],

	["defend_forward_staff_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "defend_staff", 56, 70, arf_blend_in_1]
	],

	["defend_forward_staff_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "defend_staff", 56, 70, arf_blend_in_1]
	],

	["defend_forward_staff_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "defend_staff", 56, 70, arf_blend_in_1]
	],

	["defend_up_staff", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "anim_human", 37110, 37120, arf_blend_in_3]
	],

	["defend_up_staff_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "anim_human", 37120, 37120, arf_blend_in_3|arf_cyclic]
	],

	["defend_up_staff_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 37121, 37130, arf_blend_in_1]
	],

	["defend_up_staff_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 37121, 37130, arf_blend_in_1]
	],

	["defend_up_staff_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 37121, 37130, arf_blend_in_1]
	],

	["defend_right_staff", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "anim_human", 37210, 37220, arf_blend_in_3]
	],

	["defend_right_staff_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "anim_human", 37220, 37220, arf_blend_in_3|arf_cyclic]
	],

	["defend_right_staff_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 37221, 37230, arf_blend_in_1]
	],

	["defend_right_staff_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 37221, 37230, arf_blend_in_1]
	],

	["defend_right_staff_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 37221, 37230, arf_blend_in_1]
	],

	["defend_left_staff", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_play|amf_keep|amf_restart|amf_client_owner_prediction|amf_use_inertia,
		[0.75, "anim_human", 37310, 37320, arf_blend_in_3]
	],

	["defend_left_staff_keep", 0, amf_priority_defend|amf_rider_rot_defend|amf_use_defend_speed|amf_keep|amf_client_owner_prediction,
		[2.0, "anim_human", 37320, 37320, arf_blend_in_3|arf_cyclic]
	],

	["defend_left_staff_parry_1", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 37321, 37330, arf_blend_in_1]
	],

	["defend_left_staff_parry_2", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.6, "anim_human", 37321, 37330, arf_blend_in_1]
	],

	["defend_left_staff_parry_3", 0, amf_priority_defend_parry|amf_rider_rot_defend|amf_play|amf_restart,
		[0.8, "anim_human", 37321, 37330, arf_blend_in_1]
	],

	["strike_head_left", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 55, 71, arf_blend_in_3]
	],

	["strike_head_right", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 4, 19, arf_blend_in_3]
	],

	["strike_head_front", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 180, 198, arf_blend_in_3]
	],

	["strike_head_back", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.6, "strikes_back", 4, 25, arf_blend_in_3]
	],

	["strike_chest_left", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 706, 724, arf_blend_in_3]
	],

	["strike_chest_right", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.6, "strikes", 487, 512, arf_blend_in_3]
	],

	["strike_chest_front", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.6, "strikes", 881, 905, arf_blend_in_3]
	],

	["strike_chest_back", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes_back", 401, 418, arf_blend_in_3]
	],

	["strike_abdomen_left", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.58, "strikes", 1425, 1444, arf_blend_in_3]
	],

	["strike_abdomen_right", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.6, "strikes", 1168, 1188, arf_blend_in_3]
	],

	["strike_abdomen_front", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.6, "strikes", 1618, 1640, arf_blend_in_3]
	],

	["strike_abdomen_back", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.53, "strikes_back", 886, 904, arf_blend_in_3]
	],

	["strike_legs_left", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 2284, 2305, arf_blend_in_3]
	],

	["strike_legs_right", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.56, "strikes", 1999, 2020, arf_blend_in_3]
	],

	["strike_legs_front", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.56, "strikes", 2655, 2676, arf_blend_in_3]
	],

	["strike_legs_back", 0, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes_back", 1120, 1137, arf_blend_in_3]
	],

	["strike2_head_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 55, 71, arf_blend_in_3]
	],

	["strike2_head_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 4, 19, arf_blend_in_3]
	],

	["strike2_head_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 180, 198, arf_blend_in_3]
	],

	["strike2_head_back", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes_back", 4, 25, arf_blend_in_3]
	],

	["strike2_chest_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes", 706, 724, arf_blend_in_3]
	],

	["strike2_chest_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 487, 512, arf_blend_in_3]
	],

	["strike2_chest_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 881, 905, arf_blend_in_3]
	],

	["strike2_chest_back", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes_back", 401, 418, arf_blend_in_3]
	],

	["strike2_abdomen_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 1425, 1444, arf_blend_in_3]
	],

	["strike2_abdomen_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 1168, 1188, arf_blend_in_3]
	],

	["strike2_abdomen_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 1618, 1640, arf_blend_in_3]
	],

	["strike2_abdomen_back", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.53, "strikes_back", 886, 904, arf_blend_in_3]
	],

	["strike2_legs_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 2284, 2305, arf_blend_in_3]
	],

	["strike2_legs_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.56, "strikes", 1999, 2020, arf_blend_in_3]
	],

	["strike2_legs_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.56, "strikes", 2655, 2676, arf_blend_in_3]
	],

	["strike2_legs_back", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.5, "strikes_back", 1120, 1137, arf_blend_in_3]
	],

	["strike3_head_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.99, "strikes3_head", 107, 146, arf_blend_in_3]
	],

	["strike3_head_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_head", 208, 251, arf_blend_in_3]
	],

	["strike3_head_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_head", 14, 48, arf_blend_in_3]
	],

	["strike3_head_back", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_head", 309, 346, arf_blend_in_3]
	],

	["strike3_chest_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_chest", 61, 97, arf_blend_in_3]
	],

	["strike3_chest_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_chest", 108, 145, arf_blend_in_3]
	],

	["strike3_chest_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.8, "strikes3_chest", 3, 27, arf_blend_in_3]
	],

	["strike3_abdomen_left", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_abdomen", 105, 150, arf_blend_in_3]
	],

	["strike3_abdomen_right", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_abdomen", 63, 98, arf_blend_in_3]
	],

	["strike3_abdomen_front", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.9, "strikes3_abdomen", 4, 43, arf_blend_in_3]
	],

	["strike3_abdomen_back", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.08, "strikes3_abdomen_back", 0, 53, arf_blend_in_3]
	],

	["strike_head_front_left_reloc", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.6, "strike_frontal", 0, 37, arf_blend_in_3]
	],

	["fall_face_hold", acf_align_with_ground|acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.2, "death_face", 8, 60, arf_blend_in_16|arf_make_custom_sound, 127, (0.0, 0.0, 0.0), 0.6]
	],

	["fall_chest_front", acf_align_with_ground|acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[1.0, "death_chest", 4, 37, arf_blend_in_16|arf_make_custom_sound, 229, (0.0, 0.0, 0.0), 0.5]
	],

	["fall_abdomen_hold_front", acf_align_with_ground|acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.7, "death_abdomen", 5, 96, arf_blend_in_16|arf_make_custom_sound, 102, (0.0, 0.0, 0.0), 0.5]
	],

	["fall_head_front", acf_align_with_ground|acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[1.2, "anim_human", 40100, 40138, arf_blend_in_16|arf_make_custom_sound, 204, (0.0, 0.0, 0.0), 0.8]
	],

	["fall_right_front", acf_align_with_ground|acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.0, "death2", 0, 53, arf_blend_in_16|arf_make_custom_sound, 165, (0.0, 0.0, 0.0), 1.0]
	],

	["fall_body_back", acf_align_with_ground|acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.7, "death", 0, 83, arf_blend_in_16|arf_make_custom_sound, 53623, (0.0, 0.0, 0.0), 1.8]
	],

	["fall_rider_right_forward", acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.2, "anim_human", 40200, 40275, arf_blend_in_3|arf_make_custom_sound, 204, (0.0, 0.0, 0.0), 0.3]
	],

	["fall_rider_right", acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.2, "anim_human", 40200, 40275, arf_blend_in_3|arf_make_custom_sound, 204, (0.0, 0.0, 0.0), 0.3]
	],

	["fall_rider_left", acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_client_prediction|amf_keep,
		[2.2, "anim_human", 40200, 40275, arf_blend_in_3|arf_make_custom_sound, 204, (0.0, 0.0, 0.0), 0.3]
	],

	["rider_fall_right", acf_enforce_all|acf_displace_position, amf_priority_fall_from_horse|amf_accurate_body|amf_client_prediction|amf_play,
		[2.5, "anim_human_02", 350, 382, arf_blend_in_8, 0, (0.8, -1.8, 0.0), 0.5]
	],

	["rider_fall_roll", acf_enforce_all|acf_displace_position, amf_priority_fall_from_horse|amf_accurate_body|amf_client_prediction|amf_play,
		[2.5, "anim_human", 42000, 42084, arf_blend_in_8, 0, (0.0, 0.0, 0.0), 1.0]
	],

	["strike_chest_front_stop", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.4, "anim_human", 45000, 45010, arf_blend_in_3]
	],

	["strike_fall_back_rise", acf_align_with_ground|acf_enforce_lowerbody, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.7, "anim_human", 45400, 45453, arf_blend_in_2|arf_make_custom_sound, 102, (0.0, 0.0, 0.0), 0.5]
	],

	["strike_fall_back_rise_upper", acf_align_with_ground, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.44, "anim_human", 45400, 45445, arf_blend_in_2]
	],

	["cheer", 0, amf_priority_mount|amf_play,
		[6.0, "man_cheer", 0, 185, arf_blend_in_5],
		[3.0, "man_cheer", 200, 289, arf_blend_in_5],
		[4.5, "man_cheer", 300, 437, arf_blend_in_5],
		[5.5, "man_cheer", 450, 617, arf_blend_in_5]
	],

	["cheer_stand", acf_anim_length(16), amf_priority_mount|amf_play,
		[31.5, "man_cheer", 650, 1597, arf_blend_in_5]
	],

	["stand_townguard", 0, 0,
		[79.0, "stand_guardsman", 0, 2397, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["stand_lady", 0, 0,
		[29.0, "lady_stand", 0, 863, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["stand_lord", 0, 0,
		[10.0, "lord_stand", 0, 111, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["dance", 0, 0,
		[20.0, "anim_human", 0, 387, arf_blend_in_5]
	],

	["pose_1", 0, 0,
		[3.0, "poses", 0, 0, arf_cyclic]
	],

	["pose_2", 0, 0,
		[3.0, "poses", 2, 2, arf_cyclic]
	],

	["pose_3", 0, 0,
		[3.0, "poses", 4, 4, arf_cyclic]
	],

	["pose_4", 0, 0,
		[3.0, "poses", 6, 6, arf_cyclic]
	],

	["pose_5", 0, 0,
		[3.0, "poses", 8, 8, arf_cyclic]
	],

	["wedding_guest", 0, amf_priority_die|amf_play,
		[30.0, "wedding_guest", 0, 906, arf_cyclic]
	],

	["wedding_guest_notr", 0, amf_priority_die|amf_play,
		[32.0, "wedding_guest_notr", 0, 962, arf_cyclic]
	],

	["wedding_guest_woman", 0, amf_priority_die|amf_play,
		[27.5, "wedding_guest_woman", 0, 825, arf_cyclic]
	],

	["wedding_dad_stairs", 0, amf_priority_die|amf_start_instantly|amf_play,
		[10.0, "wedding_dad_stairs", 0, 300, arf_blend_in_0]
	],

	["wedding_dad_walk", 0, amf_priority_die|amf_start_instantly|amf_play,
		[4.5, "wedding_dad_walk", 0, 134, arf_blend_in_0]
	],

	["wedding_bride_stairs", 0, amf_priority_die|amf_start_instantly|amf_play,
		[10.0, "wedding_bride_stairs", 0, 300, arf_blend_in_0]
	],

	["wedding_bride_walk", 0, amf_priority_die|amf_start_instantly|amf_play,
		[4.5, "wedding_bride_walk", 0, 134, arf_blend_in_0]
	],

	["wedding_groom_wait", 0, amf_priority_die|amf_start_instantly|amf_play|amf_keep,
		[10.0, "wedding_groom_last", 0, 2, arf_blend_in_0]
	],

	["wedding_groom_last", 0, amf_priority_die|amf_start_instantly|amf_play|amf_keep,
		[10.0, "wedding_groom_last", 0, 300, arf_blend_in_0]
	],

	["wedding_dad_last", 0, amf_priority_die|amf_start_instantly|amf_play|amf_keep,
		[10.0, "wedding_dad_last", 0, 300, arf_blend_in_0]
	],

	["wedding_bride_last", 0, amf_priority_die|amf_start_instantly|amf_play|amf_keep,
		[10.0, "wedding_bride_last", 0, 300, arf_blend_in_0]
	],

	["equip_bayonet", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_musket", 5, 13, arf_blend_in_0]
	],

	["unequip_bayonet", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_musket", 5, 13, arf_blend_in_0]
	],

	["crouch_unarmed", 0, amf_client_prediction,
		[11.0, "crouch_stand_man", 0, 315, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["crouch_single", 0, amf_client_prediction,
		[11.0, "crouch_stand_man", 0, 315, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["crouch_greatsword", 0, amf_client_prediction,
		[6.0, "crouch_greatsword_cstance", 0, 170, arf_cyclic|arf_use_stand_progress, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["crouch_staff", 0, amf_client_prediction,
		[5.0, "crouch_staff_cstance", 0, 120, arf_cyclic|arf_use_stand_progress]
	],

	["crouch_crossbow", 0, amf_client_prediction,
		[2.0, "staff_cstance", 0, 60, arf_cyclic|arf_use_stand_progress]
	],

	["crouch_ready_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_pistol|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
		[0.5, "throwing_slinge_20_35", 0, 15, arf_blend_in_6|arf_make_custom_sound|arf_cyclic, 28707, (0.0, 0.0, 0.0), 0.0]
	],

	["crouch_release_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_pistol|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[2.0, "throwing_slinge", 30, 59, arf_blend_in_0]
	],

	["reload_musket_full", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[0.3, "throwing_slinge", 80, 119, arf_blend_in_0]
	],

	["reload_musket_two_third", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[0.3, "throwing_slinge", 110, 119, arf_blend_in_0]
	],

	["reload_musket_one_third", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[0.3, "throwing_slinge", 90, 119, arf_blend_in_0]
	],

	["crouch_pike", 0, amf_client_prediction,
		[3.3, "crouch_staff_cstance_attack", 0, 100, arf_cyclic|arf_use_stand_progress]
	],

	["crouch_pike_recover", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[1.2, "crouch_staff_cstance_attack", 105, 137, arf_blend_in_3]
	],

	["ready_overswing_spear", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "attacks_staff_thrust_overhead", 6, 21, arf_blend_in_6]
	],

	["release_overswing_spear", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.45, "attacks_staff_thrust_overhead", 21, 43, arf_blend_in_5]
	],

	["release_overswing_spear_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "attacks_staff_thrust_overhead", 43, 50, arf_blend_in_2]
	],

	["parried_overswing_spear", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "attacks_staff_thrust_overhead", 50, 43, arf_blend_in_2]
	],

	["blocked_overswing_spear", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "attacks_staff_thrust_overhead", 50, 43, arf_blend_in_2]
	],

	["reload_pistol_half", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
		[0.3, "throwing_slinge", 100, 119, arf_blend_in_0]
	],

	["ready_overswing_musket", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "1h_spear_thrust_overhead", 0, 20, arf_blend_in_6]
	],

	["release_overswing_musket", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.45, "1h_spear_thrust_overhead", 20, 41, arf_blend_in_5]
	],

	["release_overswing_musket_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.3, "1h_spear_thrust_overhead", 41, 52, arf_blend_in_2]
	],

	["parried_overswing_musket", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "1h_spear_thrust_overhead", 26, 22, arf_blend_in_2]
	],

	["blocked_overswing_musket", 0, amf_priority_defend_parry|amf_use_weapon_speed|amf_play,
		[0.3, "1h_spear_thrust_overhead", 26, 22, arf_blend_in_2]
	],

	["ready_thrust_musket", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_use_inertia,
		[0.35, "romanthrust", 0, 2, arf_blend_in_6]
	],

	["release_thrust_musket", acf_enforce_rightside|acf_thrust|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_continue_to_next,
		[0.3, "romanthrust", 2, 7, arf_blend_in_5]
	],

	["release_thrust_musket_continue", 0, amf_priority_continue|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
		[0.45, "romanthrust", 7, 10, arf_blend_in_1]
	],

	["parried_thrust_musket", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "romanthrust", 3, 1, arf_blend_in_5]
	],

	["blocked_thrust_musket", acf_enforce_rightside, amf_priority_defend_parry|amf_rider_rot_thrust|amf_use_weapon_speed|amf_play,
		[0.6, "romanthrust", 3, 1, arf_blend_in_5]
	],

	["equip_pistol_melee", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_pistol", 0, 10, arf_blend_in_0]
	],

	["unequip_pistol_melee", 0, amf_priority_equip|amf_client_prediction|amf_play|amf_restart,
		[0.3, "equip_pistol", 0, 10, arf_blend_in_0]
	],

	["shield_bash", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.5, "defend_shield_parry_all", 1, 50, arf_blend_in_3],
		[1.5, "defend_shield_right", 1, 50, arf_blend_in_3],
		[1.5, "defend_shield_left", 1, 50, arf_blend_in_3],
		[1.5, "defend_shield_right", 1, 50, arf_blend_in_3]
	],

	["shield_strike", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.0, "anim_human", 45000, 45010, arf_blend_in_3|arf_make_custom_sound],
		[1.7, "anim_human", 45400, 45453, arf_blend_in_2|arf_make_custom_sound],
		[1.44, "anim_human", 45400, 45445, arf_blend_in_2|arf_make_custom_sound]
	],

	["spearwall_hold", acf_align_with_ground|acf_enforce_all|acf_thrust, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[4.0, "anim_human", 27310, 27310, arf_blend_in_6]
	],

	["sit_drink", acf_enforce_all, amf_accurate_body,
		[3.0, "sit_drink", 0, 2, arf_cyclic, 0, (0.0, 0.0, 0.0), 0.25]
	],

	["unused_human_anim_48", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_49", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_50", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_51", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_52", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_53", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_54", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_55", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_56", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_57", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_58", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_59", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_60", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_61", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_62", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_63", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_64", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_65", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_66", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_67", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_68", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_69", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_70", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_71", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_72", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_73", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_74", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_75", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_76", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_77", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_78", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_79", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_80", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_81", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_82", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_83", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_84", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_85", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_86", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_87", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_88", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_89", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_90", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_91", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_92", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_93", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_94", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_95", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_96", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_97", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_98", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_99", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["unused_human_anim_100", 0, 0,
		[1.0, "anim_human", 0, 1, 0]
	],

	["horse_stand", 0, amf_client_prediction,
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 644, 688, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 688, 732, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[3.5, "anim_horse", 732, 820, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress],
		[2.5, "anim_horse", 820, 908, arf_cyclic|arf_use_stand_progress]
	],

	["horse_pace_1", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[1.0, "anim_horse", 0, 31, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 3938413375, (0.0, 0.0, 0.0), 0.25]
	],

	["horse_pace_2", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.8, "anim_horse", 50, 69, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 2829396006, (0.0, 0.0, 0.0), 0.9]
	],

	["horse_pace_3", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.6, "anim_horse", 100, 116, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 1801057005, (0.0, 0.0, 0.0), 0.6]
	],

	["horse_pace_4", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
		[0.5, "anim_horse", 150, 165, arf_make_walk_sound|arf_cyclic|arf_use_walk_progress, 4022947686, (0.0, 0.0, 0.0), 0.2]
	],

	["horse_walk_backward", acf_enforce_lowerbody, amf_client_prediction,
		[1.9, "anim_horse", 31, 0, arf_make_walk_sound|arf_cyclic|arf_use_inv_walk_progress, 2693669137, (0.0, 0.0, 0.0), 0.0]
	],

	["horse_rear", acf_enforce_lowerbody|acf_ignore_slope, amf_priority_rear|amf_play,
		[1.7, "anim_horse", 265, 297, arf_blend_in_8]
	],

	["horse_jump", acf_enforce_lowerbody, amf_priority_jump|amf_priority_ride|amf_client_prediction|amf_play,
		[1.6, "anim_horse", 205, 222, arf_blend_in_4]
	],

	["horse_jump_end", acf_enforce_lowerbody, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[0.1, "anim_horse", 222, 224, arf_blend_in_8]
	],

	["horse_turn_right", 0, amf_client_prediction,
		[1.0, "anim_horse", 500, 533, arf_blend_in_4|arf_cyclic]
	],

	["horse_turn_left", 0, amf_client_prediction,
		[1.0, "anim_horse", 450, 483, arf_blend_in_4|arf_cyclic]
	],

	["horse_turn_right_head", 0, amf_client_prediction,
		[1.0, "anim_horse", 500, 533, arf_blend_in_4|arf_cyclic]
	],

	["horse_turn_left_head", 0, amf_client_prediction,
		[1.0, "anim_horse", 450, 483, arf_blend_in_4|arf_cyclic]
	],

	["horse_slow", 0, amf_client_prediction,
		[3.0, "anim_horse", 0, 31, arf_cyclic],
		[1.5, "anim_horse", 0, 31, arf_cyclic]
	],

	["horse_fall_in_place", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_client_prediction|amf_keep,
		[4.0, "anim_horse", 0, 38, arf_blend_in_16|arf_make_custom_sound]
	],

	["horse_fall_right", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_client_prediction|amf_keep,
		[1.75, "anim_horse", 350, 375, arf_blend_in_8|arf_make_custom_sound, 153, (0.0, 0.0, 0.0), 0.5]
	],

	["horse_fall_roll", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_client_prediction|amf_keep,
		[2.5, "anim_horse", 400, 428, arf_blend_in_8|arf_make_custom_sound, 76, (0.0, 0.0, 0.0), 1.8]
	],

	["unused_horse_anim_1", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_2", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_3", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_4", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_5", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_6", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_7", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_8", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_9", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_10", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_11", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_12", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_13", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_14", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_15", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_16", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_17", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_18", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_19", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_20", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_21", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_22", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_23", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_24", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_25", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_26", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_27", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_28", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_29", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_30", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_31", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_32", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_33", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_34", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_35", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_36", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_37", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_38", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_39", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_40", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_41", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_42", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_43", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_44", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_45", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_46", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_47", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_48", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_49", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_50", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_51", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_52", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_53", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_54", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_55", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_56", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_57", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_58", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_59", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_60", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_61", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_62", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_63", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_64", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_65", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_66", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_67", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_68", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_69", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_70", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_71", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_72", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_73", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_74", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_75", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_76", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_77", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_78", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_79", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_80", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_81", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_82", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_83", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_84", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_85", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_86", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_87", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_88", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_89", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_90", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_91", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_92", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_93", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_94", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_95", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_96", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_97", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_98", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_99", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

	["unused_horse_anim_100", 0, 0,
		[1.0, "anim_horse", 0, 1, 0]
	],

]