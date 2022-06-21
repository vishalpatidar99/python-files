import textwrap
string, max_width = input(), int(input())
print("\n".join(textwrap.wrap(string, max_width)))