from TDStoreTools import StorageManager
import TDFunctions as TDF

class Main:
	

	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def LoadPostEffect(self, bank, file):
		
		if file != '':
			run("parent().par.Bank"+str(bank)+"File = "+ file, fromOP=me)
		else:
			run("parent().par.Bank"+str(bank)+"File = '/Lib/base_addpost/base_emptypostfx.tox", fromOP=me)
		
		op('postfxbank'+str(bank)).par.Enableexternaltoxpulse.pulse()
