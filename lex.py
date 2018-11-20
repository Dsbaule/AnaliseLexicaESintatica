import TokenAFDs



afd = TokenAFDs.getStringAFD('(')

print(afd.accepts("(while)"))
print(afd.accepts("whitle"))
