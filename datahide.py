class JustCounter:
	secretcount = 0
	def count(self):
		self.secretcount += 1
		print self.secretcount
counter = JustCounter()
counter.count()
counter.count()
counter.count()
print counter.secretcount
