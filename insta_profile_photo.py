#importing library
import instaloader

mod = instaloader.Instaloader()

a = input("Enter The User Name:")

mod.download_profile(a,profile_pic_only=True)