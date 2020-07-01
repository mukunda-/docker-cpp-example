
# LLVM+Clang installer script for v10.
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh

# Normally this would stop and prompt for some timezone stuff.
DEBIAN_FRONTEND=noninteractive TZ=America/New_York ./llvm.sh 10

# Setup default commands.
update-alternatives --install /usr/bin/clang     clang     /usr/bin/clang-10     100 \
                    --slave   /usr/bin/clang++   clang++   /usr/bin/clang++-10       \
                    --slave   /usr/bin/clang-cpp clang-cpp /usr/bin/clang-cpp-10     \
                    --slave   /usr/bin/clangd    clangd    /usr/bin/clangd-10

update-alternatives --install /usr/bin/cc  cc  /usr/bin/clang-10   100 \
                    --slave   /usr/bin/c++ c++ /usr/bin/clang++-10     \
                    --slave   /usr/bin/cxx cxx /usr/bin/clang++-10
                    
update-alternatives --install /usr/bin/lldb lldb /usr/bin/lldb-10 100


