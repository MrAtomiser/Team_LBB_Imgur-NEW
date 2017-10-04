# class Comment():
#   def __init__(self,user, date_created, image_id, text, score):
#     self.user = user
#     self.date_created = date_created
#     self.image_id = image_id
#     self.text = text
#     self.score = score

import time

class Comment:
  def __init__(self, message, user, points, post_ID,replies = [], up_vote_list = [], down_vote_list = []):  # CommentID Needed?
    self.message = message
    self.timesent = time()
    self.user = user
    self.points = points
    self.replies = replies
  
  def edit_comment(self, old_comment, updated_comment):
        if old_comment in self.comments:
            updated_comment = old_comment
        print("New reply is: {}".format(updated_comment))

  def vote_comment(self):
    pass


  def delete_reply(self,reply):
    if reply in self.replies:
          self.replies.remove(reply)


  def create_reply(self):
      new_reply = Reply(input("Please enter comment: "))
      self.replies.append(new_reply)

  def up_vote_comment(self, user):
      if user in self.up_vote_list:
          print('You cannot up vote twice')

      elif user not in self.up_vote_list or user not in self.down_vote_list:
          self.up_vote_list.append(user)

      elif user in self.down_vote_list:
          self.down_vote_list.remove(user)

          self.up_vote_list.append(user)

  def down_vote_comment(self, user):
      if user in self.down_vote_list:
          print('You cannot down vote twice')
      elif user not in self.down_vote_list or user not in self.up_vote_list:
          self.down_vote_list.append(user)
      elif user in self.up_vote_list:
          self.down_vote_list.remove(user)
          self.up_vote_list.append(user)

