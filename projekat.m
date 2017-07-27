[tm,sig]=rdsamp('mitdb/123',1);

signal=sig(1:3600);

slope=zeros(length(signal),1);

for i=3:length(signal)-2
    slope(i)= -2*signal(i-2)-signal(i-1)+signal(i+1)+2*signal(i+2);
end

maxi=0;

slope_tresh=(16/16)*maxi;

sloper=zeros(length(slope),1);

for i=1:length(slope)
    if (slope(i)>slope_tresh)
        maxi=((slope(i)-maxi)/16)+maxi;
        sloper(i)=slope(i);
    end
end

sloper2=zeros(length(sloper),1);

pt_tresh=0.1*slope_tresh;

for i=73:length(sloper2)-10
    if (sloper(i)>0.5 && sloper(i)>sloper(i-1) && sloper(i)>sloper(i+1)) %% 0.5mV je najmanja amplituda normalnog R
        j=i;
        m=j-72;

        for z=m:j
            if (sloper(z)>pt_tresh)
                sloper2(z)=sloper(z);
            end
        end
    end
end
            
p=zeros(length(sloper2),1);
koor=1:3600;

for i=1:length(p)
    if (sloper2(i)>0)
        p(i)=i;
    end
end

p(p==0)=[];

r=zeros(length(sloper2),1);

figure(2);
plot(sloper2);

kvad=sloper2.^4;

for i=3:length(kvad)-2
    if (kvad(i)>45 && kvad(i)>kvad(i+1) && kvad(i)>kvad(i-1) && kvad(i)>kvad(i+2) && kvad(i)>kvad(i-2))
        r(i)=i+4;
    end
end

r(r==0)=[];

figure(3);
plot(koor,signal(koor),r,signal(r),'o');



    





        
        
    


