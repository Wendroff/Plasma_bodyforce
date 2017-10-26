function [fx,fy,fz] = plasma_Maden2013(x1,y,z1,a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,yp0,zp0,theta)
    %检查输入参数是否正确
    if ( (a0<0) || (b0<0) || (lp<0) || (lt<0) || (c<0))
        error('incorrect input among a0 b0 c lp lt')
    end
    %将坐标转换到等离子体激发器坐标系中
    x = -(x1 - xp0) * sin(theta)  +  (z1 - zp0) * cos(theta);
    z =  (x1 - xp0) * cos(theta)  +  (z1 - zp0) * sin(theta);
    %计算x方向体积力分布
    if (x>0)
        X = (a1*x + a2*x^2) * exp(-a0*x);
    else
        X = 0;
    end
    %计算y方向体积力分布
    if ((y-yp0)>=0)
        Y = (b1*(y-yp0) + b2*(y-yp0)^2) * exp(-b0*(y-yp0)^0.4);
    else
        error('incorrect y : y < 0')
    end
    %计算z方向体积力分布
    if (z > lp/2 + lt)
        Z = 0;
    elseif (z > lp/2)
        Z = (-z + lt + lp/2)/lt;
    elseif (z > -lp/2)
        Z = 1;
    elseif (z > -lp/2 - lt)
        Z = (z + lt + lp/2)/lt;
    else
        Z = 0;
    end
    %计算体积力的绝对值
    f = c*X*Y*Z;
    %计算体积力分量
    fx = -f*sin(theta);
    fz =  f*cos(theta);
    fy =  0;
    
    




end