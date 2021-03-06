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

# This could ideally be converted to static methods on Config class, once 
# I have an internet connectoin and can google for how to do that ;-)

import sqlalchemysetup
from tableclasses import *

# get an appropriately typed config value, indexed by key_name
def getValue( key_name ):
   configrow = sqlalchemysetup.session.query(Config).filter(Config.config_key == key_name ).first()
   if configrow == None:
      return None
   return configrow.getValue()

