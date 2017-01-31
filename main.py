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


def build_page(username_entered,email_entered):
    header = "<h1>Signup</h1>"

    username_label = "<label>Username</label>"
    username_input = "<input type='text' name='username' value='{0}'/>".format(username_entered)

    password_label = "<label>Password</label>"
    password_input = "<input type='text' name='password'/>"

    verify_password_label = "<label>Verify Password</label>"
    verify_password_input = "<input type='text' name='verify'/>"

    email_label = "<label>Email (optional)</label>"
    email_input = "<input type='text' name='email' value='{0}'/>".format(email_entered)

    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
            username_label  + username_input + "<br>" +
            password_label + password_input + "<br>" +
            verify_password_label + verify_password_input + "<br>" +
            email_label  + email_input + "<br>" +
            submit + "</form>")

    header = "<h2>Signup</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = build_page("","")
        self.response.write(content)

    def post(self):
        username = self.request.get('username')
        email = self.request.get('email')
        content = build_page(username,email)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
