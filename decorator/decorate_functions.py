__author__ = 'uhs374h'
"""
Decorator in python form use a
easy to use syntax with the @ annotation:

* The first function gets the parameter of the decorated annotation.
* The second function gets the name of the decorated function.
* The third function gets the parameter of the decorated function.
"""


def tags(tag_name):
	def tags_decorator(functionname):
		def func_wrapper(parameter):
			"""
			wrapper can only take a function with one parameter
			"""
			return "<{0}>{1}</{0}>".format(tag_name, functionname(parameter))
		return func_wrapper
	return tags_decorator


def tag_right(tag_name):
	def tags_decorator(functionname):
		def func_wrapper(*args, **kwargs):
			"""
			wrapper can take a unlimited number of parameter
			"""
			return "{1}<{0}/>".format(tag_name, functionname(*args, **kwargs))
		return func_wrapper
	return tags_decorator


@tags("div")
@tags("p")
@tags("strong")
@tag_right("br")
def say_hello(name):
	return "Hello %s!" % name


def main():
	print(say_hello("John"))
	print(say_hello("Franz"))
	print(say_hello(""))

"""
<div><p><strong>Hello John!<br/></strong></p></div>
<div><p><strong>Hello Franz!<br/></strong></p></div>
<div><p><strong>Hello !<br/></strong></p></div>
"""

if __name__ == "__main__":
	main()