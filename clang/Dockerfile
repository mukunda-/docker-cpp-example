# Clang and Friends
#
# Contains clang compiler and other utilities:
#   CMake
#   GDB (LLDB support in vscode is not great currently.)
#   Python3.8
#------------------------------------------------------------------------------
FROM ubuntu:20.04
LABEL maintainer="mukunda@mukunda.com"

#------------------------------------------------------------------------------
# Any packages we want plus essentials for the clang installer.
RUN apt-get update && apt-get install -y \
   cmake                                 \
   curl                                  \
   gdb                                   \
   lsb-release                           \
   python3.8                             \
   software-properties-common            \
   wget                                  \
   xz-utils

#------------------------------------------------------------------------------
# Copy script(s).
COPY . /

#------------------------------------------------------------------------------
# Install clang and do some housekeeping.
RUN ./install_clang.sh \
    && rm -rf /var/lib/apt/lists

#------------------------------------------------------------------------------
# (Default entrypoint is /bin/bash)
#
