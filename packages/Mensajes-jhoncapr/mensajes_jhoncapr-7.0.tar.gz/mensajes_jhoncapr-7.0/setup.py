from setuptools import setup, find_packages

setup(
    name='Mensajes-jhoncapr', #recomendable que el nombre sea unico para que al publicarlo no hayan problemas
    version=7.0,
    description='Un paquete para saludar y despedirse',
    long_description=open('readme.md').read(), #importarlo de forma dinamica
    long_description_content_type='text/markdown', #especificar el tipo para markdow 
    author='El bebecito programados',
    author_email='bebecito@gmail.com',
    url='https://www.google.com',
    license_File=['LICENSE'], #licencia particular
    packages=find_packages(),
    scripts=[],
    test_suite='tests', #nombre del folder donde estan las pruebas, Pero se debe incluir como paquete para que funcione
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],#para instalar los paquetes se hace como ↑. Importante para automatizar
    
    #creacion de las categorias donde se quiere publicar nuestro paquete
    classifiers=[
        'Environment :: Console',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft',
    ],
)                   
