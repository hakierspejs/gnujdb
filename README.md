# gnujdb

The goal of this project is to expose a central database of items collected in
Hackerspace Łódź. The project generates QR codes like this:

<img src="https://raw.githubusercontent.com/hakierspejs/gnujdb/master/example_qrcodes.png" height="200">

All of them point to https://g.hs-ldz.pl/ + some random suffix. Once you visit
the URL, you can see a website like this:

<img src="https://raw.githubusercontent.com/hakierspejs/gnujdb/master/example_form.png" height="400">

Here you can upload an image of the object you attached the sticker to, who
is the owner, on what terms the object can be used, how much it's worth and
any other extra information. The data can then be viewed and edited by anyone
who either has an access to the link or the sticker. If the sticker wears off,
the text below it says what should be entered after https://g.hs-ldz.pl/
prefix.

TODO: 
 - add description of project on HSL wiki https://github.com/hakierspejs/wiki/wiki
 - SSO login into django-admin
 - tesseract to parse text on images and add data to fts 
 - multiple images for item
 - images proxying + caching + cropping

No i w ogóle w bazie przydałyby się takie pola:
– właściciel (żeby móc identyfikować rzeczy niebędące własnością HS-u – tutaj przy porządkowaniu pewnie będzie sporo przypadków, gdzie nie będzie się go dało od razu ustalić, nie będzie pewności, czy coś jest np. spejsowe, czy przez kogoś przywleczone i nie traktowane przez tę osobę jako dar, czyli pewnie szczególnie na początku często będzie się pojawiać wartość “nieznany” – ale mimo wszystko to potrzebne pole)
– miejsce, do którego przynależy (tu przydałaby się relacja z tabelą przechowującą listę miejsc, żeby to był w miarę zamknięty katalog, oczywiście z możliwością rozszerzania, i żeby to samo miejsce nie występowało pod 20 różnymi nazwami)
– wpisywanie miejsca IMO powinno być wymuszone – inaczej nigdy tego porządku nie ogarniemy, a użyteczność tej bazy będzie znikoma,
– kategoria (tu fajnie by było mieć w ogóle taką wielopoziomową kategoryzację, coś jak w sklepach internetowych czy na Allegro… np. jakieś konkretne kombinerki mogą być w kategorii: Narzędzia → Ręczne → Szczypce → Kombinerki… ale jak to ma być za trudne w stworzeniu, to ostatecznie płaska lista kategorii lub mechanizm tagów też by dał radę)
– dodatkowy opis

AFAIK tam była też opcja drukowania labelek na naszej drukarce do etykiet – tutaj przydałaby się dodatkowo opcja, żeby wydrukowana labelka miała format chorągiewki – żeby można było w łatwy sposób używać też tego do kabli.

I jeszcze fajna by była opcja wiązania ze sobą poszczególnych artefaktów, tak by po otwarciu danej rzeczy wyświetlały się powiązane. Np. rzutnik – pilot do rzutnika.

