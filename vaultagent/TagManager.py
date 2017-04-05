import boto.utils
import boto.ec2

class TagManager:
	def __init__(self):
		self.tag_id = None
	def get_tagid(self):
		region=boto.utils.get_instance_metadata()['placement']['availability-zone']
		instance_id = boto.utils.get_instance_metadata()['instance-id']
		conn=boto.ec2.connect_to_region(region[0:-1])
		reservations = conn.get_all_instances(instance_ids=[instance_id])
		instance = reservations[0].instances[0]
		tags = instance.tags
		for items in tags:
			self.tag_id += tags[items]
		return self.tag_id

