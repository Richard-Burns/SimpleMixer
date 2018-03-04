import os
from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class Main:
	"""
	This is the main class for simple mixer. It handles the top level
	scripting bits and bobs.
	
	For more information about Simple Mixer email Richard Burns
	richard@richard-burns.com
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		return
		
	def Save(self):
		if ui.performMode == False:
			project.save(saveExternalToxs=True)
		return