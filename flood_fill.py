import matplotlib.pyplot as plt

def floodfill(picture, start_x: int = 0, start_y: int = 0):
    if start_x < 0 or start_y < 0:
        return picture
    try:
        current_pixel = picture[start_x][start_y]
    except IndexError:
        return picture
    if current_pixel == 2 or current_pixel == 0:
        return picture
    if current_pixel == 1:
        picture[start_x][start_y] = 2
        picture = floodfill(picture, start_x + 1, start_y)
        picture = floodfill(picture, start_x - 1, start_y)
        picture = floodfill(picture, start_x, start_y + 1)
        picture = floodfill(picture, start_x, start_y - 1)
    return picture

def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(50)
    plt.clf()


if __name__ == "__main__":
    main()

