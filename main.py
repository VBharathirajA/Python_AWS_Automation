import boto3
from botocore.exceptions import ClientError,NoCredentialsError
import os



session = boto3.session.Session()
regions = session.get_available_regions('s3')


while True:
    loc = os.environ.get("AWS_DEFAULT_REGION", "ap-south-1")

    if loc in regions:
        print("Valid region")
        
        break
    else:
        print("Invalid region. Enter again.")
        print("Available regions:", regions)
s3=boto3.client('s3',region_name=loc)

class S3_operation:
    
    def create(self):
            name=input("Enter Bucket Name:")
            
            try:
                
                s3.create_bucket(
                        Bucket=name,
                        CreateBucketConfiguration={
                        'LocationConstraint': loc})
                print("Bucket Created Successfully")
            except ClientError as e :
                response=e.response['Error']['Code']
                if response =='BucketAlreadyOwnedByYou':
                    print("Bucket is already Owned by you change bucket name")
                elif response=='BucketAlreadyExists':
                    print("Bucket Already Exists in your S3")
                elif response=='InvalidBucketName':
                    print("Bucket Name is Invalid")
                                    
            except:
                print("Unexpected Error")

                
    def display(self):
        try:
            
            resource=s3.list_buckets()
            buck=resource['Buckets']
            if len(buck)!=0:
                print("\nAvailable Buckets")
                      
                for i in buck:
                    print(i['Name'])
            else:
                print("No Bucket Foud")
        except ClientError as e:
            print("Error",e)

            
    def upload(self):
        
        file=input("Enter Local File name:")
        bucket=input("Enter Bucket name:")
        obj=input("Enter Object name:")
        
        
        try:
            if not os.path.exists(file):
                print("File does not exist")
                return
            s3.upload_file(file,bucket,obj)
            print("File uplaoded successfully")
            
        except FileNotFoundError:
            print("Local file not found")

        except NoCredentialsError:
            print("AWS credentials not configured")

        except ClientError as e:

            error_code = e.response['Error']['Code']

            if error_code == "NoSuchBucket":
                print("Bucket does not exist")

            elif error_code == "AccessDenied":
                print("Permission denied to upload file")

            else:
                print("AWS Error:", e)

    def download(self):
        
        bucket=input("Enter Bucket name:")
        obj=input("Enter Object name:")
        file=input("Enter File name:")
        
        
        try:

            s3.download_file(bucket,obj,file)
            print("File Downloaded Successfully")

        except NoCredentialsError:
            print("AWS credentials not configured")

        except ClientError as e:

            error_code = e.response['Error']['Code']

            if error_code == "NoSuchBucket":
                print("Bucket does not exist")

            elif error_code == "NoSuchKey":
                print("File not found in bucket")

            elif error_code == "AccessDenied":
                print("Permission denied")

            else:
                print("AWS Error:", e)
    def list_objects(self):

        bucket=input("Enter Bucket Name:")
         
        try:
            
           
            response=s3.list_objects_v2(Bucket=bucket)

            if 'Contents' not in response:
                print("Bucket is empty")
                return

            print("\nObjects in bucket:")
            
            for i in response['Contents']:
                print(i['Key'])
    
        except ClientError as e:
            error_code=e.response['Error']['Code']
            if error_code == "NoSuchBucket":
                print("Bucket Does not exist")
            elif error_code == "AccessDenied":
                print("Permission Denied")
            else:
                print("Aws Error:",e)
    def delete_object(self):
        bucket=input("Enter Bucket Name:")
        file=input("Enter File name:")
        try:
            
            s3.delete_object(Bucket=bucket,Key=file)
            print("Object Deleted Successfully")

        except ClientError as e:
            error_code=e.response['Error']['Code']
            if error_code=='NoSuchBucket':
                print("Bucket does not exist")
            elif error_code=='AccessDenied':
                print("Permission denied")
            elif error_code=='NoCredentialsError':
                print("AWS Credentials not configured")
            elif error_code=='EndpointConnectionError':
                print("Network or region issue")
            else:
                print("AWS Error:",e)
                

                                    
    def delete_bucket(self):
        name=input("Enter Bucket Name to Delete:")
        try:
            
            s3.delete_bucket(Bucket=name)
            print("Bucket Deleted Successfully")
            
        except ClientError as e:
            error_code=e.response['Error']['Code']
            if error_code=='BucketNotEmpty':
                    print("Bucket is not empty. Delete objects first")
            elif error_code == "NoSuchBucket":
                print("Bucket does not exist")

            else:
                print("AWS Error:", e)
        except:
            print("Unexcepted Error")

    def find(self):
        name=input("Enter Bucket Name:")

        try:
            s3.head_bucket(Bucket=name)
            print("Bucket Exists")
        except:
            print("Bucket does not exist")
class Ec2_operation:
    def create(self):
        ec2 = boto3.client('ec2', region_name='ap-south-1')

        response = ec2.run_instances(
            ImageId='ami-078b9ee40ca940985',
            InstanceType='t3.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='keypc1'
        )

                
obj=S3_operation()
obj2=Ec2_operation()
def UI():
    while True:
        print("1. Ec2 Operations")
        print("2. S3 Operations")
        print("3. Exit")
        inp=int(input("Enter Choice:"))
        if inp==1:
            while True:
                print("1. Create Ec2")
                print("2. Exit program")
                print("3. Main Menu")
                choice = int(input("Enter Choice:"))
                if choice==1:
                    obj2.create()
                elif choice==2:
                    print("Exiting Program")
                    return 
                elif choice==3:
                   break
                else:
                    print("Invalid choice")
                
        
        elif inp==2:    
            while True:

                print("\nAWS S3 Operations")
                print("1. Create Bucket")
                print("2. List Buckets")
                print("3. Upload File")
                print("4. Download File")
                print("5. List Objects")
                print("6. Delete Object")
                print("7. Delete Bucket")
                print("8. Check Bucket Exists")
                print("9. Main menu")
                print("10. Exit")

                choice = int(input("Enter Choice: "))

                if choice == 1:
                    obj.create()

                elif choice == 2:
                    obj.display()

                elif choice == 3:
                    obj.upload()

                elif choice == 4:
                    obj.download()

                elif choice == 5:
                    obj.list_objects()

                elif choice == 6:
                    obj.delete_object()

                elif choice == 7:
                    obj.delete_bucket()

                elif choice == 8:
                    obj.find()

                elif choice==9:
                    break

                elif choice == 10:
                    print("Exiting Program")
                    return

                else:
                    print("Invalid Choice")
        elif inp==3:
            print("Exiting Program")
            break
        else:
            print("Invalid input")
UI()             

if __name__ == "__main__":
    main()

