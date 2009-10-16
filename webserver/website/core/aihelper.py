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

from utils import *
from tableclasses import *
import sqlalchemysetup
import botrunnerhelper

def getallais():
   return sqlalchemysetup.session.query(AI)

# return list of supported (ainame,aiversion) tuples
def getsupportedais( botrunnername ):
   botrunner = botrunnerhelper.getbotrunner(botrunnername)
   if botrunner == None:
      return []
   supportedais = []
   #for ai in botrunner.supportedais:
   #   supportedais.append( [ ai.ai.ai_name, ai.ai.ai_version ] )
   #  hmmm, in fact we just return all ais for now ;-)
   for ai in getallais():
      supportedais.append( [ ai.ai_name, ai.ai_version ] )
   return supportedais

def getai( ainame, aiversion ):
   return sqlalchemysetup.session.query(AI).filter(AI.ai_name == ainame ).filter(AI.ai_version == aiversion ).first()

def addaiifdoesntexist(ainame, aiversion):
   ai = getai( ainame, aiversion )
   if ai == None:
      try:
         ai = AI(ainame, aiversion )
         sqlalchemysetup.session.add( ai )
         sqlalchemysetup.session.commit()
      except:
         return(False,"error adding to db: " + str( sys.exc_value ) )

   return (True,'')


