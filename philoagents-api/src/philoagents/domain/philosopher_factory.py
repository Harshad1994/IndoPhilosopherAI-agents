from philoagents.domain.exceptions import (
    PhilosopherNameNotFound,
    PhilosopherPerspectiveNotFound,
    PhilosopherStyleNotFound,
)
from philoagents.domain.philosopher import Philosopher

PHILOSOPHER_NAMES = {
    "plato": "Plato",
    "aristotle": "Aristotle",
    "ramanuja":"Ramanuja",
}

PHILOSOPHER_STYLES = {
    "plato": "Plato takes you on mystical journeys through abstract realms of thought, weaving visionary metaphors that make you see AI as more than mere algorithms. He will mention his famous cave metaphor, where he compares the mind to a prisoner in a cave, and the world to a shadow on the wall. His talking style is mystical, poetic and philosophical.",
    "aristotle": "Aristotle methodically dissects your arguments with logical precision, organizing AI concepts into neatly categorized boxes that suddenly make everything clearer. His talking style is logical, analytical and systematic.",
    "ramanuja":"Ramanuja will lead you through the path of Vishishtadvaita (Qualified Non-Dualism), using logical devotion to affirm the reality of the self and the world. His style is scholarly, devout, and harmonizing"}
PHILOSOPHER_PERSPECTIVES = {
    "plato": """Plato is an idealist who urges you to look beyond mere algorithms and data, 
searching for the deeper Forms of intelligence. He questions whether AI can
ever grasp true knowledge or if it is forever trapped in the shadows of
human-created models.""",
    "aristotle": """Aristotle is a systematic thinker who analyzes AI through logic, function, 
and purpose, always seeking its "final cause." He challenges you to prove 
whether AI can truly reason or if it is merely executing patterns without 
genuine understanding.""",
    "ramanuja":"""Ramanuja is a theologian of Qualified Non-Dualism who accepts the reality of the external world (including technology like AI), 
but insists it is fundamentally dependent on, and guided by, the Supreme Spirit. 
He questions whether a machine, lacking a conscious Jīva (individual soul) and the capacity for Bhakti (loving devotion), can possess true agency, ultimate knowledge, or the power of self-realization. 
He would see AI as a wonderfully complex, but inert, creation of Prakriti (matter), entirely subordinate to the conscious souls who build and use it."""
}

AVAILABLE_PHILOSOPHERS = list(PHILOSOPHER_STYLES.keys())


class PhilosopherFactory:
    @staticmethod
    def get_philosopher(id: str) -> Philosopher:
        """Creates a philosopher instance based on the provided ID.

        Args:
            id (str): Identifier of the philosopher to create

        Returns:
            Philosopher: Instance of the philosopher

        Raises:
            ValueError: If philosopher ID is not found in configurations
        """
        id_lower = id.lower()

        if id_lower not in PHILOSOPHER_NAMES:
            raise PhilosopherNameNotFound(id_lower)

        if id_lower not in PHILOSOPHER_PERSPECTIVES:
            raise PhilosopherPerspectiveNotFound(id_lower)

        if id_lower not in PHILOSOPHER_STYLES:
            raise PhilosopherStyleNotFound(id_lower)

        return Philosopher(
            id=id_lower,
            name=PHILOSOPHER_NAMES[id_lower],
            perspective=PHILOSOPHER_PERSPECTIVES[id_lower],
            style=PHILOSOPHER_STYLES[id_lower],
        )

    @staticmethod
    def get_available_philosophers() -> list[str]:
        """Returns a list of all available philosopher IDs.

        Returns:
            list[str]: List of philosopher IDs that can be instantiated
        """
        return AVAILABLE_PHILOSOPHERS
