procedure TForm1.DETRMINISTIK1Click(Sender: TObject);
begin              {daun}
 xwmin := -3.5;
 xwmax := 3.5;
 ywmin := 0;
 ywmax := 11;
 xvmin := 0;
 xvmax := 350;
 yvmin := 10;
 yvmax := 560;
 canvas.BRUSH.Color := clwhite;
 canvas.Pen.Color := clwhite;
 canvas.rectangle(XVMIN,YVMIN,XVMAX+1,YVMAX+1);
 canvas.FloodFill(10,yvmax-10,clwhite,fssurface);

// 4 Transformasi Affine :
 a[1] := 0; 
 b[1] := 0; 
 c[1] := 0;
 d[1] := 0.2;
 e[1] := 0;
 f[1] := 0;
 a[2] :=  0.85 * cos(-2.5 * pi / 180);
 b[2] := -0.85 * sin(-2.5 * pi / 180);
 c[2] :=  0.85 * sin(-2.5 * pi / 180);
 d[2] :=  0.85 * cos(-2.5 * pi / 180);
 e[2] :=  0;
 f[2] :=  1.9;
 a[3] :=  0.3  * cos(50 * pi / 180); 
 b[3] := -0.34 * sin(50 * pi / 180);
 c[3] :=  0.3  * sin(50 * pi / 180);
 d[3] :=  0.34 * cos(40 * pi / 180);
 e[3] :=  0;
 f[3] :=  1.5;
 a[4] :=  0.3  * cos(-40 * pi / 180);
 b[4] := -0.34 * sin(-40 * pi / 180);
 c[4] :=  0.3  * sin(-40 * pi / 180);
 d[4] :=  0.34 * cos(-40 * pi / 180);
 e[4] :=  0;
 f[4] :=  1.2;
  
canvas.Pen.Color := clgreen;
  canvas.moveto(xvmax div 2,yvmin);
  canvas.LineTo(xvmax div 2,yvmax);
  k := 1;
  iterationNumber := 25;
  bm := tbitmap.create;
  bm.Width  := xvmax-xvmin;
  bm.Height := yvmax-yvmin;
  while k <= iterationNumber do begin
     bm.canvas.BRUSH.Color := clwhite;
     bm.canvas.Pen.Color := clwhite;
     bm.canvas.rectangle(0, 0, bm.WIDTH + 1, bm.HEIGHT + 1);
     for i := xvmin to xvmax do
       for j := yvmin to yvmax do begin
        if canvas.pixels[i,j] <> clwhite then begin
          VW(i, j, x, y);
          xb := a[1] * x + b[1] * y + e[1];
          yb := c[1] * x + d[1] * y + f[1];
          WV(XB,YB,XI,YI);  
          bm.canvas.Pixels[xI,yI] := clgreen;
          xb := a[2] * x + b[2] * y + e[2];    
          yb := c[2] * x + d[2] * y + f[2];
          WV(XB,YB,XI,YI); 
          bm.canvas.Pixels[xI,yI] := clgreen;
          xb := a[3] * x + b[3] * y + e[3];    
          yb := c[3] * x + d[3] * y + f[3];
          WV(XB,YB,XI,YI); 
          bm.canvas.Pixels[xI,yI] := clgreen;
          xb := a[4] * x + b[4] * y + e[4];    
          yb := c[4] * x + d[4] * y + f[4];
          WV(XB,YB,XI,YI); 
          bm.canvas.Pixels[xI,yI] := clgreen;
       end;
     end;
     CANVAS.CopyRect(RECT(xvmin,yvmin,xvmax+1,yvmax+1), 
                    bm.CANVAS,RECT(xvmin,yvmin,xvmax+1,yvmax+1));
     k:=k+1;
  end;
end;

{ end of section }

procedure TForm1.Pohon2(Sender: TObject);
VAR alpa, beta, gama, i, j, xi, yi : integer; x, y, xb, yb : real; bm : Tbitmap;
begin     
  
  {seting window dan viewport}
  xwmin := -3; xwmax :=   3; ywmin := 0; ywmax := 7;
  xvmin :=  0; xvmax := 600; yvmin := 0; yvmax := 700;
  
  {4 transformasi Affine }
  alpa :=   5; 
  beta := -50; 
  gama :=  40;  //silahkan diubah-ubah sudutnya
  
  a[1] :=    0;
  b[1] :=    0;
  c[1] :=    0;
  d[1] := 0.37;
  e[1] :=    0;
  f[1] :=    0;
  
  a[2] :=  0.65 * cos(alpa * pi / 180);  
  b[2] := -0.65 * sin(alpa * pi / 180);
  c[2] :=  0.65 * sin(alpa * pi / 180);  
  d[2] :=  0.65 * cos(alpa * pi / 180);  
  e[2] :=  0;  
  f[2] :=  2.5;
  
  a[3] :=  0.5 * cos(beta * pi / 180);  
  b[3] := -0.5 * sin(beta * pi / 180);
  c[3] :=  0.5 * sin(beta * pi / 180);  
  d[3] :=  0.5 * cos(beta * pi / 180); 
  e[3] :=  0;  
  f[3] :=  1.5;

  a[4] :=  0.5 * cos(gama * pi / 180);  
  b[4] := -0.5 * sin(gama * pi / 180);
  c[4] :=  0.5 * sin(gama * pi / 180);  
  d[4] :=  0.5 * cos(gama * pi / 180); 
  e[4] :=  0;  
  f[4] :=  1.7;

 {memberi warna latarbelakang PUTIH }
 canvas.BRUSH.Color := clwhite; canvas.Pen.Color := clwhite;
 canvas.rectangle(XVMIN,YVMIN,XVMAX,YVMAX);
 canvas.FloodFill(100,100,clwhite,fssurface);

{membuat gambar awal lingkaran hitam...bisa diganti lainnya}
 canvas.Pen.Color := clblack;  
 canvas.Ellipse(100,100,400,500);

{menyiapkan variabel bitmap bm}
 bm := tbitmap.create;  bm.Width := xvmax - xvmin;
 bm.Height := yvmax - yvmin;
iterationNumber := 8; //banyaknya iterasi
k := 0;
while k <= iterationNumber do begin
     {memberi warna latarbelakang PUTIH pada bm}
     bm.canvas.BRUSH.Color := clwhite;
     bm.canvas.Pen.Color := clwhite;
     bm.canvas.rectangle(0, 0, BM.Width, BM.Height);
     for i := xvmin to xvmax-1 do begin
       for j := yvmin to yvmax-1 do begin
          if canvas.pixels[i,j] <> CLwhite then begin
             VW(i,j,x,y);
             xb := a[1] * x + b[1] * y + e[1];
             yb := c[1] * x + d[1] * y + f[1];
             WV(xb,yb,xi,yi);
             bm.canvas.Pixels[xi,yi] := RGB(128,128,0); //Warna coklat untuk T1 ...batang pohon
             xb := a[2] * x + b[2] * y + e[2];
             yb := c[2] * x + d[2] * y + f[2];
             WV(xb,yb,xi,yi);
             bm.canvas.Pixels[xi,yi] := CLgreen;
             xb := a[3] * x + b[3] * y + e[3];
             yb := c[3] * x + d[3] * y + f[3];
             WV(xb,yb,xi,yi);
             bm.canvas.Pixels[xi,yi] := CLgreen;
             xb := a[4] * x + b[4] * y + e[4];
             yb := c[4] * x + d[4] * y + f[4];
             WV(xb,yb,xi,yi);
             bm.canvas.Pixels[xi,yi] := CLgreen;
          end;
      end;)

    {menampilkan gambar di bm ke layar...dengan copy/operasi move pada memori (RAM screen)}
      CANVAS.CopyRect(RECT(0,0,BM.Width,BM.Height), bm.CANVAS,RECT(0,0,BM.Width,BM.Height));
      k := k+1;
  end;
end;

{
    Transformasi Window toViewport dan sebaliknay:
}

procedure Tform1.WV(xw,yw:real;var xv,yv:integer);
begin
   xv := xvmin + round((xw - xwmin) * (xvmax - xvmin) / (xwmax - xwmin));
   yv := yvmax - round((yw - ywmin) * (yvmax - yvmin) / (ywmax - ywmin));
end;
procedure Tform1.VW(xv,yv:integer;var xw,yw:real);
begin
   xw := xwmin + (xv - xvmin) * (xwmax - xwmin) / (xvmax - xvmin);
   yw := ywmin + (yvmax - yv) * (ywmax - ywmin) / (yvmax - yvmin);
end;