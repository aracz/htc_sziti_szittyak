import streamlit as st


def create_homepage():
    """

    :param type:
    """
    st.title("Bevezető")
    st.markdown("""#### **Mi ez?**""")
    st.markdown("""Kíváncsi vagy, miből áll össze a főváros költségvetése? Honnan kapja és mire költi a pénzét az önkormányzat? Mi is kíváncsiak voltunk, ezért készítettünk egy gyűjtőoldalt, ahol interaktív adatvizualizációkat és fogalommagyarázatokat találsz. """)
    st.markdown("""A vizualizációk segítségével megismerheted és megértheted a költségvetés fogalmait és szerkezetét és a kérdéseidre válaszokat találhatsz a részletek közötti összefüggések feltérképezésével.""")
    st.markdown("""*Honnan van a fővárosnak pénze? Mennyi pénze van egyáltalán? Mi mindenre költi? Mi az, ami a legtöbb pénzébe kerül Budapestnek? Van-e elég pénze a fővárosnak?  Mik azok a területek, amik az utóbbi években pénzügyileg is kitüntetett figyelmet kaptak?*""")
    st.markdown("""Csak néhány kérdés a sokból, amire ezen a portálon választ találhatsz.""")

    st.markdown("""#### **Hogy működik? Mit hol találok?**""")

    st.markdown("""A BEVEZETŐ a portált mutatja be, a második részében pedig a költségvetési fogalmak magyarázatát tartalmazza.""")
    st.markdown("""Az ÁTTEKINTÉS egy nagyobb grafikon segítségével mutatja meg a költségvetés szerkezetét, a pénzek áramlását a bevételek és a kiadások között.""")
    st.markdown("""Az ÖSSZEHASONLÍTÁS a bevételek és a kiadások részletesebb bontásban és az egyes évek között történő összehasonlítását teszi lehetővé. Az egyes kategóriák bontása, az összehasonlítandó évek és így az adatvizualizációk tartalma legördülő menüből választhatóak. Ezt a részt szántuk arra, hogy az érdeklődők maguk keressenek válaszokat a kérdéseikre. """)
    st.markdown("""A MOZGÁSTÉR című részt inspirációnak szántuk, ahol egy saját felfedezést akartunk megosztani, amit az adatok értelmezése közben, az egyik előzetes kérdésünkre válaszként találtunk.""")

    st.markdown("""#### **Kik vagyunk?**""")
    st.markdown("""A Hack the City hackathonon résztvevő csapat, a Sziti Szittyák: Balogh Kitti, Rácz Anna, Kocsis Krisztina, Horváth Tamás""")
    st.markdown("""Találtál egy hibát? Kérdésed vagy észrevételed van? Írj nekünk: teamszitiszittyak@gmail.com""")

    st.markdown("""#### **Mit érdemes tudni az adatokról?**""")

    st.markdown("""A 2017-es, 2018-as, 2019-es és 2020-as évi költségvetési számsorok a tényadatokat, a 2021-es évi számok pedig 2021. szeptemberi módosított előirányzatot mutatják.""")
    st.markdown("""A számok ezer forintban értendők.""")
    st.markdown("""Forrás: Budapest Főváros Önkormányzata""")

    st.markdown("""#### **Mi micsoda?** - Részletes fogalommagyarázat""")
    st.markdown("""#### Bevételek""")
    st.markdown("""**Bevétel típusa:** a költségvetési bevétel az adott évben befolyó, tervezhető bevételeket 
    jelenti. A finanszírozási bevétel a korábbi évek megmaradt forrásainak felhasználása, vagy hitelből származó 
    bevételek felhasználása.""")
    st.markdown("""**Főbb bevételi kategória:** a bevétel típusa szerinti kategorizálás.""")
    st.markdown("""**Szervezeti egység típusai:** három szervezeti egység típus van:  
- **Fővárosi Önkormányzat:** ez a legnagyobb jogi személy, de nincs saját végrehajtó szervezete, hanem a Főpolgármesteri Hivatalon, a fővárosi fenntartású intézményeken és a fővárosi tulajdonú cégek közszoolgáltatásain keresztül látja el feladatait \n
- **Főpolgármesteri Hivatal:** a Fővárosi Önkormányzat végrehajtó szervezete, önálló jogi személy \n
- **Költségvetési intézmény:** a Fővárosi Önkormányzat által fenntartott intézmények: idősotthonok, hajléktalanellátó, múzeumok, könyvtár, önkormányzati rendészet, óvodák, művelődési házak \n
**Év:** Az adott bevétel beérkezésének éve \n
**Bevétel (ezer Ft) - reálérték:** Az adott bevétel összege inflációval korrigálva - ezer forintban \n
**Reálérték:**  (nominál érték / adott évi GDP deflátor) * 100
""")
    st.markdown("""#### Kiadások:""")
    st.markdown("""**Címkód:** a kifizetési jogcím egyedi azonosítója a költségvetésben és a könyvelésben \n
**Címkód megnevezése:** a kifizetés címzettje (intézmény, szervezet vagy feladat) vagy rövid megnevezése \n
**Ágazat:** szakterület \n
**Szervezeti egység típusai:** három szervezeti egység típus van:  
- **Fővárosi Önkormányzat:** ez a legnagyobb jogi személy, de nincs saját végrehajtó szervezete, hanem a Főpolgármesteri Hivatalon, a fővárosi fenntartású intézményeken és a fővárosi tulajdonú cégek közszoolgáltatásain keresztül látja el feladatait \n
- **Főpolgármesteri Hivatal:** a Fővárosi Önkormányzat végrehajtó szervezete, önálló jogi személy \n
- **Költségvetési intézmény:** a Fővárosi Önkormányzat által fenntartott intézmények: idősotthonok, hajléktalanellátó, múzeumok, könyvtár, önkormányzati rendészet, óvodák, művelődési házak \n
**Év:** az adott kiadás kifizetésének éve""")
    st.markdown("""**Kiadás (ezer Ft) - reálérték:** Az adott kiadás összege inflációval korrigálva - ezer forintban \n
**Reálérték** = (nominál érték / adott évi GDP deflátor) * 100""")


    st.markdown("""*Segítség a költségvetési fogalmak értelmezéséhez:*
    https://k-monitor.hu/cikkek/20190604-koltsegvetesi-abc-hallasd-a-hangod-a-helyi-penzugyekben""")