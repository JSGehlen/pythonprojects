from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Home':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/jeremygehlen/Desktop/Home/Other/Uncategorized",
#Audio
    '.aif' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.cda' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.mid' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.midi' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.mp3' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.mpa' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.ogg' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.wav' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.wma' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.wpl' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
    '.m3u' : "/Users/jeremygehlen/Desktop/Home/Media/Audio",
#Text
    '.txt' : "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
    '.doc' : "/Users/jeremygehlen/Desktop/Home/Text/Microsoft/Word",
    '.docx' : "/Users/jeremygehlen/Desktop/Home/Text/Microsoft/Word",
    '.odt ' : "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
    '.pdf': "/Users/jeremygehlen/Desktop/Home/Text/PDF",
    '.rtf': "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
    '.tex': "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
    '.wks ': "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
    '.wps': "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
    '.wpd': "/Users/jeremygehlen/Desktop/Home/Text/TextFiles",
#Video
    '.3g2': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.3gp': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.avi': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.flv': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.h264': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.m4v': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.mkv': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.mov': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.mp4': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.mpg': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.mpeg': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.rm': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.swf': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.vob': "/Users/jeremygehlen/Desktop/Home/Media/Video",
    '.wmv': "/Users/jeremygehlen/Desktop/Home/Media/Video",
#Images
    '.ai': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.bmp': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.gif': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.ico': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.jpg': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.jpeg': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.png': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.ps': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.psd': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.svg': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.tif': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.tiff': "/Users/jeremygehlen/Desktop/Home/Media/Images",
    '.CR2': "/Users/jeremygehlen/Desktop/Home/Media/Images",
#Internet
    '.asp': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.aspx': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.cer': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.cfm': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.cgi': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.pl': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.css': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.htm': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.js': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.jsp': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.part': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.php': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.rss': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
    '.xhtml': "/Users/jeremygehlen/Desktop/Home/Other/Internet",
#Compressed
    '.7z': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.arj': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.deb': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.pkg': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.rar': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.rpm': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.tar.gz': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.z': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
    '.zip': "/Users/jeremygehlen/Desktop/Home/Other/Compressed",
#Disc
    '.bin': "/Users/jeremygehlen/Desktop/Home/Other/Disc",
    '.dmg': "/Users/jeremygehlen/Desktop/Home/Other/Disc",
    '.iso': "/Users/jeremygehlen/Desktop/Home/Other/Disc",
    '.toast': "/Users/jeremygehlen/Desktop/Home/Other/Disc",
    '.vcd': "/Users/jeremygehlen/Desktop/Home/Other/Disc",
#Data
    '.csv': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.dat': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.db': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.dbf': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.log': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.mdb': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.sav': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.sql': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.tar': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.xml': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
    '.json': "/Users/jeremygehlen/Desktop/Home/Programming/Database",
#Executables
    '.apk': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
    '.bat': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
    '.com': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
    '.exe': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
    '.gadget': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
    '.jar': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
    '.wsf': "/Users/jeremygehlen/Desktop/Home/Other/Executables",
#Fonts
    '.fnt': "/Users/jeremygehlen/Desktop/Home/Other/Fonts",
    '.fon': "/Users/jeremygehlen/Desktop/Home/Other/Fonts",
    '.otf': "/Users/jeremygehlen/Desktop/Home/Other/Fonts",
    '.ttf': "/Users/jeremygehlen/Desktop/Home/Other/Fonts",
#Presentations
    '.key': "/Users/jeremygehlen/Desktop/Home/Text/Presentations",
    '.odp': "/Users/jeremygehlen/Desktop/Home/Text/Presentations",
    '.pps': "/Users/jeremygehlen/Desktop/Home/Text/Presentations",
    '.ppt': "/Users/jeremygehlen/Desktop/Home/Text/Presentations",
    '.pptx': "/Users/jeremygehlen/Desktop/Home/Text/Presentations",
#Programming
    '.c': "/Users/jeremygehlen/Desktop/Home/Programming/C&C++",
    '.class': "/Users/jeremygehlen/Desktop/Home/Programming/Java",
    '.dart': "/Users/jeremygehlen/Desktop/Home/Programming/Dart",
    '.py': "/Users/jeremygehlen/Desktop/Home/Programming/Python",
    '.sh': "/Users/jeremygehlen/Desktop/Home/Programming/Shell",
    '.swift': "/Users/jeremygehlen/Desktop/Home/Programming/Swift",
    '.html': "/Users/jeremygehlen/Desktop/Home/Programming/C&C++",
    '.h': "/Users/jeremygehlen/Desktop/Home/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/jeremygehlen/Desktop/Home/Text/Microsoft/Excel",
    '.xlr' : "/Users/jeremygehlen/Desktop/Home/Text/Microsoft/Excel",
    '.xls' : "/Users/jeremygehlen/Desktop/Home/Text/Microsoft/Excel",
    '.xlsx' : "/Users/jeremygehlen/Desktop/Home/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.cab' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.cfg' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.cpl' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.cur' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.dll' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.dmp' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.drv' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.icns' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.ico' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.ini' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.lnk' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.msi' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.sys' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
    '.tmp' : "/Users/jeremygehlen/Desktop/Home/Text/Other/System",
}

folder_to_track = '/Users/jeremygehlen/Desktop'
folder_destination = '/Users/jeremygehlen/Desktop/Home'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()