"""Cheap and simple API helper

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
with enhancements for attributes (c) peterfuchs1
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 2.0 $"
__date__ = "$Date: 2014/11/23 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

# While this is a good example script to teach about introspection,
# in real life it has been superceded by PyDoc, which is part of the
# standard library in Python 2.1 and later.
#
# Your IDE may already import the "help" function from pydoc
# automatically on startup; if not, do this:
#
# >>> from pydoc import help
#
# The help function in this module takes the object itself to get
# help on, but PyDoc can also take a string, like this:
#
# >>> help("string") # gets help on the string module
# >>> help("apihelper.help") # gets help on the function below
# >>> help() # enters an interactive help mode
#
# PyDoc can also act as an HTTP server to dynamically produce
# HTML-formatted documentation of any module in your path.
# That's wicked cool.  Read more about PyDoc here:
#   http://www.onlamp.com/pub/a/python/2001/04/18/pydoc.html


def info(obj, spacing=10, collapse=1, **kwargs):
	"""Print methods with doc strings and attributes.

	:param obj:	the object to introspect (modules, classes, lists, dictionaries and strings
	:param spacing:	default 10; how many spaces between elements and the description
	:param collapse:	default 1; shall we consume all white spaces ?
	:param attributes:	default False; shall we show all attributes too?
	"""
	# let's iterate through the keyword arguments
	attributes = False
	for k, v in kwargs.items():
		if k == 'attributes':
			if v:
				attributes = True
		else:
			raise TypeError('incompatible kw argument: (%s : %s) ' % (k, v))

	methodlist = [e for e in dir(obj) if callable(getattr(obj, e))]
	attributlist = [e for e in dir(obj) if not callable(getattr(obj, e))]
	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print("\n".ljust(spacing, '=') + "\nMethods:")
	print("\n".join(
		["%s %s" % (method.ljust(spacing),
			processFunc(str(getattr(obj, method).__doc__)))
			for method in methodlist])
	)
	if attributes:
		print("\n".ljust(spacing, '=')+"\nAttributes:")
		print("\n".join([a for a in attributlist]))
if __name__ == "__main__":
	print(help.__doc__)
