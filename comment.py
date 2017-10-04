# class Comment():
#   def __init__(self,user, date_created, image_id, text, score):
#     self.user = user
#     self.date_created = date_created
#     self.image_id = image_id
#     self.text = text
#     self.score = score
from reply import Reply
import datetime

class Comment:
  def __init__(self, message, user, points=0, replies = [], timesent=None, up_vote_list = [], down_vote_list = []):
    self.message = message
    self.timesent = datetime.datetime.now()
    self.user = user
    self.points = points
    self.replies = []
    self.up_vote_list = up_vote_list
    self.down_vote_list = down_vote_list

  def edit_comment(self, updated_message):
    message = updated_message
    print("New reply is: {}".format(updated_message))

  def delete_reply(self,reply):
    if reply in self.replies:
      self.replies.remove(reply)


  def create_reply(self,text,user):
    new_reply = Reply(text=text,user=user)
    self.replies.append(new_reply)

  def count_replies(self):
    print("there are {} replies currently".format(len(self.replies)))

  def up_vote(self, user):
    if user in self.up_vote_list:
      print('You cannot up vote twice')
    elif user not in self.up_vote_list or user not in self.down_vote_list:
      self.up_vote_list.append(user)
    elif user in self.down_vote_list:
      self.down_vote_list.remove(user)
      self.up_vote_list.append(user)

  def down_vote(self, user):
    if user in self.down_vote_list:
      print('You cannot down vote twice')
    elif user not in self.down_vote_list or user not in self.up_vote_list:
      self.down_vote_list.append(user)
    elif user in self.up_vote_list:
      self.down_vote_list.remove(user)
      self.up_vote_list.append(user)

  def score_comment(self):
    self.score = len(self.up_vote_list) - len(self.down_vote_list)
    print("'{}' rating is {}".format(self.message ,self.score))


c1 = Comment("Hello World", "sadiq", 12)
# c1.edit_comment("Hi World")
# c1.delete_reply("Hi world")
# c1.create_reply("Andrew is handsome", sadiq)
# c1.create_reply("Andrew is handsome", sadiq)