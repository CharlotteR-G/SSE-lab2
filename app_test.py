from app import process_query


def test_knows_about_dinosaurs():
    expected = "Dinosaurs ruled the Earth 200 million years ago"
    assert (
        process_query("dinosaurs") == expected
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"

def test_knows_name_returns_name():
    assert process_query("What is your name?") == "Team_Won"