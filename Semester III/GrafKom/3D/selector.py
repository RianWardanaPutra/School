a = "0  b -a    b  a  0   -b  a  0 \
 0  b  a   -b  a  0    b  a  0 \
 0  b  a    0 -b  a   -a  0  b \
 0  b  a    a  0  b    0 -b  a \
 0  b -a    0 -b -a    a  0 -b \
 0  b -a   -a  0 -b    0 -b -a \
 0 -b  a    b -a  0   -b -a  0 \
 0 -b -a   -b -a  0    b -a  0 \
-b  a  0   -a  0  b   -a  0 -b \
-b -a  0   -a  0 -b   -a  0  b \
 b  a  0    a  0 -b    a  0  b \
 b -a  0    a  0  b    a  0 -b \
 0  b  a   -a  0  b   -b  a  0 \
 0  b  a    b  a  0    a  0  b \
 0  b -a   -b  a  0   -a  0 -b \
 0  b -a    a  0 -b    b  a  0 \
 0 -b -a   -a  0 -b   -b -a  0 \
 0 -b -a    b -a  0    a  0 -b \
 0 -b  a   -b -a  0   -a  0  b \
 0 -b  a    a  0  b    b -a  0"
b = a.split(' ');
a = [x for x in b if x]
b = []
for i in a:
    try:
        b.append(int(i))
    except:
        b.append(i)
c = [tuple(b[i:i+3]) for i in range(0, len(b), 3)]

print(tuple(dict.fromkeys(c)))

