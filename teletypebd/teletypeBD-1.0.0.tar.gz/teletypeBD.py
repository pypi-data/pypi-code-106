import requests
import json
import random

class Client:
	def __init__(self, tokens, group_id):
		self.api = random.choice(tokens)
		self.group_id = group_id

	def insert_one(self, post: dict):
		if self.find_one({"_id": post["_id"]}) != 0:
			raise TypeError(f"id <{post['_id']}> уже записан в базе")

		requests.get(self.api.replace("{{method}}", "wall.post"), params={
			"owner_id": self.group_id,
			"message": str(post)
		})

	def find_one(self, post: dict):
		response = requests.get(self.api.replace("{{method}}", "wall.get"), params={
			"owner_id": self.group_id
		})

		check = 0

		for key in response.json()["response"]["items"]:
			posts = json.loads(key["text"].replace("'", "\""))

			if posts["_id"] == post["_id"]:
				check = posts
				break

		return check

	def update(self, post: dict, update: dict):
		response = requests.get(self.api.replace("{{method}}", "wall.get"), params={
			"owner_id": self.group_id
		})

		for key in response.json()["response"]["items"]:
			posts = json.loads(key["text"].replace("'", "\""))

			if posts["_id"] == post["_id"]:
				for modificator in update:
					if modificator in ["$set", "$inc"] and len(update[modificator]) == 1:
						for keyPosts in update[modificator]:
							if keyPosts in posts:
								if modificator == "$set":
									posts[keyPosts] = update[modificator][keyPosts]
								elif modificator == "$inc":
									posts[keyPosts] += update[modificator][keyPosts]
					else:
						raise TypeError(f"Неизвестный модификатор <{modificator}>")

				response = requests.get(self.api.replace("{{method}}", "wall.edit"), params={
					"owner_id": self.group_id,
					"post_id": key['id'],
					"message": str(posts)
				})
