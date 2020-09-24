


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