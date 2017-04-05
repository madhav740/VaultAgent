import UserIdManager
import sys
import os
import json
from CurlUtility import CurlUtility

class SecretManager:
	def __init__(self,secret_name):
		self.user_id = UserIdManager.UserIdManager().generate_user_id()
		self.app_id = os.environ.get('VAULT_APP_ID')
		self.vault_url = "" #url of vault server eg http://vault.myexample.com:8080
		self.secret_name = secret_name
	def authorize(self):
		login_credentials = None
		try:
			api_login_endpoint = self.vault_url+"/v1/auth/app-id/login"
			user_data = '{"app_id":"' + self.app_id + '", "user_id":"' + self.user_id +'"}'
			print api_login_endpoint
			login_credentials = CurlUtility().curl(api_login_endpoint, req_type="POST", data=user_data)
		except Exception,authorization_failed:
			print "Failed to authenticate With vault"
			print authorization_failed
		return login_credentials
	def get_secret(self):
		secret = None
		login_token = None
		header_info = dict()
		login_credentials = self.authorize()
		if login_credentials == None:
			return secret
		else:
			login_token = json.loads(login_credentials["content"])["auth"]["client_token"]
		header_info = dict()
		header_info['X-Vault-Token'] = login_token
		try:
			api_secret_endpoint = self.vault_url+"/v1/secret/"+self.secret_name
			secret = CurlUtility().curl(api_secret_endpoint, req_type="GET", headers = header_info)
		except Exception,secret_not_found:
			print "Failed to retrieve secret"
			print secret_not_found
		return secret
