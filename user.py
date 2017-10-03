import datetime
from comment import Comment
from reply   import Reply
from image   import Image
from image_gallery import ImageGallery


class User():

  def __init__(self, username, password, date_created, profile_image, my_images = []):
    self.username = username
    self. password = password
    self.date_created = date_created
    self.profile_image = profile_image
    self.my_images = my_images


  def create_image(self):
    title = input("What's the image title? ")
    description = input("what the description? ")
    tags = input("What are the tags? ")
    image_gallery_id = input("What gallery? ")
    score = input("Score it: ")
    new_image = Image(title,description,tags,image_gallery_id,score)
    self.my_images.append(new_image)

  def read_images(self):
    for image in self.my_images:
      print(image.title)

  def delete_image(self,image):
    if image in self.my_images:
      self.my_images.remove(image)
      print("{} successfully delete".format(image.title))
    else:
      print("image does not exist to begin with")

  def update_image_title(self,image,new_title):
    if image in self.my_images:
      image.title = new_title
      print("New title is: {}".format(image.title))

  def update_image_description(self,image,new_description):
    if image in self.my_images:
      image.description = new_description
      print("New description is: {}".format(image.description))

  def image_search(self, title):
    for image in self.my_images:
      if title in image.title:
        print(image)




if __name__ == "__main__":

  sadiq = User(username = "sadiq", password = "password", date_created="", profile_image="sadiqimage",my_images = [])
  tomi = User(username = "tomi", password = "password", date_created="", profile_image="tomiimage",my_images = [])
  abdul = User(username = "abdul", password = "password", date_created="", profile_image="abdulimage",my_images = [])
  dare = User(username = "dare", password = "password", date_created="", profile_image="dareimage",my_images = [])
  charles = User(username = "charles", password = "password", date_created="", profile_image="charlesimage",my_images = [])

  cat_image = Image("cat","this is a cat","cat, internet, other","other gallery")
  dog_image = Image("dog","this is a cat","cat, internet, other","other gallery")
  rat_image = Image("rat","this is a cat","cat, internet, other","other gallery")
  fish_image = Image("fish","this is a cat","cat, internet, other","other gallery")


  sadiq.my_images.append(cat_image)
  sadiq.my_images.append(dog_image)
  sadiq.my_images.append(rat_image)
  sadiq.my_images.append(fish_image)

  # sadiq.create_image()
  sadiq.read_images()
  sadiq.delete_image(dog_image)
  sadiq.read_images()
  sadiq.update_image_title(rat_image,"danger mouse")
  sadiq.update_image_description(rat_image,"this is the new description. Means it was changed!")
  sadiq.read_images()
  sadiq.image_search(title='cat')

  cat_image.up_vote(sadiq)
  cat_image.up_vote(sadiq)
  cat_image.up_vote(dare)
  cat_image.score_image()
  cat_image.down_vote(sadiq)
  cat_image.down_vote(sadiq)
  cat_image.score_image()
  cat_image.up_vote(charles)
  cat_image.up_vote(abdul)
  cat_image.score_image()


