---
title: Jak odstranit otravnou reklamu na internetu
date: 2015-08-22
location: Plzeň
---

Poslední roky se stala reklama na internetu pěkně nenažranou a připravuje na
nás různé klikací pasti, nutí nás pustit si video reklamu před tím, než si
pustíme jinou reklamu na youtube, apod. Všimnul jsem si, že spousta lidí neví,
jak používat blokovače reklam, tak jsem sepsal malý návod, jak se zbavit
většiny otravných reklam na webu.

Dlouhodobým pomocníkem při jarním úklidu webu byl známý Adblock Plus, ale
poslední dobou začal žrát příliš
paměti[[1]](http://lifehacker.com/adblock-plus-once-again-found-to-dramatically-increase-1576341872)[[2]](http://lifehacker.com/ublock-is-a-fast-and-lightweight-alternative-to-adblock-1625246461)
a autor si začal nechal platit za odblokování vybraných
reklam[[3]](http://www.theverge.com/2015/2/2/7963577/google-ads-get-through-adblock).
Nikdo nemáme rádi korupci, proto na oba problémy přišla odpověď ve formě
moderního blokovoče - µBlock Origin. Autoři zdůrazňují, že to není jen pouhý
blokovač reklam, ale všeúčelový
blokovač[[4]](https://github.com/gorhill/uBlock) - reklamy, sledování identity
na webu, apod.


## 1. Nainstalování
Stáhněte si doplněk do prohlížeče.

* Chrome - [uBlock Origin - Chrome Web Store](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=cs)
* Firefox - [uBlock Origin :: Mozilla Add-ons](https://addons.mozilla.org/cs/firefox/addon/ublock-origin/)

Po nainstalování začne bez jakéhokoliv dalšího nastavování blokovat většinu
reklamy a špíny pocházející ze zahraničních serverů - např. youtube je od teď bez
reklam. Toho je dosaženo pomocí statických filtrů, které spravuje komunita.

<figure>
    <video autoplay loop>
        <source src="static/ublock1.mp4" />
    </video>
    <figcaption>Video 1. Nainstalování doplňku</figcaption>
</figure>

## 2. Odfiltrování dodatečných reklam z českých stránek
uBlock umožňuje vytvářet vlastní blokovací pravidla, čehož využijeme pro
vlastní filtraci bordelu, který nebyl doteď řádně podchycen. Zapneme pokročilý
mód, který nám umožní nastavování vlastních dynamických pravidel. Odfiltrujeme
všechny domény, které nesouvisí se stránkou, na které se právě nacházíme. 

<figure>
    <video autoplay loop>
        <source src="static/ublock2.mp4" />
    </video>
    <figcaption>Video 2. Povolení pokročilého módu</figcaption>
</figure>

Většina z nich jsou nějaké trackery, které sledují naši aktivitu na stránce,
servery ze kterých se tahá reklama, apod. Některé z nich jsou ale prvky, které
stránka vyžaduje - například fonty stažené z fonts.googleapis.com nebo obrázky
a skripty ze sítě pro doručování obsahu (content delivery network - cdn). Druhý
pozor budeme dávat při blokování facebooku, twitteru a jiných stránek, které
jinak používáme, ale nechceme, aby nás sledovaly na této stránce. uBlock
umožňuje blokovat tyhle případy pouze lokálně pro aktuální stránku. První
sloupec zablokuje domény **všude**. Sloupec vpravo od něj zablokuje doménu jen
na aktuální stránce. Pokud se chcete pošťourat v nastavení více detailu, pak
existuje podrobnější [návod jak na
to](https://github.com/gorhill/uBlock/wiki/Dynamic-filtering:-quick-guide).

<figure>
    <video autoplay loop>
        <source src="static/ublock3.mp4" />
    </video>
    <figcaption>Video 3. Dynamické blokování domén</figcaption>
</figure>


uBlock je příjemná věc tvořená lidmi pro lidi. Nezmínil jsem pokročilejší
funkce, jako například kosmetické filtrování - tj. odstranění konkrétních prvků
na stránce pomocí nástroje pipeta. Časem uvidíme, jestli uBlock nepotká stejný
osud jako Adblock Plus a nenahradí ho nová generace nezkorumpovaných blokovačů,
ale prozatím platí, že je to v téhle kategorii ten nejsilnější nástroj pro ty
nejsvalnatější a nejchlupatější chlapy.

