set -e

indent() { sed '/^$/d' | sed 's/^/       /' ; }

BASE="pypy3.8-v7.3.7-linux64"
FILENAME="${BASE}.tar.bz2"
URL="https://downloads.python.org/pypy/${FILENAME}"
wget -P $CACHE_DIR -nc $URL 2>&1 | indent
tar xf ${CACHE_DIR}/${FILENAME}
PYPY_EXE="./${BASE}/bin/pypy"
$PYPY_EXE --version | indent
mkdir -p .profile.d
echo "export PYPY_EXECUTABLE=\$(realpath $PYPY_EXE)" > .profile.d/pypy_exe_path.sh
chmod +x .profile.d/pypy_exe_path.sh
echo "pypy installed successfully to $PYPY_EXE" | indent
