import datetime


class Reply():

  def __init__(self,text, user, score=0, up_vote_list=[], down_vote_list=[]):
    self.text = text
    self.user = user
    self.score = score
    self.up_vote_list = up_vote_list
    self.down_vote_list = down_vote_list

  def update_reply(self, reply, updated_text):
    if reply in self.replies:
      text = updated_text
      print("New reply is: {}".format(updated_text))

  def delete_reply(self,reply):
    if reply in self.replies:
      self.replies.remove(reply)

  # from here, lets score the replies: UpVote and DownVote

  def score_reply(self):
    self.score = len(self.up_vote_list) - len(self.down_vote_list)
    print("The score is {}".format(self.score))

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

