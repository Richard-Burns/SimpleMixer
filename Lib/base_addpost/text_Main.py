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
		cmd = "op('constant_fadebanks').par.value"+str(bank-1)+" = 1"
		run(cmd, fromOP=me)
		args = [ bank, filepath]
		run("args[0](args[1],args[2])", self.Delayassign, bank, filepath, fromOP=me, delayMilliSeconds=1000)
		
		return
		
	def Deassignbank(self,bank):
		#print("op(\'constant_fadebanks\').par.value1 = -1")
		cmd = "op('constant_fadebanks').par.value"+str(bank-1)+" = 1"
		run(cmd, fromOP=me)
		run("args[0]("+str(bank)+")", self.Delaydeassign, fromOP=me, delayMilliSeconds=1000)
		return
		
	def Delaydeassign(self,bank):
		o = op("postfxbank"+str(bank))
		o.par.externaltox = "Lib/base_addpost/base_emptypostfx.tox"
		o.par.reinitnet.pulse()
		#o.outputConnectors[0].connect(op('switch'+str(bank)))
		return
		
	def Delayassign(self, bank, filepath):
		o = op("postfxbank"+str(bank))
		o.par.externaltox = filepath
		o.par.reinitnet.pulse()
		#o.outputConnectors[0].connect(op('switch'+str(bank)))
		cmd = "op('constant_fadebanks').par.value"+str(bank-1)+" = -1"
		run(cmd, fromOP=me)
		return