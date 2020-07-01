#!/usr/bin/python3
#------------------------------------------------------------------------------
# docker-cpp-example               © 2020 Mukunda Johnson <mukunda@mukunda.com>
#
# Script for building our program.
#------------------------------------------------------------------------------
import os, argparse

def myprint( *args, **kwargs ): myprint.print( "(Build)", *args, **kwargs )
myprint.print = print
print = myprint

sh = os.system

#------------------------------------------------------------------------------
# A simple check here to make sure that we're in the docker container. Could
#                                    probably be more comprehenive than this.
if not os.path.exists( "/llvm.sh" ):
   print( "This is meant to be run in the clang container." )
   exit( 1 )

#------------------------------------------------------------------------------
# Build options.
argparser = argparse.ArgumentParser()
argparser.add_argument(
   "--build",
   default="DEBUG",
   help="Build mode. Can be DEBUG or RELEASE. Defaults to DEBUG." )
args = argparser.parse_args()

opts = lambda: None
opts.build = args.build.upper()

#------------------------------------------------------------------------------
try:
   # The mounted build volume.
   os.chdir( "/build" )
   if opts.build == "RELEASE":
      os.makedirs( "release", exist_ok = True )
      os.chdir( "release" )
   else:
      os.makedirs( "debug", exist_ok = True )
      os.chdir( "debug" )
except:
   print( "Couldn't open build directory. Is it mounted?" )
   exit( 1 )

#------------------------------------------------------------------------------
if not os.path.exists( "Makefile" ):
   # Makefile doesn't exist yet.
   print( "Setting up first-time build." )
   sh( "cmake --target docker-cpp-example -DCMAKE_BUILD_TYPE=%s /wd"
       % ("Release" if opts.build == "RELEASE" else "Debug") )

#------------------------------------------------------------------------------
sh( "make" )
