# POC for Using Molecule

## To install Molecule:
Need to use PIP to install
```bash
$ pip install molecule
```

Need to set some vars for language coding:
```bash
export LC_ALL=en_GB.UTF-8
export LANG=en_GB.UTF-8
```

## Using Molecule

To create Molecule role, remember Molecule is TDD (test first, then code):
```bash
$ molecule init role -r [rolename] -d [docker]
```

Going into the [rolename] directory, we can test that everything is working with:
```bash
$ molecule test
```

This should run through the default skeleton, creating the docker image and running the default task (which is to check that the root user is present).

Molecule creates the folder structure for the role and add a molecule directory containing stubs for the tests.

Tests are in _./molecule/default/tests/test_default.py_

This is a python file, so you write your assertions here, then its a case of writing the ansible to make the tests you've written work.

And then you have working and tested ansible code.

To create the tests use the docs here to see what you can do: [testinfra](https://testinfra.readthedocs.io/en/latest/)

Note: The default image is centos 7, but this seems to cause issues with Docker and Ansible that mean that Ansible can't work out if something is running or not.

## This example

Here we are doing a simple install of nginx and checking that its running with the following in _test_defualt.py_

```python
 assert host.package("nginx").is_installed
 assert host.service("nginx").is_running
```

I've added the main task for installing and a handler to check its started up.

If you need to debug the ansible you can use the debug flag:
```bash
$ molecule --debug test
```
