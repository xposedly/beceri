window = {
	"name" : "SelectSkill",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH / 2 - 95,
	"y" : SCREEN_HEIGHT / 2 - 88,

	"width" : 190,
	"height" : 175,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 190,
			"height" : 175,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 5,
					"y" : 6,

					"width" : 190-12,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : "Skill Penceresi", 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "Skill_1",
					"type" : "button",

					"x" : 20,
					"y" : 40,

					"default_image" : "d:/ymir work/ui/BeceriTahtasi/Yakin1.png",
					"over_image" : "d:/ymir work/ui/BeceriTahtasi/Yakin2.png",
					"down_image" : "d:/ymir work/ui/BeceriTahtasi/Yakin1.png",
				},

				{
					"name" : "Skill_2",
					"type" : "button",

					"x" : 20,
					"y" : 80,

					"default_image" : "d:/ymir work/ui/BeceriTahtasi/Uzak1.png",
					"over_image" : "d:/ymir work/ui/BeceriTahtasi/Uzak2.png",
					"down_image" : "d:/ymir work/ui/BeceriTahtasi/Uzak1.png",
				},

				{
					"name" : "Cancel",
					"type" : "button",

					"x" : 20,
					"y" : 120,

					"default_image" : "d:/ymir work/ui/BeceriTahtasi/Sonra1.png",
					"over_image" : "d:/ymir work/ui/BeceriTahtasi/Sonra2.png",
					"down_image" : "d:/ymir work/ui/BeceriTahtasi/Sonra1.png",
				},
			),
		},
	),
}
