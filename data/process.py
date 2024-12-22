import re


def prepare_data():
    with open("kokoro_utf8.txt", "r") as file:
        text = file.read()

    processed = process_text(text)

    with open("kokoro.txt", "w") as outfile:
        outfile.write(processed)


def process_text(input):
    return remove_multi_newlines(remove_headings(remove_ruby(remove_ruby_marker(input))))


def remove_ruby_marker(input):
    return input.replace("｜", "")


def remove_ruby(input):
    pattern = r"《[^《》]+》"
    return re.sub(pattern, "", input)


def remove_headings(input):
    pattern = r"^.*［.+］.*\n"
    return re.sub(pattern, "", input, flags=re.MULTILINE)


def remove_multi_newlines(input):
    pattern = r"\n{2,}"
    return re.sub(pattern, "\n\n", input)


def test():
    text = """
    ［＃２字下げ］上　先生と私［＃「上　先生と私」は大見出し］


    ［＃５字下げ］一［＃「一」は中見出し］

    　私《わたくし》はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚《はば》かる遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執《と》っても心持は同じ事である。よそよそしい頭文字《かしらもじ》などはとても使う気にならない。
    """

    expected = """

    　私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚かる遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執っても心持は同じ事である。よそよそしい頭文字などはとても使う気にならない。
    """

    assert process_text(text) == expected


if __name__ == "__main__":
    prepare_data()
