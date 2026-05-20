import streamlit as st

st.title("Krimidinner 🐮🔨")

eingabe_roh = st.text_input(
    "Lösung", value=None, placeholder="Hier Lösung eingeben",
    label_visibility="collapsed")

if st.button("Eingabe überprüfen"):
    eingabe = eingabe_roh.upper().strip()
    loesungen = [
        "GELB", "LÖWE", "SCHMIDT", "2005", "24", "DREISATZ", "883",
        "CLAUDIUS", "TIBERIUS", "NASENLOCH", "LOCKANGEBOT"]
    if eingabe in loesungen:
        st.success("Super, das ist richtig.", icon="😎", width=250)
        st.write("#### Hinweis:")
        if eingabe == loesungen[0]: # gelb
            st.write(
                """Warum hat eigentlich noch niemand den Gärtner unter Verdacht?
                Der ist doch immer der Übeltäter...""")
        elif eingabe == loesungen[1]: # Löwe
            st.write(
                """Ulrike ist eine Freundin von Marion aus Kindheitstagen.
                Sie ist sehr enttäuscht, dass sie nicht zu Marions 60. Geburtstag eingeladen
                wurde. So sehr, dass sie deshalb die Holzkuh zerstörte?""")
        elif eingabe == loesungen[2]: # Schmidt
            st.write(
                """Die Hunde sagen, sie waren das nicht mit der kaputten Kuh.
                Und sie wissen auch nicht, was mit der Salami passiert ist,
                die letzte Woche aus der Küche verschwunden ist...""")
        elif eingabe == loesungen[3]: # 2005
            st.write(
                """Bianca aus der Kirche hat Marion eine Vase für die Altardeko zu Christi Himmelfahrt
                verliehen. Leider ging die Vase beim Abschmücken des Altars kaputt.
                Hat sich Bianca etwa gerächt und im Gegenzug die Holzkuh beschädigt?""")
        elif eingabe == loesungen[4]: # 24
            st.write(
                """Franz-Hubertus hat seinen kürzlich erworbenen Gartenzwerg \"Titus\" genannt.
                Er steht künftig zwischen \"Claudius\" und \"Tiberius\".""")
        elif eingabe == loesungen[5]: # Dreisatz
            st.image("Mallorca-Status.png")
        elif eingabe == loesungen[6]: # 883
            st.write(
                """Tabea wurde am 1. Mai beim Ausführen auf die Sommerweide von einer Kuh verletzt.
                Ist sie deshalb aktuell womöglich nicht gut auf Kühe zu sprechen?
                Kamen beim Anblick der Holzkuh am Hof die Erinnerungen an den Unfall hoch,
                sodass sie die Kuh vorsätzlich zerstörte?""")
        elif eingabe in (loesungen[7], loesungen[8]): # Claudius / Tiberius
            st.image("Wetterbericht.png")
        elif eingabe == loesungen[9]: # Nasenloch (Hunde sortieren)
            st.write(
                """Franz-Hubertus hat Marion zu ihrem Geburtstag auch etwas geschenkt.
                Wie könnte es anders sein: einen wunderschönen Gartenzwerg.
                Leider ist der aber nicht in Marions WhatsApp-Status gelandet,
                sondern nur diese doofe Holzkuh...""")
        elif eingabe == loesungen[10]: # Lockangebot (Pferde sortieren)
            st.write(
                """Marion hat sich bei Bianca mehrfach für das Missgeschick entschuldigt und die Vase ersetzt.
                Bianca hat die Entschuldigung wohlwollend angenommen. Für sie ist damit alles in Ordnung.""")
    else:
        st.error("Schade, das ist nicht richtig.", icon="🙁")
