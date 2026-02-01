INSERT INTO d_game_class_type (alias,class_level,cell_level,cell_add_amount) VALUES
	 ('full',1,1,2),
	 ('full',5,3,2),
	 ('full',10,1,2),
	 ('full',10,2,3),
	 ('full',10,3,1),
	 ('full',10,4,3),
	 ('full',10,5,2),
	 ('full',17,9,1),
	 ('half',2,1,2),
	 ('half',5,2,2),
	 ('half',9,3,2),
	 ('half',10,1,2),
	 ('half',10,2,1);
INSERT INTO d_class (alias,title,choose_subclass_level,"type") VALUES
	 ('wizard','Волшебник',2,'full'),
	 ('cleric','Жрец',1,'full'),
	 ('ranger','Следопыт',3,'half');
INSERT INTO d_subclass (class_alias,alias,title) VALUES
	 ('wizard','transmutation','школа преобразования'),
	 ('wizard','evocation','школа воплощения'),
	 ('cleric','life','домен жизни'),
	 ('cleric','peace','домен мира'),
	 ('cleric','light','домен света');
INSERT INTO d_spell (id,alias,title,"level") VALUES
	 (1,'spell1','spell_wizard_1lvl',1),
	 (2,'spell2','spell_wizard_5lvl',3),
	 (3,'spell3','spell_wizard_20lvl',9),
	 (4,'spell4','spell_cleric_1lvl',1),
	 (5,'spell5','spell_cleric_life_1lvl',1),
	 (6,'spell6','spell_wiz_cleric_5lvl',3),
	 (7,'spell7','spell_ranger_5lvl',2),
	 (8,'spell8','spell_ranger_9lvl',3);
INSERT INTO dl_spell_availability (spell_id,class_alias,subclass_alias) VALUES
	 (1,'wizard',NULL),
     (2,'wizard',NULL),
     (3,'wizard',NULL),
     (6,'wizard',NULL),
     (4,'cleric',NULL),
     (6,'cleric',NULL),
     (5,'cleric','life'),
     (7,'ranger',NULL),
     (8,'ranger',NULL);