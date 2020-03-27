# required flask modules
from flask import Flask, render_template, request, redirect

import os
import sys
import json

app = Flask(__name__)
application = app