-----------------------------------------------------------------------------------------------------------------------
# Arat:
			"WarUC"					: self.__GuildWar_UpdateMemberCount,
# Altına Ekle:
			###--5LEVEL-BECERI--###
			"open_select_skill_window"						: self.open_select_skill_window,
			###--5LEVEL-BECERI--###
-----------------------------------------------------------------------------------------------------------------------
# En Alta Ekle:
	def open_select_skill_window(self, job):
		# if app.WJ_SECURITY_SYSTEM and player.IsSecurityActivate():## Güvenlik Sistemi Kullanıyorsanız Aktif Edin !!!
			# return
		if self.interface:
			self.interface.OpenSelectSkillWindow(job)
-----------------------------------------------------------------------------------------------------------------------