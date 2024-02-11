from ttl.ttl import TTL

ttl = TTL("templates")
ttl.process("index.ttl", "index.html")
