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

import cgi

from utils import *
import sqlalchemysetup
import tableclasses
from tableclasses import *

botrunnername = ""

def botrunnerauthorized():
   global botrunnername 

   botrunnername = formhelper.getValue("botrunnername")
   sharedsecret = formhelper.getValue("sharedsecret")
   return validatesharedsecret( botrunnername, sharedsecret )

def getbotrunner(botrunnername ):
   return sqlalchemysetup.session.query(tableclasses.BotRunner).filter(tableclasses.BotRunner.botrunner_name == botrunnername ).first()

def validatesharedsecret(lbotrunnername, sharedsecret):
   global botrunnername

   botrunner = getbotrunner( lbotrunnername )

   if botrunner == None: 
      # Never seen this botrunner before, just add it
      botrunner = tableclasses.BotRunner()
      botrunner.botrunner_name = lbotrunnername
      botrunner.botrunner_sharedsecret = sharedsecret
      sqlalchemysetup.session.add(botrunner)
      sqlalchemysetup.session.commit()

      # if this fails, return true anyway
      return True
   else:
      if botrunner.botrunner_sharedsecret == sharedsecret:
         botrunnername = lbotrunnername
         return True
      return False

def getOwnerUsername(botrunnername):
   botrunner = getbotrunner( botrunnername )
   if botrunner == None:
      return None
   if botrunner.owneraccount == None:
      return None
   return botrunner.owneraccount.username

