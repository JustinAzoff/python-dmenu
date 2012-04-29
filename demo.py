from dmenu import dmenu
import os
def demo():
    choice = "/"
    while choice:
        if not os.path.isdir(choice):
            return os.path.join(os.getcwd(), choice)
        os.chdir(choice)
        paths = [".."] + sorted(os.listdir("."))
        choice = dmenu(paths, lines=10, bottom=True, prompt="Browse..")

if __name__ == "__main__":
    print "Selected", demo()
