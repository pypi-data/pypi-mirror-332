from setuptools import setup, find_packages

setup(
    name='mkdocs-tccp-docs-styles',
    version='0.1.0',
    description='MkDocs plugin for TCCP documentation styles',
    author='Jeff Bendixsen',
    author_email='jeff_bendixsen@trimble.com',
    license='MIT',
    license_files=['LICENSE'],
    packages=find_packages(),
    include_package_data=True,
    package_data={'mkdocs_tccp_docs_styles': ['styles/*.css']},
    install_requires=['mkdocs>=1.0.0'],
    entry_points={
        'mkdocs.plugins': [
            'tccp-docs-styles = mkdocs_tccp_docs_styles:TCCPDocsStylesPlugin',
        ]
    }
)
