from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage html", pty=True)

#Windows käyttöön
def start_w(ctx):
    ctx.run("python3 src/index.py")

@task
def test_w(ctx):
    ctx.run("pytest src")

@task
def coverage_report_w(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

@task
def format_w(ctx):
    ctx.run("autopep8 --in-place --recursive src")
