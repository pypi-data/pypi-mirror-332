# __all__ declared at the module's end


from .github_api_error import\
	GitHubApiError


_KEY_DOC_URL = "documentation_url"
_KEY_MESSAGE = "message"
_KEY_STATUS = "status"


def detect_github_api_error(request_url, api_response_data):
	"""
	This function examines data from the GitHub API and raises a GitHubApiError
	if it is the result of an erroneous request. The request is erroneous if
	the data is a dictionary whose keys are "message", "documentation_url" and
	"status".

	Args:
		request_url (str): the URL of the request for the given data.
		api_response_data: the object returned by the parsing of the response's
			content, which is in JSON.

	Raises:
		GitHubApiError: if the examined data is the result of an erroenous
			request.
	"""
	if isinstance(api_response_data, dict):
		message = api_response_data.get(_KEY_MESSAGE)
		doc_url = api_response_data.get(_KEY_DOC_URL)
		status = api_response_data.get(_KEY_STATUS)

		if message is not None and doc_url is not None and status is not None:
			raise GitHubApiError(message, doc_url, status, request_url)


__all__ = [detect_github_api_error.__name__]
