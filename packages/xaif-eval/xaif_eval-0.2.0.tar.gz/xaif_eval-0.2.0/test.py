from xaif_eval import AIF

aif = AIF("here is the text.")

speaker = "First Speaker"
text = "another text"
aif.add_component("locution", text, speaker)
aif.add_component("locution", "the third text. fourth text", "Second Speaker")
aif.add_component("segment", 2, ["the third text.", "fourth text"])
aif.add_component("proposition", 3, "the third text.")
aif.add_component("proposition", 4, "fourth text.")
aif.add_component("argument_relation", "RA", 5,7)


print(aif.xaif)

print(aif.get_csv("argument-relation"))