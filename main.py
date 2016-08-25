#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        encrypted = self.request.get("encrypted")

        ceasar_form = """
            <form method="POST">
                <input type="text" name="rot" id="rot">
                <textarea name="text" id="text">""" + encrypted + """</textarea>
            </form>
        """

        self.response.write(page_header + caesar_form + page_footer)

    def post(self):
        rot = self.request.get("rot")
        text = self.request.get("text")

        encrypted_text = encrypt(text, rot)

        self.redirect("/?encrypted={}".format(encrypted_text))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
