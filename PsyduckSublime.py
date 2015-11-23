import os
import sublime
import sublime_plugin


PSYDUCK = ''

with open(os.path.dirname(os.path.realpath(__file__)) + '/psyduck', 'r') as psyduck:
	PSYDUCK = psyduck.read()


class PsyduckCommand(sublime_plugin.TextCommand):
	def run(self, view, **kwargs):
		sels = self.view.sel()
		for region in sels:
			self.view.insert(view, region.begin(), PSYDUCK)
