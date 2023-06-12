-----------------------------------------------------------------------------------------------------------------------
# �mportlara Ekle:
import uibeceriekrani
-----------------------------------------------------------------------------------------------------------------------
# Arat:
		self.wndQuestWindow = {}
# Üstüne Ekle:
		self.wndBeceriEkrani = None
-----------------------------------------------------------------------------------------------------------------------
# Arat:
		self.wndChatLog = wndChatLog
# Altına Ekle:
		self.wndBeceriEkrani = uibeceriekrani.BeceriEkrani()
-----------------------------------------------------------------------------------------------------------------------
# Arat:
		del self.mallPageDlg
# Altına Ekle:
		del self.wndBeceriEkrani
-----------------------------------------------------------------------------------------------------------------------
# Arat:
	def BUILD_OnMouseLeftButtonUp(self):
# Üstüne Ekle:
	def OpenSelectSkillWindow(self, job):
		if self.wndBeceriEkrani:
			self.wndBeceriEkrani.Open(job)
-----------------------------------------------------------------------------------------------------------------------
