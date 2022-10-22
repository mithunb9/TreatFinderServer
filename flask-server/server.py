from PIL import Image


def main():
    pass

if (__name__ == '__main__'):
    main()

def fetch_map():
    img = Image.new('RGB', (60, 30), color = 'red')
    img.save('map.png')