import ui
import item
import net
import mouseModule
import player
import constInfo

class BeceriEkrani(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Ekran()

	def __Ekran(self):
		KygnPyYukle = ui.PythonScriptLoader()
		KygnPyYukle.LoadScriptFile(self, "UIScript/beceriekrani.py")

		KygnObject = self.GetChild
		self.titleBar = KygnObject("titlebar")
		self.Skill_1 = KygnObject("Skill_1")
		self.Skill_2 = KygnObject("Skill_2")
		self.Cancel = KygnObject("Cancel")


		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.Skill_1.SetEvent(lambda arg=1: self.ButtonEvent(arg))
		self.Skill_2.SetEvent(lambda arg=2: self.ButtonEvent(arg))
		self.Cancel.SetEvent(ui.__mem_func__(self.Close))


	def ButtonEvent(self, arg):
		net.SendChatPacket("/select_skill_group %d" % int(arg))
		self.Close()

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Open(self, job):
		if int(job) == 0:
			self.ButtonImage(self.Skill_1, "d:/ymir work/ui/BeceriTahtasi/Bedensel1.png", "d:/ymir work/ui/BeceriTahtasi/Bedensel2.png", "d:/ymir work/ui/BeceriTahtasi/Bedensel1.png")
			self.ButtonImage(self.Skill_2, "d:/ymir work/ui/BeceriTahtasi/Zihinsel1.png", "d:/ymir work/ui/BeceriTahtasi/Zihinsel2.png", "d:/ymir work/ui/BeceriTahtasi/Zihinsel1.png")
		elif int(job) == 1:
			self.ButtonImage(self.Skill_1, "d:/ymir work/ui/BeceriTahtasi/Yakin1.png", "d:/ymir work/ui/BeceriTahtasi/Yakin2.png", "d:/ymir work/ui/BeceriTahtasi/Yakin1.png")
			self.ButtonImage(self.Skill_2, "d:/ymir work/ui/BeceriTahtasi/Uzak1.png", "d:/ymir work/ui/BeceriTahtasi/Uzak2.png", "d:/ymir work/ui/BeceriTahtasi/Uzak1.png")
		elif int(job) == 2:
			self.ButtonImage(self.Skill_1, "d:/ymir work/ui/BeceriTahtasi/BuyuluSilah1.png", "d:/ymir work/ui/BeceriTahtasi/BuyuluSilah2.png", "d:/ymir work/ui/BeceriTahtasi/BuyuluSilah1.png")
			self.ButtonImage(self.Skill_2, "d:/ymir work/ui/BeceriTahtasi/KaraBuyu1.png", "d:/ymir work/ui/BeceriTahtasi/KaraBuyu2.png", "d:/ymir work/ui/BeceriTahtasi/KaraBuyu1.png")
		elif int(job) == 3:
			self.ButtonImage(self.Skill_1, "d:/ymir work/ui/BeceriTahtasi/Ejderha1.png", "d:/ymir work/ui/BeceriTahtasi/Ejderha2.png", "d:/ymir work/ui/BeceriTahtasi/Ejderha1.png")
			self.ButtonImage(self.Skill_2, "d:/ymir work/ui/BeceriTahtasi/Iyilestirme1.png", "d:/ymir work/ui/BeceriTahtasi/Iyilestirme2.png", "d:/ymir work/ui/BeceriTahtasi/Iyilestirme1.png")
		self.Show()

	def ButtonImage(self, button, UpVisual, OverVisual, DownVisual):
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Close(self):
		self.Hide()
