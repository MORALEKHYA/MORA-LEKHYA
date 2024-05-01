inputfile='npy.wav'
outfile='npy.wav'
[y,fs]=audioread(inputfile);
reversedData=flipud(y);
audiowrite(outputfile,reversedData,fs);
disp('audio is reversed and successfully saved')




