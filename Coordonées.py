class Coordonnées:
	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon

	def recup_url_image():
		S = request_Session()

		URL = "https://en.wikipedia.org/w/api.php"

		TITLE = 'Wikimedia Foundation'

		PARAMS = {
    		'action':"query",
    		'prop':"coordinates",
    		'titles': TITLE,
    		'format':"json"
				}