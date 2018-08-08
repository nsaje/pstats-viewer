# online pstats viewer

An online version of [Snakeviz](https://jiffyclub.github.io/snakeviz/).

Since Python profile files are just marshalled dictionaries and [Python documentation](https://docs.python.org/2/library/marshal.html) warns against unmarshaling data from an untrusted source,
the unmarshalling is performed in AWS Lambdas.

## Deploy

If you want to host your own,
- host the content of the `static` directory somewhere online
- set the `STATIC_URL` in `impl/main.py` to where you're hosting the static files
- install [Apex](http://apex.run/) and run `apex deploy`.
