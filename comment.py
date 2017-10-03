# class Comment():
#   def __init__(self,user, date_created, image_id, text, score):
#     self.user = user
#     self.date_created = date_created
#     self.image_id = image_id
#     self.text = text
#     self.score = score

import time

class Comment:
  def __init__(self, message, sender_ID, points, post_ID,replies=[], comments=[]):  # CommentID Needed?
    self.message = message
    self.timesent = time()
    self.sender_ID = sender_ID
    self.points = points
    self.post_ID = post_ID
    self.replies = replies
    self.comments = comments

  def edit_comment(self, old_comment, updated_comment):
        if old_comment in self.comments:
            updated_comment = old_comment
        print("New reply is: {}".format(updated_comment))


  def vote_comment(self):
    pass


  def delete_comment(self,r_comment):
    if r_comment in self.comments:
          self.comments.remove(r_comment)

  def send_comment(self):
      self.message.append(input("Pls enter your comment: "))

