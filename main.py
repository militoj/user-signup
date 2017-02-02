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
import re


def build_page(username_entered,email_entered,username_error_element,password_error_element,verify_error_element,email_error_element):
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
            username_label  + username_input + username_error_element +"<br>" +
            password_label + password_input + password_error_element +"<br>" +
            verify_password_label + verify_password_input + verify_error_element +"<br>" +
            email_label  + email_input + email_error_element +"<br>" +
            submit + "</form>")

    header = "<h2>Signup</h2>"

    return header + form


# Validating against regular expressions

def username_check(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def password_check(username):
    USER_RE = re.compile(r"^.{3,20}$")
    return USER_RE.match(username)

def verify_check(password, verify):
    if password == verify:
        return True
    else:
        return False

def email_check(username):
    USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return USER_RE.match(username)



class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = build_page("","")
        self.response.write(content)

    def post(self):
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('username')
        verify = self.request.get('email')


        username_pass = False
        password_pass = False
        verify_pass = False
        email_pass = False


        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''

        username_error_element = 'BLAH '
        password_error_element = 'BLAH '
        verify_error_element = 'BLAH '
        email_error_element = 'BLAH '

        if username_check(username):
            username_pass = True
        else:
            username_error = "Please enter a valid username"

        if password_check(password):
            password_pass = True
        else:
            password_error = "Please enter a password"

        if verify_check(password,verify):
            verify_pass = True
        else:
            verify_error = "Your passwords do not match"

        if email_check(email):
            email_pass = True
        else:
            email_error = "Please enter a valid email address"



        if username_error:
            username_error_element = (
                "<p class='error'>" +
                cgi.escape(username_error, quote=True) +
                "</p>"
            )
        else:
            username_error_element  = " "

        if password_error:
            password_error_element = (
                "<p class='error'>" +
                cgi.escape(password_error, quote=True) +
                "</p>"
            )
        else:
            password_error_element  = " "

        if verify_error:
            verify_error_element = (
                "<p class='error'>" +
                cgi.escape(verify_error, quote=True) +
                "</p>"
            )
        else:
            verify_error_element = " "

        if email_error:
            email_error_element = (
                "<p class='error'>" +
                cgi.escape(email_error, quote=True) +
                "</p>"
            )
        else:
            email_error_element  = " "

        content = build_page(username,email,username_error_element,password_error_element,verify_error_element,email_error_element)
        self.response.write(content)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
