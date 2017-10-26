% 测试生成体积力的子程序
%————————————————————————————————————————
clear all
close all
format long
clc

%等离子体激发器相关参数
lp = 100;
lt = 100;
a0 = 2;
a1 = 0.1;
a2 = 0.05;
b0 = 9;
b1 = 0.07;
b2 = 0.002;
c = 10000;
xp0 = 0;
% zp01 = 0;
% zp02 = 0.06;
% theta = 0;
theta = 0;
%计算网格参数
nx = 1;
ny = 110;
nz = 100;
%计算体积力
x  = linspace(0,1,nx);
y  = linspace(0,1,ny);
z  = linspace(0,2*pi,nz);
fx = zeros(nx,ny,nz);
fy = zeros(nx,ny,nz);
fz = zeros(nx,ny,nz);
for i = 1:nx
    for j = 1:ny
        for k = 1:nz
            [fx_temp,fy_temp,fz_temp] = plasma_Maden2013(x(i),y(j),z(k),a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,0,theta);
            fx(i,j,k) = fx(i,j,k) + fx_temp;
            fy(i,j,k) = fy(i,j,k) + fy_temp;
            fz(i,j,k) = fz(i,j,k) + fz_temp;
%             [fx_temp,fy_temp,fz_temp] = plasma_Maden2013(x(i),y(j),z(k),a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,0.06,theta);
%             fx(i,j,k) = fx(i,j,k) + fx_temp;
%             fy(i,j,k) = fy(i,j,k) + fy_temp;
%             fz(i,j,k) = fz(i,j,k) + fz_temp;
%             [fx_temp,fy_temp,fz_temp] = plasma_Maden2013(x(i),y(j),z(k),a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,0.12,theta);
%             fx(i,j,k) = fx(i,j,k) + fx_temp;
%             fy(i,j,k) = fy(i,j,k) + fy_temp;
%             fz(i,j,k) = fz(i,j,k) + fz_temp;
%             [fx_temp,fy_temp,fz_temp] = plasma_Maden2013(x(i),y(j),z(k),a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,0.18,theta);
%             fx(i,j,k) = fx(i,j,k) + fx_temp;
%             fy(i,j,k) = fy(i,j,k) + fy_temp;
%             fz(i,j,k) = fz(i,j,k) + fz_temp;
%             [fx_temp,fy_temp,fz_temp] = plasma_Maden2013(x(i),y(j),z(k),a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,-0.06,theta);
%             fx(i,j,k) = fx(i,j,k) + fx_temp;
%             fy(i,j,k) = fy(i,j,k) + fy_temp;
%             fz(i,j,k) = fz(i,j,k) + fz_temp;
%             [fx_temp,fy_temp,fz_temp] = plasma_Maden2013(x(i),y(j),z(k),a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,-0.12,theta);
%             fx(i,j,k) = fx(i,j,k) + fx_temp;
%             fy(i,j,k) = fy(i,j,k) + fy_temp;
%             fz(i,j,k) = fz(i,j,k) + fz_temp;
        end
    end
end





fid = fopen('test.dat','w');
fprintf(fid,'VARIABLES = X Y Z fx fy fz \n');
fprintf(fid,'ZONE T = TestPlasma F = POINT I = %d J= %d K = %d \n',nx,ny,nz);

for k = 1:nz
    for j = 1:ny
        for i = 1:nx
            fprintf(fid,'%20.13e %20.13e %20.13e %20.13e %20.13e %20.13e \n',x(i),y(j),z(k),fx(i,j,k),fy(i,j,k),fz(i,j,k));%
        end
    end
end

fclose(fid);