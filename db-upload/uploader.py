import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKedajjoyoagdbZBNv9Dfcf7Ao06Agut4fDyxsYbkTR8rmzWXecC6dcdD2NJTBAXNDMTK7Hda3sHqxSATfi5pCy8wcPO1n-2DXa-8H2EPQauYoVK2r2NktXkbmIl6reuB2omXcI'
    transferData = TransferData(access_token)

    file_from = str(raw_input("Enter the file path to transfer : -"))
    file_to = str(raw_input("enter the full path to upload to dropbox:- "))  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()