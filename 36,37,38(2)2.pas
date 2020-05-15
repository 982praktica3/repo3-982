uses sistematest;

var
    a,b,ss,aa,chislo,k: integer;
    massiv: array [1..5] of integer;
    
function stepen(a,b,c: integer): integer;
var q,prom,z: integer;
begin
    prom:=1;
    q:=round(perevodv10(a,b));
    z:=c;
    z:=round(perevodv10(z,b));
    prom:=q;    
    writeln(q);
    for var i:=1 to z - 1 do
            prom:=ymnojenie(prom,q);
    stepen:=round(prom);
end;

begin
    write('Введите систему счисления: ');
    readln(ss);
    write('Введите число: ');
    readln(a);
    write('Введите степень: ');
    readln(b);
    aa:=stepen(a,ss,b);
    writeln(aa);
    writeln(perevod(aa,ss));
    write('Введите систему счисления: ');
    readln(ss);
    for var i:=1 to 5 do
        begin
          write('Введите число',i,': ');
            readln(chislo);
            massiv[i]:=chislo;
        end;
    writeln(massiv,' - Исходный массив');
    for var i:=1 to 5 do
            massiv[i]:=round(perevodv10(massiv[i],ss));
    writeln(massiv,' - Массив в 10 системе');
    for var i:=1 to 4 do
        begin
            for var j:=i+1 to 5 do
                begin
                    if bolshe(massiv[i],massiv[j]) then
                        begin
                            k:=massiv[i];
                            massiv[i]:=massiv[j];
                            massiv[j]:=k;
                        end;
                end;
        end;
    writeln(massiv,' - Отсортированный массив в 10');
    for var i:=1 to 5 do
        massiv[i]:=strtoint(perevod(massiv[i],ss));
    writeln(massiv,' - Отсортированный массив в ',ss);
end.