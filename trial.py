from main import BlogPost, db


puclications = {}
data = db.session.query(BlogPost).all()
n = 0
for d in data:
    puclications[n] = [d.name, d.link]
    n += 1

print(puclications)
for n, m in puclications.items():
    print(n)
    print(m)