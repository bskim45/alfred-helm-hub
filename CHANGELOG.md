# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [2.0.0](https://github.com/bskim45/alfred-helm-hub/compare/1.3.0...2.0.0) (2022-05-08)

### Breaking changes

Python 2 has been removed from macOS 12.3 Monterey,
and default system Python is now Python 3.8.
(https://www.alfredapp.com/help/kb/python-2-monterey/)

This is first version that supports macOS 12.3+ (Python 3.8+).

Please note that **Python 2 and Alfred 3 is no longer supported.**
If you are using macOS 12.2 or below, please do not upgrade to 2.0.0+
and keep using 1.3.0.

Special thanks to @NorthIsUp for porting [alfred-workflow](https://github.com/NorthIsUp/alfred-workflow-py3) to Python 3.

### Features

* support python3 (macOS 12.3+) ([ef9f083](https://github.com/bskim45/alfred-helm-hub/commit/ef9f083a625d24fc9853c850a6dc804e06185570))


## v1.3.0 (2021-06-16)

### Changelog
- Fix `artifacthub.io` search (api changes in `artifacthub.io`)


## v1.2.0 (2021-03-22)

### Breaking Changes

[Jfrog is sunsetting Bintray, JCenter, GoCenter, and ChartCenter](https://jfrog.com/center-sunset/).
`chartcenter.io` is now disabled by default, and also disabled automatically upon version upgrade.
Support for `hub.helm.sh` and `chartcenter.io` will be removed in next release.

### Changelog
- Disable `chartcenter.io` by default, and also disabled automatically upon version upgrade.


## v1.1.0 (2020-10-12)

### Breaking Changes

`hub.helm.sh` is no longer enabled by default, in flavor of `artifacthub.io`.
You still can enable/disable individual hub repo by hub repo command.
Users upgrading from previous version is not affected. (`artifacthub.io` is enabled by default)

### Changelog
- Added support for `artifacthub.io`
- `hub.helm.sh` is disabled by default, in flavor of `artifacthub.io`.


## v1.0.0 (2020-10-02)

initial release
