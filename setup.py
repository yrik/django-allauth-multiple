from setuptools import setup, find_packages


setup(
    name='django-allauth-multiple',
    version='0.01',
    author='Yuri Kriachko',
    author_email='iurii.kriachko@gmail.com',
    description=('Allauth with multiple usertypes'),
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-allauth',
    ],

)
