import nose.tools as n
import os

def test_has_data_submodule():
    'The sprint should have a submodule called "data".'
    n.assert_true(os.path.isdir('data'))
    n.assert_true(os.path.isfile(os.path.join('data', '.git')))

def test_python_init():
    'If there are any python files in the code directory, there should be an __init__.py'
    n.assert_true(os.path.isdir('code'))
    if filter(lambda filename: filename.endswith('.py'), os.listdir('code')):
        n.assert_true(os.path.isfile(os.path.join('code', '__init__.py')))

def test_python_files_correspond():
    '.py files in ``code`` should correspond with test files in ``test``'
    n.assert_true(os.path.isdir('code'))
    code_files = filter(lambda filename: filename.endswith('.py'), os.listdir('code'))
    test_files = filter(lambda filename: filename.startswith('test_') and filename.endswith('.py'), os.listdir('test'))
    n.assert_set_equal(set([test_file[5:] for test_file in test_files]), set(code_files))

def test_shell_files_correspond():
    '.sh files in ``code`` should correspond with test directories in ``test``'
    n.assert_true(os.path.isdir('code'))
    code_files = filter(lambda filename: filename.endswith('.sh'), os.listdir('code'))
    test_files = filter(lambda filename: (not filename.startswith('.')) and filename.endswith('.sh') and os.path.isdir(os.path.join('test', filename)), os.listdir('test'))
    n.assert_set_equal(set(test_files), set(code_files))

@n.nottest
def test_python_test_coverage():
    pass

@n.nottest
def test_shell_test_coverage():
    pass

def check_has_directory(dirname):
    n.assert_true(os.path.isfile(dirname))

def test_has_directories():
    for dirname in ['code', 'data', 'lib', 'test']:
        yield check_has_directory, dirname

def check_has_file(filename):
    n.assert_true(os.path.isfile(filename))

def test_has_files():
    for filename in ['readme.md', 'slides.md']:
        yield check_has_file, filename

def check_readme_has_section():
    raise NotImplementedError

def test_has_a_test():
    if os.path.isdir('test'):
        n.assert_true(len(os.listdir('test')) > 0)
    else:
        raise AssertionError('There is no test directory.')
