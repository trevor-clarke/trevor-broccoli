from ttl.ttl import TTL

ttl = TTL("templates")
# ttl.process("index.ttl", "html/index.html")
# ttl.process("career.ttl", "html/career.html")
ttl.process("testing.ttl", "html/testing.html")
