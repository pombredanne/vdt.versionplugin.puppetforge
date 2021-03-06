from setuptools import find_packages, setup

pkgname = "vdt.versionplugin.puppetforge"

setup(name=pkgname,
      version="0.2",
      description="Version Increment Plugin that builds a package from a puppet module from puppet forge",
      author="Lars van de Kerkhof",
      author_email="lars@permanentmarkers.nl",
      maintainer="Lars van de Kerkhof",
      maintainer_email="lars@permanentmarkers.nl",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['vdt', 'vdt.versionplugin'],
      zip_safe=True,
      install_requires=[
          "setuptools",
          "vdt.version",
          "vdt.versionplugin.default",
          "pyyaml",
      ],
      entry_points={},
)



