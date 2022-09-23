import os, os.path, subprocess

images_path = 'static/img/'

def main():
    here = os.path.dirname(__file__)
    print(here)
    top = os.path.join(here, images_path)
    print(top)
    if not os.path.exists(top):
        print('ERROR: path', top, 'not found. make sure you are running this script from the right place')
        return
    for root, dirs, files in os.walk(top):
        for f in files:
            fext = f[-3:].lower()
            if fext == 'png' or fext == 'jpg':
                img = os.path.join(root, f)
                cmd = 'convert -interlace line ' + img + ' ' + img
                print(cmd)
                subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    main();
