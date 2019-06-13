from tidylib import tidy_document
with open ("wer.xhtml") as document:
	document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
    		options={"force-output": 1})
	print (document)
	print(errors)
