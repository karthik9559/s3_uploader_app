from flask import send_from_directory
import botocore
import pdb
from flask import request, redirect
import requests
import boto3
import logging
from flask_cors import CORS
from flask import Flask
import json
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx', 'csv'}
