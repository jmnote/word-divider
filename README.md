# word-divider

```
C:\word-divider-master>chcp 65001
Active code page: 65001

C:\word-divider-master>type 1.txt
안녕하세요           그곳에서 봐요.
반갑습니다 아아아
이런게 있습니다.
A이라는게 B라고 보면 된다.

C:\word-divider-master>python go.py 1.txt 2.txt
input file: 1.txt
output file: 2.txt
==================================
>>> 안녕하세요           그곳에서 봐요.
 ==> 안녕하세요 그 곳에서 봐요.
>>> 반갑습니다 아아아
 ==> 반갑습니다 아아아
>>> 이런게 있습니다.
 ==> 이런 게 있습니다.
>>> A이라는게 B라고 보면 된다.
 ==> A이라는 게 B라고 보면 된다.
=> Done...


C:\word-divider-master>type 2.txt
안녕하세요 그 곳에서 봐요.
반갑습니다 아아아
이런 게 있습니다.
A이라는 게 B라고 보면 된다.
```
