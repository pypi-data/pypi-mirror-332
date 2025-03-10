from Download import *
from Extract import *
from Desktop import *
from Move import *
from Cleanup import *
from StartMenu import *

if __name__ == '__main__':

    GH_API_ELONA = "https://api.github.com/repos/vichmartins/ElonaPlusCGXDownload/releases/latest"
    GH_API_CGX = "https://api.github.com/repos/JianmengYu/ElonaPlusCustom-GX/releases/latest"
    ELONA_FILE_NAME = 'Elona.zip'
    CGX_FILE_NAME = 'Custom-GX.zip'
    EXE = 'elonapluscgx.exe'
    SHORTCUT_NAME = 'ElonaPlusCustom-GX'
    INSTALL_PATH = os.getenv('APPDATA')

    def main():
        print("downloading latest version of Elona+ to your %APPDATA% folder")
        elona = Download(file_name=ELONA_FILE_NAME, link=GH_API_ELONA, install_path=INSTALL_PATH)
        elona.create_file()
        elona.get_file()

        print("downloading latest version of CustomGX variant.")
        cgx = Download(file_name=CGX_FILE_NAME, link=GH_API_CGX, install_path=INSTALL_PATH)
        cgx.create_file()
        cgx.get_file()

        print("extracting Elona+")
        e = Extract(elona.get_name(), install_path=INSTALL_PATH)
        e.extract_zip()

        print("extracting CustomGX")
        c = Extract(cgx.get_name(), install_path=INSTALL_PATH)
        c.extract_zip()

        print("Moving files to the latest version")
        mover = Move(source_path = cgx.get_install_path(), destination = e.find_latest_version())
        result = mover.execute()
        print(f"Operation {'successful' if result['success'] else 'failed'}")

        print("Creating Desktop Shortcut")
        path = e.find_latest_version()
        version = e.scrape_version()
        d = Desktop(name=SHORTCUT_NAME, path=path, version=version, exe=EXE, description=SHORTCUT_NAME)
        d.create_shortcut()

        print("Cleaning up Downloaded Files")
        try:
            cleaner = Cleanup(main_game=ELONA_FILE_NAME, mod=CGX_FILE_NAME)
            cleaner.execute()
        except Exception as e:
            print(f"Error: {e}")

        print("Creating Start Menu Shortcut")
        start_menu = StartMenu(path + "\\" + EXE, use_all_users=False, folder_name=SHORTCUT_NAME)
        start_menu.create_shortcut()

        print('Setup Finished! Enjoy ElonaCustom-GX!')

    main()
