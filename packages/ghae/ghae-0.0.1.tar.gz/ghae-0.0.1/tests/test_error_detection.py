import pytest

import json
from pathlib import Path

from syspathmodif import\
	sp_append,\
	sp_remove


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"

_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parent

_FAKE_URL = "https://api.github.com/repos/nobody/nothing"


sp_append(_REPO_ROOT)
from ghae import\
	GitHubApiError,\
	detect_github_api_error
sp_remove(_REPO_ROOT)


def _load_whole_json_file(json_path):
	with json_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as json_file:
		return json.load(json_file)


def test_error_detection_valid_request():
	response_data = _load_whole_json_file(
		_LOCAL_DIR/"response_to_valid_request.json")

	# Success if GitHubApiError is not raised.
	detect_github_api_error(_FAKE_URL, response_data)


def test_error_detection_erroneous_request():
	response_data = _load_whole_json_file(
		_LOCAL_DIR/"response_to_erroneous_request.json")

	with pytest.raises(GitHubApiError) as except_info:
		detect_github_api_error(_FAKE_URL, response_data)

	# The GitHubApiError instance
	e = except_info.value
	assert e.message == "Not Found"
	assert e.doc_url\
		== "https://docs.github.com/rest/repos/repos#get-a-repository"
	assert e.status == "404"
	assert e.req_url == "https://api.github.com/repos/nobody/nothing"
