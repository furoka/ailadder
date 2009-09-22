// Copyright Hugh Perkins 2009
// hughperkins@gmail.com http://manageddreams.com
//
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU General Public License as published by the
// Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
// or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
//  more details.
//
// You should have received a copy of the GNU General Public License along
// with this program in the file licence.txt; if not, write to the
// Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-
// 1307 USA
// You can find the licence also on the web at:
// http://www.opensource.org/licenses/gpl-license.php
//

#include <iostream>
#include <cstdlib>
#include <pthread.h>
#include <fstream>

using namespace std;

char *endgamemessageprefix = "[   024131] Team";
char *endgamemessagepostfix = " kicked the bucket";

void hang() {
         while(true) {
            sleep(1000);
         }         
}

ofstream Infolog("infolog.txt");

void openInfolog() {
   // I think it's opened by the constructor
}

void writeToInfolog( char *message ) {
   Infolog << message << endl;
}

void writeStuffToInfologbis() {
   for( int i = 0; i < 100; i++ ) {
      writeToInfolog("blah");
      writeToInfolog("foo");
   }
}

void writeStuffToInfolog() {
   for( int i = 0; i < 3; i++ ) {
      writeStuffToInfologbis();
      sleep(1);
   }
   writeStuffToInfologbis();
}

int main( int argc, char** argv ) {
   srand((unsigned)time(0)); // seed the pseudo-random numbers with system time
   int randomnumber = rand() % 5;
   int a = 0;
   int b = 0;
   char message[1024];
   switch( randomnumber ) {
      case 0:   // crash
         cout << "crashing" << endl;
         writeStuffToInfolog();
         a = 0;
         b = 5 / a;
         break;

      case 1:   // hang 
         cout << "hanging" << endl;
         writeStuffToInfolog();
         hang();
         break;

      case 2:   // ai0 dies
         cout << "ai0 dieing..." << endl;
         writeStuffToInfolog();
         sprintf( message, "%s%i%s", endgamemessageprefix, 0, endgamemessagepostfix );
         writeToInfolog( message );
         hang();
         break;

      case 3:   // ai1 dies
         cout << "ai1 dieing..." << endl;
         writeStuffToInfolog();
         sprintf( message, "%s%i%s", endgamemessageprefix, 1, endgamemessagepostfix );
         writeToInfolog( message );
         hang();
         break;

      case 4:   // both ais die
         cout << "both dieing..." << endl;
         writeStuffToInfolog();
         sprintf( message, "%s%i%s", endgamemessageprefix, 0, endgamemessagepostfix );
         writeToInfolog( message );
         sprintf( message, "%s%i%s", endgamemessageprefix, 1, endgamemessagepostfix );
         writeToInfolog( message );
         hang();
         break;

   }
   return 0;
}
