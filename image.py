class Image():
  def __init__(self,title, description, tags, image_gallery_id, score=0):
    self.title = title
    self.description = description
    self.tags = tags
    self.image_gallery_id = image_gallery_id
    self.score = score
    print("Image: {} successfully uploaded".format(title))

  # def vote(self, choice):
  #   if choice == +1:
  #     self.score += choice
  #
  #   elif choice == -1:
  #     self.score -= choice

  def up_vote(self):
    self.score += 1
    print(self.score)

  def down_vote(self):
    self.score -= 1
    print(self.score)






