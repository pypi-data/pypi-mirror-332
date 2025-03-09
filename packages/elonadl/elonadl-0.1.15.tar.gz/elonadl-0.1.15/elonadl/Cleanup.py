import os
import shutil

class Cleanup:
    def __init__(self, path=None):
        self.path = path or os.getenv('APPDATA')
        if not self.path:
            raise ValueError("APPDATA environment variable not found and no path provided.")
        
        # Files to delete
        self.files_to_delete = ['cgx.zip', 'elona.zip']
        
    def find_targets(self) -> dict:
        results = {
            "files": [],
            "directories": []
        }
        
        # Check if the specified files exist
        for file_name in self.files_to_delete:
            file_path = os.path.join(self.path, file_name)
            if os.path.isfile(file_path):
                results["files"].append(file_path)
                
        # Find directories starting with 'Elona+'
        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isdir(item_path) and item.startswith('Elona+'):
                results["directories"].append(item_path)
                
        return results
    
    def delete_items(self, targets):
        # Delete files
        for file_path in targets["files"]:
            try:
                os.remove(file_path)
            except OSError:
                pass
                
        # Delete directories
        for dir_path in targets["directories"]:
            try:
                shutil.rmtree(dir_path)
            except OSError:
                pass
    
    def execute(self, dry_run=False):
        # Find targets
        targets = self.find_targets()
        
        # If dry run, don't actually delete anything
        if dry_run:
            return
        
        # Delete the items
        self.delete_items(targets)


# Example usage
if __name__ == "__main__":
    try:
        cleaner = Cleanup()
        cleaner.execute()
    except Exception as e:
        print(f"Error: {e}")