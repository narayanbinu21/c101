import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self,files_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(files_from,'rb') 
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.A2gE50BZRhqYeqALMGX--j06MRTccm0ZVxN1QrTj9RVEmyTv1eR72rUavERKNKFKRuyvUNOzC_attNiEbnbpUBwC_L1ApahKHHu7xSCs_0GeOqHGrvBI0gAmookD0X8mde28X90'
    transferData =  TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload to dropbox")

    transferData.upload_file(file_from, file_to)
    print("files have been moved")

main()