#/bin/bash -x

export PATH=$HOME/dkrz/git/eccodes/build/bin:$PATH
export LD_LIBRARY_PATH=$HOME/dkrz/git/eccodes/build/lib:$LD_LIBRARY_PATH
export ECCODES_DEFINITION_PATH=$HOME/dkrz/git/eccodes/definitions

case $1 in
  'd'):
    python3 -m ipdb ./tigge_check.py "data/source.grib"
    ;;
  *):
    ./tigge_check.py "data/source.grib"
    ;;
esac
