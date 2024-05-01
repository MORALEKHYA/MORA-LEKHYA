clc
clear all
close all
a=[1,2,3]
b=[4,5,6]
sum=0
for i=1:length(a)
    sum=sum+a(i).*b(i)
endfor
  disp(['dot product of two lists',num2str(sum)])
