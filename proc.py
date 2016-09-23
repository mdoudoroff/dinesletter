#!/usr/bin/env python
# encoding: utf-8

import os

fns = u'''2016-annual-forecast.html
address-change.html
bio.html
bookstore.html
contact.html
faq-dines-letter.html
faq-iwb.html
faqs.html
gold-bug.html
high-states-sample.html
high-states.html
index.html
interim-warning-bulletin.html
mass-psychology.html
master-course.html
media.html
one-liners.html
subscriber-services.html
testimonials.html
the-dines-letter.html'''.split('\n')


linkMapping = {
u'http://dinesletter.com/index.php?option=com_content&view=article&id=10&Itemid=11': u'gold-bug.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=17&Itemid=28': u'subscriber-services.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=18&Itemid=30': u'media.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=19&Itemid=40': u'high-states.html',  # or secrets?
u'http://dinesletter.com/index.php?option=com_content&view=article&id=20&Itemid=41': u'mass-psychology.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=21&Itemid=42': u'master-course.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=22&Itemid=19': u'the-dines-letter.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=22&Itemid=32': u'the-dines-letter.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=23&Itemid=18': u'interim-warning-bulletin.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=23&Itemid=33': u'interim-warning-bulletin.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=29&Itemid=43': u'one-liners.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=31&Itemid=21': u'bio.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=31&Itemid=27': u'bio.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=59&Itemid=18': u'high-states-secrets.html',
u'http://dinesletter.com/index.php?option=com_content&view=category&layout=blog&id=1&Itemid=2': u'testimonials.html',
u'http://dinesletter.com/index.php?option=com_content&view=category&layout=blog&id=10&Itemid=20': u'faqs.html',
u'http://dinesletter.com/index.php?option=com_content&view=category&layout=blog&id=9&Itemid=23': u'contact.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=15&Itemid=55': u'faq-iwb.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=16&Itemid=54': u'faq-dines-letter.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=17&Itemid=28': u'subscriber-services.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=17&Itemid=28&showForm=1': u'subscriber-services.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=17&Itemid=28&showForm=1': u'subscriber-services.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=18&Itemid=30': u'media.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=19&Itemid=40': u'high-states.html',
u'http://dinesletter.com/index.php?option=com_content&view=article&id=55&Itemid=22': u'bookstore.html',
}


for fn in fns:

	assetsPath = fn.split('.html')[0]+'_files'

	# READ
	f = open(fn,'rb')
	h = f.read().decode("utf-8")
	f.close()



	# fix the css paths
	##h = h.replace('rel="stylesheet" href="./%s/' % assetsPath, 'rel="stylesheet" href="css/')






	# fix nav links
	# for key in linkMapping:
	# 	h = h.replace(key.replace("&","&amp;"),linkMapping[key])




	# rip out eMetrics
	# startIdx = h.find('<!-- WiredMinds eMetrics tracking with Enterprise Edition V5.4 START -->')
	# endIdx = h.find('<!-- WiredMinds eMetrics tracking with Enterprise Edition V5.4 END -->')+len('<!-- WiredMinds eMetrics tracking with Enterprise Edition V5.4 END -->')
	# if startIdx > -1:
	# 	h = h[:startIdx] + h[endIdx:]



	# rip out all javscript
	# while h.find('<script ')>-1:
	# 	startIdx = h.find('<script ')
	# 	endIdx = h.find('</script>',startIdx) + len('</script>')
	# 	if startIdx > -1 and endIdx > -1:
	# 		h = h[:startIdx] + h[endIdx:]
	# 	else:
	# 		break



	# fix all the gfx
	h = h.replace('./%s/' % assetsPath,'images/' )




	# WRITE
	# f = open(fn,'wb')
	# h = f.write(h.encode('utf-8'))
	# f.close()

# links = set(shit)
# for l in sorted(links):
# 	print l
