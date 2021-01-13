from .document import *

localization = "pytex/"

# Main file of PyTeX package

class Pytex():
	##############
	##   Code   ##
	##############

	package_init = ""
	head_code = ""
	document_code = ""


	#################
	##   Packages  ##
	#################

	packages_list = []

	def init():
		packages_list_file = open(localization + "packages/packages_list", "r")
		Pytex.packages_list = packages_list_file.read().split("\n")
		document.set_pytex(Pytex)
	
	def execute():
		output_code = ""
		output_code += "\document_class{" + document.document_class + "}\n \n"
		output_code += Pytex.package_init
		output_code += "\n \n"
		output_code += Pytex.head_code
		output_code += "\\begin{document}\n"
		output_code += Pytex.document_code
		output_code += "\\end{document}\n"
		print(output_code)



def include(package_name):
	if package_name in Pytex.packages_list:
		package_file = open(localization + "packages/" + package_name, "r")
		Pytex.package_init += package_file.read()
	else:
		Pytex.package_init += "\include{" + package_name + "}\n"

def tex(x):
	Pytex.document_code += x + "\n";

def execute():
	Pytex.execute()

