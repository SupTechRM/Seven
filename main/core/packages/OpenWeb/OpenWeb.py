import webbrowser

def OpenWeb(put):
	link = put.split()
	if put.startswith('open '):
		try:
			webbrowser.open('https://www.' + link[1] + '.com')
		except Exception as e:
			print(str(e))