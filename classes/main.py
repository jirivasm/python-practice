from user import User
from post import Post



user1 =User("nacho@gmail.com", "Nacho Rivas", "pw1", "job title")
user1.get_user_info()
user1.change_job_title("unemployed")
user1.get_user_info()

post1 =Post("message",user1.name)
post1.get_post_info()