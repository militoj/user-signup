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


def build_page(textarea_content):
    signup_header = "<h1>Signup</h1>"

    username_label = "<label>Username</label>"
    username_input = "<input type='text' name='username'/>"

    password_label = "<label>Password</label>"
    password_input = "<input type='text' name='password'/>"

    verify_password_label = "<label>Verify Password</label>"
    verify_password_input = "<input type='text' name='verify'/>"

    email_label = "<label>Email (optional)</label>"
    email_input = "<input type='text' name='email'/>"

    submit = "<input type='submit'/>"

    form = ("<form method='post'>" +
    username_label + username_input + "<br>" +
            message_label + textarea + "<br>" +
            submit + "</form>")

    message_label = "<label>Type a message:</label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
            rot_label + rotation_input + "<br>" +
            message_label + textarea + "<br>" +
            submit + "</form>")

    header = "<h2>Web Caesar</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):

        signup_header = "<h1>Signup</h1>"

        username_label = "<label>Username</label>"
        username_input = "<input type='text' name='username'/>"

        password_label = "<label>Password</label>"
        password_input = "<input type='text' name='password'/>"

        verify_password_label = "<label>Verify Password</label>"
        verify_password_input = "<input type='text' name='verify'/>"

        email_label = "<label>Email (optional)</label>"
        email_input = "<input type='text' name='email'/>"

        submit = "<input type='submit'/>"

        form = ("<form method='post'>" +
        username_label + username_input + "<br>" +
                message_label + textarea + "<br>" +
                submit + "</form>")



        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
