import os
from flask_script import Manager, Shell, Command
from app import create_app

app = create_app()
app.config.from_object(os.environ.get('FLASK_CONFIG'))

manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()