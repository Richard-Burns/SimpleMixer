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
		
	def Setbank(self, bank, tox, store=parent.sm.op('base_tox')):
		# bank can be:
		# "topleft", "topright", "bottomleft", "bottomright"
		# tox is the name of the tox file which should be
		# located in self.toxStore. The top that is referenced
		# will be called out1. So self.toxStore.op(tox+'/out1')
		
		self.toxStore = store
		
		try:
			self.toxStore.op(tox).Reset()
		except:
			#no reset function
			pass
		
	
		if bank == "topleft":
			curfade = parent().par.Bankfades1
			parent().par.Topleftbank = self.toxStore.op(tox)
			if curfade == 1:
				op('select_'+bank+'a').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades1 = -1
			else:
				op('select_'+bank+'b').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades1 = 1
				
		if bank == "topright":
			parent().par.Toprightbank = self.toxStore.op(tox)
			curfade = parent().par.Bankfades3
			if curfade == 1:
				op('select_'+bank+'a').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades3 = -1
			else:
				op('select_'+bank+'b').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades3 = 1
		
		if bank == "bottomleft":
			parent().par.Bottomleftbank = self.toxStore.op(tox)
			curfade = parent().par.Bankfades2
			if curfade == 1:
				op('select_'+bank+'a').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades2 = -1
			else:
				op('select_'+bank+'b').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades2 = 1
		
		if bank == "bottomright":
			parent().par.Bottomrightbank = self.toxStore.op(tox)
			curfade = parent().par.Bankfades4
			if curfade == 1:
				op('select_'+bank+'a').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades4 = -1
			else:
				op('select_'+bank+'b').par.top = self.toxStore.op(tox+'/out1')
				parent().par.Bankfades4 = 1
		
		v = int(op.gui.op('container_show/container_userpanel/constant1')['v1'])
		op.gui.op('container_show/container_userpanel').UpdatePanels(v)
		
		
		return
		
	def Unload(self, bank, side):
		# bank can be;
		# "topleft", "topright", "bottomleft", "bottomright"
		# side can be:
		# "a" or "b"
	
		op('select_'+bank+side).par.top = ""
		
		return
	
	def SwapBankOrder(self, bank, side):

		return