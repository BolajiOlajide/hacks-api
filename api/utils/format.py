def format_tag(tag):
	return {
		'tag': tag.tag
	}

def format_hack(hack):
	return {
		'hack': {
			'id': hack.hackId,
			'name': hack.name,
			'description': hack.description,
			'image_url': hack.image_url,
			'location': {
				'location': hack.location.location,
				'country': hack.location.country
			},
			'tag': [format_tag(tag) for tag in hack.tag.select_related()]
		}
	}


def format_hacks(hacks):
	return [format_hack(hack) for hack in hacks]
