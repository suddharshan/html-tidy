from tidylib import tidy_document
document="wer.xhmtl"
document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
    options={'numeric-entities':1})
print (document)
print (errors)

