import streamlit as st


def create_homepage():
    """

    :param type:
    """
    st.title("BEVEZETŐ")
    st.markdown("""**Mi ez?**   Kíváncsi vagy, miből áll össze a főváros költségvetése? Honnan kapja és mire költi a pénzét az önkormányzat? Mi is kíváncsiak voltunk, ezért készítettünk egy gyűjtőoldalt,ahol interaktív adatvizualizációkat találsz. Ezek segítségével megismerheted a költségvetés szerkezetét és a részletek közötti összefüggéseket találhatsz. """)
    st.markdown("""Honnan van a fővárosnak pénze? Mennyi pénze van egyáltalán? Mi mindenre költi? Mi az, ami a legtöbb pénzébe kerül Budapestnek? Van-e elég pénze a fővárosnak?  Mik azok a területek, amik az utóbbi években pénzügyileg is kitüntetett figyelmet kaptak?""")
    st.markdown("""Találtál egy hibát? Kérdésed vagy észrevételed van? Írj nekünk: hello@email.hu""")
    st.markdown("""## Az adatokról""")
    # st.markdown("""#### Az adatok leírása""")
    st.markdown("""A 2017-es, 2018-as, 2019-es és 2020-as évi költségvetési számsorok a tényadatokat, a 2021-es évi számok pedig 2021. szeptemberi módosított előirányzatot mutatják.""")
    st.markdown("""Forrás: Budapest Főváros Önkormányzata""")
    st.markdown("""*Segítség a költségvetési fogalmak értelmezéséhez:*
    https://k-monitor.hu/cikkek/20190604-koltsegvetesi-abc-hallasd-a-hangod-a-helyi-penzugyekben""")
    st.markdown("""## Fogalommagyarázat""")
    st.markdown("""#### Bevételek""")
    st.markdown("""**Bevétel típusa:** a költségvetési bevétel az adott évben befolyó, tervezhető bevételeket 
    jelenti. A finanszírozási bevétel a korábbi évek megmaradt forrásainak felhasználása, vagy hitelből származó 
    bevételek felhasználása.""")
    st.markdown("""**Főbb bevételi kategória:** a bevétel típusa szerinti kategorizálás.""")
    st.markdown("""**Működési célú átvett pénzeszközök:** fenntartói visszatérítendő támogatás az intézmények részére (kölcsön), vagy az intézmények egymás közötti szolgáltatásainak elszámolása, pályázati támogatások.""")
    st.markdown("""**Működési célú támogatások államháztartáson belülről:** az önkormányzati feladatellátás támogatási a központi kormányzati költségvetésből - célzottan feladatokra vagy általánosan az önkormányzat működésére.""")
    st.markdown("""**Közhatalmi bevételek:** adóbevételek.""")
    st.markdown("""**Felhalmozási bevételek:** ingatlaneladásból vagy részesedés eladásából származó olyan bevételke, amelyeket felhalmozási céllal kell felhasználni.""")
    st.markdown("""**Felhalmozási célú átvett pénzeszközök:** felhalmozási célú kölcsön vagy támogatás.""")
    st.markdown("""**Felhalmozási célú támogatások államháztartáson belülről:** a központi költségvetésből célzottan egy projektre érkező támogatás (pl. Biodóm).""")
    st.markdown("""**Belföldi finanszírozás bevételei:** saját források - korábbi évek pénzmaradványai vagy hitelfelvételből származó pénzek.""")
    st.markdown("""**Külföldi finanszírozás bevételei:** külföldi hitelek felvétele""")
    st.markdown("""**Főbb bevételi kategória alkategóriái:** a főbb bevételi kategórián belüli, szűkített, de még mindig többelemű halmaz \n
**Megnevezés:** a konkrét bevétel megnevezése \n
**Forrás:** finanszírozó szerinti kategorizálás (állami, saját bevétel vagy saját korábbi forrás) \n
**Szervezeti egység típusai:** három szervezeti egység típus van:  
- **Fővárosi Önkormányzat:** ez a legnagyobb jogi személy, de nincs saját végrehajtó szervezete, hanem a Főpolgármesteri Hivatalon, a fővárosi fenntartású intézményeken és a fővárosi tulajdonú cégek közszoolgáltatásain keresztül látja el feladatait \n
- **Főpolgármesteri Hivatal:** a Fővárosi Önkormányzat végrehajtó szervezete, önálló jogi személy \n
- **Költségvetési intézmény:** a Fővárosi Önkormányzat által fenntartott intézmények: idősotthonok, hajléktalanellátó, múzeumok, könyvtár, önkormányzati rendészet, óvodák, művelődési házak \n
**Év:** Az adott bevétel beérkezésének éve \n
**Bevétel (ezer Ft) - nominál érték:** Az adott bevétel összege a tárgy évi folyóáron - ezer forintban \n
**Bevétel (ezer Ft) - reálérték:** Az adott bevétel összege inflációval korrigálva - ezer forintban \n
**Reálérték:**  (nominál érték / adott évi GDP deflátor) * 100
""")
    st.markdown("""#### Kiadások:""")
    st.markdown("""**Címkód:** a kifizetési jogcím egyedi azonosítója a költségvetésben és a könyvelésben \n
**Címkód megnevezése:** a kifizetés címzettje (intézmény, szervezet vagy feladat) vagy rövid megnevezése \n
**Ágazat:** szakterület \n
**Ágazat alábontás:** szakterületen belüli szervezeti egység vagy feladatcsoport \n
**Feladat megnevezése:** konkrét feladat \n
**Szervezeti egység típusai:** három szervezeti egység típus van:  
- **Fővárosi Önkormányzat:** ez a legnagyobb jogi személy, de nincs saját végrehajtó szervezete, hanem a Főpolgármesteri Hivatalon, a fővárosi fenntartású intézményeken és a fővárosi tulajdonú cégek közszoolgáltatásain keresztül látja el feladatait \n
- **Főpolgármesteri Hivatal:** a Fővárosi Önkormányzat végrehajtó szervezete, önálló jogi személy \n
- **Költségvetési intézmény:** a Fővárosi Önkormányzat által fenntartott intézmények: idősotthonok, hajléktalanellátó, múzeumok, könyvtár, önkormányzati rendészet, óvodák, művelődési házak \n
**Év:** az adott kiadás kifizetésének éve""")
    st.markdown("""**Kiadás (ezer Ft) - nominál érték:** az adott kiadás összege a tárgy évi folyóáron - ezer forintban \n
**Kiadás (ezer Ft) - reálérték:** Az adott kiadás összege inflációval korrigálva - ezer forintban \n
**Reálérték** = (nominál érték / adott évi GDP deflátor) * 100""")
