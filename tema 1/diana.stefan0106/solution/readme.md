# TEMA 1 - ISC 2023
### Stefan Diana Maria - 332CC

## 1. CRYPTO ATTACK

Am decodat cele doua hinturi cu ***cifrul lui Caesar*** => ***`RSA chosen ciphertext attack`***

Am gasit link-ul urmator, pe care s-a bazat toata rezolvarea: https://crypto.stackexchange.com/questions/2323/how-does-a-chosen-plaintext-attack-on-rsa-work

Dupa ce am decodat in ***base64*** textul din fisierul `message.txt`, am obtinut un json ce contine *'e'*, *'n'* si *'flag'*.

Am creat mai departe un json care contine doar campul *'flag'*. Am inmultit textul criptat cu ***5^e mod n*** si am folosit rezultatul pentru a completa flag-ul.

Am dat ca input serverului noul json, pentru care am primit ca raspuns sirul decriptat, pe care l-am impartit la ***5*** pentru a obtine doar decriptarea flag-ului.

Flag-ul obtinut este: ***`SpeishFlag{ulT8bYRjg5qhr6UTHm0la8nEi0x3c2mQ}`***.

## 2. LINUX ACL

M-am conectat prin ***ssh*** cu cheia privata la `janitor@isc2023.1337.cx`, gasit in ***id_rsa.pub***.

Am intrat in ***/usr/local/bin***, cum e indicat in ***task.txt***.

`robot-sudo` are owner-ul `iamrobot` si grupul `superboss`.

Am identificat utilizatorii din sistem.

- `janitor-coffee.sh`: 
Apeleaza `robot-sudo` cu argumentele ***"make me a coffee"***.

- `janitor-vacuum.sh`: 
Daca nu se primesc argumente, executa `robot-sudo /usr/local/bin/vacuum-control "$@"`.

- `vacuum-control`: 
Daca user ID ul este mai mic decat ***7000***, nu se permite accesul. Daca este mai mare, se afiseaza `"Okay!"`.

> [!NOTE]
> User: `janitor:1000`
> 
> User: `superboss:9000`
> 
> User: `iamrobot:7619`

Am dat `strings robot-sudo` si am gasit: 

    /usr/lib/tar/gay/r0b0t3rs.conf
    Missing configuration file!

Am afisat continutul fisierului `r0b0t3rs.conf` si a aparut: 

    allow iamrobot /.you.are.never/.gonnafindthis/f1n4-b055 allow janitor /usr/local/bin/vacuum-control

In fisierul `f1n4-b055` am gasit: 

    10721525985ed26d31c825f32563ed54
    Access denied!
    I will contact you when I require your cleaning services, janitor!
    Congratulations, here's your flag:
    cat /etc/dir/ceva/.my.flag

=> ***10721525985ed26d31c825f32563ed54*** = argument pentru iamrobot

***/etc/dir/ceva/.my.flag*** nu poate fi accesat decat de root.
Nu se poate scrie in vacuum-control, deci am facut un nou script
(vacuum-control2), cu continutul: 
`/.you.are.never/.gonnafindthis/f1n4-b055 10721525985ed26d31c825f32563ed54`.

Dupa comanda `robot-sudo /usr/local/bin/vacuum-control2`, am obtinut flag-ul: ***`SpeishFlag{CNvBchcXoYWok5s9LB2pjyZkqnozAAoz}`***.

## 3. BINARY EXPLOIT

Am deschis fisierul executabil `casino` si m-am uitat cu ghidra in functia `loop`. 
Variabila `local_bc` este adresa unde se stocheaza numerele introduse.

- bc (hexa) -> 188 (dec)
- Numerele introduse sunt pe 4 bytes, deci 188 / 4 = ***47 numere***.

Am folosit comanda `nm casino` pentru a afla adresa functiei `win` pentru a putea face ***overflow***. Adresa este `0x08049170 -> 134517302 (dec)`.

Am rulat programul si, dupa ce am obtinut un `lucky number`, am introdus ***47 de numere***, iar la al 48-lea am pus adresa functiei `win`, inca ***un numar*** pentru a umple spatiul ramas (***EBP***) si apoi luckynumber-ul pentru argumentul functiei `win`.

Numerele introduse:

    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 134517302 1 82206

Am primit mesajul:

    File opening failed!
    Note: there is no flag available locally, try it on the remote server!

Am rulat programul pe server (`telnet isc2023.1337.cx 10083`) si am urmat aceiasi pasi si am primit flag-ul:
***`SpeishFlag{ZytH5tA9g6Ws9UKc9OYe0XkJnQjvw1iC}`***.
