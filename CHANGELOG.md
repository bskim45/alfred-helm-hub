# CHANGELOG

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
