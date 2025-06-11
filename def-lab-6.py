
def wrap_in_tag(tag, msg):
    result = f"<{tag}>{msg}<{tag}>"
    return result

print(wrap_in_tag("p", "hello"))
print(wrap_in_tag("b", "world"))