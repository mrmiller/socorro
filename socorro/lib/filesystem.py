#!/usr/bin/python
#
# Copyright 2005 by Centaur Software Engineering, Inc.
#
#    This file is part of The CSE Python Library.
#
#    The CSE Python Library is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    The CSE Python Library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with The CSE Python Library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import os

#--------------------------------------------------
# d e f a u l t A c c e p t a n c e F u n c t i o n
#--------------------------------------------------
def defaultAcceptanceFunction (dummy):
  return True


#----------------------------------
# f i n d F i l e G e n e r a t o r
#----------------------------------
def findFileGenerator(rootDirectory, acceptanceFunction=defaultAcceptanceFunction, directoryAcceptanceFunction=defaultAcceptanceFunction):
  """This function returns a generator that walks a filesystem tree.  It applies a user supplied function
  to each file that it encounters.  It only returns files for which the user supplied function returns true.
  It returns a tuple consiting of three items: the root path of the file, the name of the object, and the
  complete pathname of the object.  The user supplied function uses the same tuple as its input.
  """
  for aCurrentDirectoryItem in [ (rootDirectory, x, os.path.join(rootDirectory, x)) for x in os.listdir(rootDirectory) ]:
    if os.path.isdir(aCurrentDirectoryItem[2]) and directoryAcceptanceFunction(aCurrentDirectoryItem):
      for aSubdirectoryItem in findFileGenerator(aCurrentDirectoryItem[2], acceptanceFunction, directoryAcceptanceFunction):
        yield aSubdirectoryItem
    if acceptanceFunction(aCurrentDirectoryItem):
      yield aCurrentDirectoryItem


if __name__ == "__main__":

  for path, name, pathname in findFileGenerator("."):
    print pathname