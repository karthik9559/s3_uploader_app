from flask import Flask
from flask_cors import CORS
import os
import logging
import boto3
import requests
import boto3, botocore
from flask import request, redirect

logging.basicConfig(
 level=logging.DEBUG, format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)

logger = logging.getLogger()

app = Flask(__name__)
S3_BUCKET = "gdrgbghrd"
S3_KEY = "AKIAS5H6RGXZ5A245RVF"
S3_SECRET = "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"
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format("gdrgbghrd")

s3 = boto3.client(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)

cors = CORS(app)

@app.route("/", methods=["POST"])
def upload_file():
    if "user_file" not in request.files:
        return "No user_file key in request.files"

    file = request.files["user_file"]

    if file.filename == "":
        return "Please select a file"

    if file:
        file.filename = secure_filename(file.filename)
        output = send_to_s3(file, S3_BUCKET)
        return str(output)

    else:
        return redirect("/")

def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type    #Set appropriate content type as per the file
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return "{}{}".format(S3_LOCATION, file.filename)

@app.route('/sign_s3/')
def sign_s3():
  file_name = request.args.get('file_name')
  file_type = request.args.get('file_type')

  s3 = boto3.client('s3')

  presigned_post = s3.generate_presigned_post(
    Bucket = S3_BUCKET,
    Key = file_name,
    Fields = {"acl": "public-read", "Content-Type": file_type},
    Conditions = [
      {"acl": "public-read"},
      {"Content-Type": file_type}
    ],
    ExpiresIn = 3600
  )

  return json.dumps({
    'data': presigned_post,
    'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
  })

if __name__ == "__main__":
 # app.run(host='192.168.120.212', port=8443, ssl_context=context, threaded=True, debug=False)
 app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

