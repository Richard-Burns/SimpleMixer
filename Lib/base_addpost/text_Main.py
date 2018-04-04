"""
Help: search "Extensions" in wiki
"""

class Main:
	"""
	Main description
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
	
	def Assignbank(self, bank, filepath):
		o = op("postfxbank"+str(bank))
		o.par.externaltox = filepath
		o.par.reinitnet.pulse()
		
		return
		
	def Deassignbank(self,bank):
		o = op("postfxbank"+str(bank))
		o.par.externaltox = "Lib/base_addpost/base_emptypostfx.tox"
		o.par.reinitnet.pulse()
		return