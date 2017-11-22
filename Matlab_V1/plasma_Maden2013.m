function [fx,fy,fz] = plasma_Maden2013(x1,y,z1,a0,a1,a2,b0,b1,b2,c,lp,lt,xp0,yp0,zp0,theta)
    %�����������Ƿ���ȷ
    if ( (a0<0) || (b0<0) || (lp<0) || (lt<0) || (c<0))
        error('incorrect input among a0 b0 c lp lt')
    end
    %������ת�����������弤��������ϵ��
    x = -(x1 - xp0) * sin(theta)  +  (z1 - zp0) * cos(theta);
    z =  (x1 - xp0) * cos(theta)  +  (z1 - zp0) * sin(theta);
    %����x����������ֲ�
    if (x>0)
        X = (a1*x + a2*x^2) * exp(-a0*x);
    else
        X = 0;
    end
    %����y����������ֲ�
    if ((y-yp0)>=0)
        Y = (b1*(y-yp0) + b2*(y-yp0)^2) * exp(-b0*(y-yp0)^0.4);
    else
        error('incorrect y : y < 0')
    end
    %����z����������ֲ�
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
    %����������ľ���ֵ
    f = c*X*Y*Z;
    %�������������
    fx = -f*sin(theta);
    fz =  f*cos(theta);
    fy =  0;
    
    




end