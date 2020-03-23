import rstr

from random import choice
pattern = '^ed2k://\\|file\\|([a-zA-Z\\+\\-\\_\\.]{1,})\\|([0-9]{1,})\\|([0-9a-fA-F]{32})\\|/'

error_start = '^(d2k://|e2k://|edk://|e2k/|edk//|d2k//)\\|file\\|([a-zA-Z+-_]{1,})\\|([0-9]{1,})\\|([0-9a-f]{32})\\|/'
error_type = '^ed2k://\\|(fil|fie|fle|ile)\\|([a-zA-Z+-_]{1,})\\|([0-9]{1,})\\|([0-9a-f]{32})\\|/'
error_name = '^ed2k://\\|file\\|([a-zA-Z+-_0-9]{1,})\\|([0-9]{1,})\\|([0-9a-f]{32})\\|/'
error_size = '^ed2k://\\|file\\|([a-zA-Z+-_0-9]{1,})\\|([0-9a-zA-Z]{1,})\\|([0-9a-f]{32})\\|/'
error_hash = '^ed2k://\\|file\\|([a-zA-Z+-_0-9]{1,})\\|([0-9a-zA-Z]{1,})\\|([0-9a-z]{,32})\\|/'
error_brackets = '^ed2k://(\\,\\.)file(\\,\\.)([a-zA-Z+-_]{1,})(\\.\\!)([0-9]{1,})(\\,\\!)([0-9a-f]{32})(\\,\\.\\!)/'


def generation():
	with open('genSTR.txt', 'w') as f:
		for _ in range(1000000):
			err = choice((error_start, error_brackets, error_type, error_name, error_hash, error_size))
			s = rstr.xeger(choice((pattern, err)))
			f.write(s + '\n')
	f.close()
