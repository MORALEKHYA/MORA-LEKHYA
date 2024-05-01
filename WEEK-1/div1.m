clc 
clear all
close all
a=input("Enter a value:")
b=input("Enter b value:")
try   
  div=a/b
  disp(['result of division:',num2str(div)])
catch
  disp("Error:Enter either float integer value")
end_try_catch
