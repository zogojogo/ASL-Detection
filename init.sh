git clone https://github.com/AlexeyAB/darknet

cd darknet/
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/LIBSO=0/LIBSO=1/' Makefile

make

cd data/
find -maxdepth 1 -type f -exec rm -rf {} \;
cd ..

rm -rf cfg/
mkdir cfg

gdown --id 18256IBSB1PZfIMvfYpuPLC4yrReC6OFR
mv ./custom-detector.cfg cfg

cd cfg
sed -i 's/batch=64/batch=1/' custom-detector.cfg
sed -i 's/subdivisions=16/subdivisions=1/' custom-detector.cfg
cd ..

gdown --id 1swotEAlzaCHFDgvQEGlgGMq5IqO7xNza
gdown --id 1-1hue92BkaHT-0ThI24CXMbl6WefX5tt
mv ./obj.names data
mv ./obj.data  data
cp data/obj.names data/coco.names

cd ..
mkdir static
mkdir uploads

mkdir weights
gdown --id 18hI3qTKrAmyqt_I9dmqBOaZefCqAjQV3
mv ./custom-detector.weights weights