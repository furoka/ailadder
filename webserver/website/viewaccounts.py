#!/usr/bin/python

# Copyright Hugh Perkins 2009
# hughperkins@gmail.com http://manageddreams.com
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
# You should have received a copy of the GNU General Public License along
# with this program in the file licence.txt; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-
# 1307 USA
# You can find the licence also on the web at:
# http://www.opensource.org/licenses/gpl-license.php
#

import cgitb; cgitb.enable()

from utils import *
from core import *

dbconnection.connectdb()

sqlalchemysetup.setup()

loginhelper.processCookie()

menu.printPageTop()

def go():
   if loginhelper.gusername == '':
      print "Please login first before using this page."
      return

   accounts = dbconnection.querytomaplist( "select username, userfullname from accounts" )

   print "<h3>AILadder - Account List</h3>" \
   "<table border='1' padding='3'>" \
   "<tr class='tablehead'><td>username</td><td>User full name</td><td>Delete</td></tr>"

   for account in accounts:
      print "<tr>"
      print "<td><a href='viewaccount.py?username=" + account['username'] + "'>" + account['username'] + "</td><td>" + account['userfullname'] + "</a></td>"
      if not roles.isInRole2( account['username'], roles.accountadmin ):
         print "<td><a href='removeaccount.py?username=" + account['username'] + "'>Delete account</a></td>"
      else:
         print "<td>(Drop accountadmin role before deleting account)</td>"
      print "</tr>"

   print "</table>"

   if roles.isInRole(roles.accountadmin):

      print "<p />"
      print "<hr />"
      print "<p />"

      print "<h4>Create new account:</h4>"
      print "<form action='addaccount.py' method='post'>" \
      "<table border='1' padding='3'>" \
      "<tr><td>Username</td><td><input name='username'</td></tr>" \
      "<tr><td>User full name</td><td><input name='userfullname'</td></tr>" \
      "<tr><td>User email address</td><td><input name='useremailaddress'</td></tr>" \
      "<tr><td>User password</td><td><input type='password' name='userpassword'</td></tr>" \
      "<tr><td></td><td><input type='submit' value='Add' /></td></tr>" \
      "</table>" \
      "</form>"


go()

sqlalchemysetup.close()

dbconnection.disconnectdb()

menu.printPageBottom()

