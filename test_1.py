from pytex import *

def test1():
	Pytex.init()

	## code
	include("standard")

	tex("aaa")
	tex(r"b\u\{a\}bbbb")

	document.document_class = "beamer"

	make_title()

	execute()

test1()