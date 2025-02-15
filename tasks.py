from pathlib import Path
import shutil

from docutils.core import publish_cmdline
from invoke import task
from rellu.tasks import clean
from robot.libdoc import libdoc


assert Path.cwd() == Path(__file__).parent


@task
def kw_docs(ctx):
    """Generates the library keyword documentation

    Documentation is generated by using the Libdoc tool.
    """
    libdoc(str(Path('CalculatorLibrary.py')),
           str(Path('docs/CalculatorLibrary.html')))


@task
def project_docs(ctx):
    """Generate project documentation.

     These docs are visible at http://robotframework.org/RobotDemo/.
     """
    args = ['--stylesheet=style.css,extra.css',
            '--link-stylesheet',
            'README.rst',
            'docs/index.html']
    publish_cmdline(writer_name='html5', argv=args)
    print(Path(args[-1]).absolute())


@task
def move_docs(ctx):
    """Move report.html and log.html to docs

    These docs are visible http://robotframework.org/RobotDemo/.
    """
    log = Path('./log.html')
    report = Path('./report.html')
    dest = Path('.') / 'docs'
    print(log.absolute())
    shutil.copy(log.absolute(), str(dest))
    print(report.absolute())
    shutil.copy(report.absolute(), str(dest))
# git push test
@task
def hook_test:
    pass
