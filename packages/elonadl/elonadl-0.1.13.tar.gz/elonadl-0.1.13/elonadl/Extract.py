from zipfile import ZipFile
from os import getenv, path, listdir
from re import findall


class Extract:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def extract_zip(self):
        local = getenv('APPDATA')
        c = path.join(local, self.file_name)

        with ZipFile(c) as z:
            z.extractall(local)

    def find_latest_version(self):
        t = listdir(path=getenv('APPDATA'))
        n = "elonaplus"
        u = list()

        for x in t:
            h = findall(n + "[0-9].[0-9][0-9]", x)
            if h:
                u.append(x)

        if not u:
            exit()

        result = path.join(getenv('APPDATA'), max(u) + '\\')

        return result

    def scrape_version(self):
        t = listdir(path=getenv('APPDATA'))
        n = "elonaplus"
        u = list()

        for x in t:
            h = findall(n + "[0-9].[0-9][0-9]", x)
            if h:
                u.append(x)

        return max(u)[9:]
