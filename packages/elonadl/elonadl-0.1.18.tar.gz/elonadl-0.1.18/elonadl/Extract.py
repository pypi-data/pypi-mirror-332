from zipfile import ZipFile
from os import path, listdir
from re import findall


class Extract:

    def __init__(self, file_name, install_path) -> None:
        self.file_name = file_name
        self.install_path = install_path

    def extract_zip(self):
        local = self.install_path
        c = path.join(local, self.file_name)

        with ZipFile(c) as z:
            z.extractall(local)

    def find_latest_version(self):
        t = listdir(path=self.install_path)
        n = "elonaplus"
        u = list()

        for x in t:
            h = findall(n + "[0-9].[0-9][0-9]", x)
            if h:
                u.append(x)

        if not u:
            exit()

        result = path.join(self.install_path, max(u) + '\\')

        return result

    def scrape_version(self):
        t = listdir(path=self.install_path)
        n = "elonaplus"
        u = list()

        for x in t:
            h = findall(n + "[0-9].[0-9][0-9]", x)
            if h:
                u.append(x)

        return max(u)[9:]
