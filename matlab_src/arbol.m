fprintf("PROGRAM MAAAAAAN");

fileID = fopen("post-operative.data");
%uiimport("post-operative.data")
m = width(postoperative);
X = postoperative(:, m);
Classes = table2array(unique(X));
HT = 0;
ItClassesAll = table2array(X);
CountAll = length(ItClassesAll);
CountCat = countcats(ItClassesAll);

for k = 1:length(Classes)
    if(CountCat(k) == 0 || CountCat(k) == CountAll)
        HT= HT+0;
    else
    div = (CountCat(k)/CountAll);
    HT= HT -div*log2(div);
    end
end
Ha = size(m-1); 
for i = 1:m-1
    AttrX = postoperative(:, i);
    AttrClasses = table2array(unique(AttrX));
    TempHa = 0;
    AttrClassesAll = table2array(AttrX);
    AttrCountAll = length(AttrClassesAll);
    AttrCountCat = countcats(AttrClassesAll);
    TempArrayHa = size(length(AttrClasses)+1);
    for k = 1:length(AttrClasses)%Falta un loop dentro
        if(AttrCountCat(k) == 0 || AttrCountCat(k) == AttrCountAll)
            TempHa= TempHa+0;
        else
        div = (AttrCountCat(k)/AttrCountAll);
        TempHa= TempHa -div*log2(div);
        end
        TempArrayHa(k) = TempHa;
    end
    Ha(i) = TempArrayHa;
end