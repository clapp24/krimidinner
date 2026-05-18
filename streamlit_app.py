import streamlit as st

st.title("Krimidinner 🐮🔨")

eingabe_roh = st.text_input(
    "Lösung", value=None, placeholder="Hier Lösung eingeben",
    label_visibility="collapsed")

if st.button("Eingabe überprüfen"):
    eingabe = eingabe_roh.upper().strip()
    loesungen = ["KUH", "1234", "TAXI", "BLUB", "BLA", "LOESUNG", "FAIL"]
    if eingabe in loesungen:
        st.success("Super, das ist richtig.", icon="😎", width=250)
        st.write("Hinweis:")
        if eingabe == loesungen[0]:
            st.write(
                """Tabea wurde am 1. Mai beim Weidegang von einer Kuh verletzt.
                Ist sie deshalb aktuell wohlmöglich nicht gut auf Kühe zu sprechen?
                Kamen beim Anblick der Holzkuh am Hof die Erinnerungen an den Unfall hoch,
                sodass sie die Kuh vorsätzlich zerstörte?""")
        elif eingabe == loesungen[1]:
            st.write(
                """Franz-Hubertus hat Marion zu ihrem Geburtstag auch etwas geschenkt.
                Wie könnte es anders sein: einen wunderschönen Gartenzwerg.""")
        elif eingabe == loesungen[2]:
            st.write(
                """Ulrike ist eine Freundin von Marion aus Kindheitstagen.
                Sie ist sehr enttäuscht, dass sie nicht zu Marions 60. Geburtstag eingeladen
                wurde. So sehr, dass sie deshalb die Holzkuh zerstörte?""")
        elif eingabe == loesungen[3]:
            pass
            # WhatsApp-Bild: Ulrike auf Mallorca
            # We
            #st.write(
            #    """Ulrike macht seit einer Woche Urlaub auf Mallorca""")
    else:
        st.error("Schade, das ist nicht richtig.", icon="🙁")
