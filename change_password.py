import os
import boto3
from dotenv import load_dotenv
load_dotenv()

access_token = 'eyJraWQiOiJyaW9XQ3RhWjh3NGJkNVRDb0VLdUVNZHNYM0hDMnNMZmtmYitcL05YUEduOD0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiNmYyZmZmNDctN2ZlZC00ZmQ5LTkwMTItOGM2NjljYjZlZGIzIiwic3ViIjoiNWRiYmI5NTItYzkwNC00ZmQ0LTlkNmQtZGNkYjg3OTkyNTViIiwiZXZlbnRfaWQiOiI3NzhhZTQwNi1lYjFkLTRmMzQtOGRkZS04NWMyZWQxNzVjMzMiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjQ3NTQ4MzA2LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9JeUJqSlI1Z0YiLCJleHAiOjE2NDc1NTE5MDYsImlhdCI6MTY0NzU0ODMwNiwianRpIjoiOWJhM2FmMmYtZWE5YS00NjZhLTk5ZWUtOTAyY2U3YmM5NjZjIiwiY2xpZW50X2lkIjoiYXNuZ25jazNpZXEwY2w0ZWRxcXJudGJpZyIsInVzZXJuYW1lIjoiNWRiYmI5NTItYzkwNC00ZmQ0LTlkNmQtZGNkYjg3OTkyNTViIn0.D2qpuCB-Gc6vSIBhZsUkaZjfxOIiijxVkPMp46NFF2WgNXKOktBOkbm6SQeyOYgpYWGpr894KbOg_tMo-F86FO8bV8BGMV9AYXIPYEUUptM05H0iTYeyCdUKsYTc2ICHNjZ3NkukB_gkr_JUFfCTK9ZeLGpNkMFI7YDfWP51hM61OwAqPtfuONFeeNyyqtr8sxAPr5hE5kFZPBAwAUY0UuqVWx6O_A486mWzjZS8hsIFyhUqzOSf__VLgUoQhR8lQARB34OVt899abUGDR1tgXEBGjH-mnYkei15qbLxhVHGqC7eOSJls69NAsEwBLdaomlEYCGSHBlTyz4Z0NnSeg'

previous_password = '#1234Abc'
new_password = '#Abc1234'

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))

response = client.change_password(
    PreviousPassword = previous_password,
    ProposedPassword = new_password,
    AccessToken = access_token
)

print(response)