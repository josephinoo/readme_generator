from PIL import Image,ImageFont,ImageDraw
1902 × 461

class Genarator:
    def __init__(self, user,repositorie):
        self.user=user
        self.repositorie=repositorie

    def build_header(user,repositorie,name="logo.png"):
        return "![header](https://raw.githubusercontent.com/"+user+"/"+repositorie+"/master/images/"+name+")"
    
    def create_readme():
        file_readme=open("README.md","a")
        file_readme.close()
    
    def title(self,title):
        file_readme=open("README.md","a")
        file_readme.write("# "+title)
        file_readme.close()

    def description(self,description):
        file_readme=open("README.md","a")
        file_readme.write(description)
        file_readme.close()

        
    def add_image(user,repositorie,name="logo.png"):
        file_readme=open("README.md","a")
        file_readme.write("![header](https://raw.githubusercontent.com/"+user+"/"+repositorie+"/master/images/"+name+")")
        file_readme.close()
    def add_header_image(self,name_project):
        img=Image.new('RGBA',(1902 , 461),'white')
        font=ImageFont.truetype("arial.tff",100)
        w,h=font.getsize(name_project)
        draw=ImageDraw.Draw(img)
        draw.text((1902-w)/2,(461-h)/2,name_project,font=font,fill="black")

