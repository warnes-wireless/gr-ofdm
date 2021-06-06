# ITPP
## Fedora
### Dependencies
sudo dnf install lapack-devel lapack64-devel lapack64 blas blas64 blas-devel blas64-devel fftw fftw-devel fftw-libs
### it++ download and compilation
wget https://sourceforge.net/projects/itpp/files/latest -O itpp.tar.bz2  
tar -xjvf itpp.tar.bz2 && cd itpp-*  
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
## Ubuntu
https://stackoverflow.com/questions/41077559/quick-and-hassle-free-installation-usage-of-it-library-on-linux-windows#_=_