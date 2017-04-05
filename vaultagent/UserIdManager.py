#!/usr/bin/python
import requests
import boto.utils
import hashlib, uuid

import TagManager
class UserIdManager:
	def __init__(self):
		self.salt = "9a77a433e1ec4e918992cabb5566a926"
		self.user_tag = None
		self.user_id = ""
	def generate_user_id(self):
		tag_manager = TagManager.TagManager()
		self.user_tag = tag_manager.get_tagid()
		self.user_id = hashlib.sha512(self.user_tag + self.salt).hexdigest()
		return self.user_id

