import numpy as np
import matplotlib.pyplot as plt
from Tkinter import Tk
from tkFileDialog import askopenfilename
from textwrap import wrap

def view_toronto_mnist_tensor(toronto_tensor, vid_id=None, delay=None, prompt_keypress=False, titles=None, gen_seeds=None):
    '''
    View a video stored with wacky Toronto dimensions
    :param toronto_tensor: A tensor with dims T x V x H x W
    :param vid_id: Index of video to play. If None, choose random video
    :param delay: How long to wait between frames. If None, advance on click
    :return:
    '''
    vid_id_list = range(toronto_tensor.shape[1]) if vid_id is None else [vid_id]
    plt.figure()
    while True:
        for vid_id in vid_id_list:
            video = toronto_tensor[:, vid_id, :, :]
            if gen_seeds:
                print(gen_seeds[vid_id])
            for i in range(video.shape[0]):
                plt.clf()
                if titles:
                    plt.title('\n'.join(wrap(titles[vid_id], 60)))
                plt.imshow(video[i, :, :], cmap='gray', vmin=0, vmax=255)
                plt.tight_layout()
                plt.draw()
                if delay:
                    plt.pause(delay)
                    if i == video.shape[0]-1 and prompt_keypress:
                        print('Ended video. Press any key to continue.')
                        plt.waitforbuttonpress()
                else:
                    plt.waitforbuttonpress()

def main():
    # Select file path (https://stackoverflow.com/a/3579625)
    Tk().withdraw()
    filename = askopenfilename(initialdir='../output')
    if not filename: exit()
    tensor = np.load(filename, mmap_mode='r')
    print(tensor.shape)
    view_toronto_mnist_tensor(tensor, delay=0.001)


if __name__ == '__main__':
    main()