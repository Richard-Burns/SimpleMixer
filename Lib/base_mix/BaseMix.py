"""
Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class BaseMix:
	"""
	BaseMix description
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.toxStore = parent.sm.op('base_tox')
		
	def SetBank(self, bank, tox):
		# bank can be:
		# "topleft", "topright", "bottomleft", "bottomright"
		# tox is the name of the tox file which should be
		# located in op.TOX
		
	
		if bank == "topleft":
			curfade = parent().par.Bankfades1
			parent().par.Topleftbank = op.TOX.op(tox)
			if curfade == 1:
				op('select_'+bank+'a').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades1 = -1
			else:
				op('select_'+bank+'b').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades1 = 1
				
		if bank == "topright":
			parent().par.Toprightbank = op.TOX.op(tox)
			curfade = parent().par.Bankfades3
			if curfade == 1:
				op('select_'+bank+'a').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades3 = -1
			else:
				op('select_'+bank+'b').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades3 = 1
		
		if bank == "bottomleft":
			parent().par.Bottomleftbank = op.TOX.op(tox)
			curfade = parent().par.Bankfades2
			if curfade == 1:
				op('select_'+bank+'a').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades2 = -1
			else:
				op('select_'+bank+'b').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades2 = 1
		
		if bank == "bottomright":
			parent().par.Bottomrightbank = op.TOX.op(tox)
			curfade = parent().par.Bankfades4
			if curfade == 1:
				op('select_'+bank+'a').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades4 = -1
			else:
				op('select_'+bank+'b').par.top = op.TOX.op(tox+'/out1')
				parent().par.Bankfades4 = 1

		
		
		return
		
	def Unload(self, bank, side):
		# bank can be;
		# "topleft", "topright", "bottomleft", "bottomright"
		# side can be:
		# "a" or "b"
	
		op('select_'+bank+side).par.top = ""
		
		return