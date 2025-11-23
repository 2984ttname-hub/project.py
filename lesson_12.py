import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<.*?>', '', html, flags=re.DOTALL)

    lines = cleaned_text.splitlines()
    cleaned_lines = []
    for line in lines:
        if line.strip():
            cleaned_lines.append(line.strip())

    final_text = '\n'.join(cleaned_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)
