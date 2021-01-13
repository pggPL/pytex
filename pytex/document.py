from .__init__ import *

class document():
	####################
	##   Properties   ##
	####################
	document_class = "article"
	title = ""
	author = ""
	date = ""

	def set_pytex(pytex):
		document.pytex = pytex

def make_title():
	document.pytex.document_code += "\maketitle" + "\n";

