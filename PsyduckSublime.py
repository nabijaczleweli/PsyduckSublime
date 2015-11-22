import os
import sublime
import sublime_plugin


def load_psyduck():
	global PSYDUCK
	if not PSYDUCK:
		with open(os.path.dirname(os.path.realpath(__file__)) + '/psyduck', 'r') as psyduck:
			PSYDUCK = psyduck.read()


class PsyduckCommand(sublime_plugin.TextCommand):
	def run(self, view, **kwargs):
		load_psyduck()
		sels = self.view.sel()
		for region in sels:
			self.view.insert(view, region.begin(), PSYDUCK)
