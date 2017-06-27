from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
	("cant_find_this", "cant_find_this.ogg", 0, 0),

	("armorer", "armorer.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 0),

	("capture", "capture.ogg", mtf_module_track, 0),

	("empty_village", "empty_village.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("escape", "escape.ogg", mtf_persist_until_finished|mtf_module_track, 0),

#euro begin	
	("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
#euro battle music 1
	("euro_1", "euro_1.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_module_track,mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro battle/siege music 2
	("euro_2", "euro_2.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro travel music 1
	("euro_3", "euro_3.mp3", mtf_culture_1|mtf_sit_tavern|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_sit_travel),
#euro travel music 2
	("euro_4", "euro_4.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_sit_travel),
#euro battle/siege music 3
	("euro_5", "euro_5.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro siege music 1
	("euro_6", "euro_6.ogg", mtf_culture_1|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro travel music 3
	("pog", "pog.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_sit_travel),
#euro battle/siege music 4
	("euro_8", "euro_8.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_sit_ambushed|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro travel music 4
	("euro_9", "euro_9.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_sit_travel),
#euro battle/siege music 5
	("euro_10", "euro_10.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro battle/siege music 6
	("euro_11", "euro_11.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_sit_ambushed|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#euro battle music 11
	#("euro_12", "euro_12.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_sit_travel),
#euro travel music 5
	("euro_13", "euro_13.mp3", mtf_culture_1|mtf_sit_travel|mtf_sit_tavern|mtf_module_track, mtf_culture_1|mtf_sit_travel),

#euro end

#balt begin
#balt siege music 1
	("baltic_1", "baltic_1.ogg", mtf_culture_2|mtf_sit_siege|mtf_module_track, mtf_culture_2),
#balt battle/siege music 1
	("baltic_2", "baltic_2.ogg", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#balt travel music 1
	("baltic_3", "baltic_3.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2|mtf_sit_travel),
#balt battle/siege music 2
	("baltic_4", "baltic_4.ogg", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#balt siege music 2
	("baltic_5", "baltic_5.ogg", mtf_culture_2|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#balt travel music 2
	("baltic_6", "baltic_6.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2|mtf_sit_travel),
#balt travel music 3
	
#balt travel music 4
#balt battle/siege music 3
#balt battle/siege music 4
#balt battle/siege music 5
#balt battle/siege music 6

#balt end

	
#rus begin
#rus battle/siege music 1
	("rus_1", "rus_1.ogg", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all), 
#rus battle/siege music 2
	("rus_2", "rus_2.ogg", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_sit_ambushed|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#rus travel music 1
	("rus_3", "rus_3.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5|mtf_sit_travel),
#rus battle/siege music rus 3
	("rus_4", "rus_4.ogg", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_sit_ambushed|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#rus travel music 2
	("rus_5", "rus_5.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5|mtf_sit_travel),
#rus travel music 3
#rus travel music 4	
#rus battle/siege music 4
#rus battle/siege music 5
#rus battle/siege music 6
#rus end

#sandnigger begin
#sandnigger battle/siege music 1
	("saracen_1", "saracen_1.ogg", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_sit_ambushed|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#sandnigger travel music 1
	("saracen_2", "saracen_2.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4|mtf_sit_travel),
#sandnigger siege music 1
	("saracen_3", "saracen_3.ogg", mtf_culture_4|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#sandnigger travel music 2
	("saracen_4", "saracen_4.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4|mtf_sit_travel),
	#("saracen_5", "saracen_5.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4), <<<--- WHAT the fuck?
#sandnigger battle/siege music 2
	("saracen_6", "saracen_6.ogg", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_sit_ambushed|mtf_module_track, mtf_culture_4),
#sandnigger siege music 2
	("saracen_7", "saracen_7.ogg", mtf_culture_4|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#sandnigger travel music 2
	("saracen_2", "saracen_8.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4|mtf_sit_travel),
#sandnigger travel music 3
#sandnigger travel music 4	
#rus battle/siege music 3
#rus battle/siege music 4
#rus battle/siege music 5	
#sandnigger end 

#mongols begin

	#("mong_1", "mong_1.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3), <-- this is rus wtf is in here?
#not mongol music btw
	("mong_2", "mong_2.ogg", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all), #<-- this is  not mongol wtf is in here?
#mongols battle/siege music 1
	("mong_3", "mong_3.ogg", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#mongols travel music 1
	#("mong_4", "mong_4.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3|mtf_sit_travel),
#mongols travel music 2
	("mong_5", "mong_5.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3|mtf_sit_travel),
#mongols battle/siege music 2
	("mong_6", "mong_6.ogg", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#mongols travel music 3
	("mong_7", "mong_7.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3|mtf_sit_travel),
#mongols siege music 1
	("mong_8", "mong_8.ogg", mtf_culture_3|mtf_sit_siege|mtf_module_track,  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
#mongols end

	("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

	("coronation", "coronation.ogg", mtf_persist_until_finished, 0),

	#("ambient_1", "ambient_1.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_2", "ambient_2.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_3", "ambient_3.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_4", "ambient_4.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_5", "ambient_5.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_6", "ambient_6.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_7", "ambient_7.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_8", "ambient_8.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_9", "ambient_9.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	#("ambient_10", "ambient_10.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	#("silence", "silence.ogg", mtf_persist_until_finished|mtf_module_track, 0),

]