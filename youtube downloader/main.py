from pytube import *
import sys
from tabulate import tabulate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

link = sys.argv[1]
downloader = YouTube(link)
print(tabulate([
                            [1, "Highest Resolution"], [2, 'Lowest Resolution'],[3, "Audio only"], [4, "Exit the program"]
                           ],headers=['Code', 'Options'], tablefmt="simple_grid", numalign="center"), "\n")

code = int(input("Enter a single code: "))
# path = input("Enter the full path where you want to download the video: ")
path = "/Users/vijaykarthick/Downloads"
print(f"Title: {downloader.title}")
print(f"Views: {downloader.views}")

while code not in range(1, 6):
    code = int(input("Enter a proper code from the above table : "))
if code == 4:
    quit()
elif code == 1:
    video = downloader.streams.get_highest_resolution()
    print(f"Size: {int(video.filesize*0.000001)}Mb")
    video.download(output_path=path)

elif code == 2:
    video = downloader.streams.get_lowest_resolution()
    print(f"Size: {int(video.filesize*0.000001)}Mb")
    video.download(output_path=path)
elif code == 3:
    video = downloader.streams.get_audio_only()
    print(f"Size: {int(video.filesize*0.000001)}Mb")
    video.download(output_path=path)

quit()