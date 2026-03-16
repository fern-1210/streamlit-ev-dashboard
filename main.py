import random

import streamlit as st


# Predefined list of fun superhero catchphrases
CATCHPHRASES = [
    "To the skies and beyond!",
    "Justice never sleeps!",
    "In the name of truth and thunder!",
    "Where darkness falls, I rise!",
    "Evil beware, your days are numbered!",
    "From the shadows, I bring the light!",
    "Powered by courage, guided by hope!",
]


def main() -> None:
    st.set_page_config(page_title="Superhero Name Generator", page_icon="🦸")

    st.title("Superhero Name Generator")
    st.write("Create your own comic-book hero profile in seconds!")
    st.divider()

    st.subheader("Origin Story Inputs")
    st.write("Fill in the details below, then click **Generate Superhero** to reveal your hero.")

    col1, col2 = st.columns(2)

    with col1:
        color = st.text_input("Favorite color", placeholder="e.g., Crimson")
        lucky_number = st.number_input(
            "Lucky number",
            min_value=0,
            step=1,
            value=7,
            help="Pick any whole number. This will become part of your hero's legend.",
        )

    with col2:
        animal = st.text_input("Favorite animal", placeholder="e.g., Falcon")
        superpower = st.selectbox(
            "Choose your superpower",
            [
                "Flying",
                "Invisibility",
                "Super strength",
                "Telepathy",
                "Time control",
            ],
        )

    st.divider()

    generate_clicked = st.button("Generate Superhero", type="primary")

    if generate_clicked:
        if not color.strip() or not animal.strip():
            st.warning("Please enter both a favorite color and a favorite animal to forge your superhero identity.")
            return

        safe_color = color.strip().title()
        safe_animal = animal.strip().title()
        number_part = int(lucky_number)

        if number_part == 0:
            hero_name = f"{safe_color} {safe_animal} of Infinity"
        else:
            hero_name = f"{safe_color} {safe_animal} of {number_part}"

        motto = f"Guarding the world with {superpower.lower()}!"

        with st.container():
            st.subheader("Your Superhero Profile")
            st.markdown("---")
            st.markdown(f"## 🦸 {hero_name}")
            st.markdown(f"**Signature Power:** {superpower}")
            st.markdown(f"**Superhero Motto:** _{motto}_")

        st.markdown("---")

        if st.button("Generate Random Superhero Catchphrase"):
            phrase = random.choice(CATCHPHRASES)
            st.markdown(f"> \"{phrase}\"")


if __name__ == "__main__":
    main()

