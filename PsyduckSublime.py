import sublime
import sublime_plugin

PSYDUCK = '''
//                    // //  //
//         __    ____||_//  //
//       _/__--~~        ~~~-_
//      /  /___        ___    \
//     /  /(  +)      ( + )    |
//    /  |  ~~~    __  ~~~   _/\/|
//   |    \  ___.-~  ~-.___  \   /
//    \    \(     ` '      ~~)|   \
//     \     )              / |    \
//      \/   /              \ |    |
//      /   |               | |    |
//     |    /               |  \__/
//     |    \_            _/      |    ___
//     \      ~----...---~       /_.-~~ _/
//      \_                      |    _-~
//        \                    /  _-~
//         ~-.__             _/--~
//        _.-~  ~~~-----~~~~~
//       ~-.-. _-~     /_ ._ \
//            ~       ~  ~  ~-
'''

class PsyduckCommand(sublime_plugin.TextCommand):
	def run(self, view, **kwargs):
		sels = self.view.sel()
		for region in sels:
			self.view.insert(view, region.begin(), PSYDUCK)
