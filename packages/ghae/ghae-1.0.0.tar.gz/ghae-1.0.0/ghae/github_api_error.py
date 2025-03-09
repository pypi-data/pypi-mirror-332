# __all__ declared at the module's end


class GitHubApiError(Exception):
	"""
	This exception can be raised when a response from the GitHub API indicates
	that the request is erroneous.
	"""

	def __init__(self, message, doc_url, status, req_url):
		"""
		The constructor needs the data relevant to the request's failure. The
		response to an erroneous request contains an error message, the URL to
		the error's documentation and a status code.

		Args:
			message (str): the error message.
			doc_url (str): the URL to the error's documentation.
			status (str): the response's status code.
			req_url (str): the erroneous request's URL.
		"""
		self._message = message
		self._doc_url = doc_url
		self._status = status
		self._req_url = req_url

	def __repr__(self):
		return self.__class__.__name__\
			+ f"('{self._message}', '{self._doc_url}', "\
			+ f"'{self._status}', '{self._req_url}')"

	def __str__(self):
		return f"[{self._req_url}] {self._status}: {self._message}."\
			+ f" Documentation: {self._doc_url}"

	@property
	def message(self):
		"""
		str: the error message.
		"""
		return self._message

	@property
	def doc_url(self):
		"""
		str: the URL to the error's documentation.
		"""
		return self._doc_url

	@property
	def status(self):
		"""
		str: the response's status code.
		"""
		return self._status

	@property
	def req_url(self):
		"""
		str: the erroneous request's URL.
		"""
		return self._req_url


__all__ = [GitHubApiError.__name__]
