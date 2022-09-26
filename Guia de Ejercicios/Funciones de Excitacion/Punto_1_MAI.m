syms s;


C1 = 1/5;
L1=1;
C2=8/45;
L2=9/16;
C3=8/27;
L3=27/16;

Y1=1/(s*L1+1/(s*C1));
Y2=s*C2+1/(s*L2);
Y3=s*C3+1/(s*L3);

YMAI = [Y1, -Y1, 0, 0;-Y1, Y1+Y2, -Y2, 0;0,-Y2,Y2+Y3,-Y3;0,0,-Y3,Y3];



Y03_03 = det(YMAI(2:3,2:3));
Y3_3 = det(YMAI(1:3,1:3));
Z = Y03_03/Y3_3;

[symNum,symDen] = numden(Z); %Get num and den of Symbolic TF
TFnum = sym2poly(symNum);    %Convert Symbolic num to polynomial
TFden = sym2poly(symDen);    %Convert Symbolic den to polynomial
Z =tf(TFnum,TFden);

zpk(Z)