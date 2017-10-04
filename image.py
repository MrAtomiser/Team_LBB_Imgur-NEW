from comment import Comment
# test
class Image():

    def __init__(self,title, description, tags, image_gallery_id, score = 0, up_vote_list = [], down_vote_list = [], comments=[]):
        self.title = title
        self.description = description
        self.tags = tags
        self.image_gallery_id = image_gallery_id
        self.score = score
        self.up_vote_list = up_vote_list
        self.down_vote_list = down_vote_list
        self.comments = comments
        print("Image: {} successfully uploaded".format(title))

    def create_comment(self,user,comment_text):
        new_comment = Comment(message=comment_text,user=user)
        self.comments.append(new_comment)
        # user.my_comments.append(new_comment)
        print(new_comment)

    def delete_comment(self,user,comment):
        if comment in self.comments and user in user.my_comments:
            self.comments.remove(user)
            # user.my_comments.remove(user)

    def score_image(self):
        self.score = len(self.up_vote_list) - len(self.down_vote_list)
        print("{} rating is {}".format(self.title ,self.score))

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










