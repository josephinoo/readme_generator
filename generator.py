



def build_header(user,repositorie,name="logo.png"):
    return "![header](https://raw.githubusercontent.com/"+user+"/"+repositorie+"/master/images/"+name+")"
def create_readme(add):
    file_readme=open("README.md","a")
    file_readme.write(add)
    file_readme.close