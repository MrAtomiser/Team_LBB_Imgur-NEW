import smtplib
import hashlib
import datetime
from comment import Comment
from reply  import Reply
from image  import Image
from image_gallery import ImageGallery


class User():

    def __init__(self, username, password, profile_image, email, date_created=None, my_images = [],
                 my_comments=[]):
        self.username = username
        self.__password = hashlib.md5('password'.encode('utf-8')).hexdigest()
        self.email = email
        self.date_created = datetime.datetime.now()
        self.profile_image = profile_image
        self.my_images = my_images
        print("{}, You have successfully signed up: {}".format(self.username, self.date_created))
        # self.send_email()

    def send_email(self):
        # Sending email to user after account is created
        gmail_user = 'draogtech@gmail.com'
        gmail_pwd = input("Enter your password: ")
        FROM = 'draogtech@gmail.com'
        TO = self.email
        SUBJECT = 'Welcome to Imgur'
        TEXT = 'Hello {}, Your account has been successfully created. Welcome to a new experience on Imgur'\
            .format(self.username)

        # P actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
           """ % (FROM, "".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except Exception as e:
            print(e)

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

    def get_password(self):
        return self.__password


if __name__ == "__main__":
    # User creation and Sending successful email after account creation
    sadiq = User(username = "sadiq", password = hashlib.md5("password".encode('utf-8')).hexdigest(),
                 email='sokocha@gmail.com', profile_image="sadiqimage",my_images = [])
    tomi = User(username = "tomi", password = hashlib.md5("password".encode('utf-8')).hexdigest(),
                email='oluwatomisin.adeshiyan@meltwater.org', profile_image="tomiimage",my_images = [])
    abdul = User(username = "abdul", password = hashlib.md5("password".encode('utf-8')).hexdigest(),
                 email='abdulquadri.sotomiwa@meltwater.org', profile_image="abdulimage",my_images = [])
    dare = User(username = "dare", password = hashlib.md5("password".encode('utf-8')).hexdigest(),
                email='draogtech@gmail.com', profile_image="dareimage",my_images = [])
    charles = User(username = "charles", password = hashlib.md5("password".encode('utf-8')).hexdigest(),
                   email='charles.thompson@meltwater.org',profile_image="charlesimage",my_images = [])

    cat_image = Image("cat","this is a cat","cat, internet, other","other gallery")
    dog_image = Image("dog","this is a cat","cat, internet, other","other gallery")
    rat_image = Image("rat","this is a cat","cat, internet, other","other gallery")
    fish_image = Image("fish","this is a cat","cat, internet, other","other gallery")

    fish_image.create_comment(sadiq,"h")


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
    cat_image.score_image()
    cat_image.up_vote(charles)
    cat_image.up_vote(abdul)
    cat_image.score_image()

    cat_image_comment = Comment("abcde", cat_image, "i love things", "4")
    dog_image_comment = Comment("abcde", dog_image, "i love things", "4")
    rat_image_comment = Comment("abcde", rat_image, "i love things", "4")
    fish_image_comment = Comment("abcde", fish_image, "i love things", "4")

    cat_image_comment.create_reply('heeeeeee',sadiq)
    cat_image_comment.edit_comment("yoooooooo")
    cat_image_comment.score_comment()
    cat_image_comment.up_vote(sadiq)
    cat_image_comment.score_comment()
    cat_image_comment.down_vote(sadiq)
    cat_image_comment.down_vote(sadiq)
    cat_image_comment.score_comment()

    a = cat_image_comment.create_reply(text="tefsfsfd",user=sadiq)
    # a.count_replies()