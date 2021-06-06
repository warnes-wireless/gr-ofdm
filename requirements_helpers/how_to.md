# ITPP
## Dependencies
### Fedora  
`sudo dnf install lapack-devel lapack64-devel lapack64 blas blas64 blas-devel blas64-devel fftw fftw-devel fftw-libs`  
### Ubuntu  
`sudo apt-get install liblapack64-dev liibblas64-dev libfftw3-dev`  
https://stackoverflow.com/questions/41077559/quick-and-hassle-free-installation-usage-of-it-library-on-linux-windows#_=_  
#### Searching for current versions avaialble in the main ubuntu repository
apt search ...  
e.g. `apt search lapack`  
## it++ download and compilation
### Download
wget https://sourceforge.net/projects/itpp/files/latest -O itpp.tar.bz2  
### Unpack the archive
tar -xjvf itpp.tar.bz2 && cd itpp-*  
### Compile [and install] with cmake
```
mkdir build1 build2
cd build1                   # DYNAMIC (*.so file)  
cmake ..  
make  
make install  

cd bulid2                   # STATIC (*.a file)
cmake .. -DITPP_SHARED_LIB=off
make
make install
```