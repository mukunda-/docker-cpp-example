# docker-cpp-example               © 2020 Mukunda Johnson <mukunda@mukunda.com>
#------------------------------------------------------------------------------
cmake_minimum_required( VERSION 3.15 )
project( docker-cpp-example VERSION 1.0 LANGUAGES CXX )

#------------------------------------------------------------------------------
# List of source files.
#------------------------------------------------------------------------------
set( SRC_FILES
   src/main.cpp
)

#------------------------------------------------------------------------------
add_executable( docker-cpp-example ${SRC_FILES} )
